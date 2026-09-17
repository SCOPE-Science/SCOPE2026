# Exact Chernoff envelopes for heterogeneous Bernoulli randomization

## Setup

Consider a finite population of \(n\) units. Treatment assignments are independent,
\[
Z_i\sim \mathrm{Bernoulli}(\pi_i),\qquad 0<\pi_i<1,
\]
with possibly unequal propensities. Potential outcomes satisfy known deterministic, possibly unit-specific bounds
\[
Y_i(0),Y_i(1)\in[a_i,b_i].
\]
Write
\[
c_i=\frac{a_i+b_i}{2},\qquad r_i=\frac{b_i-a_i}{2},
\]
and let
\[
\tau_n=\frac1n\sum_{i=1}^n\bigl(Y_i(1)-Y_i(0)\bigr)
\]
be the finite-population sample average treatment effect.

For deterministic centers \(m_i\), define the centered Horvitz--Thompson estimator
\[
\widehat\tau_n^{\mathbf m}
=
\frac1n\sum_{i=1}^n
\left[
(Y_i(1)-m_i)\frac{Z_i}{\pi_i}
-
(Y_i(0)-m_i)\frac{1-Z_i}{1-\pi_i}
\right].
\]
It is design-unbiased for \(\tau_n\).

The purpose of this note is to compute the exact worst-case cumulant-generating-function envelope over all bounded potential outcomes, optimize the centering for that exponential criterion, and extract finite-sample and asymptotic confidence bounds for heterogeneous propensities.

## Exact directional cumulant envelopes

Define, for \(p\in(0,1)\),
\[
F_p(\lambda,d)
=
\log\!\left[
(1-p)e^{-\lambda d/(1-p)}
+
p e^{\lambda d/p}
\right].
\]

### Theorem 1

For every \(\lambda\ge0\),
\[
U_{\mathbf m}(\lambda)
:=
\sup_{\substack{Y_i(0),Y_i(1)\in[a_i,b_i]\\1\le i\le n}}
\log\mathbb E\exp\!\left\{
\lambda n(\widehat\tau_n^{\mathbf m}-\tau_n)
\right\}
\]
is exactly
\[
U_{\mathbf m}(\lambda)
=
\sum_{i=1}^n
\max\!\left\{
F_{\pi_i}(\lambda,a_i-m_i),
F_{\pi_i}(\lambda,b_i-m_i)
\right\}.
\]
Likewise,
\[
L_{\mathbf m}(\lambda)
:=
\sup_Y
\log\mathbb E\exp\!\left\{
-\lambda n(\widehat\tau_n^{\mathbf m}-\tau_n)
\right\}
\]
is exactly
\[
L_{\mathbf m}(\lambda)
=
\sum_{i=1}^n
\max\!\left\{
F_{\pi_i}(-\lambda,a_i-m_i),
F_{\pi_i}(-\lambda,b_i-m_i)
\right\}.
\]

Thus the exact worst-case two-sided cgf envelope is
\[
K_{\mathbf m}(\lambda)
=
\max\{U_{\mathbf m}(\lambda),L_{\mathbf m}(\lambda)\}.
\]

### Proof

A direct algebraic rearrangement gives
\[
n(\widehat\tau_n^{\mathbf m}-\tau_n)
=
\sum_{i=1}^n
d_i\,\frac{Z_i-\pi_i}{\pi_i(1-\pi_i)},
\]
where
\[
d_i=(1-\pi_i)Y_i(1)+\pi_iY_i(0)-m_i.
\]
Because \(d_i\) is a convex combination of the two potential outcomes minus \(m_i\),
\[
d_i\in[a_i-m_i,b_i-m_i].
\]
Conversely, both endpoints are attainable: set both potential outcomes equal to \(a_i\) or both equal to \(b_i\).

Independence gives
\[
\log\mathbb E e^{\lambda n(\widehat\tau_n^{\mathbf m}-\tau_n)}
=
\sum_{i=1}^nF_{\pi_i}(\lambda,d_i).
\]
For fixed \(p,\lambda\), \(d\mapsto F_p(\lambda,d)\) is convex, since it is a log-sum-exp of two affine functions. Its maximum on a compact interval is therefore attained at an endpoint. The units can choose their endpoint configurations independently, so the displayed sum of endpoint maxima is not merely an upper bound but the exact supremum. Replacing \(\lambda\) by \(-\lambda\) proves the lower-tail formula. \(\square\)

