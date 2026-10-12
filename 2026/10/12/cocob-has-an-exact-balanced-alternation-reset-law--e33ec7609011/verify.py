import math
import random

EULER_GAMMA = 0.5772156649015328606

def a(n):
    return math.tanh(1.0/(2*n+1))

def replay(L, N):
    w1 = 0.0
    G = L
    reward = 0.0
    theta = 0.0
    w = w1
    iterates = [w1]
    states = []
    for t in range(1, 2*N+1):
        g = L if t % 2 else -L
        G += abs(g)
        reward += (w-w1)*g
        theta += g
        beta = math.tanh(theta/(G+L))/L
        w_next = w1 + beta*(L+reward)
        states.append((t, G, reward, theta, beta, w, w_next))
        w = w_next
        iterates.append(w)
    return states, iterates

def product_P(n):
    p = 1.0
    for k in range(1, n+1):
        p *= 1.0-a(k)
    return p

# Exact recurrence identities for varied scales.
for L in (0.03, 1.0, 7.5, 1000.0):
    states, it = replay(L, 100)
    P = 1.0
    for n in range(1, 101):
        an = a(n)
        prev = P
        P *= 1.0-an
        # w_{2n} is stored as iterate index 2n-1 in zero-based Python list
        w_2n = it[2*n-1]
        w_2n1 = it[2*n]
        assert abs(w_2n - an*prev) < 5e-13
        assert abs(w_2n - (prev-P)) < 5e-13
        assert abs(w_2n1) < 5e-13

        st_odd = states[2*n-2]
        st_even = states[2*n-1]
        wealth_odd = L + st_odd[2]
        wealth_even = L + st_even[2]
        assert abs(wealth_odd - L*prev) < 2e-11*max(1.0,L)
        assert abs(wealth_even - L*P) < 2e-11*max(1.0,L)

# Exact source-average telescope for both even and odd horizons.
L=3.7
states, it = replay(L, 200)
for T in range(1, 400):
    N=T//2
    avg=sum(it[:T])/T
    P=product_P(N)
    exact=(1.0-P)/T
    assert abs(avg-exact) < 2e-13

# Independent computation of the asymptotic constant.
M = 300000
log_cosh_sum = 0.0
for k in range(1, M+1):
    x = 1.0/(2*k+1)
    log_cosh_sum += math.log(math.cosh(x))
C_trunc = math.exp(1.0-EULER_GAMMA/2.0)/(2.0*math.exp(log_cosh_sum))
C_target = 0.907181022378999
assert abs(C_trunc-C_target) < 6e-7

# Direct large-n power laws.
N = 200000
P = 1.0
exc = None
for n in range(1, N+1):
    an=a(n)
    exc=an*P
    P *= (1.0-an)
assert abs(math.sqrt(N)*P - C_target) < 2e-5
assert abs((N**1.5)*exc - C_target/2.0) < 2e-5

# Scale independence of the iterate path.
reference = replay(1.0, 50)[1]
for L in (0.1, 10.0, 100.0):
    path = replay(L, 50)[1]
    assert max(abs(x-y) for x,y in zip(reference,path)) < 2e-12

print("verification passed")
