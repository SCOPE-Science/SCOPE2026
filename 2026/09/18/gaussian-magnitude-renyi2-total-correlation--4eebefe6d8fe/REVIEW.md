# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The folded-density reduction was checked from first principles. For a
positive-definite correlation matrix \(R\), the magnitude density is the sum
of the \(2^n\) sign-reflected Gaussian densities, while the product of the
half-normal marginals is \(2^n\varphi_I\) on the positive orthant. Expanding
the order-2 density overlap and using sign invariance of \(N(0,I)\) reduces
the double sign sum to the single relative-sign sum in `RESULT.md`.

For a relative sign matrix \(D\), the corresponding Gaussian integral has
quadratic form
\[
B_D=R^{-1}+DR^{-1}D-I.
\]
Its value is
\[
(\det R)^{-1}\det(B_D)^{-1/2}
\]
when \(B_D\succ0\), and diverges otherwise. The identity-sign term gives
\(B_I=2R^{-1}-I\), so finiteness forces \(\lambda_{\max}(R)<2\).
Conversely, that spectral condition implies
\(R^{-1}\succ I/2\) and \(DR^{-1}D\succ I/2\) for every sign matrix, proving
that every term is finite. This establishes both the formula and the iff
threshold.

The bivariate specialization was recomputed algebraically. There are two
relative-sign classes: the equal-sign class has determinant one, and the
opposite-sign class contributes \((1-\rho^2)/(1+\rho^2)\). After the
prefactor \(1/\det R\) and sign averaging, this gives exactly
\(e^{D_2}=(1-\rho^4)^{-1}\).

The local expansion was checked independently from the Hermite generating
function. Coordinatewise sign averaging retains only multi-indices with all
even entries. The smallest surviving multigraph is a doubled edge, producing
the coefficient \(\varepsilon^4A_{ij}^4\) in the squared \(L^2\) norm. The
only three-edge even-degree multigraph is a triangle, whose Hermite norm is
\((2!)^3=8\), producing the stated sixth-order term. All remaining terms
have at least four edges and begin at order eight. The deterministic
verification artifact agrees with the exact determinant formula.

## Originality

Ouimet and Greaves (2026), arXiv:2609.20234, is the closest source. Their
Corollary 4.11 considers the same pair \((P_R,Q)\) and the same order-2 Rényi
total correlation, but gives a Cauchy--Schwarz lower bound based on product
moments. The paper explicitly motivates that certificate as avoiding direct
evaluation of the joint density ratio. The inspected theorem and corollary do
not give the exact divergence, characterize when it is infinite, or state
the bivariate formula or the weak-correlation cycle expansion.

Benko, Hübnerová and Witkovský (2025) give the full multivariate folded-normal
density as a sum of \(2^n\) sign-reflected Gaussian densities and develop its
MGF and characteristic function. Their accessible full text was checked for
Rényi divergence, chi-square divergence, divergence, and entropy terminology;
no such calculation was located. The older univariate folded-normal
information literature concerns entropy or KL-type quantities and does not
cover the centered multivariate total-correlation problem here.

Searches for combinations of "Gaussian magnitudes", "absolute Gaussian",
"multivariate folded normal", "Rényi total correlation", "chi-square
divergence", the exact bivariate expression \(1-\rho^4\), and the spectral
threshold did not locate a prior statement of the displayed formulas.
Accordingly the originality assessment is **to the best of our knowledge**.

The principal residual originality risk is generic Gaussian-mixture
\(L^2\)/chi-square-divergence literature. Closed-form overlaps of Gaussian
mixtures are standard, and an older source may contain a general formula
that specializes mechanically to the determinant average here without
discussing folded Gaussians or total correlation. This is why the record
claims the folded-Gaussian specialization, finiteness threshold, bivariate
closed form, and local cycle expansion, not novelty of Gaussian integration.

## Value

The result turns the new product-moment lower certificate into an exact
information quantity. The finiteness criterion shows that order-2 total
correlation can diverge strictly inside the positive-definite correlation
cone; positive equicorrelation gives an explicit threshold
\(\rho=1/(n-1)\). In two dimensions, the full dependence measure collapses
to the elementary identity \(-\log(1-\rho^4)\).

The weak-correlation expansion also exposes a structural effect of sign
loss. Ordinary Gaussian dependence is visible at quadratic order in
correlations, whereas dependence of coordinatewise magnitudes first appears
at fourth order. The next correction detects triangles at sixth order,
giving a concrete hierarchy from pairwise magnitude dependence to the first
three-way cycle term.

## Limitations

Only positive-definite correlation matrices are treated. The exact
determinant sum is exponential in dimension. No arbitrary-order Rényi
formula or computationally efficient high-dimensional approximation is
claimed.

The residual originality risk from general Gaussian-mixture overlap theory
remains material enough to state explicitly, although no inspected source
gave the present specialization or its consequences.
