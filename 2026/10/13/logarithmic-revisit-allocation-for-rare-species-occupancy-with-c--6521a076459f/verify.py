"""Reproducible exact checks for the calibrated occupancy-design identities.

All finite checks are illustrations of the identities, not replacements for the
asymptotic proof in the accompanying article.
"""
from fractions import Fraction as F
from math import comb, log


def information_exact(k, psi, p, f):
    ans = F(0)
    for j in range(k + 1):
        P = p**j * (1-p)**(k-j)
        Q = f**j * (1-f)**(k-j)
        mix = psi*P + (1-psi)*Q
        ans += comb(k, j) * (P-Q)**2 / mix
    return ans


def latent_exact(k, psi, p, f):
    R = F(0)
    for j in range(k + 1):
        P = p**j * (1-p)**(k-j)
        Q = f**j * (1-f)**(k-j)
        mix = psi*P + (1-psi)*Q
        R += comb(k, j) * P*Q/mix
    return (1-R) / (psi * (1-psi))


count = 0
for p, f in [(F(4,5), F(1,10)), (F(2,3), F(1,3)), (F(9,10), F(1,20))]:
    for psi in [F(1,2), F(1,10), F(1,100)]:
        for k in range(1, 9):
            direct = information_exact(k, psi, p, f)
            assert direct == latent_exact(k, psi, p, f)
            assert 0 < direct <= 1/(psi*(1-psi))
            count += 1

zero_count = 0
for p in [F(1,10), F(1,2), F(4,5)]:
    cutoff = p/(2-2*p+p*p)
    for psi in [F(1,100), F(1,1000)]:
        assert psi < cutoff
        for k in range(1, 15):
            a = 1-(1-p)**k
            exact = information_exact(k, psi, p, F(0))
            assert exact == a/(psi*(1-psi*a))
            if k>1:
                assert exact/k < information_exact(1, psi, p, F(0))
            zero_count+=1

p, f = .8, .1
d = p*log(p/f)+(1-p)*log((1-p)/(1-f))
assert d>0
# Numerically stable count-aggregated information; small k only.
for psi in [1.e-2,1.e-4,1.e-6,1.e-8]:
    T=log(1/psi)
    vals=[]
    for k in range(1, max(40, int(3*T/d))):
        v=0.
        for j in range(k+1):
            P=p**j*(1-p)**(k-j)
            Q=f**j*(1-f)**(k-j)
            v+=comb(k,j)*(P-Q)**2/(psi*P+(1-psi)*Q)
        vals.append(v/k)
    kopt = vals.index(max(vals))+1
    assert 0.3 < kopt / (T/d) < 3.
print(f'VERIFY_OK identity_cases={count} false_positive_free_cases={zero_count} rare_prevalence_tests=4')
