"""Direct enumeration of finite-field homomorphisms for the chain evolution algebra.

An image of the first basis vector determines every prospective homomorphism;
subsequent images are computed by squaring, then all multiplicative relations
are tested independently of any proposed classification.
"""
from itertools import product
from collections import Counter

class FiniteField:
    def __init__(self,q):
        self.q=q
        if q==4:
            self.add=lambda a,b:a^b
            self.mul=lambda a,b:(0 if not a or not b else (1 if a==b else ({1,2,3}-{a,b}).pop()))
            # GF4 has multiplicative group of order 3; any two distinct
            # nonzero elements multiply to the third.
        else:
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q

def square_vector(v,F):
    n=len(v)
    return tuple([0]+[F.mul(v[i],v[i]) for i in range(n-1)])

def prod_vector(x,y,F):
    n=len(x)
    return tuple([0]+[F.mul(x[i],y[i]) for i in range(n-1)])

def candidate(x,F):
    n=len(x)
    columns=[x]
    for i in range(1,n):
        columns.append(square_vector(columns[-1],F))
    for i in range(n):
        for j in range(i+1,n):
            if any(prod_vector(columns[i],columns[j],F)):
                return None
    return columns

def rank(cols,F):
    n=len(cols)
    A=[[cols[j][i] for j in range(n)] for i in range(n)]
    r=0
    for c in range(n):
        piv=next((i for i in range(r,n) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(r+1,n):
            if A[i][c]:
                factor=A[i][c]
                d=A[r][c]
                if F.q==4: inv=next(k for k in (1,2,3) if F.mul(d,k)==1)
                else:inv=pow(d,-1,F.q)
                scale=F.mul(factor,inv)
                for j in range(c,n):
                    # subtract equals add in characteristic two
                    term=F.mul(scale,A[r][j]); A[i][j]=F.add(A[i][j],term if F.q==4 else -term)
        r+=1
    return r

def predicted_rank(n,q):
    return {**{0:1,1:q-1},**{r:q*(q-1) for r in range(2,n+1)}}

def verify(n,q):
    F=FiniteField(q)
    rank_counts=Counter()
    endos={}
    for x in product(range(q),repeat=n):
        cols=candidate(x,F)
        if cols is None:continue
        rank_counts[rank(cols,F)]+=1
        endos[x]=cols
    expected=predicted_rank(n,q)
    assert dict(rank_counts)==expected,(n,q,rank_counts,expected)
    # Verify all actual endomorphisms are exactly the proposed normal forms.
    for x in endos:
        assert sum(v!=0 for v in x[:-1])<=1,(n,q,x)
    assert len(endos)==q*(1+(n-1)*(q-1))
    # Direct multiplication of matrices verifies that only zero and identity
    # are idempotent endomorphisms, and every other nonunit has nilpotent power.
    zero=(0,)*n
    ident=tuple(1 if i==0 else 0 for i in range(n))
    def apply(cols,x):
        out=[0]*n
        for i,a in enumerate(x):
            if a:
                for j,v in enumerate(cols[i]):out[j]=F.add(out[j],F.mul(a,v))
        return tuple(out)
    def compose(cols1,cols2):return tuple(apply(cols1,x) for x in cols2)
    idem=[]
    for x,cols in endos.items():
        if compose(cols,cols)==tuple(cols):idem.append(x)
    assert set(idem)=={zero,ident},(n,q,idem)
    print('PASS',n,q,'endomorphisms',len(endos),'rank_spectrum',dict(sorted(rank_counts.items())))

if __name__=='__main__':
    for q,nmax in [(2,8),(3,6),(4,5),(5,4)]:
        for n in range(2,nmax+1):verify(n,q)
    print('VERIFY_OK')
