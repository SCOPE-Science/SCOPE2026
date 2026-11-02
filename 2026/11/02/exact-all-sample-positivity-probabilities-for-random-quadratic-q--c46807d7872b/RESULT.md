# Exact all-sample positivity probabilities for random quadratic quadrature

## Finding

Let \(m\ge 2\) and let \(Y_1,\ldots,Y_m\) be independent uniform random points of \([0,1]\). Define \(p_m\) as the probability that there are **strictly positive weights at every sampled point**, \(w_j>0\), satisfying
\[
\sum_{j=1}^m w_j f(Y_j)=\int_0^1 f(t)\,dt
\qquad\text{for every polynomial }f\text{ of degree at most }2.
\]
Set \(b=1/6\), \(B=1/2\), and \(\tau=1/12\). Then, for **every integer \(m\ge2\)**,
\[
\boxed{\displaystyle
p_m=1-\left(\frac23\right)^m+\left(\frac13\right)^m
-m\int_b^B\left[
\left(u+\frac{\tau}{u}\right)^{m-1}
+\left(1-u-\frac{\tau}{u}\right)^{m-1}
\right]du.}
\]
In particular, \(p_m\) is always an explicitly computable rational-linear combination of \(1\) and \(\log 3\). For illustration, \(p_2=0\), \(p_3=\tfrac12\log3-\tfrac13\), \(p_4=\log3-\tfrac23\), and \(p_5=\tfrac{25}{12}\log3-\tfrac{410}{243}\). The three-node case was already available and is **not** claimed as new here; the result is the entire sample-size law and its sharp tail.

The failure probability has the exact leading asymptotic
\[
\boxed{\displaystyle \lim_{m\to\infty}
\frac{1-p_m}{(2/3)^m}=3.}
\]
The smallest sample count with a success probability at least \(0.95\) is **\(m=11\)**: \(p_{10}=0.9411269334147931\ldots\), whereas \(p_{11}=0.9603356140490007\ldots\).

## Assumptions and scope

The underlying measure is Lebesgue probability measure on \([0,1]\); nodes are i.i.d. uniform and almost surely distinct. The trial function space is \(\operatorname{span}\{1,t,t^2\}\), with no bound on the size of the positive weights beyond positivity and the normalization implied by integrating constants. A quadrature rule may use all \(m\) nodes, or be reduced to three nodes if nonnegative rather than everywhere strictly positive weights are allowed. No adaptive choice of nodes is assumed.

All event characterizations below hold almost surely. Degenerate samples, ties, nodes at \(1/2\), and equality in geometric inequalities have probability zero. The statement does **not** concern the stronger constraint that each weight be close to \(1/m\), nor polynomial degrees above two.

## Proof

**1. Convex-hull reduction and the exact sample criterion.** A quadrature rule is exact on the three trial monomials precisely when
\[
\sum_j w_j=1,\qquad
\sum_jw_jY_j=\frac12,\qquad
\sum_jw_jY_j^2=\frac13.
\]
Writing \(\Gamma(t)=(t,t^2)\), this is the membership condition
\[
Q=\left(\frac12,\frac13\right)\in
\operatorname{conv}\{\Gamma(Y_j):1\le j\le m\}.
\]
For \(m\ge3\), almost surely the convex hull has nonempty interior, and positive weights on **all** nodes exist if and only if \(Q\) is an interior point. To prove the nontrivial direction, let \(\bar\Gamma=m^{-1}\sum_j\Gamma(Y_j)\). If \(Q\) is interior, for sufficiently small \(\varepsilon>0\), the point \((Q-\varepsilon\bar\Gamma)/(1-\varepsilon)\) remains in the convex hull. A convex representation of that point, mixed with \(\varepsilon\bar\Gamma\), has every coefficient at least \(\varepsilon/m>0\). Conversely, a positive representation cannot lie on a supporting edge of a full-dimensional convex hull unless every vertex lies on that edge.

Suppose the nodes straddle \(1/2\). Define their extreme and nearest distances on the two sides by
\[
\begin{aligned}
L&=\max_{Y_j<1/2}(1/2-Y_j),&R&=\max_{Y_j>1/2}(Y_j-1/2),\\
\ell&=\min_{Y_j<1/2}(1/2-Y_j),&r&=\min_{Y_j>1/2}(Y_j-1/2).
\end{aligned}
\]
For sorted distinct points on a strictly convex parabola, the lower polygonal envelope consists of chords between consecutive nodes, and the upper envelope is the chord between the two extreme nodes. At horizontal position \(t=1/2\), the chord joining \(1/2-u\) and \(1/2+v\) has ordinate \(1/4+uv\). Thus \(Q\) lies strictly between the lower and upper envelopes exactly when
\[
\boxed{\ell r<\tau<LR,\qquad \tau=1/12.}
\]
A sample supported on only one side cannot represent the target mean. For \(m=2\), the convex hull is a segment and contains \(Q\) with probability zero; this agrees with the formula below.

**2. Two disjoint failure events.** Define \(F_{\rm ext}\) to mean that the sample does not straddle the midpoint or that \(LR\le\tau\), and \(F_{\rm near}\) to mean that it straddles but \(\ell r\ge\tau\). These events are disjoint up to probability-zero boundaries because \(\ell r\le LR\). Their union is precisely failure of positive quadratic-exact quadrature.

For \(u,v\in(0,B)\), the joint density of the two *extreme* distances on opposite sides is
\[
f_{\rm ext}(u,v)=m(m-1)(u+v)^{m-2}.
\]
Indeed, designate the two extreme observations and require every other observation to fall in the interval of length \(u+v\). The joint density of the two *nearest* distances, on the other hand, is
\[
f_{\rm near}(u,v)=m(m-1)(1-u-v)^{m-2},
\]
since every other observation must avoid the central gap of length \(u+v\).

