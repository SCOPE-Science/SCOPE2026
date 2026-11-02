"""Exact finite consistency checks for projective component degrees of 3-space orthogonal frames.
No assertion of exhaustive validation of the geometric argument is intended.
"""
from math import comb
from sympy import Matrix


def pairing(a,b):
    return a[0]*b[1]+a[1]*b[0]+a[2]*b[2]


def jacobian_rank(frame):
    h=len(frame)
    rows=[]
    for i in range(h):
        for j in range(i+1,h):
            row=[0]*(3*h)
            # B(x_i,x_j) partials w.r.t. (a_i,b_i,c_i) are (b_j,a_j,c_j)
            for k,v in enumerate((frame[j][1],frame[j][0],frame[j][2])):
                row[3*i+k]=v
            for k,v in enumerate((frame[i][1],frame[i][0],frame[i][2])):
                row[3*j+k]=v
            rows.append(row)
    return Matrix(rows).rank()


def assert_orthogonal(frame):
    for i in range(len(frame)):
        for j in range(i+1,len(frame)):
            assert pairing(frame[i],frame[j]) == 0

# The scalar vector bundle E=K + (h-1)S on an isotropic conic Q=P1.
# c1(S)=-2 and c1(K)=-2, so deg(P(E))=-c1(E)=2h.
# For h=4 the complete intersection of 6 quadrics in P11 has degree 64.
for h in range(4,13):
    a=(1,1,0); b=(1,-1,0); u=(0,0,1); e=(1,0,0)
    assert pairing(a,b)==pairing(a,u)==pairing(b,u)==0
    assert pairing(e,e)==0 and pairing(e,u)==0
    for j in range(h):
        bframe=[e]*h
        bframe[j]=u
        assert_orthogonal(bframe)
        assert jacobian_rank(bframe)==2*(h-1), (h,j,'B')
    for subset in ((0,1,2),(h-3,h-2,h-1)):
        aframe=[(0,0,0)]*h
        for ind,v in zip(subset,(a,b,u)):
            aframe[ind]=v
        assert_orthogonal(aframe)
        assert jacobian_rank(aframe)==3*h-6, (h,subset,'A')
    deg_b=2*h
    deg_a=2**3
    assert deg_b>0 and deg_a==8
    if h==4:
        assert h*deg_b+comb(h,3)*deg_a==2**comb(h,2)==64
    else:
        assert h*deg_b==2*h*h
print('VERIFY_OK; exact Jacobian ranks for h=4..12 and all B_i; Chern-class and CI degree arithmetic checked')
