# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** Pulling the folded density ratio back to `R^n` gives the sign average of the ordinary Gaussian likelihood ratio. Positivity gives a lower comparison with one sign component and convexity gives an upper comparison with the full Gaussian Rényi integral. The latter is finite exactly when `gamma R^{-1}-(gamma-1)I` is positive definite, yielding the claimed condition on `lambda_max(R)`. The same inequalities bound the folded divergence within `(n-1) log 2` of the unfurled Gaussian divergence, so the critical logarithmic blow-up coefficient follows from the top-eigenspace multiplicity.

For integer orders, expansion of the finite sign average followed by one Gaussian integral gives the determinant formula. In the stated finite regime, `R^{-1}>((m-1)/m)I`, which makes every determinant matrix positive definite; outside it the all-equal-sign term diverges.

At order two, the sign average is the orthogonal projection of the Gaussian likelihood ratio onto the coordinatewise-even subspace of Gaussian `L^2`. Parseval in the probabilists' Hermite basis gives the nonnegative series. The pair contribution uses `E[H_2(X_i)H_2(X_j)]=2 rho_ij^2`; the three-coordinate contribution uses `E[H_2(X_i)H_2(X_j)H_2(X_k)]=8 rho_ij rho_ik rho_jk`. These yield the fourth- and sixth-order terms. In two dimensions the standard bivariate Hermite identity sums the series to `1/(1-rho^4)`, hence `D_2=-log(1-rho^4)`.

The numerical artifact independently evaluates the determinant sum, verifies the bivariate formula to floating-point precision, checks integer-order finiteness transitions, and recovers the analytic fourth- and sixth-order coefficients. It supports but is not needed for the proof.

## Originality

**PASS, to the best of our knowledge.** Ouimet--Greaves (2026) explicitly introduce order-two Rényi total correlation for Gaussian magnitudes and give a product-moment lower bound, noting that their certificate avoids direct evaluation of the joint density ratio. Their paper does not state an exact density-ratio formula or characterize when the order-two divergence is finite.

The folded-normal literature was searched under multivariate folded normal, Gaussian magnitudes, absolute Gaussian, chi-square divergence, Rényi divergence, Rényi mutual information, and total correlation. Benko--Hübnerová--Witkovský (2025) was inspected in full text; it develops characteristic and moment-generating functions and contains no Rényi-, Kullback--Leibler-, or entropy-divergence calculation. Liu et al. (2023) and Chakraborty--Chatterjee (2013) are directly relevant distributional prior work. Accessible descriptions of them concern marginals, conditional distributions, independence, estimation, and general folded-normal properties rather than information divergences. Tsagris--Beneki--Hassani (2014) treats univariate folded-normal entropy and Kullback--Leibler quantities and is not an exact multivariate dependence result.

No prior statement was found of the exact Rényi integrability spectrum of centered Gaussian magnitudes, the integer sign-determinant formula, the bivariate identity `-log(1-rho^4)`, the even-Hermite Parseval representation, or the associated pair/triangle weak-dependence expansion. Standard Rényi formulas for unfurled Gaussian laws and standard Hermite/Wick machinery are not claimed as new.

The full texts of Liu et al. (2023) and Chakraborty--Chatterjee (2013) were not fully inspected. Because both concern the same multivariate folded-normal family, they remain the principal residual originality risk. The originality claim is therefore explicitly limited to the folded-Gaussian Rényi dependence formulas stated in the record.

## Value

**PASS.** The result turns a recent moment-based lower certificate into an exact dependence calculation at order two and, more generally, an exact integrability phase diagram at every Rényi order greater than one. The sharp threshold shows that deleting all coordinate signs does not regularize high-order likelihood ratios. The determinant formula makes every integer order computable by a finite sign sum, while the Hermite representation identifies pairwise correlations at quartic order and triangle interactions at sixth order. The closed bivariate formula supplies a simple benchmark for future Gaussian-magnitude dependence bounds.

## Limitations

The Gaussian correlation matrix is assumed positive definite. Noninteger Rényi orders have a sharp finiteness criterion and critical asymptotic but no finite determinant-sum formula here. The Hermite decomposition and local graph expansion are developed only for order two. No statistical estimation procedure or convergence rate from data is claimed. Cross-model review has not been performed.
