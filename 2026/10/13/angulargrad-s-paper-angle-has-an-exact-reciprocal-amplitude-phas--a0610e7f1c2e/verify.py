import math
import random

def paper_angle(G):
    if abs(G-1.0) < 1e-15:
        return math.pi/2.0
    return math.atan(2.0*G/abs(1.0-G*G))

def phi_cos_direct(G):
    A=paper_angle(G)
    return 0.5*(1.0+math.tanh(abs(math.cos(A))))

def phi_tan_direct(G):
    if abs(G-1.0) < 1e-15:
        return 1.0
    A=paper_angle(G)
    return 0.5*(1.0+math.tanh(abs(math.tan(A))))

def phi_cos_closed(G):
    return 0.5*(1.0+math.tanh(abs(1.0-G*G)/(1.0+G*G)))

def phi_tan_closed(G):
    if abs(G-1.0) < 1e-15:
        return 1.0
    return 0.5*(1.0+math.tanh(2.0*G/abs(1.0-G*G)))

# Direct source formula versus closed forms.
random.seed(350067)
for _ in range(5000):
    G=10.0**random.uniform(-6.0,6.0)
    if abs(G-1.0) < 1e-8:
        continue
    assert abs(phi_cos_direct(G)-phi_cos_closed(G)) < 3e-13
    assert abs(phi_tan_direct(G)-phi_tan_closed(G)) < 3e-13

# Exact reciprocal-amplitude symmetry.
for G in (1e-5,0.01,0.1,0.3,0.7,1.3,3.0,10.0,1e5):
    assert abs(phi_cos_closed(G)-phi_cos_closed(1.0/G)) < 3e-13
    assert abs(phi_tan_closed(G)-phi_tan_closed(1.0/G)) < 3e-13

# Unique-extremum pattern sampled densely on either side.
left=[10.0**(-6.0+6.0*j/4000.0) for j in range(4000)]
prev=phi_cos_closed(left[0])
prev_t=phi_tan_closed(left[0])
for G in left[1:]:
    c=phi_cos_closed(G)
    t=phi_tan_closed(G)
    assert c < prev + 1e-15
    assert t > prev_t - 1e-15
    prev,prev_t=c,t
assert phi_cos_closed(1.0)==0.5
assert phi_tan_closed(1.0)==1.0

# Endpoint limits.
lim_cos=0.5*(1.0+math.tanh(1.0))
assert abs(phi_cos_closed(1e-10)-lim_cos) < 2e-10
assert abs(phi_cos_closed(1e10)-lim_cos) < 2e-10
assert abs(phi_tan_closed(1e-10)-0.5) < 2e-10
assert abs(phi_tan_closed(1e10)-0.5) < 2e-10

# Exact crossover amplitudes and sign regions.
z=1.0+math.sqrt(5.0)
d=math.sqrt(2.0+2.0*math.sqrt(5.0))
Gm=(z-d)/2.0
Gp=(z+d)/2.0
assert abs(Gm*Gp-1.0) < 2e-15
for G in (Gm,Gp):
    assert abs(phi_cos_closed(G)-phi_tan_closed(G)) < 2e-14
for G in (0.1,0.3,3.2,10.0):
    assert phi_cos_closed(G) > phi_tan_closed(G)
for G in (0.5,0.9,1.0,1.1,2.0):
    assert phi_tan_closed(G) > phi_cos_closed(G)

# Direct alternating-angle replay: after t>=3 both adjacent angles equal A(G).
for G in (0.2,0.7,1.0,1.8,5.0):
    gs=[None]+[(G if t%2 else -G) for t in range(1,8)]
    As={}
    for t in range(2,8):
        den=1.0+gs[t]*gs[t-1]
        if abs(den) < 1e-15:
            As[t]=math.pi/2.0
        else:
            As[t]=math.atan(abs((gs[t]-gs[t-1])/den))
    for t in range(3,8):
        assert abs(As[t]-As[t-1]) < 2e-15
        assert abs(min(As[t-1],As[t])-paper_angle(G)) < 2e-15

print('verification passed')
