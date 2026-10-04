from itertools import combinations
from collections import deque
from scipy.optimize import linprog


def double_fan(n):
    N=n+2
    adj=[set() for _ in range(N)]
    for u in (0,1):
        for v in range(2,N):
            adj[u].add(v); adj[v].add(u)
    for v in range(2,N-1):
        adj[v].add(v+1); adj[v+1].add(v)
    edges=[]
    for u in range(N):
        for v in adj[u]:
            if u<v: edges.append((u,v))
    D=[[10**9]*N for _ in range(N)]
    for s in range(N):
        D[s][s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if D[s][v]==10**9:
                    D[s][v]=D[s][u]+1; q.append(v)
    elems=[('v',v) for v in range(N)]+[('e',e) for e in edges]
    def dist(s,e):
        if e[0]=='v': return D[s][e[1]]
        a,b=e[1]; return min(D[s][a],D[s][b])
    neighborhoods=[]
    for a,b in combinations(elems,2):
        R=tuple(s for s in range(N) if dist(s,a)!=dist(s,b))
        assert R
        neighborhoods.append(R)
    return neighborhoods


def solve_lp(N, neighborhoods, objective=None, total=None):
    A=[]; b=[]
    for R in neighborhoods:
        row=[0.0]*N
        for v in R: row[v]=-1.0
        A.append(row); b.append(-1.0)
    c=[1.0]*N if objective is None else objective
    kwargs={}
    if total is not None:
        kwargs['A_eq']=[[1.0]*N]; kwargs['b_eq']=[total]
    res=linprog(c,A_ub=A,b_ub=b,bounds=[(0.0,1.0)]*N,method='highs',**kwargs)
    assert res.success
    return res


def predicted(n):
    N=n+2
    if n==2:
        return 4.0,[1.0]*4
    if n==3:
        return 4.0,[1.0,1.0,1.0,0.0,1.0]
    x=[0.5]*N
    x[2]=1.0
    x[N-1]=1.0
    return (n+4)/2,x

neighborhoods_checked=0
coordinate_lps=0
for n in range(2,21):
    N=n+2
    R=double_fan(n)
    neighborhoods_checked += len(R)
    sets=set(frozenset(r) for r in R)
    # Every pair of vertices is an exact resolving neighborhood.
    assert all(frozenset(p) in sets for p in combinations(range(N),2))
    singleton={next(iter(s)) for s in sets if len(s)==1}
    if n==2: expected_single=set(range(N))
    elif n==3: expected_single={0,1,2,4}
    else: expected_single={2,N-1}
    assert singleton==expected_single,(n,singleton,expected_single)

    opt,xstar=predicted(n)
    # Predicted vector directly satisfies every original constraint.
    assert all(sum(xstar[v] for v in rr)>=1-1e-12 for rr in R)
    res=solve_lp(N,R)
    assert abs(res.fun-opt)<1e-8,(n,res.fun,opt)

    # Prove/check uniqueness computationally by optimizing each coordinate
    # over the optimum face of the original, unreduced LP.
    for j,t in enumerate(xstar):
        c=[0.0]*N; c[j]=1.0
        lo=solve_lp(N,R,c,opt).fun
        c[j]=-1.0
        hi=-solve_lp(N,R,c,opt).fun
        coordinate_lps += 2
        assert abs(lo-t)<1e-7 and abs(hi-t)<1e-7,(n,j,lo,hi,t)

print('VERIFY_OK')
print('double_fan_parameters_checked = 19')
print('n = 2..20')
print('original_element_pair_constraints_checked =',neighborhoods_checked)
print('coordinate_optimization_LPs =',coordinate_lps)
print('every two-vertex set occurred as an exact resolving neighborhood')
print('all singleton resolving-neighborhood classifications matched')
print('all original LP optima matched the closed formula')
print('all optimum coordinate ranges collapsed to the predicted unique optimizer')
