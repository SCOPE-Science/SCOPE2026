# Review of a quartic-edge impurity crossover in a zigzag quantum chain

## Correctness — PASS
The theorem fixes a real scaled detuning \(s\) and takes \(\varepsilon\downarrow0\) with hopping ratio \(a_\varepsilon=1/4+s\varepsilon^{2/3}\). The exact Bloch polynomial in \(u=1+\cos k\) identifies the upper band edge on each side of the merger. Positive rank-one resolvent monotonicity gives one simple exterior eigenvalue. Quartic-edge rescaling reduces its equation to the convergent integral
\[
\frac{1}{\pi}\int_0^\infty\frac{dx}{y-4sx^2+x^4/4}=\frac{1}{2\sqrt y\sqrt{\sqrt y-4s}},
\]
whose unique unit-level root is precisely the positive root of \(t^2(t-4s)=1/4\). Uniform-on-compact convergence away from the limiting edge and root bracketing justify the limiting eigenvalue. Four finite-matrix checks and 15 exact-resolvent numerical tests supported, but do not substitute for, the analytic argument.

## Originality — PASS, qualified historical priority
Stockhofe and Schmelcher (arXiv:1506.01937, original release 2015-06-05) treat this hopping dispersion, its merger point and single-defect bound states. The contribution assessed here is narrower and different: a simultaneous \(\varepsilon^{2/3}\) hopping-detuning and \(\varepsilon^{4/3}\) bound-energy limit with the full explicit cubic crossover. Their accessible complete text was compared at the statement level and no such scaling theorem was found. Koiller and Brandi (DOI:10.1007/BF00554383, 1981) develop earlier long-range impurity transfer matrices; only their abstract was accessible. An implicit or equivalent specialization there remains a material priority uncertainty. The generic quartic continuum integral is not claimed separately.

## Mathematical value — PASS
This classifies a natural singular spectral transition at which the standard nondegenerate quadratic band-edge law changes, while the impurity vanishes. The complete crossover is a motivated structural result, not an arbitrary lattice parameter slice: it specifies both exponents, the exact critical coefficient \(2^{-4/3}\), and asymptotic matching behavior on opposite sides of the band-topology transition.

## Scope and residual risks
The result is pointwise in fixed \(s\). No bound is proved uniformly as \(|s|\to\infty\) while defect strength vanishes. Numerical checks are finite evidence only. Specialized older impurity papers may contain an equivalent asymptotic not identified in accessible material. An independent external review has not been performed.

Self-review: passed. Independent audit: not yet performed.
