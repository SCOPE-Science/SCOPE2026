"""Independent combinatorial homology check for the Paley(17) neighborhood complex.

Constructs faces from intersections of vertex-neighbor sets, not by taking
subsets of maximal faces. Uses sparse modular Gaussian elimination.
Run: python verify_modular.py
"""
from collections import Counter

N = 17
NONZERO_SQUARES = {((a*a) % N) for a in range(1, N)}
HOODS = [sum(1 << j for j in range(N) if (j - i) % N in NONZERO_SQUARES)
         for i in range(N)]


def reconstruct_faces():
    all_vertices = (1 << N) - 1
    common = [0] * (1 << N)
    common[0] = all_vertices
    faces = [[] for _ in range(8)]
    for s in range(1, 1 << N):
        lowbit = s & (-s)
        vertex = lowbit.bit_length()-1
        common[s] = common[s ^ lowbit] & HOODS[vertex]
        if common[s]:
            faces[s.bit_count()-1].append(s)
    return faces


def signed_boundary(simplex):
    sign = 1
    for v in range(N):
        bit = 1 << v
        if simplex & bit:
            yield simplex ^ bit, sign
            sign = -sign


def boundary_rank(faces_lower, faces_upper, p):
    index = {s: i for i, s in enumerate(faces_lower)}
    pivot_columns = {}
    for simplex in faces_upper:
        v = {index[face]: sign % p for face, sign in signed_boundary(simplex)}
        while v:
            row = min(v)
            if row not in pivot_columns:
                inv = pow(v[row], -1, p)
                pivot_columns[row] = {key: (value*inv)%p for key,value in v.items()}
                break
            c = v[row]
            for key, value in pivot_columns[row].items():
                reduced = (v.get(key,0) - c * value) % p
                if reduced:
                    v[key] = reduced
                else:
                    v.pop(key,None)
    return len(pivot_columns)


def main():
    faces = reconstruct_faces()
    f = list(map(len, faces))
    assert f == [17,136,612,1122,952,476,136,17]
    assert len({s for z in faces for s in z}) == sum(f)
    assert len({s for z in faces for s in z if s.bit_count()==8}) == 17
    for p, expected in ((2,{3:35}), (3,{2:1,3:36}), (5,{3:35})):
        ranks = [0] + [boundary_rank(faces[k-1],faces[k],p) for k in range(1,8)] + [0]
        betti = {k:f[k]-ranks[k]-ranks[k+1] for k in range(8)}
        assert betti[0] == 1
        reduced = {k:v for k,v in betti.items() if k > 0 and v}
        assert reduced == expected, (p, reduced, ranks)
        print(f'field F_{p}: boundary ranks {ranks[1:8]}, reduced Betti {reduced}')
    print('independent face/field-homology checks passed')

if __name__ == '__main__':
    main()
