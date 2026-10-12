import math
import numpy as np

def direct_feddyn(H, bs, x0, alpha, rounds):
    m, d = bs.shape
    x_server = x0.copy()
    g = np.zeros((m, d))
    clients = np.zeros((m, d))
    out = []
    for t in range(1, rounds + 1):
        new_clients = []
        for k in range(m):
            rhs = H @ bs[k] + g[k] + alpha * x_server
            uk = np.linalg.solve(H + alpha*np.eye(d), rhs)
            new_clients.append(uk)
        clients = np.array(new_clients)
        # Source gradient-state recursion; exact local optimality makes this
        # equal to the true local gradient after the first update.
        for k in range(m):
            g[k] = g[k] - alpha * (clients[k] - x_server)
            true_g = H @ (clients[k] - bs[k])
            assert np.linalg.norm(g[k] - true_g) < 2e-10
        gamma = clients.mean(axis=0)
        h = g.mean(axis=0)
        x_server = gamma - h/alpha
        out.append((clients.copy(), gamma.copy(), x_server.copy()))
    return out

rng = np.random.default_rng(350054)
for d in (2, 4, 6):
    for _ in range(8):
        Q, _ = np.linalg.qr(rng.normal(size=(d,d)))
        eig = np.linspace(0.7, 6.3, d)
        H = Q @ np.diag(eig) @ Q.T
        m = 5
        bs = rng.normal(size=(m,d))
        x0 = rng.normal(size=d)
        alpha = float(10**rng.uniform(-0.5, 1.0))
        xstar = bs.mean(axis=0)
        R = alpha * np.linalg.inv(H + alpha*np.eye(d))
        S = H @ np.linalg.inv(H + alpha*np.eye(d))
        direct = direct_feddyn(H, bs, x0, alpha, 6)
        for t, (clients, gamma, server) in enumerate(direct, start=1):
            gamma_formula = xstar + np.linalg.matrix_power(R,t) @ (x0-xstar)
            assert np.linalg.norm(gamma-gamma_formula) < 2e-9
            for k in range(m):
                dev_formula = np.linalg.matrix_power(S,t) @ (bs[k]-xstar)
                assert np.linalg.norm((clients[k]-gamma)-dev_formula) < 2e-9
            server_formula = xstar + (np.eye(d)-H/alpha) @ np.linalg.matrix_power(R,t) @ (x0-xstar)
            assert np.linalg.norm(server-server_formula) < 2e-9

# Endpoint operator factors and geometric-mean balance.
for mu, L in ((1.0,1.0),(1.0,4.0),(0.25,9.0),(2.0,18.0)):
    astar = math.sqrt(mu*L)
    r = astar/(astar+mu)
    s = L/(L+astar)
    target = math.sqrt(L/mu)/(1.0+math.sqrt(L/mu))
    assert abs(r-s) < 1e-14
    assert abs(r-target) < 1e-14
    # Nearby multiplicative perturbations are strictly worse when mu < L.
    if mu < L:
        for fac in (0.4,0.7,1.3,2.5):
            a = fac*astar
            rho = max(a/(a+mu), L/(L+a))
            assert rho > target

# Isotropic cancellation: the server is exactly at the global optimum
# after round one, while both exact channels halve per round.
a = 3.25
H = a*np.eye(3)
bs = np.array([[1.,2.,-1.],[-2.,1.,3.],[4.,-1.,0.]])
x0 = np.array([3.,-4.,2.])
xstar = bs.mean(axis=0)
direct = direct_feddyn(H,bs,x0,a,6)
for t,(clients,gamma,server) in enumerate(direct,start=1):
    assert np.linalg.norm(server-xstar) < 2e-12
    assert np.linalg.norm((gamma-xstar) - (0.5**t)*(x0-xstar)) < 2e-12
    for k in range(len(bs)):
        assert np.linalg.norm((clients[k]-gamma) - (0.5**t)*(bs[k]-xstar)) < 2e-12

print("verification passed")
