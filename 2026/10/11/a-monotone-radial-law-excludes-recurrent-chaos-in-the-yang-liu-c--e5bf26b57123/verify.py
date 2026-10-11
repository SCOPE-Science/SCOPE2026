from fractions import Fraction

# Polynomial dictionary: monomial exponents in (a,b,c,x,y,z,w) -> rational coefficient.
N=7

def mono(i, coeff=1):
    e=[0]*N; e[i]=1
    return {tuple(e):Fraction(coeff)}

def add(p,q):
    r=dict(p)
    for m,c in q.items():
        r[m]=r.get(m,Fraction(0))+c
        if r[m]==0: del r[m]
    return r

def neg(p): return {m:-c for m,c in p.items()}
def mul(p,q):
    r={}
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(i+j for i,j in zip(m,n))
            r[k]=r.get(k,Fraction(0))+c*d
    return {m:c for m,c in r.items() if c}
def scale(p,s): return {m:Fraction(s)*c for m,c in p.items() if c}

a,b,c,x,y,z,w=[mono(i) for i in range(N)]
xd=mul(mul(y,z),w)
yd=add(mul(a,y),neg(mul(mul(x,z),w)))
zd=add(neg(mul(b,z)),mul(mul(x,y),w))
wd=add(neg(mul(c,w)),mul(mul(x,y),z))
lie=add(scale(mul(x,xd),2),scale(mul(y,yd),2))
expected=scale(mul(a,mul(y,y)),2)
assert lie==expected, (lie,expected)
print('VERIFY_OK')
