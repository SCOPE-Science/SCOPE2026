"""Independent finite-generator checks for exclusion/reaction count covariance formulas.

Requires numpy and scipy. Exact proofs are in RESULT.md; numerical tests are not proofs.
"""
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply


def validate_graph(vertex_count, edges, birth, death, lags=(0.17, 0.81)):
    """edges = [(tail, head, forward_rate, reverse_rate, observed), ...]."""
    n = vertex_count
    count = 1 << n
    rows, cols, vals = [], [], []
    ar, ac, av = [], [], []
    dr, dc, dv = [], [], []
    jr, jc, jv = [], [], []
    balance = np.zeros(n)
    bias = 0.0
    for u, v, p, q, observed in edges:
        balance[u] += p - q
        balance[v] -= p - q
        if observed:
            bias += p - q
    assert np.max(np.abs(balance)) < 1.e-12
    for state in range(count):
        departure = 0.0
        for i in range(n):
            target = state ^ (1 << i)
            occupied = bool(state & (1 << i))
            rate = death if occupied else birth
            rows.append(state); cols.append(target); vals.append(rate)
            departure += rate
            rr, cc, vv = (dr, dc, dv) if occupied else (ar, ac, av)
            rr.append(state); cc.append(target); vv.append(rate)
        for u, v, p, q, observed in edges:
            occ_u = bool(state & (1 << u))
            occ_v = bool(state & (1 << v))
            if occ_u == occ_v:
                continue
            target = state ^ (1 << u) ^ (1 << v)
            rate = p if occ_u else q
            rows.append(state); cols.append(target); vals.append(rate)
            departure += rate
            if observed:
                jr.append(state); jc.append(target); jv.append(rate * (1 if occ_u else -1))
        rows.append(state); cols.append(state); vals.append(-departure)
    shape = (count, count)
    qmat = csr_matrix((vals, (rows, cols)), shape=shape)
    amat = csr_matrix((av, (ar, ac)), shape=shape)
    dmat = csr_matrix((dv, (dr, dc)), shape=shape)
    jmat = csr_matrix((jv, (jr, jc)), shape=shape)
    rho = birth / (birth + death)
    omega = birth + death
    pi = np.array([rho ** state.bit_count() *
                  (1-rho) ** (n-state.bit_count()) for state in range(count)])
    one = np.ones(count)
    assert np.max(np.abs(pi @ qmat)) < 2.e-12
    mean_j = float(pi @ jmat @ one)
    assert abs(mean_j - bias * rho * (1-rho)) < 2.e-12
    checks = 0
    for lag in lags:
        # Expectations evaluated from the complete Markov generator, not from
        # the sector-averaged Ehrenfest model used in the proof.
        row_j = expm_multiply(lag*qmat, jmat @ one)
        row_a = expm_multiply(lag*qmat, amat @ one)
        row_d = expm_multiply(lag*qmat, dmat @ one)
        means = {"A":float(pi @ amat @ one), "D":float(pi @ dmat @ one)}
        for label, mat, first_coefficient, second_coefficient, row in (
            ("A", amat, birth*bias*(1-rho)**2*(1-2*rho),
             -birth*bias*rho*(1-rho)*(1-2*rho), row_a),
            ("D", dmat, -death*bias*rho**2*(1-2*rho),
             death*bias*rho*(1-rho)*(1-2*rho), row_d)):
            fwd = float(pi @ mat @ row_j) - means[label]*mean_j
            rev = float(pi @ jmat @ row) - means[label]*mean_j
            scale = np.exp(-omega*lag)
            for actual, expected in [(fwd, first_coefficient*scale),
                                     (rev, second_coefficient*scale)]:
                assert abs(actual - expected) <= 2.e-9*(1+abs(expected)), (label, actual, expected)
                checks += 1
    return checks, bias, rho


def torus_edges(nx=3, ny=3):
    idx = lambda x,y: (x % nx)*ny + (y % ny)
    px, qx = [.9, 1.3, .7], [.2, .3, .1]
    py, qy = [.5, 1., .4], [.2, .25, .1]
    edges=[]
    for x in range(nx):
        for y in range(ny):
            edges.append((idx(x,y),idx(x+1,y),px[y],qx[y],True))
            edges.append((idx(x,y),idx(x,y+1),py[x],qy[x],False))
    return edges


def cycle_edges(n=5):
    # A nonrectangular balanced directed transport network.
    edges=[(i,(i+1)%n, .8 + .1*i, .6 + .1*i, i in (0,1,2)) for i in range(n)]
    # A second, disjoint cycle circulation on a triangle.
    edges.extend([(0,2,.5,.2,False),(2,4,.55,.25,True),(4,0,.65,.35,True)])
    return edges

if __name__ == '__main__':
    total=0
    for birth, death in [(0.4,0.6),(0.6,0.4),(0.5,0.5)]:
        checks, bias, rho = validate_graph(9,torus_edges(),birth,death)
        total+=checks
        print('torus: rho=%.2f, summed bias=%.3f, %d checks passed' % (rho,bias,checks))
    for birth, death in [(0.3,0.7),(0.7,0.3)]:
        checks,bias,rho=validate_graph(5,cycle_edges(),birth,death)
        total+=checks
        print('balanced cycle network: rho=%.2f, bias=%.3f, %d checks passed' % (rho,bias,checks))
    print('PASS: %d complete-generator event-covariance checks.' % total)
