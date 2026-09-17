# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.**

The estimator error was expanded exactly as
\[
n(\widehat\tau_n^{\mathbf m}-\tau_n)
=
\sum_i
\frac{d_i(Z_i-\pi_i)}{\pi_i(1-\pi_i)},
\qquad
d_i=(1-\pi_i)Y_i(1)+\pi_iY_i(0)-m_i.
\]
The feasible set for each \(d_i\) is exactly the interval \([a_i-m_i,b_i-m_i]\), with both endpoints attainable. Independence therefore factorizes the mgf, and convexity of the Bernoulli log-mgf in \(d_i\) makes the endpoint formula an exact supremum rather than a relaxation.

The midpoint theorem was checked by two independent structural facts: the two-sided worst-case envelope is convex in the center vector, and reflection through the unitwise midpoint swaps its upper- and lower-tail components. The explicit \(g_q\) representation follows from the monotonicity of \(t\sinh(x/t)\) for \(x>0\). The finite-sample confidence interval is then a direct Chernoff-Markov argument with a two-sided union bound.

The Hoeffding comparison uses the exact support length \(|d_i|/[\pi_i(1-\pi_i)]\). The Bernstein corollary uses
\[
\operatorname{Var}(X_i)\le r_i^2/[\pi_i(1-\pi_i)]
\]
and \(|X_i|\le r_i/\min(\pi_i,1-\pi_i)\); solving the Bernstein exponent gives the displayed quadratic root. For the lower-bound sequence \(Y_i(0)=Y_i(1)=b_i\), the variance sum is exactly \(V_n\), and \(M_n/\sqrt{V_n}\to0\) implies Lindeberg, yielding the stated normal limit and rate obstruction.

The statements were also stress-tested against equal-propensity and balanced-propensity special cases. No hidden requirement that treatment propensities be equal is used.

## Originality

**PASS, to the best of our knowledge.**

The closest directly relevant current sources were compared at the theorem level.

Freidling (arXiv:2609.18586) treats independent Bernoulli assignment with heterogeneous propensities and gives a Hoeffding confidence interval for centered Horvitz--Thompson estimation. His sharper sub-Bernoulli result is stated for equal assignment probabilities. The present result instead computes the exact worst-case cgf for arbitrary independent propensities, proves pointwise midpoint optimality for that cgf criterion, and exposes the aggregate heterogeneous effective-sample-size scale.

Sandoval et al. (arXiv:2601.11744) obtain nonasymptotic treatment-effect intervals with the correct effective sample-size behavior under common-propensity Bernoulli randomization. Their result supplies an important equal-propensity comparison but does not provide the heterogeneous endpoint envelope proved here.

Aronow and Lopatto (arXiv:2605.20572) prove that midpoint-differenced Horvitz--Thompson is minimax for worst-case squared error among all unbiased estimators under pairwise-independent inclusion indicators. That theorem is stronger in estimator class but different in loss: it does not establish the pointwise cgf envelope, Chernoff certificate, or heterogeneous tail rate here.

Bertail and Clémençon, "Bernstein-type exponential inequalities in survey sampling: Conditional Poisson sampling schemes", DOI 10.3150/18-BEJ1101, is a particularly relevant older survey-sampling source. Its accessible abstract and bibliographic record were inspected; the full theorem text was not inspected. It concerns Bernstein-type tail bounds for conditional Poisson/rejective sampling and contrasts those designs with independent Poisson sampling. Because generic Poisson-sampling concentration results could specialize to parts of the present argument, this source is the principal residual literature risk.

Targeted searches covered midpoint-differenced Horvitz--Thompson estimation together with Chernoff/cumulant-generating functions, heterogeneous Bernoulli treatment assignment with sub-Bernoulli bounds, unequal-propensity treatment-effect concentration, and Poisson-sampling Horvitz--Thompson exponential inequalities. No prior source was located that states the combined exact endpoint cgf, midpoint pointwise cgf minimaxity, and heterogeneous effective-sample-size consequence.

The novelty claim is therefore deliberately narrow: it is the explicit exact cgf/minimax/tail package for bounded potential outcomes under heterogeneous independent Bernoulli randomization, not a claim to invent the Chernoff method, Horvitz--Thompson estimation, midpoint differencing, or general Poisson-sampling concentration.

## Value

**PASS.**

The result sharpens a concrete current finite-sample randomization-inference problem in the regime where assignment propensities vary by unit. It replaces a support-length Hoeffding relaxation with an exact, separable cgf envelope requiring only a one-dimensional optimization, while preserving finite-sample design-based validity.

The midpoint theorem shows that the same center that is known to be optimal for worst-case squared error also has an exact pointwise optimality property for a substantially different exponential criterion within the centered Horvitz--Thompson family. The variance-scale corollary replaces dependence on the worst or squared inverse propensity by the aggregate quantity
\[
\sum_i[\pi_i(1-\pi_i)]^{-1},
\]
under a transparent no-dominant-unit condition, and the endpoint CLT shows that the resulting \(\sqrt{V_n}/n\) scale is unavoidable for fixed-radius midpoint-centered intervals.

## Scientific limitations retained

The theorem requires independent Bernoulli assignments and known bounded potential outcomes. It does not cover dependent randomization designs or claim minimaxity among all unbiased estimators. Exactness applies to the worst-case cgf; Chernoff inversion is not an exact-tail or shortest-interval theorem. The closed-form Bernstein specialization is not data-adaptive. Residual originality risk remains from older Poisson-sampling and survey-sampling concentration literature, especially results not available here at full theorem-text level.
