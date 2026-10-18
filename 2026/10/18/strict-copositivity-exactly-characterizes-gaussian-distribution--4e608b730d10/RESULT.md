# Strict copositivity exactly characterizes Gaussian distribution-copositivity

## Finding

Let \(X=(X_1,\ldots,X_d)\) be any centered Gaussian random vector, possibly with singular covariance \(\Sigma\), satisfying \(\Sigma_{ii}>0\) for every coordinate. Following Sei's definition, let \(\beta(X)\) be the infimum of
\[
\frac{\operatorname{Var}\!\left(\sum_{i=1}^d f_i(X_i)\right)}{\sum_{i=1}^d\operatorname{Var}(f_i(X_i))}
\]
over all nonzero families of centered, nondecreasing, square-integrable coordinate functions \(f_i\). The source's formulation with admissible increasing coordinate transformations has the same infimum by its Lemma 15.

Define the nonnegative-simplex covariance minimum
\[
 m(\Sigma)=\min\left\{w^{\mathsf T}\Sigma w:\ w_i\ge0,\ \sum_{i=1}^d w_i=1\right\},\qquad M(\Sigma)=\max_i\Sigma_{ii}.
\]
Then, with no nonsingularity assumption,
\[
\boxed{\ \beta(X)>0\ \Longleftrightarrow\ m(\Sigma)>0\ \Longleftrightarrow\ \Sigma\text{ is strictly copositive}.\ }
\]
More quantitatively, whenever \(m(\Sigma)>0\),
\[
\boxed{\ \beta(X)\ge \frac{m(\Sigma)}{M(\Sigma)}>0.\ }
\]
When \(m(\Sigma)=0\), one has \(\beta(X)=0\). This settles the Gaussian covariance-copositivity implication proposed as Conjecture 4 by Sei (2021), including singular Gaussian laws.

## Assumptions and scope

Throughout, \(d\ge1\), \(X\) has mean zero and a real symmetric positive-semidefinite covariance \(\Sigma\); each marginal variance is strictly positive, so every Gaussian marginal has a Lebesgue density. Coordinate functions are nondecreasing, measurable and square-integrable, and are centered without loss of generality. The denominator is positive. The covariance is **strictly copositive** when \(w^{\mathsf T}\Sigma w>0\) for every nonzero \(w\in\mathbb R_{\ge0}^d\). Compactness of the nonnegative unit simplex makes this equivalent to \(m(\Sigma)>0\) and to the normalized version in the original source.

The result concerns the positivity of \(\beta\), not the exact numerical value of \(\beta\). It does not establish the separate, stronger formula equating \(\beta\) to the optimal linear copositivity modulus.

## Proof

**1. Positive common-factor decomposition.** Let \(r=\operatorname{rank}\Sigma\), choose a real \(d\times r\) factor \(B\) with \(\Sigma=BB^{\mathsf T}\), and write its row vectors as \(b_i\in\mathbb R^r\). Let \(G\sim N(0,I_r)\), so \(X\) has the same law as \(BG\). Consider the compact convex hull \(C=\operatorname{conv}\{b_1,\ldots,b_d\}\). Its squared distance to the origin is exactly
\[
\operatorname{dist}(0,C)^2=\min_{w\in\Delta_{d-1}}\left\|\sum_iw_i b_i\right\|^2=m(\Sigma),
\]
where \(\Delta_{d-1}\) is the nonnegative unit simplex. Suppose \(m(\Sigma)>0\), and let \(p\in C\) be a closest point to the origin, of length \(\delta=\sqrt{m(\Sigma)}>0\). The projection variational inequality gives
\[
\langle p,b_i-p\rangle\ge0\quad\text{for every }i.
\]
Consequently, for the unit vector \(u=p/\delta\), each \(a_i=\langle b_i,u\rangle\ge\delta>0\). Decompose \(G=uZ+H\), with \(Z\sim N(0,1)\), \(H\) jointly Gaussian, supported on the orthogonal complement of \(u\), and \(Z\perp H\). Thus
\[
 X_i=a_iZ+Y_i,\qquad Y_i=\langle b_i,H\rangle,
 \qquad \operatorname{Var}(Y_i)=\Sigma_{ii}-a_i^2.
\]
Every coordinate has a strictly positive loading on the **same** Gaussian factor \(Z\).

