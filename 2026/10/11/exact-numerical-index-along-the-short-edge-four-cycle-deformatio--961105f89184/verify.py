"""Exact rational checks supplementing the analytic weighted four-cycle proof."""
from fractions import Fraction as Q
from itertools import permutations

def dual_vertices(t):
    """Vertices of the zero-sum weighted cube section, in three coordinates."""
    assert Q(0) < t <= Q(1)
    vertices = set()
    for r in (t, -t):
        for u in set(permutations((Q(1), Q(-1), r))):
            vertices.add(tuple(u))
    return sorted(vertices)

def pair(u, p):
    return sum((a*b for a, b in zip(u, p)), Q(0))

def check(t):
    t = Q(t)
    e1, e2, e3 = ((Q(1),Q(0),Q(0)),
                  (Q(0),Q(1),Q(0)),
                  (Q(0),Q(0),Q(1)))
    p4 = (-Q(1)/t,)*3
    pp = [e1,e2,e3,p4]
    uu = dual_vertices(t)
    assert all(max(map(abs, u)) == 1 and abs(sum(u)) <= t for u in uu)
    assert all(abs(pair(u,p4))==1 for u in uu)
    z = ((1-t)/(1+t), Q(2)/(1+t), Q(0))
    phi = (Q(1), -Q(1,2), -Q(1,2))
    norm_z = max(abs(pair(u,z)) for u in uu)
    norm_phi = max(abs(pair(phi,p)) for p in pp)
    assert norm_z == 2-t
    assert norm_phi == 1
    numerical_radius = max(abs(pair(phi,p)*pair(u,z))
                           for p in pp for u in uu if abs(pair(u,p))==1)
    assert numerical_radius == 1
    assert numerical_radius/(norm_z*norm_phi) == 1/(2-t)
    # Every nonnorming dual vertex for a long-edge primal molecule is
    # decomposable into norming vertices with total coefficient mass 2-t.
    for i in range(3):
        for u in uu:
            if abs(u[i])==1:
                continue
            norming = [v for v in uu if v[i]==1]
            target = u if u[i]>0 else tuple(-x for x in u)
            candidates = [v for v in norming]
            assert any(tuple(v[k]-(1-t)*Q(x[k]+y[k],2) for k in range(3))
                       == target
                       for v in candidates for x in candidates for y in candidates)

if __name__ == '__main__':
    params = [Q(1,5),Q(1,3),Q(1,2),Q(2,3),Q(3,4),Q(9,10),Q(1)]
    for p in params:
        check(p)
    print(f'VERIFY_OK rational_parameters={len(params)} '
          'three_dimensional_vertex_profiles=True analytic_family_proof_required=True')
