from itertools import product

def heawood():
    n=14
    edges=[]
    for j in range(7):
        for p in (j,(j+1)%7,(j+3)%7):
            edges.append((p,7+j))
    return n,sorted(set(tuple(sorted(e)) for e in edges))

def distances(n,edges):
    INF=99
    d=[[INF]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for a,b in edges: d[a][b]=d[b][a]=1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                q=d[i][k]+d[k][j]
                if q<d[i][j]: d[i][j]=q
    return d

def chains(n,d,k,l):
    ans=[]
    for t in product(range(n), repeat=k+1):
        if any(t[i]==t[i+1] for i in range(k)): continue
        if sum(d[t[i]][t[i+1]] for i in range(k))==l:
            ans.append(t)
    return ans

def dp_count(n,d,k,l):
    cur={(v,0):1 for v in range(n)}
    for _ in range(k):
        nxt={}
        for (v,s),c in cur.items():
            for w in range(n):
                if w==v: continue
                ns=s+d[v][w]
                if ns<=l: nxt[(w,ns)]=nxt.get((w,ns),0)+c
        cur=nxt
    return sum(c for (v,s),c in cur.items() if s==l)

def boundary_columns(d,src,k,l,target_index):
    cols=[]
    for t in src:
        mask=0
        for i in range(1,k):
            if d[t[i-1]][t[i+1]]==d[t[i-1]][t[i]]+d[t[i]][t[i+1]]:
                u=t[:i]+t[i+1:]
                mask ^= 1<<target_index[u]
        cols.append(mask)
    return cols

def rank_columns(cols):
    piv={}
    for v0 in cols:
        v=v0
        while v:
            p=v.bit_length()-1
            if p in piv: v ^= piv[p]
            else:
                piv[p]=v
                break
    return len(piv)

def rank_rows(cols,nrows):
    rows=[0]*nrows
    for j,col in enumerate(cols):
        x=col
        while x:
            lb=x & -x
            i=lb.bit_length()-1
            rows[i] |= 1<<j
            x ^= lb
    return rank_columns(rows)

def apply_boundary(colmask, cols):
    out=0
    j=0
    x=colmask
    while x:
        lb=x & -x
        j=lb.bit_length()-1
        out ^= cols[j]
        x ^= lb
    return out

def count_shortest_paths(d,a,b,edges):
    n=len(d)
    adj=[[] for _ in range(n)]
    for u,v in edges: adj[u].append(v); adj[v].append(u)
    memo={b:1}
    def f(v):
        if v in memo:return memo[v]
        memo[v]=sum(f(w) for w in adj[v] if d[w][b]==d[v][b]-1)
        return memo[v]
    return f(a)

def main():
    n,edges=heawood(); assert len(edges)==21
    d=distances(n,edges)
    assert max(max(r) for r in d)==3
    C2=chains(n,d,2,4); C3=chains(n,d,3,4); C4=chains(n,d,4,4)
    assert (len(C2),len(C3),len(C4))==(840,2268,1134)
    assert tuple(dp_count(n,d,k,4) for k in (2,3,4))==(840,2268,1134)
    i2={t:i for i,t in enumerate(C2)}; i3={t:i for i,t in enumerate(C3)}
    d3=boundary_columns(d,C3,3,4,i2)
    d4=boundary_columns(d,C4,4,4,i3)
    r3c=rank_columns(d3); r3r=rank_rows(d3,len(C2))
    r4c=rank_columns(d4); r4r=rank_rows(d4,len(C3))
    assert (r3c,r3r,r4c,r4r)==(840,840,1092,1092)
    for col in d4:
        assert apply_boundary(col,d3)==0
    betti=len(C3)-r3c-r4c
    assert betti==336
    # Point 0 is not incident with line 8 (= line j=1 = {1,2,4}); distance is 3.
    assert d[0][8]==3 and count_shortest_paths(d,0,8,edges)==3
    print('vertices=14 edges=21 diameter=3')
    print('C2_4=840 C3_4=2268 C4_4=1134')
    print('rank_d3=840 rank_d4=1092 beta_3_4_F2=336')
    print('nongeodetic_witness=(0,8) shortest_paths=3')
    print('VERIFY_OK')
if __name__=='__main__': main()
