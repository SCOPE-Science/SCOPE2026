#!/usr/bin/env python3
"""Independent enumerator for the pure discrete-Morse complex of a cycle.

Uses only the Python standard library. Enumerates rooted spanning-path
orientations, their faces, and signed fixed-simplex Lefschetz traces.
"""
from itertools import combinations
from math import comb


def maximal_faces(n):
    answer=set()
    for removed in range(n):
        order=[(removed+1+i)%n for i in range(n)]
        for root in range(n):
            face=[]
            for i,v in enumerate(order):
                if i==root:
                    continue
                w=order[i+1 if i<root else i-1]
                edge=v if w==(v+1)%n else w
                incidence=2*edge+(0 if edge==v else 1)
                face.append(incidence)
            answer.add(tuple(sorted(face)))
    assert len(answer)==n*n
    return sorted(answer)


def all_faces(facets):
    return set(sub for f in facets for k in range(len(f)+1) for sub in combinations(f,k))


def act(n,j,reflect):
    # Reflection x -> j-x and rotation x -> j+x.
    permutation=[]
    for i in range(n):
        e=(j-i-1)%n if reflect else (j+i)%n
        permutation.extend((2*e+(1 if reflect else 0),
                            2*e+(0 if reflect else 1)))
    return permutation


def signed_fixed_face(face, permutation):
    mapped=[permutation[x] for x in face]
    if set(mapped)!=set(face):
        return 0
    inv=sum(a>b for i,a in enumerate(mapped) for b in mapped[i+1:])
    return -1 if inv%2 else 1


def lefschetz(faces,permutation):
    total=0
    for f in faces:
        sign=signed_fixed_face(f,permutation)
        if sign:
            total+=((-1) if (len(f)%2==0) else 1)*sign
    return total


def reflection_polynomial(faces,n,j=0):
    p=act(n,j,True)
    coeff=[0]*(n+1)
    for f in faces:
        if all(p[x] in f for x in f):
            assert len(f)%2==0
            coeff[len(f)//2]+=1
    return coeff


def run():
    for n in range(5,12):
        facets=maximal_faces(n)
        faces=all_faces(facets)
        assert max(len(f) for f in faces)==n-1
        for j in range(n):
            p=act(n,j,False)
            actual=lefschetz(faces,p)
            top=2 if (n%2 or j%2==0) else -2
            expect=1+((-1)**(n-2))*top
            assert actual==expect,(n,j,actual,expect)
            ps=act(n,j,True)
            assert lefschetz(faces,ps)==1,(n,j)
            coef=reflection_polynomial(faces,n,j)
            a=(n-2)//2
            b=(n-2)-a
            wanted=[comb(a,k)+comb(b,k)-(1 if k==0 else 0)
                    for k in range(n+1)]
            assert coef==wanted,(n,j,coef,wanted)
        even=tuple(range(0,2*n,2))
        odd=tuple(range(1,2*n,2))
        for simplex in (even,odd):
            assert simplex not in faces
            assert all(tuple(simplex[:i]+simplex[i+1:]) in faces for i in range(n))
        print(f'n={n} faces={len(faces)} facets={len(facets)} dihedral_elements={2*n} passed')
    print('PASS: signed equivariant enumeration and reflection fixed-face formula')

if __name__=='__main__':
    run()
