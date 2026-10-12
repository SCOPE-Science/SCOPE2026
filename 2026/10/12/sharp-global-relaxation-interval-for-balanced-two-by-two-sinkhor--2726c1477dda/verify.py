import math

def potential(K,x,y):
    s=[(x+y)/2,(x-y)/2,(-x+y)/2,(-x-y)/2]
    v=[K[0][0],K[0][1],K[1][0],K[1][1]]
    return math.log(sum(v[i]*math.exp(s[i]) for i in range(4)))

def step(K,x,y,omega):
    A=K[0][0]*math.exp(y/2)+K[0][1]*math.exp(-y/2)
    B=K[1][0]*math.exp(y/2)+K[1][1]*math.exp(-y/2)
    xc=math.log(B/A)
    xx=(1-omega)*x+omega*xc
    C=K[0][0]*math.exp(xx/2)+K[1][0]*math.exp(-xx/2)
    D=K[0][1]*math.exp(xx/2)+K[1][1]*math.exp(-xx/2)
    yc=math.log(D/C)
    yy=(1-omega)*y+omega*yc
    return xx,yy

def row_and_col_sums(K,x,y):
    U=[math.exp(x/2),math.exp(-x/2)]
    V=[math.exp(y/2),math.exp(-y/2)]
    P=[[U[i]*K[i][j]*V[j] for j in range(2)] for i in range(2)]
    S=sum(sum(r) for r in P)
    P=[[z/S for z in r] for r in P]
    return [sum(z) for z in P], [P[0][j]+P[1][j] for j in range(2)]

K=[[100.,1.],[1.,100.]]
assert (100-1)/(100+1)==99/101
assert abs(2/(1+99/101)-101/100)<1e-14
assert 101/100<19/10<2
assert abs(potential(K,0.,0.)-math.log(202))<1e-14
x0,y0=math.log(2),0.
expected_gap=math.log(3/(2*math.sqrt(2)))
assert expected_gap>0
assert abs((potential(K,x0,y0)-potential(K,0,0))-expected_gap)<1e-13

for omega in [0.7,1.0,1.9]:
    x,y=x0,y0
    old=potential(K,x,y)
    for _ in range(1200):
        x,y=step(K,x,y,omega)
        new=potential(K,x,y)
        assert new<=old+1e-12
        old=new
    rows,cols=row_and_col_sums(K,x,y)
    assert max(abs(t-.5) for t in rows+cols)<1e-7

# Equal-target conditional reflection is energy-preserving at omega=2.
x,y=x0,y0
initial=potential(K,x,y)
for _ in range(20):
    x,y=step(K,x,y,2.)
    assert abs(potential(K,x,y)-initial)<5e-12
assert initial>potential(K,0.,0.)

# For omega>2 the potential cannot decrease.
x,y=x0,y0
for _ in range(6):
    old=potential(K,x,y)
    x,y=step(K,x,y,2.01)
    assert potential(K,x,y)>=old-1e-12

# Test a nonsymmetric positive kernel from a remote initialization.
M=[[4.,1.],[2.,3.]]
x,y=-0.7,1.2
for _ in range(2000):
    x,y=step(M,x,y,1.9)
rows,cols=row_and_col_sums(M,x,y)
assert max(abs(t-.5) for t in rows+cols)<1e-8
print('VERIFY_OK')
print('published_sufficient_upper',101/100)
print('tested_global_parameter',19/10)
print('exact_initial_boundary_gap',expected_gap)
