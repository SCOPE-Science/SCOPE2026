# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The three-dimensional witness is exact. The displayed matrix `U3` is orthogonal, and direct conjugation of `diag(10,2,1)` gives the stated positive-definite matrix `B3`. Correlation normalization yields
\[
\|C\|_F^2=1800677/320013,
\]
while the conjectured bound is \(945/169\); their exact difference is \(1902128/54082197>0\). The block-diagonal extension is exact and its gap factors as a positive rational function for every integer \(r=n-3\ge0\).

The two-dimensional positive result was checked independently from the counterexample construction. After weighted normalization of an orthonormal basis, its two-vector frame operator has eigenvalues \(1\pm|r|\), with \(|r|\le |a-b|/(a+b)\). Von Neumann's trace inequality for the two positive semidefinite frame operators then gives the claimed universal cross-frame bound. A common 45-degree frame attains it.

The symbolic artifact recomputes the exact counterexample and extension from their definitions. It supports but does not replace the analytic proof in `RESULT.md`.

## Originality

**PASS, to the best of our knowledge.** Loe--Huang--Needell (arXiv:2609.17947, submitted 16 September 2026) explicitly leave the weighted-cosine Frobenius upper bound as a conjecture in Appendix A after proving the equal-diagonal Hadamard value and a stationarity statement for the common-frame objective. The present result gives an exact counterexample, shows failure for every dimension at least three, proves the conjecture in dimensions at most two, and supplies a dimension-four witness that beats an actually available Hadamard frame.

Searches covered the source title and arXiv identifier; the phrases `weighted cosine`, `singular-vector coherence`, `Hadamard frame`, `correlation matrix prescribed spectrum`, `fixed eigenvalues Frobenius norm`, `orthogonal orbit correlation matrix`, and equivalent formulations in terms of correlation-normalizing `U Sigma U^T`. No located source states this dimensional threshold or the explicit counterexample family.

Relevant older literature was checked for possible equivalent coverage. Grone--Pierce studies permanental inequalities for correlation matrices; Higham studies nearest-correlation-matrix approximation; Chen studies quotient geometry of fixed-rank correlation matrices; and Chehab--Oviedo--Raydan study structured inverse eigenvalue problems on fixed-spectrum manifolds. Their located statements address different objectives and do not imply the claimed weighted-cosine extremum.

The full theorem statements of some broad fixed-spectrum/correlation-matrix background papers were not all inspected. Among the located sources, Chehab--Oviedo--Raydan is the most plausible broad fixed-spectrum source that could contain an unnoticed related optimization observation; its accessible abstract describes prescribed-entry inverse eigenvalue reconstruction rather than diagonal correlation normalization, so the residual originality risk appears low. The source ACA preprint itself is very recent, so simultaneous follow-up work remains a material residual risk.

## Value

**PASS.** The result resolves a concrete conjecture posed in a new numerical-analysis paper and identifies the exact first dimension in which it fails. The dimension-four witness directly distinguishes stationarity/equal-diagonal symmetry from global optimality even when a real Hadamard frame exists. The all-dimension embedding shows the obstruction is structural rather than a one-off numerical example, while the two-dimensional theorem explains why low-dimensional experiments can support the conjecture.

## Limitations

The result concerns real orthogonal frames and strictly positive diagonal weights under the weighted-cosine Frobenius objective defined in Appendix A of arXiv:2609.17947. It does not characterize the true global maximum for \(n\ge3\), does not address complex unitary frames, and does not provide a replacement upper bound sharp in general dimension. It does not invalidate the source paper's exterior-algebraic residual identities, CUR/ACA bounds, or weighted-mass pivoting experiments.
