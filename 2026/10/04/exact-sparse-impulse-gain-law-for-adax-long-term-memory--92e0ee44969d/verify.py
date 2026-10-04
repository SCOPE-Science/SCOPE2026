import math

def kernel(t,b2):
    return math.sqrt(((1.0+b2)-(1.0+b2)**(-(t-1)))/b2)

def gain(b1,b2,tol=1e-15):
    if b1 == 0.0:
        return 1.0
    s=0.0
    t=1
    while True:
        term=(1.0-b1)*(b1**(t-1))*kernel(t,b2)
        s += term
        if t>100 and term<tol:
            break
        t += 1
        assert t < 2000000
    return s

# Closed AdaX recurrence on one impulse.
b1=0.9
b2=1e-4
G=2.0
m=0.0
v=0.0
prev_vhat=None
for t in range(1,401):
    g=G if t==1 else 0.0
    m=b1*m+(1.0-b1)*g
    v=(1.0+b2)*v+b2*g*g
    vhat=v/((1.0+b2)**t-1.0)
    m0=(1.0-b1)*(b1**(t-1))*G
    v0=b2*((1.0+b2)**(t-1))*G*G
    vh0=G*G*b2*((1.0+b2)**(t-1))/((1.0+b2)**t-1.0)
    assert abs(m-m0) < 1e-12
    assert abs(v-v0) < 1e-10
    assert abs(vhat-vh0) < 1e-10
    if prev_vhat is not None:
        assert vhat < prev_vhat
    prev_vhat=vhat

# Kernel monotonicity, permitting numerical saturation only at machine precision.
for b2 in (1e-4,1e-2,0.2):
    prev=kernel(1,b2)
    assert abs(prev-1.0)<1e-12
    ceiling=math.sqrt((1.0+b2)/b2)
    strict_seen=0
    for t in range(2,5000):
        cur=kernel(t,b2)
        assert cur >= prev-2e-15*max(1.0,prev)
        assert cur <= ceiling+2e-15*max(1.0,ceiling)
        if cur > prev:
            strict_seen += 1
        prev=cur
    assert strict_seen > 20

# Gain monotonicity.
for b2 in (1e-4,1e-2,0.2):
    vals=[gain(r,b2) for r in (0.0,0.2,0.5,0.8,0.9,0.95,0.99)]
    assert all(b>a for a,b in zip(vals,vals[1:]))
    ceiling=math.sqrt((1.0+b2)/b2)
    assert all(v<ceiling for v in vals)

# Source-default value and limiting ceiling.
assert abs(gain(0.9,1e-4)-2.8555435149032955) < 2e-12
ceil=math.sqrt(1.0001/1e-4)
assert abs(ceil-100.00499987500625) < 2e-12

# Adam impulse regimes.
def adam_step(t,b1,b2):
    return (1.0-b1)*(b1**(t-1))*math.sqrt((1.0-b2**t)/((1.0-b2)*(b2**(t-1))))

b2=0.81
crit=math.sqrt(b2)

sub=[adam_step(t,0.8,b2) for t in range(1,1000)]
assert sub[-1] < 1e-20
assert sum(sub) < 20.0

target=(1.0-crit)/math.sqrt(1.0-b2)
critical=adam_step(500,crit,b2)
assert abs(critical-target) < 2e-12

a=adam_step(80,0.95,b2)
b=adam_step(81,0.95,b2)
assert b>a
assert a>1.0

print("verification passed")
