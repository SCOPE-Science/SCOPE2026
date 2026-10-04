#!/usr/bin/env python3
from itertools import combinations, product
import json

N = 9

def b2m(x):
    return [[(x >> (3*i+j)) & 1 for j in range(3)] for i in range(3)]

def m2b(A):
    return sum((A[i][j] & 1) << (3*i+j) for i in range(3) for j in range(3))

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) & 1 for j in range(3)] for i in range(3)]

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2] ^ A[1][2]*A[2][1]) ^
            A[0][1]*(A[1][0]*A[2][2] ^ A[1][2]*A[2][0]) ^
            A[0][2]*(A[1][0]*A[2][1] ^ A[1][1]*A[2][0])) & 1

def inv3(A):
    R = [A[i][:] + [int(i == j) for j in range(3)] for i in range(3)]
    for c in range(3):
        p = next(i for i in range(c,3) if R[i][c])
        R[c], R[p] = R[p], R[c]
        for i in range(3):
            if i != c and R[i][c]:
                R[i] = [a ^ b for a,b in zip(R[i], R[c])]
    return [r[3:] for r in R]

def triangularizable(x):
    a = [(x >> i) & 1 for i in range(9)]
    tr = a[0] ^ a[4] ^ a[8]
    e2 = (a[0]*a[4] ^ a[1]*a[3] ^
          a[0]*a[8] ^ a[2]*a[6] ^
          a[4]*a[8] ^ a[5]*a[7]) & 1
    d = det3(b2m(x))
    # The four split monic cubics over F_2 are:
    # t^3, t^2(t+1), t(t+1)^2, (t+1)^3.
    return (tr,e2,d) in {(0,0,0),(1,0,0),(0,1,0),(1,1,1)}

GOOD = [triangularizable(x) for x in range(512)]

def span_tuple(B):
    arr = [0]
    for b in B:
        arr += [x ^ b for x in arr]
    return tuple(sorted(arr))

def rref_subspaces(k, n=N):
    # Unique RREF basis for every k-subspace of F_2^n.
    for piv in combinations(range(n), k):
        allowed = [[j for j in range(p+1,n) if j not in piv] for p in piv]
        for codes in product(*[range(1 << len(cols)) for cols in allowed]):
            rows = []
            for i,p in enumerate(piv):
                r = 1 << p
                for b,j in enumerate(allowed[i]):
                    if (codes[i] >> b) & 1:
                        r |= 1 << j
                rows.append(r)
            yield piv, rows

def space_good(B):
    return all(GOOD[x] for x in span_tuple(B))

def null_basis_from_rref(piv, rows, n=N):
    free = [j for j in range(n) if j not in piv]
    B = []
    for j in free:
        v = 1 << j
        for i,p in enumerate(piv):
            if (rows[i] >> j) & 1:
                v |= 1 << p
        B.append(v)
    return B

def enumerate_direct(k):
    total = 0
    good = []
    for _,B in rref_subspaces(k):
        total += 1
        if space_good(B):
            good.append(span_tuple(B))
    return total, set(good)

def enumerate_via_orthogonal(codim):
    total = 0
    good = []
    for piv,U in rref_subspaces(codim):
        total += 1
        B = null_basis_from_rref(piv,U)
        if space_good(B):
            good.append(span_tuple(B))
    return total, set(good)

def conjugate(x,P,Pi):
    return m2b(mm(mm(P,b2m(x)),Pi))

def orbit(S, GL):
    return {tuple(sorted(conjugate(x,P,Pi) for x in S)) for P,Pi in GL}

def rep_T():
    return tuple(sorted(x for x in range(512)
                        if all(b2m(x)[i][j] == 0 for i in range(3) for j in range(3) if i > j)))

def rep_left_sl2():
    # sl_2(F_2) vee M_1(F_2): [[a,b,u],[c,a,v],[0,0,d]].
    out = []
    for a,b,c,u,v,d in product(range(2), repeat=6):
        out.append(m2b([[a,b,u],[c,a,v],[0,0,d]]))
    return tuple(sorted(out))

def rep_right_sl2():
    # M_1(F_2) vee sl_2(F_2): [[d,u,v],[0,a,b],[0,c,a]].
    out = []
    for a,b,c,u,v,d in product(range(2), repeat=6):
        out.append(m2b([[d,u,v],[0,a,b],[0,c,a]]))
    return tuple(sorted(out))

def common_invariant_lines(S):
    ans = []
    for v in range(1,8):
        vv = [(v >> i) & 1 for i in range(3)]
        ok = True
        for x in S:
            A = b2m(x)
            y = [sum(A[i][j]*vv[j] for j in range(3)) & 1 for i in range(3)]
            yb = sum(y[i] << i for i in range(3))
            if yb not in (0,v):
                ok = False; break
        if ok: ans.append(v)
    return ans

def common_invariant_planes(S):
    # Plane ker(f) is invariant iff f A lies in span(f) for every A.
    ans = []
    for f in range(1,8):
        ff = [(f >> i) & 1 for i in range(3)]
        ok = True
        for x in S:
            A = b2m(x)
            y = [sum(ff[i]*A[i][j] for i in range(3)) & 1 for j in range(3)]
            yb = sum(y[j] << j for j in range(3))
            if yb not in (0,f):
                ok = False; break
        if ok: ans.append(f)
    return ans

# Main exhaustive checks.
total6, good6_direct = enumerate_direct(6)
total7, good7_direct = enumerate_direct(7)
total_codim3, good6_orth = enumerate_via_orthogonal(3)
assert total6 == 788035
assert total7 == 43435
assert total_codim3 == 788035
assert len(good6_direct) == 35
assert len(good7_direct) == 0
assert good6_direct == good6_orth

GL = []
for x in range(512):
    P = b2m(x)
    if det3(P):
        GL.append((P, inv3(P)))
assert len(GL) == 168

T = rep_T(); L = rep_left_sl2(); R = rep_right_sl2()
assert all(GOOD[x] for x in T)
assert all(GOOD[x] for x in L)
assert all(GOOD[x] for x in R)
OT, OL, OR = orbit(T,GL), orbit(L,GL), orbit(R,GL)
assert [len(OT),len(OL),len(OR)] == [21,7,7]
assert OT.isdisjoint(OL) and OT.isdisjoint(OR) and OL.isdisjoint(OR)
assert OT | OL | OR == good6_direct

# Structural invariants distinguish the three types.
inv_summary = {
    'T3': [len(common_invariant_lines(T)), len(common_invariant_planes(T))],
    'sl2_vee_M1': [len(common_invariant_lines(L)), len(common_invariant_planes(L))],
    'M1_vee_sl2': [len(common_invariant_lines(R)), len(common_invariant_planes(R))],
}
assert inv_summary['T3'][0] >= 1 and inv_summary['T3'][1] >= 1
assert inv_summary['sl2_vee_M1'] == [0,1]
assert inv_summary['M1_vee_sl2'] == [1,0]

cert = {
    'ambient_matrices': 512,
    'triangularizable_matrices': sum(GOOD),
    'six_subspaces_total': total6,
    'six_subspaces_all_triangularizable': len(good6_direct),
    'seven_subspaces_total': total7,
    'seven_subspaces_all_triangularizable': len(good7_direct),
    'max_dimension': 6,
    'GL3_order': len(GL),
    'orbit_sizes': {'T3':len(OT),'sl2_vee_M1':len(OL),'M1_vee_sl2':len(OR)},
    'common_invariant_line_plane_counts': inv_summary,
    'orthogonal_enumeration_agrees': good6_direct == good6_orth,
}
print(json.dumps(cert, sort_keys=True, indent=2))
