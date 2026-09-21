# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was re-derived from the exact second-derivative identity in Simić--Bin-Mohsin (2021). Writing
\[
w_p(t)=t(2p-t),\qquad g(t)=\frac{f''(x_t)+f''(y_t)}2
\]
gives
\[
T_p[f]=\frac{(b-a)^2}{8}\int_0^1w_p(t)g(t)\,dt,
\]
with \(m\le g\le M\) and \(\int_0^1w_p=p-1/3\). Translating \(f''\) by a constant proves that the coefficient multiplying \(m+M\) is forced to be \((3p-1)/48\). Centering at \((m+M)/2\) then reduces the optimal remainder to the weighted \(L^1\) norm of \(w_p\), namely
\[
\frac1{16}\int_0^1|w_p(t)|\,dt.
\]
Direct integration gives the three pieces in the result.

Sharpness within \(C^2\) was checked at the level of the exact admissible class. Any continuous function \(G:[0,1]\to[m,M]\) is realized by the symmetric prescription \(f''(s)=G(2\min\{s,1-s\})\) after normalization. Continuous profiles can approximate the sign of \(w_p\) in \(L^1(|w_p|dt)\) while attaining both curvature extrema. Hence the constants are genuine suprema/infima rather than artifacts of a relaxed measurable class.

The minimax calculation is elementary: on \([0,1/2]\), the sharp constant is \((1-3p+8p^3)/48\), whose unique critical point is \(p=1/(2\sqrt2)\); the outer pieces are linear and larger. The uncentered characterization follows from the same quadratic-translation test, forcing \(3p-1=0\).

The standalone verification artifact checks the coefficient identities on exact rational samples, the Simpson value \(1/162\), and the minimax parameter and constant; it also performs a dense numerical check of the global minimum. These computations corroborate but do not replace the analytic proof.

## Originality

PASS, to the best of our knowledge, with a deliberately narrow originality claim.

The 2021 Simić--Bin-Mohsin source was checked at Lemma 2.7, Theorem 2.8, Remark 2.9, and Corollary 2.10. It proves the same three valid lower/upper bounds but does not state their all-parameter optimality, the forced curvature-midpoint centering, the exact centered oscillation constant, or the minimax parameter \(1/(2\sqrt2)\). It conjectures only that the Simpson constant \(1/162\) is best possible.

That Simpson-specific sharpness is not new. Cruz-Uribe--Neugebauer (2002), Theorem 1.19, gives a sharp \(W^{2,p}\) Simpson estimate. Its \(p=\infty\), one-panel case yields the sharp second-derivative distance bound, from which the \((M-m)/162\) estimate follows by choosing the midpoint constant. The present record therefore excludes the Simpson-only sharpness from its originality claim.

The 2020 Simić--Bin-Mohsin paper studies the same endpoint-midpoint family under convexity/concavity hypotheses on the second derivative and establishes different best-possible parameter assertions. A 2025 paper citing the 2021 source concerns fractional Hermite--Hadamard refinements and does not supply the parameterized curvature-range envelope here.

Searches used the exact source title and DOI; the cubic \(1-3p+8p^3\); the parameter \(1/(2\sqrt2)\); centered curvature-oscillation language; sharp three-point quadrature terminology; and equivalent Simpson/Hermite--Hadamard formulations. No located source stated the combined all-\(p\) sharp envelope, unique centering, and minimax parameter.

The principal residual risk is older general quadrature literature in different notation. Cerone (2001), *Three point rules in numerical integration*, has an abstract describing broad three-point Ostrowski-type bounds, but theorem-level full text was not available in the sources inspected. Ujević's 2004 papers *Sharp inequalities of Simpson type and Ostrowski type* and *Two Sharp Inequalities of Simpson Type and Applications* were also available only through abstracts in the inspected sources; their titles and abstracts are Simpson-specific, but theorem-by-theorem exclusion of an equivalent parameterized statement was not possible. These are concrete literature risks, not evidence of known coverage.

## Value

PASS.

The result converts a previously valid but apparently non-sharp-looking three-regime theorem into an exact optimization theorem over the entire real parameter line. The quadratic-translation argument identifies the only centering compatible with a curvature-oscillation seminorm; the exact kernel norm then gives a closed-form optimal constant. The unexpected minimax weight \(1/(2\sqrt2)\) separates two notions that coincide only superficially: Simpson's weight is uniquely correction-free, whereas the best curvature-centered rule has a slightly different endpoint weight. This provides a reusable way to distinguish polynomial exactness from minimax oscillation control in related quadrature families.

## Limitations

- The result is restricted to the symmetric endpoint-midpoint one-parameter family and information only through \(\min f''\) and \(\max f''\).
- Sharpness for nonconstant curvature is generally nonattained in \(C^2\); it is an exact supremum/infimum obtained by continuous approximation of bang-bang curvature profiles.
- The minimax conclusion applies after the necessary curvature-centering correction. Without a correction, only Simpson's parameter admits a finite oscillation-only bound.
- The Simpson-specific \(1/162\) sharpness is prior-covered and not claimed as original.
- Older general three-point quadrature literature may contain an equivalent all-parameter theorem under different notation; the specific inaccessible sources above are the main residual originality risk.
- Independent audit has not been performed.
