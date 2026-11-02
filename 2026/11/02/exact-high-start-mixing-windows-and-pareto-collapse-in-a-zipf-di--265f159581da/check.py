"""Supplemental exact-rational checks for Zipf-disaster high-start mixing.

Run: python check.py (standard-library Python 3 only).
All transition probabilities and zeta brackets are rational. The stationary
probability is enclosed by rigorous integral-test bounds, with no floats.
"""
from fractions import Fraction as Q

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def zeta_bounds(beta, count=500):
    z = sum((Q(1,k**beta) for k in range(1,count+1)), Q(0))
    z_lower = z + Q(1,(beta-1)*(count+1)**(beta-1))
    z_upper = z + Q(1,(beta-1)*count**(beta-1))
    # z_lower < zeta(beta) < z_upper, so invert the brackets.
    return 1/z_upper, 1/z_lower

def transitions(beta, initial, horizon):
    masses = {initial: Q(1)}
    yield masses.copy()
    for _ in range(horizon):
        new = {}
        for k, m in masses.items():
            advance = Q(k+1,k+2)**beta
            new[k+1] = new.get(k+1,Q(0)) + m*advance
            new[0] = new.get(0,Q(0)) + m*(1-advance)
        masses = new
        yield masses.copy()

def renewals(beta, N):
    a = [Q(1,(k+1)**beta) for k in range(N+2)]
    f = [Q(0)] + [a[k-1]-a[k] for k in range(1,N+1)]
    u = [Q(1)]
    for n in range(1,N+1):
        u.append(sum((f[j]*u[n-j] for j in range(1,n+1)),Q(0)))
    return u

def criterion(beta, i, N):
    H = sum((Q(1,k**(beta-1)) for k in range(1,N+1)), Q(0))
    return Q(beta,(beta-1)*(i+1))*H < Q(i+1,i+N+1)**beta

cases = ((2,5,2),(2,10,5),(2,20,10),(2,30,30),(2,50,50),
         (3,5,2),(3,10,5),(3,20,20),(3,30,30),(4,30,30))
for beta,i,N in cases:
    lower0, upper0 = zeta_bounds(beta)
    check(criterion(beta,i,N), f"finite criterion beta={beta},i={i},N={N}")
    u = renewals(beta,N)
    for r in range(N):
        check(u[r+1] <= u[r], f"renewal monotonicity beta={beta},r={r}")
        check(u[r+1] >= lower0, f"renewal stationary lower beta={beta},r={r}")
    for n,p in enumerate(transitions(beta,i,N)):
        check(sum(p.values(),Q(0)) == 1, f"probability mass beta={beta},i={i},n={n}")
        survivor = Q(i+1,i+n+1)**beta
        check(p.get(i+n,Q(0)) == survivor, f"first-reset survivor beta={beta},i={i},n={n}")
        for k in range(i+n+1):
            mass = p.get(k,Q(0))
            lo = lower0/(k+1)**beta
            hi = upper0/(k+1)**beta
            if k == i+n:
                check(mass > hi, f"survivor positive beta={beta},i={i},n={n},k={k}")
            else:
                check(mass < lo, f"all other states negative beta={beta},i={i},n={n},k={k}")
        # The unique positive part fixes total variation exactly.
        lo_tv = survivor-upper0/(i+n+1)**beta
        hi_tv = survivor-lower0/(i+n+1)**beta
        check(0 < lo_tv <= hi_tv < 1, f"TV zeta bracket beta={beta},i={i},n={n}")
        if n:
            first_reset = sum((Q(i+1,i+j)**beta - Q(i+1,i+j+1)**beta)*u[n-j]
                              for j in range(1,n+1))
            check(first_reset == p.get(0,Q(0)),f"independent delayed renewal beta={beta},i={i},n={n}")

for beta,i,delta,N in ((2,50,Q(2,5),50),(3,30,Q(1,4),30)):
    lower0,upper0 = zeta_bounds(beta)
    # Compare exact analytic threshold against rigorous stationary-zeta bounds.
    crossed = None
    for n,p in enumerate(transitions(beta,i,N)):
        survivor = Q(i+1,i+n+1)**beta
        lo_tv = survivor-upper0/(i+n+1)**beta
        hi_tv = survivor-lower0/(i+n+1)**beta
        if crossed is None:
            if hi_tv <= delta:
                crossed = n
            else:
                check(lo_tv > delta, f"ambiguous threshold beta={beta},i={i},n={n}")
        if crossed is not None:
            check(hi_tv <= delta, f"post-threshold beta={beta},i={i},n={n}")
    check(crossed is not None, f"threshold inside certified horizon beta={beta},i={i}")
    print(f"beta={beta}, start={i}, delta={delta}: exact mixing time={crossed}")

print(f"All {checks} exact-rational checks passed.")
