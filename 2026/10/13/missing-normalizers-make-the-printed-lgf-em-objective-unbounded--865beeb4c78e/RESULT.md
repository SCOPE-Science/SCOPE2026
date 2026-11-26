# Missing normalizers make the printed logarithmic–gamma frailty EM objective unbounded in frailty shape

## Finding

For the logarithmic–gamma frailty (LGF) model of Rahmouni [1], let \(\theta,\lambda>0\) and \(0<\eta<1\). For one observation and its latent count and frailty, the three factors in Eq. (4.2) give the joint contribution
\[
\frac{\eta^n}{-n\log(1-\eta)}\,
\frac{\lambda^\lambda}{\Gamma(\lambda)} z^{\lambda-1}e^{-\lambda z}\,
n\theta z e^{-n\theta zy},\qquad n\ge1,\quad z>0,\quad y\ge0.
\]
The two factors of \(n\) cancel, but the logarithmic-series and gamma normalizers do not. In particular the complete-data log contribution is
\[
n\log\eta-\log[-\log(1-\eta)]+\log\theta+\lambda\log\lambda-\log\Gamma(\lambda)
+\lambda\log z-\lambda z-n\theta zy.
\]
Neither \(-\log[-\log(1-\eta)]\) nor \(-\log\Gamma(\lambda)\) can be absorbed in a constant in a joint M-step. Equation (4.3) omits both factors; Eqs. (4.4) and (4.5) omit their logs. Equation (4.5) also replaces \(\lambda\log\lambda\) by \((\lambda+1)\log\lambda\).

For a nonempty sample with a frozen E-step, use
\[
A=\sum_i E(N_i\mid y_i),\quad B=\sum_i E(\log Z_i\mid y_i),\quad
C=\sum_i E(Z_i\mid y_i),\quad D=\sum_i y_i E(N_iZ_i\mid y_i),
\]
where all expectations are at the old parameters. The corrected auxiliary function, up to a constant in the new parameters, is
\[
Q=A\log\eta-m\log[-\log(1-\eta)]+m\log\theta
+m\{\lambda\log\lambda-\log\Gamma(\lambda)\}+\lambda(B-C)-\theta D.
\]
The literal Eq. (4.5), in contrast, gives
\[
Q_{4.5}=A\log\eta+m\log\theta+m(\lambda+1)\log\lambda+\lambda(B-C)-\theta D.
\]
For every such E-step, both the literal \(Q_{4.5}\) and the expected version of Eq. (4.4) diverge to \(+\infty\) as \(\lambda\to\infty\) with \(\eta,\theta\) fixed. Thus the printed objective has no finite joint M-step maximizer on the unbounded shape domain. For a fixed positive lower shape bound, a **sufficiently large** upper shape bound is selected by a global maximizer on the corresponding closed interval. A given finite box need not select its upper endpoint.

The corrected interior scores are
\[
\partial_\lambda Q=m\{\log\lambda+1-\psi(\lambda)\}+B-C,
\qquad
\partial_\eta Q=\frac{A}{\eta}-\frac{m}{(1-\eta)[-\log(1-\eta)]}.
\]
Here \(\psi\) is the digamma function. Equation (4.9) includes the missing logarithmic normalizer's derivative and therefore is incompatible with the literal Eq. (4.5), whose interior \(\eta\)-score is just \(A/\eta\). The corrected shape objective tends to \(-\infty\) at both ends of \((0,\infty)\) and has a unique finite shape maximizer for each such E-step.

## Proof

Multiplication of the logarithmic count PMF, the gamma density of shape and rate \(\lambda\), and the conditional exponential density of rate \(n\theta z\) gives the displayed joint density. Conditioning and integrating at the old parameters gives the auxiliary function. In particular, at interior old parameters \((\theta_0,\lambda_0,\eta_0)\), the conditional frailty given \(N=n,y\) has gamma shape \(\lambda_0+1\) and rate \(\lambda_0+n\theta_0 y\); the conditional count weights are proportional to \(\eta_0^n(\lambda_0+n\theta_0 y)^{-\lambda_0-1}\). Thus the conditional frailties are nondegenerate and the moments used here are finite, by geometric decay of the count weights.

