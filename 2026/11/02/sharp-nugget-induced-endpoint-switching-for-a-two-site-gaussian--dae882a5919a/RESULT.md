# Sharp nugget-induced endpoint switching for a two-site Gaussian-process likelihood

## Finding

A fixed-variance Gaussian process can have **no finite maximum-likelihood lengthscale even with a strictly positive observation-noise nugget and nonconstant data**. In an exact two-site contrast model, an entire high-noise regime has only two competing limits: zero correlation (vanishing lengthscale) and perfect latent correlation (infinite lengthscale). The optimum jumps between these limits at an explicit, kernel-independent threshold.

**Theorem.** Fix two distinct sites, unit prior marginal variance, known prior mean zero, and a known independent Gaussian-noise variance \(h>0\). Observe the residual contrast \(Y=(b,-b)^{\mathsf T}\), where \(b\in\mathbb R\). Let the stationary kernel's intersite correlation \(t(\lambda)\) be continuous with \(0<t(\lambda)<1\) at every finite lengthscale, and with limits \(t(\lambda)\to0\) as \(\lambda\downarrow0\) and \(t(\lambda)\to1\) as \(\lambda\to\infty\). Equivalently, minimize the Gaussian negative log marginal likelihood on the compactified correlation interval \(t\in[0,1]\).

For \(h\ge1\), put
\[
\kappa(h)=\frac{h(1+h)}2\log\left(\frac{(1+h)^2}{h(h+2)}\right).
\]
Then the **complete** compactified maximum-likelihood classification is
\[
\operatorname*{argmin}_{0\le t\le1}\ell_h(t;b)=
\begin{cases}
\{1\},&b^2<\kappa(h),\\
\{0,1\},&b^2=\kappa(h),\\
\{0\},&b^2>\kappa(h).
\end{cases}
\]
Every interior \(t\in(0,1)\) is strictly worse than at least one endpoint, even on the equality curve. In particular, under the stated correlation assumptions, **no positive finite lengthscale attains the likelihood supremum** in this entire \(h\ge1\) contrast family.

The critical value \(\kappa(h)\) is strictly increasing for \(h\ge1\), satisfies \(\kappa(1)=\log(4/3)\), and tends to \(1/2\) as \(h\to\infty\). Thus a fixed contrast satisfying \(\log(4/3)<b^2<1/2\) has a unique high-noise threshold at which its preferred lengthscale jumps discontinuously from \(0\) to \(\infty\) as \(h\) increases. Furthermore, **for every \(h>0\)**, if \(b^2\ge1/2\), the unique compactified optimum is \(t=0\). Large noise therefore does *not* force a constant latent GP for every possible fixed dataset.

## Assumptions and scope

The signal variance is fixed to one, the mean function is known, the nugget variance \(h\) is known, and there are exactly two distinct sites with opposite residuals \(b\) and \(-b\). All claims concern the Gaussian marginal likelihood, not the posterior-predictive risk. The two-site latent covariance is \(\begin{psmallmatrix}1&t\\t&1\end{psmallmatrix}\). The observed covariance, including the independent nugget, is
\[
\Sigma_h(t)=\begin{pmatrix}1+h&t\\t&1+h\end{pmatrix}.
\]
For the compactified problem \(0\le t\le1\), this matrix is positive definite whenever \(h>0\); no singular limit occurs. The true lengthscale parameter is usually \(0<\lambda<\infty\); its endpoint values are *limits*, not automatically admissible finite MLEs. For squared-exponential and standard positive Matérn kernels, the required intersite correlation limits hold.

Write \(A=1+h>1\), \(z=b^2\ge0\), and
\[
\ell_h(t;b)=Y^{\mathsf T}\Sigma_h(t)^{-1}Y+\log\det\Sigma_h(t).
\]
This is twice the Gaussian negative log marginal likelihood, up to an additive constant, and thus has exactly the same minimizers.

## Proof

