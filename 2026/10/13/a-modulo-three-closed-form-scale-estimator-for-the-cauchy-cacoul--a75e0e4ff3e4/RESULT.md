# A modulo-three closed-form scale estimator for the Cauchy–Cacoullos family
## Finding
For the Cauchy–Cacoullos family
\[
\Pr_\lambda\{X=k\}
=
\frac{\lambda\tanh(\pi\lambda)}
{\pi(\lambda^2+k^2)},
\qquad k\in\mathbb Z,\quad \lambda>0,
\]
a single modulo-three count gives a closed-form scale estimator that uniformly improves the parity estimator proposed in the motivating paper.

Let
\[
\widehat q_n
=
\frac1n\sum_{j=1}^n\mathbf 1_{\{3\mid X_j\}},
\qquad
\widehat\beta_{3,n}
=
\frac{3\widehat q_n-1}{2}.
\]
On \(0<\widehat\beta_{3,n}\le1\), define
\[
\widehat\lambda_{3,n}
=
\frac3\pi
\operatorname{arcosh}\!\left(
\frac12\sqrt{3+\widehat\beta_{3,n}^{-1}}
\right),
\]
and assign any fixed value otherwise. The exceptional rule is asymptotically irrelevant: the displayed formula holds eventually almost surely.

Then \(\widehat\lambda_{3,n}\to\lambda\) almost surely, and
\[
\sqrt n(\widehat\lambda_{3,n}-\lambda)
\Rightarrow
N(0,V_3(\lambda)).
\]
Writing
\[
c=\cosh(\pi\lambda/3),
\]
the asymptotic variance is
\[
V_3(\lambda)
=
\frac{9}{32\pi^2}
\frac{(4c^2-3)^2(4c^2-1)}{c^2}.
\]
For the source's parity estimator the asymptotic variance is
\[
V_2(\lambda)
=
\frac{\cosh^2(\pi\lambda)}{\pi^2}.
\]
Their exact ratio is
\[
\frac{V_3(\lambda)}{V_2(\lambda)}
=
\frac{9(4c^2-1)}{32c^4}
<
\frac{27}{32},
\qquad \lambda>0.
\]
The ratio decreases strictly from \(27/32\) in the limit \(\lambda\downarrow0\) to \(0\) as \(\lambda\to\infty\). Hence the modulo-three construction reduces asymptotic variance by more than \(5/32\) uniformly over the parameter space.

Using the Fisher information in the source,
\[
I(\lambda)\longrightarrow\frac{4\pi^2}{3}
\qquad(\lambda\downarrow0).
\]
Consequently the modulo-three estimator's small-scale asymptotic efficiency relative to the MLE tends to
\[
\frac{1}{I(\lambda)V_3(\lambda)}
\longrightarrow\frac89,
\]
whereas the parity estimator tends to \(3/4\).

## Assumptions and scope
The observations are iid from the one-parameter Cauchy–Cacoullos family with \(\lambda>0\). Divisibility by \(3\) is understood on \(\mathbb Z\), including \(0\).

The finite-sample statistic \(\widehat\beta_{3,n}\) can be nonpositive, in which case the inverse formula is not real. Assigning an arbitrary fixed value on that event gives a total estimator. Because the true transform value lies strictly between zero and one, the strong law implies that the inverse formula is used eventually almost surely. The consistency and asymptotic-normality statements therefore concern every such fixed extension.

The result compares only with the parity estimator explicitly analyzed in the motivating paper. It does not claim to dominate the MLE, an optimally tuned multi-frequency empirical-characteristic-function estimator, or every possible closed-form estimator.

## Proof
Papadatos gives the characteristic function
\[
\phi_\lambda(t)
=
\frac{\cosh(\lambda(t-\pi))}
{\cosh(\pi\lambda)},
\qquad 0\le t\le2\pi.
\]
Set
\[
u=\frac{\pi\lambda}{3},
\qquad
c=\cosh u.
\]
At \(t=2\pi/3\),
\[
\beta_3
:=
\phi_\lambda(2\pi/3)
=
\frac{\cosh u}{\cosh 3u}.
\]
Using
\[
\cosh 3u=c(4c^2-3),
\]
we obtain
\[
\beta_3=\frac1{4c^2-3}.
\]
For integer \(X\),
\[
\cos(2\pi X/3)
=
\begin{cases}
1,&3\mid X,\\
-1/2,&3\nmid X.
\end{cases}
\]
Therefore, with \(q_\lambda=\Pr_\lambda\{3\mid X\}\),
\[
\beta_3
=
\frac{3q_\lambda-1}{2}.
\]
This proves that \(\widehat\beta_{3,n}\) is the empirical mean of \(\cos(2\pi X/3)\) and yields the inverse
\[
c
=
\frac12\sqrt{3+\beta_3^{-1}},
\qquad
\lambda
=
\frac3\pi\operatorname{arcosh}c.
\]
Since \(0<\beta_3<1\), the strong law proves eventual validity of the inverse and strong consistency.

