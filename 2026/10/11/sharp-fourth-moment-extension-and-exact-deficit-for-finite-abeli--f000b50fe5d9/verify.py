from fractions import Fraction
from collections import Counter


def cadd(z,w): return (z[0]+w[0], z[1]+w[1])
def csub(z,w): return (z[0]-w[0], z[1]-w[1])
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def cconj(z): return (z[0],-z[1])
def abs2(z): return z[0]*z[0]+z[1]*z[1]

def check(v,D):
    D=list(D); k=len(D)
    reps={g:[] for g in range(v)}
    for a in D:
        for b in D:
            reps[(a-b)%v].append((a,b))
    lambdas={len(reps[g]) for g in range(1,v)}
    assert len(lambdas)==1
    lam=lambdas.pop()
    assert k*(k-1)==lam*(v-1)

    vals={d:(Fraction(i+1,2), Fraction((i*i+2*i+1)%7-3,5)) for i,d in enumerate(D)}
    S=sum(abs2(vals[d]) for d in D)
    Q=sum(abs2(vals[d])**2 for d in D)
    A={}; B={}
    for g in range(v):
        z=(Fraction(0),Fraction(0)); bg=Fraction(0)
        for a,b in reps[g]:
            z=cadd(z,cmul(vals[a],cconj(vals[b])))
            bg += abs2(vals[a])*abs2(vals[b])
        A[g]=z; B[g]=bg
    l4=sum(abs2(A[g]) for g in range(v))
    C4=Fraction(1)+Fraction(lam)*(Fraction(1)-Fraction(1,k))
    lhs=C4*S*S-l4
    rhs=Fraction(lam)*(Q-S*S/Fraction(k)) + sum(Fraction(lam)*B[g]-abs2(A[g]) for g in range(1,v))
    assert lhs==rhs and lhs>=0

    ones={d:(Fraction(1),Fraction(0)) for d in D}
    A1={}
    for g in range(v):
        z=(Fraction(0),Fraction(0))
        for a,b in reps[g]: z=cadd(z,cmul(ones[a],cconj(ones[b])))
        A1[g]=z
    l41=sum(abs2(A1[g]) for g in range(v))
    assert l41==C4*k*k
    return k,lam,C4,lhs

cases=[
    (7,[0,3,5,6]),
    (11,[1,3,4,5,9]),
    (19,[1,4,5,6,7,9,11,16,17]),
]
out=[]
for v,D in cases:
    out.append((v,)+check(v,D)[:3])
print('VERIFY_OK cases='+repr(out)+' exact_deficit=1 sharpness=1')
