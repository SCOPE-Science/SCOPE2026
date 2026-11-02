"""Exact standalone checks for the characteristic-five symmetric-sextic theorem.

Usage: python3 verify_hesse_sextic.py
Only Python standard library is required. These are finite/symbolic consistency
checks; the arbitrary-algebraically-closed-field conclusions use the proof.
"""
from itertools import product
from math import factorial

P = 5
BASIS = [(i, j, 3-i-j) for i in range(4) for j in range(4-i)]
MONOMIALS = [(6,0,0),(0,6,0),(0,0,6),(2,2,2)]

def addpoly(a,b):
    c=a.copy()
    for e,v in b.items():
        c[e]=(c.get(e,0)+v)%P
        if not c[e]: del c[e]
    return c

def mulpoly(a,b):
    c={}
    for x,ax in a.items():
        for y,by in b.items():
            z=tuple(xi+yi for xi,yi in zip(x,y))
            c[z]=(c.get(z,0)+ax*by)%P
    return {e:v for e,v in c.items() if v}

def expand_multinomial():
    """Coefficients indexed by (x,y,z,t) exponents."""
    d={}
    for a in product(range(5),repeat=4):
        if sum(a)!=4:continue
        ex=tuple(sum(a[z]*MONOMIALS[z][j] for z in range(4)) for j in range(3))+(a[3],)
        c=factorial(4)
        den=1
        for z in a:den*=factorial(z)
        c=(c//den)%P
        d[ex]=(d.get(ex,0)+c)%P
    return {e:v for e,v in d.items() if v}

def expand_by_convolution():
    F={(6,0,0,0):1,(0,6,0,0):1,(0,0,6,0):1,(2,2,2,1):1}
    a={(0,0,0,0):1}
    for _ in range(4):a=mulpoly(a,F)
    return a

def coeff_polynomial(full,e):
    return {n:full.get(e+(n,),0) for n in range(5) if full.get(e+(n,),0)}

def matrix_full():
    full=expand_multinomial()
    assert full==expand_by_convolution(), 'two independent expansions disagree'
    return [[coeff_polynomial(full,tuple(5*(a+1)-(b+1) for a,b in zip(I,J)))
             for J in BASIS] for I in BASIS]

# Arithmetic in F_25=F_5[w]/(w^2-3): a+b*w encoded as (a,b).
def add(x,y):return ((x[0]+y[0])%5,(x[1]+y[1])%5)
def sub(x,y):return ((x[0]-y[0])%5,(x[1]-y[1])%5)
def neg(x):return ((-x[0])%5,(-x[1])%5)
def mul(x,y):return ((x[0]*y[0]+3*x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0])%5)
ZERO=(0,0);ONE=(1,0)
def powf(x,n):
    if n<0:return powf(powf(x,23),-n)
    a=ONE
    while n:
        if n&1:a=mul(a,x)
        x=mul(x,x);n//=2
    return a

def polyeval(f,t):
    r=ZERO
    for n,c in f.items():r=add(r,mul((c,0),powf(t,n)))
    return r

def rank(M):
    a=[row[:] for row in M];i=0
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]!=ZERO),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        c=powf(a[i][j],23)
        a[i]=[mul(c,x) for x in a[i]]
        for k in range(len(a)):
            if k==i:continue
            c=a[k][j]
            if c!=ZERO:a[k]=[sub(x,mul(c,y)) for x,y in zip(a[k],a[i])]
        i+=1
        if i==len(a):break
    return i

def singular_points(t,els):
    out=[]
    # projective points in 3 disjoint charts z=1; z=0,y=1; z=y=0,x=1.
    pts=[(x,y,ONE) for x in els for y in els]+[(x,ONE,ZERO) for x in els]+[(ONE,ZERO,ZERO)]
    for x,y,z in pts:
        F=add(add(powf(x,6),powf(y,6)),add(powf(z,6),mul(t,mul(powf(x,2),mul(powf(y,2),powf(z,2))))))
        d=[add(powf(x,5),mul((2,0),mul(t,mul(x,mul(powf(y,2),powf(z,2)))))),
           add(powf(y,5),mul((2,0),mul(t,mul(y,mul(powf(x,2),powf(z,2)))))),
           add(powf(z,5),mul((2,0),mul(t,mul(z,mul(powf(x,2),powf(y,2))))))]
        if F==ZERO and all(v==ZERO for v in d):out.append((x,y,z))
    return out

def run():
    H=matrix_full()
    expected={(0,0):{2:1},(1,8):{1:2},(2,7):{1:2},(3,3):{2:1},
              (4,6):{1:2},(5,5):{1:4,4:1},(6,4):{1:2},(7,2):{1:2},
              (8,1):{1:2},(9,9):{2:1}}
    assert len(BASIS)==10
    assert {(i,j):H[i][j] for i in range(10) for j in range(10) if H[i][j]}==expected
    els=[(a,b) for a in range(5) for b in range(5)]
    smooth_count=0;singular_count=0
    for t in els:
        u=powf(t,3)
        singular=(u==(3,0))
        points=singular_points(t,els)
        assert bool(points)==singular, ('singular count mismatch',t,points)
        if singular:
            singular_count+=1;continue
        smooth_count+=1
        Ht=[[polyeval(h,t) for h in row] for row in H]
        r=rank(Ht)
        exp=0 if t==ZERO else (9 if u==ONE else 10)
        assert r==exp,(t,r,exp)
        # Stable rank: the ten-term matrix is monomial with one possible zero,
        # so its semilinear Frobenius powers have the same rank (direct proof).
        for power in (1,2,5):
            Hpower=Ht
            for n in range(1,power):
                Hfro=[[powf(x,5**n) for x in row] for row in Ht]
                Hpower=[[sum_product(Hpower[i], [Hfro[k][j] for k in range(10)])
                    for j in range(10)] for i in range(10)]
            assert rank(Hpower)==exp, ('stable rank',t,power)
    assert (smooth_count,singular_count)==(22,3)
    print('CHAR5_HESSE_SEXTIC_FULL_HASSE_10X10_F25_SMOOTHNESS_AND_STABLE_RANK_PASS')
    print('F25 smooth parameters: 22; singular parameters: 3; all 10 matrix entries proved symbolically')

def sum_product(v,w):
    a=ZERO
    for x,y in zip(v,w):a=add(a,mul(x,y))
    return a

if __name__=='__main__':run()
