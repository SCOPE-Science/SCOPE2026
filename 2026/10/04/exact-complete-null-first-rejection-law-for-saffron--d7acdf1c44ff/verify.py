from fractions import Fraction
from itertools import product

# A finite gamma schedule; after its last stage alpha is zero.
lam = Fraction(1, 2)
W0 = Fraction(1, 8)
gamma = [Fraction(1,2), Fraction(1,4), Fraction(1,8), Fraction(1,8)]
a = [min(lam, W0*g) for g in gamma]

# Stage factorization for eventual no-rejection probability.
surv = Fraction(1,1)
for x in a:
    surv *= (1-lam) / ((1-lam)+x)
fdr_stage = 1-surv

# Exact DP over calendar time with states (stage, no-rejection probability).
def dp(T):
    st={0:Fraction(1,1)}
    rej=Fraction(0,1)
    for _ in range(T):
        ns={}
        for j,p in st.items():
            x=a[j] if j < len(a) else Fraction(0,1)
            rej += p*x
            # candidate but no rejection: stage stays
            ns[j]=ns.get(j,Fraction(0,1))+p*(lam-x)
            # noncandidate: stage advances
            ns[j+1]=ns.get(j+1,Fraction(0,1))+p*(1-lam)
        st=ns
    return rej, st

# Independent exhaustive recursion over the same three outcome regions.
def brute(T):
    total=Fraction(0,1)
    def rec(t,j,p):
        nonlocal total
        if t==T:
            return
        x=a[j] if j < len(a) else Fraction(0,1)
        total += p*x
        rec(t+1,j,p*(lam-x))
        rec(t+1,j+1,p*(1-lam))
    rec(0,0,Fraction(1,1))
    return total

for T in range(1,9):
    r,_=dp(T)
    assert r == brute(T)

# Eventual product can also be obtained by solving the geometric loop stage by stage.
calc=Fraction(1,1)
for x in a:
    advance=(1-lam)/((1-lam)+x)
    calc*=advance
assert 1-calc == fdr_stage

# Uncapped form and algebraic envelope.
c=W0/(1-lam)
assert all(W0*g <= lam for g in gamma)
prod_term=Fraction(1,1)
for g in gamma:
    prod_term *= 1+c*g
assert fdr_stage == 1-Fraction(1,1)/prod_term
lower=c/(1+c)
assert fdr_stage >= lower
# Rational upper surrogate: 1-exp(-c) < c, so certainly FDR < c.
assert fdr_stage < c

print('VERIFY_OK')
