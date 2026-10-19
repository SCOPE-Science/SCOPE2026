# A convexity barrier for mixed-order nonlinear public-goods coexistence

## Finding
Consider a well-mixed evolutionary public-goods game in which interactions may occur in any finite number of distinct group sizes, each with its own synergy or discount factor. Under the geometric-increment public-good benefit law, the payoff difference between cooperators and defectors is convex in cooperation frequency, regardless of the number of sizes and regardless of whether the nonlinearities are synergistic or discounting. Consequently the replicator flow has **at most two isolated interior equilibria**, and **at most one asymptotically stable interior equilibrium**. The two-interior-equilibrium bound is attained by an explicit game mixing **three** different group sizes; no proliferation of coexistence states is possible merely by adding more group sizes in this model.

## Assumptions and scope
Let \(L\) be any finite nonempty subset of integers \(\{2,3,\ldots\}\). Let \(w_\ell>0\) for \(\ell\in L\) with \(\sum_{\ell\in L}w_\ell=1\); let \(\delta_\ell>0\) be group-size-specific geometric marginal-benefit multipliers, and let \(b_\ell>0\) be group-size-specific benefit scales. Cooperators pay constant cost \(c>0\), and benefits in groups of size \(\ell\) are shared equally. Conditional on a random group of that size, other members cooperate independently with probability \(x\in[0,1]\). We study the infinite-population, two-strategy replicator dynamics with \(x\) the cooperator fraction and with fixed sampling weights \(w_\ell\). No claim is made about finite-population stochastic dynamics or heterogeneous network correlations.

The difference between the expected cooperator and defector payoffs, after common payoffs are canceled, is
\[
H(x)=G(x)-c,\qquad
G(x)=\sum_{\ell\in L}\frac{w_\ell b_\ell}{\ell}\,[1+(\delta_\ell-1)x]^{\ell-1},
\]
and the evolution equation is
\[
\dot x=x(1-x)H(x),\qquad 0\le x\le1.
\]
The original mixed-order geometric public-goods model is recovered by taking a common benefit ratio \(b_\ell/c=r\) and a fixed number of sizes; the present claim additionally allows all positive benefit scales to depend on size.

## Proof
If a focal cooperator replaces a focal defector in a size-\(\ell\) game with \(K\) other cooperators, the added marginal collective return is \(b_\ell\delta_\ell^K\), shared among \(\ell\) group members. Here \(K\sim\operatorname{Binomial}(\ell-1,x)\). The binomial identity
\[
\mathbb E[\delta_\ell^K]=(1-x+\delta_\ell x)^{\ell-1}
\]
gives the displayed expression for \(H\). For \(\ell\ge3\), twice differentiating gives
\[
G''(x)=\sum_{\substack{\ell\in L\\\ell\ge3}}
\frac{w_\ell b_\ell(\ell-1)(\ell-2)(\delta_\ell-1)^2}{\ell}
[1+(\delta_\ell-1)x]^{\ell-3}\ge0.
\]
Every base \(1+(\delta_\ell-1)x\) is strictly positive on \([0,1]\). Therefore \(G\) is strictly convex if and only if some size \(\ell\ge3\) with positive weight has \(\delta_\ell\ne1\). Otherwise all summands have degree at most one and \(G\) is affine. A strictly convex function has at most two intersections with a horizontal line; an affine nonconstant function has at most one. If \(G\equiv c\), every \(x\in(0,1)\) is stationary but **none is an isolated equilibrium**. Thus the universal isolated-equilibrium bound includes all degeneracies.

