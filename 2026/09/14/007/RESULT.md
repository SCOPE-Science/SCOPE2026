# Interior one-third cusp for the three-point free power: nonexistence with full classification

## Context

Let mu = (delta_{-1} + delta_0 + delta_1)/3 and let mu^{boxplus t}, t >= 1, be its
Nica-Speicher free additive convolution power. The admitted target asks whether
there exist t in (1, 3/2) and an interior point x0 of supp(mu^{boxplus t}),
not a support-component endpoint and distinct from surviving atoms, with
p_t(x0) = 0 and p_t(x) = C |x - x0|^{1/3} (1 + o(1)) for some C > 0, as opposed
to square-root edge vanishing or strict positivity. A complete answer is either
an explicit (t, x0) with proof of the cubic-root rate, or a proof of
nonexistence with classification of all zeros.

## Definitions

G_mu(w) = (1/3)(1/(w+1) + 1/w + 1/(w-1)) = (3w^2 - 1)/(3w(w^2 - 1)) is the Cauchy
transform of mu; F_mu = 1/G_mu. For t > 1 the Bercovici-Voiculescu subordination
gives an analytic map omega_t: C^+ -> C^+ with G_t = G_mucirc omega_t and
H_t(omega_t(z)) = z, where H_t(w) = t w - (t-1) F_mu(w)
= w(3w^2 + 2t - 3)/(3w^2 - 1). The equation H_t(w) = x is
P_{t,x}(w) := 3w^3 - 3xw^2 + (2t-3)w + x = 0.
The density of the absolutely continuous part is p_t = -Im G_t/pi where
omega_t takes values in C^+. Atoms satisfy x = t a with mu({a}) > 1 - 1/t.

## Result

For every t >= 1 there is no interior point x0 of supp(mu^{boxplus t})
(not a component endpoint, distinct from atoms) with p_t(x0) = 0 and rate
|x - x0|^{1/3}. Precisely:

(a) For 1 < t < 3/2 the a.c. part is supported on two symmetric bands
+- (sqrt(y1), sqrt(y2)) with 0 < y1 < y2 < t^2; p_t > 0 strictly inside each
band; the four endpoints are square-root edge zeros; atoms of mass 1 - 2t/3
sit at -t, 0, t in the gaps. No interior zero at all.

(b) For t = 3/2, supp = [-3/2, 3/2] with no atoms; p_{3/2}(x) > 0 on
(-3/2, 0) union (0, 3/2), with interior pole
p_{3/2}(x) = C |x|^{-1/3}(1 + o(1)), C = 3^{5/6}/(6 pi), and inverse
square-root blow-ups at +- 3/2. No zeros inside.

(c) For t > 3/2 there is a single band (-b, b) with p_t > 0 inside and
square-root edge zeros at +- b, no atoms. At t = 1 the measure is purely
atomic. The unique cubic degeneracy with t > 1 is (t, w) = (3/2, 0), which
produces the -1/3 blow-up above, never a +1/3 zero.

## Proof / evidence

Derivatives: H_t'(w) = (9w^4 - 6tw^2 + 3 - 2t)/(3w^2 - 1)^2 and
H_t''(w) = 36(t-1)w(w^2 + 1)/(3w^2 - 1)^3. Hence H_t''(w) = 0 iff
w in {0, +- i}; H_t'(+- i) = (3+t)/4 != 0, and H_t'(0) = 3 - 2t vanishes only
at t = 3/2, where H_{3/2}(w) = 3w^3/(3w^2 - 1) has a triple root at 0. Since
w = 0 is a pole of G_mu, this cubic point is a -1/3 pole, not a +1/3 zero.
The cubic discriminant is disc_w P_{t,x} = 12 Q(t,x) with
Q = 9x^4 + Bx^2 + C, B = 3t^2 - 36t + 27, C = (3 - 2t)^3; in y = x^2,
R(y) = 9y^2 + By + C has y-discriminant 9(t-1)(t+3)^3 and
R(t,t^2) = (2t-3)^2(3t^2 - 2t + 3). This yields the band structure:
Q < 0 exactly on the stated bands, Q > 0 on gaps containing the atoms
+-t, 0. Real critical points are simple except (3/2, 0); for 1 < t < 3/2
they are v = +- sqrt(s_+-) in (-1,1) \ {0} with G_mu regular, nonzero, and
G_mu'(v) != 0 (since G_mu' numerator is -(3w^4+1) > 0 on R), giving one-sided
square-root vanishing; for t > 3/2 the same holds at v = +- sqrt(s_+),
|v| > 1; at t = 3/2 the preimages +-1 are poles (inverse-sqrt blow-ups).
The pole constant follows from 3w^3 + x approx 0, upper branch
w_+ = (x/3)^{1/3} e^{i pi/3}, G_mu(w) = 1/(3w) + O(w), giving the stated C.
All symbolic identities were verified with residual 0; numeric checks confirm
strict interior positivity, the t = 3/2 zero set, and the blow-up constant
(see output/artifacts/verify_target.py and verify_output.txt).

## Limitations

The result is specific to the symmetric three-point law
(delta_{-1}+delta_0+delta_1)/3. The local cubic analysis uses direct root
perturbation of the explicit cubic P_{t,x} together with the cited
Bercovici-Voiculescu subordination and Huang atomic/square-root-edge boundary
regularity for free convolution powers of finitely supported laws.

## Reproducibility

Run python3 output/artifacts/verify_target.py; expect all symbolic residuals 0
and ALL CHECKS PASSED, with details in output/artifacts/verify_output.txt.

## References

H. Huang, Supports of Measures in a Free Additive Convolution Semigroup,
IMRN 2015; S. T. Belinschi, The Lebesgue decomposition of the free additive
convolution (2007); S. T. Belinschi and H. Bercovici, Atoms and regularity
for measures in a partially defined free convolution semigroup (2004);
Z. Bao, L. Erdos, K. Schnelli, On the support of the free additive
convolution (2018); P. Moreillon, Density of the free additive convolution
of multi-cut measures, arXiv:2209.15607.
