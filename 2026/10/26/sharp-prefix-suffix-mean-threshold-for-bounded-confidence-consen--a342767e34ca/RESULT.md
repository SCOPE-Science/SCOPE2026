# Sharp prefix–suffix mean threshold for bounded-confidence consensus on a path

## Finding
Let a finite path contain \(n\ge3\) agents with strictly increasing initial opinions \(a_1<\cdots<a_n\). Define the cut-centroid separation
\[
D_k=\frac{1}{n-k}\sum_{j=k+1}^{n}a_j-\frac1k\sum_{j=1}^{k}a_j,
\qquad \Theta=\max_{1\le k<n}D_k.
\]
For random asynchronous Deffuant compromise of strength \(0<\mu\le\tfrac12\), with *strict* confidence condition (a selected adjacent pair updates precisely when its gap is less than \(\varepsilon\)), the following is a complete classification of whether consensus has probability one.

1. If \(\varepsilon>\Theta\), consensus occurs almost surely.
2. If \(0<\varepsilon<\Theta\), there is a finite positive-probability sequence of edge selections that creates an irreversibly inactive path edge. The probability of eventual consensus is therefore strictly below one.
3. If \(\varepsilon=\Theta\), consensus occurs almost surely unless \(\mu=\tfrac12\) and one of the following holds: \(n=3\), or \(n=4\) and \(D_2=\Theta\). In precisely those exceptions a finite positive-probability edge-selection sequence freezes an edge permanently, so consensus has probability strictly below one.

For equally spaced \(a_j=a_1+(j-1)h\), every cut has \(D_k=nh/2\). Thus \(\Theta=nh/2=n(a_n-a_1)/(2(n-1))\). With opinions \(0,\tfrac1{n-1},\ldots,1\), the threshold is \(n/[2(n-1)]\). In particular, at equality, midpoint compromise can fragment paths of 3 or 4 agents, whereas all paths with at least 5 agents converge almost surely. Smaller compromise \(\mu<1/2\) makes every path with at least 3 agents converge almost surely at equality.

## Assumptions and scope
The graph consists **only** of path edges \(\{j,j+1\}\) for \(1\le j<n\). Every edge has an independent Poisson clock with a fixed positive finite rate, so any prescribed finite ordering of edge-ring events has positive probability. Opinions are scalar reals, initially strictly increasing, and never change except when a clock rings at a receptive edge. For a selected edge with gap \(d=x_{j+1}-x_j\ge0\), when \(d<\varepsilon\) the update is
\[
x'_j=x_j+\mu d,\qquad x'_{j+1}=x_{j+1}-\mu d,
\qquad0<\mu\le\tfrac12.
\]
When \(d\ge\varepsilon\), no opinions change. ``Consensus'' means all opinions converge to one common limit as time tends to infinity; it does not require equality at a finite time. ``Fragmentation'' means that at least one path cut becomes permanently nonreceptive with distinct conserved means on the two sides. No claim is made about the exact probability of fragmentation when it is positive.

The strict inequality is essential: changing the update convention to allow equality at the confidence bound changes the boundary-case conclusion. The result does not assume i.i.d. initial opinions, complete interaction graphs, synchronous updating, or fixed interaction weight \(\mu=1/2\) exclusively.

## Proof
**Order and frozen cuts.** The update is a convex symmetric averaging, so \(x_1\le\cdots\le x_n\) at every finite time. If at some time the gap \(d_k=x_{k+1}-x_k\) is at least \(\varepsilon\), that edge can never become receptive again: updates wholly on the left can only decrease its rightmost opinion \(x_k\), and updates wholly on the right can only increase its leftmost opinion \(x_{k+1}\). Consequently the two sides never exchange opinion mass afterward, and the difference of their conserved means is at least \(d_k\ge\varepsilon>0\). This prevents global consensus.

**Cut-centroid monotonicity.** For each cut \(k\), write
\[
\Delta_k(t)=\frac1{n-k}\sum_{j>k}x_j(t)-\frac1k\sum_{j\le k}x_j(t).
\]
Updates on any other edge leave \(\Delta_k\) unchanged. An effective update across edge \(k\) changes it by
\[
\Delta'_k-\Delta_k=-\mu (x_{k+1}-x_k)
\left(\frac1k+\frac1{n-k}\right)\le0.
\]
At every finite time, monotonicity of opinions gives \(0\le d_k\le\Delta_k(t)\le\Delta_k(0)=D_k\le\Theta\). Since initial opinions are strictly increasing and \(n\ge3\), each initial adjacent gap is strictly less than its own cut-centroid separation \(D_k\), and hence strictly less than \(\Theta\).

**Above the threshold.** If \(\varepsilon>\Theta\), every edge remains receptive under every clock history. The process is ordinary connected asynchronous symmetric averaging. To see almost-sure consensus without relying on a finite experiment, fix one full sweep of all path edges. Its product of averaging matrices strictly decreases Euclidean distance to the conserved global mean for every nonconstant vector. By compactness of the mean-zero unit sphere its contraction factor is uniformly below one. A fixed sweep occurs infinitely often in the independent edge-ring sequence almost surely, so variance tends to zero. Hence all opinions converge to their common initial mean.

**Below the threshold.** Choose a cut \(k\) attaining \(\Theta\). Prescribe an infinite periodic edge sequence visiting all edges except edge \(k\), and consider its successive finite prefixes. If any edge reaches gap at least \(\varepsilon\) at finite time, an irreversible fragmentation has been constructed. Otherwise every prescribed within-block update is performed, and ordinary connected averaging independently on both blocks forces each block to its own initial mean. The gap at the omitted cut must then tend to \(D_k=\Theta>\varepsilon\), a contradiction. Thus some finite prefix freezes an edge. Its prescribed edge-selection word has positive probability under positive-rate independent clocks, proving fragmentation has positive probability.

