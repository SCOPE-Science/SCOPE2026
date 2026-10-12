# Small-rate log-convexity disproves universal DGM PMF log-concavity
## Finding
For the discrete Gompertz–Makeham (DGM) distribution,
\[
S_z=
\exp\!\left[
-\alpha z-\frac{\theta}{\mu}\left(e^{\mu z}-1\right)
\right],
\qquad
p_z=S_z-S_{z+1},
\qquad z=0,1,2,\ldots,
\]
with \(\alpha,\theta,\mu>0\), the probability mass function is **not** log-concave for every admissible parameter triple.

A robust low-rate obstruction is available. Fix arbitrary \(a,b,\mu>0\), set
\[
\alpha=\varepsilon a,\qquad
\theta=\varepsilon b,\qquad
r=e^\mu,\qquad
c=\frac{b}{\mu}(r-1),
\]
and let \(\varepsilon\downarrow0\). For each fixed \(z\ge1\),
\[
p_z^2-p_{z-1}p_{z+1}
=
-\varepsilon^2 a c r^{z-1}(r-1)^2
+O(\varepsilon^3).
\]
The leading coefficient is strictly negative. Therefore, for every fixed integer \(m\ge1\), there is an \(\varepsilon_m>0\) such that
\[
p_z^2<p_{z-1}p_{z+1}
\qquad
(1\le z\le m)
\]
whenever \(0<\varepsilon<\varepsilon_m\). Thus an arbitrarily long initial segment of the DGM PMF can be strictly log-convex.

A concrete admissible instance is
\[
\mu=\log 2,\qquad
\alpha=0.01,\qquad
\theta=0.01\log 2.
\]
Then
\[
p_0=0.0198013266932446977\ldots,
\]
\[
p_1=0.0289692488060412931\ldots,
\]
and
\[
p_2=0.0463920064647544359\ldots.
\]
Consequently,
\[
p_1^2-p_0p_2
=
-0.0000794058995773977\ldots<0,
\]
or equivalently
\[
\frac{p_1^2}{p_0p_2}
=
0.9135598872191721690\ldots<1.
\]

This directly contradicts Theorem 1 of the 2025 DGM paper, which states that the DGM PMF is log-concave for all positive parameters.

## Assumptions and scope
The parameter domain is exactly
\[
\alpha>0,\qquad \theta>0,\qquad \mu>0,
\]
and the PMF is the survival-discretization PMF printed in the source.

The result disproves **universal PMF log-concavity**. It does not claim that the DGM PMF is globally log-convex, nor does it give a complete phase diagram for PMF curvature over all parameter triples. It also does not deny the source's separate increasing-failure-rate theorem.

The source associates PMF log-concavity with unimodality and convolution stability. The present finding shows that those consequences cannot be justified from the claimed universal log-concavity theorem. It does not by itself prove that every such consequence fails for every counterexample parameter triple.

## Proof
For one unit step, define
\[
d_z=-\log\frac{S_{z+1}}{S_z}.
\]
Under the scaling
\[
\alpha=\varepsilon a,\qquad \theta=\varepsilon b,
\]
one obtains exactly
\[
d_z
=
\varepsilon
\left[
a+\frac{b}{\mu}(e^\mu-1)e^{\mu z}
\right]
=
\varepsilon q_z,
\]
where
\[
q_z=a+c r^z,\qquad
r=e^\mu>1,\qquad
c=\frac{b}{\mu}(r-1)>0.
\]

For each fixed \(z\), one has
\[
S_z=1+O(\varepsilon)
\]
and
\[
1-e^{-d_z}
=
\varepsilon q_z+O(\varepsilon^2).
\]
Since
\[
p_z=S_z(1-e^{-d_z}),
\]
it follows that
\[
p_z=\varepsilon q_z+O(\varepsilon^2).
\]
Therefore
\[
p_z^2-p_{z-1}p_{z+1}
=
\varepsilon^2
\left(q_z^2-q_{z-1}q_{z+1}\right)
+O(\varepsilon^3).
\]
A direct calculation gives
\[
q_z^2-q_{z-1}q_{z+1}
=
-a c r^{z-1}(r-1)^2<0.
\]
Hence the log-concavity determinant is negative for all sufficiently small positive \(\varepsilon\), at every fixed \(z\).

For a finite set \(1\le z\le m\), take the minimum of the finitely many positive small-\(\varepsilon\) neighborhoods. This gives a common \(\varepsilon_m>0\) on which all \(m\) determinants are negative simultaneously.

For the explicit example, choose
\[
r=2,\qquad
\mu=\log2,\qquad
a=1,\qquad
b=\log2.
\]
Then \(c=1\), and with \(\varepsilon=0.01\),
\[
S_z=
\exp[-0.01(z+2^z-1)].
\]
The three displayed PMF values and the negative determinant follow by direct substitution.

The source's Appendix A does not compute this determinant. It computes the second finite difference of \(\log S_z\), correctly finding that the survival sequence is log-concave, and then concludes that its first difference \(p_z=S_z-S_{z+1}\) is log-concave. That transfer is not valid in general. Moreover, its displayed equation (A.2), presented as equivalent to PMF log-concavity, contains only survival terms and is not algebraically equivalent to
\[
(S_z-S_{z+1})^2
\ge
(S_{z-1}-S_z)(S_{z+1}-S_{z+2}).
\]

## Verification
The included checker uses only Python's decimal arithmetic. It reconstructs the exact special-ray survival
\[
S_z=\exp[-\varepsilon(z+2^z-1)]
\]
and independently evaluates \(p_0,p_1,p_2\), the log-concavity determinant, and the ratio
\[
p_1^2/(p_0p_2).
\]
It also verifies numerically, at successively smaller \(\varepsilon\), that
\[
\frac{p_1^2-p_0p_2}{\varepsilon^2}\to-1,
\]
which is the specialization of the analytic coefficient
\[
-a c r^{z-1}(r-1)^2
\]
at \(a=c=1\), \(r=2\), and \(z=1\).

These finite calculations are consistency checks only. The open low-rate counterexample region follows from the analytic expansion.

## Relationship to prior work
The 2025 DGM article defines the survival-discretization PMF and states in Theorem 1 that it is log-concave for every positive parameter triple. Appendix A bases the proof on curvature of the survival sequence.

Bagnoli and Bergstrom study log-concavity and log-convexity relationships among continuous densities, distribution functions, reliability functions, and their integrals. In the inspected reliability-function results, log-concavity of a continuous density can pass to its reliability function, and log-convexity of a density can pass to a reliability function under an endpoint condition. Those statements do not assert that a log-concave survival sequence must have log-concave first differences.

Focused searches using the exact DGM name and DOI, PMF log-concavity, survival discretization, small-rate aliases, and correction terminology did not locate a corrigendum or a published statement of the low-rate obstruction above.

## Limitations
The finding is a counterexample theorem and a local low-rate asymptotic, not a complete characterization of the DGM parameter region in which the full PMF is log-concave.

The scale \(\varepsilon_m\) is proved to exist for each finite prefix but is not optimized in closed form. The explicit parameter triple certifies failure already at \(z=1\).

No claim is made here about the separate maximum-likelihood, Bayesian, moment, or data-fitting results in the source.

## References
1. A. Elshahhat, H. Rezk, and R. Alotaibi, “The discrete Gompertz–Makeham distribution for multidisciplinary data analysis,” AIMS Mathematics 10 (2025), 17117–17178. DOI: 10.3934/math.2025768.
2. M. Bagnoli and T. Bergstrom, “Log-concave probability and its applications,” Economic Theory 26 (2005), 445–469. DOI: 10.1007/s00199-004-0514-4.