## Midpoints are pointwise minimax for two-sided exponential loss

### Theorem 2

Let \(\mathbf c=(c_1,\ldots,c_n)\). For every \(\lambda\ge0\) and every deterministic center vector \(\mathbf m\),
\[
K_{\mathbf c}(\lambda)\le K_{\mathbf m}(\lambda).
\]
Consequently every symmetric Chernoff confidence certificate obtained from the exact worst-case cgf is pointwise no wider at the unitwise midpoints than at any other deterministic centering in this centered Horvitz--Thompson family.

At the midpoint, put
\[
q_i=\min\{\pi_i,1-\pi_i\}
\]
and, for \(0<q\le\tfrac12\),
\[
g_q(x)
=
\log\!\left[
q e^{x/q}+(1-q)e^{-x/(1-q)}
\right],
\qquad x\ge0.
\]
Then the two-sided envelope has the explicit form
\[
K_{\mathbf c}(\lambda)
=
\sum_{i=1}^n g_{q_i}(\lambda r_i).
\]

### Proof

For fixed \(\lambda\), \(U_{\mathbf m}(\lambda)\) and \(L_{\mathbf m}(\lambda)\) are convex functions of \(\mathbf m\): each is a sum of maxima of convex functions. Hence \(K_{\mathbf m}(\lambda)\), their maximum, is convex.

Reflect the centers through the midpoint:
\[
\mathbf m^\star=2\mathbf c-\mathbf m.
\]
The two endpoint deviations for each unit are negated by this reflection. Since
\[
F_p(\lambda,-d)=F_p(-\lambda,d),
\]
we have
\[
U_{\mathbf m^\star}(\lambda)=L_{\mathbf m}(\lambda),
\qquad
L_{\mathbf m^\star}(\lambda)=U_{\mathbf m}(\lambda),
\]
and therefore
\[
K_{\mathbf m^\star}(\lambda)=K_{\mathbf m}(\lambda).
\]
Convexity now yields
\[
K_{\mathbf c}(\lambda)
\le
\frac{K_{\mathbf m}(\lambda)+K_{\mathbf m^\star}(\lambda)}2
=
K_{\mathbf m}(\lambda).
\]

At \(\mathbf c\), the endpoint set is \(\{-r_i,r_i\}\), so upper and lower envelopes coincide. If \(p\le1/2\) and \(x\ge0\),
\[
p\sinh(x/p)\ge(1-p)\sinh(x/(1-p)),
\]
because \(t\mapsto t\sinh(x/t)\) is decreasing. Hence
\[
F_p(\lambda,r)\ge F_p(\lambda,-r)
\]
for \(p\le1/2\); the reverse endpoint is selected when \(p\ge1/2\). This gives the formula in terms of \(q_i=\min(p_i,1-p_i)\). \(\square\)

## A finite-sample heterogeneous-propensity confidence interval

Let
\[
\ell_\alpha=\log(2/\alpha).
\]
For every deterministic \(\lambda>0\), define
\[
R_\alpha(\lambda)
=
\frac{
\ell_\alpha+\sum_{i=1}^n g_{q_i}(\lambda r_i)
}{n\lambda}.
\]

### Corollary 3

For all bounded potential-outcome arrays satisfying the stated ranges,
\[
\Pr\!\left(
|\widehat\tau_n^{\mathbf c}-\tau_n|
\le R_\alpha(\lambda)
\right)\ge1-\alpha.
\]
Thus
\[
\left[
\widehat\tau_n^{\mathbf c}-R_\alpha(\lambda),
\widehat\tau_n^{\mathbf c}+R_\alpha(\lambda)
\right]
\]
is a finite-sample design-based confidence interval. Since \(\lambda\) depends only on the known design, bounds, and confidence level, it may be optimized in one dimension before observing outcomes.

