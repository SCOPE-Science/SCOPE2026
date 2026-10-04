from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
lam = [D(1), D(2), D(5)]
u0 = [D(1), D(7)/D(10), -D(9)/D(10)]
# Compatible two-step warm-up with positive finite steps.
a0, a1 = D(7)/D(100), D(11)/D(100)
u1 = [((D(1)-a1*l)*(D(1)-a0*l))*v for l, v in zip(lam, u0)]
C = (lam[2]-lam[1])/(lam[1]-lam[0])

def moments(u):
    return [sum((l**j)*(x*x) for l, x in zip(lam, u)) for j in range(4)]

def psi_values(u):
    # Proposition-11 determinant ratio using K=[u,Hu].
    m0, m1, m2, m3 = moments(u)
    den = m1*m3 - m2*m2
    if den == 0:
        raise ArithmeticError('degenerate projected denominator')
    vals = []
    for t in lam:
        # det(K^T(H-tI)K) / det(K^T H K)
        a = m1 - t*m0
        b = m2 - t*m1
        c = m3 - t*m2
        vals.append((a*c - b*b)/den)
    return vals

def ratio(u):
    return abs(u[0]/u[2])

u = [u0, u1]
ratios = [ratio(u0), ratio(u1)]
max_rel = D(0)
for k in range(10):
    pv = psi_values(u[k])
    nxt = [pv[i]*u[k+1][i] for i in range(3)]
    if any(x == 0 for x in nxt):
        raise ArithmeticError('unexpected finite termination')
    u.append(nxt)
    r = ratio(nxt)
    predicted = C*ratios[k+1]/(ratios[k]*ratios[k])
    rel = abs(r-predicted)/max(D(1), abs(predicted))
    max_rel = max(max_rel, rel)
    ratios.append(r)

if max_rel > D('1e-60'):
    raise SystemExit(f'FAIL max_relative_residual={max_rel}')
print('VERIFY_OK')
print('max_relative_residual=', max_rel)
print('ratios=', ','.join(str(x) for x in ratios[:8]))
