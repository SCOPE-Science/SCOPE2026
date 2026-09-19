from itertools import product
from math import comb


def add(a,b):
    n=max(len(a),len(b)); out=[0]*n
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return trim(out)

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return trim(out)

def scale(a,c): return trim([c*x for x in a])
def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def pshift(a): return [0]+a

def one_minus_3p_pow(k):
    return [comb(k,j)*((-3)**j) for j in range(k+1)]

def one_minus_lamp_pow(k,lam):
    return [comb(k,j)*((-lam)**j) for j in range(k+1)]

def expand_from_counts(counts,n,lam=3):
    out=[0]
    for k,c in enumerate(counts):
        if not c: continue
        term=[0]*k+[1]
        term=mul(term,one_minus_lamp_pow(n-k,lam))
        out=add(out,scale(term,c))
    return trim(out)

def path_edges(n): return [(i,i+1) for i in range(n-1)]
def cycle_edges(n): return [(i,(i+1)%n) for i in range(n)]

def adjacency(n,edges):
    A=[set() for _ in range(n)]
    for u,v in edges:
        A[u].add(v); A[v].add(u)
    return A

def forces_lambda(n,edges,assignment,lam):
    A=adjacency(n,edges)
    col=list(assignment)
    for u,v in edges:
        if col[u] and col[u]==col[v]:
            return False
    changed=True
    while changed:
        changed=False
        for v in range(n):
            if col[v]: continue
            seen={col[w] for w in A[v] if col[w]}
            if len(seen)==lam-1:
                remaining=set(range(1,lam+1))-seen
                if len(remaining)!=1:
                    return False
                col[v]=next(iter(remaining))
                changed=True
    if any(x==0 for x in col): return False
    return all(col[u]!=col[v] for u,v in edges)

def brute_counts(n,edges,lam=3):
    counts=[0]*(n+1)
    for a in product(range(lam+1), repeat=n):
        if forces_lambda(n,edges,a,lam):
            counts[sum(x!=0 for x in a)]+=1
    return counts

def path_recurrence(nmax):
    F={1:[0,3],2:[0,0,6]}
    # F_n = 2p F_{n-1} + 2p(1-3p) F_{n-2}.
    factor=[0,2,-6]
    for n in range(3,nmax+1):
        F[n]=add(scale(pshift(F[n-1]),2), mul(factor,F[n-2]))
    return F

def seq_rec(a0,a1,coef1,coef2,nmax):
    # Q_n = coef1 * p * Q_{n-1} + coef2 * p(1-3p) * Q_{n-2}.
    Q={0:a0,1:a1}
    for n in range(2,nmax+1):
        first=scale(pshift(Q[n-1]),coef1)
        second=scale(mul([0,1,-3],Q[n-2]),coef2)
        Q[n]=add(first,second)
    return Q

def cycle_recurrence(nmax):
    A=seq_rec([2],[0,2],2,2,nmax)
    B=seq_rec([2],[0,-1],-1,-1,nmax)
    return {n:add(A[n],scale(B[n],2)) for n in range(3,nmax+1)}

def chromatic_count_path(n): return 3*(2**(n-1))
def chromatic_count_cycle(n): return (2**n)+2*((-1)**n)

def eval_at_third(poly):
    # Return 3^n f(1/3) when n = degree upper bound supplied separately elsewhere.
    from fractions import Fraction
    x=Fraction(1,3)
    return sum(Fraction(c)*(x**i) for i,c in enumerate(poly))

P=path_recurrence(8)
C=cycle_recurrence(8)

for n in range(1,9):
    counts=brute_counts(n,path_edges(n))
    poly=expand_from_counts(counts,n)
    assert poly==P[n], ("path",n,poly,P[n])
    assert (3**n)*eval_at_third(poly)==chromatic_count_path(n)
    print(f"path {n}: forcing-counts={counts}; polynomial={poly}")

for n in range(3,9):
    counts=brute_counts(n,cycle_edges(n))
    poly=expand_from_counts(counts,n)
    assert poly==C[n], ("cycle",n,poly,C[n])
    assert (3**n)*eval_at_third(poly)==chromatic_count_cycle(n)
    print(f"cycle {n}: forcing-counts={counts}; polynomial={poly}")

# The bipartite lambda=2 formula extends across isolated vertices.
def components(n,edges):
    A=adjacency(n,edges); seen=set(); sizes=[]
    for v in range(n):
        if v in seen: continue
        stack=[v]; seen.add(v); c=0
        while stack:
            x=stack.pop(); c+=1
            for y in A[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        sizes.append(c)
    return sizes

def bipartite_fc2_poly(n,edges):
    out=[1]
    for m in components(n,edges):
        # 2*((1-p)^m-(1-2p)^m)
        a=[comb(m,j)*((-1)**j) for j in range(m+1)]
        b=[comb(m,j)*((-2)**j) for j in range(m+1)]
        out=mul(out,scale(add(a,scale(b,-1)),2))
    return out

def disjoint_union(parts):
    edges=[]; off=0
    for n,e in parts:
        edges.extend((u+off,v+off) for u,v in e); off+=n
    return off,edges

fc2_tests=[
    (1,[]),
    (2,path_edges(2)),
    (3,path_edges(3)),
    (4,cycle_edges(4)),
    disjoint_union([(2,path_edges(2)),(1,[])]),
    disjoint_union([(4,cycle_edges(4)),(1,[])]),
]
for n,edges in fc2_tests:
    counts=brute_counts(n,edges,2)
    poly=expand_from_counts(counts,n,2)
    formula=bipartite_fc2_poly(n,edges)
    assert poly==formula, ("lambda2",n,edges,poly,formula)
    print(f"lambda2 n={n}, components={components(n,edges)}: polynomial={poly}")

print("ALL CHECKS PASSED")
