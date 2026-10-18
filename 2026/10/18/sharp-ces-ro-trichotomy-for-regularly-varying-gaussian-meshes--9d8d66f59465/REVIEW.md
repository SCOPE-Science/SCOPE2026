# Scientific review: regularly varying Gaussian Cesàro meshes

## Correctness — PASS
The exact Bauschke–Tung Gaussian feature Gram identity identifies the squared Cesàro norm as an explicit nonnegative double sum. In the high-density regime, local slow variation yields Gaussian row mass \(\sqrt\pi/d_i\). A separate comparison for indices beyond twice the base index proves that remote Gaussian tails vanish even when the mesh decreases slowly. Karamata summation contributes exactly the factor \(1/(1+\alpha)\), and weighted Cesàro convergence safely replaces \(\rho_i\rho_j\) by \(\rho_\infty^2\). In the finite-density regime, proportional mesh windows converge to logarithmic distances and the bounded Gram kernel gives a rigorous two-dimensional Riemann limit. The explicit power-law mesh satisfies the recurrence inequality for every index, with \(0<c\le1/16\). No finite experiment is used as an infinite proof.

## Originality — PASS, subject to residual literature risk
The original Bauschke–Tung paper (arXiv:2605.25491, especially Theorem 7.6 and Example 7.7) proves qualitative convergence when \(n d_n\to\infty\), and a squared-norm upper bound of order \((n d_n)^{-1}\), but not its sharp constant. The published *Exact Cesàro norm limit for the harmonic firmly nonexpansive counterexample* gives exactly the pure-harmonic special case, which this result explicitly excludes from its novelty claim. The new statement gives an all-regularly-varying sharp high-density coefficient \(\sqrt\pi/(1+\alpha)\) and a full finite-density classification for meshes beyond that single harmonic sequence. Directly inspected published results do not imply this general theorem. Broad prior kernel-summation literature might contain an equivalent localization lemma; this remains an identified priority risk.

## Value — PASS
The motivating paper constructs firmly nonexpansive nonlinear orbits whose Cesàro means may or may not converge strongly but leaves sharp rates and constants undetermined. The theorem supplies a phase transition controlled by the natural local density \(n d_n\), a genuinely sharp polynomial rate and leading constant for the source's power-law example, and a boundary law for logarithmically slow meshes. This quantifies a concrete nonlinear mean-ergodic phenomenon and is not a change of notation or a generic boundedness consequence.

## Closest literature and limitations
Bauschke–Tung, *Cesàro means of firmly nonexpansive iterates need not converge strongly* (2026), arXiv:2605.25491; *Exact Cesàro norm limit for the harmonic firmly nonexpansive counterexample* (public research record, 2026-10-04). Only admissible regularly varying increments and the specified Gaussian orbit are covered. An equivalently stated general kernel asymptotic could exist outside the inspected literature. Independent validation has not been conducted.

Self-review: passed. Independent audit: not yet performed.
