import math

def h(p):
    if p == 0.0 or p == 1.0:
        return 0.0
    return -p*math.log(p)-(1-p)*math.log(1-p)

def closed(t):
    theta=t*t/(1+t*t)
    s=h(theta)
    N=math.exp(s)
    D=math.sqrt((11*N-8)/(3*N))
    r=(D-1)/2
    Z=1+4*N*r+3*N*r*r
    B=Z/(1+r)**4
    w=(1/Z,4*N*r/Z,3*N*r*r/Z)
    return theta,s,N,D,r,Z,B,w

def face_obj(t,w):
    w0,w1,w2=w
    theta=t*t/(1+t*t)
    N=math.exp(h(theta))
    H=-sum(x*math.log(x) for x in w if x>0)
    m=w1+2*w2
    return H+w1*math.log(4*N)+w2*math.log(3*N)-4*h(m/4)

for t in (1.0,0.5,0.1,0.01):
    theta,s,N,D,r,Z,B,w=closed(t)
    assert 1 < N <= 2+1e-14
    assert 0 < r < 1
    assert abs(r*(1+r)-2*(N-1)/(3*N)) < 3e-14
    assert abs(sum(w)-1) < 3e-14
    m=w[1]+2*w[2]
    assert abs(m-4*r/(1+r)) < 3e-14
    assert abs(face_obj(t,w)-math.log(B)) < 3e-13
    assert B > 1
    assert B <= N+1e-14
    # Dense-grid corroboration on the simplex face.
    best=-1e100
    step=1/300
    for i in range(301):
        w1=i*step
        for j in range(301-i):
            w2=j*step
            w0=1-w1-w2
            v=face_obj(t,(w0,w1,w2))
            if v>best: best=v
    assert best <= math.log(B)+2e-4

for t in (1e-2,3e-3,1e-3):
    theta,s,N,D,r,Z,B,w=closed(t)
    ratio=math.log(B)/(s*s)
    assert abs(ratio-4/3) < (0.01 if t==1e-2 else 0.002)

# Algebraically equivalent closed form.
for t in (1.0,0.2,0.02):
    theta,s,N,D,r,Z,B,w=closed(t)
    B2=8*(3*N-2+N*D)/(1+D)**4
    assert abs(B-B2) < 5e-14

print('VERIFY_OK')
