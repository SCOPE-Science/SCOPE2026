"""Reproduce spectral and metric checks for symmetric-design incidence graphs.

Requires Python 3 and NumPy; optional SciPy for root solving is not used.
Run: python verify.py
"""
import collections
import math
import numpy as np


def plane_incidence(prime):
    """Points and lines are 1-dimensional and 2-dimensional F_p subspaces."""
    p = prime
    vectors = [(a, b, c) for a in range(p) for b in range(p)
               for c in range(p) if (a, b, c) != (0, 0, 0)]
    def canon(x):
        z = next(y for y in x if y % p)
        inv = pow(z, -1, p)
        return tuple((y*inv) % p for y in x)
    pts = sorted(set(map(canon, vectors)))
    # Every nonzero triple represents a line ax+by+cz=0.
    lines = pts
    return np.array([[int(sum(a*b for a,b in zip(point,line)) % p == 0)
                     for line in lines] for point in pts], dtype=int)


def cyclic_design(v, offsets):
    return np.array([[int((j-i) % v in offsets) for j in range(v)]
                     for i in range(v)], dtype=int)


def spectral_prediction(v,k,lam,p):
    a=2.0**p; b=3.0**p
    s=math.sqrt(k-lam)
    return (-a-(b-1)*s, -a+(b-1)*s,
            a*(v-1)-b*(v-k)-k)


def p_s(r):
    lo=0.; hi=1.
    for _ in range(85):
        mid=(lo+hi)/2
        if math.sqrt(r)*(3.**mid-1)>2.**mid: hi=mid
        else: lo=mid
    return (lo+hi)/2


def p_global(v,k,lam):
    ps=p_s(k-lam)
    def g(p):return (v-1)*2.**p-(v-k)*3.**p-k
    if g(ps)<=1.e-10:return None
    lo=0.; hi=ps
    for _ in range(85):
        mid=(lo+hi)/2
        if g(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2


def check(N,tag):
    v=len(N); k=int(sum(N[0])); lam=int((N@N.T)[0,1]); r=k-lam
    assert k>=3 and r>=2
    assert np.array_equal(N@N.T,r*np.eye(v,dtype=int)+lam*np.ones((v,v),dtype=int))
    assert np.all(N.sum(axis=0)==k)
    # Independently build the graph's true distances by BFS.
    graph=[[] for _ in range(2*v)]
    for i in range(v):
        for j in range(v):
            if N[i,j]:
                graph[i].append(v+j);graph[v+j].append(i)
    distances=np.zeros((2*v,2*v),dtype=int)
    for source in range(2*v):
        dist={source:0}; queue=collections.deque([source])
        while queue:
            u=queue.popleft()
            for w in graph[u]:
                if w not in dist:dist[w]=dist[u]+1;queue.append(w)
        assert len(dist)==2*v
        for w,t in dist.items():distances[source,w]=t
    J=np.ones((v,v)); I=np.eye(v)
    exact=np.block([[2*(J-I),3*J-2*N],[3*J-2*N.T,2*(J-I)]])
    assert np.array_equal(distances,exact)
    B=np.linalg.svd(N,compute_uv=False)
    assert abs(B[0]-k)<1.e-7 and np.max(np.abs(B[1:]-math.sqrt(r)))<1.e-7
    ps=p_s(r); pg=p_global(v,k,lam)
    crit=min(ps,pg if pg is not None else 100)
    E=np.eye(2*v)-np.ones((2*v,2*v))/(2*v)
    for p in [0,0.2*crit,0.6*crit,0.99*crit,crit,crit+0.03]:
        powered=distances.astype(float)**p
        # At p=0, off-diagonal entries become 1; zero diagonal by definition.
        np.fill_diagonal(powered,0)
        ev=np.linalg.eigvalsh(E@powered@E)[1:] # remove one zero constant eigenvalue (not necessarily smallest)
        all_ev=np.linalg.eigvalsh(E@powered@E)
        pred=spectral_prediction(v,k,lam,p)
        expected=np.sort(np.array([pred[0]]*(v-1)+[pred[1]]*(v-1)+[pred[2]]+[0]))
        assert np.max(np.abs(all_ev-expected))<5.e-8,(tag,p,np.max(np.abs(all_ev-expected)))
        if p<crit-1e-5: assert max(pred[1],pred[2]) < -1.e-6
        if p>crit+1e-5: assert max(pred[1],pred[2]) > 1.e-5
    s=math.sqrt(r); u=2**ps
    phase='global' if u>(k+s)/(k-1)+1.e-8 else 'spectral' if u<(k+s)/(k-1)-1.e-8 else 'resonant'
    if phase=='global':assert pg is not None and pg<ps
    if phase=='spectral':assert pg is None
    pred=spectral_prediction(v,k,lam,crit)
    nullity=(v-1 if abs(pred[1])<1e-8 else 0)+(1 if abs(pred[2])<1e-8 else 0)
    rank=2*v-1-nullity
    print(f'{tag}: v={v},k={k},lambda={lam},r={r},phase={phase}, p*={crit:.12f}, zero-sum nullity={nullity}, affine rank={rank}')


def main():
    for q in (2,3,5,7):
        N=plane_incidence(q)
        check(N,f'PG(2,{q}) incidence')
        check(1-N,f'PG(2,{q}) complementary design')
    R={1,3,4,5,9}
    N=cyclic_design(11,R)
    check(N,'cyclic symmetric (11,5,2)')
    check(1-N,'complementary (11,6,3)')
    print('All 10 full-graph BFS, singular-spectrum, powered-distance and endpoint checks passed.')

if __name__=='__main__':main()
