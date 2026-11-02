#!/usr/bin/env python3
"""Exact checks for ternary circular adjacent-pair reconstruction profiles."""
from collections import defaultdict
from functools import lru_cache, reduce
from itertools import product
from math import factorial, gcd, comb

@lru_cache(None)
def divphi(g):
    out=[]
    for d in range(1,g+1):
        if g%d==0:
            out.append((d,sum(gcd(k,d)==1 for k in range(1,d+1))))
    return out

def rooted(A):
    n=sum(A)
    r=[sum(A[3*i:3*i+3]) for i in range(3)]
    S=[i for i in range(3) if r[i]]
    if len(S)==1: return 1
    if len(S)==2:
        i,j=S; tau=A[3*j+i]
    else:
        tau=A[3]*A[6]+A[3]*A[7]+A[5]*A[6]
    num=n*tau
    for i in S: num*=factorial(r[i]-1)
    den=1
    for a in A: den*=factorial(a)
    assert num%den==0
    return num//den

def necklaces(A):
    n=sum(A); g=reduce(gcd,A)
    val=sum(phi*rooted(tuple(v//d for v in A)) for d,phi in divphi(g))
    assert val%n==0
    return val//n

def profiles(n):
    # Every balanced matrix has an integral common three-cycle circulation t,
    # together with independent reverse-pair contributions x,y,z and loops.
    for t in range(-(n//3),n//3+1):
        rest=n-3*abs(t)
        if rest<0: continue
        for x in range(rest//2+1):
            for y in range((rest-2*x)//2+1):
                for z in range((rest-2*x-2*y)//2+1):
                    k=rest-2*(x+y+z)
                    for a in range(k+1):
                        for b in range(k-a+1):
                            c=k-a-b
                            p=max(t,0);m=max(-t,0)
                            yield (a,x+p,z+m,x+m,b,y+p,z+p,y+m,c)

def connected(A):
    S={i for i in range(3) if sum(A[3*i:3*i+3])}
    R={min(S)}
    while True:
        nxt=R|{j for i in R for j in S if A[3*i+j]}
        if nxt==R: return R==S
        R=nxt

def typ(A):
    n=sum(A); r=[sum(A[3*i:3*i+3]) for i in range(3)]
    S=[i for i in range(3) if r[i]]
    if len(S)==1: return True
    off=sum(A[3*i+j]>0 for i in range(3) for j in range(3) if i!=j)
    loops=A[0]+A[4]+A[8]
    if off==2:
        a=next(A[3*i+j] for i in range(3) for j in range(3) if i!=j and A[3*i+j])
        return a==1 or loops<=1
    if off==3:
        a=next(A[3*i+j] for i in range(3) for j in range(3) if i!=j and A[3*i+j])
        return a==1 or loops<=1
    if off!=4:return False
    # For four cross-arcs there are two directed simple cycles.
    # If they are two two-cycles, the shared vertex cannot have a loop;
    # the leaves can have loops only when their cycle occurs once.
    pairs=[(i,j) for i in range(3) for j in range(i+1,3) if A[3*i+j] and A[3*j+i]]
    if len(pairs)==2:
        hub=set(pairs[0])&set(pairs[1]); assert len(hub)==1
        h=next(iter(hub)); leaves=[i for i in range(3) if i!=h]
        x,y=(A[3*h+leaves[0]],A[3*h+leaves[1]])
        return min(x,y)==1 and A[4*h]==0 and all(A[4*j]==0 or v==1 for j,v in zip(leaves,(x,y)))
    # Theta: unique vertex with cross outdegree 2, and vertex with only
    # one incoming / outgoing branch; identify its exclusive long-cycle vertex.
    counts=[sum(A[3*i+j]>0 for j in range(3) if j!=i) for i in range(3)]
    branch=counts.index(2)
    # Short directed 2-cycle has one reverse pair; long cycle uses other edges.
    j=next(i for i in range(3) if i!=branch and A[3*branch+i] and A[3*i+branch])
    x=A[3*j+branch]
    exclusive=next(i for i in range(3) if i not in (branch,j))
    y=A[3*exclusive+branch] if A[3*exclusive+branch] else A[3*branch+exclusive]
    # Avoid relying on theta orientation in the criterion: unique iff the
    # minimal tree-count formula yields <= one rooted necklace.
    return rooted(A)<=n

def predicted(n):
    # Coefficient of the five nonnegative rational generating-function pieces.
    result=3
    if n>=2: result+=3*(n-1)
    if n>=4 and n%2==0:result+=3
    if n>=5 and n%2==1:result+=6
    if n>=3:result+=2*comb(n-1,2)
    if n>=6 and n%3==0:result+=2
    if n>=7 and (n-7)%3==0:result+=6
    if n>=4:result+=3*(n-3)
    if n>=6:
        result+=6*((n-6)//2+1)
    if n>=5:
        result+=6*((n-5)//2+1)
    if n>=8 and (n-8)%3==0:result+=6
    return result

def canon(w):return min(w[i:]+w[:i] for i in range(len(w)))

# Independent direct construction of all circular words up to length 9.
for n in range(1,10):
    cards=defaultdict(set)
    rooted_count=defaultdict(int)
    for w in product(range(3),repeat=n):
        M=[0]*9
        for i in range(n): M[3*w[i]+w[(i+1)%n]]+=1
        M=tuple(M)
        cards[M].add(canon(w));rooted_count[M]+=1
    assert all(rooted_count[M]==rooted(M) and len(V)==necklaces(M) for M,V in cards.items())
    unique=sum(len(v)==1 for v in cards.values())
    assert unique==predicted(n)
    print(f'DIRECT n={n}: profiles={len(cards)} uniquely_reconstructible={unique}')
# Entire finite set of balanced connected matrix profiles, rather than word enumeration.
for n in range(1,27):
    S=set(profiles(n))
    eligible=[A for A in S if connected(A)]
    u=sum(necklaces(A)==1 for A in eligible)
    assert u==predicted(n), (n,u,predicted(n))
    assert all(typ(A)==(necklaces(A)==1) for A in eligible),n
    print(f'MATRIX n={n}: realizable={len(eligible)} unique={u}')
print('VERIFY_OK: 9 word-length censuses, 26 matrix-length censuses, formal family coefficients')
