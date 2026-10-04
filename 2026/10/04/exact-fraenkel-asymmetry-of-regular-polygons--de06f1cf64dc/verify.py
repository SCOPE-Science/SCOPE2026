import math

def asym_formula(n):
    t=math.pi/n
    q=math.sqrt(math.sin(2*t)/(2*t))
    beta=math.acos(math.cos(t)/q)
    return 2*n/math.pi*(beta-math.sin(beta)*math.cos(beta))

def centered_intersection_numeric(n, steps=120000):
    # Circumradius is normalized to one.  Integrate the radial intersection
    # over one side-normal sector and multiply by n.
    t=math.pi/n
    c=math.cos(t)
    q=math.sqrt(math.sin(2*t)/(2*t))
    h=2*t/steps
    acc=0.0
    for j in range(steps):
        th=-t+(j+0.5)*h
        rho=c/math.cos(th)
        acc += min(q*q, rho*rho)
    return n*0.5*h*acc, q

for n in (3,4,5,6,7,10,17,32,60):
    af=asym_formula(n)
    area_int,q=centered_intersection_numeric(n)
    area=math.pi*q*q
    af_num=2*(area-area_int)/area
    assert 0.0 < af < 2.0
    assert abs(af-af_num) < 2e-9, (n,af,af_num)

C=4*math.pi**2/(9*math.sqrt(3))
mu=3*math.sqrt(3*math.pi)/4
for n in (500,1000,2000):
    af=asym_formula(n)
    assert abs(af*n*n/C-1) < 3e-5
    P=2*math.sqrt(n*math.tan(math.pi/n))
    ratio=(P-2*math.sqrt(math.pi))/af
    assert abs(ratio/mu-1) < 5e-5

print('VERIFY_OK regular polygon Fraenkel asymmetry')
