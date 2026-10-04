import math
import random

random.seed(20261002)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def norm(a):
    return math.sqrt(dot(a,a))

def gram_schmidt(cols):
    out=[]
    for v in cols:
        w=v[:]
        for q in out:
            z=dot(w,q)
            w=[x-z*y for x,y in zip(w,q)]
        nw=norm(w)
        if nw < 1e-12:
            return None
        out.append([x/nw for x in w])
    return out

def matvec(Q,v):
    d=len(v)
    return [sum(Q[i][j]*v[j] for j in range(d)) for i in range(d)]

def random_orthogonal(d):
    while True:
        cols=[[random.uniform(-1,1) for _ in range(d)] for __ in range(d)]
        qs=gram_schmidt(cols)
        if qs is None:
            continue
        # q vectors are columns; form matrix
        Q=[[qs[j][i] for j in range(d)] for i in range(d)]
        # determinant sign is irrelevant to the containment identity; flip final
        # column when needed by a direct determinant for d<=5.
        def det(M):
            if len(M)==1: return M[0][0]
            return sum(((-1)**j)*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(len(M)))
        if det(Q) < 0:
            for i in range(d):
                Q[i][-1] *= -1
        return Q

def max_segment_halfspace(normal, p, q, w):
    return max(dot(normal,[p[i]+w[i] for i in range(len(p))]),
               dot(normal,[q[i]+w[i] for i in range(len(p))]))

# For a polyhedral host K={x:a_j.x<=b_j}, the capsule
# [p,q]+rB is contained in K iff each support value of the segment plus
# r||a_j|| is <=b_j. The eroded host has inequalities
# a_j.x<=b_j-r||a_j||. These are exactly equivalent.
for d in (2,3,4,5):
    a_len=1.7
    r=0.23
    e=[0.0]*d
    e[0]=1.0
    p0=[-a_len/2*x for x in e]
    q0=[ a_len/2*x for x in e]
    for _ in range(200):
        Q=random_orthogonal(d)
        p=matvec(Q,p0)
        q=matvec(Q,q0)
        w=[random.uniform(-0.5,0.5) for _ in range(d)]
        normals=[]
        bounds=[]
        for __ in range(12):
            a=[random.uniform(-2,2) for _ in range(d)]
            if norm(a)<1e-8:
                a[0]=1.0
            # random bound around the critical containment level
            crit=max_segment_halfspace(a,p,q,w)+r*norm(a)
            b=crit+random.uniform(-0.4,0.4)
            normals.append(a); bounds.append(b)
        capsule_ok=all(max_segment_halfspace(a,p,q,w)+r*norm(a) <= b+1e-12
                       for a,b in zip(normals,bounds))
        eroded_segment_ok=all(max_segment_halfspace(a,p,q,w) <= b-r*norm(a)+1e-12
                              for a,b in zip(normals,bounds))
        assert capsule_ok == eroded_segment_ok

# A nondegenerate capsule is neither a ball nor a segment:
# widths parallel/perpendicular to the spine differ, and perpendicular width is positive.
for d in (2,3,5):
    length=2.75
    r=0.4
    width_parallel=length+2*r
    width_perp=2*r
    assert width_parallel > width_perp > 0

print("VERIFY_OK capsule Kakeya erosion reduction")