**1. Exact one-parameter likelihood.** The vector \((b,-b)^{\mathsf T}\) is an eigenvector of \(\Sigma_h(t)\) with eigenvalue \(A-t\). Hence
\[
\ell_h(t;b)=\frac{2z}{A-t}+\log(A^2-t^2),\qquad 0\le t\le1.
\tag{1}
\]
At \(t=0\), the first term is \(2z/A\) and the logarithm is \(2\log A\). For \(t>0\), subtracting the value at zero and factoring gives
\[
\ell_h(t;b)-\ell_h(0;b)=\frac{2t}{A(A-t)}\bigl[z-J_A(t)\bigr],
\quad J_A(t)=-\frac{A(A-t)}{2t}\log\left(1-\frac{t^2}{A^2}\right).
\tag{2}
\]
Both factors outside the square brackets are strictly positive. Notice that \(J_A(1)=\kappa(h)\).

**2. Strict ordering of the comparison threshold for \(A\ge2\).** Set \(u=t/A\in(0,1/2]\) and
\[
H(u)=-\frac{1-u}{u}\log(1-u^2)
=\sum_{k=1}^{\infty}\frac{u^{2k-1}-u^{2k}}{k}.
\]
The series and its derivative converge locally uniformly on \((0,1)\). On \(0<u\le1/2\),
\[
H'(u)=\sum_{k=1}^{\infty}\frac{u^{2k-2}}{k}
\left[(2k-1)-2ku\right]>0.
\tag{3}
\]
Indeed every bracket is nonnegative, and all those with \(k\ge2\) are strictly positive. Since \(J_A(t)=AH(t/A)/2\), \(J_A(t)\) increases strictly on \((0,1]\) when \(A\ge2\), with \(\lim_{t\downarrow0}J_A(t)=0\). Consequently, if \(z\ge J_A(1)\), equation (2) gives \(\ell_h(t;b)>\ell_h(0;b)\) for every \(0<t<1\). At \(t=1\), strict inequality holds if \(z>J_A(1)\), and equality holds if \(z=J_A(1)\).

**3. Exclusion of hidden interior minima in the other regime.** Direct differentiation of (1) yields
\[
\ell'_h(t;b)=\frac{2q_{A,z}(t)}{(A-t)^2(A+t)},
\quad q_{A,z}(t)=t^2+(z-A)t+Az.
\tag{4}
\]
For \(A\ge2\), the elementary inequality \(-\log(1-x)<x/(1-x)\) on \((0,1)\) gives
\[
\kappa(h)<\frac{A}{2(A+1)}\le\frac{A-1}{A+1}.
\tag{5}
\]
If \(0<z<\kappa(h)\), then \(q_{A,z}(0)=Az>0\), while \(q_{A,z}(1)=z(A+1)-(A-1)<0\). An upward-opening quadratic with opposite signs at the two endpoints has exactly one zero in \((0,1)\), at which the derivative switches from positive to negative. Hence its only interior stationary point is a *maximum* of \(\ell_h\); the minimum must be at an endpoint. By (2), \(\ell_h(1;b)<\ell_h(0;b)\), so \(t=1\) is the unique minimizer. If \(z=0\), equation (4) gives \(q_{A,0}(t)=t(t-A)<0\) for \(0<t\le1\), and the same conclusion holds. The tie case and remaining regime follow from Step 2. This proves the exact trichotomy.

**4. Monotonicity of the sharp threshold.** Let \(u=1/A\in(0,1/2]\), and set
\[
S(u)=\sum_{j=0}^{\infty}\frac{u^{2j}}{j+1}.
\]
Then \(\kappa(h)=(1-u)S(u)/2\). On \((0,1/2]\), \(S(u)\ge1\) and
\[
(1-u)S'(u)<\frac{2u(1-u)}{1-u^2}=\frac{2u}{1+u}\le\frac23<1\le S(u).
\]
Therefore \((1-u)S(u)\) is strictly decreasing in \(u\); since \(u=1/(1+h)\) decreases with \(h\), \(\kappa(h)\) increases strictly. At \(h=1\), substitution gives \(\log(4/3)\). As \(h\to\infty\), \(u\to0\) and \(S(u)\to1\), so \(\kappa(h)\to1/2\). Continuity and strict monotonicity give the unique noise threshold for \(\log(4/3)<z<1/2\).

