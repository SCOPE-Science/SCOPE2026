"""Exact integer checks supporting the tetrahedral Fourier-support classification.

The theorem's exclusion of support sizes 5 and 7 is proved analytically;
finite searches here are corroboration, not an infinite or complex-valued proof.
"""
from itertools import product

SIGNS = tuple(s for s in product((-1, 1), repeat=3) if s[0]*s[1]*s[2] == 1)
PERMS = ((0, 1, 2), (1, 2, 0), (2, 0, 1))

def matrices():
    for perm in PERMS:
        for sign in SIGNS:
            yield tuple(tuple(sign[i] if j == perm[i] else 0 for j in range(3)) for i in range(3))

G = tuple(matrices())

def value(u, v, m):
    return sum(u[i] * m[i][j] * v[j] for i in range(3) for j in range(3))

def count_support(u, v):
    return sum(value(u,v,m)!=0 for m in G)

WITNESSES = {
    4: ((1,0,0), (1,0,0)),
    6: ((1,1,1), (1,1,0)),
    8: ((1,1,0), (1,0,0)),
    9: ((1,1,1), (2,1,1)),
    10: ((2,2,1), (2,2,1)),
    11: ((1,3,7), (1,2,-1)),
    12: ((1,1,1), (1,1,1)),
}

def multiply(a,b):
    return tuple(tuple(sum(a[i][h]*b[h][j] for h in range(3)) for j in range(3)) for i in range(3))

def run():
    assert len(G)==12 and len(set(G))==12
    assert all(multiply(a,b) in G for a in G for b in G)
    # Matrix-coefficient orthogonality: sum_g rho_ij(g)rho_kl(g)=4 delta_ik delta_jl.
    for i,j,k,l in product(range(3),repeat=4):
        lhs=sum(m[i][j]*m[k][l] for m in G)
        assert lhs == (4 if (i==k and j==l) else 0)
    for wanted,(u,v) in WITNESSES.items():
        assert count_support(u,v)==wanted,(wanted,u,v,count_support(u,v))
        # Fourier transform: sum_g f(g)rho(g)^T = 4 v u^T.
        for i,j in product(range(3),repeat=2):
            assert sum(value(u,v,m)*m[j][i] for m in G)==4*v[i]*u[j]
        # No 1-dimensional Fourier component: each V4 coset sum is zero.
        for b in range(3):
            assert sum(value(u,v,G[4*b+r]) for r in range(4))==0
        print(f'support {wanted:2d}: u={u}, v={v}; verified')
    vectors=[x for x in product((-2,-1,0,1,2),repeat=3) if x!=(0,0,0)]
    observed={count_support(u,v) for u in vectors for v in vectors}
    assert observed <= set(WITNESSES)
    print('Integer-grid corroboration, 5^3-1 vectors per side:', sorted(observed))

if __name__=='__main__':run()
