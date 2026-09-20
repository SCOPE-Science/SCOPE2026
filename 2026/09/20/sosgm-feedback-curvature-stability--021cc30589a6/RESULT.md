# Population feedback targets and sharp curvature-stability thresholds in stochastic OSGM

## Statement

Consider the one-dimensional common-minimizer stochastic quadratic family
\[
 f_A(x)=\tfrac12 A x^2,\qquad A>0,
\]
and an independent evaluation batch with curvature \(B>0\).  For a scalar proposed stepsize \(p\ge 0\), the stochastic-gradient proposal is
\[
 x^+=(1-pA)x.
\]
The out-of-sample ratio and hypergradient feedbacks introduced for OSGM-SGD in Zhang--Gao--Ye--Udell (2026) reduce exactly to
\[
 R(p;A,B)=\frac BA(1-pA)^2,
 \qquad
 H(p;A,B)=B\left(-\frac pA+\frac{p^2}{2}\right).
\]
Assume the displayed moments are finite and \(A,B\) are independent.  Their unconstrained population minimizers are
\[
 \boxed{p_{\rm ratio}=\frac1{\mathbb E A}},\qquad
 \boxed{p_{\rm hyp}=\mathbb E[A^{-1}]}.
\]
By contrast, the fixed stepsize minimizing the actual one-step mean-square state error
\[
 Q(p):=\frac{\mathbb E[(x^+)^2]}{x^2}
      =1-2(\mathbb EA)p+\mathbb E[A^2]p^2
\]
is
\[
 \boxed{p_{\rm ms}=\frac{\mathbb EA}{\mathbb E[A^2]}}.
\]
Consequently
\[
 \boxed{p_{\rm ms}\le p_{\rm ratio}\le p_{\rm hyp}},
\]
with equality throughout only for deterministic curvature.  Thus independence of the evaluation batch removes same-batch overfitting in this model, but the two feedback objectives still target different deterministic stepsizes from the mean-square-optimal stochastic-gradient step.

If the scalar candidate set is an interval \(I\), the corresponding population feedback minimizers are simply the clipped values \(\Pi_I(p_{\rm ratio})\) and \(\Pi_I(p_{\rm hyp})\).  The results below concern the raw, unclipped proposals and therefore diagnose when clipping or the algorithm's null-step safeguard becomes essential.

## Exact mean-square consequences

Write
\[
 \mu=\mathbb EA,\qquad m_2=\mathbb E[A^2],\qquad h=\mathbb E[A^{-1}].
\]
A fixed raw proposal is mean-square contractive exactly when
\[
 0<p<\frac{2\mu}{m_2}.
\]
At the ratio target,
\[
 \boxed{Q(p_{\rm ratio})
 =\frac{m_2}{\mu^2}-1
 =\frac{\operatorname{Var}(A)}{\mu^2}}
\]
is exactly the squared coefficient of variation of the update-batch curvature.  Hence the ratio target is mean-square contractive iff \(\operatorname{CV}(A)<1\).

At the hypergradient target,
\[
 Q(p_{\rm hyp})=1-2\mu h+m_2h^2,
\]
so raw mean-square contraction is equivalent to
\[
 \boxed{\frac{\mathbb E[A^{-1}]\,\mathbb E[A^2]}{\mathbb EA}<2.}
\]
The hypergradient target is therefore more sensitive to small-curvature batches: the inverse moment that drives its feedback target can push the proposed step beyond the mean-square stability interval even though the evaluation batch is independent.

## Sharp support-only phase diagrams

Suppose only that
\[
 0<m\le A\le L,
 \qquad \kappa=L/m.
\]
Scale by \(m\), so the support is \([1,\kappa]\).

### Ratio feedback

Bhatia--Davis gives
\[
 \operatorname{Var}(A)\le (\kappa-\mu)(\mu-1).
\]
Maximizing the resulting coefficient-of-variation bound over \(1\le\mu\le\kappa\) yields
\[
 \sup_{\operatorname{supp}(A)\subset[1,\kappa]}
 Q(p_{\rm ratio})
 =\boxed{\frac{(\kappa-1)^2}{4\kappa}}.
\]
Equality is attained by the endpoint distribution supported on \(\{1,\kappa\}\) with
\[
 \mathbb P(A=\kappa)=\frac1{\kappa+1}.
\]
Therefore the raw ratio target is mean-square contractive for **every** curvature distribution in \([m,L]\) exactly when
\[
 \boxed{\kappa<3+2\sqrt2=5.828427124746\ldots}. 
\]
At equality there is a noncontractive endpoint law; above it there is an endpoint law for which the raw ratio proposal is mean-square unstable.

### Hypergradient feedback

