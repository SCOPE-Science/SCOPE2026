from fractions import Fraction as F

Pi=F(2)
alpha=F(1,2)
eta=F(1)
mu=F(1)
p=F(1,2)
omega=F(1)
xi=F(0)

V_inf=alpha*Pi/(eta+mu)
residual=(1-p)*eta*V_inf
h=omega+mu+xi
floor=residual/h

assert V_inf == F(1,2)
assert residual == F(1,4)
assert floor == F(1,8)
assert residual > 0 and floor > 0
print("VERIFY_OK")
