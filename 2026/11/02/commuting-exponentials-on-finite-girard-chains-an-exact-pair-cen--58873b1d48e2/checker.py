"""Finite exhaustive checks for commuting exponential floor maps on residuated chains."""
from itertools import product, combinations

def nm_multiply(n, a, b):
    return 0 if a + b <= n-1 else min(a, b)

def bang_axioms(n, mul, f):
    unit = n - 1
    if f[unit] != unit or any(f[x] > x for x in range(n)):
        return False
    if any(f[f[x]] != f[x] for x in range(n)):
        return False
    return all(mul(f[x], f[y]) == f[min(x,y)]
               for x in range(n) for y in range(n))

def floor_map(n, fixed):
    return tuple(max((s for s in fixed if s <= a), default=0)
                 for a in range(n))

def commute(f, g):
    return all(f[g[x]] == g[f[x]] for x in range(len(f)))

def nonmixed_in_common_gaps(h, a, b):
    sa = {0, h-1} | {i+1 for i in range(h-2) if a & (1 << i)}
    sb = {0, h-1} | {i+1 for i in range(h-2) if b & (1 << i)}
    common = sorted(sa & sb)
    for left, right in zip(common, common[1:]):
        if any(left < x < right for x in (sa - sb)) and \
           any(left < x < right for x in (sb - sa)):
            return False
    return True

def run():
    verified_functions = 0
    for n in range(2, 7):
        mul = lambda x,y: nm_multiply(n, x, y)
        # Check the monoid law, unit, residuation (explicit right residual).
        assert all(mul(x,n-1)==x for x in range(n))
        assert all(mul(mul(x,y),z)==mul(x,mul(y,z))
                   for x in range(n) for y in range(n) for z in range(n))
        imp = lambda x,y: max(t for t in range(n) if mul(x,t)<=y)
        assert all((mul(x,z)<=y) == (z<=imp(x,y))
                   for x in range(n) for y in range(n) for z in range(n))
        assert all(imp(imp(x,0),0)==x for x in range(n))
        E = tuple(e for e in range(n) if mul(e,e)==e)
        floors = set()
        for mask in range(1 << (len(E)-2)):
            S = (E[0], E[-1]) + tuple(E[i+1] for i in range(len(E)-2)
                                       if mask & (1 << i))
            f = floor_map(n, S)
            assert bang_axioms(n,mul,f)
            floors.add(f)
        valid = set()
        for f in product(range(n), repeat=n):
            verified_functions += 1
            if bang_axioms(n, mul, f):
                valid.add(f)
        assert valid == floors, (n,valid,floors)
        assert len(valid)==2**(len(E)-2)
    seq = []
    for h in range(2,10):
        r=h-2
        maps=[]
        for mask in range(1 << r):
            E=(0,h-1)+tuple(i+1 for i in range(r) if mask&(1<<i))
            maps.append(floor_map(h,E))
        comm_count=0
        for a,b in product(range(1<<r),repeat=2):
            is_comm = commute(maps[a],maps[b])
            assert is_comm == nonmixed_in_common_gaps(h,a,b),(h,a,b)
            if is_comm: comm_count += 1
        expected=1 if r==0 else 4 if r==1 else 4*seq[-1]-2*seq[-2]
        assert comm_count==expected,(h,comm_count,expected)
        seq.append(comm_count)
    assert seq == [1,4,14,48,164,560,1912,6528]
    print('ALL_CHECKS_OK functions_examined=%d commuting_counts=%s' % (verified_functions,seq))

if __name__=='__main__':run()