For \(A\in[1,\kappa]\), the pointwise chord bounds
\[
 A^2\le (\kappa+1)A-\kappa,
 \qquad
 A^{-1}\le \frac{\kappa+1-A}{\kappa}
\]
give, for fixed \(\mu=\mathbb EA\),
\[
 \frac{\mathbb E[A^{-1}]\mathbb E[A^2]}{\mu}
 \le
 \frac{(\kappa+1-\mu)((\kappa+1)\mu-\kappa)}{\kappa\mu}.
\]
Both bounds are simultaneously attained by an endpoint distribution with the prescribed mean.  Maximizing over \(\mu\in[1,\kappa]\) gives \(\mu=\sqrt\kappa\), hence the sharp identity
\[
 \boxed{
 \sup_{\operatorname{supp}(A)\subset[1,\kappa]}
 \frac{\mathbb E[A^{-1}]\mathbb E[A^2]}{\mathbb EA}
 =\frac{(\kappa-\sqrt\kappa+1)^2}{\kappa}.}
\]
The extremizer is the endpoint law with
\[
 \mathbb P(A=\kappa)=\frac1{\sqrt\kappa+1}.
\]
It follows that the raw hypergradient target is mean-square contractive for every curvature law in \([m,L]\) exactly when
\[
 \boxed{
 \kappa<\kappa_{\rm hyp}:=
 \left(\frac{1+\sqrt2+\sqrt{2\sqrt2-1}}{2}\right)^2
 =3.546455444685\ldots.}
\]
Thus the support-only robust region of the raw hypergradient target is strictly smaller than that of the ratio target.

## A concrete two-curvature example and the role of the null step

For the equal-probability law \(A\in\{m,L\}\), let \(\kappa=L/m\).  Then
\[
 p_{\rm ms}=\frac{m+L}{m^2+L^2},\qquad
 p_{\rm ratio}=\frac{2}{m+L},\qquad
 p_{\rm hyp}=\frac{m+L}{2mL}.
\]
The raw mean-square factors are
\[
 Q(p_{\rm ms})=\frac{(\kappa-1)^2}{2(\kappa^2+1)},
\]
\[
 Q(p_{\rm ratio})=\left(\frac{\kappa-1}{\kappa+1}\right)^2,
\]
and
\[
 \boxed{
 Q(p_{\rm hyp})=
 \frac{(\kappa-1)^2(\kappa^2+1)}{8\kappa^2}.}
\]
The raw hypergradient target becomes unstable at
\[
 \kappa>2+\sqrt3=3.732050807569\ldots.
\]
For example, with \(m=1,L=4\),
\[
 p_{\rm ms}=5/17,\qquad p_{\rm ratio}=2/5,\qquad p_{\rm hyp}=5/8,
\]
and
\[
 Q(p_{\rm ms})=0.2647058824,\quad
 Q(p_{\rm ratio})=0.36,\quad
 Q(p_{\rm hyp})=1.1953125.
\]

The hypergradient branch of OSGM-SGD in the source paper includes a null step that compares the proposal with the current point on the independent evaluation batch.  In this positive quadratic family the factor \(B\) cancels from that comparison, so a proposal is accepted exactly when
\[
 |1-pA|\le1,
 \quad\text{i.e.}\quad 0\le pA\le2.
\]
At \(p=p_{\rm hyp}\) for the equal two-point law, the high-curvature proposal is rejected exactly when \(\kappa>3\).  For \(\kappa>3\), the resulting squared-state multiplier is
\[
 \boxed{Q_{\rm hyp,null}
 =\frac12\left[1+\left(\frac{\kappa-1}{2\kappa}\right)^2\right]}
 \longrightarrow \frac58.
\]
At \(\kappa=4\), this is \(0.5703125\), in contrast with the unstable raw value \(1.1953125\).  Thus this example does **not** show divergence of the published hypergradient algorithm; instead it shows that its null step can be mathematically essential rather than cosmetic when the feedback target is driven by heterogeneous curvature.

## Why large batches reconcile the targets

Let \(A_b\) be the average curvature of \(b\) iid samples with mean \(\mu>0\) and variance \(\sigma^2\).  Then
\[
 p_{{\rm ratio},b}=\frac1\mu,
 \qquad
 p_{{\rm ms},b}=\frac{\mu}{\mu^2+\sigma^2/b},
 \qquad
 p_{{\rm hyp},b}=\mathbb E[A_b^{-1}].
\]
Hence
\[
 p_{{\rm ms},b}\le \frac1\mu\le p_{{\rm hyp},b}.
\]
If the sample curvatures are bounded away from zero and have bounded moments sufficient for the Taylor expansion, then
\[
 \boxed{
 p_{{\rm ms},b}
 =\frac1\mu-\frac{\sigma^2}{\mu^3b}+O(b^{-2}),
 \qquad
 p_{{\rm hyp},b}
 =\frac1\mu+\frac{\sigma^2}{\mu^3b}+O(b^{-2}).}
\]
The ratio target stays exactly at the center \(1/\mu\), while the mean-square optimum and hypergradient target approach it from opposite sides at equal first-order magnitude.  This gives an elementary mechanism, within an interpolation model, for why increasing batch size makes the stochastic feedback geometry resemble its deterministic counterpart.

