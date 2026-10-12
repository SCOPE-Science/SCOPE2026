import mpmath as mp

mp.mp.dps = 70

def phi(u, theta, c):
    return (theta-1)*(mp.e**u+c) + theta*c*u

def hazard(x, alpha, theta, gamma):
    c = 2*alpha-1
    u = gamma*x**theta
    return theta*gamma*mp.e**u*x**(theta-1)/(mp.e**u+c)

def hprime_formula(x, alpha, theta, gamma):
    c = 2*alpha-1
    u = gamma*x**theta
    pref = theta*gamma*x**(theta-2)*mp.e**u/(mp.e**u+c)**2
    return pref*phi(u,theta,c)

def Aplus(theta):
    return (theta-1)/theta*mp.e**(1/theta)

def Aminus(theta):
    return (1-theta)/theta*mp.e**(1/theta)

# Differentiate the actual hazard and compare with the closed derivative.
for alpha,theta,gamma,x in [
    (mp.mpf("0.03"),mp.mpf("2.52"),mp.mpf("0.03"),mp.mpf("2")),
    (mp.mpf("5"),mp.mpf("0.5"),mp.mpf("1"),mp.mpf("4")),
    (mp.mpf("0.7"),mp.mpf("1"),mp.mpf("2"),mp.mpf("1.3")),
]:
    num = mp.diff(lambda z: hazard(z,alpha,theta,gamma), x)
    form = hprime_formula(x,alpha,theta,gamma)
    assert abs(num-form) < mp.mpf("1e-55")

# Source simulation parameters.
alpha = mp.mpf("0.03")
theta = mp.mpf("2.52")
gamma = mp.mpf("0.03")
c = 2*alpha-1
A = Aplus(theta)
acrit = (1-A)/2
assert alpha < acrit

# Unique minimum is negative.
u_star = mp.log((-c)*theta/(theta-1))
assert abs(u_star-mp.mpf("0.4436731629470593")) < mp.mpf("1e-15")
assert phi(u_star,theta,c) < 0

# Find the two roots.
root1 = mp.findroot(lambda u: phi(u,theta,c), (mp.mpf("0.05"),mp.mpf("0.2")))
root2 = mp.findroot(lambda u: phi(u,theta,c), (mp.mpf("0.5"),mp.mpf("0.9")))
assert 0 < root1 < u_star < root2
x1 = (root1/gamma)**(1/theta)
x2 = (root2/gamma)**(1/theta)

# Sign sequence + - +.
for u,sgn in [
    (root1/2,1),
    ((root1+root2)/2,-1),
    (root2+1,1),
]:
    assert mp.sign(phi(u,theta,c)) == sgn

# Exact threshold equality: one zero at u=1/theta.
c_eq = -A
u_eq = 1/theta
assert abs(phi(u_eq,theta,c_eq)) < mp.mpf("1e-60")
assert phi(u_eq-mp.mpf("0.1"),theta,c_eq) > 0
assert phi(u_eq+mp.mpf("0.1"),theta,c_eq) > 0

# Simple theta>1 counterexample: source theorem predicts increasing but derivative is negative.
alpha_a=mp.mpf("0.01"); theta_a=mp.mpf("2"); gamma_a=mp.mpf("1"); x_a=mp.mpf("1")
c_a=2*alpha_a-1
assert phi(mp.mpf("1"),theta_a,c_a) < 0
assert hprime_formula(x_a,alpha_a,theta_a,gamma_a) < 0

# Simple theta<1 counterexample: source theorem predicts decreasing but derivative is positive.
alpha_b=mp.mpf("5"); theta_b=mp.mpf("0.5"); gamma_b=mp.mpf("1"); x_b=mp.mpf("4")
c_b=2*alpha_b-1
u_b=gamma_b*x_b**theta_b
assert abs(u_b-2) < mp.mpf("1e-60")
assert phi(u_b,theta_b,c_b) > 0
assert hprime_formula(x_b,alpha_b,theta_b,gamma_b) > 0

# Dual threshold classification check.
B = Aminus(theta_b)
assert c_b > B
broot1 = mp.findroot(lambda u: phi(u,theta_b,c_b), mp.mpf("1.5"))
broot2 = mp.findroot(lambda u: phi(u,theta_b,c_b), mp.mpf("2.8"))
assert 0 < broot1 < broot2

print("VERIFY_OK")
print("source_Aplus", mp.nstr(A, 30))
print("source_alpha_threshold", mp.nstr(acrit, 30))
print("source_u_roots", mp.nstr(root1,30), mp.nstr(root2,30))
print("source_x_roots", mp.nstr(x1,30), mp.nstr(x2,30))
print("simple_theta2_phi_at_u1", mp.nstr(phi(1,theta_a,c_a),30))
print("simple_theta_half_phi_at_u2", mp.nstr(phi(2,theta_b,c_b),30))
