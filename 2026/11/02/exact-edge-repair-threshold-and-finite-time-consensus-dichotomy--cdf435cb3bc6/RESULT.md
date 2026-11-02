# Exact edge-repair threshold and finite-time consensus dichotomy in adaptive bounded-confidence networks

## Finding
For every integer \(n\geq 3\), there is a nonempty open set of initial opinions and adaptive bounds on the complete network for which the adaptive Hegselmann–Krause model exhibits a sharp edge-restoration transition at \(\delta_c=1/(n-1)\). Every trajectory in this class converges to one common opinion, but the manner of consensus changes discontinuously: when \(0\leq\delta\leq\delta_c\), one dyad remains permanently unreceptive and all opinions are pairwise distinct at least at the two extreme agents at every finite time; when \(\delta_c<\delta<1\), the dyad becomes receptive after an explicitly determined finite number of iterations and all agents agree exactly one iteration later. The threshold is independent of the positive confidence-growth rate \(\gamma\).

## Assumptions and scope
The static underlying graph is the complete simple graph on \(n\geq3\) vertices. Opinions \(x_i(t)\in[0,1]\) evolve synchronously by averaging the agent's own opinion and the opinions of currently receptive neighbours. Two agents \(i\ne j\) are receptive at time \(t\) exactly when \(|x_i(t)-x_j(t)|<c_{ij}(t)\), with strict inequality. All dyadic bounds are initially \(c_{ij}(0)=c_0\in(0,1)\). At each iteration a receptive dyad updates its bound to \(c_{ij}(t)+\gamma(1-c_{ij}(t))\), while an unreceptive dyad updates it to \(\delta c_{ij}(t)\), with \(0<\gamma\leq1\) and \(0\leq\delta<1\). These are the original adaptive-confidence HK update rules of Li, Luo and Porter [1].

Relabel the two extreme initial opinions as \(a=x_1(0)\) and \(b=x_2(0)\), and suppose \(0\leq a<x_j(0)<b\leq1\) for \(3\leq j\leq n\). Set \(\Delta=b-a\). Assume
\[
\max_{\{i,j\}\neq\{1,2\}} |x_i(0)-x_j(0)|<c_0\leq \Delta .
\]
Thus precisely the edge \(\{1,2\}\) is absent from the initial effective graph. The strict inequalities are feasible on a full-dimensional open parameter region; for example take \(a=1/10\), \(b=9/10\), \(c_0=13/20\), and all middle opinions sufficiently close to \(1/2\). Initial openness refers to the region with \(c_0<\Delta\); equality is also allowed in the theorem.

Set \(q=(n-1)\delta\). In the non-repair regime \(0\leq q\leq1\), the exact endpoint gap and missing-edge bound are
\[
x_2(t)-x_1(t)=\frac{\Delta}{(n-1)^t},\qquad c_{12}(t)=c_0\delta^t\quad(t\geq0).
\]
The common limiting opinion in this regime is
\[
L=\frac{(n-1)(a+b)+n\sum_{j=3}^n x_j(0)}{n^2-2}.
\]
The limit effective graph has all edges except \(\{1,2\}\), although every opinion tends to \(L\); the missing confidence bound tends to \(0\) and the other confidence bounds tend to \(1\).

In the repair regime \(q>1\), let \(T\) denote the first receptive time of \(\{1,2\}\). Then
\[
T=\min\{t\in\mathbb Z_{\geq0}:q^t>\Delta/c_0\}
=\left\lfloor\frac{\log(\Delta/c_0)}{\log q}\right\rfloor+1.
\]
All \(n\) opinions are exactly equal at time \(T+1\), and all edges remain receptive thereafter. For fixed \(\Delta>c_0\), the exact repair time grows as \(T\sim\log(\Delta/c_0)/\log q\) when \(q\downarrow1\) through values greater than one.

## Proof
Define \(z_0=(n-2)^{-1}\sum_{j=3}^n x_j(0)\), which strictly lies between \(a\) and \(b\). While the only absent receptive edge is \(\{1,2\}\), the two endpoints each average themselves with all \(n-2\) intermediate opinions, while every intermediate agent averages the opinions of all \(n\) agents. Therefore the endpoints satisfy
\[
a_{t+1}=\frac{a_t+(n-2)z_t}{n-1},\qquad b_{t+1}=\frac{b_t+(n-2)z_t}{n-1},
\]
where \(z_t\) is the average of the intermediate opinions. Already at time \(1\) the intermediate agents all share their common opinion, and their next value is
\[
z_{t+1}=\frac{a_t+b_t+(n-2)z_t}{n}.
\]
These equations also hold from time \(0\) to time \(1\) for the mean \(z_0\). Subtracting gives \(b_{t+1}-a_{t+1}=(b_t-a_t)/(n-1)\). Direct subtraction also gives
\[
z_{t+1}-a_{t+1}=\frac{(n-1)(b_t-z_t)+(z_t-a_t)}{n(n-1)},
\]
\[
b_{t+1}-z_{t+1}=\frac{(n-1)(z_t-a_t)+(b_t-z_t)}{n(n-1)}.
\]
Whenever \(a_t<z_t<b_t\), both differences are positive and smaller than \((b_t-a_t)/n\). Since each intermediate initial opinion is within confidence \(c_0\) of both endpoints, \(\Delta<2c_0\). Hence \((b_t-a_t)/n\leq\Delta/n<c_0\), as \(n\geq3\). All intermediate–endpoint dyads are consequently receptive after each such update, and every intermediate–intermediate dyad is receptive because their opinions are then identical and their bounds remain at least \(c_0>0\). By induction all edges other than \(\{1,2\}\) stay receptive until (and after) that edge becomes receptive. As those bounds update by the increasing rule, they never fall below \(c_0\).

