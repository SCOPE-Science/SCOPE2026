# Exact Jeffreys prior for the unit Shanker model
## Finding
For the unit Shanker distribution with parameter \(\alpha>0\), the exact per-observation Fisher information is
\[
I(\alpha)=
\frac{2(3\alpha^2+1)}
{\alpha^2(\alpha^2+1)^2}
+
\frac{\alpha^2}{\alpha^2+1}
e^{\alpha^2}E_1(\alpha^2),
\]
where
\[
E_1(z)=\int_z^\infty \frac{e^{-u}}{u}\,du.
\]
Therefore the Jeffreys-rule prior is
\[
\pi_J(\alpha)\propto\sqrt{I(\alpha)}.
\]

This prior is not proportional to \(1/\alpha\). In fact,
\[
\lim_{\alpha\downarrow0}\alpha\sqrt{I(\alpha)}=\sqrt2,
\qquad
\lim_{\alpha\to\infty}\alpha\sqrt{I(\alpha)}=1.
\]
Because the proportionality ratio has two different endpoint limits, no constant can make \(\sqrt{I(\alpha)}\) equal to \(1/\alpha\) on the parameter space.

Section 6 of Mohammad et al. (2026) uses
\[
\pi(\alpha)\propto\alpha^{-1}
\]
and calls it Jeffreys' prior, explaining it as the limiting gamma kernel obtained when both gamma hyperparameters tend to zero. That limiting argument does produce the improper log-uniform prior, but Jeffreys' rule is instead determined by the Fisher information of the statistical model.

The distinction is not a posterior-propriety failure. For every sample size \(n\ge1\) and every sample \(0<x_i<1\), the posterior under \(\pi(\alpha)\propto\alpha^{-1}\) is proper. Thus the published calculations using that prior remain mathematically interpretable as log-uniform-prior analyses; they are not Jeffreys-rule analyses unless they are recomputed with \(\pi_J\).

## Assumptions and scope
The unit Shanker model is the one-parameter submodel defined in Mohammad et al. by
\[
f_X(x;\alpha)=
\frac{\alpha^2[\alpha-(\alpha-1)x]}
{(\alpha^2+1)(1-x)^3}
\exp\!\left[-\frac{\alpha x}{1-x}\right],
\qquad 0<x<1,\quad\alpha>0.
\]
It is obtained from the positive-support Shanker distribution by the transformation
\[
X=\frac{T}{1+T},
\qquad
T=\frac{X}{1-X}.
\]

The transformation does not depend on \(\alpha\). Consequently its Jacobian contributes no \(\alpha\)-derivative to the log likelihood, and the Fisher information for \(\alpha\) is the same in the \(T\)- and \(X\)-parameterizations of the observation.

“Jeffreys prior” here means Jeffreys' rule for a scalar regular model:
\[
\pi_J(\alpha)\propto\sqrt{I(\alpha)}.
\]
The finding does not claim that every use of the term “non-informative prior” must follow Jeffreys' rule.

## Proof
The parent Shanker density is
\[
f_T(t;\alpha)=
\frac{\alpha^2}{\alpha^2+1}
(\alpha+t)e^{-\alpha t},
\qquad t>0.
\]
For one observation \(t\),
\[
\ell(\alpha;t)
=
2\log\alpha-\log(\alpha^2+1)
+\log(\alpha+t)-\alpha t.
\]
Differentiating twice gives
\[
\frac{\partial^2\ell}{\partial\alpha^2}
=
-\frac{2}{\alpha^2}
-\frac{2(1-\alpha^2)}{(\alpha^2+1)^2}
-\frac{1}{(\alpha+t)^2}.
\]
Hence
\[
I(\alpha)
=
-\mathbb E_\alpha\!\left[
\frac{\partial^2\ell}{\partial\alpha^2}
\right]
=
\frac{2}{\alpha^2}
+\frac{2(1-\alpha^2)}{(\alpha^2+1)^2}
+
\mathbb E_\alpha[(\alpha+T)^{-2}].
\]

The remaining expectation is
\[
\begin{aligned}
\mathbb E_\alpha[(\alpha+T)^{-2}]
&=
\frac{\alpha^2}{\alpha^2+1}
\int_0^\infty
\frac{e^{-\alpha t}}{\alpha+t}\,dt\\
&=
\frac{\alpha^2}{\alpha^2+1}
e^{\alpha^2}E_1(\alpha^2).
\end{aligned}
\]
Combining the elementary terms yields
\[
\frac{2}{\alpha^2}
+\frac{2(1-\alpha^2)}{(\alpha^2+1)^2}
=
\frac{2(3\alpha^2+1)}
{\alpha^2(\alpha^2+1)^2},
\]
which proves the displayed Fisher-information formula.

