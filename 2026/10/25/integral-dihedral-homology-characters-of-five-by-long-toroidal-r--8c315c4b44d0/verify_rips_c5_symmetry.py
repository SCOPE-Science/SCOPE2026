#!/usr/bin/env python3
"""Exact test of dihedral homology traces for scale-two Rips complexes of 5-by-n grids.

The all-width proof uses a periodic simplicial collapse to two-column blocks;
this finite verifier separately checks the local orientation characters and
signed simplicial Lefschetz formula on complete complexes.
"""
from itertools import product
from verify_rips_c5_cylinder import two_column_faces,full_torus_faces,local_octahedron_certificate,check_uniform_global_collapses


def signed_face_lefschetz(vertices, faces, transform):
    lookup={v:i for i,v in enumerate(vertices)}
    p={i:lookup[transform(v)] for i,v in enumerate(vertices)}
    total=0
    for f in faces:
        w=[p[i] for i in f]
        if sorted(w)!=list(f):continue
        sign=(-1)**sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))
        total+=(-1)**(len(f)-1)*sign
    return total


def predicted_local(row_reflect,swap):
    return (-1)**(row_reflect+swap)


def check_local():
    verts,faces=two_column_faces()
    k=0
    for row_sign,rotation,colswap in product((1,-1),range(5),(0,1)):
        transform=lambda v: ((row_sign*v[0]+rotation)%5, (1-v[1] if colswap else v[1]))
        assert signed_face_lefschetz(verts,faces,transform)-1 == predicted_local(row_sign==-1,colswap)
        k+=1
    print(f'{k} complete local dihedral signed-Lefschetz checks passed')


def fixed_blocks(n,d,reflect):
    if not reflect: return n if d%n==0 else 0
    return sum((2*b+1-d)%n==0 for b in range(n))


def check_global(n):
    verts,faces=full_torus_faces(n)
    count=0
    for rs,ra,cs,ca in product((1,-1),range(5),(1,-1),range(n)):
        transform=lambda v:((rs*v[0]+ra)%5,(cs*v[1]+ca)%n)
        tr_h1=cs
        tr_h2=(rs*cs)*fixed_blocks(n,ca,cs==-1)
        predicted=1-tr_h1+tr_h2
        actual=signed_face_lefschetz(verts,faces,transform)
        assert actual == predicted,(n,rs,ra,cs,ca,predicted,actual)
        count+=1
    print(f'C5 x C{n}: {count} full-complex signed-Lefschetz comparisons agree with the complete homology character')


def main():
    local_octahedron_certificate()
    check_local()
    for n in (7,8,9,10): check_uniform_global_collapses(n)
    for n in (7,8,9): check_global(n)
    print('Every exact test passed; infinite-family assertions use uniform collapse and integral naturality.')

if __name__=='__main__':main()
