"""Independent finite checks of a graph/Horn closure classification.
Python >=3.9, no third-party packages.
"""
from itertools import combinations
from math import comb, factorial

def neighbors(n, mask):
    p=list(combinations(range(n),2))
    a=[0]*n
    for k,(i,j) in enumerate(p):
        if mask>>k&1:
            a[i]|=1<<j; a[j]|=1<<i
    return a

def single(n, v, antecedent, x):
    return x|(1<<v) if x&antecedent==antecedent else x

def onepass(n, pre, x):
    return x|sum(1<<v for v in range(n) if pre[v]&x==pre[v])

def closed(n, pre, x):
    return all(single(n,v,pre[v],x)==x for v in range(n))

def is_clique_union(n,a):
    return all((a[u]&~(1<<v)) == (a[v]&~(1<<u)) for u in range(n) for v in range(u+1,n) if a[u]>>v&1)

def is_matching(n,a):
    return all(z.bit_count()<=1 for z in a)

def exchange(n,pre):
    for x in range(1<<n):
        cx=onepass(n,pre,x)
        for a in range(n):
            if x>>a&1:continue
            cxa=onepass(n,pre,x|(1<<a))
            for b in range(n):
                if a==b or x>>b&1 or cx>>b&1 or not (cxa>>b&1):continue
                if not (onepass(n,pre,x|(1<<b))>>a&1):
                    return False
    return True

def join_closed(n,pre):
    f=[x for x in range(1<<n) if closed(n,pre,x)]
    return all(closed(n,pre,x|y) for x in f for y in f)

def telephone(n):
    return sum(factorial(n)//(factorial(n-2*k)*factorial(k)*2**k) for k in range(n//2+1))

def bell(n):
    dp=[0]*(n+1);dp[0]=1
    for _ in range(n):
        dp=[sum(comb(k,j)*dp[j] for j in range(k+1)) if k else 1 for k in range(n+1)] if False else dp
    st=[[0]*(n+1) for _ in range(n+1)]; st[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1):st[i][j]=j*st[i-1][j]+st[i-1][j-1]
    return sum(st[n])

def graph_finite_tests():
    for n in range(1,6):
        cmat=csub=0
        for g in range(1<<comb(n,2)):
            a=neighbors(n,g)
            # Every one-pass value is the actual closure, after one update per head in either order.
            for x in range(1<<n):
                target=onepass(n,a,x)
                order=x
                for v in range(n): order=single(n,v,a[v],order)
                assert target==order,('one-pass',n,g,x)
                order=x
                for v in reversed(range(n)): order=single(n,v,a[v],order)
                assert target==order,('reverse-one-pass',n,g,x)
                miss=((1<<n)-1)^x
                no_isolated=all(a[v]&miss for v in range(n) if miss>>v&1)
                assert closed(n,a,x)==no_isolated,('fixed',n,g,x)
            mat=is_clique_union(n,a)
            sub=is_matching(n,a)
            assert mat==exchange(n,a),('exchange',n,g)
            assert sub==join_closed(n,a),('submodular',n,g)
            cmat+=mat;csub+=sub
        assert cmat==bell(n),(n,cmat,bell(n))
        assert csub==telephone(n),(n,csub,telephone(n))
        print('graph exhaustive n=%d graphs=%d matroid=%d submodular=%d'%(n,1<<comb(n,2),cmat,csub))

def rule_finite_tests():
    # Exhaust all ordered elementary clause pairs; then entire families on <=4 heads.
    for n in range(1,5):
        possible=[[(m &~(1<<v)) for m in range(1<<n) if not (m>>v&1)] for v in range(n)]
        rules=[(v,a) for v in range(n) for a in possible[v]]
        for va in rules:
            for vb in rules:
                if va[0]==vb[0]:want=True
                else:
                    want=bool(va[1]>>vb[0]&1)==bool(vb[1]>>va[0]&1)
                got=all(single(n,va[0],va[1],single(n,vb[0],vb[1],x))==single(n,vb[0],vb[1],single(n,va[0],va[1],x)) for x in range(1<<n))
                assert want==got,(n,va,vb)
        from itertools import product
        count=0
        for pre in product(*possible):
            commute=all(bool(pre[v]>>u&1)==bool(pre[u]>>v&1) for u in range(n) for v in range(u+1,n))
            if commute:count+=1
        assert count==2**comb(n,2)
        print('all-rule-pairs/families n=%d rules=%d commuting families=%d'%(n,len(rules),count))

def mean_formula(n):
    return sum((-1)**j*comb(n,j)*2**(-comb(j,2))*(1+2**(-j))**(n-j) for j in range(n+1))

def random_check():
    for n in range(1,6):
        gnum=1<<comb(n,2)
        avg=sum(sum(closed(n,neighbors(n,g),x) for x in range(1<<n)) for g in range(gnum))/gnum
        want=mean_formula(n)
        assert abs(avg-want)<1e-8,(n,avg,want)
        print('random n=%d E[fixed]=%.10f'%(n,avg))

if __name__=='__main__':
    rule_finite_tests();graph_finite_tests();random_check()
    print('VERIFY_OK')
