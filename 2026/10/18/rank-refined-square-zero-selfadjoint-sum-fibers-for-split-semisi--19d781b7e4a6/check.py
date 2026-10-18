"""Exact checks for finite-field selfadjoint square-zero sum fibers.

Self-contained arithmetic for prime fields and F_9; no external dependencies.
"""
from itertools import product
from math import prod

class Field:
    def __init__(self, q):
        assert q in (3,5,9)
        self.q=q
        self.zero=0
        self.one=1
        self.add=[[0]*q for _ in range(q)]
        self.neg=[0]*q
        self.mul=[[0]*q for _ in range(q)]
        if q!=9:
            for a in range(q):
                self.neg[a]=(-a)%q
                for b in range(q):
                    self.add[a][b]=(a+b)%q
                    self.mul[a][b]=(a*b)%q
        else:
            for a in range(q):
                a0,a1=a%3,a//3
                self.neg[a]=(-a0)%3+3*((-a1)%3)
                for b in range(q):
                    b0,b1=b%3,b//3
                    self.add[a][b]=((a0+b0)%3)+3*((a1+b1)%3)
                    self.mul[a][b]=((a0*b0+2*a1*b1)%3)+3*((a0*b1+a1*b0)%3)
        self.inv=[None]*q
        for a in range(1,q):
            self.inv[a]=next(b for b in range(1,q) if self.mul[a][b]==1)
        self.squares={self.mul[a][a] for a in range(1,q)}

    def chi(self,a):
        assert a!=0
        return 1 if a in self.squares else -1

    def mulseq(self,vals):
        z=1
        for a in vals: z=self.mul[z][a]
        return z


def rank(M,F):
    A=[list(row) for row in M]
    n=len(A); m=len(A[0]) if n else 0
    p=0
    for c in range(m):
        pivot=next((i for i in range(p,n) if A[i][c]),None)
        if pivot is None: continue
        A[p],A[pivot]=A[pivot],A[p]
        inv=F.inv[A[p][c]]
        for j in range(c,m): A[p][j]=F.mul[A[p][j]][inv]
        for i in range(n):
            if i==p or A[i][c]==0: continue
            k=A[i][c]
            for j in range(c,m):
                A[i][j]=F.add[A[i][j]][F.neg[F.mul[k][A[p][j]]]]
        p+=1
        if p==n: break
    return p


def sqzero(A,F):
    n=len(A)
    z=F.add; t=F.mul
    return all(sum_dummy(i,j,A,n,z,t)==0 for i in range(n) for j in range(n))

def sum_dummy(i,j,A,n,z,t):
    out=0
    for k in range(n): out=z[out][t[A[i][k]][A[k][j]]]
    return out


def ordered_forms(F,G):
    n=len(G)
    idx=[(i,j) for i in range(n) for j in range(i,n)]
    inv=[F.inv[g] for g in G]
    for vals in product(range(F.q), repeat=len(idx)):
        H=[[0]*n for _ in range(n)]
        for (i,j),v in zip(idx,vals): H[i][j]=H[j][i]=v
        A=tuple(tuple(F.mul[inv[i]][H[i][j]] for j in range(n)) for i in range(n))
        yield A


def brute(F, G, C):
    n=len(G)
    assert len(C)==n
    out={}
    for A in ordered_forms(F,G):
        if not sqzero(A,F): continue
        B=tuple(tuple(F.add[(C[i] if i==j else 0)][F.neg[A[i][j]]] for j in range(n)) for i in range(n))
        if sqzero(B,F):
            r=rank(A,F)
            assert r==rank(B,F)
            out[r]=out.get(r,0)+1
    return out


def group_gl(q,n):
    return prod(q**n-q**i for i in range(n))

def group_o(q,m,eps=None):
    if m==0: return 1
    if m%2:
        k=(m-1)//2
        return 2*q**(k*k)*prod(q**(2*i)-1 for i in range(1,k+1))
    k=m//2
    assert eps in (-1,1)
    return 2*q**(k*(k-1))*(q**k-eps)*prod(q**(2*i)-1 for i in range(1,k))

def s_count(q,r):
    if not r:return 1
    g=group_gl(q,r)
    if r%2:return 2*g//group_o(q,r)
    return g//group_o(q,r,1)+g//group_o(q,r,-1)

def i_count(q,n,eps,r):
    if r==0:return 1
    x=1
    for i in range(r):
        k=n-2*i
        if k%2:
            L=(q**(k-1)-1)//(q-1)
        else:
            assert eps in (-1,1)
            L=(q**(k-1)-1+eps*(q-1)*q**(k//2-1))//(q-1)
        x*=L
    for j in range(1,r+1):
        den=(q**j-1)//(q-1)
        assert x%den==0
        x//=den
    return x

def spectrum(F,G,C):
    q=F.q
    n=len(G)
    eig={v:[i for i,c in enumerate(C) if c==v] for v in range(q)}
    used=set(); fact=1; base=0
    for v in range(1,q):
        if v in used:continue
        nv=F.neg[v]; used.add(v);used.add(nv)
        plus=eig[v]; minus=eig[nv]
        if len(plus)!=len(minus): return {}
        if not plus: continue
        m=len(plus)
        dp=F.mulseq([G[i] for i in plus]); dm=F.mulseq([G[i] for i in minus])
        # b+ isometric to minus b- iff this determinant squareclass test succeeds.
        obstruction=F.mulseq(([F.neg[1]] if m%2 else [])+[dp,dm])
        if F.chi(obstruction)!=1:return {}
        ep=F.chi(F.mulseq(([F.neg[1]] if (m//2)%2 else [])+[dp])) if m%2==0 else None
        fact*=group_o(q,m,ep)
        base+=m
    Z=eig[0]; dim=len(Z)
    if dim%2:
        eps=None; w=dim//2
    else:
        det=F.mulseq([G[i] for i in Z]);
        eps=F.chi(F.mulseq(([F.neg[1]] if (dim//2)%2 else [])+[det]))
        w=dim//2 if eps==1 else max(0,dim//2-1)
    result={}
    for r in range(w+1):
        val=fact*i_count(q,dim,eps,r)*s_count(q,r)
        if val:result[base+r]=val
    return result


def check_case(q,G,C,expected=None):
    F=Field(q)
    got=brute(F,G,C)
    th=spectrum(F,G,C)
    print('q=',q,'G=',G,'C=',C,'computed=',got,'theorem=',th)
    assert got==th,(q,G,C,got,th)
    if expected is not None: assert got==expected

if __name__=='__main__':
    check_case(3,[1,2],[0,0],{0:1,1:4})
    check_case(3,[1,1],[0,0],{0:1})
    check_case(3,[1,2],[1,2],{1:2})
    check_case(3,[1,1],[1,2],{})
    check_case(5,[1,1],[1,4],{1:2}) # -1 square over 5
    check_case(9,[1,1],[1,2],{1:2}) # 2 is -1 in F9 and -1 is a square
    check_case(3,[1,2,1,2],[0,0,0,0],{0:1,1:32,2:144})
    check_case(3,[1,2,1,2],[1,2,0,0],{1:2,2:8})
    check_case(3,[1,1,1,1],[1,1,2,2],{2:8})
    check_case(3,[1,1,1,2],[1,1,2,2],{})
    f=Field(3)
    checked=0
    for n in (1,2,3):
        for G in product((1,2),repeat=n):
            for C in product(range(3),repeat=n):
                assert brute(f,G,C)==spectrum(f,G,C),(n,G,C)
                checked+=1
    assert checked==258
    print('ALL_EXACT_CHECKS_PASSED',checked,'additional diagonal tests')