More generally, for any other center vector \(\mathbf m\), replacing the midpoint envelope by \(K_{\mathbf m}(\lambda)\) gives a valid symmetric certificate, and Theorem 2 shows that its half-width is at least the midpoint half-width for every fixed \(\lambda\). The same remains true after optimizing over \(\lambda\).

### Proof

For the upper tail, Markov's inequality and Theorem 1 give
\[
\Pr\!\left(
\widehat\tau_n^{\mathbf c}-\tau_n\ge t
\right)
\le
\exp\{-\lambda nt+K_{\mathbf c}(\lambda)\}.
\]
The lower tail has the same midpoint envelope. Setting the right side to \(\alpha/2\) and applying the union bound proves the claim. \(\square\)

## Relation to Hoeffding and a sharper heterogeneous effective-sample-size scale

For each unit,
\[
g_{q_i}(\lambda r_i)
\le
\frac{\lambda^2r_i^2}
{8\pi_i^2(1-\pi_i)^2}
\]
by Hoeffding's lemma. If
\[
A_n=\sum_{i=1}^n
\frac{r_i^2}{\pi_i^2(1-\pi_i)^2},
\]
then choosing
\[
\lambda=\sqrt{\frac{8\ell_\alpha}{A_n}}
\]
gives
\[
R_\alpha(\lambda)
\le
\frac1n\sqrt{\frac{\ell_\alpha A_n}{2}}.
\]
For common outcome bounds this is exactly the midpoint version of the heterogeneous-propensity Hoeffding radius in Freidling (2026). Hence the exact cgf certificate is never worse than that support-length Hoeffding benchmark.

A closed-form variance-sensitive bound reveals the sharper propensity scale. Define
\[
V_n=\sum_{i=1}^n\frac{r_i^2}{\pi_i(1-\pi_i)},
\qquad
M_n=\max_{1\le i\le n}\frac{r_i}{q_i}.
\]
For every admissible potential-outcome array at midpoint, the summands \(X_i\) in
\[
n(\widehat\tau_n^{\mathbf c}-\tau_n)=\sum_iX_i
\]
satisfy
\[
\sum_i\operatorname{Var}(X_i)\le V_n,
\qquad
|X_i|\le M_n.
\]
Bernstein's inequality therefore gives the valid half-width
\[
R_{\mathrm{Ber},\alpha}
=
\frac1n
\left[
\frac{M_n\ell_\alpha}{3}
+
\sqrt{
2V_n\ell_\alpha+
\frac{M_n^2\ell_\alpha^2}{9}
}
\right].
\]

If \(V_n\to\infty\) and
\[
\frac{M_n}{\sqrt{V_n}}\to0,
\]
then, for fixed \(\alpha\),
\[
R_{\mathrm{Ber},\alpha}
=
\frac{\sqrt{2V_n\ell_\alpha}}{n}(1+o(1)).
\]

For common half-range \(r_i=r\), write
\[
n_{\mathrm{eff}}
=
\frac{n^2}{
\sum_{i=1}^n[\pi_i(1-\pi_i)]^{-1}
}.
\]
The leading radius is then of order
\[
\frac{r}{\sqrt{n_{\mathrm{eff}}}}.
\]
When all propensities equal \(\pi\),
\[
n_{\mathrm{eff}}=n\pi(1-\pi),
\]
recovering the familiar \(1/\sqrt{n\pi}\) scale for rare treatment. The formula therefore extends the effective-sample-size behavior to genuinely heterogeneous independent assignments through an aggregate harmonic propensity quantity rather than a minimum propensity alone.

## The heterogeneous rate is unavoidable for the midpoint estimator

The preceding rate is not only an upper-bound artifact.

### Proposition 4

Consider a triangular sequence of designs and bounded ranges with \(V_n\to\infty\) and \(M_n/\sqrt{V_n}\to0\). Choose the admissible endpoint configuration
\[
Y_i(0)=Y_i(1)=b_i.
\]
Then
\[
\frac{
n(\widehat\tau_n^{\mathbf c}-\tau_n)
}{\sqrt{V_n}}
\Longrightarrow N(0,1).
\]

