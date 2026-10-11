"""Independent finite tests for graph Cech nerves of projective-plane incidence graphs.

Run: python3 verify_projective_cech.py
Requires only the Python 3 standard library. All graph edges have length one.
"""
from itertools import combinations
from collections import deque, Counter


def projective_points(p):
    ans = set()
    for a in range(p):
        for b in range(p):
            for c in range(p):
                triple = (a,b,c)
                if triple != (0,0,0):
                    first = next(x for x in triple if x)
                    inv = pow(first,-1,p)
                    ans.add(tuple(x*inv%p for x in triple))
    return sorted(ans)


def plane(p):
    pts = projective_points(p)
    lines = projective_points(p)
    N = len(pts)
    incidence = [(i,j) for i,u in enumerate(pts) for j,v in enumerate(lines)
                 if sum(x*y for x,y in zip(u,v))%p == 0]
    assert N==p*p+p+1 and len(incidence)==N*(p+1)
    E = set(incidence)
    for i in range(N):
        assert sum((i,j) in E for j in range(N))==p+1
        assert sum((j,i) in E for j in range(N))==p+1
    for i,j in combinations(range(N),2):
        assert sum((i,k) in E and (j,k) in E for k in range(N))==1
        assert sum((k,i) in E and (k,j) in E for k in range(N))==1
    return N,E


def generate_faces(facets):
    faces = set()
    for F in facets:
        s = F
        while s:
            faces.add(s)
            s = (s-1)&F
    return faces


def mod2_betti(faces):
    dim = max(m.bit_count() for m in faces)-1
    groups = [[f for f in faces if f.bit_count()==k+1] for k in range(dim+1)]
    ranks = []
    for k in range(1,dim+1):
        index = {face:i for i,face in enumerate(groups[k-1])}
        basis = {}
        for face in groups[k]:
            b = face
            v=0
            while b:
                bit=b&-b
                v ^= 1<<index[face^bit]
                b -= bit
            while v:
                top=v.bit_length()-1
                if top in basis: v ^= basis[top]
                else:
                    basis[top]=v
                    break
        ranks.append(len(basis))
    betti = [len(groups[0])-1-ranks[0]] if dim else [len(groups[0])-1]
    betti += [len(groups[k])-ranks[k-1]-(ranks[k] if k < dim else 0)
              for k in range(1,dim+1)]
    return tuple(len(group) for group in groups),tuple(ranks),tuple(betti)


def collapse_line_complex(N,E,side):
    neighborhoods=[]
    for center in range(N):
        if side=='point':
            verts=[i for i in range(N) if (i,center) in E]
        else:
            verts=[i for i in range(N) if (center,i) in E]
        neighborhoods.append(verts)
    faces=generate_faces([sum(1<<i for i in v) for v in neighborhoods])
    initial=set(faces)
    pairs=0
    for vert in neighborhoods:
        anchor=min(vert)
        others=[v for v in vert if v!=anchor]
        for k in range(len(others),1,-1):
            for sub in combinations(others,k):
                low=sum(1<<i for i in sub)
                high=low|(1<<anchor)
                assert low in faces and high in faces
                assert not any(z not in (low,high) and z&low==low for z in faces), 'not free'
                faces.remove(low)
                faces.remove(high)
                pairs+=1
    assert all(z.bit_count()<=2 for z in faces)
    assert len([z for z in faces if z.bit_count()==2])==N*(len(neighborhoods[0])-1)
    assert len([z for z in faces if z.bit_count()==1])==N
    assert pairs==N*(2**(len(neighborhoods[0])-1)-len(neighborhoods[0]))
    return initial,faces,pairs


def run(p):
    N,E=plane(p)
    neighbors=[[] for _ in range(2*N)]
    for i,j in E:
        neighbors[i].append(N+j)
        neighbors[N+j].append(i)
    distances=[]
    for src in range(2*N):
        ds=[None]*(2*N)
        ds[src]=0
        queue=deque([src])
        while queue:
            u=queue.popleft()
            for v in neighbors[u]:
                if ds[v] is None:
                    ds[v]=ds[u]+1
                    queue.append(v)
        distances.append(ds)
    assert max(max(d) for d in distances)==3
    computed_facets={sum(1<<i for i,d in enumerate(row) if d<=2) for row in distances}
    expected_facets=set()
    for i in range(N):
        expected_facets.add(sum(1<<v for v in range(N)) | sum(1<<(N+j) for j in range(N) if (i,j) in E))
        expected_facets.add(sum(1<<(N+j) for j in range(N)) | sum(1<<v for v in range(N) if (v,i) in E))
    assert computed_facets==expected_facets
    assert len(computed_facets)==2*N
    ap0,ap,_=collapse_line_complex(N,E,'point')
    al0,al,_=collapse_line_complex(N,E,'line')
    assert len(ap0)==N*(2**(p+1)-p-1)
    assert len(al0)==len(ap0)
    # Check K = A union B and A cap B = J_P * J_L on every possible face for p=2.
    if p==2:
        A=generate_faces([F for F in computed_facets if F&((1<<N)-1)==(1<<N)-1])
        B=generate_faces([F for F in computed_facets if F>>N==(1<<N)-1])
        K=A|B
        factors={x|(y<<N) for x in ap0|{0} for y in al0|{0}}-{0}
        assert A&B==factors
        f,r,b=mod2_betti(K)
        assert b==(0,0,0,0,p**6,0,0,0,0,0), (f,r,b)
        assert sum((-1)**i*ct for i,ct in enumerate(f))==1+p**6
        print('q=2:',len(K),'simplices, f=',f,'boundary ranks=',r,'reduced betti=',b)
    # Independent graph cycle ranks of both collapsed collinearity complexes.
    expected_cycle=N*p-N+1
    assert expected_cycle==p**3
    for X in (ap,al):
        verts=sum(x.bit_count()==1 for x in X)
        edges=sum(x.bit_count()==2 for x in X)
        assert edges-verts+1==p**3
    print('q=',p,'points/lines=',N,'Čech facets=',len(computed_facets),
          'auxiliary cycle ranks=',p**3,'predicted sphere count=',p**6)


if __name__=='__main__':
    for p in (2,3): run(p)
    print('VERIFY_OK')
