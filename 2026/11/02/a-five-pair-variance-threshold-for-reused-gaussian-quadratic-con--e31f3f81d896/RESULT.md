# A five-pair variance threshold for reused Gaussian-quadratic control variates

## Finding

A nested multifidelity mean estimator can be unbiased while having infinite variance even when both fidelities have moments of every order. The following theorem determines its precise finite-pilot boundary and, on the finite-variance side, its exact variance and the exact condition under which the fitted correction improves on uncorrected high-fidelity Monte Carlo.

For integers \(m>n\ge2\), put \(q=m-n\). Let \(Z_1,\ldots,Z_m\) be independent \(N(0,1)\) variables. Let \(\varepsilon_1,\ldots,\varepsilon_n\) be independent \(N(0,\sigma^2)\) variables independent of all \(Z_i\), with \(\sigma>0\). The real parameters \(\mu,\theta,\beta\) are fixed. Define low-fidelity and high-fidelity observations by

\[
 L_i=\theta+Z_i^2-1\quad(1\le i\le m),\qquad
 H_i=\mu+\beta(Z_i^2-1)+\varepsilon_i\quad(1\le i\le n).
\]

Thus \(\mathbb E L_i=\theta\), which need not be known to the estimator, and \(\mathbb E H_i=\mu\). Observe the paired variables \((L_i,H_i)\) for \(i\le n\) and only \(L_i\) for \(n<i\le m\). Define

\[
 S_n=\sum_{i=1}^{n}(L_i-\overline L_n)^2,\qquad
 \widehat\beta=\frac{\sum_{i=1}^n(L_i-\overline L_n)(H_i-\overline H_n)}{S_n},\qquad
 \widehat\mu=\overline H_n-\widehat\beta(\overline L_n-\overline L_m).
\]

Here \(S_n>0\) almost surely, and the bars denote means over the indicated initial observations. Write

\[
 W\sim\operatorname{Dirichlet}(\tfrac12,\ldots,\tfrac12),\quad
 V_n=\sum_{i=1}^{n}(W_i-1/n)^2,\quad
 K_n=\mathbb E[V_n^{-1}]\quad(n\ge4).
\]

The exact conclusions are:

1. For **every real** \(r>0\), the fitted slope has the sharp moment boundary
   \[
     \mathbb E|\widehat\beta-\beta|^r<\infty
     \quad\Longleftrightarrow\quad r<n/2.
   \]
   For each integer \(n\ge3\), its tail has a strictly positive exact leading constant:
   \[
     \lim_{t\to\infty}t^{n/2}\Pr\{|\widehat\beta-\beta|>t\}
     =\frac{\sigma^{n/2}\,\mathbb E|G|^{n/2}\,\mathbb E[V_n^{-n/4}]}
      {2^{n/2}\Gamma(n/2+1)},\qquad G\sim N(0,1).
   \]
2. For \(n=2\), \(\widehat\mu\) is not absolutely integrable. For \(n\ge3\), it is integrable and **exactly unbiased**, \(\mathbb E\widehat\mu=\mu\). Its variance is finite **if and only if** \(n\ge5\); in particular, three and four paired observations give an unbiased estimator of infinite variance regardless of \(m>n\).
3. For every \(n\ge5\), \(K_n\) is finite and the exact, unconditional mean-squared error is
   \[
   \boxed{\operatorname{Var}(\widehat\mu)
    =\frac{\sigma^2}{n}+\frac{2\beta^2}{m}
     +\frac{2\sigma^2 q(n^2+nq+4q)}{m^2n^2(n-2)(n-4)}\,K_n.}
   \]
   Relative to \(\operatorname{Var}(\overline H_n)=(2\beta^2+\sigma^2)/n\), the fitted multifidelity correction has **strictly lower variance if and only if**
   \[
    \boxed{\frac{\beta^2}{\sigma^2}>
      \frac{(n^2+nq+4q)K_n}{mn(n-2)(n-4)}.}
   \]
   Equality means equal variances; reversal gives strictly worse variance. Even in the ideal additive-noise regression family, a positive population-level control correlation does not alone guarantee finite-sample improvement.