For \(\alpha\downarrow0\), the exponential-integral term is \(o(\alpha^{-2})\), so
\[
I(\alpha)\sim\frac{2}{\alpha^2}.
\]
For \(\alpha\to\infty\), the standard expansion
\[
e^zE_1(z)=\frac1z+O(z^{-2})
\]
gives
\[
I(\alpha)\sim\frac{1}{\alpha^2}.
\]
Therefore
\[
\alpha\sqrt{I(\alpha)}
\to\sqrt2
\quad\text{and}\quad
\alpha\sqrt{I(\alpha)}
\to1
\]
at the two endpoints, proving that the Jeffreys-rule prior is not proportional to \(1/\alpha\).

For completeness, consider the prior actually used in the source,
\[
\pi_L(\alpha)\propto\alpha^{-1}.
\]
For observations \(0<x_i<1\), put
\[
t_i=\frac{x_i}{1-x_i}>0.
\]
Ignoring factors independent of \(\alpha\), its posterior kernel is
\[
\pi_L(\alpha\mid x)
\propto
\frac{\alpha^{2n-1}}
{(\alpha^2+1)^n}
\prod_{i=1}^n(\alpha+t_i)
\exp\!\left[-\alpha\sum_{i=1}^n t_i\right].
\]
As \(\alpha\downarrow0\), this is \(O(\alpha^{2n-1})\), which is integrable for \(n\ge1\). As \(\alpha\to\infty\), it is
\[
O\!\left(
\alpha^{n-1}e^{-\alpha\sum_i t_i}
\right),
\]
which is integrable because \(\sum_i t_i>0\). Thus the log-uniform-prior posterior is proper.

## Verification
The bundled checker independently evaluates
\[
\mathbb E_\alpha[(\alpha+T)^{-2}]
\]
by numerical integration of the Shanker density and compares it with the closed form involving \(E_1(\alpha^2)\) at several parameter values.

It also verifies the Fisher-information formula against direct numerical expectation of the negative second derivative, and checks the endpoint ratios
\[
\alpha\sqrt{I(\alpha)}
\]
near zero and at large \(\alpha\). The numerical calculations are consistency checks; the proof above is analytic.

Posterior propriety is established by the two endpoint bounds on the exact posterior kernel and does not rely on numerical integration.

## Relationship to prior work
Mohammad et al. (2026) derive the UShD likelihood, prove uniqueness of the maximum-likelihood estimator, and use observed Fisher information for frequentist asymptotic intervals. In the Bayesian section they introduce a gamma prior and then state that the limiting kernel \(1/\alpha\) serves as Jeffreys' prior. Their simulations and posterior plots subsequently label this choice as a non-informative Jeffreys prior.

Abushal (2019) studies Bayesian estimation for the parent Shanker distribution. That paper also uses a gamma prior and sets both hyperparameters to zero for a “non-informative prior,” producing the same \(1/\alpha\) kernel, but it does not identify that kernel as the model's Jeffreys-rule prior in the inspected full text.

Jeffreys' rule for a scalar model is proportional to the square root of Fisher information and is invariant under smooth reparameterization. Applying that rule to the Shanker likelihood gives the formula in this finding. Because the unit transformation is independent of \(\alpha\), no additional information calculation is needed for the bounded version.

Focused searches for the unit Shanker model, the Shanker model, Jeffreys priors, Fisher information, exponential-integral formulations, and correction notices did not locate this exact prior or a correction to the 2026 article.

## Limitations
The finding corrects the identification of the prior; it does not recompute the simulation tables, posterior means, or credible intervals under the actual Jeffreys-rule prior.

The source's \(1/\alpha\) posterior is proper for every nonempty interior sample, so the existing Bayesian numerical results are not rendered undefined. They should instead be interpreted as results under an improper log-uniform prior.

The Jeffreys-rule prior itself is improper because it behaves like a constant multiple of \(1/\alpha\) at both parameter-space endpoints. No claim is made here about whether it is preferable to weakly informative proper priors for applications.

## References
1. H. H. Mohammad, M. N. Mousa, K. S. Sultan, and M. M. M. Mansour, “Two-parameter family of Unit distributions: theory, statistical inference, and reliability applications,” AIMS Mathematics 11 (2026), 28887–28949. DOI: 10.3934/math.20261150.
2. T. A. Abushal, “Bayesian estimation of the reliability characteristic of Shanker distribution,” Journal of the Egyptian Mathematical Society 27 (2019), article 30. DOI: 10.1186/s42787-019-0033-x.
3. E. van Zwet, “A default prior for regression coefficients,” Statistical Methods in Medical Research 28 (2019), 3799–3807. DOI: 10.1177/0962280218817792.
