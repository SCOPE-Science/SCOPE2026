"""Exact independent check of natural-basis support spectra in binary rank-one evolution algebras."""
from itertools import product
from math import comb

def parity(x):return x.bit_count()&1

def direct_orthogonal_frames(n):
    vectors=[x for x in range(1,1<<n) if parity(x)]
    def extend(cols):
        if len(cols)==n:
            yield tuple(cols);return
        for v in vectors:
            if all(parity(v&w)==0 for w in cols):
                yield from extend(cols+[v])
    yield from extend([])

def expected(n,u):
    if u==(1<<n)-1: return {n}
    return {k for k in range(1,n) if k%2==parity(u)}

def check_direct(n):
    obs={u:set() for u in range(1,1<<n)}
    counts={u:{} for u in obs}
    number=0
    for cols in direct_orthogonal_frames(n):
        number+=1
        for u in obs:
            transformed=sum(parity(u&v)<<i for i,v in enumerate(cols))
            k=transformed.bit_count()
            obs[u].add(k)
            counts[u][k]=counts[u].get(k,0)+1
    bad={u:(obs[u],expected(n,u)) for u in obs if obs[u]!=expected(n,u)}
    assert not bad,(n,bad)
    for u in obs:
        if u==(1<<n)-1:
            assert counts[u]=={n:number}
        else:
            p=parity(u)
            denom=(1<<(n-1))-(p==0)-(p==(n&1))
            for k,cnt in counts[u].items():
                assert cnt*denom==number*comb(n,k),(n,u,k,cnt,number,denom)
    print(f'n={n} direct_frames={number} nonzero_u={len(obs)} all_spectra_verified')

def generated_orbit(n,u):
    switches=[(1<<i)|(1<<j) for i in range(n) for j in range(i+1,n)]
    # swap coordinates via bit-permutation
    fours=[sum(1<<i for i in ids) for ids in __import__('itertools').combinations(range(n),4)]
    seen={u};todo=[u]
    while todo:
        v=todo.pop()
        nxt=[]
        for sw in switches:
            # when the bits differ, swap = XOR both bits
            if parity(v&sw): nxt.append(v^sw)
        for w in fours:
            if parity(v&w): nxt.append(v^w)
        for x in nxt:
            if x not in seen:seen.add(x);todo.append(x)
    return seen

def check_generated(n):
    for u in range(1,1<<n):
        o=generated_orbit(n,u)
        s={v.bit_count() for v in o}
        assert s==expected(n,u),(n,u,s,expected(n,u))
        # the orbit actually contains *all* vectors of permitted weights
        full={v for v in range(1,1<<n) if v.bit_count() in expected(n,u)}
        assert o==full,(n,u,len(o),len(full))
    print(f'n={n} generated_orthogonal_actions all_orbits_match')

if __name__=='__main__':
    for n in range(1,6):check_direct(n)
    for n in range(1,10):check_generated(n)
    print('VERIFY_OK')
