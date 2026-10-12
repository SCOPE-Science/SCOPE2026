# Sharp inverse-moment thresholds and logarithmic tails for two Gaussian tensor sketches

## Finding

The two Gaussian tensor sketch constructions used in structured least squares can have radically different unbounded-error behavior despite identical row counts. Fix integers \(r_1,r_2\ge1\), set \(R=r_1r_2\), and take any ambient tensor dimensions \(n_1,n_2\ge2\). Write \(e_1,e_2\) for their first two coordinate vectors and consider the one-column regression
\[
 a=e_1\otimes e_1,\qquad b=\theta a+\delta(e_2\otimes e_2),\qquad\delta\ne0.
\]
The unsketched minimizer is uniquely \(\theta\); the one-column design is perfectly conditioned. For \(j=0,1,2\), let \(\widehat\theta_j\) minimize \(\|S_j(ax-b)\|_2^2\) and put \(E_j=(\widehat\theta_j-\theta)/\delta\). The sketches, all with \(R\) rows, are:

* **Factor-reusing tensor sketch:** \(S_1=P\otimes Q\), where the \(r_1\times n_1\) matrix \(P\) and the \(r_2\times n_2\) matrix \(Q\) have independent standard Gaussian entries.
* **Independent-row tensor sketch:** row \(i\) of \(S_2\) is \(p_i^{\mathsf T}\otimes q_i^{\mathsf T}\), with independent standard Gaussian factors \(p_i\in\mathbb R^{n_1}\), \(q_i\in\mathbb R^{n_2}\), independently resampled for every \(1\le i\le R\).
* **Dense Gaussian reference:** \(S_0\) has \(R\) independent standard Gaussian rows in \(\mathbb R^{n_1n_2}\).

All three estimates exist uniquely almost surely. For every real \(p>0\),
\[
 \mathbb E|E_1|^p<\infty\ \Longleftrightarrow\ p<\min(r_1,r_2),
 \qquad
 \mathbb E|E_2|^p<\infty\ \Longleftrightarrow\ p<R,
 \qquad
 \mathbb E|E_0|^p<\infty\ \Longleftrightarrow\ p<R.
\]
In the finite ranges, put
\[
 M_d(p)=\frac{\Gamma((p+1)/2)\Gamma((d-p)/2)}{\sqrt\pi\,\Gamma(d/2)}.
\]
Then \(\mathbb E|E_1|^p=M_{r_1}(p)M_{r_2}(p)\) and \(\mathbb E|E_0|^p=M_R(p)\). In particular, \(\mathbb E E_1^2=[(r_1-2)(r_2-2)]^{-1}\) if both dimensions exceed two and is infinite otherwise, whereas \(\mathbb E E_2^2\) is finite precisely when \(R>2\). Whenever \(R>2\), the latter strictly exceeds the dense Gaussian value \(\mathbb E E_0^2=1/(R-2)\).

There is a sharper distinction *within* the common row-count moment regime: for a positive constant \(C_R\),
\[
 \mathbb P(|E_2|>t)\sim C_Rt^{-R}(\log t)^R,
 \qquad
 \mathbb P(|E_0|>t)\sim D_Rt^{-R}\quad(t\to\infty),
\]
where
\[
 C_R=\frac{\operatorname{vol}(B_R)}{\pi^R}\,
 \mathbb E_{U,Z}|\langle U,Z\rangle|^R
 =\frac{2\Gamma((R+1)/2)}{R\pi^{(R+1)/2}\Gamma(R)}\,
 \mathbb E\left(\sum_{i=1}^R Z_i^2\right)^{R/2},
 \quad
 D_R=\frac{\Gamma((R+1)/2)}{\sqrt\pi\,\Gamma(R/2+1)}.
\]
Here \(U\) is uniform on the Euclidean unit sphere in \(\mathbb R^R\) and independent of the vector \(Z\) whose coordinates are independent products of two standard Gaussian variables. For example, \(C_1=4/\pi^2\), \(C_2=1/\pi\), and \(C_4=3/\pi^2\). The tensor-row estimator thus suffers an exact logarithmic tail penalty relative to an equally tall dense Gaussian sketch.

A particularly stark comparison occurs at \(r_1=r_2=2\) (four sketch rows): the factor-reusing estimator has infinite mean squared error, whereas both the independent-row tensor and dense Gaussian estimators have finite mean squared error. The ambient dimension may be arbitrarily large, so this remains true for genuine compression from \(n_1n_2\gg4\) observations.

## Assumptions and scope

All Gaussian coordinates and factors are independent unless explicitly shared by the tensor product \(P\otimes Q\). No regularization, trimming, repeated runs, or conditioning on favorable sketches is applied. The analysis concerns exact arithmetic and the unique minimizer of the randomly sketched scalar least-squares objective; scaling any sketch by a common nonzero scalar leaves that minimizer unchanged. The response noise \(\delta(e_2\otimes e_2)\) is deterministic and orthogonal to \(a\). Integer dimensions \(r_1,r_2,n_1,n_2\) are otherwise arbitrary within the stated ranges.

