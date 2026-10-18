"""Standalone finite checks for cyclic Boolean automorphism theorem. Python stdlib only."""
from itertools import product, permutations
from math import comb, factorial


def phi(n):
    return sum(1 for j in range(1,n+1) if __import__('math').gcd(n,j)==1)


def necklace_count(d,q):
    assert d>0 and q>0
    return sum(phi(r)*q**(d//r) for r in range(1,d+1) if d%r==0)//d


def expected_qf(d,m,k):
    N=necklace_count(d,2**k)
    return sum(comb(N,j) for j in range(1,min(m,N)+1))


def expected_orbit(d,m,k):
    N=necklace_count(d,2**k)
    return comb(N+m-1,m)


def canonical_necklace(w):
    return min(tuple(w[s:]+w[:s]) for s in range(len(w)))


def sigma_colors(d,m,k):
    q=1<<k
    for colors in product(range(q),repeat=d*m):
        yield colors


def minterm_type_signature(colors,d,m,k):
    # Evaluate the complete family of Boolean minterm terms at each atom.
    # A coordinate c=(j,t) satisfies the minterm specified by all 
    # sigma^s(x_i) literals exactly at its (s,i)-signature.
    mask=0
    for j in range(m):
        for t in range(d):
            word=tuple(colors[j*d+(t-s)%d] for s in range(d))
            code=sum(((word[s]>>i)&1)<<(s*k+i) for s in range(d) for i in range(k))
            mask |= 1<<code
    return mask


def support_signature(colors,d,m):
    return frozenset(canonical_necklace(list(colors[j*d:(j+1)*d])) for j in range(m))


def orbit_multiset(colors,d,m):
    return tuple(sorted(canonical_necklace(list(colors[j*d:(j+1)*d])) for j in range(m)))


def burnside(d,m,k):
    q=1<<k
    total=0; group=0
    for pi in permutations(range(m)):
        for shift in product(range(d),repeat=m):
            nxt=[0]*(d*m)
            for j in range(m):
                for t in range(d):
                    nxt[j*d+t]=pi[j]*d+(t+shift[j])%d
            seen=set(); cycles=0
            for x in range(d*m):
                if x not in seen:
                    cycles+=1; y=x
                    while y not in seen:
                        seen.add(y);y=nxt[y]
            total+=q**cycles; group+=1
    assert group==d**m*factorial(m)
    assert total%group==0
    return total//group


def main():
    cases=[(1,1),(1,2),(1,3),(1,4),(1,5),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2),(5,1)]
    assignment_checks=0; count_checks=0; burnside_checks=0
    for d,m in cases:
        for k in (1,2):
            q=1<<k
            if d*m<=8 and q**(d*m)<=80000:
                signatures=set(); supports=set(); multisets=set()
                mapping={}; reverse={}
                for colors in sigma_colors(d,m,k):
                    assignment_checks+=1
                    typ=minterm_type_signature(colors,d,m,k)
                    support=support_signature(colors,d,m)
                    multi=orbit_multiset(colors,d,m)
                    signatures.add(typ);supports.add(support);multisets.add(multi)
                    assert mapping.setdefault(typ,support)==support
                    assert reverse.setdefault(support,typ)==typ
                assert len(signatures)==len(supports)==expected_qf(d,m,k),(d,m,k,len(signatures),expected_qf(d,m,k))
                assert len(multisets)==expected_orbit(d,m,k)
                count_checks+=1
            if d*m<=10:
                assert burnside(d,m,k)==expected_orbit(d,m,k),(d,m,k)
                burnside_checks+=1
    # Distinct cycle-uniform profiles through 8 atoms: compute polynomial via exact values on q=2,4,...;
    # show two-atom collision and no other pair among enumerated uniform families.
    spec={}
    for n in range(1,9):
        for d in range(1,n+1):
            if n%d: continue
            m=n//d
            s=tuple(expected_qf(d,m,k) for k in range(1,5))
            spec[(d,m)]=s
    collisions=[]
    for a,pa in spec.items():
        for b,pb in spec.items():
            if a<b and pa==pb:
                collisions.append((a,b))
    assert collisions==[((1,2),(2,1))], collisions
    assert all(expected_qf(1,2,k)==expected_qf(2,1,k) for k in range(1,12))
    print('VERIFY_OK independent_minterm_assignments=%d minterm_case_checks=%d burnside_cases=%d 2_atom_unique_collision_through_8_atoms=PASS' % (assignment_checks,count_checks,burnside_checks))

if __name__=='__main__':main()
