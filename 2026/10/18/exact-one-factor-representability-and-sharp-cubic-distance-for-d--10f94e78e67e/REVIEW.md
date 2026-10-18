# Scientific review: exact one-factor Lyapunov Gramian classification

## Correctness — PASS
The covariance equation is explicitly integrated, with sign-normalized entries equal to a strict Laplace Gram kernel. Strict order-two kernel minors eliminate every three-distinct-rate choice; strict Cauchy--Schwarz and an off-diagonal tetrad eliminate the remaining two-rate patterns with both groups of size at least two. The rank-one-plus-nonnegative-diagonal construction handles precisely the permitted all-equal and singleton-exception rate patterns. Exact four-entry perturbation inequalities certify a positive Frobenius gap; a positive fourth-order determinant coefficient divided by entry size of order \(t\), paired with a third-order midpoint rank-one upper approximation, proves the matched \(\Theta(t^3)\) distance. The three-rate stationary Gramian has exact negative forced uniqueness \(-1/60\) and lower bound \((\sqrt{991}-31)/120\). The accompanying verifier replayed 4002 checks, with universal arguments analytical rather than numerical.

## Originality — PASS, with residual literature risk
The 2024 Bonnabel--Lambert--Bach article defines low-rank-plus-diagonal Riccati approximation and derives tangent projection formulas. The 2017 Bertsimas--Copenhaver--Mazumder and 2012 Saunderson et al. papers establish general factor-analysis/decomposition theory, tetrad-type constraints, and algorithmic formulations. These are acknowledged as prior art, not newly claimed. The assessed narrow contribution is the exhaustive diagonal Lyapunov damping-rate classification and the matched cubic distance law for rank-one forcing at all finite positive times and stationarity. The relevant portions of all three open-access primary articles were inspected and did not disclose the combined special theorem. Older Shapiro (1982) full text was not accessible; specialized antecedents may remain unindexed or undetected. Publication priority has not been independently verified.

## Value — PASS
The theorem explains precisely when a simple positive covariance trajectory with rank-one process forcing is structurally incompatible with nonnegative diagonal plus rank-one storage. Its strictly positive separation applies even to positive-definite Gramians and has a matched third-order local scaling. This gives a rigorous nontrivial approximation benchmark for factor-model covariance propagation, independent of implementation choices.

## Limitations
The classification requires real diagonal stable drift, zero initial covariance, rank-one forcing and nonzero forcing loadings, with \(n\ge3\). The lower bound is not the exact optimal Frobenius distance. The asymptotic error is a fixed-parameter short-time result. The theorem does not establish failure of numerical Riccati solvers, general non-diagonal dynamics, or any rank higher than one. Primary literature may contain an unknown equivalent specialization.

Self-review: passed. Independent audit: not yet performed.
