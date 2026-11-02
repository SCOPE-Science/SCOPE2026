"""Self-contained checks for edge-incidence shattering by minimal edge covers."""
from itertools import combinations
from functools import lru_cache


def edges(a,b):
    return [(i,j) for i in range(a) for j in range(b)]


def is_minimal_cover(a,b,S):
    da=[0]*a; db=[0]*b
    for i,j in S:
        da[i]+=1; db[j]+=1
    return min(da)>0 and min(db)>0 and all(da[i]==1 or db[j]==1 for i,j in S)


def witness(a,b,chosen):
    assert a>=3 and b>=3
    base={(0,j) for j in range(2,b)}|{(i,0) for i in range(2,a)}|{(1,1)}
    assert chosen<=base
    i_empty={i for i in range(2,a) if (i,0) not in chosen}
    j_empty={j for j in range(2,b) if (0,j) not in chosen}
    J={j for j in range(2,b) if (0,j) in chosen}
    I={i for i in range(2,a) if (i,0) in chosen}
    S=set(chosen)
    if (1,1) not in chosen:
        S.update((i,1) for i in i_empty)
        S.update((1,j) for j in j_empty)
        if not J or not i_empty:S.add((0,1))
        if not I or not j_empty:S.add((1,0))
    else:
        if j_empty:
            if i_empty:
                jstar=min(j_empty)
                S.update((i,jstar) for i in i_empty)
                S.update((1,j) for j in j_empty if j!=jstar)
            else:
                S.update((1,j) for j in j_empty)
        else:
            S.update((i,1) for i in i_empty)
        if not J or not I:S.add((0,0))
    assert S&base==chosen, (a,b,chosen,S)
    assert is_minimal_cover(a,b,S), (a,b,chosen,S)
    return S


def verify_constructive():
    checks=0
    for a in range(3,8):
        for b in range(3,8):
            base=sorted(({(0,j) for j in range(2,b)} |
                         {(i,0) for i in range(2,a)} | {(1,1)}))
            assert len(base)==a+b-3
            for m in range(1<<len(base)):
                chosen={e for p,e in enumerate(base) if m>>p&1}
                witness(a,b,chosen)
                checks+=1
    print('THREE_COMPONENT_ALL_TRACES_PASS', 'cases',checks)


def brute_family(a,b):
    E=edges(a,b); C=[]
    for m in range(1<<len(E)):
        S={e for p,e in enumerate(E) if m>>p&1}
        if is_minimal_cover(a,b,S):C.append(m)
    return E,C


def vc_dimension(E,C):
    m=len(E)
    last=0
    for k in range(1,m+1):
        found=False
        for support in combinations(range(m),k):
            traces=set()
            for h in C:
                t=sum(((h>>p)&1)<<idx for idx,p in enumerate(support))
                traces.add(t)
                if len(traces)==1<<k:break
            if len(traces)==1<<k:
                found=True;break
        if not found:return last
        last=k
    return last


def ldim(E,C):
    Q=[sum((1<<t) for t,x in enumerate(C) if x>>p&1) for p in range(len(E))]
    full=(1<<len(C))-1
    @lru_cache(None)
    def supports(H,k):
        if k==0:return True
        if H.bit_count() < (1<<k):return False
        if k==1:return H.bit_count()>=2
        for q in Q:
            left=H&q;right=H&~q
            if left.bit_count() <(1<<(k-1)) or right.bit_count() < (1<<(k-1)):continue
            if supports(left,k-1) and supports(right,k-1):return True
        return False
    d=0
    while supports(full,d+1):d+=1
    return d


def verify_finite():
    for a,b in [(1,3),(2,2),(2,3),(2,4),(2,5),(2,6),
                (3,3),(3,4),(3,5),(4,4)]:
        E,C=brute_family(a,b)
        target=0 if a==1 else a+b-3
        assert vc_dimension(E,C)==target,(a,b,target)
        if len(C)<=200:
            rank=ldim(E,C)
            assert rank>=target
            print('FINITE_CENSUS_PASS',a,b,'minimal_covers',len(C),'VC',target,'Ldim',rank)
        else:print('FINITE_CENSUS_PASS',a,b,'minimal_covers',len(C),'VC',target)


if __name__=='__main__':
    verify_constructive()
    verify_finite()
    print('ALL_MINIMAL_EDGE_COVER_SHATTERING_CHECKS_PASS')
