"""Independent edge-cover enumeration of minimum dominating matchings."""
from itertools import combinations


def count(n):
    k=(n+1)//3
    universe={(i,r) for i in range(n) for r in range(2)}
    edges=[]
    for i in range(n):
        for name in ('V','T','B'):
            if name=='V':
                endpoints={(i,0),(i,1)}
            else:
                row=0 if name=='T' else 1
                endpoints={(i,row),((i+1)%n,row)}
            cover=set(endpoints)
            for x,r in endpoints:
                cover.update({((x-1)%n,r),((x+1)%n,r),(x,1-r)})
            edges.append((name,i,endpoints,cover))
    all_matches=0
    counts={}
    for picks in combinations(range(len(edges)),k):
        ends=set(); covered=set(); valid=True
        for j in picks:
            _,_,end,cover=edges[j]
            if ends & end:
                valid=False
                break
            ends.update(end)
            covered.update(cover)
        if not valid or covered != universe:
            continue
        all_matches += 1
        indices=sorted(edges[j][1] for j in picks)
        gaps=tuple(sorted((indices[(q+1)%k]-indices[q])%n for q in range(k)))
        counts[gaps]=counts.get(gaps,0)+1
    expected=n*(2*n+5)//3
    gap_type=(2,)+(3,)*(k-1)
    assert all_matches==expected,(n,all_matches,expected)
    assert counts=={gap_type:expected},(n,counts)
    print(f'n={n} edges={k} dominating_matchings={all_matches} gap_pattern={gap_type}')


if __name__=='__main__':
    for n in (5,8,11,14):count(n)
    print('VERIFY_OK')
