#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction

PAIR_CACHE={n:tuple(combinations(range(n),2)) for n in range(1,7)}

def outmasks(n,bits):
    out=[0]*n
    for k,(i,j) in enumerate(PAIR_CACHE[n]):
        if (bits>>k)&1: out[i]|=1<<j
        else: out[j]|=1<<i
    return out

def amat(n,bits):
    A=[[0]*n for _ in range(n)]
    for k,(i,j) in enumerate(PAIR_CACHE[n]):
        if (bits>>k)&1:A[i][j]=1;A[j][i]=-1
        else:A[i][j]=-1;A[j][i]=1
    return A

def pfaffian_int(M):
    n=len(M)
    if n==0:return 1
    if n==2:return M[0][1]
    total=0
    for j in range(1,n):
        sub=[[M[a][b] for b in range(n) if b not in (0,j)] for a in range(n) if a not in (0,j)]
        total += ((-1)**(j+1))*M[0][j]*pfaffian_int(sub)
    return total

def bp_fast(n,bits,vertices=None):
    V=tuple(range(n)) if vertices is None else tuple(vertices)
    A=amat(n,bits)
    for r in range(1,len(V)+1,2):
        for S in combinations(V,r):
            if r==1:q=[1]
            else:
                B=[[A[i][j] for j in S] for i in S]
                q=[]
                for k in range(r):
                    minor=[[B[i][j] for j in range(r) if j!=k] for i in range(r) if i!=k]
                    q.append(((-1)**k)*pfaffian_int(minor))
                if all(z<0 for z in q):q=[-z for z in q]
                if not all(z>0 for z in q):continue
            # q is a positive left-kernel vector on S. Check nonnegative payoff against every column in V.
            ok=True
            for j in V:
                val=sum(q[t]*A[S[t]][j] for t in range(r))
                if val<0 or (j in S and val!=0):ok=False;break
            if ok:
                den=sum(q); p=[Fraction(0)]*n
                for i,z in zip(S,q):p[i]=Fraction(z,den)
                return frozenset(S),tuple(p)
    raise AssertionError('no maximal lottery')

def solve_unique(eqs,rhs,nvar):
    M=[[Fraction(x) for x in row]+[Fraction(b)] for row,b in zip(eqs,rhs)]
    r=0;piv=[]
    for c in range(nvar):
        q=next((i for i in range(r,len(M)) if M[i][c]),None)
        if q is None:continue
        M[r],M[q]=M[q],M[r]
        z=M[r][c];M[r]=[x/z for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]:
                z=M[i][c];M[i]=[M[i][j]-z*M[r][j] for j in range(nvar+1)]
        piv.append(c);r+=1
    if any(all(row[c]==0 for c in range(nvar)) and row[nvar]!=0 for row in M):return None
    if len(piv)!=nvar:return None
    x=[Fraction(0)]*nvar
    for i,c in enumerate(piv):x[c]=M[i][nvar]
    return tuple(x)

def bp_gauss(n,bits):
    A=amat(n,bits)
    for r in range(1,n+1,2):
        for S in combinations(range(n),r):
            x=solve_unique([[A[i][j] for j in S] for i in S]+[[1]*r],[0]*r+[1],r)
            if x is None or not all(z>0 for z in x):continue
            p=[Fraction(0)]*n
            for i,z in zip(S,x):p[i]=z
            pay=[sum(p[i]*A[i][j] for i in range(n)) for j in range(n)]
            if all(v>=0 for v in pay) and all(pay[j]==0 for j in S):return frozenset(S),tuple(p)
    raise AssertionError

def covers(out,y,x,S):
    return ((out[y]>>x)&1) and ((out[x]&S) & ~(out[y]&S))==0

def is_covering(out,B,n):
    full=(1<<n)-1
    rem=full^B
    x=0
    while rem:
        l=rem & -rem;x=l.bit_length()-1;rem^=l;S=B|l
        ys=B;ok=False
        while ys:
            q=ys&-ys;y=q.bit_length()-1;ys^=q
            if covers(out,y,x,S):ok=True;break
        if not ok:return False
    return True

def mc_brute(n,bits):
    out=outmasks(n,bits);stable=[]
    for B in range(1,1<<n):
        if is_covering(out,B,n):stable.append(B)
    mins=[]
    for B in stable:
        if not any(C!=B and (C&B)==C for C in stable):mins.append(B)
    assert len(mins)==1
    return frozenset(i for i in range(n) if (mins[0]>>i)&1)

