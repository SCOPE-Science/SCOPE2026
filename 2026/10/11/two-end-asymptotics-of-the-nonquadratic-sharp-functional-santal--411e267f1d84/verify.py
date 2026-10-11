import math
for n in range(2,41):
    # Use an arbitrary positive k satisfying the strict test range; coefficient identities are algebraic in k.
    k = 1.137 + 0.013*n
    a = k**(-1.0/n)
    c0 = k**(1.0/n)/math.sqrt(2.0)
    cinf = math.sqrt(2.0)/k**(1.0/n)
    assert abs(c0*cinf-1.0) < 1e-12
    coeff0_profile = 2.0**((n-1)/2.0)*a**(n-1)/(n*(n+1))
    coeff0_final = 1.0/(n*(n+1)*c0**(n-1))
    assert abs(coeff0_profile/coeff0_final-1.0) < 1e-11
    b = k**(1.0/n)
    coeff_inf_raw = ((n+1)**(n/(n+1))/n
                     * 2.0**((2*n+1)/(2*(n+1)))
                     * b**(-(2*n+1)/(n+1)))
    coeff_inf_final = ((n+1)**(n/(n+1))/n
                       * cinf**((2*n+1)/(n+1)))
    assert abs(coeff_inf_raw/coeff_inf_final-1.0) < 1e-11
print('VERIFY_OK dimensions=2..40 coefficient_identities=passed')
