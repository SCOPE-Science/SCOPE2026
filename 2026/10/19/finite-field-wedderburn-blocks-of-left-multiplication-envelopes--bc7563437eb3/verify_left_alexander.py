"""Finite matrix-rank checks for the left multiplication envelope of Latin Alexander quandle algebras.

Execute using: python3 verify_left_alexander.py
Only finite cases are tested; the accompanying proof covers the general theorem.
"""
from itertools import product
from math import gcd


def orbit_partition(items, step):
    remaining = set(items)
    ans = []
    while remaining:
        start = min(remaining)
        orbit = []
        x = start
        while x not in orbit:
            assert x in remaining, (start, x, orbit)
            orbit.append(x)
            remaining.remove(x)
            x = step(x)
        assert x == start
        ans.append(tuple(orbit))
    return ans


def matrix_rank_mod_p(rows, p):
    basis = {}
    for row in rows:
        v = dict(row)
        while v:
            i = min(v)
            if i not in basis:
                scalar = pow(v[i], -1, p)
                basis[i] = {k: x*scalar % p for k,x in v.items() if x*scalar % p}
                break
            w = basis[i]
            c = v[i]
            for k,a in w.items():
                tmp = (v.get(k, 0) - c*a) % p
                if tmp: v[k] = tmp
                elif k in v: del v[k]
    return len(basis)


def cyclic(n, beta, q):
    assert gcd(n,q)==gcd(n,beta)==gcd(n,1-beta)==1
    chars = list(range(n))
    orbits = orbit_partition(chars, lambda x: (beta*x)%n)
    orbit_map = {x:i for i,orb in enumerate(orbits) for x in orb}
    assert len(orbit_map)==n
    full_dim = sum(len(orb)**2 for orb in orbits)
    index_cycles = orbit_partition(list(range(len(orbits))), lambda i: orbit_map[(q*orbits[i][0])%n])
    blocks = sorted((len(orbits[cyc[0]]),len(cyc)) for cyc in index_cycles)
    assert sum(t*t*f for t,f in blocks)==full_dim
    order = 1
    while pow(beta,order,n)!=1: order+=1
    rows=[]
    for j in range(order):
        b=pow(beta,j,n)
        for a in range(n):
            rows.append({x*n+((a+b*x)%n):1 for x in range(n)})
    p = next(k for k in range(2,q+1) if q%k==0 and all(k%d for d in range(2,int(k**0.5)+1)))
    rank=matrix_rank_mod_p(rows,p)
    assert rank==full_dim,(n,beta,q,rank,full_dim)
    print(f'C_{n}, beta={beta}, q={q}, group={n*order}, rank={rank}, blocks={blocks}')
    return rank,blocks


def matmul(a,b,p):
    return ((a[0]*b[0]+a[1]*b[2])%p,(a[0]*b[1]+a[1]*b[3])%p,
            (a[2]*b[0]+a[3]*b[2])%p,(a[2]*b[1]+a[3]*b[3])%p)


def matrix_noncyclic(p, beta, q):
    # p is an odd prime; G=F_p^2. The coefficient field has characteristic different from p.
    assert p in (2,3,5)
    det=(beta[0]*beta[3]-beta[1]*beta[2])%p
    alpha=((1-beta[0])%p,-beta[1]%p,-beta[2]%p,(1-beta[3])%p)
    det_a=(alpha[0]*alpha[3]-alpha[1]*alpha[2])%p
    assert det and det_a and q%p
    elements=list(product(range(p),repeat=2))
    ind={x:i for i,x in enumerate(elements)}
    def image(M,x):return ((M[0]*x[0]+M[1]*x[1])%p,(M[2]*x[0]+M[3]*x[1])%p)
    # Dual action of beta is beta^T; powers of inverse have identical orbits.
    transpose=(beta[0],beta[2],beta[1],beta[3])
    chars=orbit_partition(elements,lambda x:image(transpose,x))
    dim=sum(len(x)**2 for x in chars)
    C={a:i for i,O in enumerate(chars) for a in O}
    orbit_indices=orbit_partition(list(range(len(chars))),lambda i:C[tuple(q*v%p for v in chars[i][0])])
    blocks=sorted((len(chars[O[0]]),len(O)) for O in orbit_indices)
    assert sum(t*t*f for t,f in blocks)==dim
    mat=(1,0,0,1); powers=[]
    while mat not in powers:
        powers.append(mat)
        mat=matmul(beta,mat,p)
    assert mat==(1,0,0,1)
    rows=[]
    for mat in powers:
        for a in elements:
            rows.append({i*len(elements)+ind[((image(mat,x)[0]+a[0])%p,(image(mat,x)[1]+a[1])%p)]:1 for i,x in enumerate(elements)})
    prime=next(k for k in range(2,q+1) if q%k==0 and all(k%d for d in range(2,int(k**0.5)+1)))
    rank=matrix_rank_mod_p(rows,prime)
    assert rank==dim,(p,beta,q,rank,dim)
    print(f'(C_{p})^2, beta={beta}, q={q}, rank={rank}, blocks={blocks}')


def main():
    cases=[(3,2,2),(3,2,5),(5,2,2),(5,2,3),(5,4,2),(5,4,3),
           (7,2,2),(7,2,3),(7,2,4),(7,2,9),(7,3,2),(7,4,5),(9,2,2),(9,2,5),
           (11,2,2),(11,2,3),(13,2,2)]
    for c in cases: cyclic(*c)
    assert cyclic(7,2,2)[1] == [(1,1),(3,1),(3,1)]
    assert cyclic(7,2,3)[1] == [(1,1),(3,2)]
    matrix_noncyclic(2,(0,1,1,1),3)
    matrix_noncyclic(2,(0,1,1,1),5)
    matrix_noncyclic(3,(2,0,0,2),2)
    matrix_noncyclic(3,(0,1,1,1),2)
    matrix_noncyclic(3,(0,1,1,1),5)
    print('PASS: 19 cyclic configurations (including 2 repeated checks) and five noncyclic configurations')

if __name__=='__main__':main()
