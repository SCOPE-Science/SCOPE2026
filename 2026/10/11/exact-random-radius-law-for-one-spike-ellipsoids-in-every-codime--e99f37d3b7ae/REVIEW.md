# Same-model review

## Correctness

PASS. The ellipsoid quadratic form is a scalar operator plus a single rank-one perturbation. Its compression to a codimension-\(n\) subspace therefore has only one nontrivial eigenvalue,
\[
b^{-2}-(b^{-2}-a^{-2})\|P_Ee_1\|^2.
\]
For a Haar random subspace, the complementary squared projection is exactly
\[
\operatorname{Beta}\!\left(\frac n2,\frac{N-n}{2}\right).
\]
This proves the distributional representation. The CDF is a monotone inversion, the moments follow from Euler's beta integral, and the proportional-dimensional limit follows from the exact beta variance. The checker independently replays the compression and integral identities.

## Originality

PASS. The recent source and the earlier full ellipsoid paper provide broad high-probability, expected-radius, and asymptotic-order results. Neither inspected paper states the exact one-spike beta law, finite CDF, all-moment formula, or finite factor-\(C\) random-versus-optimal success curve. Targeted searches under one-spike, axisymmetric, beta-law, exact-distribution, and random-information terminology found no covering theorem.

## Value

PASS. The one-spike ellipsoid is a canonical anisotropic test family for the random-information problem. The complete law gives a sharp finite benchmark in every codimension and shows that, under proportional codimension and extreme anisotropy, the random/optimal radius ratio converges exactly to
\[
\lambda^{-1/2}.
\]
Thus the general \(\sqrt{N/n}\) degradation mechanism is realized with its exact leading constant on a natural family.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest sources are Guedon--Litvak--Tatarko--Vritsiou on random diameters of convex bodies and Hinrichs--Krieg--Novak--Prochno--Ullrich on random sections of Hilbert ellipsoids. They give the governing framework and strong general estimates but do not determine this finite distribution.

The theorem relies on the one-spike rank-one structure. It does not produce a comparable closed law for ellipsoids with several distinct semiaxis levels. An equivalent formula may exist under older random-compression or multivariate-statistics terminology; this remains the main originality risk.
