# A sharp spectrum-and-orientation crossover for two-query Nyström trace estimation

## Finding
Let \(A\) be any real symmetric positive-definite \(2\times2\) matrix, available through matrix-vector products. Compare the following two unbiased estimators of \(\operatorname{tr}(A)\), each using exactly two products with \(A\):

1. **Two-probe Hutchinson:** with independent vectors \(z_1,z_2\in\{-1,+1\}^2\) having independent symmetric coordinates, set
   \[
   H=\tfrac12(z_1^{\mathsf T}Az_1+z_2^{\mathsf T}Az_2).
   \]
2. **One-sketch Nyström plus one Rademacher residual probe:** with independent \(u\sim N(0,I_2)\) and \(z\in\{-1,+1\}^2\), form
   \[
   B=\frac{(Au)(Au)^{\mathsf T}}{u^{\mathsf T}Au},\qquad
   N=\operatorname{tr}(B)+z^{\mathsf T}(A-B)z.
   \]
   Computing \(Au\) and \(Az\) costs two matrix-vector products. The formula is a Gaussian-sketch/Rademacher-residual variant of the one-pass Nyström trace-decomposition method, **not** the all-Gaussian implementation of Nyström++.

Write
\[
A=\beta U_\theta\begin{pmatrix}t^2&0\\0&1\end{pmatrix}U_\theta^{\mathsf T},\quad
U_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},
\quad \beta>0,\quad t\ge1.
\]
The value of \(\sin^2(2\theta)\) does not depend on sign or coordinate-permutation conventions. The **exact variances** are
\[
\boxed{\operatorname{Var}(H)=\frac{\beta^2(t^2-1)^2}{2}\sin^2(2\theta)}
\]
and
\[
\boxed{\operatorname{Var}(N)=\beta^2\left[
\frac{2t^3}{(t+1)^2}
+\frac{t(t-1)^2(t^2+4t+1)}{2(t+1)^2}\sin^2(2\theta)
\right].}
\]
For \(t>1\), define
\[
Q(t)=\frac{4t^3}{(t-1)^2(t^2+1)(t^2+3t+1)}.
\]
Then the Nyström variant has **strictly smaller variance** than two-probe Hutchinson if and only if
\[
\boxed{\sin^2(2\theta)>Q(t).}
\]
Equality of variances occurs at equality in this inequality; elsewhere the reverse comparison holds. At \(t=1\), the Nyström variance is \(\beta^2/2\) whereas the Hutchinson variance is zero.

Moreover, \(Q\) decreases strictly from infinity to zero on \((1,\infty)\). There is a unique \(t_*>1\) defined by
\[
(t_*-1)^2(t_*^2+1)(t_*^2+3t_*+1)=4t_*^3,
\]
with \(t_*\approx1.752931245525\), hence \(t_*^2\approx3.072767951539\). Thus, if the spectral condition number is at most \(t_*^2\), **no orientation** makes the Nyström variant strictly preferable; beyond that threshold, a nonempty explicit angular sector does. For example, at \(t=2\) and \(\theta=\pi/4\), the variances are \(29\beta^2/9\) (Nyström) and \(9\beta^2/2\) (Hutchinson), whereas at the same eigenvalues but \(\theta=0\), they are \(16\beta^2/9\) and zero.

This orientation reversal survives in **every dimension** \(d\ge3\) for strictly positive-definite matrices: for each \(t>t_*\), choose any \(0<\theta_-<\tfrac12\arcsin\sqrt{Q(t)}\) and \(\theta_+=\pi/4\), then append an identical sufficiently small positive diagonal tail \(\delta I_{d-2}\). In particular, neither compared matrix needs to be diagonal. The resulting two matrices have identical eigenvalues but opposite strict orderings of the two estimators' variances, with the same one-sketch/one-residual-probe versus two-probe comparison.

## Assumptions and scope
All arithmetic is exact; \(u,z,z_1,z_2\) are mutually independent when the two estimators are defined; the Gaussian sketch is standard isotropic and each Rademacher vector has independent equiprobable signs. The only access counted is a product \(v\mapsto Av\); inner products, vector arithmetic, and forming the rank-one matrix implicitly are not counted as products. The main exact classification holds for every real symmetric positive-definite \(2\times2\) input, any positive scale \(\beta\), and every eigenvector orientation. The higher-dimensional consequence concerns a specific family with a small positive isotropic tail, rather than an exact all-matrix formula.

