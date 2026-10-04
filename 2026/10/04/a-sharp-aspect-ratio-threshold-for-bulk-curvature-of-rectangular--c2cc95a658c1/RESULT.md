# A sharp aspect-ratio threshold for bulk curvature of rectangular determinantal degrees
## Finding
Let \(2\le m<n\), and let \(D_{m,n,r}\) denote the projective degree of the determinantal variety
\[
\left\{[A]\in\mathbb P(\operatorname{Mat}_{m\times n}(\mathbb C)): \operatorname{rank}A\le r\right\},
\qquad 0\le r\le m.
\]
For an interior rank \(1\le r\le m-1\), put \(c=m-r\). Then the neighboring-rank curvature ratio is
\[
\frac{D_{m,n,r-1}D_{m,n,r+1}}{D_{m,n,r}^2}
=
\frac{c(n+c)(n-m+c)(m-c)}{(n-m+2c)^2\bigl((n-m+2c)^2-1\bigr)}.
\]

Now take any integer sequences with \(m_k\to\infty\), \(n_k/m_k\to\lambda>1\), and \(c_k/m_k\to x\in(0,1)\). Then
\[
\frac{D_{m_k,n_k,m_k-c_k-1}D_{m_k,n_k,m_k-c_k+1}}{D_{m_k,n_k,m_k-c_k}^2}
\longrightarrow
R_\lambda(x)
:=
\frac{x(\lambda+x)(\lambda-1+x)(1-x)}{(\lambda-1+2x)^4}.
\]
There is a sharp aspect-ratio threshold
\[
\lambda_*:=\frac{1+\sqrt{17}}4\approx1.2807764064.
\]
If \(\lambda>\lambda_*\), then \(R_\lambda(x)<1\) for every \(x\in(0,1)\); hence every fixed bulk rank is eventually strictly log-concave. If \(1<\lambda<\lambda_*\), then \(R_\lambda(x)>1\) on a nonempty open interval of \(x\)-values; hence a bulk log-convex rank window persists asymptotically. At the critical aspect ratio, \(R_{\lambda_*}(x)\le1\) for every \(x\in(0,1)\), with equality at a unique point \(x_*\in(0,1)\), numerically
\[
x_*\approx0.0566631563.
\]

## Assumptions and scope
The ground field is \(\mathbb C\). The matrix is generic and rectangular, with \(2\le m<n\). The finite exact identity applies to every interior rank. The phase statement concerns bulk ranks: \(c/m\to x\) with limiting value \(x\in(0,1)\). No claim is made here about a uniform finite-size threshold simultaneously covering coranks that themselves approach an endpoint on a smaller scale.

## Proof
For \(m\le n\), the classical degree product for the rank-at-most-\(r\) determinantal variety is
\[
D_{m,n,r}
=
\prod_{j=0}^{m-r-1}
\frac{(n+j)!\,j!}{(r+j)!\,(n-r+j)!}.
\]
Friedland and Krattenthaler reproduce this classical determinantal-degree product as their formula (1.2), after interchanging row and column parameters when necessary.

Set \(c=m-r\) and write \(D_c=D_{m,n,m-c}\). Direct cancellation in the product gives
\[
\frac{D_{c+1}}{D_c}
=
\frac{(n+c)!\,c!\,(n-m+c)!}
{(m-c-1)!\,(n-m+2c)!\,(n-m+2c+1)!}.
\]
Therefore
\[
\frac{D_{m,n,r-1}D_{m,n,r+1}}{D_{m,n,r}^2}
=
\frac{D_{c+1}/D_c}{D_c/D_{c-1}},
\]
and a second cancellation yields the displayed exact rational function.

For the scaling limit, divide numerator and denominator by \(m^4\) and use \(n/m\to\lambda\) and \(c/m\to x\). This gives \(R_\lambda(x)\).

