"""Reproduce minimum feedback-vertex-set counts in labeled cycle prisms.

Standard Python only. No external graph libraries.
"""
from itertools import combinations
from math import comb


def edges_of_prism(n):
    return ([(i, (i+1)%n) for i in range(n)]
            + [(n+i, n+(i+1)%n) for i in range(n)]
            + [(i,n+i) for i in range(n)])


def complementary_forest(n, mask, edges):
    roots=list(range(2*n))
    def find(x):
        while roots[x]!=x:
            roots[x]=roots[roots[x]]
            x=roots[x]
        return x
    for x,y in edges:
        if (mask>>x)&1 or (mask>>y)&1:
            continue
        rx,ry=find(x),find(y)
        if rx==ry:
            return False, -1
        roots[rx]=ry
    left=[i for i in range(2*n) if not (mask>>i)&1]
    return True,len({find(v) for v in left})


def pattern_prediction(n, mask):
    deleted=[((mask>>i)&1)+((mask>>(n+i))&1) for i in range(n)]
    col=[int(x>0) for x in deleted]
    if any(not(col[i] or col[(i+1)%n]) for i in range(n)):
        return False, -1
    r=n//2
    if n%2:
        if sum(col)!=r+1 or 2 in deleted:
            return False,-1
    else:
        if sum(col)==r:
            if deleted.count(2)!=1:
                return False,-1
            return True,1
        if sum(col)!=r+1 or 2 in deleted:
            return False,-1
    cuts=sum(1 for i in range(n)
        if deleted[i]==deleted[(i+1)%n]==1
        and ((mask>>i)&1)!=((mask>>((i+1)%n))&1))
    if cuts:
        return True,cuts
    return False,-1


def expected(n):
    if n%2:
        r=(n-1)//2
        return (n*(2**r),n*(2**r),0)
    r=n//2
    total=n*(3*r+2)*(2**(r-2))
    trees=n*(r+1)*(2**(r-1))
    two=r*r*(2**(r-1))
    assert trees+two==total
    return total,trees,two


def run():
    inspected=0
    count_tables=[]
    for n in range(3,13):
        k=(n+2)//2
        edges=edges_of_prism(n)
        actual=[0,0,0]
        for ss in combinations(range(2*n),k):
            mask=sum(1<<i for i in ss)
            f,c=complementary_forest(n,mask,edges)
            p,d=pattern_prediction(n,mask)
            assert f==p and (not f or c==d),(n,ss,f,c,p,d)
            inspected+=1
            if f:
                assert c in (1,2)
                actual[0]+=1
                actual[c]+=1
        assert tuple(actual)==expected(n),(n,actual,expected(n))
        for ss in combinations(range(2*n),k-1):
            mask=sum(1<<i for i in ss)
            f,c=complementary_forest(n,mask,edges)
            assert not f,(n,ss)
            inspected+=1
        count_tables.append((n,k,*actual))
    print('VERIFY_OK orders=3..12 graph_combinations_checked='+str(inspected))
    print('columns: n,minimum_feedback_set_size,total_optimal,tree_complements,two_component_complements')
    for row in count_tables:print(*row)

if __name__=='__main__':run()