**Exactly at the threshold.** For an edge to reach \(d_k\ge\Theta\), the chain
\[
 d_k\le\Delta_k(t)\le D_k\le\Theta
\]
must consist entirely of equalities. Therefore \(D_k=\Theta\), no effective update has crossed this cut, and *both* blocks at the cut must already have become exactly homogeneous in finite time. Conversely, when both blocks are each of size at most two, midpoint compromise \(\mu=1/2\) can homogenize them by one averaging of each size-two block, without touching the cut, producing the exact frozen gap \(D_k=\Theta\).

To classify possible finite-time block homogeneity, consider a block of \(m\) initially strictly increasing opinions and its nonnegative adjacent-gap vector. If \(\mu<1/2\), each initially positive gap remains positive at every finite step, because updating its own edge multiplies it by \(1-2\mu>0\) and adjacent updates only add a nonnegative amount. If \(\mu=1/2\) and \(m\ge3\), a nonzero gap vector cannot become identically zero after a finite number of steps: averaging an edge with positive gap sets that gap to zero but deposits half its positive size into at least one neighboring gap. Updating a zero-gap edge changes nothing. Thus the only initially nonconstant blocks capable of becoming exactly homogeneous in finite time are blocks of size two, and only with midpoint compromise.

For \(n\ge5\), every cut has a block of size at least three, so no edge can reach the strict threshold \(\Theta\); for \(\mu<1/2\), the same conclusion holds for every \(n\ge3\). For \(n=3\), each cut has block sizes one and two, giving positive-probability freezing at any maximizing cut if \(\mu=1/2\). For \(n=4\), only cut \(k=2\) has both block sizes at most two; it can freeze if and only if \(D_2=\Theta\) and \(\mu=1/2\). In all remaining cases no cut ever becomes nonreceptive, and the sweep argument gives almost-sure consensus. This proves the classification.

## Verification
The bundled standalone `verify.py` uses exact rational arithmetic to check cut-centroid nonincrease, ordered trajectories, global gap envelopes, positive-probability freezing words below the threshold, and explicit exceptional equality witnesses. It reports more than one million exact assertions on rational initial profiles and compromises. All unrestricted-\(n\) assertions above are proved analytically; finite checking is only corroboration.

As transparent examples, for initial opinions \((0,\tfrac12,1)\) the critical confidence is \(\Theta=\tfrac34\); one midpoint update on either path edge freezes the other at equality. For \((0,\tfrac13,\tfrac23,1)\), \(\Theta=\tfrac23\), and first averaging the two external edges freezes the central edge at equality. For \((0,\tfrac14,\tfrac12,\tfrac34,1)\), \(\Theta=\tfrac58\), but no finite sequence can freeze any path edge at equality; ordinary asynchronous averaging converges almost surely.

To reproduce computational checks, run `python verify.py` using Python 3 standard library only. The script's `Fraction` operations perform the calculations without floating-point rounding.

## Relationship to prior work
Dubovskaya, Fennell, Burke, Gleeson and O'Kiely (arXiv:2210.07167, DOI 10.1137/22M1499765) analyze mean-field Deffuant equations, confidence-dependent clustering and linear stability, using the same strict confidence and midpoint convention. Their object is a population density / degree-class approximation rather than a finite ordered path with a fixed deterministic initial profile and exact probability-one threshold.

Lanchier and Li (arXiv:2005.13141) give a topology-uniform lower bound for consensus probability on finite connected graphs, from i.i.d. initial opinions, and prove convergence to cluster configurations. Their interaction convention accepts **equality** at the confidence threshold, in contrast to the strict boundary rule here; their bound does not supply this deterministic-profile sharp path cutoff or the exceptional small-size equality classification.

Zhang, Yuan, Wang, Altafini and Shi (arXiv:2107.04948) study clique-mean bounded confidence updates and possible nonconvergence. Group-pressure updating is not the two-endpoint symmetric exchange used here. Classical connected randomized-gossip convergence supplies a standard ingredient; the cut-centroid sharpness, constructive nonconsensus converse and equality-case classification are the specific claims advanced here.

## Limitations
The claim is restricted to finite paths, strictly ordered deterministic scalar initial data, fixed positive edge activation rates, and symmetric nonexpansive pairwise compromise. For nonmonotone starting data, nonpath graphs, adaptive confidence, or unilateral averaging, the order and cut-centroid arguments do not apply without additional work. The result distinguishes probability one from probability strictly below one but does not calculate the latter. General literature on deterministic-profile finite-gossip thresholds may use alternative names for a related invariant; priority should be independently checked before publication.

## References
Dubovskaya, A., Fennell, S. C., Burke, K., Gleeson, J. P., and O'Kiely, D., *Analysis of Mean-Field Approximation for Deffuant Opinion Dynamics on Networks*, arXiv:2210.07167v1 (2022), SIAM J. Appl. Math. 83 (2023), 436–459, DOI 10.1137/22M1499765.

Lanchier, N., and Li, H.-L., *Probability of consensus in the multivariate Deffuant model on finite connected graphs*, arXiv:2005.13141v1 (2020).

Zhang, J., Yuan, D., Wang, L., Altafini, C., and Shi, G., *Dynamics of Opinions with Bounded Confidence in Social Cliques: Emergence of Fluctuations*, arXiv:2107.04948v1 (2021).