Consequently, any deterministic symmetric half-width \(h_n=o(\sqrt{V_n}/n)\) centered at \(\widehat\tau_n^{\mathbf c}\) has worst-case coverage tending to zero. More generally, a sequence of such fixed-radius intervals having asymptotic coverage at least \(1-\alpha\) uniformly over the bounded potential outcomes must have
\[
\liminf_{n\to\infty}
\frac{nh_n}{\sqrt{V_n}}
\ge z_{1-\alpha/2},
\]
whenever the normalized radii have a limiting lower envelope, where \(z_{1-\alpha/2}\) is the standard-normal quantile.

### Proof

At this endpoint configuration,
\[
d_i=r_i,
\qquad
\operatorname{Var}(X_i)
=
\frac{r_i^2}{\pi_i(1-\pi_i)},
\]
so the variance sum is exactly \(V_n\). Moreover \(|X_i|\le M_n=o(\sqrt{V_n})\), which is the Lindeberg condition for the independent triangular array. The central limit theorem follows. The coverage lower bounds are immediate by evaluating any proposed interval along this admissible endpoint sequence. \(\square\)

## Context

Freidling (2026) develops finite-sample randomization-inference confidence intervals based on concentration inequalities. For independent Bernoulli assignment he allows unequal propensities and gives a heterogeneous Hoeffding interval; his sharper sub-Bernoulli specialization is stated for a common assignment probability. Sandoval, Balakrishnan, Feller, Jordan and Waudby-Smith (2026) develop nonasymptotic treatment-effect intervals attaining the correct effective sample-size scale under common-propensity Bernoulli randomization. Aronow and Lopatto (2026) prove a stronger minimax result of a different kind: for bounded finite-population outcomes, midpoint-differenced Horvitz--Thompson is minimax for worst-case squared error among all unbiased estimators under pairwise-independent inclusion indicators.

The present result concerns a different criterion. It computes the exact bounded-potential-outcome cgf envelope for independent heterogeneous assignments, proves pointwise midpoint optimality for that two-sided exponential envelope within the centered Horvitz--Thompson family, and yields an immediately computable finite-sample Chernoff interval. Its variance scale identifies the heterogeneous analogue of the common-propensity effective sample size, and the endpoint central limit theorem shows that this scale cannot be improved for deterministic symmetric radii centered at the midpoint estimator under the stated no-dominant-unit condition.

## Limitations

- Assignment indicators must be independent Bernoulli variables. Complete randomization, rejective sampling, rerandomization, and other dependent designs are not covered.
- The potential-outcome ranges must be known deterministic bounds.
- The midpoint minimax statement is only for the two-sided cgf envelope within the unitwise-centered Horvitz--Thompson family. It is not a minimax theorem over all unbiased estimators.
- The cgf envelope is exact over bounded potential outcomes, but Chernoff inversion and the two-sided union bound are not claimed to give the exact tail probability or the shortest possible confidence interval.
- The closed-form Bernstein interval is not variance-adaptive to benign realized outcomes.
- Originality is to the best of our knowledge. Older Poisson-sampling and survey-sampling concentration literature may contain equivalent endpoint-cgf observations under different notation.

## References

1. T. Freidling, "Randomization Inference with Concentration Inequalities", arXiv:2609.18586 (2026). https://arxiv.org/abs/2609.18586
2. R. J. Sandoval, S. Balakrishnan, A. Feller, M. I. Jordan, I. Waudby-Smith, "On Nonasymptotic Confidence Intervals for Treatment Effects in Randomized Experiments", arXiv:2601.11744 (2026). https://arxiv.org/abs/2601.11744
3. P. M. Aronow, P. Lopatto, "Minimax unbiased estimation for finite populations with bounded outcomes", arXiv:2605.20572 (2026). https://arxiv.org/abs/2605.20572
4. P. Bertail, S. Clémençon, "Bernstein-type exponential inequalities in survey sampling: Conditional Poisson sampling schemes", Bernoulli 25(4B), 3527--3554 (2019). https://doi.org/10.3150/18-BEJ1101
5. W. Hoeffding, "Probability inequalities for sums of bounded random variables", Journal of the American Statistical Association 58(301), 13--30 (1963). https://doi.org/10.1080/01621459.1963.10500830
