import math
import itertools

# Parameters used in Fig. 2 / Sec. IV.2 of arXiv:2609.20710v1.
g = 10.0/7.0
h = 8.0/5.0
A = 0.1
sigma_g = -1
sigma_h = -1
s_k = 1

alpha = math.acos((h*h - g**-2 - 1.0)/(2.0*g**-1))
beta = math.acos((g**-2 - h*h - 1.0)/(2.0*h))

def cvec(r, theta):
    return complex(r*math.cos(theta), r*math.sin(theta))

# One planar realization of the three affine-related triads satisfying Eq. (14).
K = cvec(1.0, 0.0)
P = cvec(g**-1, -alpha)
Q = cvec(h, beta)
KHINV = cvec(h**-1, -beta)
PHINV = cvec((g*h)**-1, -(alpha+beta))
KG = cvec(g, alpha)
QG = cvec(g*h, alpha+beta)

support = {
    'k': K,
    'p': P,
    'q': Q,
    'kh^-1': KHINV,
    'ph^-1': PHINV,
    'kg': KG,
    'qg': QG,
}

triad_residuals = [abs(K+P+Q), abs(K+KHINV+PHINV), abs(K+KG+QG)]

# Cross-triplet pair p and qg forces the missing wavevector k_ext=-(p+qg).
k_ext = -(P + QG)
k_ext_mag = abs(k_ext)
min_support_distance = min(abs(k_ext-v) for v in support.values())
min_signed_support_distance = min(abs(k_ext-eps*v) for v in support.values() for eps in (1.0,-1.0))

# Confirm that, after the physical real-valued completion by conjugate wavevectors,
# (-p,-qg) is the unique unordered support pair summing to k_ext.
signed = []
for name, v in support.items():
    signed.append((name, v))
    signed.append(('-'+name, -v))
unique_pairs = []
for i, (n1, v1) in enumerate(signed):
    for n2, v2 in signed[i:]:
        if abs(v1+v2-k_ext) < 1e-12:
            unique_pairs.append((n1,n2))

# Source helicities for sigma_g=sigma_h=-1:
# s_p=s_k sigma_g=-1, s_qg=s_k sigma_g sigma_h=+1.
s_p = s_k*sigma_g
s_qg = s_k*sigma_g*sigma_h
p_mag = abs(P)
qg_mag = abs(QG)

# Since p<|k_ext|<qg, use the source's Eq. (5) with k_ext as the middle leg.
alpha_ext = math.acos((qg_mag*qg_mag-k_ext_mag*k_ext_mag-p_mag*p_mag)/(2*k_ext_mag*p_mag))
beta_ext = math.acos((p_mag*p_mag-k_ext_mag*k_ext_mag-qg_mag*qg_mag)/(2*qg_mag*k_ext_mag))

# At t=0, Eq. (43) with f_nr=1,f_ni=0 gives
# u_p=-i A g^(1/3), u_qg=+i A g^(-1/3) h^(-1/3),
# hence conj(u_p)conj(u_qg)=A^2 h^(-1/3).
amp_product = A*A*h**(-1.0/3.0)

rows = []
for s_ext in (+1,-1):
    s_prod = s_ext*s_p*s_qg
    Qgeom = 0.25*s_prod*math.sin(alpha_ext+beta_ext)*(
        s_ext + s_p*p_mag/k_ext_mag + s_qg*qg_mag/k_ext_mag
    )
    coeff = Qgeom*(s_p*p_mag-s_qg*qg_mag)
    du = coeff*amp_product
    rows.append((s_ext,Qgeom,coeff,du))

print('alpha = %.15f' % alpha)
print('beta = %.15f' % beta)
print('intended_triad_max_residual = %.3e' % max(triad_residuals))
print('k_ext = (%.15f, %.15f)' % (k_ext.real,k_ext.imag))
print('|k_ext| = %.15f' % k_ext_mag)
print('min_distance_to_7_mode_support = %.15f' % min_support_distance)
print('min_distance_to_signed_support = %.15f' % min_signed_support_distance)
print('support_pairs_summing_to_k_ext = %r' % (unique_pairs,))
print('p_mag = %.15f' % p_mag)
print('qg_mag = %.15f' % qg_mag)
print('alpha_ext = %.15f' % alpha_ext)
print('beta_ext = %.15f' % beta_ext)
print('amp_product = %.15f' % amp_product)
for s_ext,Qgeom,coeff,du in rows:
    print('s_ext=%+d Q=%.15f interaction_coeff=%.15f du_dt=%.15f' % (s_ext,Qgeom,coeff,du))

assert max(triad_residuals) < 1e-12
assert min_signed_support_distance > 1e-3
assert unique_pairs == [('-p','-qg')]
assert all(abs(row[3]) > 1e-6 for row in rows)
print('all_checks_passed=True')
