#!/usr/bin/env python3
"""Finite checks for fixed-sum triple partition intersection (stdlib only).

This checks finite boundary cases and sample orders, not the unbounded proof.
"""

def partitions(n):
    return tuple((a,b,n-a-b) for a in range(1,n//3+1)
                 for b in range(a,(n-a)//2+1))


def clique_stats(n):
    parts=partitions(n)
    m=len(parts)
    masks=[sum(1 << j for j,q in enumerate(parts)
               if i != j and not set(p).isdisjoint(q))
           for i,p in enumerate(parts)]
    max_size=0
    nonstar_size=0
    max_count=0
    nonstar_four=0
    max_families=[]
    maximal_count=0

    # Maximal cliques; every clique extends to a maximal clique,
    # so their largest nonstar members suffice to bound nonstars.
    def bk(R,P,X):
        nonlocal max_size,nonstar_size,max_count,nonstar_four,maximal_count,max_families
        if not P and not X:
            maximal_count += 1
            size=R.bit_count()
            common=None
            for i in range(m):
                if R>>i&1:
                    common = set(parts[i]) if common is None else common & set(parts[i])
            if not common:
                nonstar_size=max(nonstar_size,size)
                if size==4: nonstar_four +=1
            if size>max_size:
                max_size=size;max_count=1
                max_families=[tuple(parts[i] for i in range(m) if R>>i&1)]
            elif size==max_size:
                max_count+=1
                max_families.append(tuple(parts[i] for i in range(m) if R>>i&1))
            return
        px=P|X
        if px:
            v=max((i for i in range(m) if px>>i&1),key=lambda i:(P&masks[i]).bit_count())
            candidates=P &~masks[v]
        else:
            candidates=P
        while candidates:
            bit=candidates & -candidates
            i=bit.bit_length()-1
            bk(R|bit,P&masks[i],X&masks[i])
            P &=~bit; X|=bit; candidates&=~bit
    bk(0,(1<<m)-1,0)
    return {'n':n,'parts':m,'maximum':max_size,'maximal_count':maximal_count,
            'maximum_count':max_count,'nonstar_maximal_max':nonstar_size,
            'nonstar_maximal_four_count':nonstar_four,'max_families':max_families}


def check_witnesses():
    special=((1,2,5),(1,3,4),(2,2,4),(2,3,3))
    assert sum(sum(p) != 8 for p in special)==0
    assert not set.intersection(*(set(p) for p in special))
    assert all(set(p)&set(q) for i,p in enumerate(special) for q in special[:i])
    for n in range(9,101):
        F=((1,2,n-3),(1,3,n-4),(2,3,n-5),(1,4,n-5))
        assert len({tuple(sorted(x)) for x in F}) ==4
        assert all(sum(p)==n and min(p)>=1 for p in F)
        assert not set.intersection(*(set(p) for p in F))
        assert all(set(p)&set(q) for i,p in enumerate(F) for q in F[:i])
    print('WITNESSES_OK n=8..100')


def main():
    check_witnesses()
    expected={3:1,4:1,5:2,6:2,7:3,8:4}
    for n in range(3,21):
        row=clique_stats(n)
        mx=expected.get(n,(n-1)//2)
        assert row['maximum']==mx,(n,row)
        assert row['nonstar_maximal_max']<=4, row
        if n>=8: assert row['nonstar_maximal_max']==4,row
        if n==8:
            assert row['maximum_count']==1
            assert row['max_families'][0]==((1,2,5),(1,3,4),(2,2,4),(2,3,3)),row
        if n>=11:
            centers=[x for x in range(1,n) if sum(x in p for p in partitions(n))==mx]
            expected_centers=[1,2] if n%2==0 else [1]
            assert centers==expected_centers
            expected_stars={frozenset(p for p in partitions(n) if x in p) for x in centers}
            assert {frozenset(F) for F in row['max_families']}==expected_stars,row
        print('n=%02d partitions=%02d max=%02d maximal=%d max_cliques=%d nonstar=%d' %
               (n,row['parts'],row['maximum'],row['maximal_count'],row['maximum_count'],row['nonstar_maximal_max']))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
