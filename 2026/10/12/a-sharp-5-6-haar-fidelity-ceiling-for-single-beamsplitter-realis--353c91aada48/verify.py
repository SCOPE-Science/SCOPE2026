from fractions import Fraction

# Bell labels phi+,phi-,psi+,psi-. Equal priors 1/4.
# For every polarization-preserving beamsplitter and number-resolving photon counting,
# phi+ and phi- have identical output distributions, hence their total MAP contribution
# is at most max(1/4,1/4)=1/4. psi pair can contribute at most 1/2.
p_map_upper = Fraction(3,4)
# Standard 50:50 Bell analyzer distinguishes psi+ and psi- and distinguishes their
# supports from the common phi support; a random/MAP tie-break within phi gives 1/4.
p_map_attained = Fraction(1,2) + Fraction(1,4)
assert p_map_attained == p_map_upper

# Haar mean of a nonidentity Pauli fidelity for a pure qubit is 1/3.
# Bloch r uniform on S^2: E[r_j^2]=1/3.
f_wrong = Fraction(1,3)
f_correct = Fraction(1,1)
f_avg = p_map_upper*f_correct + (1-p_map_upper)*f_wrong
assert f_avg == Fraction(5,6)

# A coordinate-uniform polar-angle weighting (not Haar) would give E[cos^2 theta]=1/2,
# hence the familiar 7/8 = .875 ~ .88 at the same analyzer. This is only a diagnostic,
# not an assertion about the source's implementation.
f_wrong_uniform_theta = Fraction(1,2)
f_uniform_theta = p_map_upper + (1-p_map_upper)*f_wrong_uniform_theta
assert f_uniform_theta == Fraction(7,8)

print('VERIFY_OK')
print('p_MAP_max =', p_map_upper)
print('Haar_wrong_Pauli_fidelity =', f_wrong)
print('Haar_F_max =', f_avg)
print('uniform_theta_diagnostic =', f_uniform_theta)
