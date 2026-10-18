# Scientific review: a curvature sign law for one-probe functional Nyström sketches

## Correctness
PASS. The theorem is reconstructed from rank-one Nyström eigenvalue formulas. Scalar concavity/convexity produces the relevant monotonicity of \(f(t)/t\); a two-distribution covariance comparison and Jensen's inequality establish the sign for arbitrary spectra and probes. The zero-denominator case, exact trace underestimation, and strict-curvature conditions are covered. The rare-angle Gaussian change of variables and beta integral establish the stated divergent-gap asymptotics. The standalone `verify.py` produced 11,722 passing checks; those checks supplement rather than replace the analytic proof.

## Originality
PASS under the accessible comparison, with risk of an undiscovered equivalent spectral-mean inequality. The main source (Persson–Kressner, arXiv:2209.11023) supplies the two Nyström constructions and general approximation bounds but does not state or imply by one of its published conclusions a same-probe universal curvature-sign trace dominance for one-column sketches. Gittens–Mahoney, arXiv:1303.1849, supplies classical Nyström spectral and trace-norm bounds without comparing two functional orders. A previously recorded one-column Gaussian Nyström residual distribution contains the isolated ordinary \(f(t)=t\) case, not the all-function convex/concave reversal. Targeted mathematical-record searches returned no equivalent claim; this does not establish uniqueness.

## Value
PASS. Function-after-sketch and sketch-after-function are explicitly compared as two alternatives in the motivating work. The deterministic one-column law determines which always retains greater functional trace using only the curvature of \(f\), and it applies to every input and power-iteration count. The sharp nearly rank-one examples show that the difference in expected trace deficits can diverge as a power of spectral separation in either direction. This is a structural algorithm-ordering statement, not an arbitrary computation of a single matrix. It does not imply a universal higher-rank or Löwner-order comparison.

## Limits and closest comparison
This is a one-column, identical-probe exact-arithmetic theorem; its algebraic proof does not use Gaussianity, except in the sharp asymptotic illustrations. Comparable trace underestimation for both methods does not imply matrix Löwner dominance or comparisons in other norms. Generic Jensen and covariance inequalities are standard proof ingredients, not independently new claims. Literature outside the inspected sources may already contain an equivalent scalar ratio inequality.

Self-review: passed. Independent audit: not yet performed.
