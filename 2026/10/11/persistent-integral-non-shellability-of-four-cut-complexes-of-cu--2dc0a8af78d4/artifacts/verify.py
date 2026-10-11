#!/usr/bin/env python3
"""Independent finite checks for a simplicial-complex theorem on path powers."""
from itertools import combinations
from collections import Counter

TRI = (1, 2, 8)
CYCLE = {(3,5):1, (4,5):-1, (4,6):1, (3,6):-1}
T = (1,3,5,8)

def connected_four(Q):
    """Four ordered labels induce connected graph of P_n^3 iff each gap <=3."""
    return all(v-u <= 3 for u,v in zip(Q,Q[1:]))

def good_face(Q):
    return all(connected_four(R) for R in combinations(Q,4))

def signed_sort(t):
    s = -1 if sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))%2 else 1
    return tuple(sorted(t)),s

def join_three_cycle():
    bd_triangle = {(2,8):1,(1,8):-1,(1,2):1}
    z=Counter()
    for E,coeff1 in bd_triangle.items():
        for F,coeff2 in CYCLE.items():
            face,sign = signed_sort(E+F)
            z[face] += coeff1*coeff2*sign
    return {f:v for f,v in z.items() if v}

def boundary(c):
    d=Counter()
    for f,a in c.items():
        for i in range(len(f)):
            d[f[:i]+f[i+1:]] += a*((-1)**i)
    return {f:v for f,v in d.items() if v}

def run():
    z=join_three_cycle()
    assert len(z)==12
    assert not boundary(z), 'oriented join cycle has nonzero boundary'
    assert all(good_face(Q) for Q in z), 'join not included in K8'
    assert abs(z[T])==1, 'chosen cochain not primitive against cycle'
    for t in range(2,8):
        W=tuple(sorted(T+(t,)))
        assert not good_face(W), ('triangle has a coface',t)
        assert any(not connected_four(S) for S in combinations(W,4))
    for n in range(8,14):
        total=0
        for length in range(n+1):
            for Q in combinations(range(1,n+1),length):
                if not good_face(Q): continue
                total+=1
                U=tuple(sorted({min(i,8) for i in Q}))
                assert good_face(U),('clamp fails',n,Q,U)
        assert total>0
        bad=tuple([1,2,3,n])
        assert not connected_four(bad) # ensures 4-cut complex is nonvoid
        print('n',n,'faces of dual',total,'retraction checked')
    print('VERIFY_OK 12 oriented join tetrahedra; 4 coface exclusions; six complete retraction enumerations')
if __name__=='__main__':
    run()
