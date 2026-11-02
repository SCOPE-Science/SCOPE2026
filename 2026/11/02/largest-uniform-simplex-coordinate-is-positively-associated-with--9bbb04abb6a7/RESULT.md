# Largest uniform-simplex coordinate is positively associated with every Schur-convex statistic

## Finding
For any integer \(m\ge2\), take a random probability vector \(X\sim\operatorname{Dirichlet}(1,\ldots,1)\), i.e. uniform measure on the \((m-1)\)-dimensional probability simplex. Put \(M=\max_iX_i\). For every permutation-symmetric continuously differentiable function \(F\) defined on a neighborhood of that closed simplex and Schur-convex when restricted to it,
\[
\operatorname{Cov}(M,F(X))\ge0,
\]
with **strict inequality unless \(F\) is constant on the simplex**. For Schur-concave \(F\), the sign reverses. In particular, \(\operatorname{Cov}(M,\sum_iX_i^p)>0\) for real \(p>1\). For Shannon entropy \(H(X)=-\sum_iX_i\log X_i\), which need not have bounded derivatives at the boundary,
\[
\operatorname{Cov}(M,H(X))<0\quad(m\ge2).
\]
For two components, \(\operatorname{Cov}(M,H(X))=(\log2-1)/12\). The result is a sign theorem for a *whole order-structured class*, rather than an identity limited to a specified moment or diversity index.

## Assumptions and scope
A vector \(u\) majorizes \(v\) when their totals agree and every initial partial sum of their decreasing rearrangements is at least as large for \(u\) as for \(v\). A function is Schur-convex if it respects this preorder and Schur-concave if it reverses it. The smooth theorem requires permutation symmetry, \(C^1\) regularity in an open neighborhood of the closed simplex, and Schur-convexity on that simplex. "Nonconstant" means nonconstant *on the simplex*, not merely outside it. All coordinates are almost surely strictly positive and have distinct values. The separate entropy conclusion follows using an integrable limiting argument rather than the \(C^1\)-boundary assumption. No claim is made for arbitrary unequal Dirichlet concentration parameters.

## Proof
**Step 1: the ranked-gap simplex is uniform.** Write the decreasingly ordered coordinates of \(X\) as \(x_1>\cdots>x_m>0\) and put \(x_{m+1}=0\). Define
\[
Y_j=j(x_j-x_{j+1}),\qquad j=1,\ldots,m.
\]
Then \(Y_j>0\), \(\sum_jY_j=\sum_kx_k=1\), and the inverse transformation is \(x_k=\sum_{j=k}^mY_j/j\). The joint density of the ordered \(x\)'s is constant on their ordered simplex chamber. The displayed bijection is linear with constant nonzero Jacobian, so \(Y\sim\operatorname{Dirichlet}(1,\ldots,1)\). In particular \(M=x_1=\sum_jY_j/j\).

**Step 2: a covariance integration-by-parts identity.** For any \(C^1\) function \(f\) on the simplex and fixed coefficients \(a_j\), set \(A=\sum_ja_jY_j\). Uniform Dirichlet integration by parts gives
\[
\operatorname{Cov}(A,f(Y))
=\frac1m\,\mathbb E\sum_{1\le i<j\le m}Y_iY_j(a_i-a_j)
 (\partial_{y_i}f-\partial_{y_j}f). \tag{1}
\]
Here the partial derivatives refer to any smooth extension off the affine hyperplane; their differences are extension-independent. To prove (1), use coordinates \(y_1,\ldots,y_{m-1}\), with \(y_m=1-\sum_{\ell<m}y_\ell\). For each \(i<m\), integrate the divergence of the tangential field with components \(V_\ell=y_i(\delta_{i\ell}-y_\ell)f\) over the simplex. Its normal component vanishes on every face: on \(y_\ell=0\) and on \(y_m=0\). Expanding the divergence yields
\[
 m\,\mathbb E[(Y_i-1/m)f(Y)]
 =\mathbb E\Big[Y_i\big(\partial_{y_i}f-\sum_jY_j\partial_{y_j}f\big)\Big].
\]
The identity for \(i=m\) follows by summing over \(i\), since \(\sum_i(Y_i-1/m)=0\). Multiply by \(a_i\), sum and pair the \((i,j)\) and \((j,i)\) terms to obtain (1). The boundary argument is valid for bounded first derivatives; the entropy case will be handled separately.

