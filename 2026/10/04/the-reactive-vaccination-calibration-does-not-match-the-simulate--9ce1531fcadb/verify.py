from decimal import Decimal as D, getcontext

getcontext().prec = 60
T = D(150)
VE = D('0.93')
Sinf = D('0.067')
S0 = D('0.33')
S1 = D('0.22')
H0 = D('0.165')
H1 = D('0.11')

# Supplementary affine target-relaxation calibration:
# S(T) = Sinf + (S(0)-Sinf) exp(-nu T).
nu0 = -((H0 - Sinf) / (S0 - Sinf)).ln() / T
nu1 = -((H1 - Sinf) / (S1 - Sinf)).ln() / T
assert abs(nu0 - D('0.006581243690047950876386591039070240420238761643604')) < D('1e-50')
assert abs(nu1 - D('0.008461585371325820263781217189148872728826986288998')) < D('1e-50')

def affine_endpoint(s0, nu):
    return Sinf + (s0 - Sinf) * (-nu*T).exp()

assert abs(affine_endpoint(S0, nu0) - H0) < D('1e-50')
assert abs(affine_endpoint(S1, nu1) - H1) < D('1e-50')

# Main/article-and-code multiplicative vaccination-only law:
# S(T) = S(0) exp(-nu VE T).
nu_half = D(2).ln() / (VE*T)
assert abs(nu_half - D('0.0049687969932612566983314130570478607030501801746255')) < D('1e-50')

def multiplicative_endpoint(s0, nu):
    return s0 * (-nu*VE*T).exp()

assert abs(multiplicative_endpoint(S0, nu_half) - H0) < D('1e-50')
assert abs(multiplicative_endpoint(S1, nu_half) - H1) < D('1e-50')

m0 = multiplicative_endpoint(S0, nu0)
m1 = multiplicative_endpoint(S1, nu1)
assert abs(m0 - D('0.13176356729605854555009192388968474372649127524735')) < D('1e-50')
assert abs(m1 - D('0.067574884777283111884249289880675013071871071669830')) < D('1e-50')
assert m0 != H0 and m1 != H1

# Scenario rates actually explored in the source do not halve susceptibility
# over 150 days under the multiplicative vaccination-only law.
for rate in (D('0.001'), D('0.002'), D('0.003')):
    ratio = (-rate*VE*T).exp()
    assert ratio > D('0.5')

print('VERIFY_OK')
