"""Exact rational checks for the rectangular Monge inball theorem.

Standard library only. Finite verification supplements, but does not replace,
the all-size transportation-duality proof in RESULT.md.
"""
from fractions import Fraction
from math import gcd


def transport(p, q):
    n = p*q
    return [[max(0, min((i+1)*q, n-j*p) - max(i*q, n-(j+1)*p))
             for j in range(q)] for i in range(p)]


def delta(z, i, j):
    return z[i][j]+z[i+1][j+1]-z[i][j+1]-z[i+1][j]


def certificate(p, q):
    n = p*q
    lam = transport(p, q)
    assert all(sum(lam[i]) == q for i in range(p))
    assert all(sum(lam[i][j] for i in range(p)) == p for j in range(q))
    parents = list(range(p+q))
    def find(a):
        while parents[a] != a:
            parents[a] = parents[parents[a]]
            a = parents[a]
        return a
    edges = []
    for i in range(p):
        for j in range(q):
            if lam[i][j]:
                a, b = find(i), find(p+j)
                assert a != b, ('unexpected cycle', p, q)
                parents[a] = b
                edges.append((i,j))
    assert len(edges) == p+q-gcd(p,q)
    # Equality potentials for cost c_ij=ij on the positive support.
    a = [None]*p
    b = [None]*q
    for i0 in range(p):
        if a[i0] is not None:
            continue
        a[i0] = 0
        changed = True
        while changed:
            changed = False
            for i,j in edges:
                if a[i] is not None and b[j] is None:
                    b[j] = i*j-a[i]
                    changed=True
                if b[j] is not None and a[i] is None:
                    a[i] = i*j-b[j]
                    changed=True
    assert all(t is not None for t in a+b)
    cmps = {v:find(v) for v in range(p+q)}
    labels = {z:k for k,z in enumerate(sorted(set(cmps.values())))}
    ci = [labels[cmps[i]] for i in range(p)]
    cj = [labels[cmps[p+j]] for j in range(q)]
    g = len(labels)
    assert g == gcd(p,q)
    # Dual potentials may shift independently between support components.
    # Tiny strict slack on every unused transport cell shows full face dimension.
    eps = Fraction(1,n+1)
    constraints=[]
    for i in range(p):
        for j in range(q):
            slack = Fraction(i*j-a[i]-b[j])
            if lam[i][j]:
                assert slack==0
                continue
            assert ci[i]!=cj[j] or slack>=eps
            if ci[i]!=cj[j]:
                constraints.append((cj[j],ci[i],slack-eps))
    dist=[Fraction(0) for _ in range(g)]
    for _ in range(g):
        changed=False
        for u,v,w in constraints:
            if dist[v] > dist[u]+w:
                dist[v]=dist[u]+w
                changed=True
        if not changed:break
    assert not any(dist[v]>dist[u]+w for u,v,w in constraints)
    y=[[Fraction(i*j-a[i]-b[j])-dist[ci[i]]+dist[cj[j]] for j in range(q)]
       for i in range(p)]
    for i in range(p):
        for j in range(q):
            assert y[i][j]==0 if lam[i][j] else y[i][j]>=eps, (p,q,i,j)
    assert all(delta(y,i,j)==1 for i in range(p-1) for j in range(q-1))
    t=sum(min(u*v,(p-u)*(q-v)) for u in range(1,p) for v in range(1,q))
    anti=sum(i*j*lam[i][j] for i in range(p) for j in range(q))
    independent=sum(i*j for i in range(p) for j in range(q))
    assert t == independent-anti == sum(sum(row) for row in y)
    # Each Monge-sum lower-bound weight is positive.
    for u in range(1,p):
        for v in range(1,q):
            high=sum(lam[i][j] for i in range(u,p) for j in range(v,q))
            assert (p-u)*(q-v)-high == min(u*v,(p-u)*(q-v))>0
    return t, len(edges), g


def main():
    count=0
    for p in range(2,13):
        for q in range(2,13):
            t,e,g=certificate(p,q)
            if p==q:
                assert t==p*p*(p*p-1)//12
            if p==2:
                assert t==q*q//4
            count+=1
    for p,q in [(2,3),(3,4),(4,6),(5,7),(6,9),(8,12)]:
        t,e,g=certificate(p,q)
        print(f'({p},{q}) T={t} support_edges={e} incenter_dimension={g-1}')
    print('RECTANGULAR_MONGE_CERTIFICATES_OK cases=',count)

if __name__=='__main__':
    main()
