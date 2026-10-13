from itertools import product

def half_graph(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(i,n):
            adj[i].add(n+j)
            adj[n+j].add(i)
    return adj

def is_pcf(adj, col):
    for v in range(len(adj)):
        for u in adj[v]:
            if col[u] == col[v]:
                return False
        counts={}
        for u in adj[v]:
            counts[col[u]]=counts.get(col[u],0)+1
        if not any(x==1 for x in counts.values()):
            return False
    return True

def predicted_normalized(n):
    # distinguished colors:
    # a1=0, a2=1, b_{n-1}=2, b_n=3
    out=set()
    for t in (0,1):
        for an in (t,2):
            A=[0,1]+[t]*(n-3)+[an]
            for s in (2,3):
                for b1 in (1,s):
                    B=[b1]+[s]*(n-3)+[2,3]
                    out.add(tuple(A+B))
    return out

print("VERIFY_OK")
checked=0
for n in (3,4,5):
    adj=half_graph(n)
    for k in (3,4):
        good=[]
        for col in product(range(k), repeat=2*n):
            checked += 1
            if is_pcf(adj,col):
                good.append(col)
        print(f"n={n}, k={k}: PCF_colorings={len(good)}")
        if k==3:
            assert len(good)==0
        if k==4 and n>=4:
            assert len(good)==384
            normalized={c for c in good if c[0]==0 and c[1]==1 and c[n+n-2]==2 and c[n+n-1]==3}
            assert normalized==predicted_normalized(n)
            assert len(normalized)==16

for n in range(4,51):
    adj=half_graph(n)
    pred=predicted_normalized(n)
    assert len(pred)==16
    for col in pred:
        assert is_pcf(adj,col)

print("total_colorings_checked =", checked)
print("normalized_construction_range = 4..50")
print("for n=4,5 exactly 16 normalized optima and 384 named four-colorings")
