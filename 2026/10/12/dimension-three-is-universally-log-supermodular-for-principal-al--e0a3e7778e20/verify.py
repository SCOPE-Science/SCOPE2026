from fractions import Fraction
from itertools import permutations, combinations

VARS = ("alpha","a","b","c","u","v","p","q","r","s")
N = len(VARS)

def clean(P):
    return {m:c for m,c in P.items() if c}

def const(c):
    return {(0,)*N: Fraction(c)} if c else {}

def var(name):
    m=[0]*N; m[VARS.index(name)]=1
    return {tuple(m):Fraction(1)}

def add(P,Q):
    R=dict(P)
    for m,c in Q.items(): R[m]=R.get(m,Fraction(0))+c
    return clean(R)

def neg(P): return {m:-c for m,c in P.items()}
def sub(P,Q): return add(P,neg(Q))

def mul(P,Q):
    R={}
    for m,c in P.items():
        for n,d in Q.items():
            k=tuple(x+y for x,y in zip(m,n))
            R[k]=R.get(k,Fraction(0))+c*d
    return clean(R)

def powp(P,n):
    R=const(1)
    for _ in range(n): R=mul(R,P)
    return R

def cycles(perm):
    seen=set(); c=0
    for i in range(len(perm)):
        if i not in seen:
            c+=1; j=i
            while j not in seen:
                seen.add(j); j=perm[j]
    return c

def per_alpha_poly(M, idx):
    al=var("alpha"); out={}
    for perm in permutations(range(len(idx))):
        term=powp(al,cycles(perm))
        for ii,jj in enumerate(perm): term=mul(term,M[idx[ii]][idx[jj]])
        out=add(out,term)
    return out

al,a,b,c,u,v,p,q,r,s = [var(x) for x in VARS]
M=[[a,u,r],[v,b,p],[s,q,c]]
p123=per_alpha_poly(M,[0,1,2])
p2=per_alpha_poly(M,[1])
p12=per_alpha_poly(M,[0,1])
p23=per_alpha_poly(M,[1,2])
defect=sub(mul(p123,p2),mul(p12,p23))
expected=mul(powp(al,2), add(add(mul(mul(mul(powp(b,2),r),s),al), mul(mul(mul(b,u),p),s)), mul(mul(q,v), sub(mul(b,r),mul(u,p)))))
assert defect == expected
print("symbolic_defect_identity=OK")

# Exact directed-cycle example M0=I-B and A0=M0^{-1}.
A=[[Fraction(8,7),Fraction(4,7),Fraction(2,7)],
   [Fraction(2,7),Fraction(8,7),Fraction(4,7)],
   [Fraction(4,7),Fraction(2,7),Fraction(8,7)]]
# Inverse is [[1,-1/2,0],[0,1,-1/2],[-1/2,0,1]], whose asymmetric zero pattern rules out diagonal symmetrization.

def per_num(subset, alpha):
    if not subset: return Fraction(1)
    I=list(subset); total=Fraction(0)
    for perm in permutations(range(len(I))):
        term=alpha**cycles(perm)
        for ii,jj in enumerate(perm): term*=A[I[ii]][I[jj]]
        total+=term
    return total

def all_subsets(n):
    out=[]
    for k in range(n+1): out += list(combinations(range(n),k))
    return out

for alpha in [Fraction(1,10),Fraction(1,2),Fraction(1),Fraction(2),Fraction(7,3)]:
    subs=all_subsets(3)
    for S in subs:
        SS=set(S)
        for T in subs:
            TT=set(T)
            lhs=per_num(tuple(sorted(SS|TT)),alpha)*per_num(tuple(sorted(SS&TT)),alpha)
            rhs=per_num(S,alpha)*per_num(T,alpha)
            assert lhs>=rhs
    d=per_num((0,1,2),alpha)*per_num((1,),alpha)-per_num((0,1),alpha)*per_num((1,2),alpha)
    assert d == Fraction(512,2401)*alpha*alpha*(alpha+1)
print("nonsymmetrizable_example_checks=OK")
print("CHECK_OK")
