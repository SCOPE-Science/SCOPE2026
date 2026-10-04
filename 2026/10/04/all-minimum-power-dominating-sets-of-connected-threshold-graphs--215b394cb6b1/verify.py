from itertools import product

def graph(bits):
    n=len(bits); adj=[set() for _ in range(n)]
    for j in range(1,n):
        if bits[j]=='1':
            for i in range(j):
                adj[i].add(j); adj[j].add(i)
    return adj

def power_dominates(adj, S):
    obs=set(S)
    for v in list(S):
        obs |= adj[v]
    while True:
        new=set()
        for v in obs:
            unobs=adj[v]-obs
            if len(unobs)==1:
                new |= unobs
        if not new:
            break
        obs |= new
    return len(obs)==len(adj)

def blocks(bits):
    out=[]; start=0
    for j in range(1,len(bits)+1):
        if j==len(bits) or bits[j]!=bits[start]:
            out.append((bits[start], list(range(start,j))))
            start=j
    return out

def theorem(bits, v):
    bl=blocks(bits)
    A=[verts for typ,verts in bl if typ=='0']
    B=[verts for typ,verts in bl if typ=='1']
    for i,verts in enumerate(B):
        if v in verts:
            return all(len(A[j])==1 for j in range(i+1,len(A)))
    if v in A[0]:
        return len(A[0])<=2 and all(len(A[j])==1 for j in range(1,len(A)))
    return False

creation_sequences=0
singleton_checks=0
for n in range(2,13):
    for middle in product('01', repeat=n-2):
        bits='0'+''.join(middle)+'1'
        adj=graph(bits)
        creation_sequences += 1
        for v in range(n):
            actual=power_dominates(adj,{v})
            predicted=theorem(bits,v)
            singleton_checks += 1
            if actual != predicted:
                raise AssertionError((bits,v,actual,predicted,blocks(bits)))
print(f'VERIFY_OK creation_sequences={creation_sequences} singleton_checks={singleton_checks} max_order=12')
