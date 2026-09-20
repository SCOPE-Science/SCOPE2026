# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.**

The success probability was checked from two equivalent representations: \(p_n=g_n(s)=\mathbb E s^{C_n}\) and the exponential-race integral
\[
p_n=q\int_0^\infty e^{-qt}\prod_i(1-e^{-s w_{i,n}t})\,dt.
\]
After scaling, the exponent is strictly concave with a unique saddle. The saddle equation, compact bounds, curvature formula, and uniform first-order Laplace approximation follow from the fixed bounds \(m\le x_{i,n}\le M\).

The equal-probability specialization was checked against the exact gamma ratio
\[
\Gamma(n+1)\Gamma(nq/s+1)/\Gamma(n/s+1),
\]
and Stirling's formula gives the same prefactor and exponential rate as the saddle calculation.

For the derivative calculation, writing \(c_z=(1-z)/z\) and differentiating the integral representation gives exactly
\[
g_n'(s)/p_n=(n\bar y_n-1/c)/s^2.
\]
Substitution into Wang-Lu's definition
\[
\alpha=s(p-qg'(s))/(1-p)
\]
gives
\[
\alpha_n=\frac{p_n}{1-p_n}(1+s-cn\bar y_n).
\]
Laplace concentration yields \(\bar y_n-y_n=O(n^{-1/2})\), so \(\alpha_n=-cny_np_n(1+O(n^{-1/2}))\). Because the saddle stays bounded above and away from zero and \(p_n\) is exponentially small, Wang-Lu's two-sided theorem gives \(d_K=\Theta(np_n)\).

The profile limit follows from weak convergence on a compact support and strict concavity. The Schur-concavity statement follows pointwise from strict concavity of \(x\mapsto\log(1-e^{-xy})\), and the variance penalty follows from a uniform lower bound on its curvature over the compact \((x,y)\) region.

## Originality

**PASS, to the best of our knowledge.**

The closest reset-specific results located are materially different:

- Jocković-Todić derive a finite unequal-probability waiting-time distribution and analyze asymptotics of the mean in the equal-probability case.
- Li-Dai-Kim derive an explicit expected-waiting-time formula for arbitrary standard probabilities, but the accessible article description does not state a balanced non-uniform saddle asymptotic or a profile rate functional.
- Long gives the exact unequal-probability regenerative transform and a qualitative rare-success exponential limit conditional on transform/derivative hypotheses; the paper explicitly leaves estimation of the ordinary unequal coupon transform as the needed input.
- Wang-Lu prove the general sharp \(d_K\asymp p+|\alpha|\) theorem and explicitly list non-uniform coupon probabilities as a further direction, identifying evaluation of \(D_1\) and \(\alpha\) in terms of the probability vector as the challenge.

Searches for reset coupon collectors combined with non-uniform/unequal probabilities, saddle-point or Laplace-transform asymptotics, profile-rate functionals, majorization, and sharp exponential-approximation rates did not locate a prior statement of the theorem package here. Ordinary unequal coupon-collector literature contains extensive asymptotics and Schur-ordering results, but no located source supplied the fixed-reset success exponent, the explicit \(\alpha_n\sim-cny_np_n\) evaluation, or the resulting \(d_K=\Theta(np_n)\) rate for balanced non-uniform profiles.

Residual originality risk remains from older generalized coupon-collector, restart, and saddle-point literature under different notation. In particular, the Poissonization integral and majorization mechanism are classical ingredients; originality is claimed for the reset-specific profile asymptotics and their coupling to the recent sharp memoryless-catastrophe rate theorem, not for Laplace's method or Schur concavity themselves.

No inaccessible source was identified whose title or abstract specifically advertises the balanced non-uniform reset asymptotics proved here. Some older ordinary unequal-coupon papers were accessible only through abstracts or bibliographic descriptions, so an equivalent transform asymptotic hidden in that literature remains the main residual risk.

## Value

**PASS.**

The result answers a concrete open direction stated in the September 2026 memoryless-catastrophe paper in a broad, mathematically natural regime. It reduces an \(n\)-dimensional probability vector to an explicit one-dimensional saddle coupled to its empirical profile, provides the exponential scale and first prefactor for success and mean waiting time, and converts a general abstract convergence-rate theorem into a coupon-specific sharp order.

The quantitative heterogeneity penalty also gives structural information beyond the limit law: any persistent balanced deviation from uniformity increases the expected reset completion time by an exponential factor.

## Scientific limitations retained

The result assumes fixed reset probability and balanced probabilities of order \(1/n\). It does not cover moving-reset regimes, probabilities with vanishingly rare types, Zipf-like profiles, or second-order saddle corrections. The heterogeneity constant is explicit but not asserted optimal. The exponential-approximation theorem itself is taken from Wang-Lu; the contribution here is its non-uniform coupon specialization and asymptotic evaluation.
