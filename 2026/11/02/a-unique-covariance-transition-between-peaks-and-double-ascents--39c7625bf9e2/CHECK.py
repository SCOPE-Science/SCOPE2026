"""Exact-rational reproducibility for Mallows peak/double-ascent covariance."""
from fractions import Fraction as F
from itertools import permutations


def inv(p):
    return sum(a > b for i, a in enumerate(p) for b in p[i+1:])


def peak(p, i):
    return p[i] < p[i+1] > p[i+2]


def asc(p, i):
    return p[i] < p[i+1] < p[i+2]


def a_poly(q):
    return q**8-q**7-2*q**6-2*q**5-4*q**4-3*q**3-q**2-2*q-2


def c_poly(q):
    return 2*q**5+3*q**4+5*q**3+5*q**2+3*q+1


def cov_formula(n, q):
    if n == 3:
        return -q/((q+1)*(q*q+q+1)**2)
    D = (q+1)**2*(q*q+1)*(q*q+q+1)**2*(q**4+q**3+q*q+q+1)
    return q*((n-3)*a_poly(q)-c_poly(q))/D


def direct(n, q):
    z = zP = zA = zPA = 0
    for p in permutations(range(n)):
        wt = q**inv(p)
        P = sum(peak(p, i) for i in range(n-2))
        A = sum(asc(p, i) for i in range(n-2))
        z += wt
        zP += wt*P
        zA += wt*A
        zPA += wt*P*A
    return zPA/z - zP*zA/z**2


def window_cross(t, q):
    lo = min(0, t)
    k = max(3, t+3)-lo
    z = zP = zA = zPA = 0
    for p in permutations(range(k)):
        wt = q**inv(p)
        I = int(peak(p, -lo))
        J = int(asc(p, t-lo))
        z += wt
        zP += wt*I
        zA += wt*J
        zPA += wt*I*J
    return zPA/z-zP*zA/z**2


def overlap_cov(n, q):
    return (n-4)*(window_cross(-2,q)+window_cross(2,q)) + (n-3)*(window_cross(-1,q)+window_cross(1,q)) + (n-2)*window_cross(0,q)

checks = 0
for n in range(3, 8):
    for q in (F(1,3), F(1,1), F(3,2), F(5,2), F(3,1)):
        assert direct(n,q) == cov_formula(n,q), (n,q,'full')
        checks += 1

assert direct(8,F(3,1)) == cov_formula(8,F(3,1))
checks += 1

for n in range(4, 20):
    for q in (F(1,3), F(1,2), F(1,1), F(3,2), F(2,1), F(5,2), F(3,1), F(7,2), F(4,1)):
        assert overlap_cov(n,q) == cov_formula(n,q), (n,q,'window')
        checks += 1

# Verify signs at rational brackets by exact integer evaluation; not used in infinite proof.
assert a_poly(F(2487,1000)) < 0 < a_poly(F(2488,1000))
checks += 1
for n in range(4,60):
    assert cov_formula(n,F(2,1)) < 0
    assert cov_formula(n,F(3,1)) > 0
    checks += 2

print(f'PASS {checks} exact checks, independently full-enumerated permutations through n=8.')

# Completely symbolic polynomial identity over Z[q].  This is an independent
# method from evaluating covariance at specific rational parameters.
def padd(a,b):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def pneg(a):return [-x for x in a]
def psub(a,b):return padd(a,pneg(b))
def pscale(a,k):return [x*k for x in a]
def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def powers(k,t):
    lo=min(0,t)
    dim=max(3,t+3)-lo
    z=[0]; x=[0]; y=[0]; xy=[0]
    for p in permutations(range(dim)):
        v=inv(p)
        bit=[0]*v+[1]
        z=padd(z,bit)
        if peak(p,-lo):x=padd(x,bit)
        if asc(p,t-lo):y=padd(y,bit)
        if peak(p,-lo) and asc(p,t-lo):xy=padd(xy,bit)
    return z,psub(pmul(xy,z),pmul(x,y))

vals={t:powers(3,t) for t in range(-2,3)}
Z={3:vals[0][0], 4:vals[1][0], 5:vals[2][0]}
assert vals[-1][0]==Z[4] and vals[-2][0]==Z[5]
Zsquared={k:pmul(Z[k],Z[k]) for k in Z}
Q=pmul(Zsquared[3],pmul(Zsquared[4],Zsquared[5]))
Zother={k:pmul(*[Zsquared[h] for h in sorted(Z) if h!=k]) for k in Z}
# The order in these coefficient lists is from constant to highest q power.
Acoef=[-2,-2,-1,-3,-4,-2,-2,-1,1]
Ccoef=[1,3,5,5,3,2]
D=pmul(pmul([1,2,1],[1,0,1]),pmul([1,1,1,1,1],pmul([1,2,3,2,1],[1,1,1,1,1])))
# The preceding D's first factor for S5 is already included by construction:
# D=(q+1)^2*(q^2+1)*(q^2+q+1)^2*(q^4+...+1).
D=pmul(pmul([1,2,1],[1,0,1]),pmul([1,2,3,2,1],[1,1,1,1,1]))
for n in (4,5):
    terms=[]
    for t in range(-2,3):
        dim=max(3,t+3)-min(0,t)
        weight={2:n-4,1:n-3,0:n-2,-1:n-3,-2:n-4}[t]
        terms.append(pscale(pmul(vals[t][1],Zother[dim]),weight))
    numerator=[0]
    for term in terms:numerator=padd(numerator,term)
    N=psub(pscale(Acoef,n-3),Ccoef)
    assert pmul(D,numerator)==pmul([0]+N,Q), ('symbolic',n)
    checks+=1
print(f'PASS symbolic-polynomial identities for every integer n>=4 (affine in n); {checks} total checks.')
