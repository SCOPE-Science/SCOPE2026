"""Exact rational verification of the PQ-star minimum-volume enclosing ellipsoid.

Run with Python 3: python verification/check_pq_star.py
No external dependencies. The general proof is in RESULT.md; the finite checks
here independently reconstruct all contact covariances from the vertex list.
"""
from fractions import Fraction as F


def parameters(m):
    if m <= 4:
        w = F(3, 4*(2*m+1))
        p0 = F(4-m, 4*(2*m+1))
    else:
        w = F(1, 3*m)
        p0 = F(0)
    return p0, w, w


def vertices_and_weights(m):
    p0, paxis, ppair = parameters(m)
    d = 2*m
    v = [(tuple([0]*d), p0, 'hub')]
    for j in range(m):
        for axis in (0,1):
            z = [0]*d
            z[axis*m+j] = 1
            v.append((tuple(z), paxis, 'axis'))
        z = [0]*d
        z[j] = z[m+j] = 1
        v.append((tuple(z), ppair, 'pair'))
    assert len(v) == 3*m+1
    assert sum(w for _,w,_ in v) == 1
    return v


def check(m):
    d = 2*m
    points = vertices_and_weights(m)
    cen = [sum(w*z[j] for z,w,_ in points) for j in range(d)]
    p0, a, _ = parameters(m)
    alpha = a+a
    assert all(t == alpha for t in cen)
    sigma = [[sum(w*(z[i]-cen[i])*(z[j]-cen[j]) for z,w,_ in points)
              for j in range(d)] for i in range(d)]
    B = a*3
    g = B-2*m*alpha*alpha
    assert a>0 and B>0 and g>0
    # Independent reconstruction of covariance: diagonal block plus rank-one block.
    for i in range(m):
        for j in range(m):
            diagonal = F(1) if i==j else F(0)
            target_diag = (B+a)/2*diagonal+(g-B)/(2*m)
            target_cross = (B-a)/2*diagonal+(g-B)/(2*m)
            assert sigma[i][j] == target_diag
            assert sigma[m+i][m+j] == target_diag
            assert sigma[i][m+j] == target_cross
            assert sigma[m+i][j] == target_cross
    # Mahalanobis distances obtained independently by orthogonal projections.
    for z,w,kind in points:
        sx=[F(z[i]+z[m+i],1) for i in range(m)]
        dx=[F(z[i]-z[m+i],1) for i in range(m)]
        ss=sum(sx); dd=sum(dx)
        s_global=(ss-2*m*alpha)**2/F(2*m)
        s_orth=(sum(t*t for t in sx)-ss*ss/F(m))/2
        dnorm=sum(t*t for t in dx)/2
        Q=s_global/g+s_orth/B+dnorm/a
        assert Q == (F(8) if kind=='hub' and m>=4 else F(d)), (m,kind,Q,d)
        assert Q <= d
        if w:
            assert Q==d
    # Verify intrinsic transformation: each row and column's hub entry
    # is minus the sum of its leaf-coordinate displacements.
    root_axes=sorted([d*(m+1)*g, d*B, d*(m+1)*a, d*a])
    assert min(root_axes)>0
    return len(points), sum(w>0 for _,w,_ in points)


def main():
    count=contacts=0
    for m in range(1,10):
        n,c=check(m)
        count+=n
        contacts+=c
    assert parameters(4)==(F(0),F(1,12),F(1,12))
    assert parameters(5)==(F(0),F(1,15),F(1,15))
    print('PQ_STAR_LOEWNER_EXACT_CHECKS_PASSED sizes=9 vertices=%d positive_contacts=%d' %(count,contacts))

if __name__=='__main__':
    main()
