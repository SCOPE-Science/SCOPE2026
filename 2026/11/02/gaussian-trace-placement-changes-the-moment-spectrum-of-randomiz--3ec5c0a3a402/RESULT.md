# Gaussian trace placement changes the moment spectrum of randomized generalized cross-validation

## Finding

Let \(n\ge 2\) and \(m\ge 1\) be integers. Let \(H\) be a nonzero real symmetric matrix with \(0\preceq H\prec I_n\), let \(R=I_n-H\), and fix nonzero data \(b\in\mathbb R^n\). Put \(C=\|Rb\|_2^2>0\). Given independent standard Gaussian vectors \(g_1,\dots,g_m\in\mathbb R^n\), consider the two unbiased estimates of the same effective residual degrees of freedom \(d=\operatorname{tr}R=n-\operatorname{tr}H\):

\[
D_{\mathrm{direct}}=\frac1m\sum_{j=1}^m g_j^{\mathsf T}Rg_j,
\qquad
D_{\mathrm{sub}}=n-\frac1m\sum_{j=1}^m g_j^{\mathsf T}Hg_j.
\]

Define the respective randomized generalized cross-validation scores \(G_{\mathrm{direct}}=C/D_{\mathrm{direct}}^2\) and \(G_{\mathrm{sub}}=C/D_{\mathrm{sub}}^2\), taking values on their almost-sure nonzero denominators. Although both denominators have expectation \(d\), they give **different sharp positive-moment thresholds**: for every real \(q>0\),

\[
\mathbb E[G_{\mathrm{direct}}^q]<\infty
\quad\Longleftrightarrow\quad q<\frac{mn}{4},
\qquad
\mathbb E[G_{\mathrm{sub}}^q]<\infty
\quad\Longleftrightarrow\quad q<\frac12.
\]

The latter threshold never improves with the number of Gaussian probes. More precisely, as \(t\to\infty\),

\[
\Pr(G_{\mathrm{direct}}>t)\sim
\frac{(m/2)^{mn/2}C^{mn/4}}{\Gamma(mn/2+1)\det(R)^{m/2}}
 t^{-mn/4},
\]

and

\[
\Pr(G_{\mathrm{sub}}>t)\sim
2\sqrt C\,f_H(n)\,t^{-1/2},
\]

where \(f_H\) is the continuous, strictly positive density on \((0,\infty)\) of \(m^{-1}\sum_jg_j^{\mathsf T}Hg_j\). In particular \(0<f_H(n)<\infty\).

If the probes are instead independent Rademacher vectors with coordinates \(\pm1\), then \(D_{\mathrm{direct}}=D_{\mathrm{sub}}\ge n\lambda_{\min}(R)>0\) **for every realization**, so both randomized scores coincide and have moments of every positive order. The same conclusion holds for any isotropic probe law supported on the sphere of radius \(\sqrt n\).

## Assumptions and scope

This is a pointwise statement for a **fixed** symmetric positive-contraction smoothing matrix \(H\) and **fixed** nonzero residual data \(b\), not for a matrix or data vector selected using the same probes. Gaussian test vectors are independent and unnormalized, with covariance \(I_n\); numerator \(C\) is not randomized. The score convention omits any deterministic dimensional prefactor, which does not change finiteness thresholds. We assume \(H\ne0\); if \(H=0\), the subtraction denominator is the deterministic value \(n\) and has no pole. Strict \(H\prec I_n\) guarantees \(R\succ0\); boundary singular residual smoothers are not covered by the direct threshold claimed here.

## Proof

Diagonalize \(R=U\operatorname{diag}(\lambda_1,\dots,\lambda_n)U^{\mathsf T}\), with every \(\lambda_i>0\). Orthogonal Gaussian invariance gives

\[
D_{\mathrm{direct}}=m^{-1}\sum_{i=1}^n\lambda_i\sum_{j=1}^m Z_{ij}^2,
\]

with \(mn\) independent standard normal variables. Near zero, the joint Gaussian density tends uniformly to its origin value on the shrinking ellipsoid \(\sum_{ij}\lambda_i Z_{ij}^2<m\varepsilon\). Its volume yields the exact small-ball equivalent

\[
\Pr(D_{\mathrm{direct}}<\varepsilon)
\sim\frac{(m/2)^{mn/2}}{\Gamma(mn/2+1)\det(R)^{m/2}}
\varepsilon^{mn/2}.
\]

Since \(G_{\mathrm{direct}}>t\) precisely when \(D_{\mathrm{direct}}<\sqrt{C/t}\), substitution proves its tail equivalent. Since \(D_{\mathrm{direct}}\) is positive with exponentially light upper tail, integration of \(\Pr(G>t)\) establishes the iff moment criterion, including divergence at equality.

Write the positive eigenvalues of \(H\) as \(\eta_1,\dots,\eta_r\), where \(1\le r\le n\). Then

\[
S_H:=m^{-1}\sum_jg_j^{\mathsf T}Hg_j
=\sum_{i=1}^r(\eta_i/m)\,Y_i,
\qquad Y_i\sim\chi_m^2
\]

