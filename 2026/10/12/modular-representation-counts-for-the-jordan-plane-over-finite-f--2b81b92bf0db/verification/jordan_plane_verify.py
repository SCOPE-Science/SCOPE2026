"""Independent finite-field matrix checks for Jordan-plane representation counts.
Stdlib only. Finite experiments corroborate, but do not replace, the proof."""
from itertools import product
from fractions import Fraction
from math import prod
import random

def A(a,b,q): return (a ^ b) if q==4 else ((a+b)%q)
def N(a,q): return a if q==4 or q==2 else ((-a)%q)
def S(a,b,q): return A(a,N(b,q),q)
def M(a,b,q):
    if q!=4: return (a*b)%q
    z=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1): z ^= 1 << (i+j)
    if z & 8: z ^= 0b1110  # x^3 = x*(x+1), reduce x^2+x+1
    if z & 4: z ^= 0b111  # x^2=x+1
    return z

def inv(a,q):
    for x in range(1,q):
        if M(a,x,q)==1:return x
    raise ValueError((a,q))

def matmul(A_,B_,q,n):
    return tuple(sumfield([M(A_[i*n+k],B_[k*n+j],q) for k in range(n)],q) for i in range(n) for j in range(n))
def sumfield(vals,q):
    a=0
    for v in vals:a=A(a,v,q)
    return a

def zero(n): return (0,)*(n*n)
def ident(n):return tuple(int(i==j) for i in range(n) for j in range(n))
def matsub(a,b,q):return tuple(S(x,y,q) for x,y in zip(a,b))
def matscale(a,c,q):return tuple(M(x,c,q) for x in a)
def matpow(a,r,q,n):
    out=ident(n)
    for _ in range(r):out=matmul(out,a,q,n)
    return out

def rank(A_,q):
    if not A_:return 0
    v=[list(row) for row in A_];n=len(v);m=len(v[0]);r=0
    for c in range(m):
        piv=next((i for i in range(r,n) if v[i][c]),None)
        if piv is None:continue
        v[r],v[piv]=v[piv],v[r]
        w=inv(v[r][c],q)
        v[r]=[M(w,x,q) for x in v[r]]
        for i in range(n):
            if i==r:continue
            w=v[i][c]
            if w:v[i]=[S(x,M(w,y,q),q) for x,y in zip(v[i],v[r])]
        r+=1
        if r==n:break
    return r

def commutator_map(y,q,n):
    # [X,Y] columns in basis E_{ab}
    cols=[]
    for a in range(n):
        for b in range(n):
            e=[0]*(n*n);e[a*n+b]=1;e=tuple(e)
            cols.append(matsub(matmul(e,y,q,n),matmul(y,e,q,n),q))
    return [[cols[k][i] for k in range(n*n)] for i in range(n*n)]

def field_fiber(y,q,n):
    coeff=commutator_map(y,q,n)
    b=matmul(y,y,q,n)
    r=rank(coeff,q)
    ra=rank([row+[b[i]] for i,row in enumerate(coeff)],q)
    return (0 if ra!=r else q**(n*n-r)),n*n-r

def predicted(y,q,n):
    p=2 if q==4 else q
    if matpow(y,n,q,n)==zero(n): return True
    if n==2 and p==2:
        for a in range(1,q):
            t=matsub(y,matscale(ident(n),a,q),q)
            if t!=zero(n) and matpow(t,2,q,n)==zero(n):return True
        return False
    if n==3 and p==3:
        for a in range(1,q):
            t=matsub(y,matscale(ident(n),a,q),q)
            if matpow(t,3,q,n)==zero(n) and matpow(t,2,q,n)!=zero(n):return True
        return False
    if n==3 and p==2:
        for a in range(1,q):
            # characteristic polynomial t (t-a)^2 and non-semisimple at a
            # Directly require Y(Y-aI)^2=0, ker Y dimension 1, and rank of Y-aI=2
            t=matsub(y,matscale(ident(n),a,q),q)
            if matmul(y,matpow(t,2,q,n),q,n)==zero(n) and rank([list(y[i*n:(i+1)*n]) for i in range(n)],q)==2 and matmul(y,t,q,n)!=zero(n):
                return True
        return False
    return False

def direct_count(q,n):
    arr=list(product(range(q),repeat=n*n));counts={};total=0
    for y in arr:
        yy=matmul(y,y,q,n);cnt=0
        for x in arr:
            z=matsub(matmul(x,y,q,n),matmul(y,x,q,n),q)
            if z==yy:cnt+=1
        prediction,cdim=field_fiber(y,q,n)
        assert cnt==prediction,(q,n,y,cnt,prediction,cdim)
        eligible=predicted(y,q,n)
        assert eligible is not None and (cnt!=0)==eligible,(q,n,y,cnt,eligible)
        counts[cnt]=counts.get(cnt,0)+1
        total+=cnt
    return total,counts

def irr_number(q,d):
    def mobius(n):
        k=0
        for i in range(2,n+1):
            if n%i==0:
                e=0
                while n%i==0:n//=i;e+=1
                if e>1:return 0
                k+=1
        if n>1:k+=1
        return (-1)**k
    return sum(mobius(e)*q**(d//e) for e in range(1,d+1) if d%e==0)//d

def polynomial_product(a,b,N):
    c=[Fraction(0) for _ in range(N+1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N:c[i+j]+=x*y
    return c

def euler_coeff(q,p,N):
    out=[Fraction(1)]+[Fraction(0)]*N
    for d in range(1,N+1):
        c=(1 if d==1 else 0)
        if d<=N//p:c += irr_number(q,d)-(1 if d==1 else 0)
        # zero polynomial t separately; nonzero polynomials have allowed parts divisible by p
        for mode,count in [('zero',1 if d==1 else 0),('nonzero',irr_number(q,d)-(1 if d==1 else 0))]:
            if count==0:continue
            for part in range(1,N+1):
                w=part if mode=='zero' else p*d*part
                if w>N:break
                local=[Fraction(0)]*(N+1)
                for m in range(N//w+1):
                    denom=prod((1-Fraction(1,q**(d*j))) for j in range(1,m+1))
                    local[m*w]=Fraction(1)/denom
                for _ in range(count):out=polynomial_product(out,local,N)
    return out

def gl_order(q,n):return prod((q**n-q**j) for j in range(n))

def main():
    expected={(2,2):40,(3,2):153,(4,2):1216,(2,3):2192}
    for q,n in [(2,2),(3,2),(4,2),(2,3)]:
        total,counts=direct_count(q,n)
        print('EXHAUSTIVE',q,n,total,counts)
        assert total==expected[(q,n)]
        p=2 if q==4 else q
        coef=euler_coeff(q,p,n)
        assert coef[n]*gl_order(q,n)==total,(q,n,coef,gl_order(q,n))
    rng=random.Random(20261010)
    for q,n in [(3,3),(4,3)]:
        for _ in range(500):
            y=tuple(rng.randrange(q) for _ in range(n*n))
            ct,dim=field_fiber(y,q,n)
            pr=predicted(y,q,n)
            assert (ct>0)==pr,(q,n,y,ct,dim,pr)
        print('RANDOM_AFFINE',q,n,500)
    for q,p in [(2,2),(3,3),(4,2),(5,5)]:
        N=5
        coeff=euler_coeff(q,p,N)
        vals=[int(coeff[n]*gl_order(q,n)) if n else 1 for n in range(N+1)]
        assert all(coeff[n]*gl_order(q,n)==vals[n] for n in range(N+1))
        print('EULER_INTEGER',q,vals)
    print('VERIFY_OK_JORDAN_PLANE')
if __name__=='__main__':main()
