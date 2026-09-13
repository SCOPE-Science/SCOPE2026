# Brown Measure of s1^2+s1 s2 Has No Atom at Zero

## Context

Let (M,tau) be a tracial W*-probability space and let s1, s2 in M be freely independent standard semicircular variables (selfadjoint, mean zero, variance one). Let p1 = s1^2 + s1 s2 and let mu1 be its Brown measure. The admitted target asked for the exact atom mass mu1({0}) and the exact support-gap radius r1 around zero. This record resolves the first component exactly and leaves the second explicitly open.

## Definitions

The Fuglede-Kadison determinant is Delta(x) = exp(tau(log|x|)) with exp(-infinity) := 0. For any x with Brown measure mu_x, log Delta(x - lambda) = integral_C log|z - lambda| d mu_x(z) for all lambda (Haagerup-Schultz logarithmic identity). The factors a = s1 and b = s1 + s2 have centred semicircular laws of variance 1 and 2 with densities rho1(t) = sqrt(4-t^2)/(2 pi) on [-2,2] and rho2(t) = sqrt(8-t^2)/(4 pi) on [-2 sqrt(2), 2 sqrt(2)], both bounded with compact support.

## Result

mu1({0}) = 0. That is, the Brown measure of p1 has no atom at zero. Sharply, Delta(s1) = e^{-1/2}, Delta(s1+s2) = sqrt(2) e^{-1/2}, and Delta(p1) = sqrt(2)/e > 0 (approximately 0.60653, 0.85776, 0.52026).

## Proof / Evidence

Factor p1 = s1 (s1 + s2) = a b. Boundedness of rho1 and rho2 makes t -> log|t| integrable, so Delta(a) > 0 and Delta(b) > 0. For the centred semicircular law of variance sigma^2, scaling gives I(sigma) = log sigma + I(1) where I(sigma) = integral log|t| rho^{(sigma)}(t) dt. With t = 2 sin theta, I(1) = (1/pi) integral_0^2 log t sqrt(4-t^2) dt = J/pi with J = 4 log 2 integral_0^{pi/2} cos^2 + 4 integral_0^{pi/2} cos^2 log sin; using integral_0^{pi/2} cos^2 = pi/4, integral log sin = -(pi/2) ln 2, and integral sin^2 log sin = pi/8 - (pi/4) ln 2 (via differentiating F(p) = integral sin^p with digamma values), J = -pi/2, i.e. I(1) = -1/2. Hence Delta(a) = e^{-1/2}, Delta(b) = sqrt(2) e^{-1/2}, and by FK multiplicativity Delta(xy) = Delta(x)Delta(y), Delta(p1) = sqrt(2)/e > 0 with log Delta(p1) approx -0.653. Then integral log|z| d mu1(z) = log Delta(p1) > -infinity. But p1 is bounded (||p1|| <= 8) so mu1 is compactly supported; if mu1({0}) = m > 0 then integral log|z| d mu1 <= C - n m -> -infinity, a contradiction. Hence m = 0. Numerical quadrature on a 400001-point grid gives I1 = -0.499996, I2 = -0.153423, Delta(p1) = 0.520264, matching the exact values to better than 1e-3 (see output/artifacts/fk_atom_check.py).

## Limitations

This record proves only mu1({0}) = 0. It does not determine the support-gap radius r1 (whether mu1({z: 0 < |z| < r}) = 0 for some r > 0). The Hermitized-linearization / operator-valued-subordination edge analysis at z = 0 and any small-ball estimate near zero were attempted but did not close to proof standard, so no value of r1 is claimed.

## Reproducibility

Run python3 output/artifacts/fk_atom_check.py (requires numpy). It recomputes tau(log|s1|), tau(log|s1+s2|), and log Delta(p1) by direct quadrature against the bounded semicircle densities, asserts agreement with -1/2 and log(sqrt(2))-1/2 to 1e-3, and confirms strict positivity of all three determinants.

## References

L. G. Brown, Lidskii's theorem in the type II case; Fuglede-Kadison, Determinant theory in finite factors; Haagerup-Schultz, Invariant subspaces for operators in a general II_1-factor; Mingo-Speicher, Free Probability and Random Matrices (Brown measure chapter); Ho, The Brown measure of unbounded variables with free semicircular imaginary part (arXiv:2011.14222, scope-compared non-covering lead).