**Step 3: Schur monotonicity orders all derivatives.** Define \(f(y)=F(x(y))\) and
\[
b_j(y)=\partial_{y_j}f(y)=\frac1j\sum_{k=1}^j \partial_{x_k}F(x).
\]
For a differentiable symmetric Schur-convex function, the two-coordinate transfer criterion says
\[
 (x_i-x_j)(\partial_{x_i}F-\partial_{x_j}F)\ge0.
\]
This follows directly by differentiating \(F(x+t(e_i-e_j))\) in the direction that increases an already-larger coordinate while decreasing a smaller one. Because \(x_1>\cdots>x_m\), the gradient components \(g_k=\partial_{x_k}F(x)\) are nonincreasing in \(k\), so their prefix means \(b_1\ge b_2\ge\cdots\ge b_m\). Put \(a_j=1/j\) in (1). Every term in the exact representation
\[
\boxed{\operatorname{Cov}(M,F(X))
=\frac1m\mathbb E\sum_{1\le i<j\le m}Y_iY_j
\left(\frac1i-\frac1j\right)(b_i-b_j)\ge0}
\tag{2}
\]
is nonnegative.

**Step 4: exact equality condition.** If equality holds in (2), then the sum's continuous nonnegative integrand is zero on the interior of the \(Y\)-simplex, because uniform Dirichlet has positive density there. All weights \(Y_iY_j(1/i-1/j)\) are strictly positive in its interior. Thus \(b_i=b_j\) everywhere there for all \(i,j\). Consequently the gradient of \(f\) annihilates every tangent direction \(e_i-e_j\); since the simplex interior is connected, \(f\) is constant. By continuity and permutation symmetry, \(F\) is constant on the whole simplex. Conversely a constant has zero covariance. Applying the result to \(-F\) establishes the Schur-concave case.

**Step 5: entropy at the boundary.** The symmetric function \(-H(x)=\sum_kx_k\log x_k\) is strictly Schur-convex. Replace it by the smooth functions \(F_\varepsilon(x)=\sum_k(x_k+\varepsilon)\log(x_k+\varepsilon)\), with \(\varepsilon>0\). For each \(\varepsilon\), (2) has strictly positive terms on the interior because \(\partial_{x_k}F_\varepsilon=1+\log(x_k+\varepsilon)\) is strictly decreasing along sorted \(x\). Since \(x\log x\) extends continuously at zero, \(F_\varepsilon\to-H\) uniformly on the compact simplex. More strongly, in the integrand in (2), each difference of prefix means increases as \(\varepsilon\downarrow0\) (it is a positive weighted sum of logarithmic ratios of distinct ordered coordinates); monotone convergence applies termwise. The positive limiting integral is finite by the left covariance limit, and remains strictly positive because its integrand is positive on the interior. Hence \(\operatorname{Cov}(M,-H)>0\), as claimed. For \(m=2\), elementary integration with \(X_1\) uniform on \([0,1]\), \(M=\max(X_1,1-X_1)\), and \(H=-X_1\log X_1-(1-X_1)\log(1-X_1)\) yields \(\operatorname{Cov}(M,H)=(\log2-1)/12\).

## Verification
The accompanying standalone program `verify.py` expresses ordered coordinates as exact rational linear forms in the uniform Dirichlet gaps and integrates polynomials using the factorial Dirichlet moment rule. It independently computes \(\operatorname{Cov}(M,\sum_iX_i^p)\) and the right side of (2) for all \(2\le m\le8\) and \(p\in\{2,3,4\}\). Every compared fraction is equal and strictly positive: 63 exact assertions passed, plus an analytic sign check for the two-dimensional entropy example, 64 total. These finite checks are diagnostics; Steps 1–5 prove the statements for all dimensions and all permitted functions.

## Relationship to prior work
Barthe, Gamboa, Lozada-Chang and Rouault (arXiv:1002.1544, first posted 2010-02-08) develop Dirichlet geometry and coordinate negative association; the latter concerns disjoint coordinate sets and does not imply covariance signs for *overlapping symmetric functions of the entire vector*. Itkin (arXiv:2302.13707) studies ranked Dirichlet weights and their moment distributions; such marginal/rank moments do not establish (2) for every Schur-convex statistic. A previously available isolated identity for the covariance with the squared-spacing sum is a special instance of the sign consequence here, not a proof of the all-function statement. The key structural addition is the uniform Dirichlet distribution of ranked gaps coupled with the exact positive-pair covariance representation (2). The standard differentiable Schur-convexity criterion supplies the deterministic gradient ordering; the Dirichlet covariance identity supplies the probabilistic sign mechanism.

## Limitations
The law is established only for the uniform (all concentration parameters one) Dirichlet distribution. No implication for arbitrary asymmetric Dirichlet parameters, stochastic domination, joint association of arbitrary pairs of Schur-convex statistics, or correlation rates is asserted. The one-dimensional entropy formula is illustrative rather than a substitute for the general proof. Priority comparisons are limited to inspected accessible primary sources and indexed searches; an equivalent result in earlier literature remains possible. Independent assessment has not been performed.

## References
- F. Barthe, F. Gamboa, L. Lozada-Chang and A. Rouault, *Generalized Dirichlet distributions on the ball and moments*, arXiv:1002.1544v1, publicly submitted 2010-02-08, https://arxiv.org/abs/1002.1544 .
- D. Itkin, *Generalized Rank Dirichlet Distributions*, arXiv:2302.13707, 2023, https://arxiv.org/abs/2302.13707 .
