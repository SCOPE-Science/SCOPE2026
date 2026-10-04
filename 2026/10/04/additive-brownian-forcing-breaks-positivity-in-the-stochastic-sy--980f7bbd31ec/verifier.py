from collections import Counter
from math import exp, sqrt, erf

# Symbolic bookkeeping for the twelve drifts in Eq. (24).
# A transfer label appears with opposite signs in its source and destination.
D = []
def c(**kw):
    return Counter(kw)
D.append(c(pi_m=1, phi_m_Rm=1, inf_m=-1, mu_Sm=-1))
D.append(c(inf_m=1, gamma_m_Imp=-1, mu_Imp=-1, tr_m1=-1))
D.append(c(gamma_m_Imp=1, beta_m_Ims=-1, tr_m2=-1, mu_Ims=-1))
D.append(c(beta_m_Ims=1, mu_Lm=-1, tr_m3=-1, delta_m_Lm=-1))
D.append(c(tr_m1=1, tr_m2=1, tr_m3=1, mu_Rm=-1, phi_m_Rm=-1))
D.append(c(pi_f=1, phi_f_Rf=1, inf_f=-1, pi_p_Sf=-1, mu_Sf=-1))
D.append(c(inf_f=1, gamma_f_Ifp=-1, mu_Ifp=-1, rho_f1=-1, pi_p_Ifp=-1, delta_f_Ifp=-1))
D.append(c(gamma_f_Ifp=1, beta_f_Ifs=-1, rho_f2=-1, mu_Ifs=-1, pi_p_Ifs=-1, delta_f_Ifs=-1))
D.append(c(beta_f_Ifs=1, mu_Lf=-1, rho_f3=-1, pi_p_Lf=-1, delta_f_Lf=-1))
D.append(c(rho_f1=1, rho_f2=1, rho_f3=1, pi_p_Ifp=1, pi_p_Ifs=1, pi_p_Lf=1, kappa_pi_p_Ifp=-1, kappa_pi_p_Ifs=-1, kappa_pi_p_Lf=-1, mu_Rf=-1, phi_f_Rf=-1))
D.append(c(kappa_pi_p_Ifp=1, kappa_pi_p_Ifs=1, kappa_pi_p_Lf=1, mu_C=-1, delta_c_C=-1))
D.append(c(delta_m_Lm=1, delta_f_Ifp=1, delta_f_Ifs=1, delta_f_Lf=1, delta_c_C=1, mu_D=-1))
S = {}
for row in D:
    for key, value in row.items():
        S[key] = S.get(key, 0) + value
S = {k: v for k, v in S.items() if v}
expected_c = c(pi_m=1, pi_f=1, pi_p_Sf=-1, mu_Sm=-1, mu_Imp=-1, mu_Ims=-1, mu_Lm=-1, mu_Rm=-1, mu_Sf=-1, mu_Ifp=-1, mu_Ifs=-1, mu_Lf=-1, mu_Rf=-1, mu_C=-1, mu_D=-1)
expected = dict(expected_c)
assert S == expected, (S, expected)

# Representative evaluation of the strictly positive Gaussian tail.
mu = 1.0
Pi = 2.0
T0 = 12.0
sigma2 = 12 * (0.5 ** 2)
t = 1.0
m = T0 * exp(-mu*t) + Pi/mu * (1-exp(-mu*t))
v = sigma2/(2*mu) * (1-exp(-2*mu*t))
z = -m/sqrt(v)
Phi = 0.5*(1+erf(z/sqrt(2)))
assert v > 0 and Phi > 0
print('VERIFY_OK')