with independent \(Y_i\). Each summand has a strictly positive gamma density on \((0,\infty)\). Convolution shows that \(S_H\) has a continuous, finite, strictly positive density at every \(s>0\), in particular \(f_H(n)>0\). For every sufficiently small \(\varepsilon>0\),

\[
\Pr(|D_{\mathrm{sub}}|<\varepsilon)
=\int_{n-\varepsilon}^{n+\varepsilon} f_H(s)\,ds
\sim 2\varepsilon f_H(n).
\]

Substituting \(\varepsilon=\sqrt{C/t}\) proves the second tail equivalent. Its \(t^{-1/2}\) exponent proves the second moment-spectrum criterion for every finite \(m\). The possible sign change of \(D_{\mathrm{sub}}\) does not matter because it is squared; the exact event \(D_{\mathrm{sub}}=0\) has probability zero.

Finally every fixed-norm vector \(z\) with \(\|z\|_2^2=n\) obeys

\[
z^{\mathsf T}Rz=n-z^{\mathsf T}Hz\ge n\lambda_{\min}(R).
\]

Averaging this identity over any test vectors proves samplewise equality of the two trace forms, strict positivity, and boundedness of all their reciprocal powers. Standard Rademacher probes are isotropic and satisfy the stated norm exactly.

## Verification

For the explicit scalar-smoother witness \(n=2\), \(m=3\), \(H=\tfrac12I_2\), and \(\|b\|_2=1\), the true score is \(G=1/4\). If \(X\sim\chi_6^2\), then

\[
D_{\mathrm{direct}}=X/6,\quad D_{\mathrm{sub}}=2-X/6,
\quad \mathbb E G_{\mathrm{direct}}=9/8,
\quad \mathbb E G_{\mathrm{sub}}=\infty.
\]

The exact tail coefficients simplify to

\[
\Pr(G_{\mathrm{direct}}>t)\sim(9/16)t^{-3/2},
\qquad
\Pr(G_{\mathrm{sub}}>t)\sim54e^{-6}t^{-1/2}.
\]

The included `verify.py` carries out 836 exact-rational, chi-square-density, tail-asymptotic spot checks, and exhaustive small-dimensional Rademacher checks; it returns `VERIFY_OK`. The distributional and all-dimensional statements follow from the preceding proof, not from the finite checks. Reproduce with `python verify.py` (Python standard library only).

## Relationship to prior work

Generalized cross-validation uses a squared residual divided by a squared residual effective-degrees-of-freedom trace; its stochastic approximation is discussed in the inverse-problems literature. Gazzola and Sabaté Landman (2020) explicitly discuss GCV and stochastic Hutchinson trace estimation in the full-text overview of parameter-choice rules. Chung and Gazzola (2021 preprint; 2024 SIAM Review version) survey the large-scale inverse-problem setting. Gaussian and Rademacher quadratic trace estimators themselves are classical (Girard and Hutchinson). The present comparison is not a new GCV formula or new unbiased trace estimator. It identifies the different **inverse-moment laws of two algebraically equal trace placements after unnormalized Gaussian sketching**, proves sharp tails and thresholds for all probe counts, and isolates fixed-norm probes as a samplewise remedy. Direct source comparisons did not establish a pre-existing identical theorem; a specialized earlier discussion of noisy GCV denominator poles remains a priority risk.

## Limitations

The statement concerns frozen linear smoothers, Gaussian or fixed-norm probes, a non-random numerator, and unregularized reciprocal-squared GCV scores. It does not imply that any particular implementation uses complement subtraction, that GCV minimizers inherit the same moment divergence after adapting their regularization parameter, or that a truncated/regularized denominator has infinite moments. Unbiasedness of either denominator is not unbiasedness of the corresponding nonlinear score. The fixed-norm conclusion is about denominator positivity and moment finiteness, not accuracy or relative variance. Mathematical originality is a best-knowledge assessment and has not been independently audited.

## References

1. S. Gazzola and M. Sabaté Landman, *Krylov methods for inverse problems: Surveying classical, and introducing new, algorithmic approaches*, GAMM-Mitteilungen 43 (2020), e202000017, DOI:10.1002/gamm.202000017. Full open-access text inspected, especially parameter-choice and GCV sections.
2. J. Chung and S. Gazzola, *Computational Methods for Large-Scale Inverse Problems: A Survey on Hybrid Projection Methods*, arXiv:2105.07221, first public 2021-05-15; SIAM Review 66 (2024), 205–284, DOI:10.1137/21M1441420. Publisher metadata/abstract inspected; full text unavailable in this review.
3. Tyler Chen, *The Girard–Hutchinson Estimator*, online numerical linear algebra notes, trace-estimation distribution and covariance exposition; full relevant HTML sections inspected.
4. M. F. Hutchinson, *A stochastic estimator of the trace of the influence matrix for Laplacian smoothing splines*, Communications in Statistics—Simulation and Computation 19 (1990), 433–450. Classical trace-estimation reference.