**2. Conditional monotonicity.** For arbitrary admissible \(f_i\), fix the whole residual vector \(H\). Because \(a_i>0\), the random variables \(f_i(a_iZ+Y_i)\) are nondecreasing functions of one common real variable \(Z\). For independent copies \(Z,Z'\),
\[
 2\operatorname{Cov}(g(Z),h(Z))
 =\mathbb E[(g(Z)-g(Z'))(h(Z)-h(Z'))]\ge0
\]
for any square-integrable nondecreasing functions \(g,h\). Thus all off-diagonal conditional covariances are nonnegative. The law of total variance yields
\[
\operatorname{Var}\!\left(\sum_i f_i(X_i)\right)
\ge\mathbb E\operatorname{Var}\!\left(\sum_i f_i(X_i)\mid H\right)
\ge\sum_i\mathbb E\operatorname{Var}(f_i(X_i)\mid H).
\]
No independence among the residual coordinates \(Y_i\) is assumed or needed.

**3. Gaussian conditional-variance contraction.** Fix a coordinate with variance \(s_i^2=\Sigma_{ii}>0\), and put \(\tau_i^2=s_i^2-a_i^2\). The conditional mean of \(f_i(X_i)\) given \(H\) depends only on \(Y_i\):
\[
\mathbb E[f_i(X_i)\mid H]=\mathbb E[f_i(a_iZ+Y_i)\mid Y_i].
\]
When \(0<\tau_i<s_i\), the two standardized normals \(X_i/s_i\) and \(Y_i/\tau_i\) have correlation \(\rho_i=\tau_i/s_i\in(0,1)\). Expand the centered function in probabilists' Hermite polynomials, \(f_i(s_ix)=\sum_{k\ge1}c_{ik}H_k(x)\), with \(\sum_{k\ge1}k!c_{ik}^2<\infty\). The elementary correlated-Gaussian identity
\[
\mathbb E[H_k(X_i/s_i)\mid Y_i]
=\rho_i^k H_k(Y_i/\tau_i)
\]
follows, for instance, by conditioning the Hermite generating function \(e^{t x-t^2/2}\) and comparing coefficients. Parseval's identity therefore gives
\[
\operatorname{Var}(\mathbb E[f_i(X_i)\mid H])
=\sum_{k\ge1}k!c_{ik}^2\rho_i^{2k}
\le\rho_i^2\operatorname{Var}(f_i(X_i)).
\]
Hence the law of total variance implies
\[
\mathbb E\operatorname{Var}(f_i(X_i)\mid H)
\ge (1-\rho_i^2)\operatorname{Var}(f_i(X_i))
=\frac{a_i^2}{s_i^2}\operatorname{Var}(f_i(X_i)).
\]
If \(\tau_i=0\), then \(Y_i=0\) almost surely, the conditional mean is constant, and the same inequality holds with factor one. The case \(\tau_i=s_i\) is excluded because \(a_i>0\). Summing over coordinates in Step 2 establishes
\[
\operatorname{Var}\!\left(\sum_i f_i(X_i)\right)
\ge\min_i\frac{a_i^2}{\Sigma_{ii}}\sum_i\operatorname{Var}(f_i(X_i))
\ge\frac{m(\Sigma)}{M(\Sigma)}\sum_i\operatorname{Var}(f_i(X_i)).
\]
Taking the infimum gives the claimed quantitative lower bound.

**4. Necessity.** If \(m(\Sigma)=0\), some \(w\in\Delta_{d-1}\) satisfies \(w^{\mathsf T}\Sigma w=0\). Thus \(\sum_iw_iX_i=0\) almost surely. For the centered nondecreasing linear coordinate functions \(f_i(x)=w_ix\), the numerator defining \(\beta\) is zero, while the denominator \(\sum_iw_i^2\Sigma_{ii}\) is positive. Therefore \(\beta=0\) under the nondecreasing formulation. For a formulation requiring strictly positive slopes, replace each \(w_i\) with \(w_i+\varepsilon\) and send \(\varepsilon\downarrow0\); the ratio converges to zero. This proves both directions.

**Explicit singular, mixed-sign example.** Let \(G_1,G_2\) be independent standard Gaussian variables and set
\[
(X_1,X_2,X_3,X_4)=(G_1+3G_2,\,G_1+2G_2,\,G_1-2G_2,\,G_1-3G_2).
\]
Its covariance has rank two, diagonal \((10,5,5,10)\), and four negative off-diagonal entries among its six unordered pairs. Every convex combination of its row factors has first coordinate one, and the convex hull contains \((1,0)\), so \(m(\Sigma)=1\), \(M(\Sigma)=10\), and \(\beta\ge1/10\). This example demonstrates that a nontrivial singular covariance with a four-edge negative-correlation graph lies within the theorem.

## Verification

The companion \`verify.py\` uses only Python's standard library. It verifies the displayed exact rank-two Gram matrix, the simplex certificate \(m(\Sigma)=1\), the coefficient \(1/10\), a boundary matrix admitting a nonnegative kernel vector, and exact-rational finite checks of the Hermite-contraction and monotone-covariance mechanisms. Run \`python verify.py\` in the directory containing the files. The universal assertions are proved analytically in Steps 1–4, not by finite checks.

## Relationship to prior work

Sei's *Coordinate-wise transformation of probability distributions to achieve a Stein-type identity* (first made public June 28, 2021) defines distribution copositivity in Equation (8), proves that positive-definite Gaussian covariance is sufficient in Appendix E.2, and states the singular strictly copositive extension as **Conjecture 4** in Section 7. The theorem above gives the missing implication through a positive common Gaussian factor and an exact conditional-variance contraction, without asserting the stronger equality of linear and nonlinear moduli. Classical copositive-matrix literature treats the matrix condition but does not, by itself, establish the nonlinear Gaussian inequality.

## Limitations

The result is specific to jointly Gaussian laws with nondegenerate one-dimensional marginals; the joint distribution itself may be singular. It makes no assertion about non-Gaussian common-factor models, exact numerical evaluation of \(\beta\), uniqueness of a Stein-type transformation, or sharpness of the given covariance-simplex lower bound. Previous priority under equivalent terminology cannot be ruled out solely by bibliographic searching. Independent mathematical validation has not been performed.

## References

1. T. Sei, “Coordinate-wise transformation of probability distributions to achieve a Stein-type identity,” *Information Geometry* **5** (2022), 325–354; first published 2021-06-28. DOI: 10.1007/s41884-021-00051-9. Relevant: Equation (8), Lemma 15, Appendix E.2, Section 7, Conjecture 4. Open-access full text: https://link.springer.com/article/10.1007/s41884-021-00051-9
2. J.-B. Hiriart-Urruty and A. Seeger, “A variational approach to copositive matrices,” *SIAM Review* **52** (2010), 593–629. DOI: 10.1137/090750391. Matrix-copositivity background; not a Gaussian-distribution theorem.
