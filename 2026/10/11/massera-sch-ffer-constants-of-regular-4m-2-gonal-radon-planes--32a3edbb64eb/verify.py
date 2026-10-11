import math

def norm_poly(v, N):
    x,y=v
    return max(
        x*math.cos(2*math.pi*j/N)+y*math.sin(2*math.pi*j/N)
        for j in range(N)
    )

def vertices(N):
    a=math.pi/N
    R=1/math.cos(a)
    return [
        (R*math.cos((2*j+1)*a), R*math.sin((2*j+1)*a))
        for j in range(N)
    ]

def formula(N):
    assert N%4==2
    a=math.pi/N
    if N%8==2:
        return 2*math.sin(math.pi/4+a/2)
    return 2/math.cos(a)*math.sin(math.pi/4+a/2)

for m in range(1,101):
    N=4*m+2
    a=math.pi/N
    vs=vertices(N)

    for v in vs:
        assert abs(norm_poly(v,N)-1)<5e-12

    best=-1.0
    count=0
    for j,x in enumerate(vs):
        n0=(math.cos(2*j*a), math.sin(2*j*a))
        n1=(math.cos(2*(j+1)*a), math.sin(2*(j+1)*a))
        for y in vs:
            q0=n0[0]*y[0]+n0[1]*y[1]
            q1=n1[0]*y[0]+n1[1]*y[1]
            if q0*q1 <= 2e-12:
                count += 1
                d=norm_poly((x[0]-y[0],x[1]-y[1]),N)
                best=max(best,d)

    target=formula(N)
    assert abs(best-target)<2e-10,(N,best,target)
    assert count==4*N,(N,count)

    Aminus=math.pi/4-a/2
    Aplus=math.pi/4+a/2
    if m%2==0:
        dminus=2/math.cos(a)*math.sin(Aminus)
        dplus=2*math.sin(Aplus)
    else:
        dminus=2*math.sin(Aminus)
        dplus=2/math.cos(a)*math.sin(Aplus)
    assert dplus>dminus-1e-14
    assert abs(dplus-target)<2e-14

assert abs(formula(6)-2)<2e-14
phi=(1+math.sqrt(5))/2
assert abs(formula(10)-phi)<2e-14

print("VERIFY_OK m=1..100 orthogonal_vertex_pairs=4N formula=MS_B_regular_4m_plus_2")
