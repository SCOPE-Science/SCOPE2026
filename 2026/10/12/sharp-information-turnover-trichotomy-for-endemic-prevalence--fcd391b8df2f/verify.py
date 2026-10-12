from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

def root(beta, u1, u2, c, k):
    B = beta + k * (u1 - c * u2)
    disc = B * B + D(4) * beta * k * u2 * c
    return D(2) * c / (B + disc.sqrt())

def residual(beta, u1, u2, c, k, I):
    return beta * I + k * u1 * I / (D(1) + k * u2 * I) - c

def check_case(beta, u1, u2, c, regime):
    ks = [D(1), D(10), D(100), D(10000), D(1000000000000)]
    vals = [root(beta, u1, u2, c, k) for k in ks]
    assert all(vals[i+1] < vals[i] for i in range(len(vals)-1))
    assert all(abs(residual(beta, u1, u2, c, k, I)) < D('1e-60') for k, I in zip(ks, vals))
    k = ks[-1]
    I = vals[-1]
    if regime == 'supercritical':
        target = c / (u1 - c * u2)
        observed = k * I
    elif regime == 'critical':
        target = (c / (beta * u2)).sqrt()
        observed = k.sqrt() * I
    else:
        target = (c - u1 / u2) / beta
        observed = I
    rel = abs(observed - target) / target
    assert rel < D('1e-5'), (regime, observed, target, rel)
    return observed, target, rel

if __name__ == '__main__':
    beta, u2, c = D(2), D(1), D(3)
    cases = [('supercritical', D(5)), ('critical', D(3)), ('floor', D(1))]
    for regime, u1 in cases:
        observed, target, rel = check_case(beta, u1, u2, c, regime)
        print(regime, 'observed=', observed, 'target=', target, 'relative_error=', rel)
    print('VERIFY_OK')
