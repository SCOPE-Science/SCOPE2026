#!/usr/bin/env python3
"""Alternate cubical-incidence construction and simplicial-field homology checks."""
from collections import Counter,defaultdict


def cubical_incidence():
    # Separate integer-bit model, with original cube vertices as 0..7.
    # The other side is made of six coordinate hyperplanes.
    E=[]
    for side in range(6):
        axis=side//2; fixed=side%2
        for corner in range(8):
            if ((corner>>axis)&1)==fixed:
                E.append((corner,8+side))
    return tuple(sorted(E))


def enumerate_matchings(E):
    by_degree=defaultdict(list)
    def rec(index,occupied,selection):
        if index==len(E):
            if selection:by_degree[len(selection)-1].append(tuple(selection))
            return
        rec(index+1,occupied,selection)
        u,v=E[index]
        if occupied&(1<<u|1<<v)==0:
            selection.append(index)
            rec(index+1,occupied|(1<<u)|(1<<v),selection)
            selection.pop()
    rec(0,0,[])
    return by_degree


def matrix_rank_mod2(columns, row_map):
    pivot={}
    for face in columns:
        vec=0
        for j in range(len(face)):
            vec^=1<<row_map[face[:j]+face[j+1:]]
        while vec:
            lead=vec.bit_length()-1
            if lead not in pivot:
                pivot[lead]=vec
                break
            vec^=pivot[lead]
    return len(pivot)


def matrix_rank_mod3(columns,row_map):
    pivot={}
    for face in columns:
        x={row_map[face[:j]+face[j+1:]]:(1 if j%2==0 else 2) for j in range(len(face))}
        while x:
            lead=max(x)
            if lead not in pivot:
                c=x[lead]
                if c==2:x={i:(2*v)%3 for i,v in x.items()}
                pivot[lead]=x
                break
            basis=pivot[lead]
            fac=x[lead]
            for i,v in basis.items():
                nv=(x.get(i,0)-fac*v)%3
                if nv:x[i]=nv
                else:x.pop(i,None)
    return len(pivot)


def case(name,E,expected):
    simplices=enumerate_matchings(E)
    dims=max(simplices)
    face_counts=[len(simplices[d]) for d in range(dims+1)]
    boundary2=[0]+[matrix_rank_mod2(simplices[d],{f:i for i,f in enumerate(simplices[d-1])}) for d in range(1,dims+1)]+[0]
    boundary3=[0]+[matrix_rank_mod3(simplices[d],{f:i for i,f in enumerate(simplices[d-1])}) for d in range(1,dims+1)]+[0]
    betti2=[face_counts[d]-boundary2[d]-boundary2[d+1]-(1 if d==0 else 0) for d in range(dims+1)]
    betti3=[face_counts[d]-boundary3[d]-boundary3[d+1]-(1 if d==0 else 0) for d in range(dims+1)]
    assert betti2==betti3==expected, (name,betti2,betti3,expected)
    print(f'{name}: counts={face_counts} ranks_F2={boundary2[1:-1]} ranks_F3={boundary3[1:-1]} reduced_betti_F2={betti2} reduced_betti_F3={betti3}')

def main():
    full=cubical_incidence()
    assert len(full)==24 and len(set(full))==24
    e=full[0]
    assert e==(0,8)
    assert Counter(u for edge in full for u in edge)[0]==3
    case('full',full,[0,0,0,0,39,0])
    case('delete',tuple(f for f in full if f!=e),[0,0,0,0,26,0])
    case('link',tuple(f for f in full if all(x not in f for x in e)),[0,0,0,13,0])
    print('FIELD_CROSSCHECK_OK')

if __name__=='__main__':main()