## Proof
**1. Residual identity and unbiasedness.** Let \(u=(u_1,u_2)^{\mathsf T}\ne0\), and let \(J u=(-u_2,u_1)^{\mathsf T}\). In two dimensions, direct multiplication gives
\[
A-\frac{(Au)(Au)^{\mathsf T}}{u^{\mathsf T}Au}
=\frac{\det A}{u^{\mathsf T}Au}(Ju)(Ju)^{\mathsf T}.
\]
This is positive semidefinite and has off-diagonal entry
\[
(A-B)_{12}=-\frac{(\det A)u_1u_2}{u^{\mathsf T}Au}.
\]
For a symmetric \(2\times2\) matrix \(R\) and a Rademacher probe \(z\), the exact centered quadratic form is
\[
z^{\mathsf T}Rz-\operatorname{tr}(R)=2R_{12}z_1z_2.
\]
Its conditional mean is zero and its conditional variance is \(4R_{12}^2\). The decomposition \(A=B+(A-B)\) proves unbiasedness of \(N\); averaging two independent probes similarly proves unbiasedness of \(H\). Therefore
\[
\operatorname{Var}(N)=4(\det A)^2\mathbb E\frac{u_1^2u_2^2}{(u^{\mathsf T}Au)^2},
\qquad \operatorname{Var}(H)=2A_{12}^2.
\]

**2. Exact Gaussian angular moments.** Use rotational invariance to write \(u=U_\theta(x,y)^{\mathsf T}\), where \(x,y\) are independent standard Gaussians. Set \(D=t^2x^2+y^2\). Polar integration yields
\[
\mathbb E\frac{x^2}{D}=\frac1{t(t+1)},\qquad
\mathbb E\frac{y^2}{D}=\frac1{t+1}.
\]
For example, setting \(s=\tan\phi\) in the uniform angular integral reduces the first identity to the rational integral
\[
\frac2\pi\int_0^\infty\frac{ds}{(s^2+1)(s^2+t^2)}=\frac1{t(t+1)}.
\]
Differentiating this first expectation with respect to \(t^2\), then using \(t^2x^2+y^2=D\), gives all three needed fourth-order ratio moments:
\[
\begin{aligned}
\mathbb E\frac{x^4}{D^2}&=\frac{2t+1}{2t^3(t+1)^2},\\
\mathbb E\frac{x^2y^2}{D^2}&=\frac1{2t(t+1)^2},\\
\mathbb E\frac{y^4}{D^2}&=\frac{t+2}{2(t+1)^2}.
\end{aligned}
\]
All these integrals are finite and differentiation is justified locally on \(t>0\) by bounded homogeneous angular integrands.

Now
\[
u_1u_2=\tfrac12\sin(2\theta)(x^2-y^2)+\cos(2\theta)xy.
\]
The cross term has zero expectation after division by \(D^2\), by oddness. Substituting the displayed ratio moments and \(\det A=\beta^2t^2\) gives the stated exact Nyström variance. Since \(A_{12}=\beta(t^2-1)\sin(2\theta)/2\), the Hutchinson variance follows immediately.

**3. Sharp comparison and uniqueness of the boundary.** Algebraic subtraction yields
\[
\operatorname{Var}(N)-\operatorname{Var}(H)
=\frac{\beta^2}{2(t+1)^2}
\left[4t^3-(t-1)^2(t^2+1)(t^2+3t+1)\sin^2(2\theta)\right].
\]
For \(t>1\), the sign is exactly the sign of \(Q(t)-\sin^2(2\theta)\). Differentiation gives
\[
Q'(t)=-\frac{4t^2(t+1)(3t^4+2t^3+2t+3)}
{(t-1)^3(t^2+1)^2(t^2+3t+1)^2}<0.
\]
The limits at both endpoints and the intermediate value theorem prove the unique threshold and the strict classification, including equality cases. At \(t=1\) the two formulas give the separate isotropic case.

