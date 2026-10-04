import cmath
import math

def H(beta, omega):
    return (1.0-beta)/(1.0-beta*cmath.exp(-1j*omega))

def ratio(alpha, b1, b3, omega):
    return alpha*abs(H(b3,omega))/abs(H(b1,omega))

def crossover(alpha,b1,b3):
    C=(alpha*(1.0-b3)/(1.0-b1))**2
    c=(1.0+b3*b3-C*(1.0+b1*b1))/(2.0*(b3-C*b1))
    return math.acos(c)

b1=0.9
b3=0.9999

# Strict monotonicity for source-like and randomized admissible examples.
for alpha in (2.0,4.0,5.0,8.0,10.0,20.0):
    prev=ratio(alpha,b1,b3,0.0)
    for j in range(1,5001):
        w=math.pi*j/5000.0
        cur=ratio(alpha,b1,b3,w)
        assert cur < prev
        prev=cur

# Closed endpoint values.
for alpha in (4.0,5.0,8.0,10.0):
    assert abs(ratio(alpha,b1,b3,0.0)-alpha) < 1e-12
    rpi=alpha*(1.0-b3)*(1.0+b1)/((1.0+b3)*(1.0-b1))
    assert abs(ratio(alpha,b1,b3,math.pi)-rpi) < 1e-12

# Source-parameter crossover periods.
expected={
    4.0:16222.186598391592,
    5.0:12824.712591201307,
    8.0:7915.445393004867,
    10.0:6314.238635418405,
}
for alpha,T in expected.items():
    w=crossover(alpha,b1,b3)
    assert abs(ratio(alpha,b1,b3,w)-1.0) < 2e-9
    assert abs(2.0*math.pi/w-T) < 2e-5
    assert ratio(alpha,b1,b3,w*0.9) > 1.0
    assert ratio(alpha,b1,b3,min(math.pi,w*1.1)) < 1.0

def direct_endpoint(kind, alpha, b1, b2, b3, G=2.0, T=300000):
    m1=0.0
    m2=0.0
    v=0.0
    last=None
    for t in range(1,T+1):
        if kind == "dc":
            g=G
        else:
            g=G if t%2 else -G
        m1=b1*m1+(1.0-b1)*g
        m2=b3*m2+(1.0-b3)*g
        v=b2*v+(1.0-b2)*g*g
        m1hat=m1/(1.0-b1**t)
        vhat=v/(1.0-b2**t)
        adem=(m1hat+alpha*m2)/math.sqrt(vhat)
        adam=m1hat/math.sqrt(vhat)
        last=(adem,adam,vhat)
    return last

b2=0.999
for alpha in (4.0,5.0,8.0,10.0):
    adem,adam,vhat=direct_endpoint("dc",alpha,b1,b2,b3,T=200000)
    assert abs(vhat-4.0) < 1e-12
    assert abs(abs(adem/adam)-(1.0+alpha)) < 5e-8

    adem,adam,vhat=direct_endpoint("nyquist",alpha,b1,b2,b3,T=200000)
    rpi=alpha*(1.0-b3)*(1.0+b1)/((1.0+b3)*(1.0-b1))
    assert abs(vhat-4.0) < 1e-12
    assert abs(abs(adem/adam)-(1.0+rpi)) < 5e-8

# Published numeric endpoint gains.
assert abs(1.0+4.0*(1-b3)*(1+b1)/((1+b3)*(1-b1))-1.0038001900095002) < 1e-15
assert abs(1.0+10.0*(1-b3)*(1+b1)/((1+b3)*(1-b1))-1.0095004750237502) < 1e-15

print("verification passed")
