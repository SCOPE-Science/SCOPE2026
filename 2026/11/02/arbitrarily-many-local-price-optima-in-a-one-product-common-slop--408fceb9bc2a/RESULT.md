# Arbitrarily many local price optima in a one-product common-slope logit mixture

## Finding

**Theorem (unbounded price multimodality with one product).** For every integer \(m\geq1\) there exist strictly increasing positive valuations \(0<\theta_1<\cdots<\theta_m\) and strictly positive market shares \(w_1,\ldots,w_m\), with \(\sum_{j=1}^m w_j=1\), such that the expected revenue from selling one product at a single nonnegative price,
\[
R_m(p)=p\sum_{j=1}^m\frac{w_j}{1+\exp(p-\theta_j)},\qquad p\geq0,
\]
has at least \(m\) distinct **strict local maxima** in \((0,\infty)\), separated by at least \(m-1\) distinct strict local minima. All customer segments have exactly the same price sensitivity, equal to one. The parameter tuples satisfying these conclusions include a nonempty open subset of the positive-share, strictly ordered-valuation parameter space.

Thus the number of distinct local price optima for a single product is unbounded as the number of latent customer segments increases, even with a common price coefficient and no price discrimination. This is a lower-bound existence theorem; it does **not** assert that \(m\) is the largest possible number of maxima for \(m\) segments.

## Assumptions and scope

The model has one seller, one purchasable product, an outside option, zero marginal cost, and a common price \(p\geq0\). Segment \(j\) has deterministic product utility \(\theta_j-p\), whereas the outside option has deterministic utility zero. Independent, identically distributed type-I extreme-value utility shocks produce the binary logit purchase probability
\[
q_j(p)=\frac{1}{1+\exp(p-\theta_j)}.
\]
The weights \(w_j\) are the positive proportions of potential customers. Units normalize the common price coefficient to one; multiplying price and valuations by a common positive monetary scale yields equivalent models. No supply constraints, price caps, nonlinear costs, or interactions between different customers are assumed. The claim concerns exact population expected revenue, not finite-sample pricing estimates.

## Proof

Write
\[
f_\theta(p)=\frac{p}{1+\exp(p-\theta)},\qquad
f_\theta'(p)=\frac{1+(1-p)\exp(p-\theta)}{(1+\exp(p-\theta))^2}.
\]
We first establish four elementary facts for \(p\geq0\), \(\theta>0\):

