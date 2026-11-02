"""Exact four-round first-order type comparison of small symplectic polar graphs.

Only equality and the adjacency relation B(u,v)=0 are visible.
The routine computes root four-types by recording full atomic extension sets
of ordered triples. Fixing the first point is valid because the symplectic
group is transitive on projective points. These are finite checks; the
field-uniform theorem is proved separately by linear algebra.
"""
import itertools


def multiply(a, b, q):
    if q != 4:
        return a*b % q
    # GF(4)=F_2[t]/(t^2+t+1), represented by 0,1,t,t+1.
    z = 0
    if b & 1: z ^= a
    if b & 2: z ^= a << 1
    if z & 8: z ^= 0b1100
    if z & 4: z ^= 0b111
    return z


def points(q, d):
    # Projective representatives have first nonzero coordinate equal to one.
    for x in itertools.product(range(q), repeat=2*d):
        if x and any(x) and x[next(i for i,t in enumerate(x) if t)] == 1:
            yield x


def form(u, v, q, d):
    if q == 4:
        return __import__('functools').reduce(
            int.__xor__, (multiply(u[i],v[i+d],q)^multiply(u[i+d],v[i],q)
                           for i in range(d)), 0)
    return sum(u[i]*v[i+d]-u[i+d]*v[i] for i in range(d)) % q


def root_type(q,d):
    v=list(points(q,d));n=len(v)
    a=[]
    for x in v:
        a.append(sum(1<<j for j,y in enumerate(v)
                     if x!=y and form(x,y,q,d)==0))
    universe=(1<<n)-1
    pairs4=tuple(itertools.combinations(range(4),2))
    pairs3=tuple(itertools.combinations(range(3),2))
    def atom4(t):
        return (tuple(int(t[i]==t[j]) for i,j in pairs4),
                tuple(int(bool(a[t[i]]&(1<<t[j]))) for i,j in pairs4))
    def atom3(t):
        return (tuple(int(t[i]==t[j]) for i,j in pairs3),
                tuple(int(bool(a[t[i]]&(1<<t[j]))) for i,j in pairs3))
    outcome=set()
    for y in range(n):
        atom2=(int(y==0), int(bool(a[0]&(1<<y))))
        triple_types=set()
        for z in range(n):
            rest=universe & ~(1 | 1<<y | 1<<z)
            masks=[]
            for mask in range(8):
                candidates=rest
                for bit,k in enumerate((0,y,z)):
                    candidates &= a[k] if (mask>>bit)&1 else (universe^a[k])
                masks.append(int(bool(candidates)))
            equals=tuple(sorted(set(atom4((0,y,z,w)) for w in (0,y,z))))
            triple_types.add((atom3((0,y,z)),tuple(masks),equals))
        outcome.add((atom2,frozenset(triple_types)))
    return frozenset(outcome),n

def main():
    cases=[(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2),(7,2)]
    types={}
    for q,d in cases:
        types[q,d],n=root_type(q,d)
        assert n == (q**(2*d)-1)//(q-1)
        print(f"MODEL q={q} d={d} vertices={n} rooted_two_types={len(types[q,d])}")
    for a,b in itertools.combinations(cases,2):
        expected=(a[0]==2)==(b[0]==2) and (a[1]==2)==(b[1]==2)
        assert (types[a]==types[b]) == expected, (a,b)
    print("ALL_28_PAIRWISE_RANK4_COMPARISONS_OK")
    print("FOUR_REPRESENTATIVE_CLASSES_OK")
    print("VERIFY_OK")

if __name__=='__main__': main()
