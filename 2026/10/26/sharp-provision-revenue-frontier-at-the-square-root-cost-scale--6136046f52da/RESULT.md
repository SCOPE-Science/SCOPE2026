# Sharp provision–revenue frontier at the square-root cost scale

## Finding

Let \(V_1,\ldots,V_n\) be independent \(\mathrm{Unif}[0,1]\) private values for one binary, non-excludable public good. A direct mechanism chooses a provision probability \(q(v)\in[0,1]\), charges transfers \(t_i(v)\), and is dominant-strategy incentive-compatible (DSIC) and ex-post individually rational (EPIR). Let \(c_n\ge 0\) be the provision cost, \(p=\mathbb E[q(V)]\), and
\[
Z_n=\sum_{i=1}^n(2V_i-1).
\]
Write \(Q_n\) for the quantile function of \(Z_n\), and define
\[
R_n(p)=\int_{1-p}^{1}Q_n(u)\,du,\qquad R_n(0)=R_n(1)=0.
\]

For every \(n\) and \(p\in[0,1]\), a DSIC, EPIR mechanism with expected provision probability \(p\) and nonnegative ex-ante budget exists if and only if
\[
c_np\le R_n(p).
\]
Moreover, \(R_n(p)\) is the maximum expected payment attainable at that provision probability. It is attained by providing the good exactly when \(Z_n\) exceeds its \((1-p)\)-quantile, with the standard envelope payments.

Let \(\phi\) and \(\Phi\) be the standard normal density and distribution functions. For every fixed \(p\in(0,1)\),
\[
\lim_{n\to\infty}\frac{R_n(p)}{\sqrt n}
=\frac{1}{\sqrt 3}\,\phi\!\left(\Phi^{-1}(1-p)\right).
\]
Consequently, if \(c_n/\sqrt n\to\kappa>0\), the limiting feasibility boundary is
\[
\kappa p=\frac{1}{\sqrt 3}\,\phi\!\left(\Phi^{-1}(1-p)\right).
\]
There is a unique \(p_\kappa\in(0,1)\) satisfying this equation. Every sequence of budget-feasible DSIC, EPIR mechanisms has \(\limsup_{n\to\infty}p_n\le p_\kappa\), while every fixed \(p<p_\kappa\) is feasible for all sufficiently large \(n\). No assertion is made about finite-\(n\) feasibility at the equality point, where lower-order terms can matter.

## Assumptions and scope

Values are independent and identically distributed as \(\mathrm{Unif}[0,1]\); agents have risk-neutral, quasi-linear utility \(V_iq-t_i\); the public good is indivisible and non-excludable; and the mechanism is direct, DSIC, and EPIR. Budget balance is ex ante: \(\mathbb E[\sum_i t_i(V)-c_nq(V)]\ge0\). Randomized allocation is allowed through \(q(v)\in[0,1]\). The result does not assume ex-post budget balance and does not cover interdependent values, correlated values, or nonbinary provision.

## Proof

**1. Payment identity.** DSIC makes \(q\) nondecreasing in each report. The envelope formula gives, for fixed \(v_{-i}\),
\[
t_i(v)=v_iq(v)-\int_0^{v_i}q(s,v_{-i})\,ds+t_i(0,v_{-i}).
\]
EPIR at type \(v_i=0\) implies \(t_i(0,v_{-i})\le0\). Integrating over \(V_i\sim\mathrm{Unif}[0,1]\) and changing the order of integration yields
\[
\mathbb E[t_i(V)]\le
\mathbb E[(2V_i-1)q(V)].
\]
Thus \(\mathbb E[\sum_i t_i(V)]\le\mathbb E[Z_nq(V)]\).

**2. Exact fixed-probability revenue bound.** Among all measurable \(q\in[0,1]\) satisfying \(\mathbb E q=p\), the upper-tail rearrangement inequality gives
\[
\mathbb E[Z_nq(V)]\le
\int_{1-p}^{1}Q_n(u)\,du=R_n(p).
\]
Because \(Z_n\) is continuous, the upper-tail threshold has provision probability exactly \(p\). Since \(Z_n\) increases in every \(v_i\), this allocation is monotone in every report. The envelope payments with \(t_i(0,v_{-i})=0\) are DSIC and EPIR and attain expected payment \(R_n(p)\). Therefore the ex-ante budget is nonnegative exactly when \(c_np\le R_n(p)\).

