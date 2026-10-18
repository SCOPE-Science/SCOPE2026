#!/usr/bin/env python3
"""Direct congruence-extension census for one-point Boolean perturbations."""
from itertools import combinations

def partitions(xs):
    if not xs:
        yield []
        return
    first, rest=xs[0],xs[1:]
    for blocks in partitions(rest):
        yield [[first]]+[x[:] for x in blocks]
        for j in range(len(blocks)):
            new=[x[:] for x in blocks]
            new[j].append(first)
            yield new

def bitset(elements):
    z=0
    for t in elements:z|=1<<t
    return z

def algebra_congruence_ideals(carrier,f):
    """Return all principal ideals defining operation-compatible Boolean congruences.
       Caller supplies a Boolean subalgebra as a tuple of underlying universe subsets."""
    return {J for J in carrier if all((f[x]^f[y]) &~J == 0 for x in carrier for y in carrier if (x^y)&~J == 0)}

def test_one(n,S,T):
    full=(1<<n)-1
    f={x: (x|T if x==S else x) for x in range(1<<n)}
    all_elements=tuple(range(1<<n))
    ambient=algebra_congruence_ideals(all_elements,f)
    expected_ambient={0}|{J for J in all_elements if (J&T)==T}
    assert ambient==expected_ambient,(n,S,T,ambient,expected_ambient)
    for pi in partitions(list(range(n))):
        atoms=[bitset(b) for b in pi]
        carrier=tuple(bitset(t for j,b in enumerate(pi) if (q>>j)&1 for t in b) for q in range(1<<len(pi)))
        if any(f[x] not in carrier for x in carrier): continue
        local=algebra_congruence_ideals(carrier,f)
        for I in local:
            if not any({x for x in carrier if x&~J==0}=={x for x in carrier if x&~I==0} for J in ambient):
                return False,('partition',pi,'nonextending_ideal',I)
    return True,None

def main():
    for n in range(2,6):
        all_n=(1<<n)-1
        proven=0; refuted=0
        orbit_types=set(); cep_orbit_types=set()
        for S in range(1<<n):
            for T in range(1<<n):
                if T==0 or T&S:continue
                got,witness=test_one(n,S,T)
                kind=(S.bit_count(),T.bit_count())
                orbit_types.add(kind)
                if got:cep_orbit_types.add(kind)
                expected= S==0 or (S!=0 and S.bit_count()==n-1)
                assert got==expected,(n,S,T,got,expected,witness)
                if got:proven+=1
                else:refuted+=1
        assert proven==2**n+n-1,(n,proven)
        assert proven+refuted==3**n-2**n
        assert len(orbit_types)==n*(n+1)//2
        assert len(cep_orbit_types)==n+1
        print(f'n={n}: CEP={proven}, nonCEP={refuted}, total={proven+refuted}')
    print('ONE_POINT_BOOLEAN_CEP_CENSUS_OK')
if __name__=='__main__':main()
