from fractions import Fraction
from itertools import product

# Scalar consequence of the polar argument.
def check_family(ps, alphas, betas):
    s = sum(Fraction(1,1)/p for p in ps)
    assert s <= 1
    q = sum(a*a+b*b for a,b in zip(alphas,betas))
    l = sum(a+b for a,b in zip(alphas,betas))
    d = len(ps)
    assert q >= 2*d*d
    assert l*l >= 4*d*d*d

# Exact regular equality configurations.
for d in (2,3,4,5,8,12):
    # Work with squared quantities: alpha=beta=sqrt(d).
    ps=[Fraction(d,1)]*d
    assert sum(Fraction(1,1)/p for p in ps)==1
    assert 2*sum(ps)==2*d*d

# Rational asymmetric examples satisfying sum 1/(alpha beta) <= 1.
# The choices are intentionally coarse; the proof itself is analytic.
for d in range(2,9):
    alphas=[]; betas=[]; ps=[]
    for i in range(d):
        a=Fraction(4*d+i+1,1)
        b=Fraction(5*d+2*i+1,1)
        alphas.append(a); betas.append(b); ps.append(a*b)
    check_family(ps,alphas,betas)

# Endpoint random-variable identity: E T=0 and E T^2=1/(alpha beta).
for a,b in [(Fraction(2),Fraction(3)),(Fraction(3),Fraction(5)),(Fraction(5),Fraction(7))]:
    p=a/(a+b)
    mean=p/a-(1-p)/b
    second=p/(a*a)+(1-p)/(b*b)
    assert mean==0
    assert second==1/(a*b)

# Rational Pythagorean tight-frame pairs a^2+b^2=1.
for a,b in [(Fraction(3,5),Fraction(4,5)),(Fraction(5,13),Fraction(12,13)),(Fraction(7,25),Fraction(24,25))]:
    assert a*a+b*b==1
    sigma=(1/a+1/b)/2
    assert sigma*sigma >= 2

# Equality scalar pair a=b=1/sqrt(2) has sigma=sqrt(2), checked after squaring.
# If a=b and a^2+b^2=1, then a^2=1/2 and sigma^2=2.
a2=Fraction(1,2)
sigma2=Fraction(1,1)/a2
assert sigma2==2

print('VERIFY_OK')
print('polar_scalar_families=d=2..8 exact_rational')
print('endpoint_moments=exact')
print('tight_frame_scalar_pairs=exact_rational')