**3. Gaussian limit.** The variables \(2V_i-1\) are independent, centered, and have variance \(1/3\). Hence \(Z_n/\sqrt n\) converges in distribution to \(N(0,1/3)\). Its second moments are uniformly bounded, so the normalized variables are uniformly integrable. Quantile convergence at every fixed \(p\in(0,1)\), followed by convergence of the corresponding upper-tail expectations, gives
\[
R_n(p)/\sqrt n\longrightarrow
\frac{1}{\sqrt3}\phi(\Phi^{-1}(1-p)).
\]

**4. Critical cost and sharpness.** If \(p_n\to p\in(0,1)\) and \(c_n/\sqrt n\to\kappa\), the exact budget criterion and the limit above require
\[
\kappa p\le\frac{1}{\sqrt3}\phi(\Phi^{-1}(1-p)).
\]
Also, \(R_n(p_n)/\sqrt n\le\sqrt{(1-p_n)/3}\); thus \(p_n\to1\) is impossible when \(\kappa>0\). The ratio
\[
p\longmapsto
\frac{\phi(\Phi^{-1}(1-p))}{\sqrt3\,p}
\]
is continuous and strictly decreasing from infinity to zero on \((0,1)\). This proves existence and uniqueness of \(p_\kappa\), and the limsup bound follows by taking convergent subsequences. For any fixed \(p<p_\kappa\), the limiting budget inequality is strict, so the upper-tail threshold mechanism is budget-feasible for all sufficiently large \(n\). At \(p=p_\kappa\), the leading-order terms cancel and this proof gives no finite-\(n\) conclusion.

## Verification

The payment identity, rearrangement bound, and budget criterion are exact. The asymptotic step uses the central limit theorem, quantile convergence to a continuous strictly increasing Gaussian distribution, and uniform integrability from \(\mathbb E[(Z_n/\sqrt n)^2]=1/3\). No numerical experiment or finite enumeration is used. The result proves an asymptotic frontier; it does not provide an elementary closed form for the finite-\(n\) quantile integral or settle lower-order behavior at the equality point.

## Relationship to prior work

Xi and Xie study adjusted mean-thresholding (AMT) mechanisms for public-good provision. They establish simultaneous budget balance and asymptotic efficiency when \(c_n=o(\sqrt n)\), prove an \(O(\sqrt n)\) upper order for total expected payments, and discuss the critical scale for their AMT construction. Their paper also expresses expected payments as a truncated virtual-surplus expectation. The present result uses that standard mechanism-design identity together with fixed-probability upper-tail optimization to state the full finite-\(n\) provision/revenue frontier for uniform values and its sharp Gaussian limit; it is not a new payment identity.

Kleinberg and Yuan show that optimal revenue for a uniform public project is of order \(\sqrt n\), and analyze revenue relative to welfare. Their treatment does not state the full fixed-provision-probability frontier above. Mailath and Postlewaite study a different unanimous yes/no bargaining model with positive and negative private values; the available abstract does not imply this public-good result. Hellwig studies second-best provision with many participants and is relevant background, but the available text does not establish this frontier.

## Limitations

The distribution is restricted to independent uniform values, and the result uses DSIC and EPIR. The boundary is asymptotically sharp away from equality; no finite-size guarantee is claimed at \(p=p_\kappa\). The finite-\(n\) frontier is exact as a quantile integral rather than an elementary closed form. The literature comparison found no directly equivalent statement in the searched sources, but it cannot establish absolute novelty. Independent audit has not been performed.

## References

1. Jin Xi and Haitian Xie, “Strength in Numbers: Robust Mechanisms for Public Goods with Many Agents,” arXiv:2101.02423, first submitted 7 January 2021; version 4 dated 15 May 2023.
2. Robert Kleinberg and Yang Yuan, “On the Ratio of Revenue to Welfare in Single-Parameter Mechanism Design,” Proceedings of EC 2013, 589–602; arXiv:1305.0534; DOI 10.1145/2482540.2482584.
3. George J. Mailath and Andrew Postlewaite, “Asymmetric Information Bargaining Problems with Many Agents,” The Review of Economic Studies 57(3) (1990), 351–367; DOI 10.2307/2298018.
4. Martin F. Hellwig, “Public-Good Provision with Many Participants,” The Review of Economic Studies 70(3) (2003), 589–614; DOI 10.1111/1467-937X.00257.
