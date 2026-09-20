# Review

## Status

Same-model review: passed. Independent audit: not yet performed.

Independent validation is not asserted.

## Correctness — PASS

The primary source was checked at the exact points on which the result depends. Wu--Hong Theorem 4.20 states that, for rank two with nonzero off-diagonal entries and nonzero module parameter, irreducibility is equivalent to nonexistence of a rational solution of the displayed Riccati equation. Remark 4.21 then substitutes
\(\gamma=-z'/(c_{21}z)\) but displays a second-order equation without the logarithmic derivative of \(c_{21}\).

Direct differentiation gives

\[
\gamma'=-\frac{z''}{pz}+\frac{(z')^2}{pz^2}+\frac{p'z'}{p^2z},
\]

so cancellation of the quadratic term leaves
\(z''+(d-p'/p)z'-pqz=0\). The correction is independently stress-tested by the explicit matrix
\(C=\bigl(\begin{smallmatrix}0&x\\x&0\end{smallmatrix}\bigr)\): the Riccati equation has the rational solution \(\gamma=1\), and \(z=e^{-x^2/2}\) satisfies the corrected linear equation but leaves residual \(-z\) in the uncorrected one.

The normal-form formula was re-derived from \(z=\rho w\): the coefficient of \(w'\) is \(2\rho'+P\rho\), where \(P=d-p'/p\), yielding
\(r=-pq-P'/2-P^2/4\).

The degree-parity theorem was checked adversarially at infinity. For a rational \(\gamma\sim\kappa x^m\), the derivative is strictly below at least one of \(p\gamma^2\) or \(q\), so it cannot participate in the top-degree cancellation. Under \(2D<B+Q\), either cancellation involving \(d\gamma\) would force \(2D\ge B+Q\). Hence the leading cancellation must be between \(p\gamma^2\) and \(q\), forcing \(B+2m=Q\) and equal parity. This proves the stated contrapositive without an empirical completeness assumption.

The result explicitly preserves the validity of Wu--Hong Theorem 4.20. Example 4.22 is also unaffected by the missing logarithmic derivative because its \(c_{21}\) is constant.

## Originality — PASS, to the best of our knowledge

The classical Riccati-to-linear substitution, differential-Galois algorithms, and degree/valuation methods are prior art and are not claimed as original. The claimed contribution is narrower: identifying and correcting the formula in Remark 4.21 of arXiv:2609.18184v1, giving a concrete counterexample to the displayed reduction when \(c_{21}\) is nonconstant, and extracting the stated degree-parity irreducibility criterion for the newly introduced generalized Virasoro modules.

The arXiv submission history showed only v1 at the time of review. Searches using the arXiv identifier, paper title, `Riccati`, `Kovacic`, `c21`, `correction`, and related combinations found the source paper but no public erratum, revision, or note making this correction. Searches for the degree-parity obstruction in rational Riccati equations found general Riccati and rational-solution literature, but no source applying this precise obstruction to these generalized conformal modules.

Repository overlap searches used the source identifier and terms including `Virasoro`, `conformal`, `Riccati`, and `degree parity`; no existing SCOPE record covering the claim was found before publication.

### Residual originality risk

Because the source paper is very recent, a contemporaneous correction by the authors or another reader could appear with little indexing delay. General Riccati theory is extensive, so the valuation lemma may exist in a more general form under different terminology. The record therefore does not claim novelty for the underlying ODE technique, only for the source-specific correction and its representation-theoretic corollary to the best of our knowledge.

## Value — PASS

The correction affects the computational route recommended in the source whenever \(c_{21}\) is nonconstant. The explicit example shows that the omitted term changes the equation produced by the stated substitution, so using the displayed equation can analyze a different differential problem.

The degree-parity theorem adds a reusable closed-form sufficient condition for irreducibility. In the equal-diagonal case it upgrades the single degree-comparison example in Wu--Hong to every pair of nonzero off-diagonal polynomials of opposite degree parity. It can therefore bypass a full rational-Riccati or Kovacic computation for a large family of the paper's new modules.

## Limitations

The result does not challenge the source paper's main rank-two irreducibility theorem; it corrects the auxiliary linearization in Remark 4.21. The parity criterion is sufficient, not necessary, and says nothing definitive in the same-parity or diagonal-dominant regimes.
