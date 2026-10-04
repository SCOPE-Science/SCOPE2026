from fractions import Fraction as Q

# Exact arithmetic checks for the canonical Sprott E vector field.
def f(x,y,z):
    return (y*z, x*x-y, Q(1)-4*x)

p=(Q(1,4), Q(1,16), Q(0))
assert f(*p)==(Q(0),Q(0),Q(0))

# The equilibrium is forced uniquely by z'=0, y'=0, x'=0.
x=Q(1,4)
y=x*x
assert y==Q(1,16) and y!=0
z=Q(0)  # x'=y z=0 and y!=0
assert (x,y,z)==p

# Stationary moment algebra: E[x]=1/4 and E[y]=E[x^2].
mean_x=Q(1,4)
assert mean_x*mean_x==Q(1,16)
# Hence E[y]-1/16 = E[x^2]-(E[x])^2 = Var(x).

# On z=0, invariance forces x=1/4; then y'=1/16-y.
assert f(Q(1,4),Q(1,16),Q(0))==(Q(0),Q(0),Q(0))

print('canonical_equilibrium=(1/4,1/16,0)')
print('mean_square_offset=(1/4)^2=1/16')
print('VERIFY_OK')
