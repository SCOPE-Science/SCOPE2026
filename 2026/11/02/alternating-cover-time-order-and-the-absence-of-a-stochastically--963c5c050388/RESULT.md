# Alternating cover-time order and the absence of a stochastically optimal two-walker placement

## Finding

For each integer \(n\ge2\), run two **independent synchronous, non-lazy simple random walks** on the complete bipartite graph \(K_{n,n}\). Count the starting vertices as visited, and let \(T_S\) be the first time that the union of their visited sets covers all vertices when they start at two **distinct vertices in the same part**. Let \(T_D\) be the corresponding cover time when they start in **different parts**. For \(\rho=(n-1)/n\), as integer \(s\to\infty\),

\[
\frac{\Pr(T_D\le 2s)-\Pr(T_S\le 2s)}{\rho^{4s}}\longrightarrow1,
\qquad
\frac{\Pr(T_S\le 2s+1)-\Pr(T_D\le 2s+1)}{\rho^{2s}}\longrightarrow\frac1n.
\]

Furthermore, \(\Pr(T_S\le2s+1)>\Pr(T_D\le2s+1)\) whenever \(2s\ge n-2\). Thus, for every \(n\ge2\), the two distributions have infinitely many alternating strict CDF crossings. **No deterministic or randomized initial placement of two walkers on \(K_{n,n}\) stochastically minimizes their full cover time among all initial placements.** The comparison concerns first-order stochastic order, not the means.

## Assumptions and scope

The graph has two parts \(A,B\), each of cardinality \(n\). Every walker, simultaneously at each integer time, chooses a uniform neighbor independently of the other walker and of all previous choices. There is no holding probability, no communication and no adaptive control. A configuration of initial positions is fixed before the walks start; randomizing it means taking an arbitrary probability mixture of such configurations. A cover time \(T\) includes observations at times \(0,1,\ldots,T\). The assertion is for **fixed \(n\)** with time tending to infinity, not for a joint scaling of \(n\) and time.

For integers \(m\ge0\), \(0\le c\le n\), define the coupon-coverage function

\[
U_{n,c}(m)=\sum_{j=0}^{n-c}(-1)^j\binom{n-c}{j}\left(1-\frac jn\right)^m.
\]

This is the probability that \(m\) independent uniform samples of \(n\) sites, added to \(c\) *specified distinct sites already observed*, cover every site. In particular, \(U_{n,2}\) requires \(n\ge2\). We adopt the usual convention \(0^0=1\) in finite inclusion-exclusion sums.

## Proof

**Step 1: exact marginal distribution formulas.** Since the graph is complete bipartite, each move from \(A\) chooses an independent uniform site of \(B\) and conversely. The two streams of sampled sites in the two parts are mutually independent, even after accounting for the walks' alternating parts. Set \(m=2s\). In placement \(D\), both parts have one previsited site and receive exactly \(t\) fresh uniform samples by time \(t\), so

\[
\Pr(T_D\le t)=U_{n,1}(t)^2.
\]

In placement \(S\), one part has two previsited sites, the other none. At time \(2s\) both parts have received \(2s\) samples; at \(2s+1\), the initially unvisited part has received \(2s+2\) samples, while the other has received \(2s\). Hence

\[
\begin{aligned}
\Pr(T_S\le2s)&=U_{n,0}(2s)U_{n,2}(2s),\\
\Pr(T_S\le2s+1)&=U_{n,0}(2s+2)U_{n,2}(2s).
\end{aligned}
\]

**Step 2: exact strict odd-time inequality.** By revealing one independent uniform coupon, the identities

\[
U_{n,0}(m+1)=U_{n,1}(m),\qquad
U_{n,1}(m+1)=\frac1nU_{n,1}(m)+\frac{n-1}{n}U_{n,2}(m)
\]

hold for all \(m\ge0\). Substituting and rearranging yields

\[
\Pr(T_S\le2s+1)-\Pr(T_D\le2s+1)
=\frac{U_{n,1}(2s+1)\bigl(U_{n,1}(2s+1)-U_{n,1}(2s)\bigr)}{n-1}.
\]

The distribution of the finite coupon-collection completion time has strictly positive probability at every integer \(m\ge n-1\); to see this, visit the \(n-2\) needed new sites before the last missing site, with arbitrary intervening repeats. Therefore the displayed difference is positive for \(2s\ge n-2\). Define \(\rho=1-1/n\) and \(q=1-2/n\). Inclusion-exclusion gives \(U_{n,1}(m)=1-(n-1)\rho^m+O_n(q^m)\), where at \(n=2\) the error vanishes after a finite time. Consequently the odd difference equals \(\frac1n\rho^{2s}(1+o(1))\).