## Proof

**Reduction to scalar ratios.** For any sketch whose design image \(Sa\ne0\), normal equations give
\[
 E=\frac{\langle Sa,S(e_2\otimes e_2)\rangle}{\|Sa\|_2^2}.
\]
The event \(Sa=0\) has probability zero in each construction. All coordinates outside the first two in each tensor factor disappear from this ratio; the claimed distributions therefore do not depend on ambient dimensions.

**Factor reuse and its moments.** Write \(X=Pe_1\), \(Y=Pe_2\), \(U=Qe_1\), \(V=Qe_2\). They are mutually independent, with standard Gaussian coordinates. Kronecker inner-product factorization yields
\[
 E_1=\frac{X^{\mathsf T}Y}{\|X\|^2}\frac{U^{\mathsf T}V}{\|U\|^2}.
\]
Conditioned on nonzero \(X\), the numerator \(X^{\mathsf T}Y\) is \(N(0,\|X\|^2)\); rotational invariance and independence similarly apply to \(U,V\). Therefore
\[
 E_1\ \stackrel d=\ \frac{G_1}{\chi_{r_1}}\frac{G_2}{\chi_{r_2}},
\]
where \(G_1,G_2\) are independent standard Gaussians, \(\chi_d\) is the positive square root of an independent chi-square with \(d\) degrees of freedom, and all four random variables are independent. Elementary Gaussian and chi moment integration gives
\[
 \mathbb E|G/\chi_d|^p=M_d(p)\quad(0<p<d),
\]
with divergence when \(p\ge d\) because the chi density near zero is comparable to \(z^{d-1}\). The factor product gives the first moment criterion and formula.

**Independent tensor rows and exact logarithmic tail.** Define mutually independent standard Gaussians \(X_i,Y_i,U_i,V_i\), and set \(W_i=X_iY_i\), \(Z_i=U_iV_i\), for \(1\le i\le R\). The least-squares normal equations are exactly
\[
 E_2=\frac{\sum_{i=1}^R W_iZ_i}{\sum_{i=1}^R W_i^2}.
\]
The iid \(W_i\) have the product-normal density
\[
 f(w)=\frac{K_0(|w|)}{\pi}
 =\frac{\log(1/|w|)+O(1)}{\pi}\qquad(w\to0,\ w\ne0),
\]
where \(K_0\) denotes the modified Bessel function. This follows directly by conditioning on one of two independent Gaussian factors and changing variables in the product density. The density is positive, even, integrable, bounded by \(C(1+\log_+(1/|w|))\) near zero, and exponentially decaying for large arguments.

Put \(W=\rho u\) with \(\rho>0\), \(u\) on the unit sphere. Since \(E_2=\langle u,Z\rangle/\rho\), its tail probability is exactly
\[
 \int_{S^{R-1}}\int_0^\infty
 \int_0^{|\langle u,z\rangle|/t}
 \rho^{R-1}\prod_{i=1}^R f(\rho u_i)\,d\rho\ d\sigma(u)\ d\mathbb P_Z(z),
\]
where \(d\sigma\) is unnormalized surface measure; for \(R=1\), the same expression uses the two-point zero-dimensional sphere. Change variables \(v=t\rho\). For fixed \(v>0\) and almost every angular vector with nonzero coordinates,
\[
 \frac{\prod_i f(vu_i/t)}{(\log t)^R}\longrightarrow\pi^{-R}.
\]
To justify integrating the limit, first truncate to \(\|Z\|\le t^{1/2}\). There \(0<v\le t^{1/2}\), and the density bound controls the scaled integrand by a constant times
\[
 v^{R-1}\prod_{i=1}^R\bigl(1+|\log v|+|\log|u_i||\bigr),
\]
which is integrable jointly in \(v\in(0,\|Z\|)\), sphere angle \(u\), and the product-Gaussian law of \(Z\) (all its moments and logarithmically weighted moments are finite). The excluded region \(\|Z\|>t^{1/2}\) has probability \(o(t^{-R}(\log t)^R)\) by Markov's inequality with any fixed sufficiently high moment. Dominated convergence now yields
\[
 \lim_{t\to\infty}\frac{t^R\mathbb P(|E_2|>t)}{(\log t)^R}
 =\frac1{R\pi^R}\int_{S^{R-1}}\mathbb E|\langle u,Z\rangle|^R\,d\sigma(u)=C_R>0.
\]
Using spherical rotation invariance and
\(\mathbb E|U_1|^R=\Gamma((R+1)/2)\Gamma(R/2)/(\sqrt\pi\Gamma(R))\)
turns the spherical expression into the stated gamma-and-norm formula. In particular, conditional quadratic moments and independence give \(C_2=1/\pi\); the product-normal fourth moment \(\mathbb E Z_i^4=9\) gives \(C_4=3/\pi^2\). The layer-cake formula
\[
 \mathbb E|E_2|^p=p\int_0^\infty t^{p-1}\mathbb P(|E_2|>t)\,dt
\]
shows precisely \(0<p<R\) moments are finite, while the boundary \(p=R\) already diverges because of the positive logarithmic factor.

