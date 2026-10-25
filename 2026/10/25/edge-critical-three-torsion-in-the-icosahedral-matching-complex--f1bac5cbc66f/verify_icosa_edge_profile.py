#!/usr/bin/env python3
"""Exact Morse, determinant, and symmetry certificates for the icosahedron.
The only dependency is Python 3.9+ standard library. All cells are generated.
"""
from collections import Counter, deque
from functools import lru_cache
from fractions import Fraction


def graph_edges():
    E=set()
    def add(a,b): E.add(tuple(sorted((a,b))))
    for i in range(5):
        u=1+i;v=6+i
        add(0,u);add(11,v)
        add(u,1+(i+1)%5);add(v,6+(i+1)%5)
        add(u,v);add(u,6+(i-1)%5)
    E=sorted(E)
    assert len(E)==30 and Counter(z for e in E for z in e)=={i:5 for i in range(12)}
    # Verify its canonical planar triangulation: 20 triangles, 2 per edge.
    tri=[(a,b,c) for a in range(12) for b in range(a+1,12)
         for c in range(b+1,12) if all(tuple(sorted(t)) in E for t in ((a,b),(b,c),(a,c)))]
    assert len(tri)==20
    assert all(sum(a in t and b in t for t in tri)==2 for a,b in E)
    return E


def edge_transitivity(E):
    adj=[set() for _ in range(12)]
    for a,b in E:adj[a].add(b);adj[b].add(a)
    perm=[-1]*12; unused=set(range(12));images=set();num=[0]
    def rec():
        if not unused:
            num[0]+=1;images.add(tuple(sorted((perm[E[0][0]],perm[E[0][1]]))))
            return
        x=max((v for v in range(12) if perm[v]<0),
              key=lambda v:sum(perm[z]>=0 for z in adj[v]))
        for y in sorted(unused):
            if all(((z in adj[x]) == (perm[z] in adj[y])) for z in range(12) if perm[z]>=0):
                perm[x]=y;unused.remove(y);rec();unused.add(y);perm[x]=-1
    rec()
    assert num[0]==120 and images==set(E)
    return num[0],len(images)


def simplices(E):
    out=set()
    def rec(j,occupied,face):
        if face:out.add(face)
        for i in range(j,len(E)):
            a,b=E[i]; mask=(1<<a)|(1<<b)
            if mask&occupied==0:rec(i+1,occupied|mask,face|(1<<i))
    rec(0,0,0)
    return out


def signed_faces(mask):
    for j,i in enumerate(i for i in range(mask.bit_length()) if mask>>i&1):
        yield mask^(1<<i), (-1 if j%2 else 1)


def morse(E,d,expected_counts,expected_critical,expected_pairs,expected_incidences):
    cells=simplices(E)
    counts=Counter(mask.bit_count()-1 for mask in cells)
    assert tuple(counts[k] for k in range(len(expected_counts)))==expected_counts
    remaining=set(cells);lohi={};hilo={}
    for pivot in range(len(E)):
        bit=1<<pivot
        for low in sorted(remaining):
            high=low|bit
            if high!=low and low in remaining and high in remaining:
                assert low in cells and high in cells and low.bit_count()+1==high.bit_count()
                remaining.remove(low);remaining.remove(high)
                lohi[low]=high;hilo[high]=low
    assert len(lohi)==expected_pairs
    critical={k:sorted(z for z in remaining if z.bit_count()-1==k) for k in range(6)}
    assert tuple(len(critical[k]) for k in range(6))==expected_critical
    assert set(lohi).isdisjoint(hilo)
    # Exhaustive directed Hasse graph; matched incidences reversed.
    incoming={f:0 for f in cells};outgoing={f:[] for f in cells};incident=0
    for high in cells:
        for low,_ in signed_faces(high):
            if low==0:continue
            src,dst=(low,high) if lohi.get(low)==high else (high,low)
            outgoing[src].append(dst);incoming[dst]+=1;incident+=1
    assert incident==expected_incidences
    queue=deque(f for f in cells if incoming[f]==0);seen=0
    while queue:
        x=queue.popleft();seen+=1
        for y in outgoing[x]:
            incoming[y]-=1
            if incoming[y]==0:queue.append(y)
    assert seen==len(cells)
    idx={m:i for i,m in enumerate(critical[d])}
    @lru_cache(None)
    def project(mask):
        if mask in remaining:return {idx[mask]:1}
        if mask in hilo:return {}
        upper=lohi[mask]
        oriented=list(signed_faces(upper))
        hit=next(s for f,s in oriented if f==mask)
        ans={}
        for other,sgn in oriented:
            if other==mask:continue
            for j,z in project(other).items():
                ans[j]=ans.get(j,0)-hit*sgn*z
        return {j:z for j,z in ans.items() if z}
    columns=[]
    for upper in critical[d+1]:
        result={}
        for lower,sgn in signed_faces(upper):
            for i,z in project(lower).items():result[i]=result.get(i,0)+sgn*z
        columns.append({i:z for i,z in result.items() if z})
    mat=[[col.get(i,0) for col in columns] for i in range(len(critical[d]))]
    return mat,critical,counts,incident


