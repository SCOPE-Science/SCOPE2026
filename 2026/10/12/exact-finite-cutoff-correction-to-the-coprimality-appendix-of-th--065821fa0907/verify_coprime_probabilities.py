from fractions import Fraction
from math import gcd, pi


def factor(n):
    out=[]; p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p; e+=1
            out.append((p,e))
        p += 1 if p==2 else 2
    if n>1: out.append((n,1))
    return out


def mu(n):
    if n==1: return 1
    s=0
    for _,e in factor(n):
        if e>1: return 0
        s+=1
    return -1 if s%2 else 1


def divisors(n):
    ds=[1]
    for p,e in factor(n):
        ds=[d*p**j for d in ds for j in range(e+1)]
    return sorted(ds)


def phi(n):
    r=n
    for p,_ in factor(n): r=r//p*(p-1)
    return r


def C_formula(a,N):
    return sum(mu(d)*(N//d) for d in divisors(a))


def C_brute(a,N):
    return sum(gcd(a,n)==1 for n in range(1,N+1))


def J_formula(a,N):
    return sum(mu(d)*C_formula(a,N//d)**2
               for d in range(1,N+1) if gcd(d,a)==1)


def J_brute(a,N):
    return sum(gcd(a,x)==gcd(a,y)==gcd(x,y)==1
               for x in range(1,N+1) for y in range(1,N+1))

# Exhaustive finite cross-check of exact formulas on a nontrivial grid.
for a in range(2,31):
    for N in range(1,61):
        assert C_formula(a,N)==C_brute(a,N)
        assert J_formula(a,N)==J_brute(a,N)

# Published Proposition 2 counterexample: a=6, N=10.
p2=Fraction(C_formula(6,10),10)
assert p2==Fraction(3,10)
assert p2 < Fraction(phi(6),6)  # 3/10 < 1/3

# Published Proposition 3 counterexample: a=3, N=4.
c=C_formula(3,4); j=J_formula(3,4)
p3=Fraction(j,c*c)
assert (c,j,p3)==(3,5,Fraction(5,9))
assert float(p3) < 6/pi**2

# Published Corollary 2 counterexample: a=5, N=6.
c5=C_formula(5,6); j5=J_formula(5,6)
pjoint=Fraction(j5,36)
assert (c5,j5,pjoint)==(5,13,Fraction(13,36))
assert float(pjoint) < (6/pi**2)*(Fraction(phi(5),5)**2)

# Fixed-a limiting joint density predicted by Euler factors.
def limit_joint(a):
    base=(phi(a)/a)**2 * (6/pi**2)
    for p,_ in factor(a):
        base /= (1-1/p**2)
    return base

for a in (2,3,5,6,30):
    N=20000
    empirical=J_formula(a,N)/N**2
    target=limit_joint(a)
    assert abs(empirical-target) < 2e-3

print('VERIFY_OK exact_grid=29x60 prop2=3/10<1/3 prop3=5/9<6/pi^2 cor2=13/36<96/(25*pi^2)')
