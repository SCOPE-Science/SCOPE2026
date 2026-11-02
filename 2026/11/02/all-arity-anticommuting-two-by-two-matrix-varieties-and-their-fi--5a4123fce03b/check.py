"""Independent finite-field checks for the two-by-two anticommuting-tuple census."""
from itertools import product
from functools import lru_cache
from math import comb

class Field:
    def __init__(self,p,e=1):
        assert (p,e) in {(3,1),(5,1),(7,1),(3,2)}
        self.p,self.e=p,e
        self.q=p**e
    def add(self,a,b):
        if self.e==1: return (a+b)%self.p
        return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
    def mul(self,a,b):
        if self.e==1:return a*b%self.p
        a0,a1=a%3,a//3; b0,b1=b%3,b//3
        return ((a0*b0-a1*b1)%3)+3*((a0*b1+a1*b0)%3)
    def zero(self,a,b): return self.add(a,b)==0


def formula(q,m):
    T2=q*(q-1)**3*(q+1)
    T3=T2*(q-1)
    H=(1 +(q+1)*(q**m-1) +m*q*q*(q-1)
       +comb(m,2)*T2 +m*(q*q-1)*(q**m-q)
       +comb(m,3)*T3)
    total=H+m*(q-1)*q**3+comb(m,2)*q*(q+1)*(q-1)**2
    return H,total

def independent_tracefree(F,m):
    q=F.q
    V=list(product(range(q),repeat=3))
    def B(x,y):
        # polar form for Q=z^2+x*y, scaled by two
        z,x,yv=x; zz,xx,yy=y
        return F.add(F.mul(2%F.p,F.mul(z,zz)),F.add(F.mul(x,yy),F.mul(yv,xx)))
    N=len(V)
    adj=[]
    for a in V:
        bits=0
        for i,b in enumerate(V):
            if B(a,b)==0:bits|=1<<i
        adj.append(bits)
    full=(1<<N)-1
    @lru_cache(None)
    def recurse(remaining,bits):
        if remaining==0:return 1
        if bits==0:return 0
        result=0
        v=bits
        while v:
            bit=v&-v; v-=bit; i=bit.bit_length()-1
            result+=recurse(remaining-1,bits&adj[i])
        return result
    return recurse(m,full),recurse.cache_info()

def matmul(F,a,b):
    return (F.add(F.mul(a[0],b[0]),F.mul(a[1],b[2])),
            F.add(F.mul(a[0],b[1]),F.mul(a[1],b[3])),
            F.add(F.mul(a[2],b[0]),F.mul(a[3],b[2])),
            F.add(F.mul(a[2],b[1]),F.mul(a[3],b[3])))

def anticommutes(F,a,b):
    x=matmul(F,a,b);y=matmul(F,b,a)
    return all(F.zero(u,v) for u,v in zip(x,y))

def direct_full(F,m):
    q=F.q
    mats=list(product(range(q),repeat=4))
    N=len(mats)
    masks=[]
    for a in mats:
        bits=0
        for i,b in enumerate(mats):
            if anticommutes(F,a,b):bits|=1<<i
        masks.append(bits)
    full=(1<<N)-1
    @lru_cache(None)
    def recur(k,bits):
        if k==0:return 1
        t=bits; total=0
        while t:
            b=t&-t;t-=b;j=b.bit_length()-1
            total+=recur(k-1,bits&masks[j])
        return total
    return recur(m,full),recur.cache_info()


def direct_pairs_using_rank(F):
    # For each X, the anticommutator is a linear map on four coordinates.
    # Count its kernel by row reduction, not by the classification.
    q=F.q; Z=(0,0,0,0);basis=[]
    for j in range(4):
        e=[0]*4;e[j]=1;basis.append(tuple(e))
    n=0
    for X in product(range(q),repeat=4):
        cols=[]
        for E in basis:
            a=matmul(F,X,E);b=matmul(F,E,X)
            cols.append([F.add(x,y) for x,y in zip(a,b)])
        # Rank computation with inverses via brute-force finite field.
        A=[[cols[j][i] for j in range(4)] for i in range(4)]
        r=0
        for c in range(4):
            piv=next((i for i in range(r,4) if A[i][c]!=0),None)
            if piv is None:continue
            A[r],A[piv]=A[piv],A[r]
            inv=next(t for t in range(1,q) if F.mul(t,A[r][c])==1)
            A[r]=[F.mul(inv,t) for t in A[r]]
            for i in range(4):
                if i==r:continue
                h=A[i][c]
                if h:
                    minus=next(t for t in range(q) if F.add(t,h)==0)
                    A[i]=[F.add(x,F.mul(minus,y)) for x,y in zip(A[i],A[r])]
            r+=1
            if r==4:break
        n+=q**(4-r)
    return n


def run():
    for p,e in ((3,1),(5,1),(7,1),(3,2)):
        F=Field(p,e);q=F.q
        for m in ((1,2,3,4,5,6) if q==3 else ((1,2,3,4) if q==5 else (1,2,3))):
            observed,_=independent_tracefree(F,m)
            H,all_=formula(q,m)
            assert observed==H,(q,m,observed,H)
            print('TRACEFREE',q,m,H)
        if q in (3,5):
            for m in ((1,2,3,4) if q==3 else (1,2,3)):
                observed,_=direct_full(F,m)
                assert observed==formula(q,m)[1],(q,m,observed,formula(q,m)[1])
                print('FULL',q,m,observed)
        if q==9:
            observed=direct_pairs_using_rank(F)
            assert observed==formula(q,2)[1],(q,observed,formula(q,2)[1])
            print('FULL_LINEAR_KERNEL',q,2,observed)
    print('ANTICOMMUTING_M2_ALL_ARITIES_ODD_OK')

if __name__=='__main__':run()