**Step 3: eventual strict even-time inequality and its sharp rate.** For fixed \(n\), inclusion-exclusion also gives, uniformly for \(c=0,1,2\),

\[
U_{n,c}(m)=1-(n-c)\rho^m+\binom{n-c}{2}q^m+O_n(r^m),
\]

where \(r=\max\{0,1-3/n\}\), and the error is absent when \(n\le3\). Expanding \(U_{n,1}(m)^2-U_{n,0}(m)U_{n,2}(m)\), the constant and \(\rho^m\) terms cancel, while the coefficient of \(\rho^{2m}\) is exactly

\[
(n-1)^2-n(n-2)=1.
\]

All remaining terms decay at rate at most \(q^m\), since the largest one-factor base after \(\rho\) is \(q\), and mixed products are no larger. Thus

\[
U_{n,1}(m)^2-U_{n,0}(m)U_{n,2}(m)
=\rho^{2m}+O_n(q^m).
\]

Because \(0\le q<\rho^2\), division by \(\rho^{2m}\) tends to 1. With \(m=2s\), this proves the even-time limit and eventually strictly favors \(D\). In the boundary case \(n=2\), the formula is in fact exact: the even-time difference is \(\rho^{4s}\) for every \(s\ge1\).

**Step 4: no stochastic best placement.** Up to part-exchanging automorphisms, a pair of initial vertices has only three configurations: different parts, distinct vertices in one part, or both walkers at one vertex. The last is weakly stochastically dominated by distinct same-part starts: couple all *future* uniform transitions identically, possible because a transition depends only on the part, and the distinct-start visited set initially contains the collocated-start set. Strictly alternating superiority between \(S\) and \(D\) rules out either as a first-order-stochastic minimum. Any random initial placement yields a convex mixture of these three cover-time distribution functions. At a sufficiently large even time, \(D\) strictly maximizes the CDF among the three, forcing a hypothetical stochastically optimal mixture to put probability one on \(D\); at a sufficiently large odd time \(S\) strictly beats \(D\), a contradiction.

## Verification

The standalone `checker.py` verifies 1,171 exact-rational identities or probability comparisons. In particular, a full Markov-state enumeration independently reproduces the formulas for \(n=2,3,4\) at the checked time horizons; computations also confirm the odd-time identity and eventual even-time signs over several finite \(n\). As an explicit check, on \(K_{2,2}\), at time \(1\) the cover probabilities under \(S,D\) are \(1/2,1/4\), respectively; at time \(2\) they are \(1/2,9/16\). The infinite-family assertions rely on the preceding symbolic proof, not on exhaustive finite testing. Reproduce with `python3 checker.py` in a Python 3 environment.

## Relationship to prior work

Alon et al., *Many Random Walks Are Faster Than One* (arXiv:0705.0467, 2007), investigate multi-walker cover times chiefly from collocated starts and establish speed-up bounds. Rivera, Sauerwald and Sylvester, *Multiple Random Walks on Graphs: Mixing Few to Cover Many* (arXiv:2011.07893, first submitted 2020-11-16), give general bounds and detailed comparisons of stationary and worst-case expected cover times, explicitly motivating finer analyses of initial placement. The latter source supplies the primary dated context for this result and identifies MSC \(60J10\) among its mathematical classifications. The present claim is a fixed-graph, full-distribution comparison: neither broad expectation bounds nor the one-walker coupon-collector formula decides an infinite sequence of crossings. The primary source texts inspected did not state this complete-bipartite two-start theorem. Absence of a matching statement in searches is not a proof of historical novelty.

## Limitations

The theorem is confined to two independent synchronous **non-lazy** walkers and balanced complete bipartite graphs, with initial vertices counted at time zero. It does not establish which placement minimizes *expected* cover time, and it does not settle stochastic-optimal starts on non-bipartite graphs, more walkers, or arbitrary Markov chains. The asymptotic limits fix graph size before letting time grow. An independent mathematical audit and an exhaustive historical-priority review have not been performed.

## References

1. N. Alon, C. Avin, M. Koucký, G. Kozma, Z. Lotker, M. R. Tuttle. *Many Random Walks Are Faster Than One*. arXiv:0705.0467, first posted 2007-05-03. https://arxiv.org/abs/0705.0467
2. N. Rivera, T. Sauerwald, J. Sylvester. *Multiple Random Walks on Graphs: Mixing Few to Cover Many*. arXiv:2011.07893, first posted 2020-11-16; published in *Combinatorics, Probability and Computing* 32 (2023), 594–637. https://arxiv.org/abs/2011.07893
