import math

def arrows(n):
    return [(i,(i+1)%n) for i in range(n)]+[((i+1)%n,i) for i in range(n)]

def image(e,g,n):
    a,b=g
    return tuple((a+(-1)**b*x)%n for x in e)

def face(edges,n):
    ins=[0]*n;outs=[0]*n; fwd={}
    for u,v in edges:
        outs[u]+=1;ins[v]+=1
        if ins[v]>1 or outs[u]>1:return False
        fwd[u]=v
    for u in fwd:
        v=u;seen=set()
        while v in fwd:
            if v in seen:return False
            seen.add(v);v=fwd[v]
    return True

def has_fixed(n,g):
    A=arrows(n);remaining=set(A)
    while remaining:
        e=min(remaining);orb=set();cur=e
        while cur not in orb:
            orb.add(cur);cur=image(cur,g,n)
        assert cur==e
        remaining-=orb
        if face(orb,n):return True
    return False

def group_product(g,h,n):
    a,b=g;c,d=h
    return ((a+(-1)**b*c)%n, b^d)

def generated(S,n):
    closure={(0,0)}
    while True:
        nxt=closure|{group_product(x,s,n) for x in closure for s in S}
        if nxt==closure:return closure
        closure=nxt

def is_prime_power(n):
    factors=[p for p in range(2,n+1) if n%p==0 and all(p%k for k in range(2,int(math.isqrt(p))+1))]
    return len(factors)==1, (factors[0] if len(factors)==1 else 0)

# Exhaustive finite corroboration. The accompanying proof covers every n >= 6.
for n in range(6,61):
    flags={}
    for a in range(n):
        flags[(a,0)]=has_fixed(n,(a,0))
        flags[(a,1)]=has_fixed(n,(a,1))
        assert flags[(a,0)] == (math.gcd(n,a)>=2), (n,a,'rotation')
        assert flags[(a,1)], (n,a,'reflection')
    # enumerate all subgroups: every cyclic rotation subgroup <r^k>, every dihedral subgroup <r^k,r^a s>
    for k in range(1,n+1):
        if n%k:continue
        rot={(a,0) for a in range(0,n,k)}
        N=generated([h for h in rot if flags[h]],n)
        index=len(rot)//len(N)
        ispp,p=is_prime_power(n)
        expect=(p if ispp else 1) if k==1 else 1
        assert index==expect,(n,k,index,expect)
        for a in range(k):
            H=rot|{((a+j*k)%n,1) for j in range(n//k)}
            assert len(H)==2*(n//k)
            N=generated([h for h in H if flags[h]],n)
            assert len(N)==len(H),(n,k,a,len(N),len(H))
print('FIXED_ORBITS_AND_SUBGROUPS_OK n=6..60')


# Additional independent finite cellular calculation for the free sevenfold quotient.
from itertools import combinations
from collections import defaultdict

n=7
arcs=tuple((i,(i+1)%n) for i in range(n))+tuple(((i+1)%n,i) for i in range(n))
idx={e:i for i,e in enumerate(arcs)}
perm=[idx[((u+1)%n,(v+1)%n)] for u,v in arcs]
def act(face,a):
    x=list(face)
    for _ in range(a):x=[perm[i] for i in x]
    return tuple(sorted(x))

def valid(face):
    outs={}; ins={}
    for i in face:
        u,v=arcs[i]
        if u in outs or v in ins:return False
        outs[u]=v;ins[v]=u
    for u in outs:
        s=set();v=u
        while v in outs:
            if v in s:return False
            s.add(v);v=outs[v]
    return True

reps={};by_face={}; signs={};counts={}
def sign(seq):
    return -1 if sum(x>y for i,x in enumerate(seq) for y in seq[i+1:])%2 else 1
for k in [1,2,3]:
    reps[k]=[];by_face[k]={};signs[k]={}
    faces=[F for F in combinations(range(2*n),k) if valid(F)]
    counts[k]=len(faces)
    for F in faces:
        if F in by_face[k]:continue
        rep=min(act(F,a) for a in range(n))
        j=len(reps[k]);reps[k].append(rep)
        for a in range(n):
            mapped=list(rep)
            for _ in range(a):mapped=[perm[i] for i in mapped]
            sorted_f=tuple(sorted(mapped));by_face[k][sorted_f]=j;signs[k][sorted_f]=sign(mapped)
    assert len(by_face[k])==len(faces)

def boundary(k):
    rows=len(reps[k-1]);cols=len(reps[k]);M=[[0]*cols for _ in range(rows)]
    for j,F in enumerate(reps[k]):
        for i in range(len(F)):
            G=F[:i]+F[i+1:]
            M[by_face[k-1][G]][j]+=(-1)**i*signs[k-1][G]
    return M
B1=boundary(2);B2=boundary(3)
for i,row in enumerate(B1):
    for j in range(len(B2[0])):
        assert sum(row[t]*B2[t][j] for t in range(len(row)))==0

def rank_mod(M,p):
    A=[[(x%p) for x in row] for row in M]
    R=len(A); C=len(A[0]);r=0
    for c in range(C):
        j=next((j for j in range(r,R) if A[j][c]),None)
        if j is None:continue
        A[r],A[j]=A[j],A[r]
        inv=pow(A[r][c],-1,p)
        for k in range(c,C):A[r][k]=A[r][k]*inv%p
        for j in range(r+1,R):
            if A[j][c]:
                t=A[j][c]
                for k in range(c,C):A[j][k]=(A[j][k]-t*A[r][k])%p
        r+=1
    return r
print('C7_QUOTIENT_CHAIN_ORBITS', {k:len(v) for k,v in reps.items()})
for p in [2,3,5,7,11]:
    r1=rank_mod(B1,p);r2=rank_mod(B2,p)
    dim=len(reps[2])-r1-r2
    print('H1_MOD',p,'rank',dim,'ranks',r1,r2)
    assert dim==(1 if p==7 else 0)
print('CELLULAR_OK; VERIFY_OK')
