# Sharp two-segment price bifurcation and discontinuous optimal uniform pricing

## Finding

For a unit mass of buyers whose willingness to pay is a two-component mixture of exponential distributions, the revenue-maximizing uniform price undergoes a sharp bifurcation controlled solely by the ratio of exponential rates. Specifically, write
\[
Q(p)=w e^{-p}+(1-w)e^{-kp},\qquad R(p)=pQ(p),
\]
with \(p\geq0\), \(k>1\), and \(0<w<1\). Let \(k_c=3+2\sqrt2\). For \(1<k\leq k_c\), there is exactly one strict local (hence global) maximizer. For \(k>k_c\), there is an explicit nonempty weight interval with exactly two strict local revenue maxima separated by one strict local minimum. Within this interval there exists exactly one weight \(w_*(k)\) at which the two maxima have equal revenue. Below it, the lower price is uniquely optimal; above it, the higher price is uniquely optimal. At \(w_*(k)\), the two distinct prices both optimize revenue, giving a discontinuous global-price selection.

Define, for \(1/k<p<1\),
\[
H_k(p)=e^{-(k-1)p}\frac{kp-1}{1-p},\qquad
p_\pm=\frac{k+1\pm\sqrt{k^2-6k+1}}{2k}\quad (k>k_c).
\]
Set \(w_- = H_k(p_+)/(1+H_k(p_+))\) and \(w_+=H_k(p_-)/(1+H_k(p_-))\). Then \(0<w_-<w_+<1\); exactly three stationary prices exist precisely for \(w_-<w<w_+\). At either endpoint the double stationary point is not an additional local maximum. For \(w\notin(w_-,w_+)\), revenue has exactly one strict local maximum. A unique global-optimal-price switch occurs at \(w_*(k)\in(w_-,w_+)\).

## Assumptions and scope

One product is offered at one nonnegative posted price to a normalized unit population; buyer valuations are independent of pricing, with cumulative survival \(\Pr(V\geq p)=Q(p)\). The low-price-sensitivity class has weight \(w\) and exponential rate \(1\); the high-sensitivity class has weight \(1-w\) and rate \(k>1\). Marginal cost, capacity constraints, outside-product substitution and multiple selling periods are excluded. The analysis concerns deterministic expected revenue. For physical exponential rates \(0<\lambda_1<\lambda_2\), replace normalized \(p\) by \(\lambda_1 P\) and set \(k=\lambda_2/\lambda_1\). Every statement quantifies over all indicated \(k,w,p\), including boundary classification at \(k=k_c\) and \(w=w_\pm\).

## Proof

