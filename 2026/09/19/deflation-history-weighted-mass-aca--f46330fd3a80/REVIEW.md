# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The construction is elementary and can be checked exactly. The matrix is a sum of two positive-semidefinite matrices. The first weighted-mass pivot is forced by the inequalities
\[
m_q\ge256N^2,\qquad m_b\le80N^2,\qquad m_g\le N.
\]
The first Schur-complement update removes \(v_Nv_N^\top\) exactly because the \(q\)-column of \(R_N\) is zero. At the resulting residual, the stale original diagonal entry gives
\[
m_b\ge(1+\sqrt N)^2>N\ge m_g,
\]
so the bad second pivot is forced. The two possible second updates leave \(J_N\) and \([1]\), respectively, giving the exact Frobenius residuals \(N\) and \(1\).

The rank-two SVD comparison follows from the direct-sum decomposition into \(J_N\) and a \(2\times2\) positive-definite block. The smaller block eigenvalue is the displayed \(\lambda_-(N)\), which tends to \(4/5\). The one-step Frobenius-gain formula is a direct expansion of the rank-one residual update.

The standalone verification artifact constructs the matrices numerically, confirms that the first update equals the stated residual to roundoff, reproduces the first two pivots, and checks the \(N:1\) residual ratio, the \(1:N^2\) one-step-gain ratio, and the rank-two SVD comparison for several values of \(N\).

## Originality — PASS, to the best of our knowledge

The motivating preprint introduces the weighted-mass score
\[
\sum_{j\in\mathcal N_i}(B_{jj}A_{ji})^2
\]
and explicitly describes it as a proxy using current residual mass together with original-matrix correlations. It also states that its experiments do not provide a general convergence guarantee. The inspected paper does not identify the resulting deflation-history dependence, give an adversarial family for this dependence, or quantify an unbounded fixed-rank approximation factor.

Classical and recent pivoted-Cholesky/CUR literature already analyzes residual-diagonal pivoting, randomized residual-dependent pivoting, maximum-volume criteria, and quasi-optimal cross approximations. Those results, together with the elementary rank-one Frobenius expansion, are excluded from the novelty claim. In particular, Chen–Epperly–Tropp–Webber select from the current residual diagonal, Steinerberger studies squared residual-diagonal sampling for Frobenius contraction, and Massei studies maximum-volume/cross criteria for SPSD matrices. None of the accessible statements inspected gives the source-specific obstruction caused by multiplying a current residual weight by an entry from an already-deflated original component.

No matching SCOPE record was found under the source identifier, weighted-mass/ACA terminology, pivoted-Cholesky terminology, or the deflation-history/stale-correlation claim family. Searches for the source title and identifier together with correction, counterexample, residual-correlation, and convergence terms found the motivating preprint and mirrors but no public correction or equivalent theorem.

### Residual literature risk

The main residual risk is broad older pivoted-Cholesky and ACA literature that could contain an equivalent abstract principle about history-dependent pivot scores. Harbrecht–Peters–Schneider (2012), DOI 10.1016/j.apnum.2011.10.001, was available through bibliographic metadata and an abstract describing trace-norm control, but its full text was not inspected here. This could affect the originality of a very general formulation, but it cannot contain an analysis of the 2026 weighted-mass rule by name. The novelty claim is therefore restricted to the explicit mixed-score invariance obstruction and the stated unbounded family.

The motivating preprint is recent, so contemporaneous or not-yet-indexed follow-up work cannot be excluded.

## Value — PASS

The result isolates a concrete failure mechanism in a newly proposed pivot rule: a component that has already been removed exactly can continue to dominate future scores because the correlation factor is read from the original matrix. The effect is not merely qualitative. At rank two the Frobenius error ratio is unbounded, and the exact one-step Frobenius gain of the selected second pivot is only \(1/N^2\) of an available gain.

The family also rules out an explanation based on an overwhelmingly large deflated component, since the removed rank-one term has operator norm only \(5\sqrt N\) while the surviving residual has operator norm \(N\). The mechanism therefore persists when the stale component is asymptotically negligible in norm.

A residual-consistent replacement of \(A_{ji}\) by \(R_{ji}\) removes the history dependence and fixes the full-neighborhood version of this example, while the exact one-step Frobenius gain identifies the principled but more expensive target. These observations give a concrete direction for robust variants without asserting a new convergence theorem.

## Limitations checked

The construction is a synthetic PSD family and is not shown to occur in the radial-basis Galerkin class used in the motivating experiments. It is singular, although the pivot blocks used in the construction are nonsingular. The result concerns error at a fixed target rank rather than eventual convergence; the rank-three example is solved after one further useful pivot. The theorem uses the self-containing neighborhood convention indicated by the source paper's \(\ell=1\) description. The proposed residual-consistent score is only a structural repair for stale-history dependence, not a proven universally superior pivot rule.
