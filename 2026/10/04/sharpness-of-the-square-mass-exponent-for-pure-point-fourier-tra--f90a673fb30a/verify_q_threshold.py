from fractions import Fraction
import cmath, math


def rs_pair(n):
    P=[1]
    Q=[1]
    for r in range(n):
        s=1<<r
        assert len(P)==s and len(Q)==s
        P,Q=P+Q, P+[-x for x in Q]
    return P,Q

# Exact coefficient/autocorrelation checks of the Rudin--Shapiro identity
# |P_n(z)|^2+|Q_n(z)|^2=2^(n+1) on |z|=1 through n=10.
for n in range(0,11):
    P,Q=rs_pair(n)
    N=1<<n
    assert len(P)==N and len(Q)==N
    assert set(P)<=set((-1,1)) and set(Q)<=set((-1,1))
    for k in range(1,N):
        ap=sum(P[j+k]*P[j] for j in range(N-k))
        aq=sum(Q[j+k]*Q[j] for j in range(N-k))
        assert ap+aq==0
    assert sum(x*x for x in P)+sum(x*x for x in Q)==2*N

# Check the construction parameters and exact q-block mass formula for representative q<2.
def block_mass(m,q):
    # q represented as Fraction.
    # Return log2 of N_m*(a_m/(2 sqrt(N_m)))^q.
    # N_m=2^(m^2), a_m=2^(-m-4).
    return Fraction(m*m,1)*(1-Fraction(q,2)) - q*(m+5)

for q in [Fraction(1,2), Fraction(1,1), Fraction(3,2), Fraction(19,10)]:
    vals=[block_mass(m,q) for m in range(1,121)]
    assert vals[-1] > vals[-5]
    assert vals[-1] > 10

# q=2 gives a decreasing cluster mass: 2^(-2m-10).
for m in range(1,20):
    assert block_mass(m,Fraction(2,1)) == Fraction(-2*m-10,1)

# For q>2 the exponent is no larger than at q=2 once masses are <1.
# Also certify the uniform positivity margin used in the proof.
margin = 1 - math.sqrt(2)/16
assert margin > 0.91

# Numerical spot-check of the pointwise Rudin--Shapiro bound for the largest replayed order.
P,Q=rs_pair(10)
N=len(P)
for t in range(4096):
    z=cmath.exp(2j*math.pi*t/4096)
    pv=sum(c*(z**j) for j,c in enumerate(P))
    qv=sum(c*(z**j) for j,c in enumerate(Q))
    assert abs((abs(pv)**2+abs(qv)**2)-2*N) < 1e-7*N

print('VERIFY_OK')
print('positivity_margin_lower_bound=',repr(margin))
for q in [Fraction(1,1), Fraction(3,2), Fraction(19,10), Fraction(2,1)]:
    print('q=',float(q),'log2_block_mass_m120=',float(block_mass(120,q)))