**4. Persistence in positive-definite higher dimensions.** For \(d\ge3\), fix \(t>t_*\) and write \(A_\delta^\theta=(\beta U_\theta\operatorname{diag}(t^2,1)U_\theta^{\mathsf T})\oplus\delta I_{d-2}\) with \(\delta>0\). These matrices have the same eigenvalues for both choices of \(\theta\). Hutchinson's two-probe variance is \(2\sum_{i<j}(A_\delta^\theta)_{ij}^2\), thus independent of \(\delta\). For Nyström, conditional Rademacher variance is \(4\sum_{i<j}(R_\delta)_{ij}^2\) with \(R_\delta=A_\delta^\theta-B_\delta\). Almost surely, \(R_\delta\) converges in entries to the two-dimensional residual embedded with zeros as \(\delta\downarrow0\). Furthermore \(0\preceq R_\delta\preceq A_\delta^\theta\), so for bounded \(\delta\), \(\|R_\delta\|_F^2\le(\operatorname{tr}A_\delta^\theta)^2\) is uniformly bounded. Dominated convergence proves convergence of Nyström variance to the two-dimensional formula. Its strict advantage at \(\theta_+=\pi/4\) and its strict disadvantage at any \(0<\theta_-<\tfrac12\arcsin\sqrt{Q(t)}\) therefore both persist for small \(\delta>0\). The two matrices have the same eigenvalues and both have a nonzero off-diagonal entry in the leading block. This establishes the same-spectrum reversal in every dimension without requiring a diagonal input.

## Verification
The standalone `verify.py` checks the full symbolic residual identity, the closed-form angular moment identities and resulting variance formulas, the exact comparison factorization, and the sign-determining derivative. It also checks 28 independent deterministic angular quadratures over seven eigenvalue ratios and four orientations, the exact \(t=2\) examples, and the unique positive critical root. It ran successfully with output:

```text
VERIFY_OK: symbolic identities=16, angular quadratures=28, critical_sqrt_ratio=1.752931245525, critical_ratio=3.072767951539, example_N=29/9_H=9/2
```

Run `python verify.py` after installing the dependency in `requirements.txt`. These finite and symbolic computations corroborate the proof; the theorem's universal quantifiers rest on the analytic identities and inequalities above.

## Relationship to prior work
Persson, Cortinovis and Kressner [1] introduce and analyze Nyström++ (their Algorithm 5), including the one-pass Gaussian sketch-plus-residual decomposition. Their analyzed implementation uses **Gaussian probes for both components**, whereas the present variant deliberately uses a Gaussian sketch and a Rademacher correction, and compares it at exactly two products to Rademacher Hutchinson. Their general concentration results neither state nor yield the exact basis-orientation boundary without the present two-dimensional integration.

Gambhir, Stathopoulos and Orginos [2] prove that singular-vector (SVD) deflation can increase stochastic-trace variance and derive general spectral/orientation expressions for SVD-deflated residuals. This already establishes the broader phenomenon that deflation need not help. Their exact-SVD deflation is different from a random Gaussian Nyström sketch, and their theorems do not directly provide the joint condition-number/coordinate-orientation phase diagram above. The classical Rademacher off-diagonal variance identity is an acknowledged ingredient, not a novelty claim. The contribution here is the **closed and sharp all-orientation finite-query crossover for the particular randomized Nyström/Rademacher construction**, including its spectral existence threshold and higher-dimensional persistence.

## Limitations
This is not a comparison of all possible two-product estimators or a general optimality theorem. Indeed, for \(2\times2\) matrices, querying both coordinate vectors deterministically recovers the trace exactly; the experiment isolates two prescribed, scalable randomized designs. The Nyström variant is not identical to the all-Gaussian Nyström++ implementation. The exact phase boundary is proved only for two dimensions; the higher-dimensional statement is an existence-and-continuity extension for small positive diagonal tails, not an all-SPD classification. Finite precision, dependent probes, and alternative sketch/trace-query budget splits are not analyzed. General facts about variance increasing under deflation predate this result; an unpublished or differently formulated equivalent finite-dimensional computation remains possible. No independent priority or scientific audit has been performed.

## References
[1] D. Persson, A. Cortinovis, D. Kressner, *Improved variants of the Hutch++ algorithm for trace estimation*, arXiv:2109.10659, first posted 2021-09-22 (Algorithm 5 and Sections 3–3.1), journal version SIAM J. Matrix Anal. Appl. 43 (2022), 1162–1185. https://arxiv.org/abs/2109.10659

[2] A. S. Gambhir, A. Stathopoulos, K. Orginos, *Deflation as a method of variance reduction for estimating the trace of a matrix inverse*, arXiv:1603.05988, first posted 2016-03-18 (Section 2), SIAM J. Sci. Comput. 39 (2017), A532–A558. https://arxiv.org/abs/1603.05988