There is also a simple finite-batch obstruction.  For iid per-sample curvatures taking \(1\) and \(\kappa\) with equal probability,
\[
 p_{{\rm hyp},b}
 =2^{-b}\sum_{j=0}^b {b\choose j}
 \frac1{1+(\kappa-1)j/b}.
\]
Since the all-low-curvature batch contributes \(2^{-b}\), one has \(p_{{\rm hyp},b}\ge2^{-b}\).  Raw mean-square stability would require
\[
 p_{{\rm hyp},b}
 <\frac{4(1+\kappa)}{(1+\kappa)^2+(\kappa-1)^2/b}
 \le\frac4{1+\kappa}.
\]
Therefore a necessary condition is
\[
 \boxed{b>\log_2\frac{1+\kappa}{4}.}
\]
In particular, no fixed batch size makes the unconstrained hypergradient population target raw-mean-square stable uniformly over arbitrarily large curvature ratios in this family.

## Relation to prior work and originality boundary

Zhang, Gao, Ye and Udell introduce the stochastic OSGM framework, identify failure of naive same-batch ratio/hypergradient feedback, and replace it for OSGM-SGD by independent out-of-sample feedback together with large-batch convergence guarantees.  Their hypergradient version also includes the null step analyzed above.  The present result starts from their exact feedback definitions and specializes them to a scalar random-curvature common-minimizer family.

Hypergradient learning-rate adaptation itself is much older: Almeida et al. (1999), Baydin et al. (2018), and related stochastic meta-descent methods all predate SOSGM.  Chu et al. (2025) give a rigorous online-learning analysis of hypergradient descent in the deterministic setting and explain instability phenomena there.  Classical stochastic-approximation and adaptive-filter analyses also contain extensive mean-square stepsize theory for random linear recursions.  None of those general ingredients is claimed as new here.

The narrow originality claim is the **source-specific population-target separation**
\[
 \frac{\mathbb EA}{\mathbb E[A^2]},\quad
 \frac1{\mathbb EA},\quad
 \mathbb E[A^{-1}],
\]
for mean-square SGD, the 2026 out-of-sample ratio feedback, and the 2026 out-of-sample hypergradient feedback respectively, together with the sharp support-only robust stability thresholds \(3+2\sqrt2\) and \(3.546455\ldots\), the explicit null-step rejection phase on the two-curvature family, and the finite-batch logarithmic necessary condition.  Searches by these formulas, by synonymous random-curvature/mean-square terminology, and by the source paper did not locate this combination in the checked literature or existing SCOPE records.  Because older adaptive-filter and stochastic learning-rate literature is large, historical coverage under different terminology remains a residual originality risk.

## Limitations

This is an exact analysis of a one-dimensional positive random-curvature quadratic interpolation model.  It does not establish divergence or convergence of full SOSGM on general nonlinear or multidimensional objectives.  The sharp condition-number thresholds concern **unconstrained raw population minimizers** of the two feedback losses.  The source algorithm constrains the candidate stepsize set; clipping can prevent the raw target from being used.  Its hypergradient branch also includes a null step, which the two-curvature calculation shows can restore contraction even when the raw target is unstable.  The evaluation curvature cancels from the population minimizers only because the model is scalar, quadratic, has a common minimizer, and uses an independent positive evaluation batch.  Finally, one-step mean-square optimality is not the same objective as long-horizon optimization speed.

## Reproducibility

`artifacts/verify_feedback_thresholds.py` uses only the Python standard library.  It evaluates the closed-form thresholds, checks the endpoint extremizers, tests the ordering and support bounds on deterministic pseudorandom discrete curvature laws, and computes finite-batch examples.  Its published output is in `artifacts/verification_output.txt`.

## References

1. W. Zhang, W. Gao, Y. Ye, M. Udell, *Stochastic Gradient Methods with Online Scaling*, arXiv:2609.11751v2, 2026. https://arxiv.org/abs/2609.11751
2. Y.-C. Chu, W. Gao, Y. Ye, M. Udell, *Provable and Practical Online Learning Rate Adaptation with Hypergradient Descent*, Proceedings of ICML 2025, PMLR 267:10768--10800. https://proceedings.mlr.press/v267/chu25a.html
3. A. G. Baydin, R. Cornish, D. Martinez Rubio, M. Schmidt, F. Wood, *Online Learning Rate Adaptation with Hypergradient Descent*, ICLR 2018. https://arxiv.org/abs/1703.04782
4. L. B. Almeida, T. Langlois, J. D. Amaral, A. Plakhov, *Parameter Adaptation in Stochastic Optimization*, in *On-Line Learning in Neural Networks*, Cambridge University Press, 1999. https://doi.org/10.1017/CBO9780511569920.007