For the central limit theorem, write
\[
C=\cos(2\pi X/3).
\]
Because
\[
C^2=\frac{1+\cos(4\pi X/3)}2
\]
and periodicity plus symmetry give
\[
\phi_\lambda(4\pi/3)=\phi_\lambda(2\pi/3)=\beta_3,
\]
we have
\[
\operatorname{Var}(C)
=
\frac{1+\beta_3}{2}-\beta_3^2.
\]
Differentiating
\[
\beta_3=(4c^2-3)^{-1}
\]
gives
\[
\beta_3'(\lambda)
=
-\frac{8\pi}{3}
\frac{c\sqrt{c^2-1}}{(4c^2-3)^2}.
\]
The central limit theorem and inverse delta method therefore yield
\[
V_3(\lambda)
=
\frac{\operatorname{Var}(C)}
{(\beta_3'(\lambda))^2}
=
\frac{9}{32\pi^2}
\frac{(4c^2-3)^2(4c^2-1)}{c^2}.
\]

The triple-angle identity also gives
\[
\cosh(\pi\lambda)=c(4c^2-3),
\]
so the source's parity variance satisfies
\[
V_2(\lambda)
=
\frac{c^2(4c^2-3)^2}{\pi^2}.
\]
Hence
\[
R(c)
:=
\frac{V_3(\lambda)}{V_2(\lambda)}
=
\frac{9(4c^2-1)}{32c^4}.
\]
With \(z=c^2>1\),
\[
R(z)=\frac{9(4z-1)}{32z^2},
\qquad
R'(z)=\frac{9(2-4z)}{32z^3}<0.
\]
Thus \(R<27/32\), since its boundary value at \(z=1\) is \(27/32\), and \(R\to0\) as \(z\to\infty\).

Finally, expanding the source's exact Fisher-information expression at zero gives
\[
I(\lambda)\to\frac{4\pi^2}{3}.
\]
Together with
\[
V_3(\lambda)\to\frac{27}{32\pi^2},
\qquad
V_2(\lambda)\to\frac1{\pi^2},
\]
this yields limiting MLE-relative efficiencies \(8/9\) and \(3/4\), respectively.

## Verification
The standalone script `verify.py` evaluates the transform in two algebraically independent forms, checks the delta-method variance against the Bernoulli-modulo-three representation, checks the exact variance ratio on a deterministic parameter grid, and verifies the small-scale efficiency limits numerically from the published Fisher-information formula.

A successful run ends with:
`VERIFY_OK max_identity_error<1e-12 ratio_sup<0.84375 efficiency_limits=(0.8888888889,0.75)`.

These finite calculations are regression checks only. Strong consistency, asymptotic normality, uniform variance domination, and the endpoint limits are proved analytically above.

## Relationship to prior work
Papadatos introduced the Cauchy–Cacoullos family and obtained its characteristic function in closed form. The same paper studies estimation of the scale parameter, proves asymptotic efficiency of the numerical maximum-likelihood estimator, and gives a closed-form parity estimator from the characteristic function at \(t=\pi\). It explicitly describes that parity estimator as substantially less efficient than the MLE and identifies closed-form, highly efficient characteristic-function estimators as a natural direction beyond the paper's scope.

Koutrouvelis developed empirical-characteristic-function scale estimation for the continuous Cauchy family. That methodology motivates using other frequencies, but it does not imply the discrete modulo-three inversion, its binomial sufficient reduction for this one transform, or the exact uniform variance ratio against the published parity estimator.

Targeted searches using the Cauchy–Cacoullos and discrete-Cauchy names together with modulo-three, divisibility-by-three, \(2\pi/3\), empirical characteristic function, and the exact variance ratio found no covering statement. A later public software package for the Cauchy–Cacoullos law documents maximum-likelihood estimation rather than this closed-form estimator.

## Limitations
The new estimator uses only one residue-class statistic and is not claimed to be asymptotically efficient for all \(\lambda\). Its relative efficiency against the MLE approaches \(8/9\) only at the small-scale boundary; the theorem's global efficiency statement is instead the strict uniform improvement over the source's parity estimator.

The finite-sample extension outside \(0<\widehat\beta_{3,n}\le1\) is arbitrary and has no optimality claim. Search noncoverage is evidence of originality, not proof that no equivalent calculation exists under older empirical-transform or residue-class terminology.

## References
1. N. Papadatos, *The Characteristic Function of the Discrete Cauchy Distribution (In Memory of T. Cacoullos)*, arXiv:1809.09443v1, first public 25 September 2018; revised version arXiv:1809.09443v2; *Journal of Statistical Theory and Practice* 16 (2022), article 47, DOI 10.1007/s42519-022-00268-6.
2. I. A. Koutrouvelis, *Estimation of Location and Scale in Cauchy Distributions Using the Empirical Characteristic Function*, *Biometrika* 69 (1982), 205–213, DOI 10.1093/biomet/69.1.205.
3. M. Tsagris, *CCd: The Cauchy-Cacoullos (Discrete Cauchy) Distribution*, CRAN package version 1.1, published 7 December 2024.
