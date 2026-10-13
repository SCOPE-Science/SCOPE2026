"""Exact checks of graph-state two-site cut-rank moment identities.

Pure Python 3, no packages or network. Enumerates all simple labelled graphs
for 4 <= n <= 6, with an independent bit-row rank test on each cut.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def formulas(n):
    assert n >= 4
    t = Q(1, 2 ** (n - 3))
    u = 2 * t
    a = Q(1, 2 ** (n - 1))
    p = (1-t) * (1-t/2)
    overlap_cov = t * (1-t) * (1-t+t*t) / 4
    disjoint_cov = 3*u*u * (5*u*u-12*u+12) / 64
    num_pairs = comb(n,2)
    ey = num_pairs*p
    var_y = (num_pairs*p*(1-p) + 6*comb(n,3)*overlap_cov
             + 6*comb(n,4)*disjoint_cov)
    ed = num_pairs*(1-p)
    ez = n*a
    var_z = n*a + n*(n-2)*a*a
    edz = num_pairs*a*(2+(n-2)*(3*t-2*t*t))
    cov_dz = edz-ed*ez
    resid_mean = ed-(n-1)*ez
    resid_var = var_y + (n-1)**2*var_z - 2*(n-1)*cov_dz
    resid_mse = resid_var + resid_mean**2
    return locals()


def check(n):
    edges = list(combinations(range(n),2))
    index = {p:i for i,p in enumerate(edges)}
    N = 1 << len(edges)
    sum_y = sum_y2 = sum_z = sum_z2 = sum_dz = 0
    sum_overlap = sum_disjoint = 0
    allbits = (1 << n) - 1
    for graph_bits in range(N):
        rows = [0]*n
        for i,(v,w) in enumerate(edges):
            if (graph_bits >> i) & 1:
                rows[v] |= 1 << w
                rows[w] |= 1 << v
        y = 0
        ind = {}
        for v,w in edges:
            external = allbits ^ (1 << v) ^ (1 << w)
            r0 = rows[v] & external
            r1 = rows[w] & external
            success = int(bool(r0) and bool(r1) and r0 != r1)
            ind[(v,w)] = success
            y += success
        z = sum(row == 0 for row in rows)
        d = len(edges)-y
        sum_y += y
        sum_y2 += y*y
        sum_z += z
        sum_z2 += z*z
        sum_dz += d*z
        sum_overlap += ind[(0,1)]*ind[(0,2)]
        sum_disjoint += ind[(0,1)]*ind[(2,3)]
    t = formulas(n)
    empirical = {
        'ey':Q(sum_y,N),
        'var_y':Q(sum_y2,N)-Q(sum_y,N)**2,
        'ez':Q(sum_z,N),
        'var_z':Q(sum_z2,N)-Q(sum_z,N)**2,
        'edz':Q(sum_dz,N),
        'overlap_cov':Q(sum_overlap,N)-Q(sum_y,N)/len(edges)*Q(sum_y,N)/len(edges),
        'disjoint_cov':Q(sum_disjoint,N)-Q(sum_y,N)/len(edges)*Q(sum_y,N)/len(edges),
    }
    for key,actual in empirical.items():
        assert actual == t[key], (n,key,actual,t[key])
    assert t['resid_mse'] >= 0
    print(f'n={n}: {N} graphs, E(Y)={t["ey"]}, Var(Y)={t["var_y"]}, '
          f'overlap covariance={t["overlap_cov"]}, '
          f'disjoint covariance={t["disjoint_cov"]}, '
          f'isolated-residual MSE={t["resid_mse"]} [EXACT]')

def quantum_crosscheck(n, maximum=100):
    """Independently trace graph-state amplitudes for selected simple graphs."""
    edges = list(combinations(range(n),2))
    count = min(maximum, 1 << len(edges))
    for graph_bits in range(count):
        adjacency = []
        for i,edge in enumerate(edges):
            if graph_bits >> i & 1:
                adjacency.append(edge)
        def phase(z):
            return -1 if sum(((z>>v)&1)*((z>>w)&1) for v,w in adjacency)%2 else 1
        rows = [0]*n
        for v,w in adjacency:
            rows[v] |= 1 << w
            rows[w] |= 1 << v
        for v,w in edges:
            rem = [a for a in range(n) if a not in (v,w)]
            outside_mask = sum(1 << a for a in rem)
            r0,r1= rows[v]&outside_mask, rows[w]&outside_mask
            fullrank = (r0 != 0 and r1 != 0 and r0 != r1)
            exact_maxmixed = True
            for i in range(4):
                for j in range(4):
                    numer = 0
                    for z in range(1 << (n-2)):
                        base=sum(((z>>k)&1)<<a for k,a in enumerate(rem))
                        x=base+((i&1)<<v)+(((i>>1)&1)<<w)
                        y=base+((j&1)<<v)+(((j>>1)&1)<<w)
                        numer+=phase(x)*phase(y)
                    if numer != ((1 << (n-2)) if i==j else 0):
                        exact_maxmixed=False
            assert exact_maxmixed == fullrank, (n,graph_bits,v,w)
    print(f'n={n}: {count} graph-state amplitude traces agree with binary cut rank')


if __name__ == '__main__':
    for n in range(4,7):
        check(n)
        quantum_crosscheck(n)
    print('VERIFY_OK')