For fixed \(x\in(0,1)\), logarithmic differentiation with respect to the aspect ratio gives
\[
\frac{\partial}{\partial\lambda}\log R_\lambda(x)
=
-\frac{2\lambda^2+2\lambda x-\lambda-1}
{(\lambda+x)(\lambda+x-1)(\lambda+2x-1)}.
\]
The denominator is positive for \(\lambda>1\), and the numerator is positive because at \(\lambda=1\) it equals \(2x>0\) and it increases with \(\lambda\). Thus \(R_\lambda(x)\) is strictly decreasing in \(\lambda\).

Define
\[
F_\lambda(x)
:=(\lambda-1+2x)^4-x(\lambda+x)(\lambda-1+x)(1-x).
\]
At the critical value \(\lambda_*=(1+\sqrt{17})/4\), exact expansion factors as
\[
F_{\lambda_*}(x)
=
\frac1{1088}
\left(
136x^2+(-102+34\sqrt{17})x+51-13\sqrt{17}
\right)^2.
\]
Hence \(R_{\lambda_*}(x)\le1\). The quadratic factor has negative value at \(x=0\), positive value at \(x=1\), positive leading coefficient, and negative product of roots, so it has exactly one root \(x_*\in(0,1)\); this is the unique critical equality point. Strict decrease in \(\lambda\) now proves both sides of the phase transition: above \(\lambda_*\), every bulk point is strictly log-concave, while below \(\lambda_*\), the value at \(x_*\) is strictly greater than one, and continuity supplies an open log-convex interval.

## Verification
The bundled exact-arithmetic checker independently reconstructs the classical factorial product, verifies the neighboring-rank rational identity throughout a finite grid, checks the critical square factorization in the quadratic field \(\mathbb Q(\sqrt{17})\), and regression-tests the predicted sign change on both sides of the threshold. All finite identity checks use exact integers or rational arithmetic; decimal values are used only for diagnostics.

The finite replay is not used as an infinite proof. The asymptotic theorem follows from the exact adjacent-rank identity, its scaling limit, strict aspect-ratio monotonicity, and the exact critical factorization.

## Relationship to prior work
Friedland and Krattenthaler explicitly record the general rectangular determinantal degree product and identify it with the number of plane partitions in a box. Their paper studies parity and \(2\)-adic valuations of these degrees, including rectangular matrices. Full-text inspection found no log-concavity, adjacent-rank curvature, aspect-ratio phase transition, or threshold statement of the form proved here.

A previously recorded square-matrix result gives a rank-curvature transition when the aspect ratio is exactly one. The present statement is not a restatement of that special case: it treats the genuinely rectangular two-parameter family and identifies a global aspect-ratio boundary separating persistence of a bulk log-convex window from eventual bulk log-concavity at every scaled rank.

Claim-specific searches for rectangular determinantal degree log-concavity, adjacent-rank degree ratios, plane-partition box aspect-ratio curvature, and the exact algebraic threshold did not locate a published statement implying this phase theorem.

## Limitations
The phase theorem is asymptotic in the joint limit of the two matrix dimensions. It does not assert that the same irrational threshold is an exact finite-size cutoff for every rank at a fixed pair \((m,n)\). Endpoint regimes where \(c/m\to0\) or \(c/m\to1\) require separate scaling. The literature comparison cannot exclude an unindexed source that derives the same rational ratio or aspect-ratio threshold from the equivalent plane-partition product.

## References
S. Friedland and C. Krattenthaler, *2-adic valuations of certain ratios of products of factorials and applications*, arXiv:math/0508498, first submitted 25 August 2005; Linear Algebra and its Applications 426 (2007), 159--189, DOI 10.1016/j.laa.2007.04.008.

J. Harris and L. W. Tu, *On symmetric and skew-symmetric determinantal varieties*, Topology 23 (1984), 71--84. The general rectangular degree formula is cited by Friedland--Krattenthaler in the same discussion as classical determinantal-degree formulas.