## Assumptions and scope

All limits and expectations refer to the explicitly stated independent Gaussian data-generating law, with fixed positive integers \(m>n\ge2\). The low-fidelity response is a shifted centered Gaussian square, a basic nonnegative-quadratic response after shifting; its mean \(\theta\) is an unknown offset. The high-fidelity conditional regression is exactly linear in that response with independent Gaussian noise, and the regression slope is fitted with an intercept on the **same** \(n\) paired observations used to form the corrected mean. The additional \(q\) low-fidelity observations are independent of those pairs. The estimator uses exact arithmetic and no clipping, regularization or independent pilot split. No assumption of jointly Gaussian low- and high-fidelity outputs is made or true here when \(\beta\ne0\).

The constant \(K_n\) is specified by an exact probability expectation. Equivalently, with \(w_n=1-\sum_{i<n}w_i\) and integration over the standard simplex,

\[
 K_n=\frac{\Gamma(n/2)}{\Gamma(1/2)^n}
 \int_{\substack{w_1,\ldots,w_{n-1}>0\\\sum_{i<n}w_i<1}}
 \frac{\prod_{i=1}^n w_i^{-1/2}}
      {\sum_{i=1}^n(w_i-1/n)^2}\,dw_1\cdots dw_{n-1}.
\]

This is a reproducible exact constant, not an assertion of an elementary closed form.

## Proof

