"""Independent exhaustive rank distribution check of unicyclic skew matrix formula.

Python 3 stdlib only. Verify supports and finite-field weights for listed graphs,
including even/odd cycles and trees attached to a cycle. All matrices are
skew alternating; q is prime in this executable checker.
"""
from collections import Counter
from itertools import product


def maximum_matching(n, edges):
    # Exhaustive edge subset recurrence, independent of matrix elimination.
    edges = list(edges)
    def rec(i, used):
        if i == len(edges):
            return 0
        a,b=edges[i]
        nottake=rec(i+1,used)
        take=0 if (used & ((1<<a)|(1<<b))) else 1+rec(i+1, used | (1<<a)|(1<<b))
        return max(nottake,take)
    return rec(0,0)


def max_with_edge(n, edges, e):
    a,b=e
    return 1+maximum_matching(n, [f for f in edges if a not in f and b not in f])


def matrix_rank(A, p):
    A=[row[:] for row in A]
    n=len(A)
    r=0
    for j in range(n):
        piv=next((i for i in range(r,n) if A[i][j]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][j],-1,p)
        for k in range(j,n): A[r][k]=(A[r][k]*inv)%p
        for i in range(r+1,n):
            a=A[i][j]%p
            if a:
                for k in range(j,n): A[i][k]=(A[i][k]-a*A[r][k])%p
        r+=1
        if r==n: break
    return r


def predicted(n, E, C, p):
    wc=p-1; out=Counter()
    C=set(C); cycverts=set(x for e in C for x in e)
    for s in range(1<<len(E)):
        F=[e for i,e in enumerate(E) if (s>>i)&1]
        Fset=set(F)
        nu=maximum_matching(n,F)
        ways=wc**len(F)
        if len(C)%2==0 and C<=Fset:
            # Cyclic length is number of edges; no maximum matching can use
            # a boundary edge exactly when all maximum matchings isolate cycle.
            cross=[e for e in F if (e[0] in cycverts)!=(e[1] in cycverts)]
            theta=all(max_with_edge(n,F,e)<nu for e in cross)
            if theta:
                lost=ways//wc
                out[nu]-=lost
                out[nu-1]+=lost
        out[nu]+=ways
    return out



def predicted_factorized(n, E, C, p):
    # Independent assembly of the correction from rooted forest states.
    # Unlike predicted(), never uses the global cross-edge criterion.
    t=p-1
    baseline=Counter()
    for mask in range(1<<len(E)):
        S=[e for i,e in enumerate(E) if mask>>i & 1]
        baseline[maximum_matching(n,S)]+=t**len(S)
    if len(C)%2:
        return baseline
    verts={x for e in C for x in e}
    branch_edges=[e for e in E if e not in C]
    roots=[]
    for v in sorted(verts):
        found={v}
        while True:
            expanded=found | {b for a,b in branch_edges if a in found} | {a for a,b in branch_edges if b in found}
            if expanded==found:
                break
            found=expanded
        roots.append([e for e in branch_edges if e[0] in found and e[1] in found])
    assert sum(len(r) for r in roots)==len(branch_edges)
    correction=Counter({0:1})
    for v,Sv in zip(sorted(verts),roots):
        Q=Counter()
        for mask in range(1<<len(Sv)):
            S=[e for i,e in enumerate(Sv) if mask>>i & 1]
            a=maximum_matching(n,[e for e in S if v not in e])
            if maximum_matching(n,S)==a:
                Q[a]+=t**len(S)
        correction_next=Counter()
        for j,x in correction.items():
            for k,y in Q.items():
                correction_next[j+k]+=x*y
        correction=correction_next
    for k,x in correction.items():
        baseline[len(C)//2-1+k]+=t**(len(C)-1)*x
        baseline[len(C)//2+k]-=t**(len(C)-1)*x
    return baseline


def direct(n,E,p):
    out=Counter()
    for vals in product(range(p), repeat=len(E)):
        A=[[0]*n for _ in range(n)]
        for (i,j),w in zip(E,vals):
            A[i][j]=w
            A[j][i]=(-w)%p
        rank=matrix_rank(A,p)
        assert rank%2==0
        out[rank//2]+=1
    return out


def graph(L,attached):
    # unique cycle on [0,L-1], additional edges are rooted attachments
    C=[tuple(sorted((i,(i+1)%L))) for i in range(L)]
    E=list(dict.fromkeys(C+[tuple(sorted(e)) for e in attached]))
    return max([v for e in E for v in e])+1, E, C

CASES=[
    graph(3,[]),
    graph(4,[]),
    graph(5,[]),
    graph(4,[(0,4)]),
    graph(4,[(0,4),(4,5)]),
    graph(4,[(0,4),(1,5)]),
    graph(4,[(0,4),(4,5),(1,6)]),
    graph(3,[(0,3),(3,4)]),
    graph(6,[]),
    graph(6,[(0,6)]),
]

if __name__=='__main__':
    count=0
    for n,E,C in CASES:
        for p in (2,3):
            a=predicted(n,E,C,p)
            b=direct(n,E,p)
            c=predicted_factorized(n,E,C,p)
            assert a==b==c,(n,E,p,a,b,c)
            assert sum(a.values())==p**len(E)
            print(f'OK n={n} edges={len(E)} q={p} ranks={dict(sorted(a.items()))}')
            count+=1
    print(f'VERIFY_OK {count} direct exhaustive graph-field cases; independent rooted factorization')
