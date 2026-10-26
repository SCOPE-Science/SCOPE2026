"""Independent finite crosschecks for the minimal-fort crown graph theorem."""
from itertools import combinations
from math import comb

def neighbors(n, v):
    if v < n:
        return sum(1 << (n + j) for j in range(n) if j != v)
    return sum(1 << j for j in range(n) if j != v-n)

def is_fort(n, mask):
    return mask != 0 and all((neighbors(n,v)&mask).bit_count() != 1
        for v in range(2*n) if not (mask >> v & 1))

def forces_all(n, blue):
    full=(1<<(2*n))-1
    while True:
        if blue == full: return True
        added=0
        for v in range(2*n):
            if blue>>v&1:
                white=neighbors(n,v)&~blue
                if white and not white&(white-1): added |= white
        if not added: return False
        blue |= added

def expected(n):
    ans=[]
    for side in (0,n):
        for triple in combinations(range(n),3):
            ans.append(sum(1<<(side+i) for i in triple))
    for i,j in combinations(range(n),2):
        ans.append((1<<i)|(1<<j)|(1<<(n+i))|(1<<(n+j)))
    return set(ans)

def trial(n):
    m=2*n; full=(1<<m)-1; exp=expected(n)
    assert len(exp)==2*comb(n,3)+comb(n,2)
    for x in exp:
        assert is_fort(n,x)
        assert all(not is_fort(n,sub) for sub in range(1,1<<m) if sub != x and (sub&x)==sub)
    count=0
    for x in range(1<<m):
        fort=is_fort(n,x)
        if fort:
            assert any(x&y==y for y in exp), ('fort without expected', n,x)
        blue=full^x
        a=x&((1<<n)-1); b=(x>>n)&((1<<n)-1)
        predicted = (a.bit_count()<=2 and b.bit_count()<=2
                     and not(a.bit_count()==2 and a==b))
        assert forces_all(n,blue)==predicted, ('forcing mismatch',n,x)
        count+=predicted
    exact=sum(comb(n,i)*comb(n,j) for i in range(3) for j in range(3))-comb(n,2)
    assert count==exact, (n,count,exact)
    print('n=',n,'forts=',len(exp),'zero forcing sets=',count,'min sets=',comb(n,2)**2-comb(n,2))

if __name__=='__main__':
    for n in range(3,8): trial(n)
    print('ALL CHECKS PASSED')
