from math import sin, cos, pi, isclose
import cmath

def line_intersection(theta1,h1,theta2,h2):
    a,b=cos(theta1),sin(theta1)
    c,d=cos(theta2),sin(theta2)
    det=a*d-b*c
    return ((h1*d-b*h2)/det,(a*h2-h1*c)/det)

def dot(theta,p):
    return cos(theta)*p[0]+sin(theta)*p[1]

# Fourier rigidity stress test over all admissible q and a broad range of m.
for q in range(1,31):
    for m in range(4*q+3,251):
        phi=2*pi/m
        A=sin(q*phi)
        B=sin((q+1)*phi)
        D=sin((2*q+1)*phi)
        assert A>0 and B>0 and D>0
        target=A+B
        for k in range(1,m):
            z=cmath.exp(2j*pi*k/m)
            eig=A*z**(-(q+1))+B*z**q
            assert abs(eig-target)>1e-11, (m,q,k,eig,target)

# Independently reconstruct the two sideline intersections for regular support data.
# They must lie on the homothetic image of side i with the ratio forced by summing the recurrence.
for q in range(1,8):
    for m in range(4*q+3,80):
        phi=2*pi/m
        A=sin(q*phi); B=sin((q+1)*phi); D=sin((2*q+1)*phi)
        mu=(A+B)/D
        for i in range(m):
            th=lambda j: (j % m)*phi
            p1=line_intersection(th(i-q-1),1.0,th(i+q),1.0)
            p2=line_intersection(th(i-q),1.0,th(i+q+1),1.0)
            assert abs(dot(th(i),p1)-mu)<2e-10
            assert abs(dot(th(i),p2)-mu)<2e-10

# A nonconstant support Fourier mode cannot satisfy the homothety recurrence.
for m,q,k in [(9,1,2),(13,1,3),(15,2,4),(23,3,5),(31,4,7)]:
    if not (4*q+3 <= m):
        continue
    phi=2*pi/m
    A=sin(q*phi); B=sin((q+1)*phi)
    z=cmath.exp(2j*pi*k/m)
    assert abs(A*z**(-(q+1))+B*z**q-(A+B))>1e-8

print('VERIFY_OK equiangular illumination-homothety rigidity')