1. If \(q=1/(1+\exp(p-\theta))\), then \(f_\theta'(p)=q-pq(1-q)\), and therefore
\[
|f_\theta'(p)|\leq1+\frac p4.
\]
The bound is independent of \(\theta\).
2. For every fixed \(p\geq0\), \(f_\theta'(p)\to1\) as \(\theta\to\infty\).
3. For each fixed \(\theta\), \(f_\theta'(p)<0\) for all sufficiently large \(p\), while \(f_\theta'(p)\to0\) as \(p\to\infty\). Indeed, the derivative numerator is \(1-(p-1)\exp(p-\theta)\), which eventually becomes negative, and the derivative is asymptotic to \(-(p-1)\exp(\theta-p)\).
4. At the point \(p=\theta+1\),
\[
f_\theta'(\theta+1)=\frac{1-\theta\mathrm e}{(1+\mathrm e)^2}<0
\]
whenever \(\theta>1/\mathrm e\).

We inductively construct a positive linear combination \(F_m(p)=\sum_{j=1}^m a_j f_{\theta_j}(p)\), with \(a_j>0\), together with a strictly ordered sequence of \(2m\) derivative-sign witnesses
\[
0\leq s_1<t_1<s_2<t_2<\cdots<s_m<t_m
\]
satisfying \(F_m'(s_i)>0\) and \(F_m'(t_i)<0\) for every \(i\).

For \(m=1\) take \(\theta_1=2\), \(a_1=1\), \(s_1=0\), and \(t_1=3\). The derivative is positive at zero and negative at three.

Suppose the construction holds for \(m\) segments. Let \(W\) be its finite set of \(2m\) witness prices. Set \(\delta=\min_{p\in W}|F_m'(p)|>0\) and \(K=\max_{p\in W}(1+p/4)<\infty\). Choose \(0<\varepsilon<\delta/(2K)\). For any new valuation \(\theta\), the uniform derivative bound gives
\[
|\varepsilon f_\theta'(p)|<\delta/2\quad(p\in W),
\]
so adding the new segment with coefficient \(\varepsilon\) preserves **every** previous strict witness sign.

By fact 3, there is \(u>t_m\) such that \(-\varepsilon/4<F_m'(u)<0\). Fix this \(u\). By fact 2, choose a new \(\theta>\max\{u,\theta_m,1\}\) large enough that \(f_\theta'(u)>1/2\) and \(F_m'(\theta+1)<0\); the latter also follows from fact 3. Then
\[
(F_m+\varepsilon f_\theta)'(u)>-\varepsilon/4+\varepsilon/2=\varepsilon/4>0,
\]
whereas
\[
(F_m+\varepsilon f_\theta)'(\theta+1)<0
\]
because both summands are negative at \(\theta+1\). Thus \(s_{m+1}=u\) and \(t_{m+1}=\theta+1\) append a new disjoint positive-to-negative derivative interval, leaving the previous intervals intact. This completes the induction for every \(m\).

Each closed interval \([s_i,t_i]\) has an interior maximizer because the derivative is positive at its left endpoint and negative at its right endpoint. This local maximum is **strict**: the function is real analytic and nonconstant, so its nonzero derivative has isolated zeros and an interior local maximum cannot lie on a plateau. Between successive intervals, the negative derivative at \(t_i\) and positive derivative at \(s_{i+1}\) similarly force an interior strict local minimum. The intervals are disjoint, so all those extrema are distinct.

Finally divide every coefficient \(a_j\) by \(\sum_j a_j>0\). This produces positive weights summing to one and multiplies the revenue by a positive constant, preserving every derivative sign and extremum. The same fixed \(2m\) strict witness inequalities persist under sufficiently small perturbations of the valuations and weights, proving that the configurations occupy a nonempty relatively open set. \(\square\)

## Verification

A reproducible exact-rational interval checker is supplied as `verify.py`; it uses only Python's standard library. Its four illustrative instances have valuation prefixes
\[
(2),\quad(2,15),\quad(2,15,40),\quad(2,15,40,80)
\]
and respective positive unnormalized weight prefixes from
\[
\left(1,\frac1{100},\frac1{100000},\frac1{1000000000}\right).
\]
For the four-segment instance, strict derivative signs at the ordered prices
\[
0\;(+),\;3\;(-),\;10\;(+),\;15\;(-),\;35\;(+),\;41\;(-),\;75\;(+),\;81\;(-)
\]
are certified by rational lower and upper bounds for the relevant exponentials. The script additionally certifies all initial prefixes, for a total of 50 rational assertions. For positive integers it bounds the exponential using a finite Taylor sum and an explicit geometric remainder; for negative integers it reciprocates the enclosing positive bounds. No floating-point sign decision is used for acceptance. The numerical example checks are **finite illustrations only**; the assertion for every \(m\) follows from the induction.

To reproduce: `python3 verify.py` from the directory containing that file.

## Relationship to prior work

The finite-mixture logit demand model is established. Aksoy-Pierson, Allon, and Federgruen (2013) analyze mixed-logit price competition and the lack of general quasiconcavity, focusing on sufficient conditions for equilibria. Li, Webster, Mason, and Kempf (2018) explicitly show failure of quasiconcavity in a **single-product, two-segment, common-slope** example and give conditions restoring concavity; the present claim does not treat the two-segment counterexample as novel. Van de Geer and den Boer (2022) show a two-segment, single-product multimodal revenue curve and present global approximation algorithms. Their displayed examples and algorithms do not, on the inspected sections, yield the all-integer one-product lower bound above. Here the distinct content is an explicit induction producing one additional strict price optimum for *every* added segment, while keeping the same price sensitivity, with open-set stability.

No general exact upper bound on the number of extrema is claimed. Priority remains provisional pending broader independent literature review, including possible equivalent results in the theory of mixtures and total positivity.

## Limitations

The construction uses arbitrarily separated valuations and potentially highly unequal positive segment masses. It does not assert that the local maxima have comparable revenues, remain easily detectable under noisy demand estimates, or result in a computational-complexity lower bound. It does not derive an upper bound on the number of local maxima for fixed \(m\), nor address multiple products, nonlinear costs, capacity constraints, endogenous valuations, or price discrimination. Existence of more than one local maximum is not the same as coexistence of multiple global optimizers. The originality assessment is based on inspected sources and is not independent certification.

## References

1. Aksoy-Pierson, M., Allon, G., and Federgruen, A. (2013). *Price Competition Under Mixed Multinomial Logit Demand Functions*. Management Science 59(8), 1817–1835. First published online 22 April 2013. https://doi.org/10.1287/mnsc.1120.1664 . Author-hosted full text: https://tuck.dartmouth.edu/uploads/content/SSRN-id2405684.pdf .
2. Li, H., Webster, S., Mason, N., and Kempf, K. (2018, online). *Product-Line Pricing Under Discrete Mixed Multinomial Logit Demand*. Manufacturing & Service Operations Management 21(1), 14–28. https://doi.org/10.1287/msom.2017.0675 .
3. Van de Geer, R., and den Boer, A. V. (2022). *Price Optimization Under the Finite-Mixture Logit Model*. Management Science 68(10), 7480–7496. https://doi.org/10.1287/mnsc.2021.4272 . Public full text: https://www.researchgate.net/publication/358949731_Price_Optimization_Under_the_Finite-Mixture_Logit_Model .
