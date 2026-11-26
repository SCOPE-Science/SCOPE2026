# Cooperative bistability in finite mixtures: weight criterion and quadratic onset

## Finding and scope

In an infinite well-mixed population, let the strategy-independent interaction classes have integer sizes \(n_j\ge2\), geometric-return parameters \(\delta_j>0\), and weights \(w_j\ge0\) with \(\sum_j w_j=1\). The number of classes is finite; classes may share the same size. In the deterministic replicator model with a common unit contribution cost and benefit-to-cost ratio \(r>0\), put
\[
H_w(x)=\sum_j\frac{w_j}{n_j}(1+(\delta_j-1)x)^{n_j-1},\qquad
\dot x=x(1-x)(rH_w(x)-1).
\]
Define the endpoint slopes
\[
A(w)=\sum_j w_j\frac{n_j-1}{n_j}(\delta_j-1),\qquad
B(w)=\sum_j w_j\frac{n_j-1}{n_j}(\delta_j-1)\delta_j^{n_j-2}.
\]
There are at most two **isolated** interior equilibria. Two such equilibria exist for some \(r\) if and only if \(A(w)<0<B(w)\). Thus the admissible weights are exactly the intersection of the simplex with two open halfspaces. With these slopes, let \(z\) be the unique interior minimizer of \(H_w\). The exact open interval with two isolated interior equilibria is
\[
\frac{1}{\min\{H_w(0),H_w(1)\}}<r<\frac{1}{H_w(z)}.
\]
Within this interval the lower interior equilibrium and full cooperation are locally asymptotically stable on \([0,1]\), and the upper interior equilibrium and full defection are unstable. A feasible weight vector exists exactly when there is a discounting class and a synergistic class, with at least one of the chosen pair of size at least three. This remains the existence criterion if every class must receive positive weight. If \(H_w\) is constant and \(rH_w=1\), all frequencies are equilibria and none in the interior is isolated; this case is not bistability as defined above.

For an admissible affine path \(w(t)=w^0+tv\), \(t\ge0\) near zero, write \(H_t=H_{w(t)}\). At a left-endpoint onset suppose \(H_0'(0)=0\), \(c=H_0''(0)>0\), and \(\kappa=-\partial_t H_t'(0)|_{t=0}>0\). Then for sufficiently small positive \(t\) the interior saddle-node at the upper boundary in \(r\) is located at \(z(t)=\kappa t/c+O(t^2)\). The width of the open interval is
\[
\Delta r(t)=\frac{\kappa^2}{2cH_0(0)^2}t^2+O(t^3).
\]
At a right-endpoint onset the conditions are \(H_0'(1)=0\), \(c=H_0''(1)>0\) and \(\kappa=\partial_t H_t'(1)|_{t=0}>0\). Then \(1-z(t)=\kappa t/c+O(t^2)\) and the width formula uses \(H_0(1)\) in place of \(H_0(0)\). The saddle-node point itself is not an asymptotically stable interior equilibrium; the attracting branch lies below \(z(t)\) in the two-root interval.

## Proof

Each affine base \(1+(\delta_j-1)x\) is positive on \([0,1]\). The second derivative of a class term with \(n_j\ge3\) is its weight times
\[
\frac{(n_j-1)(n_j-2)}{n_j}(\delta_j-1)^2(1+(\delta_j-1)x)^{n_j-3};
\]
pairwise terms have zero second derivative. Hence \(H_w''\) is strictly positive everywhere if some class of size at least three has positive weight and \(\delta_j\ne1\). Otherwise \(H_w\) is affine, possibly constant. An affine function has at most one isolated intersection with any horizontal line, and a strictly convex function has at most two. In the strictly convex case two interior intersections require a zero derivative between them and thus \(H_w'(0)<0<H_w'(1)\). Conversely these slopes force strict convexity in the present family and give the interior minimizer \(z\). There are two interior intersections exactly when \(H_w(z)<1/r<\min\{H_w(0),H_w(1)\}\), since \(H_w\) decreases strictly to its minimum and increases strictly thereafter. Both endpoints and the minimum are positive. The sign of \(rH_w-1\) is positive, then negative, then positive; multiplying by \(x(1-x)>0\) in the interior gives the asserted stabilities. Equality at the upper threshold gives one tangency with positive drift on both sides; equality at the lower threshold gives a boundary intersection, not two isolated interior equilibria.

