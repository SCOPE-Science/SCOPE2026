"""Exact finite checks for weak-minus-ordinary zero-divisor graphs.

Run with Python 3. No external Python dependencies.
"""
from itertools import combinations
from math import comb


def local_ring(p, kind='dual', r=1):
    if kind == 'cyclic':
        assert r == 1
        n = p*p
        mul = lambda x, y: x*y % n
        in_max = lambda x: x % p == 0
        return list(range(n)), mul, in_max, p, p
    assert kind == 'dual' or kind == 'square_zero'
    n = p**(r+1)
    def digits(x):
        d=[]
        for _ in range(r+1):
            d.append(x%p); x//=p
        return d
    def encode(ds):
        return sum(c*p**i for i,c in enumerate(ds))
    def mul(x,y):
        a=digits(x); b=digits(y)
        return encode([(a[0]*b[0])%p]+[(a[0]*b[j]+b[0]*a[j])%p for j in range(1,r+1)])
    in_max=lambda x: x%p == 0
    return list(range(n)), mul, in_max, p, p**r


def check(p,kind,r,s):
    A,mulA,in_max,q,h=local_ring(p,kind,r)
    ring=[(a,f) for a in A for f in range(s)]
    zero=(0,0)
    def mul(x,y): return (mulA(x[0],y[0]),x[1]*y[1]%s)
    vertices=[x for x in ring if x!=zero and (in_max(x[0]) or x[1]==0)]
    ann={x:[w for w in ring if w!=zero and mul(x,w)==zero] for x in vertices}
    def label(x):
        a,f=x
        if a==0 and f!=0:return 'A'
        if a!=0 and in_max(a) and f==0:return 'B'
        if a!=0 and in_max(a) and f!=0:return 'C'
        if not in_max(a) and f==0:return 'D'
        raise AssertionError((x,'unclassified'))
    clusters={c:[x for x in vertices if label(x)==c] for c in 'ABCD'}
    a,b,c,d=s-1,h-1,(h-1)*(s-1),h*(q-1)
    assert list(map(len,clusters.values()))==[a,b,c,d]
    assert len(vertices)==h*(s+q-1)-1
    adj={x:set() for x in vertices}
    observed=0
    for x,y in combinations(vertices,2):
        weak=any(mul(w,z)==zero for w in ann[x] for z in ann[y])
        expected_weak=not(label(x)==label(y)=='D')
        assert weak==expected_weak,(kind,p,r,s,x,y,'weak')
        difference=weak and mul(x,y)!=zero
        u,v=label(x),label(y)
        expected_difference=(u==v=='A' or u==v=='C' or {u,v} in ({'A','C'},{'B','D'},{'C','D'}))
        assert difference==expected_difference,(kind,p,r,s,x,y,'difference')
        if difference:
            observed+=1;adj[x].add(y);adj[y].add(x)
    expected_edges=comb(a+c,2)+d*(b+c)
    assert observed==expected_edges,(observed,expected_edges)
    # The cliques and a direct coloring certify the exact chromatic number.
    coloring={}
    for i,x in enumerate(clusters['A']+clusters['C']): coloring[x]=i
    for x in clusters['D']: coloring[x]=0  # color from A
    for x in clusters['B']: coloring[x]=a  # color from C
    assert all(coloring[x]!=coloring[y] for x in vertices for y in adj[x])
    assert len(set(coloring.values()))==a+c
    # The sets D plus one A are independent of maximum size.
    independent=clusters['D']+[clusters['A'][0]]
    assert all(y not in adj[x] for x,y in combinations(independent,2))
    assert len(independent)==d+1
    # Twin classes: every pair within the same block is twin, no cross-block pair is.
    for x,y in combinations(vertices,2):
        twins=(adj[x]-{y})==(adj[y]-{x})
        assert twins==(label(x)==label(y)),(x,y,'twins')
    return {'ring':f'{kind}(p={p},r={r}) x F_{s}', 'q':q,'h':h,'s':s,'vertices':len(vertices),'edges':observed,'omega_chi':a+c,'alpha':d+1,'sizes':[a,b,c,d], 'adj':adj}


def main():
    cases=[(2,'cyclic',1,2),(2,'dual',1,2),(2,'cyclic',1,3),(2,'dual',1,3),
           (3,'cyclic',1,2),(3,'dual',1,2),(3,'cyclic',1,3),(3,'dual',1,3),
           (2,'square_zero',2,2),(2,'square_zero',2,3),
           (3,'square_zero',2,2)]
    for args in cases:
        result=check(*args)
        print('PASS',result['ring'],'|V|=',result['vertices'],'|E|=',result['edges'],
              'omega=chi=',result['omega_chi'],'alpha=',result['alpha'], 'block sizes=',result['sizes'])
    print('VERIFY_OK',len(cases),'rings')
if __name__=='__main__':main()
