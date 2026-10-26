"""Exact finite-field incidence and tangent-space verification for a quartic's lines.

Run: python verify_fano.py (Python 3, no third-party packages).
The underlying geometric count of 48 lines is also recorded in Veniani's Example 5.4.
"""
from collections import Counter
from fano48 import ADD, NEG, MUL, q, rrefs, contained, frob


def matrix_rank(rows):
    A = [list(row) for row in rows]
    if not A:
        return 0
    nr, nc = len(A), len(A[0])
    pivot_row = 0
    for col in range(nc):
        pivot = next((i for i in range(pivot_row, nr) if A[i][col]), None)
        if pivot is None:
            continue
        A[pivot_row], A[pivot] = A[pivot], A[pivot_row]
        inv = next(t for t in range(1, q) if MUL[t][A[pivot_row][col]] == 1)
        A[pivot_row] = [MUL[inv][z] for z in A[pivot_row]]
        for i in range(nr):
            if i == pivot_row:
                continue
            c = A[i][col]
            A[i] = [ADD[A[i][j]][NEG[MUL[c][A[pivot_row][j]]]] for j in range(nc)]
        pivot_row += 1
        if pivot_row == nr:
            break
    return pivot_row

# The pair (a,b) represents a + epsilon*b with epsilon**2=0 over F9.
ZERO = (0, 0)

def dadd(a, b): return ADD[a[0]][b[0]], ADD[a[1]][b[1]]
def dneg(a): return NEG[a[0]], NEG[a[1]]
def dmul(a, b):
    return MUL[a[0]][b[0]], ADD[MUL[a[0]][b[1]]][MUL[a[1]][b[0]]]

def polymul(a, b):
    z = [ZERO]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            z[i+j] = dadd(z[i+j], dmul(u,v))
    return z

def polysum(*terms):
    z = [ZERO]*max(map(len,terms))
    for t in terms:
        for i, c in enumerate(t):
            z[i] = dadd(z[i], c)
    return z

def psi(w, x, y, z):
    return polymul(polymul(w, z), polysum(
        polymul(w,w), polymul(w,x), polymul(x,x),
        polymul(y,y), polymul(y,z), polymul(z,z)))

def linearized_quartic(r0, r1, direction):
    x = [[(r0[j], int(direction == (0,j))),
          (r1[j], int(direction == (1,j)))] for j in range(4)]
    a,b,c,d = x
    left = psi(a,b,c,d)
    right = psi([dneg(z) for z in b],a,[dneg(z) for z in d],c)
    return [dadd(z,dneg(w))[1] for z,w in zip(left,right)]

def free_coordinates(line):
    r0,r1 = line
    i = next(j for j in range(4) if r0[j] == 1)
    j = next(j for j in range(4) if r1[j] == 1)
    return [(0,k) for k in range(i+1,4) if k != j] + [(1,k) for k in range(j+1,4)]

def main():
    # Independent arithmetic sanity checks for the model F9=F3[t]/(t^2+1).
    assert len({x for x in range(1,9) if MUL[x][x] != 0}) == 8
    assert all(MUL[a][ADD[b][c]] == ADD[MUL[a][b]][MUL[a][c]]
               for a in range(9) for b in range(9) for c in range(9))
    all_rrefs = list(rrefs(9))
    assert len(all_rrefs) == len(set(all_rrefs)) == 7462
    lines = [v for v in all_rrefs if contained(*v)]
    assert len(lines) == 48
    line_set = set(lines)
    assert all(frob(v) in line_set and frob(frob(v)) == v for v in lines)
    fixed = sum(frob(v) == v for v in lines)
    assert fixed == 6
    assert sum(contained(*v) for v in rrefs(3)) == 6

    chart = Counter()
    degenerate = []
    for line in lines:
        coords = free_coordinates(line)
        Jcols = [linearized_quartic(*line, d) for d in coords]
        Jrows = list(map(list,zip(*Jcols))) if coords else []
        r = matrix_rank(Jrows)
        chart[tuple(next(i for i,x in enumerate(v) if x == 1) for v in line)] += 1
        assert r >= len(coords)-1
        if r < len(coords):
            degenerate.append(line)
    assert chart == {(0,1):33,(0,2):11,(1,2):2,(1,3):1,(2,3):1}
    assert len(degenerate) == 7
    assert sum(frob(v)==v for v in degenerate) == 1
    assert all(frob(v) in degenerate for v in degenerate)
    print('F9 Grassmannian RREF matrices:',len(all_rrefs))
    print('Geometric line supports (using Veniani geometric count):',len(lines))
    print('Frobenius cycles: 6 fixed; 21 conjugate pairs')
    print('RREF chart line totals:',dict(chart))
    print('Fano tangent dimension 1 at 7 lines (1 fixed, 3 pairs)')
    print('Fano tangent dimension 0 at 41 lines (5 fixed, 18 pairs)')
    print('All assertions passed')

if __name__ == '__main__': main()