For feasibility, a negative and a positive class slope are both necessary. If every discounting and synergistic class has size two, then \(A=B\), so the strict inequalities cannot hold. Conversely, choose a discounting class \(d\) and a synergistic class \(s\), with one of them of size at least three. Let \(-p\) and \(q\) be their left slopes at unit weight, where \(p,q>0\); their right slopes are \(-pu\) and \(qv\) with \(u=\delta_d^{n_d-2}\le1\) and \(v=\delta_s^{n_s-2}\ge1\). Here \(u<v\). Choose positive weights satisfying \(u/v<qw_s/(pw_d)<1\), give other classes zero weight, and normalize. Then \(A<0<B\), and small perturbations in the simplex may make all weights positive by strictness.

At the left-endpoint onset, strict curvature and \(H_0'(0)=0\) give \(H_0'(1)>0\) and \(H_0(0)<H_0(1)\). The implicit function theorem applied to \(H_t'(z)=0\) gives the stated location, and the endpoint slopes have opposite signs for small \(t>0\). The smaller endpoint value is still \(H_t(0)\). Taylor expansion using \(H_t'(0)=-\kappa t\) and \(H_t''(0)=c+O(t)\) gives \(H_t(0)-H_t(z(t))=\kappa^2t^2/(2c)+O(t^3)\). Subtracting the two inverse endpoint values divides this difference by \(H_t(0)H_t(z(t))=H_0(0)^2+O(t)\), yielding the formula. Reflecting \(x\) to \(1-x\) gives the right-endpoint case. Both leading coefficients are positive, so the exponent is sharp under the stated transverse-onset assumptions.

## Exact example and verification

Take \((n_j,\delta_j)=(2,1/2),(3,2),(4,1/2)\), and weights \((5/8-\theta,\theta,3/8)\) with \(\theta=57/176-t\). Direct expansion gives
\[
H_t(x)=\frac{31}{88}+\frac t6-\frac{11t}{12}x+\left(\frac{251}{1408}-\frac t3\right)x^2-\frac3{256}x^3.
\]
Thus \(H_t'(0)=-11t/12\) and \(H_t'(1)=905/2816-19t/12\). All weights are positive for small positive \(t\). This is a left-endpoint onset with \(\kappa=11/12\), \(c=251/704\), \(H_0(0)=31/88\); substitution into the width formula gives \(\Delta r(t)=(20614528/2170899)t^2+O(t^3)\). The expansion and substitution use exact rational arithmetic; the continuum exclusion and arbitrary-class conclusions follow from the proof, not from checks on a parameter grid.

## Relationship to prior work and limitations

Llabrés, Sadekar, Malizia and Battiston ([arXiv:2604.07228v2](https://arxiv.org/abs/2604.07228)) analyze the same geometric-return model for two interaction orders, proving the two-order isolated-root ceiling and deriving the pairwise/triplewise phase diagram. Zhu et al. ([DOI:10.1038/s42005-024-01865-6](https://doi.org/10.1038/s42005-024-01865-6)) mix synergy and discounting at one group size. General multiplayer Bernstein-polynomial methods include root bounds via the gain sequence (Peña, Lehmann and Nöldeke, [arXiv:1310.0498](https://arxiv.org/abs/1310.0498)). The finite-population result *A sharp four-person reversal and universal convexity of finite-population public-goods selection gradients* ([record](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-a-sharp-four-person-reversal-and-universal-convexity-of-finite-p--782b8b55b870)) establishes the discrete convexity counterpart and identifies the corresponding infinite-population gain limit. The focus here is the explicit feasibility classification in weight space and the quantitative opening of the benefit-to-cost interval on its boundary, not convexity or the two-order root ceiling as separate contributions.

No conclusion is asserted for structured populations, finite-population stationary laws or frequency-dependent class weights. Degenerate onsets with zero curvature or a zero crossing speed are outside the width law. The stated literature comparisons are bounded, not a priority guarantee.
