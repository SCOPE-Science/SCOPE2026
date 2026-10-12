from itertools import product
from collections import Counter


def compositions(n, k, min_part=1):
    if k == 1:
        if n >= min_part:
            yield (n,)
        return
    for a in range(min_part, n - min_part*(k-1) + 1):
        for rest in compositions(n-a, k-1, min_part):
            yield (a,) + rest


def chain_graph(alpha, beta):
    # Canonical twin classes A_1,...,A_p and B_1,...,B_p.
    # Vertices of A_i are adjacent to vertices of B_j exactly when j <= i.
    p = len(alpha)
    A=[]; B=[]
    nxt=0
    for i,a in enumerate(alpha):
        cls=list(range(nxt,nxt+a)); nxt+=a; A.append(cls)
    for j,b in enumerate(beta):
        cls=list(range(nxt,nxt+b)); nxt+=b; B.append(cls)
    N=nxt
    adj=[set() for _ in range(N)]
    for i in range(p):
        for j in range(p):
            if j <= i:
                for u in A[i]:
                    for v in B[j]:
                        adj[u].add(v); adj[v].add(u)
    return A,B,adj


def qtr_valid(adj, labels):
    for v,x in enumerate(labels):
        if x == 0:
            if not any(labels[u] == 2 for u in adj[v]):
                return False
        elif x == 2:
            if not any(labels[u] > 0 for u in adj[v]):
                return False
    return True


def universal_vertices(A,B,adj):
    X=[u for cls in A for u in cls]
    Y=[v for cls in B for v in cls]
    UX=[u for u in X if all(v in adj[u] for v in Y)]
    UY=[v for v in Y if all(u in adj[v] for u in X)]
    return X,Y,UX,UY


def predicted_minimum(A,B,adj,labels):
    X,Y,UX,UY=universal_vertices(A,B,adj)
    if sum(labels) != 4:
        return False
    twos=[v for v,x in enumerate(labels) if x==2]
    ones=[v for v,x in enumerate(labels) if x==1]
    # Type I: one universal 2 in each side.
    if len(twos)==2 and len(ones)==0:
        return ((twos[0] in UX and twos[1] in UY) or
                (twos[1] in UX and twos[0] in UY))
    # Type II-X: |X|=2, one universal X-vertex is 2, the other X-vertex is 1,
    # and an arbitrary Y-vertex is 1.
    if len(twos)==1 and len(ones)==2:
        t=twos[0]
        if t in UX and len(X)==2:
            other=[u for u in X if u != t][0]
            return other in ones and sum(v in Y for v in ones)==1
        if t in UY and len(Y)==2:
            other=[v for v in Y if v != t][0]
            return other in ones and sum(u in X for u in ones)==1
        return False
    # Type IV: graph order four, all labels 1.
    if len(twos)==0 and len(ones)==4 and len(X)==2 and len(Y)==2:
        return all(labels[v]==1 for v in X+Y)
    return False


def expected_min_count(A,B,adj):
    X,Y,UX,UY=universal_vertices(A,B,adj)
    s,t,u,v=len(X),len(Y),len(UX),len(UY)
    return u*v + (u*t if s==2 else 0) + (v*s if t==2 else 0) + (1 if s==2 and t==2 else 0)


def half_graph(n):
    # Same canonical ordering: A_i adjacent B_j iff j <= i.
    return chain_graph((1,)*n,(1,)*n)


graph_types=0
labelings=0
min_functions=0
by_order=Counter()
for N in range(4,9):
    for s in range(2,N-1):
        t=N-s
        if t < 2:
            continue
        for p in range(1,min(s,t)+1):
            for alpha in compositions(s,p):
                for beta in compositions(t,p):
                    A,B,adj=chain_graph(alpha,beta)
                    # Connectedness is automatic because all classes are nonempty and A_p/B_1 are universal to opposite side.
                    graph_types += 1
                    by_order[N] += 1
                    best=None
                    minima=[]
                    for labels in product(range(3), repeat=N):
                        labelings += 1
                        if qtr_valid(adj,labels):
                            w=sum(labels)
                            if best is None or w < best:
                                best=w; minima=[labels]
                            elif w == best:
                                minima.append(labels)
                    assert best == 4, (N,alpha,beta,best)
                    assert len(minima) == expected_min_count(A,B,adj), (N,alpha,beta,len(minima),expected_min_count(A,B,adj))
                    assert all(predicted_minimum(A,B,adj,f) for f in minima), (N,alpha,beta)
                    # Every predicted labeling must actually be a minimum QTRDF.
                    pred_count=0
                    for labels in product(range(3), repeat=N):
                        if predicted_minimum(A,B,adj,labels):
                            pred_count += 1
                            assert qtr_valid(adj,labels)
                    assert pred_count == len(minima)
                    min_functions += len(minima)

# Boundary checks that illustrate the optimizer correction in the published chain ordering.
A,B,adj=half_graph(3)
X,Y,UX,UY=universal_vertices(A,B,adj)
# x_3 is the universal X vertex; y_1 is the universal Y vertex; y_3 is not universal.
x3=A[2][0]; y1=B[0][0]; y3=B[2][0]
wrong=[0]*6; wrong[x3]=2; wrong[y3]=2
right=[0]*6; right[x3]=2; right[y1]=2
assert not qtr_valid(adj,wrong)
assert qtr_valid(adj,right)
assert len(UX)==1 and len(UY)==1

print("VERIFY_OK")
print("connected_chain_graph_types_checked =", graph_types)
print("orders_checked = 4..8")
print("types_by_order =", dict(sorted(by_order.items())))
print("ternary_labelings_checked =", labelings)
print("minimum_functions_checked =", min_functions)
print("all minima had weight 4 and matched the four-family classification")
print("all minimum-function counts matched u*v + [s=2]u*t + [t=2]v*s + [s=t=2]")
print("half_graph_H3_published_endpoint_pattern_x3_y3 = invalid")
print("half_graph_H3_universal_pair_x3_y1 = valid")
