#!/usr/bin/env python3
"""Exact combinatorial checks for the twisted hexagonal two-ring filtration."""
from itertools import combinations
from collections import Counter

N=12
LABEL_BY_GAP={1:'O1',2:'E2',3:'O3',4:'E4',5:'O5',6:'E6'}

def complex_for(labels):
    labels=set(labels)
    edges={(a,b) for a in range(N) for b in range(a+1,N)
           if LABEL_BY_GAP[min(b-a,N-b+a)] in labels}
    out=set()
    for mask in range(1,1<<N):
        vertices=[i for i in range(N) if mask & (1<<i)]
        if all((a,b) in edges for a,b in combinations(vertices,2)):
            out.add(mask)
    return out

def f_vector(K):
    c=Counter(z.bit_count()-1 for z in K)
    return [c[k] for k in range(max(c)+1)]

def boundary_matrices(K):
    cells={k:sorted(m for m in K if m.bit_count()==k+1)
           for k in range(12)}
    cells={k:v for k,v in cells.items() if v}
    dd={}
    for k in range(1,max(cells)+1):
        ix={m:i for i,m in enumerate(cells[k-1])}
        d=[[0 for _ in cells[k]] for _ in cells[k-1]]
        for j,mask in enumerate(cells[k]):
            vv=[i for i in range(N) if mask>>i&1]
            for pos,i in enumerate(vv):
                d[ix[mask^(1<<i)]][j]=1 if pos%2==0 else -1
        dd[k]=d
    return [len(cells.get(k,[])) for k in range(max(cells)+1)],dd

def eliminate_unit_entries(K):
    # Integral cellular cancellation with pivot +/-1. All arithmetic is exact.
    dimensions,mats=boundary_matrices(K)
    pivots=0
    while True:
        choices=[]
        for k,M in mats.items():
            for i,row in enumerate(M):
                for j,p in enumerate(row):
                    if abs(p)==1:
                        nzrow=sum(bool(x) for x in row)
                        nzcol=sum(bool(M[q][j]) for q in range(len(M)))
                        choices.append(((nzrow-1)*(nzcol-1),k,i,j))
        if not choices:break
        _,k,i,j=min(choices)
        M=mats[k];p=M[i][j]
        col=[M[u][j] for u in range(len(M))]
        row=M[i][:]
        mats[k]=[[M[u][v]-p*col[u]*row[v]
                  for v in range(len(row)) if v!=j]
                 for u in range(len(M)) if u!=i]
        if k-1 in mats:
            mats[k-1]=[rr[:i]+rr[i+1:] for rr in mats[k-1]]
        if k+1 in mats:
            mats[k+1]=mats[k+1][:j]+mats[k+1][j+1:]
        dimensions[k]-=1;dimensions[k-1]-=1;pivots+=1
    assert all(x==0 for M in mats.values() for row in M for x in row), 'nonzero boundary left'
    return {k:v for k,v in enumerate(dimensions) if v},pivots

def relative_collapse(big,small):
    s=set(big);witness=[]
    while s!=small:
        co={}
        for face in s:
            for vertex in range(N):
                if face&(1<<vertex):
                    sub=face^(1<<vertex)
                    if sub in s and sub not in small:
                        co.setdefault(sub,[]).append(face)
        pairs=[(x,upper[0]) for x,upper in co.items()
               if len(upper)==1 and upper[0] not in small]
        if not pairs:break
        x,y=max(pairs,key=lambda q:(q[1].bit_count(),q[0]))
        assert x in s and y in s and x not in small and y not in small
        assert (y^x).bit_count()==1 and x.bit_count()+1==y.bit_count()
        assert not any(z!=y and z!=x and z&x==x for z in s),'not a free face'
        s.remove(x);s.remove(y);witness.append((x,y))
    assert s==small, (len(s),len(small))
    return len(witness)

def pi1_reduction(K):
    edges={x for x in K if x.bit_count()==2}
    triangles=sorted(x for x in K if x.bit_count()==3)
    seen={0};tree=set()
    while len(seen)<N:
        options=[(v,w) for v in sorted(seen) for w in range(N)
                 if w not in seen and (1<<v)|(1<<w) in edges]
        assert options,'not connected'
        v,w=min(options);tree.add((1<<v)|(1<<w));seen.add(w)
    known=set(tree)
    while True:
        nextedge=None
        for tri in triangles:
            bd=[tri^(1<<a) for a in range(N) if tri&(1<<a)]
            unknown=[x for x in bd if x not in known]
            if len(unknown)==1:
                nextedge=unknown[0];break
        if nextedge is None:break
        known.add(nextedge)
    assert known==edges, (len(known),len(edges))
    return len(tree),len(edges)-len(tree)

ROWS=[
 ('', [12],None),
 ('O1',[12,12],None),
 ('E2',[12,12],None),
 ('E2 E4',[12,24,16],None),
 ('E2 O1',[12,24,12],None),
 ('E2 E4 E6',[12,30,40,30,12,2],None),
 ('E2 E4 O1',[12,36,28],{0:1,2:3}),
 ('E2 O1 O3',[12,36,36,12],None),
 ('E2 E4 E6 O1',[12,42,52,30,12,2],{0:1,2:1}),
 ('E2 E4 O1 O3',[12,48,76,48,12],None),
 ('E2 E4 E6 O1 O3',[12,54,112,105,36,2],None),
 ('E2 E4 O1 O3 O5',[12,60,160,240,192,64],None),
 ('E2 E4 E6 O1 O3 O5',[12,66,220,495,792,924,792,495,220,66,12,1],None)
]

def main():
    for lab,face_counts,critical in ROWS:
        K=complex_for(lab.split())
        assert f_vector(K)==face_counts,(lab,f_vector(K),face_counts)
        if critical is not None:
            actual,pairs=eliminate_unit_entries(K)
            assert actual==critical,(lab,actual)
            pi1_reduction(K)
            print('HOMOLOGY_PI1',lab,actual,'unit_cancellations',pairs)
    c={lab:complex_for(lab.split()) for lab,_,_ in ROWS}
    assert relative_collapse(c['E2 O1'],c['O1'])==12
    assert relative_collapse(c['E2 O1 O3'],c['E2 O1'])==24
    assert relative_collapse(c['E2 E4 O1 O3'],c['E2 E4 O1'])==60
    print('RELATIVE_COLLAPSES',12,24,60)
    # Every distinct-wall ordering or coincidence yields one of the stated 13 complexes.
    from math import sqrt
    walls=[2-sqrt(3),sqrt(3)-1,1.0,2.0,1+sqrt(3),2+sqrt(3)]
    test=[walls[0]/2]+[(a+b)/2 for a,b in zip(walls,walls[1:])]+[walls[-1]+1]+walls
    allowed={frozenset(x.split()) for x,_,_ in ROWS}
    for t in test:
        sq={'O1':2-sqrt(3)+t,'E2':1,'O3':2+t,'E4':3,'E6':4,'O5':2+sqrt(3)+t}
        for radius_squared in sorted(set(sq.values())):
            labels={k for k,v in sq.items() if v<=radius_squared+1e-9}
            assert frozenset(labels) in allowed,(t,labels)
    print('CLASS_TABLE',len(ROWS),'STATE_CHECKS_OK')
    print('VERIFY_OK')
if __name__=='__main__':main()
