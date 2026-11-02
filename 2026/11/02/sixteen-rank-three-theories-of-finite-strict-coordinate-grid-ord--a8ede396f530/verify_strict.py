#!/usr/bin/env python3
"""An independent geometric-atomic computation of three-round grid types."""

def atom(a, b, c):
    values = (a, b, c)
    cells = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        p, q = values[i], values[j]
        if p == q:
            cells.append('=')
        elif p[0] < q[0] and p[1] < q[1]:
            cells.append('<')
        elif q[0] < p[0] and q[1] < p[1]:
            cells.append('>')
        else:
            cells.append('!')
    return tuple(cells)

def root_type(m, n):
    points = tuple((i, j) for i in range(m) for j in range(n))
    two_round = {}
    for p in points:
        for q in points:
            two_round[(p, q)] = frozenset(atom(p, q, r) for r in points)
    one_round = {p: frozenset(two_round[(p, q)] for q in points)
                 for p in points}
    return frozenset(one_round.values())

def main():
    class_to_signature={}
    signature_to_class={}
    tested=0
    for m in range(1,8):
        for n in range(m,8):
            t=root_type(m,n)
            cap={1:3,2:4,3:5,4:6,5:6,6:6,7:7}[m]
            key=(7,7) if m==7 else (m,min(n,cap))
            assert class_to_signature.setdefault(t,key)==key
            assert signature_to_class.setdefault(key,t)==t
            tested+=1
    assert tested==28 and len(class_to_signature)==len(signature_to_class)==16
    assert max(a*b for a,b in signature_to_class)==49
    print('exact_root_classes=16')
    for a,b in sorted(signature_to_class):print(f'{a},{b}:{a*b}')
    print('sharp_within_family_representative_size=49')
    print(f'unordered_tested_pairs={tested}')
    print('verification=PASS')
if __name__=='__main__':main()