**1. Location of all stationary points.** Differentiation gives
\[
R'(p)=w e^{-p}(1-p)+(1-w)e^{-kp}(1-kp).
\]
It is positive on \(0\leq p\leq1/k\) and negative on \(p\geq1\), using strict positivity of both weights and \(k>1\). Thus every stationary price is interior to \((1/k,1)\). On this interval \(R'(p)\) has the same sign as
\[
\ell-H_k(p),\qquad \ell=\frac{w}{1-w}>0.
\]
Here \(H_k(1/k+)=0\) and \(H_k(1-)=+\infty\).

**2. Sharp bifurcation.** Direct logarithmic differentiation and exact simplification yield
\[
\frac{H_k'(p)}{H_k(p)}=
\frac{(k-1)[kp^2-(k+1)p+2]}{(1-p)(kp-1)}.
\]
The quadratic's discriminant is \(k^2-6k+1\). If \(1<k<k_c\), the numerator is positive on \((1/k,1)\), so \(H_k\) increases strictly. At \(k=k_c\), its derivative vanishes at just one point while \(H_k\) still increases strictly. Therefore \(R'\) crosses from positive to negative exactly once, giving the unique strict global maximum. If \(k>k_c\), the quadratic has precisely two roots \(1/k<p_-<p_+<1\). The function \(H_k\) increases on \((1/k,p_-)\), decreases on \((p_-,p_+)\), then increases on \((p_+,1)\). Its unique local maximum and minimum have values \(H_k(p_-)\) and \(H_k(p_+)\). Horizontal-line intersection now gives the stated weight thresholds, the one-versus-three root classification, and the alternating \(+,-,+,-\) derivative signs in the three-root window. On the two threshold curves, the tangential zero of \(R'\) does not change derivative sign and hence contributes no additional maximum. Positivity at zero and decay of revenue at infinity ensure existence of a global maximizer.

**3. Unique first-order global switch.** For \(w\in(w_-,w_+)\), denote the three roots by \(p_1(w)<p_2(w)<p_3(w)\). The first and third are strict local maxima. At the lower fold limit \(w\downarrow w_-\), the upper root and middle root coalesce at \(p_+\), and \(R(p_1,w_-)>R(p_+,w_-)\), because the revenue is strictly decreasing between the surviving lower maximum and the double stationary point. At the upper fold limit \(w\uparrow w_+\), the lower and middle roots coalesce at \(p_-\), with \(R(p_3,w_+)>R(p_-,w_+)\). Continuity and the implicit-function theorem apply to all three simple roots in the open interval.

To prove that the relative heights cross only once, write
\[
\log R(p,w)=\log p-kp+\log[1+w(e^{(k-1)p}-1)].
\]
At either stationary maximum the envelope derivative with respect to \(w\) equals
\[
G_w(p)=\frac{e^{(k-1)p}-1}{1+w(e^{(k-1)p}-1)}.
\]
For each fixed \(w\in(0,1)\), this expression is strictly increasing in \(p\). Therefore
\[
\frac{d}{dw}\log\frac{R(p_3(w),w)}{R(p_1(w),w)}
=G_w(p_3(w))-G_w(p_1(w))>0.
\]
At the lower weight endpoint the logarithmic height difference is negative; at the upper endpoint it is positive. The intermediate value theorem and strict monotonicity establish exactly one \(w_*(k)\) with equal heights and the precise winning-price ordering on either side. At equality the two maximizers are separated by the strict interior minimum. Every choice of a global-maximizing-price function must jump there; the set of optimizers at the switch contains both prices and no others.

## Verification

The accompanying `verify.py` checks the symbolic logarithmic derivative identity and discriminant with SymPy; evaluates 48 representative \((k,w)\) pairs; computes all three stationary prices and the height-crossing weight at \(k=10\) by bracketing and bisection. The numerical example yields
\[
(w_-,w_+,w_*)=(0.0230097295\ldots,\ 0.1756256102\ldots,\ 0.1228819700\ldots),
\]
\[
(p_1,p_2,p_3)=(0.1437379172\ldots,\ 0.3936711797\ldots,\ 0.9915241810\ldots),
\]
with equal optimal revenue \(0.04524709352\ldots\). These checks reproduce identities and examples, but the global existence, uniqueness and classification results are established by the preceding analytic argument, not by finite sampling. To replay, execute `python verify.py` with Python 3 and SymPy installed.

## Relationship to prior work

Kunz and Crone (2014) survey retail price optimization and document exponential price-demand models. Hetrakul and Cirillo (2014) examine heterogeneous latent-class choice and joint railway pricing and seat allocation; their full-text demand and optimization sections use a different log-linear and multinomial-choice formulation with resource allocation. The present result isolates an exactly analyzable, uncapacitated two-exponential willingness-to-pay mixture and its complete bifurcation and global-selection diagram. Kim, Blattberg and Rossi (1995) analyze heterogeneous price sensitivity in a different statistical model; complete text was not available for decisive theorem-level comparison. Kalyanam (1996) develops Bayesian mixtures over uncertain demand models; full historical overlap assessment remains incomplete. The precise theorem's independent priority is therefore provisional; no novelty is inferred merely from a failed search. No claims are made about general logit, many-class or dynamic pricing.

## Limitations

The exact switch relies on exponential valuation tails, exactly two classes, deterministic demand, a single uniform price, and zero marginal cost. Mixtures with three or more components, nonzero costs, heteroscedastic latent-class logit demand, or capacity constraints can have different phase diagrams. A bounded or empirical price grid can obscure the double optimum. The exact historical novelty of this specialized theorem remains subject to complete examination of older heterogeneous-demand pricing and general exponential-polynomial literature.

## References

1. J. Kunz and S. F. Crone, “Demand models for the static retail price optimization problem — A Revenue Management perspective,” *SCOR*, 2014, DOI: 10.4230/OASIcs.SCOR.2014.101. Public 2014-08-06. Full text: https://drops.dagstuhl.de/storage/01oasics/oasics-vol037-scor2014/OASIcs.SCOR.2014.101/OASIcs.SCOR.2014.101.pdf.
2. P. Hetrakul and C. Cirillo, “A latent class choice based model system for railway optimal pricing and seat allocation,” *Transportation Research Part E* 61 (2014), 68–83, DOI: 10.1016/j.tre.2013.10.005. Full text: https://cinziacirillo.weebly.com/uploads/5/3/6/0/53607733/tre-hc14.pdf.
3. B.-D. Kim, R. C. Blattberg and P. E. Rossi, “Modeling the Distribution of Price Sensitivity and Implications for Optimal Retail Pricing,” *Journal of Business & Economic Statistics*, 1995, DOI: 10.1080/07350015.1995.10524603 (full text not inspected).
4. K. Kalyanam, “Pricing Decisions Under Demand Uncertainty: A Bayesian Mixture Model Approach,” *Marketing Science*, 1996, DOI: 10.1287/mksc.15.3.207 (full text not inspected).
5. F. van de Geer and A. V. den Boer, “Price Optimization Under the Finite-Mixture Logit Model,” *Management Science*, DOI: 10.1287/mnsc.2021.4272 (different model; full text not inspected).
