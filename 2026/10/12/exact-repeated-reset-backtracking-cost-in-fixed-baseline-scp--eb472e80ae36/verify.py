import math

a = 3.0
beta = 1.0
L0 = 0.2
rho = 2.0
tau = 1.0e-3
z0 = 0.1
R = 2.0
Rc = 3.0

def ceil_plus(x):
    return max(0, math.ceil(x - 1e-14))

i_star = ceil_plus(math.log((a + beta) / (2.0 * L0), rho))
L_star = L0 * rho ** i_star
q_star = 1.0 - a / L_star
assert i_star == 4
assert abs(L_star - 3.2) < 1e-12
assert abs(q_star - 1.0 / 16.0) < 1e-12
assert 2.0 * L_star >= a + beta
if i_star:
    assert 2.0 * (L0 * rho ** (i_star - 1)) < a + beta

C_star = a * abs(a - L_star) / L_star
K_star = ceil_plus(math.log(C_star * abs(z0) / tau) / math.log(1.0 / abs(q_star)))
assert K_star == 2

z = z0
subproblems = 0
rejects = 0
stop_indices = []
for k in range(K_star + 1):
    accepted = False
    for i in range(i_star + 1):
        L = L0 * rho ** i
        trial = (1.0 - a / L) * z
        subproblems += 1
        assert abs(trial) < R
        assert trial * trial - Rc * Rc < 0.0
        lhs = 0.5 * a * trial * trial
        step = trial - z
        rhs = 0.5 * a * z * z - 0.5 * beta * step * step
        criterion = lhs <= rhs + 1e-14
        exact = 2.0 * L >= a + beta
        assert criterion == exact
        if criterion:
            assert i == i_star
            z_new = trial
            accepted = True
            break
        rejects += 1
    assert accepted
    residual = abs((a - L_star) * (z_new - z))
    if residual <= tau + 1e-14:
        stop_indices.append(k)
    else:
        assert k < K_star
    z = z_new

assert stop_indices == [K_star]
assert subproblems == (K_star + 1) * (i_star + 1) == 15
assert rejects == (K_star + 1) * i_star == 12
assert K_star * i_star == 8
print(f"i_star={i_star}")
print(f"L_star={L_star:.17g}")
print(f"q_star={q_star:.17g}")
print(f"K_star={K_star}")
print(f"subproblems={subproblems}")
print(f"rejects={rejects}")
print(f"warm_start_rejected_saves={K_star * i_star}")
print("VERIFY_OK")
