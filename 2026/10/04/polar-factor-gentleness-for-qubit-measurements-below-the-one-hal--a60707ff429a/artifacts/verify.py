import math, random

def rot_from_quat(q):
    w,x,y,z=q
    return [
      [1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],
      [2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],
      [2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]]

def matvec(R,v): return [sum(R[i][j]*v[j] for j in range(3)) for i in range(3)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))

def hA(r,g):
    c=2*g/(1+g*g); d=(1-g*g)/(1+g*g)
    x,y,z=r; den=1+c*z
    return [d*x/den,d*y/den,(c+z)/den]

def randrot():
    q=[random.gauss(0,1) for _ in range(4)]
    n=math.sqrt(sum(t*t for t in q)); q=[t/n for t in q]
    return rot_from_quat(q)

random.seed(20261002)
for g in [0.05,0.2,0.49,0.56,1/math.sqrt(3)-1e-6,0.6,0.8,0.95]:
    c=2*g/(1+g*g); d=(1-g*g)/(1+g*g)
    # positive-factor maximizing pure state at z=-g has disturbance exactly g
    r=[math.sqrt(1-g*g),0,-g]
    h=hA(r,g)
    D=math.sqrt((1-dot(r,h))/2)
    assert abs(D-g)<1e-12
    for _ in range(30):
        R=randrot()
        if g<=1/math.sqrt(3):
            x=(1-g*g)/2; y=g*g
            avg=x*(R[0][0]+R[1][1])-y*R[2][2]
            assert avg <= 1-2*g*g + 1e-12
        else:
            avg=d*(R[0][0]+R[1][1])/2
            assert avg <= d + 1e-12
            assert g*g/(1+g*g) >= 0.25-1e-12
print('VERIFY_OK')
