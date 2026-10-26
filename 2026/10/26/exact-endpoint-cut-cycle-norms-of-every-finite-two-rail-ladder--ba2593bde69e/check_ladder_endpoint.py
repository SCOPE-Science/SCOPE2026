"""Exact rational verification of edge cut/cycle column formulas for finite ladders.
Run with Python 3 and SymPy installed: python check_ladder_endpoint.py
"""
from sympy import Matrix, Rational, zeros, eye


def run():
    graphs = 0
    checked_columns = 0
    for n in range(2, 13):
        edges = []
        for j in range(n):
            edges.append((j, n + j, 'rung', j))
        for j in range(n - 1):
            for layer in range(2):
                edges.append((layer * n + j, layer * n + j + 1, 'rail', j))
        D = zeros(2*n, len(edges))
        for e, (a,b,_,_) in enumerate(edges):
            D[a,e] = 1
            D[b,e] = -1
        grounded = (D * D.T)[:2*n-1, :2*n-1]
        inv = grounded.inv()
        full = zeros(2*n, 2*n)
        full[:2*n-1,:2*n-1] = inv
        Q = D.T * full * D
        P = eye(len(edges)) - Q
        path_lap = zeros(n,n)
        for j in range(n-1):
            path_lap[j,j] += 1
            path_lap[j+1,j+1] += 1
            path_lap[j,j+1] -= 1
            path_lap[j+1,j] -= 1
        R = (path_lap + 2*eye(n)).inv()
        qcols = []
        pcols = []
        for e,(u,v,kind,j) in enumerate(edges):
            q = sum(abs(Q[f,e]) for f in range(len(edges)))
            p = sum(abs(P[f,e]) for f in range(len(edges)))
            if kind == 'rung':
                q_expected = 1+4*R[j,j]-2*(R[0,j]+R[n-1,j])
                p_expected = 2-2*(R[0,j]+R[n-1,j])
            else:
                g=R[:,j]-R[:,j+1]
                s=g[j]-g[j+1]
                z=g[0]-g[n-1]
                q_expected = 2-z
                p_expected = 2-s-z
            assert q == q_expected, ('cut-column', n, kind, j, q, q_expected)
            assert p == p_expected, ('cycle-column', n, kind, j, p, p_expected)
            qcols.append(q)
            pcols.append(p)
            checked_columns+=1
        central = (n-1)//2
        qmax = 1+4*R[central,central]-2*(R[0,central]+R[n-1,central])
        pmax = 2-2*(R[0,central]+R[n-1,central])
        assert max(qcols)==qmax
        assert max(pcols)==pmax
        assert qmax>pmax
        qm={e for e,q in enumerate(qcols) if q==qmax}
        pm={e for e,p in enumerate(pcols) if p==pmax}
        if n==2:
            assert qm==pm==set(range(len(edges)))
        else:
            centers={central,n-central-1}
            assert qm==pm==centers
        graphs += 1
    print(f'LADDER_ENDPOINT_EXACT_OK graphs={graphs} checked_projection_columns={checked_columns}')

if __name__=='__main__':
    run()
