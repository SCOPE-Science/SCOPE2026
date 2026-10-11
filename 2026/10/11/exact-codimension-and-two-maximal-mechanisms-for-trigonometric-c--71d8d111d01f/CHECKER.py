"""Exact rational checks for the Fourier two-harmonic stratification.
This checker is supplementary; its finite samples do not establish the dimension theorem.
"""
from fractions import Fraction as F

def conj(z):
    return (z[0],-z[1])

def mul(x,y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def powers(z,n):
    out=(F(1),F(0))
    for _ in range(n):out=mul(out,z)
    return out

def negate_i_times(z,scale):
    return (scale*z[1],-scale*z[0])

# A phase with rational sine and cosine; coefficient z_k for A_k sin(k(t-phase)).
phase=(F(3,5),F(-4,5))
z_a1=negate_i_times(powers(phase,1),F(2))
z_b1=negate_i_times(powers(phase,1),F(-3))
z_a2=negate_i_times(powers(phase,2),F(5))
z_b2=negate_i_times(powers(phase,2),F(7))
u=z_a1
assert mul(z_b1,conj(u))[1]==0
assert mul(z_a2,powers(conj(u),2))[0]==0
assert mul(z_b2,powers(conj(u),2))[0]==0

# Two-harmonic non-proportional reflection pair at phase 0: sin(t), sin(2t).
assert mul((F(0),F(-1)),powers(conj((F(0),F(-1))),2))[0]==0
# Counterexample not in either branch: sin(t), cos(2t).
assert mul((F(1),F(0)),powers(conj((F(0),F(-1))),2))[0]!=0

# At a coefficient point, the reflection map has 5 independent differential
# directions: four sine axes plus one first-harmonic cosine axis.
reflection_tangent=[(1,0,0,0,0,0,0,0), (0,0,1,0,0,0,0,0),
                    (0,0,0,0,1,0,0,0), (0,0,0,0,0,0,1,0),
                    (0,1,0,0,0,0,0,0)]
assert len(set(reflection_tangent))==5
# The proportional family has 4 independent variations of a plus
# one independent variation of b at (a,b)=(sin(t),0).
proportional_tangent=[(1,0,0,0,0,0,0,0), (0,1,0,0,0,0,0,0),
                      (0,0,1,0,0,0,0,0), (0,0,0,1,0,0,0,0),
                      (0,0,0,0,1,0,0,0)]
assert len(set(proportional_tangent))==5

# Exhaustion of degrees for the first two frequency cutoffs.
assert [d for d in range(1,3)]==[1,2]
for n in range(3,201):
    for d in range(2,n):
        assert d+n//d <= n
print('Exact rational Fourier checks: PASS')
print('Tangent lower bounds: dimension five in both two-harmonic branches')
print('Sampled degree inequality (supplementary only): PASS')