**5. A no-constant-fit obstruction for every nugget.** For arbitrary \(A>1\), the inequality \(-\log(1-x)<x/(1-x)\) in (2) implies, for \(0<t\le1\),
\[
J_A(t)<\frac{A(A-t)}{2t}\frac{t^2}{A^2-t^2}
=\frac{t}{2(1+t/A)}<\frac12.
\tag{6}
\]
Thus \(z\ge1/2\) forces \(\ell_h(t;b)>\ell_h(0;b)\) for every \(t\in(0,1]\), independent of \(h>0\). This proves the all-nugget obstruction and completes the argument.

## Verification

Run `python verify.py` using Python 3 and only its standard library. The checker evaluates the exact rational derivative identity (4), compares all global candidates over broad finite parameter grids, tests both sides of the critical curve, verifies the strict interior gap at equality, checks threshold monotonicity and the high-contrast obstruction for nuggets both above and below one, and separately checks analytic derivatives by symmetric finite differences. Its deterministic execution passed **18,374 assertions**. These tests check finite instances, not uncountably many real parameter values. The proof above establishes the universally quantified conclusions independently of computation.

## Relationship to prior work

Karvonen and Oates, *Maximum Likelihood Estimation in Gaussian Process Regression is Ill-Posed* (first public arXiv version 17 March 2022), establish instability of lengthscale maximum likelihood for noiseless data and study the nugget-regularized model in Section 4. Their equation (4.1) is precisely the general regularized likelihood specialized here. They report numerical evidence that sufficiently large nuggets favor infinite lengthscales and explicitly describe analytic behavior with a nugget as unresolved. Our two-site opposite-residual theorem supplies a sharp, limited analytic phase diagram and a counterboundary: sufficiently large noise does **not** force infinite lengthscale for every fixed contrast. The existing paper's noiseless theorem and numerical experiments are not claimed as new.

Fosdick and Raftery (2012) investigate maximum-likelihood estimation of an *unconstrained* bivariate normal correlation with known marginal variances, including the classical cubic likelihood equation. Equation (4) here is a specialized derivative of that standard type. Their unrestricted estimator is not a theorem about the positive, nugget-limited GP correlation interval \([0,1/A]\), nor does the inspected paper give the sharp two-site nugget threshold or all-nugget large-contrast obstruction. Generic Gaussian-process marginal likelihood formulas are also standard. Only the constrained global optimization and its two boundary consequences are proposed as the contribution.

## Limitations

Signal amplitude, prior mean, noise variance, and the two-site design are held fixed as specified. Estimating additional hyperparameters, allowing more than two sites, permitting a negative kernel correlation, or allowing only a truncated set of correlation values can alter the classification. No result for the full middle-signal phase diagram at \(0<h<1\) is claimed. The compactified endpoints need not correspond to actual finite admissible lengthscales; indeed none do under the stated kernel conditions. This paper does not establish predictive optimality, model-selection consistency, historical priority beyond the literature inspected, or independent validation.

## References

1. Toni Karvonen and Chris J. Oates, *Maximum Likelihood Estimation in Gaussian Process Regression is Ill-Posed*, arXiv:2203.09179 (first public 17 March 2022), Section 4, https://arxiv.org/abs/2203.09179 ; Journal of Machine Learning Research 24 (2023), article 120.
2. Bailey K. Fosdick and Adrian E. Raftery, *Estimating the Correlation in Bivariate Normal Data With Known Variances and Small Sample Sizes*, The American Statistician 66 (2012), 34–41, DOI:10.1080/00031305.2012.676329, especially Section 2.
3. Carl Edward Rasmussen and Christopher K. I. Williams, *Gaussian Processes for Machine Learning*, MIT Press (2006), Chapter 5 (general Gaussian marginal likelihood and hyperparameter selection), https://gaussianprocess.org/gpml/.