**Dense Gaussian comparison.** The two distinct coordinate columns of \(S_0\) corresponding to the design and residual are independent standard Gaussian vectors, whence \(E_0\stackrel d=G/\chi_R\). Its finite moments equal \(M_R(p)\). For its tail, the chi distribution has \(\Pr(\chi_R<s)\sim s^R/[2^{R/2}\Gamma(R/2+1)]\) at the origin. Integrating this against \(|G|\) yields the stated \(D_R\) by Gaussian moment integration.

**Mean-square comparison.** For \(R>2\), conditioning on \(W\) gives \(\mathbb E(E_2^2\mid W)=1/\sum_iW_i^2\), since the independent products \(Z_i\) are centered with variance one. Condition instead on the first factors \(X=(X_i)\), and apply the strictly convex function \(s\mapsto1/s\) to \(\sum_iX_i^2Y_i^2\):
\[
 \mathbb E\left[\left.\frac1{\sum_iX_i^2Y_i^2}\right|X\right]
 >\frac1{\sum_iX_i^2}
\]
almost surely whenever the left conditional expectation is finite; if infinite the inequality also holds in the extended sense. The established moment threshold makes the overall left side finite for \(R>2\). Since \(\sum X_i^2\sim\chi_R^2\), taking expectations proves \(\mathbb E E_2^2>1/(R-2)=\mathbb E E_0^2\). For \(R\le2\), both squared moments diverge. This completes all claims.

## Verification

The standalone standard-library program `verify.py` is runnable with `python3 verify.py` and reports `VERIFY_OK checks=1513`. It tests sampled normal-equation identities for both tensor models and the dense Gaussian reference, Gaussian/chi moment evaluations, exact polynomial moments behind \(C_2\) and \(C_4\), and finite Rademacher averaging identities. These are 1,513 finite numerical or exact-arithmetic diagnostics; they do not prove the infinite-support density asymptotic, the tail limit, or moment divergence. Those depend on the displayed analytic arguments.

## Relationship to prior work

Chen, Li, Newton and Wright (2019; published 2020) introduced the two structured Gaussian sketches for tensor-structured least-squares problems and proved high-probability embedding guarantees. The present finite-parameter family evaluates the unconditioned error distribution, distinguishing reused tensor factors from independently resampled row products at fixed row budget. Sridhar, Pilanci and Özgür (2020) analyze Gaussian sketched least squares, relevant to the classical dense comparator but without the structured inverse-moment/logarithmic-tail comparison. Bujanović and Kressner (2020) investigate moments of products of Gaussian matrices in sketching, giving distinct numerator/norm estimates, not the present ratio singularity. Chen and Jin (2020) provide high-probability tensorized sub-Gaussian sketching-dimension guarantees, including row-wise Gaussian products in their general family; their results do not give unconditional inverse-moment thresholds or the exact Gaussian least-squares tail constant. Diao, Song, Sun and Woodruff (2017) analyze tensor-regression sketching with a different TensorSketch distribution. The distributional facts about normal products, chi variables, and spherical averages are classical and are not claimed as inventions.

## Limitations

This is an exact, low-rank, one-column regression benchmark with orthogonal deterministic residual; it is not a worst-case theorem for arbitrary designs, multiple columns, anisotropic noise, regularized estimators, or nonlinear inverse problems. Row-independent tensor sketches preserve the polynomial moment threshold of the dense comparator but still have a logarithmic tail penalty and higher mean-square error. Large ambient dimensions follow by unused coordinates and do not establish optimal implementation cost or an end-to-end algorithmic speedup. Equality of sketch row counts does not equal equality of matrix-application time or storage. Error tails measure rare failures; standard finite-budget high-probability guarantees can coexist with infinite unconditioned moments.

## References

1. K. Chen, Q. Li, K. Newton, and S. J. Wright, *Structured Random Sketching for PDE Inverse Problems*, arXiv:1909.11290, first public version September 25, 2019; SIAM Journal on Matrix Analysis and Applications 41 (2020), 1742–1770; https://arxiv.org/abs/1909.11290 ; https://doi.org/10.1137/20M1310497 .
2. K. Sridhar, M. Pilanci, and A. Özgür, *Lower Bounds and a Near-Optimal Shrinkage Estimator for Least Squares using Random Projections*, arXiv:2006.08160 (2020); https://arxiv.org/abs/2006.08160 .
3. Z. Bujanović and D. Kressner, *Norm and trace estimation with random rank-one vectors*, arXiv:2004.06433 (2020); https://arxiv.org/abs/2004.06433 .
4. K. Chen and R. Jin, *Tensor-structured sketching for constrained least squares*, arXiv:2010.09791 (2020); https://arxiv.org/abs/2010.09791 .
5. H. Diao, Z. Song, W. Sun and D. P. Woodruff, *Sketching for Kronecker Product Regression and P-splines*, arXiv:1712.09473 (2017); https://arxiv.org/abs/1712.09473 .
