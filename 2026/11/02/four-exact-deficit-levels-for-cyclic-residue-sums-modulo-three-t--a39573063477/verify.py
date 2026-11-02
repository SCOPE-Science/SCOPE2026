"""Independent finite checks for the four-level residue-sum theorem.
Uses only Python integer arithmetic and finite enumerations; infinite claims rely on proof.
"""
from math import gcd

def models(a, j):
    q = 1 << a
    m = 3*q
    P = q//2
    k = 1 << j
    step = q//k
    K0 = [(1+step*t, t%2) for t in range(k)]
    K1 = [(1+2*step*t, 0) for t in range(k//2)] + [((2*t+1)*step-1, 1) for t in range(k//2)]
    ans=[]
    for K in (K0,K1):
        for sign in (False, True):
            lifted=[]
            for x, odd in K:
                c=-1 if sign and odd else 1
                t=next(z for z in (0,1,2) if (x+q*z-c)%3 == 0)
                lifted.append(x+q*t)
            assert len(set(lifted)) == k
            assert all(gcd(x,m)==1 for x in lifted)
            assert all({(x*y)%m for x in lifted} == set(lifted) for y in lifted)
            deficit=m*k//2-sum(lifted)
            ans.append(deficit)
    if (a+j)%2 == 0:
        expected=[3*P-k,5*P-k,P,3*P]
    else:
        expected=[3*P-k,P-k,5*P,3*P]
    assert ans == expected, (a,j,ans,expected)
    return ans

def independent_groups(a):
    m=3*(1<<a)
    U=[x for x in range(1,m) if gcd(x,m)==1]
    groups_by_size={}
    seen=set()
    for g in U:
        h=set()
        x=1
        while x not in h:
            h.add(x)
            x=(x*g)%m
        key=frozenset(h)
        if key not in seen:
            seen.add(key)
            groups_by_size.setdefault(len(key), []).append(h)
    assert len(groups_by_size[2]) == 7
    for h in groups_by_size[2]:
        deficit=m-sum(h)
        assert (deficit == 0) == ((m-1) in h)
    assert len(groups_by_size[1])==1
    for j in range(2,a-1):
        k=1<<j
        H=groups_by_size[k]
        assert len(H)==4,(a,j,len(H))
        expected=set(models(a,j))
        actual={m*k//2-sum(G) for G in H}
        assert actual == expected,(a,j,actual,expected)
    assert not any(m*len(h)==2*sum(h) and (m-1) not in h for H in groups_by_size.values() for h in H)
    return sum(len(X) for X in groups_by_size.values())

if __name__=='__main__':
    cells=0
    for a in range(4,13):
        for j in range(2,a-1):
            models(a,j)
            cells += 1
    total=sum(independent_groups(a) for a in range(4,10))
    print('VERIFY_OK symbolic_CRT_order_cells=',cells,' independent_full_unit_group_subgroups=',total,' a=4..9',' modulo3_character_and_sums=PASS',' finite_only=YES')
