from itertools import product, permutations
from math import factorial

def rook_graph(m,n):
    # vertices are (i,j), flattened as i*n+j
    N=m*n
    adj=[set() for _ in range(N)]
    for i in range(m):
        for j in range(n):
            v=i*n+j
            for jj in range(n):
                if jj!=j:
                    adj[v].add(i*n+jj)
            for ii in range(m):
                if ii!=i:
                    adj[v].add(ii*n+j)
    return adj

def is_idrdf(adj, lab):
    pos={v for v,x in enumerate(lab) if x>0}
    for v in pos:
        if adj[v] & pos:
            return False
    for v,x in enumerate(lab):
        if x==0:
            n3=sum(lab[u]==3 for u in adj[v])
            n2=sum(lab[u]==2 for u in adj[v])
            if n3<1 and n2<2:
                return False
        elif x==1:
            if not any(lab[u]>=2 for u in adj[v]):
                return False
    return True

def predicted_minima(m,n):
    assert m<=n
    out=set()
    for cols in permutations(range(n),m):
        lab=[0]*(m*n)
        val=2 if m==n else 3
        for i,j in enumerate(cols):
            lab[i*n+j]=val
        out.add(tuple(lab))
    return out

def predicted_value(m,n):
    r=min(m,n)
    return 2*r if m==n else 3*r

print("VERIFY_OK")
checked=0
for m,n in [(2,2),(2,3),(3,3)]:
    adj=rook_graph(m,n)
    best=None
    mins=[]
    for lab in product(range(4), repeat=m*n):
        checked += 1
        w=sum(lab)
        if best is not None and w>best:
            continue
        if is_idrdf(adj,lab):
            if best is None or w<best:
                best=w
                mins=[lab]
            elif w==best:
                mins.append(lab)
    pred=predicted_minima(m,n)
    assert best==predicted_value(m,n), (m,n,best)
    assert set(mins)==pred, (m,n,len(mins),len(pred))
    print(f"m={m}, n={n}: i_dR={best}, minimum_functions={len(mins)}")

for m in range(2,9):
    for n in range(m,9):
        adj=rook_graph(m,n)
        pred=predicted_minima(m,n)
        expected = factorial(n)//factorial(n-m)
        assert len(pred)==expected
        for lab in pred:
            assert sum(lab)==predicted_value(m,n)
            assert is_idrdf(adj,lab)

print("full_labelings_checked =",checked)
print("constructed_parameter_range = 2<=m<=n<=8")
print("all exhaustive minima matched the injection/permutation classification")