def select_independent_rows(M):
    basis={};indices=[];n=len(M[0])
    for i,row in enumerate(M):
        R={k:Fraction(v) for k,v in enumerate(row) if v}
        while R:
            p=min(R)
            if p not in basis:
                v=R[p];basis[p]={j:z/v for j,z in R.items()};indices.append(i);break
            multiple=R[p]
            for j,z in basis[p].items():
                w=R.get(j,0)-multiple*z
                if w:R[j]=w
                elif j in R:del R[j]
        if len(indices)==n:break
    return tuple(indices)


def rational_rank_rows(M):
    basis={}
    for row in M:
        R={j:Fraction(z) for j,z in enumerate(row) if z}
        while R:
            p=min(R)
            if p not in basis:
                v=R[p];basis[p]={j:z/v for j,z in R.items()};break
            a=R[p]
            for j,z in basis[p].items():
                w=R.get(j,0)-a*z
                if w:R[j]=w
                elif j in R:del R[j]
    return len(basis)


def rank_mod(M,p):
    basis={}
    for row in M:
        R={j:z%p for j,z in enumerate(row) if z%p}
        while R:
            a=min(R)
            if a not in basis:
                v=pow(R[a],-1,p)
                basis[a]={j:(z*v)%p for j,z in R.items()};break
            multiple=R[a]
            for j,z in basis[a].items():
                w=(R.get(j,0)-multiple*z)%p
                if w:R[j]=w
                elif j in R:del R[j]
    return len(basis)


def determinant_bareiss(M):
    N=[list(row) for row in M];n=len(N)
    assert all(len(row)==n for row in N)
    sign=1;divisor=1
    for k in range(n-1):
        if N[k][k]==0:
            other=next((i for i in range(k+1,n) if N[i][k]),None)
            if other is None:return 0
            N[k],N[other]=N[other],N[k];sign=-sign
        pivot=N[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=N[i][j]*pivot-N[i][k]*N[k][j]
                assert numerator%divisor==0
                N[i][j]=numerator//divisor
        for i in range(k+1,n):N[i][k]=0
        divisor=pivot
    return sign*N[-1][-1]


def main():
    E=graph_edges();removed=E[0];assert removed==(0,1)
    order,orbit=edge_transitivity(E)
    allcases=[
        ('whole',E,3,(30,315,1400,2535,1482,125),(1,0,0,125,61,0),2850,23130),
        ('edge_deleted',E[1:],3,(29,294,1260,2197,1235,100),(1,0,0,96,28,0),2495,19931),
        ('edge_link',[e for e in E if not set(e).intersection(removed)],2,(21,140,338,247,25),(1,0,9,13,0,0),374,2407)]
    complexes=[]
    for label,edges,d,fc,critical,pairs,inc in allcases:
        M,cr,count,hs=morse(edges,d,fc,critical,pairs,inc)
        rational=rational_rank_rows(M)
        rank3=rank_mod(M,3)
        if label=='edge_link':
            assert (len(M),len(M[0]),rational,rank3)==(9,13,7,7)
            # Canonical 7x7 minor using exact independent columns and rows.
            cols=select_independent_rows(list(map(list,zip(*M))))
            assert len(cols)==7
            rowset=select_independent_rows([[M[i][j] for j in cols] for i in range(len(M))])
            assert len(rowset)==7
            det=determinant_bareiss([[M[i][j] for j in cols] for i in rowset])
            assert abs(det)==1
            minor=(rowset,cols)
        else:
            assert len(M[0])==rational
            rowset=select_independent_rows(M)
            det=determinant_bareiss([M[i] for i in rowset])
            assert len(rowset)==len(M[0])
            if label=='whole':
                assert (rational,rank3,abs(det))==(61,60,3)
            else:
                assert (rational,rank3,abs(det))==(28,28,1)
            minor=(rowset,tuple(range(len(M[0]))))
        print('CASE',label,'SIMPLICES',fc,'MATCHES',pairs,
              'CRITICAL',critical,'MORSE_DIM',len(M),len(M[0]),
              'Q_RANK',rational,'F3_RANK',rank3,'MINOR_DET',det)
        print('MINOR_CERTIFICATE',label,'ROWS',minor[0],'COLUMNS',minor[1])
        complexes.append(simplices(edges))
    assert sum(bool(face&1) for face in complexes[0])==772
    assert all((face<<1) in complexes[0] for face in complexes[1])
    assert len(complexes[2])==771
    index={e:i for i,e in enumerate(E)}
    link_edges=allcases[2][1]
    for f in complexes[2]:
        lifted=1|sum(1<<index[link_edges[i]] for i in range(len(link_edges)) if f>>i&1)
        assert lifted in complexes[0]
    print('ICOSAHEDRAL_AUTOMORPHISMS',order,'EDGE_ORBIT',orbit)
    print('HOMOTOPY_TYPES', 'whole: 64 S3 plus Moore(Z/3,3)',
          'deleted: 68 S3', 'link: 2 S2 plus 6 S3')
    print('NONPRIMITIVE_CONNECTING_IMAGE_INDEX',3)
    print('VERIFY_OK_ICOSAHEDRAL_EDGE_TORSION_PROFILE')

if __name__=='__main__':main()
