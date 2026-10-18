"""Replays three exact integer minor witnesses for rook-graph neighborhood complexes.

Only uses Python's standard library. The certificates are self-contained.
"""
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent

def data(m, n):
    N = m*n
    pairs = list(combinations(range(1,N),2))
    index = {p:i for i,p in enumerate(pairs)}
    faces = set()
    for r in range(m):
        for c in range(n):
            neighbors= sorted({r*n+j for j in range(n) if j!=c} |
                              {i*n+c for i in range(m) if i!=r})
            faces.update(combinations(neighbors,3))
    return pairs,index,sorted(faces)

def boundary(tri,index):
    a,b,c=tri
    result={}
    for edge,sgn in (((a,b),1),((a,c),-1),((b,c),1)):
        if edge[0]!=0:
            result[index[edge]]=sgn
    return result

def determinant(M):
    # Exact fraction-free Gaussian elimination, including row pivoting.
    a=[row[:] for row in M];n=len(a)
    if n==0:return 1
    prev=1;sign=1
    for k in range(n-1):
        if a[k][k]==0:
            alt=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if alt is None:return 0
            a[k],a[alt]=a[alt],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            factor=a[i][k]
            for j in range(k+1,n):
                num=a[i][j]*pivot-factor*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def theta(i,j):
    if i==j:return 0
    return 1 if (j-i)%3==1 else -1

def row_cochain(u,v):
    return theta(u[0],v[0])*(-2 if u[1]==v[1] else 1)

def col_cochain(u,v):
    return row_cochain((u[1],u[0]),(v[1],v[0]))

def evaluate_cycle(pts,form):
    return sum(form(pts[i],pts[(i+1)%len(pts)]) for i in range(len(pts)))

def verify():
    cs=json.loads((HERE/'base_certificates.json').read_text())['cases']
    for name in ['3x3','3x4','4x4']:
        item=cs[name];m=item['m'];n=item['n'];pairs,index,faces=data(m,n)
        face_set=set(faces)
        selected_faces=[tuple(x) for x in item['faces']]
        assert len(set(selected_faces))==len(selected_faces)
        assert all(tri in face_set for tri in selected_faces)
        selected_rows=[tuple(x) for x in item.get('rows',pairs)]
        assert len(set(selected_rows))==len(selected_rows)
        assert all(p in index for p in selected_rows)
        rows=[index[p] for p in selected_rows];loc={r:i for i,r in enumerate(rows)}
        d=len(rows);assert d==len(selected_faces)
        M=[[0]*d for _ in range(d)]
        for j,tri in enumerate(selected_faces):
            for i,coef in boundary(tri,index).items():
                if i in loc:M[loc[i]][j]=coef
        det=determinant(M)
        assert det==item['det'],(name,det,item['det'])
        assert d=={'3x3':26,'3x4':54,'4x4':105}[name]
        print(name,'vertices',m*n,'triangles',len(faces), 'minor_order',d,'det',det)
        if m==3:
            forms=[row_cochain]+([col_cochain] if n==3 else [])
            for form in forms:
                for tri in faces:
                    a,b,c=[(i//n,i%n) for i in tri]
                    assert form(a,b)+form(b,c)+form(c,a)==0,(name,tri)
            rowscycle=[(i,0) for i in range(3)]
            assert evaluate_cycle(rowscycle,row_cochain)==-6
            if n==3:
                colscycle=[(0,j) for j in range(3)]
                assert evaluate_cycle(colscycle,col_cochain)==-6
                assert evaluate_cycle(rowscycle,col_cochain)==0
                assert evaluate_cycle(colscycle,row_cochain)==0
        else:
            def mod2(u,v):return int(u[0]!=v[0] and u[1]!=v[1])
            for tri in faces:
                a,b,c=[(i//n,i%n) for i in tri]
                assert (mod2(a,b)+mod2(b,c)+mod2(c,a))%2==0
            assert sum(mod2(*edge) for edge in [((0,0),(0,1)),((0,1),(1,1)),((1,1),(0,0))])%2==1
    # Additional finite checks of the inductive link-connectivity hypothesis.
    for m,n in [(3,k) for k in range(4,9)]+[(a,b) for a in range(4,8) for b in range(4,8)]:
        N={(i,j):({(i,k) for k in range(n) if k!=j}|{(k,j) for k in range(m) if k!=i}) for i in range(m) for j in range(n)}
        def linked(x,u,v):return bool(N[x]&N[u]&N[v])
        startrows=3 if m==3 else 4
        base=[(i,j) for i in range(startrows) for j in range(4)]
        order=(base+([(i,j) for i in range(4,m) for j in range(4)] if m>3 else [])+
               [(i,j) for j in range(4,n) for i in range(m)])
        previous=base[:]
        for x in order[len(base):]:
            reached={previous[0]}
            while True:
                extended=reached|{u for u in previous if any(linked(x,u,v) for v in reached)}
                if extended==reached:break
                reached=extended
            assert len(reached)==len(previous),(m,n,x)
            previous.append(x)
    print('LINK_CHECK_OK; CERTIFICATE_VERIFY_OK')
if __name__=='__main__':verify()
