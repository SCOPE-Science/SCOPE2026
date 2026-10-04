from fractions import Fraction as F

# The two diagonal diffusion terms each carry sigma_j^2 = 0.02*(1-w)^2*...
# and the Hamiltonian definition has an overall factor 1/2 on their sum.
assert F(1,2) * 2 * F(2,100) == F(1,50)  # 0.02 before q_SS+q_II
# After factoring q_SS+q_II as a single sum, the coefficient is 0.01 per summed Hessian expression.
assert F(1,2) * F(2,100) == F(1,100)

# H_aug(w) = beta2/2*w^2 + beta1*w - d*w - D*(1-w)^2 + eps*(w-u)^2 + const.
beta2=F(4); beta1=F(1); d=F(2); D=F(1,2); eps=F(1); u=F(1,4)
quad = beta2/F(2) - D + eps
lin = beta1 - d + 2*D - 2*eps*u
assert 2*quad == beta2 + 2*eps - 2*D
true_root = -lin/(2*quad)
formula_root = (d-beta1-2*D+2*eps*u)/(beta2+2*eps-2*D)
assert true_root == formula_root == F(1,10)

# The printed expression uses the scalar value r(u), not the coefficient/derivative needed by minimization.
r_u = d*u + D*(1-u)*(1-u)
printed = (r_u + 2*eps*u - beta1)/(beta2+2*eps)
assert printed == F(3,64)
assert printed != true_root

# Fixed-point inference obstruction: H(w)=-w^2, u*=0, eps=2 on [0,1].
# H_aug(w)=w^2 is minimized at zero, but H itself is smaller at w=1.
def H(w): return -w*w
def Haug(w): return H(w)+F(2)*w*w
assert Haug(F(0)) <= Haug(F(1))
assert H(F(1)) < H(F(0))

print('VERIFY_OK')