The positive \(m\lambda\log\lambda\) term in either printed variant dominates the linear terms. For Eq. (4.5) specifically the shape score is
\[
m(\log\lambda+1+1/\lambda)+B-C,
\]
which is eventually strictly positive. For a fixed positive lower endpoint, the objective is bounded on any compact initial segment and eventually exceeds that segment's maximum. Hence a sufficiently large upper endpoint is optimal. To see why no statement for arbitrary boxes follows, freeze \((\theta_0,\lambda_0,\eta_0)=(1,1,1/2)\) and use the single observation \(y=e^4\). Conditional on any count \(n\), the mean of \(\log Z\) is \(\psi(2)-\log(1+n e^4)<-3\), since \(\psi(2)<1\). Thus \(B<-3\) and \(C>0\). On the shape box \([1,2]\), the displayed printed score is negative throughout, so the lower endpoint is optimal instead.

At zero, \(-\log\Gamma(\lambda)\sim\log\lambda\) yields left-end decay of the corrected shape objective. At infinity, Stirling's formula gives
\[
\lambda\log\lambda-\log\Gamma(\lambda)=\lambda+\tfrac12\log\lambda+O(1).
\]
The net linear coefficient is \(m+B-C<0\): it is a sum of the conditional expectations of \(1+\log Z_i-Z_i\), which is nonpositive with equality only at \(Z_i=1\), and the conditional frailties are nondegenerate. This proves right-end decay and attainment of the maximum. For strict concavity, the trigamma series \(\psi'(\lambda)=\sum_{r\ge0}(\lambda+r)^{-2}\) strictly exceeds \(\int_0^\infty(\lambda+t)^{-2}\,dt=1/\lambda\). The second derivative of the corrected shape objective is therefore negative.

## Scope and verification

The formulas use the interior logarithmic-series domain; the paper also allows the degenerate \(\eta=0\) limit. The divergence already holds at any fixed interior \(\eta\). The diagnosis concerns the printed joint three-parameter EM formulation, not the observed likelihood in Eq. (4.1) or any implementation. Section 5 and Table 1 state that the simulation used a corrected complete-data log-likelihood and a fixed frailty shape. The application in Section 6 maximizes the observed likelihood directly, not by EM.

For the sample \((0.18,0.42,0.95,1.70,3.20)\) with frozen parameters \((1.1,2.3,0.45)\), the corrected shape maximizer is approximately 2.49636. For this example the printed shape score is positive throughout the parameter domain: its minimum per observation is \(2+(B-C)/m\approx0.78654\). This explains the numerical upper-endpoint outcomes on the four example boxes with upper endpoints 5, 10, 30 and 100. The accompanying numerical check compares the analytic scores to finite differences for this example. The universal claims and the exception for arbitrary finite boxes are analytic.

## Relationship to prior work

The normalizations are those of the model defined in [1, Section 2]; Eq. (4.2) already specifies the correct factorization. Its Eq. (4.9) and Section 5 partly anticipate a correction, but neither gives a corrected joint shape M-step or diagnoses the literal objective's divergence. The earlier related frailty model [2, Section 4.2] has an analogous omission in its complete-data log-likelihood and a subsequent shape score that includes the digamma term. It does not address the combination of errors in Eqs. (4.3)–(4.5) of [1]. No claim is made about unpublished implementation details or that the model's reported weak identifiability is attributable to this error.

## References

1. M. Rahmouni, “A logarithmic–gamma frailty model for first-failure times with heavy-tailed risk,” *AIMS Mathematics* 11 (2026), 8945–8965. DOI: 10.3934/math.2026369.
2. M. Rahmouni, “The doubly generalized exponential-geometric frailty distribution,” *AIMS Mathematics* 10 (2025), 30384–30428. DOI: 10.3934/math.20251334.