In the strictly convex case, exactly two distinct interior roots exist **if and only if**
\[
G'(0)<0<G'(1),\qquad G(m)<c<\min\{G(0),G(1)\},
\]
where \(m\in(0,1)\) is the unique root of \(G'(m)=0\). Indeed, strict convexity makes \(G\) strictly decrease up to \(m\) and strictly increase thereafter. If the two roots are \(0<x_-<m<x_+<1\), then \(H\) is positive on \((0,x_-)\cup(x_+,1)\) and negative on \((x_-,x_+)\). Since \(x(1-x)>0\) in the open interval, \(x_-\) is locally asymptotically stable, \(x_+\) is repelling, \(x=0\) is unstable from the right, and \(x=1\) attracts from the left. Every initial \(x(0)\in(0,x_+)\) converges to \(x_-\), and every initial \(x(0)\in(x_+,1)\) converges to \(1\). In all other nondegenerate cases there can be at most one interior attracting equilibrium, by convexity and the alternating signs between simple roots; a tangency at the minimum is nonhyperbolic and only one-sided attracting.

**Sharp three-order example.** Take
\[
L=\{2,3,4\},\quad (w_2,w_3,w_4)=(1/2,1/4,1/4),
\quad (\delta_2,\delta_3,\delta_4)=(1/5,1/4,2),
\quad b_\ell=200/77,\quad c=1.
\]
Let \(Q(x)=G(x)/(200/77)\) be the normalized benefit polynomial. Then
\[
Q(x)=\frac14(1-4x/5)+\frac1{12}(1-3x/4)^2+\frac1{16}(1+x)^3
=\frac{60x^3+225x^2-132x+380}{960}.
\]
Its second derivative is \(Q''(x)=3x/8+15/32>0\), and
\[
Q(0)=19/48>77/200,\qquad Q(1/4)=181/480<77/200,
\qquad Q(1)=533/960>77/200.
\]
The level \(c/b_\ell=77/200\) therefore has one intersection in \((0,1/4)\) and one in \((1/4,1)\), and strict convexity rules out others. The intersections are the two roots in \((0,1)\) of
\[
300x^3+1125x^2-660x+52=0,
\]
approximately \(0.0943400656263767\) and \(0.429863627865109\), respectively. The lower root is attracting, the upper is repelling, and full cooperation is a second attracting endpoint. These inequalities and the degree-three polynomial are verified using exact rational arithmetic in the accompanying program.

## Verification
The standalone Python 3 standard-library program `verify.py` derives the polynomial by exact fraction arithmetic, differentiates it, checks the stated sample inequalities and verifies that exactly two roots lie in the claimed disjoint intervals by strict convexity. The infinite class theorem, including the convexity inequality and degenerate affine case, follows from the displayed symbolic derivation; a finite script is not offered as a proof for all choices of \(L\).

## Relationship to prior work
Llabrés, Sadekar, Malizia and Battiston (arXiv:2604.07228, first posted 8 April 2026) study nonlinear public-goods games of one order or a mixture of two interaction orders; their Appendix A proves an at-most-two-interior-equilibria claim in the two-order case by comparing two monotone terms. The present statement establishes a uniform upper bound for **every finite number of orders**, with arbitrary, independently chosen positive synergy/discount factors and size-dependent benefit multipliers. The structural reason is convexity of each geometric-marginal-return term, and the constructed three-order example attains the limit.

Peña's analysis of group-size diversity (2012) allows random group sizes but uses a common synergy factor across sizes in its geometric public-good example, yielding a monotone payoff difference in cooperation frequency. It analyzes a different convexity—dependence on group size—rather than the mixed-sign size-dependent nonlinearities here. Hauert and McAvoy (2024) treat frequency-dependent returns in nonlinear public goods but do not establish this arbitrary-order geometric-return classification. Classical calculus and one-dimensional phase-line theory underpin the argument; no new general convexity theorem is claimed.

## Limitations
The theorem assumes geometric marginal benefit factors and positive averaging weights, a well-mixed infinite population, a constant cooperation cost, and finitely many group sizes. Arbitrarily chosen nonlinear benefit functions may have oscillatory payoff differences and more than two equilibria; the no-go bound does not extend to those models. No claim of uniqueness in the entire mathematical literature is made; prior work using a broader convexity framework might imply this specialization. The roots in the example are defined exactly by the cubic and intervals; the decimal approximations are not the proof.

## References
1. J. Llabrés, O. Sadekar, F. Malizia and F. Battiston, *Emergence of cooperation in nonlinear higher-order public goods games*, arXiv:2604.07228 (initial public posting 2026-04-08; later Phys. Rev. E 114, 034316 (2026)). https://arxiv.org/abs/2604.07228
2. J. Peña, *Group-size diversity in public goods games*, Evolution 66, 623–636 (2012), DOI:10.1111/j.1558-5646.2011.01504.x.
3. C. Hauert and A. McAvoy, *Frequency-dependent returns in nonlinear public goods games*, arXiv:2404.13728 (2024). https://arxiv.org/abs/2404.13728
