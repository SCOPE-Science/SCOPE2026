"""Finite checks for the Johnson-graph logical-width threshold.

All configurations use actual subsets or exact nonnegative Venn-cell counts.
This code checks finite instances only; the general theorem has a separate proof.
"""
from itertools import combinations


def vertices(n, r):
    return [frozenset(a) for a in combinations(range(n), r)]


def d(a, b):
    return len(a-b)


def pair_support(n, r):
    v=vertices(n,r)
    answer={}
    for a in v:
        for b in v:
            s=d(a,b)
            profile=frozenset((d(a,c),d(b,c)) for c in v)
            if s in answer:
                assert answer[s] == profile
            else:
                answer[s]=profile
    return answer


def extend(profile, n, r):
    """Enumerate exact Venn profiles after one more r-set is chosen.

    The t-set input stores memberships in nonzero masks 1..2^t-1;
    the omitted all-zero cell has n minus the occupied union elements.
    """
    t=(len(profile)+1).bit_length()-1
    assert 2**t-1==len(profile)
    cells=(n-sum(profile),)+tuple(profile)
    out=set()
    selected=[0]*len(cells)
    def walk(i, left):
        if i==len(cells):
            if left: return
            dest=[0]*(2**(t+1)-1)
            for old, a in enumerate(cells):
                b=selected[old]
                if old:
                    dest[old-1]=a-b
                new_mask=old + 2**t
                dest[new_mask-1]=b
            out.add(tuple(dest))
            return
        for b in range(min(left,cells[i])+1):
            selected[i]=b
            walk(i+1,left-b)
    walk(0,r)
    return out


def profiles(n,r,t):
    out={()}
    for _ in range(t):
        nxt=set()
        for x in out:
            nxt.update(extend(x,n,r))
        out=nxt
    return out


def compare(n,m,r,t):
    p=profiles(n,r,t)
    q=profiles(m,r,t)
    if p!=q: return False, len(p),len(q), 'held_profile_difference'
    for a in p:
        x=extend(a,n,r); y=extend(a,m,r)
        if x!=y:
            return False,len(p),len(q),'extension_support_difference'
    return True,len(p),len(q),'all_supports_identical'


def threshold_witness(n,r,s,p):
    """Explicit witness with p or fewer r-sets, union exactly s."""
    assert 2*r < s <= p*r
    j=(s-1)//r
    i=s-j*r
    assert 2 <= j <= p-1 and 1<=i<=r
    bases=[frozenset(range(h*r,(h+1)*r)) for h in range(j)]
    extra=frozenset(list(range(r-i))+list(range(j*r,j*r+i)))
    assert len(extra)==r
    sets=bases+[extra]
    assert len(set.union(*(set(a) for a in sets)))==s
    assert all(d(a,b)==r for a,b in combinations(bases,2))
    assert d(bases[0],extra)==i
    assert all(d(b,extra)==r for b in bases[1:])


if __name__=='__main__':
    for r, near in [(2,6),(3,9)]:
        a=pair_support(near,r)
        b=pair_support(near+1,r)
        c=pair_support(near-1,r)
        assert a==b
        assert a!=c
        print(f'pair support r={r}: n={near} and {near+1} identical, n={near-1} different; {len(a)} distance classes')
    for r,p,n in [(2,4,8),(3,4,12),(3,5,15)]:
        ok,a,b,msg=compare(n,n+1,r,p-1)
        assert ok,(r,p,n,msg)
        different,*_=compare(n-1,n,r,p-1)
        assert not different
        print(f'Venn extension r={r} p={p}: n={n} and {n+1} equivalent, n={n-1} separated; {a} ordered held profiles')
    count=0
    for r in (1,2,3,4):
        for p in (3,4,5):
            for s in range(2*r+1,p*r+1):
                threshold_witness(s,r,s,p)
                count+=1
    print(f'explicit threshold witness constructions checked: {count}')
    print('VENN_VERIFICATION_OK')