As \(uv>\tau\) is possible only for \(u\in(b,B)\) and \(v\in(\tau/u,B)\), integration in \(v\) gives
\[
\begin{aligned}
\Pr(F_{\rm ext})
&=1-m(m-1)\int_b^B\int_{\tau/u}^B (u+v)^{m-2}\,dv\,du\\
&=\left(\frac23\right)^m+m\int_b^B\left(u+\frac{\tau}{u}\right)^{m-1}\,du.
\end{aligned}
\]
Similarly,
\[
\begin{aligned}
\Pr(F_{\rm near})
&=m(m-1)\int_b^B\int_{\tau/u}^B (1-u-v)^{m-2}\,dv\,du\\
&=m\int_b^B\left(1-u-\frac{\tau}{u}\right)^{m-1}\,du
-\left(\frac13\right)^m.
\end{aligned}
\]
Their sum is \(1-p_m\), proving the displayed exact probability formula. For integer \(m\), both integrands are Laurent polynomials in \(u\) with rational coefficients. Integrating each monomial over the rational endpoints produces a rational number, except that exponent \(-1\) gives \(\log(B/b)=\log3\); hence the promised exact rational-logarithmic form.

**3. Sharp leading failure constant.** Write
\[
\Phi(u)=u+\frac{\tau}{u},\qquad
\Psi(u)=1-u-\frac{\tau}{u},\qquad u\in[b,B].
\]
The strictly convex function \(\Phi\) has maximum \(2/3\) only at the two endpoints, where
\[
\Phi'(b)=-2,\qquad\Phi'(B)=\frac23.
\]
By the one-sided endpoint Laplace estimate (obtained by a first-order Taylor expansion, changing to distance from the endpoint, and dominating the interior by a strictly smaller geometric factor),
\[
\lim_{m\to\infty}
\frac{m\int_b^B\Phi(u)^{m-1}\,du}{(2/3)^m}
=\frac1{|\Phi'(b)|}+\frac1{\Phi'(B)}
=\frac12+\frac32=2.
\]
Meanwhile, \(\Psi\) is maximized at \(u=\sqrt\tau\), with maximum \(1-1/\sqrt3<2/3\). Therefore \(m\int_b^B\Psi(u)^{m-1}du=o((2/3)^m)\), and also \((1/3)^m=o((2/3)^m)\). Adding the explicit extreme-failure term gives \((1-p_m)/(2/3)^m\to1+2=3\).

**4. The exact \(95\%\) cutoff.** Adding independent nodes cannot destroy convex-hull inclusion, so \(p_m\) is nondecreasing. The Laurent integrations give the exact forms
\[
\begin{aligned}
p_{10}&=-\frac{479035}{13608}+\frac{9475}{288}\log3,\\
p_{11}&=-\frac{2022183119}{34012224}+\frac{380105}{6912}\log3.
\end{aligned}
\]
The positive-term series \(\log3=2\sum_{k\ge0}2^{-(2k+1)}/(2k+1)\), with the tail after \(k=24\) bounded by \(\tfrac43\) times the first omitted summand, gives rational upper and lower bounds strong enough to certify \(p_{10}<19/20<p_{11}\). Monotonicity proves the sharp count \(11\).

## Verification

The included standalone `verify.py` uses only the Python standard library. It independently expands the Laurent powers using exact rational arithmetic and checks five explicit coefficient identities, compares the exact formula against separate numerical integrations for sixteen sample sizes, checks the rational-series certificate for the \(95\%\) threshold, and compares the chord criterion to exhaustive triangle barycentric tests on \(4{,}500\) distinct exact-rational samples. All checks passed from the included file. These finite checks are supplementary; the geometric density calculation and endpoint analysis above establish the theorem for all \(m\).

## Relationship to prior work

Neumayer, Schäfer and Ullrich [1] construct positive exact quadrature from random nodes in far greater function-space generality and give nonasymptotic sufficient sample budgets, including stronger near-uniform bounds on each weight. They do not provide the present all-sample exact success law for unconstrained positive weights in the quadratic uniform interval model. Hayakawa, Lyons and Oberhauser [2] study general random convex-hull inclusion probabilities, simplicial depth and cubature sample-size bounds; their general estimates do not state the present exact integral, rational-log sequence, or leading constant for the uniform parabola. Classical convex-hull and interpolation principles used here are not new. The three-node probability itself is prior-covered and is not part of the originality claim.

## Limitations

The probability formula assumes iid uniform nodes and exact moment feasibility, not positive weights with bounded dynamic range, approximation error, or numerical condition guarantees. The asymptotic describes failure as \(m\to\infty\), not finite-precision solver success. No claim is made about optimal sampling distributions, higher dimensions, higher polynomial degrees, or an exhaustive historical priority search. A more general older convex-hull distribution result might imply part of this special case and remains a residual literature risk.

## References

[1] S. Neumayer, M. Schäfer, and T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1 (first public 23 October 2026), https://arxiv.org/abs/2610.32699.

[2] S. Hayakawa, T. Lyons, and H. Oberhauser, *Estimating the probability that a given vector is in the convex hull of a random sample*, Probability Theory and Related Fields **185** (2023), 705–746, https://doi.org/10.1007/s00440-022-01186-1 (open-access full text).

[3] V. Tchakaloff, *Formules de cubatures mécaniques à coefficients non négatifs*, Bulletin des Sciences Mathématiques **81** (1957), 123–134; cited for classical positive cubature existence, not for the quantitative probability formula.