**1. Gaussian regression and a chi-square–Dirichlet factorization.** Put \(Y_i=Z_i^2\), \(T=\sum_{i=1}^nY_i\), and \(T'=\sum_{i=n+1}^mY_i\). Gamma normalization gives

\[
 T\sim\chi_n^2,\qquad T'\sim\chi_q^2,\qquad
 W_i=Y_i/T\ (i\le n),\qquad
 W\sim\operatorname{Dirichlet}(\tfrac12,\ldots,\tfrac12),
\]

with \(T,T',W\) mutually independent. Direct centering yields the **pathwise identities**

\[
 S_n=T^2V_n,\qquad
 \Delta:=\overline L_n-\overline L_m
 =\frac{q}{m}\left(\frac{T}{n}-\frac{T'}q\right).
\]

Condition on all low-fidelity observations. The centered regression noise is

\[
 \widehat\beta-\beta
 =\frac{\sum_{i\le n}(L_i-\overline L_n)\varepsilon_i}{S_n}
 =\frac{\sigma G}{T\sqrt{V_n}},
\]

where \(G\sim N(0,1)\) is independent of \(T,T',W\). Indeed the conditional distribution of the normalized linear form is standard Gaussian and does not depend on the conditioning data. Furthermore \(\overline\varepsilon_n\) and this normalized form are independent given those data, because their Gaussian coefficient vectors are orthogonal; their conditional joint law is constant.

**2. Sharp negative moments and tail constant.** For every \(a>0\), the chi-square density gives

\[
 \mathbb E[T^{-a}]<\infty\quad\Longleftrightarrow\quad a<n/2.
\]

On the \((n-1)\)-dimensional Dirichlet simplex, the only singularity of \(V_n^{-r/2}\) is the interior barycenter. The density is smooth and positive in a neighborhood of that point, and \(V_n\) is the squared Euclidean distance to it. Polar integration there gives

\[
 \mathbb E[V_n^{-r/2}]<\infty\quad\Longleftrightarrow\quad r<n-1.
\]

Outside such a neighborhood \(V_n\) is bounded away from zero and the Dirichlet density is integrable, including along the faces. Since \(n/2\le n-1\) for \(n\ge2\), independence and Gaussian moments prove the exact slope-moment threshold. For \(n\ge3\), the Dirichlet negative moment at \(r=n/2\) is finite. Finally,

\[
 \Pr(T\le x)\sim\frac{x^{n/2}}{2^{n/2}\Gamma(n/2+1)}\quad(x\downarrow0),
\]

and the elementary global upper bound by the same constant times \(x^{n/2}\), together with dominated convergence conditional on \(|G|/\sqrt{V_n}\), yields the stated exact regularly varying slope tail.

**3. Integrability and the sharp finite-variance cutoff.** Algebra gives

\[
 \widehat\mu-\mu
   =\beta(\overline L_m-\theta)+\overline\varepsilon_n
     -(\widehat\beta-\beta)\Delta.
\]

For \(n>2\), the bound \(|\Delta|/(T\sqrt{V_n})\le(q/m)(1/n+T'/(qT))V_n^{-1/2}\), the preceding negative-moment criteria and \(\mathbb E T'=q\) imply integrability. Conditional expectation over the Gaussian noise then gives \(\mathbb E[\widehat\mu\mid L_1,\ldots,L_m]=\mu+\beta(\overline L_m-\theta)\), whose expectation is \(\mu\).

For \(n=2\), choose a positive-probability event on which \(T'>1\), \(V_n\) is bounded below by a positive constant and \(T\) is sufficiently small. On this event \(|\Delta|\) is bounded below, and the conditional expected magnitude of the Gaussian slope-noise correction is proportional to \(|\Delta|/(T\sqrt{V_n})\). Since \(\mathbb E[T^{-1}]=\infty\) when \(n=2\), while \(\beta(\overline L_m-\theta)+\overline\varepsilon_n\) is integrable, the estimator itself is not absolutely integrable.

For \(n\ge3\), the conditional variance given all low-fidelity observations is exactly

\[
 \operatorname{Var}(\widehat\mu\mid L_1,\ldots,L_m)
 =\frac{\sigma^2}{n}+\frac{\sigma^2\Delta^2}{S_n}.
\]

The nonnegative second term has infinite expectation for \(n=3,4\): on the same positive-probability set \(T'>1\), \(V_n\) bounded below and \(T\) small, it is bounded below by a positive multiple of \(T^{-2}\), whose expectation diverges exactly when \(n\le4\). For \(n\ge5\), the independent negative moments \(\mathbb E[T^{-2}]\) and \(\mathbb E[V_n^{-1}]\) are finite, and thus so is the variance.

**4. Exact variance and exact improvement criterion.** For \(n\ge5\), the total-variance identity and \(\operatorname{Var}(\overline L_m)=2/m\) give

\[
 \operatorname{Var}(\widehat\mu)
  =\frac{\sigma^2}{n}+\frac{2\beta^2}{m}
   +\sigma^2\mathbb E\frac{\Delta^2}{S_n}.
\]

Using \(\mathbb ET'=q\), \(\mathbb E(T'^2)=q(q+2)\), \(\mathbb E(T^{-1})=1/(n-2)\), and \(\mathbb E(T^{-2})=1/((n-2)(n-4))\), independence yields

\[
 \begin{aligned}
 \mathbb E\frac{\Delta^2}{S_n}
 &=\frac{q^2K_n}{m^2}\left(\frac1{n^2}
   -\frac2{n(n-2)}
   +\frac{q+2}{q(n-2)(n-4)}\right)\\
 &=\frac{2q(n^2+nq+4q)K_n}{m^2n^2(n-2)(n-4)}.
 \end{aligned}
\]

This proves the exact variance. Comparing it with the uncorrected variance \((2\beta^2+\sigma^2)/n\), cancelling the positive factor \(2q/(nm)\), gives precisely the stated strict gain threshold and its equality/reversal cases. No finite enumeration is used to establish any all-\(n\) statement.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It checks 1,260 exact rational inverse-moment identities, 684 exact rational gain-threshold rearrangements, 800 pathwise coupling and Gamma–Dirichlet identities and four independent Monte Carlo/conditional-second-moment comparisons for \((n,m)=(8,17)\) and \((12,26)\), totaling 2,748 executed checks. It was run against the packaged source and reported `VERIFY_OK 2748`. The Monte Carlo comparisons use independent random streams for direct estimator error and for \(K_n\); the analytic proof above, not those finite tests, establishes the moment cutoffs and exact identities.

## Relationship to prior work

The nested regression correction is an instance of the classical two-phase regression estimator: Yang and Ding [3, Section 2.2] give the same regression-adjustment structure for a finite-population sampling design and study asymptotic properties. The statistical construction itself is therefore **not** claimed as new. The distinct assertion here is the exact finite-sample moment/variance transition for a quadratic-Gaussian auxiliary response under superpopulation sampling and same-sample slope fitting.

Rex and Qian [1, Section 3.3] derive population-covariance-optimal nested multifidelity coefficients and warn that pilot-estimated covariances may become ill conditioned, motivating regularization. Dai, Tchelepi and Tartakovsky [2, Sections 3.7 and 4.4] analyze multivariate multifidelity coefficients and discuss bias caused by pilot reuse *in general*. These statements neither give the negative-moment law of the shifted chi-square sample variance nor imply the present family's exact unbiasedness, \(n=5\) variance threshold, or gain criterion. Pham and Gorodetsky [4] previously address uncertain coefficients and minimum pilot sizes through ensemble approximate control variates, but the checked material did not identify this exact same-sample quadratic response calculation. The earlier two-phase and control-variate literature is credited rather than replaced. Sitter [6] studies variance estimation for the two-phase regression estimator; only its abstract could be checked, leaving the scope of any specialized finite-sample formulas unresolved.

The evidence examined did not establish an equivalent earlier result. General regression and Gamma–Dirichlet identities supply ingredients for this proof, so priority beyond the checked sources remains a limitation.

## Limitations

This is an exact benchmark for a specific independent additive-noise superpopulation family, fixed nested sample allocation and unregularized same-sample slope. It does not assert that pilot reuse is generically unbiased, that \(n\ge5\) is sufficient for every possible auxiliary distribution, that the finite-sample variance is minimized by this estimator among all nonlinear or regularized alternatives, or that the nominal optimal pilot size for a fixed cost has been solved. The one-dimensional Dirichlet integral \(K_n\) is exact but not simplified to elementary constants. All computations are finite supplementary checks; no independent mathematical audit has been performed.

## References

1. A. Rex and E. Qian, *Analytically Optimal Sample Allocations for Nested Multivariate Multifidelity Control Variate Estimators*, arXiv:2610.19371v1 (first public 2026-10-14). https://arxiv.org/abs/2610.19371
2. Z. Dai, H. A. Tchelepi and D. M. Tartakovsky, *Multifidelity Monte Carlo Estimator for High-Dimensional Quantities of Interest*, arXiv:2610.25016 (first public 2026-10-18). https://arxiv.org/abs/2610.25016
3. S. Yang and P. Ding, *Two-phase rejective sampling and its asymptotic properties*, arXiv:2403.01477 (first public 2024-03-03). https://arxiv.org/abs/2403.01477
4. T. Pham and A. A. Gorodetsky, *Ensemble Approximate Control Variate Estimators: Applications to MultiFidelity Importance Sampling*, arXiv:2101.02786 (first public 2021-01-07). https://arxiv.org/abs/2101.02786
5. M. Stanley et al., *Sample correlation adjustments for robust Multi-fidelity Monte Carlo under limited pilot sampling*, arXiv:2605.23016 (first public 2026-05-21). https://arxiv.org/abs/2605.23016
6. R. R. Sitter, *Variance Estimation for the Regression Estimator in Two-Phase Sampling*, Journal of the American Statistical Association 92 (1997), 780–787. https://doi.org/10.1080/01621459.1997.10474031
