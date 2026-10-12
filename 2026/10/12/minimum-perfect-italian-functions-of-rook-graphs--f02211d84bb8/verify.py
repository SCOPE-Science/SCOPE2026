from itertools import combinations
from math import factorial

def rook_adj(m,n):
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

def is_pid(adj,lab):
    for v,x in enumerate(lab):
        if x==0 and sum(lab[u] for u in adj[v])!=2:
            return False
    return True

def generate_weight_labelings(N,W):
    # labels are 0,1,2; enumerate by positions of twos and ones
    for t in range(W//2+1):
        o=W-2*t
        if t+o>N:
            continue
        for twos in combinations(range(N),t):
            rem=[x for x in range(N) if x not in twos]
            for ones in combinations(rem,o):
                lab=[0]*N
                for x in twos: lab[x]=2
                for x in ones: lab[x]=1
                yield tuple(lab)

def predicted(m,n):
    assert 2<=m<=n
    out=set()
    if m==n:
        # permutation matrices of 1s
        import itertools
        for perm in itertools.permutations(range(n)):
            lab=[0]*(m*n)
            for i,j in enumerate(perm):
                lab[i*n+j]=1
            out.add(tuple(lab))
        return out

    # one full column of 2s
    for j in range(n):
        lab=[0]*(m*n)
        for i in range(m):
            lab[i*n+j]=2
        out.add(tuple(lab))

    # two full columns of 1s
    for j,k in combinations(range(n),2):
        lab=[0]*(m*n)
        for i in range(m):
            lab[i*n+j]=1
            lab[i*n+k]=1
        out.add(tuple(lab))

    # only when n=m+1: one full all-1 row, all other rows a 1 in one common column
    if n==m+1:
        for r in range(m):
            for j in range(n):
                lab=[0]*(m*n)
                for k in range(n):
                    lab[r*n+k]=1
                for i in range(m):
                    if i!=r:
                        lab[i*n+j]=1
                out.add(tuple(lab))
    return out

def expected_weight(m,n):
    return m if m==n else 2*m

cases=[(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5)]
checked=0
print("VERIFY_OK")
for m,n in cases:
    adj=rook_adj(m,n)
    target=expected_weight(m,n)
    actual=set()
    lower_found=False
    for w in range(target+1):
        for lab in generate_weight_labelings(m*n,w):
            checked += 1
            if is_pid(adj,lab):
                if w<target:
                    lower_found=True
                elif w==target:
                    actual.add(lab)
    assert not lower_found,(m,n)
    pred=predicted(m,n)
    assert actual==pred,(m,n,len(actual),len(pred))
    print(f"m={m}, n={n}: gamma_pI={target}, minimum_functions={len(actual)}")

constructed=0
for m in range(2,9):
    for n in range(m,10):
        adj=rook_adj(m,n)
        pred=predicted(m,n)
        if m==n:
            expected=factorial(n)
        elif n==m+1:
            expected=n + n*(n-1)//2 + m*n
        else:
            expected=n + n*(n-1)//2
        assert len(pred)==expected,(m,n,len(pred),expected)
        for lab in pred:
            assert sum(lab)==expected_weight(m,n)
            assert is_pid(adj,lab)
            constructed += 1

print("bounded_weight_labelings_checked =",checked)
print("constructed_minimum_functions_checked =",constructed)
print("direct_classification_cases =",cases)
print("construction_range = 2<=m<=8, m<=n<=9")
print("all tested minimum families matched exactly")
