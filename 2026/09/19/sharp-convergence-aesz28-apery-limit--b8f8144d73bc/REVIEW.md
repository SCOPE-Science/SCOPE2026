# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The result reduces to three independently checkable components.

First, the Casoratian follows exactly from the second-order recurrence:
\[
W_n=\frac{4n^2(16n^2-1)}{(n+1)^4}W_{n-1},\qquad W_0=1.
\]
The stated binomial closed form is the elementary product evaluation of this recurrence. It implies the exact quotient increment \(W_n/(A_nA_{n+1})\).

Second, the dominant solution \(A_n\) has a positive double-binomial formula. Its entropy function has a unique strict interior maximum at \((3/4,3/4)\). The Hessian and Stirling prefactor give the leading constant \(2\sqrt6/(3\pi^2)\). Standard lattice Laplace expansion supplies a full inverse-power expansion; substitution into the recurrence fixes the first correction at \(-29/48\).

Third, Stirling expansion of the exact Casoratian, division by the two adjacent \(A\)-asymptotics, and summation of the resulting geometric tail give the quotient-error constant and correction. Multiplication by \(7A_n\) gives the linear-form asymptotic. Exact rational computation independently checks the Casoratian identity through \(n=79\), while high-precision numerical ratios approach \(1\) at the predicted second-order rate.

Stress tests included checking the recurrence at the first nontrivial indices, the sign and indexing of the Casoratian, the factor \(7\) in passing from the quotient error to \(\zeta(3)\), the shift from \(A_n\) to \(A_{n+1}\), and the \(1/n\) correction in the geometric tail. No contradiction was found.

## Originality — PASS, to the best of our knowledge

Bachmann's arXiv:2609.18271v1 was inspected in full for the recurrence, the initial data, the proof of \(C_n/A_n\to\zeta(3)/7\), and related discussion. The paper establishes the limiting value and positivity/monotonicity but does not state the sharp quotient-error asymptotic, the constants \(\sqrt2\pi^3/84\) or \(\sqrt3\pi/9\), or the displayed exact positive series.

Panzer's 2025 slides were inspected for the same AESZ-28 recurrence and the positive double-binomial formula for \(A_n\). The Calabi--Yau database was checked for the operator, holomorphic-solution coefficients, discriminant, and local singularity data. General Apéry-limit literature, including Chamberland--Straub, was searched for equivalent recurrence asymptotics and exact error constants. Searches by the recurrence coefficients, AESZ-28, Martin sequence, the sequence \(1,6,126,3948,149310,\ldots\), the exact constants, and linear-form formulations did not locate prior coverage.

The main residual originality risk is Sato--Tasaka, *Multivariate Apéry-like numbers, interpolations, and modular L-values*, cited by Bachmann as a manuscript in preparation. Bachmann cites it for the limiting value, but the full manuscript was not available for inspection. Because it is a closely related inaccessible source, it remains the most plausible source that could contain overlapping convergence-rate information. Very recent unindexed follow-up work is an additional residual risk.

No novelty is claimed for multivariate Laplace's method, Stirling's formula, or general Casoratian/telescoping principles. The originality claim concerns their explicit synthesis for this newly proved AESZ-28 Apéry limit, including the leading constants and first corrections.

## Value — PASS

The source theorem identifies a new Apéry limit but leaves its quantitative convergence implicit. The present result supplies a sharp \(64^{-n}\) error law, an exact positive series whose partial sums are precisely \(7C_n/A_n\), and a polynomial-size asymptotic for the associated \(\zeta(3)\) linear form. These statements make the approximation mechanism quantitatively explicit and connect the recurrence's singular scale \(64\) with the rational approximants.

The result does not claim a new irrationality measure or improved arithmetic denominator control, and those limitations materially bound its number-theoretic consequences.