As long as the endpoint dyad is unreceptive, its confidence bound is \(c_0\delta^t\), whereas its opinion difference is \(\Delta/(n-1)^t\). If \(\delta=0\) the bound vanishes after the first step, making repair impossible. For \(\delta>0\), receptiveness at time \(t\) is exactly the strict inequality \(q^t>\Delta/c_0\). Because \(\Delta/c_0\geq1\), no such time exists when \(q\leq1\), including at equality \(q=1\); when \(q>1\), the first such time is the displayed integer \(T\). The same no-other-loss induction remains valid up to \(T\). At time \(T\) all dyads are receptive. Synchronous HK averaging then sets each opinion to the common arithmetic mean at time \(T+1\). Every edge stays receptive thereafter because the confidence bounds are positive at repair and are subsequently nondecreasing. This establishes the repair dichotomy and the exact switching-time formula.

If no repair occurs, the opinion evolution from time \(0\) onward is a fixed reversible, aperiodic row-stochastic averaging chain on the connected looped graph obtained from \(K_n\) by removing one edge. The averaging denominator (self plus neighbours) is \(n-1\) for vertices \(1,2\) and \(n\) for the other vertices. Detailed balance gives its stationary weights proportional to \((n-1,n-1,n,\ldots,n)\), whose sum is \(n^2-2\). Perron convergence therefore yields the asserted \(L\). At every finite time the two endpoint opinions differ by the positive quantity \(\Delta/(n-1)^t\), so finite-time agreement is impossible. Every active dyadic bound converges to one because \(\gamma>0\); the inactive bound converges to zero because \(\delta<1\). Thus the limit effective graph omits exactly the edge \(\{1,2\}\), despite global opinion consensus. Finally, the logarithmic lifetime law is immediate from the exact floor formula with \(\Delta/c_0>1\).

## Verification
The companion standalone script `verify_edge_repair.py` uses only Python's standard library and exact rational arithmetic. Run `python verify_edge_repair.py` to reproduce 69 rational tests across \(3\leq n\leq12\), including both sides and the equality case of the threshold, edge-state consistency, the invariant weighted average and the first repair time. These finite tests supplement the all-\(n\) proof; they do not establish the infinite-domain theorem on their own.

## Relationship to prior work
Li, Luo and Porter [1] introduce the precise synchronous adaptive-confidence HK equations, show convergence and eventual effective-graph stabilization in broad regimes, and report numerical examples in which agents with equal limiting opinions remain mutually unreceptive. Their paper does not identify the sharp \(1/(n-1)\) threshold, exact edge-repair time, or finite-time versus asymptotic consensus dichotomy on the one-missing-edge open set. Their discussion explicitly calls for further analytical understanding of mutual receptiveness at consensus. Kan, Feng and Porter [2] instead adapt the edges of an asynchronous Deffuant–Weisbuch model by rewiring, not the confidence thresholds of synchronous HK agents, and therefore their framework does not imply this result. Existing results about switching lifetimes in other proximity networks do not determine the adaptive dyadic-confidence threshold here.

## Limitations
This is a sharp classification only for the stated family on complete underlying graphs with a unique initially missing extreme pair and every other dyad initially receptive. It is not a global guarantee for arbitrary initial configurations, networks or other confidence update conventions. Finite-time consensus is exact mathematical equality, not a numerical-tolerance definition. Novelty was checked against accessible literature and related records, but mathematically equivalent unindexed work remains a residual possibility. No independent audit has been performed.

## References
[1] G. J. Li, J. Luo, M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563v1 (first posted 14 March 2023); *SIAM Journal on Applied Dynamical Systems* **24** (2025), 994–1041, doi:10.1137/23M1558951.

[2] U. Kan, M. Feng, M. A. Porter, *An Adaptive Bounded-Confidence Model of Opinion Dynamics on Networks*, arXiv:2112.05856 (2021).