def uncovered_in(out,S):
    U=0; xs=S
    while xs:
        q=xs&-xs;x=q.bit_length()-1;xs^=q;covered=False
        ys=S&~q
        while ys:
            r=ys&-ys;y=r.bit_length()-1;ys^=r
            if covers(out,y,x,S):covered=True;break
        if not covered:U|=q
    return U

def mc_brandt(n,bits,BP):
    out=outmasks(n,bits);B=sum(1<<i for i in BP);full=(1<<n)-1
    while True:
        A=0; rem=full^B
        while rem:
            q=rem&-rem;a=q.bit_length()-1;rem^=q
            if uncovered_in(out,B|q)&q:A|=q
        if not A:return frozenset(i for i in range(n) if (B>>i)&1)
        V=tuple(i for i in range(n) if (A>>i)&1)
        add,_=bp_fast(n,bits,V); B |= sum(1<<i for i in add)

def perm_maps(n):
    idx={e:k for k,e in enumerate(PAIR_CACHE[n])};maps=[]
    for p in permutations(range(n)):
        m=[]
        for k,(i,j) in enumerate(PAIR_CACHE[n]):
            a,b=p[i],p[j];x,y=sorted((a,b));newk=idx[(x,y)]
            # old bit 1 means i beats j. New bit should be 1 iff p(i)<p(j) and p(i) beats p(j), or if p(i)>p(j) then bit 0 encodes win.
            flip=(a>b)
            m.append((newk,flip))
        maps.append(tuple(m))
    return maps
PM6=perm_maps(6)
def canonical6(bits):
    best=1<<16
    for m in PM6:
        u=0
        for k,(newk,flip) in enumerate(m):
            bit=(bits>>k)&1
            if bit ^ flip:u|=1<<newk
        if u<best:best=u
    return best

def payoffs(n,bits,p):
    A=amat(n,bits)
    return tuple(sum(p[i]*A[i][j] for i in range(n)) for j in range(n))

hist={};diff={};bad=[]
for n in range(1,7):
    H=Counter();d=0
    for bits in range(1<<(n*(n-1)//2)):
        B,p=bp_fast(n,bits)
        M=mc_brute(n,bits)
        assert B<=M
        H[(len(B),len(M),B==M)]+=1
        if B!=M:
            d+=1
            if n==6:bad.append(bits)
        # Independent algorithm replay for every tournament through n=5 and every strict n=6 case.
        if n<=5 or B!=M:
            assert mc_brandt(n,bits,B)==M
    hist[n]=H;diff[n]=d

assert diff=={1:0,2:0,3:0,4:0,5:0,6:1440}
assert hist[6]==Counter({(3,3,True):20480,(1,1,True):6144,(5,5,True):4704,(5,6,False):1440})
for b in bad:
    assert bp_gauss(6,b)==bp_fast(6,b)
classes=Counter(canonical6(b) for b in bad)
assert classes==Counter({344:720,345:720})

# Independent rational Gaussian replay on both canonical types.
expected={
344:(frozenset({0,1,2,4,5}),
     (Fraction(1,5),Fraction(1,5),Fraction(1,5),Fraction(0),Fraction(1,5),Fraction(1,5)),
     (Fraction(0),Fraction(0),Fraction(0),Fraction(1,5),Fraction(0),Fraction(0))),
345:(frozenset({0,1,3,4,5}),
     (Fraction(1,3),Fraction(1,9),Fraction(0),Fraction(1,3),Fraction(1,9),Fraction(1,9)),
     (Fraction(0),Fraction(0),Fraction(1,9),Fraction(0),Fraction(0),Fraction(0))),
}
for bits,(B,p,pay) in expected.items():
    assert bp_fast(6,bits)==(B,p)
    assert bp_gauss(6,bits)==(B,p)
    assert mc_brute(6,bits)==frozenset(range(6))
    assert mc_brandt(6,bits,B)==frozenset(range(6))
    assert payoffs(6,bits,p)==pay

print('VERIFY_OK')
for n in range(1,7):print('n',n,'total',1<<(n*(n-1)//2),'diff',diff[n],'hist',dict(hist[n]))
print('n6_probability','1440/32768 = 45/1024')
print('n6_classes',dict(classes))
for bits in (344,345):
    B,p,pay=expected[bits]
    print('class',bits,'BP',sorted(B),'MC',list(range(6)),'lottery',p,'pay',pay,'orbit',classes[bits])
