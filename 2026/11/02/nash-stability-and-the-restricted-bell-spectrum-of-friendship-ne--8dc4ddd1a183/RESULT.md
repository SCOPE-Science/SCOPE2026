# Nash stability and the restricted-Bell spectrum of friendship networks

## Finding

**Theorem.** For every integer \(m\ge 1\), let \(F_m=K_1\vee (mK_2)\) be the friendship graph: a hub \(h\) joined to both endpoints of each of \(m\) mutually disjoint edges (called petals). In the standard simple symmetric fractional hedonic game, a coalition structure is Nash stable **if and only if** the hub's coalition consists of \(h\) and exactly \(s\) complete petals for some \(1\le s\le m\), while the other \(m-s\) complete petals are partitioned into blocks of at most \(s\) petals each. Thus no petal can be split in a Nash-stable partition.

Let \(S_{\le s}(t,\ell)\) denote the number of partitions of \(t\) labeled objects into \(\ell\) unlabeled nonempty blocks of size at most \(s\), and let \(B_{t}^{(\le s)}\) be their sum over \(\ell\). Then the exact Nash-stable count and its joint refinement by hub-petal number and outside-coalition number are

\[
N_m=\sum_{s=1}^{m}\binom{m}{s} B_{m-s}^{(\le s)},\qquad
N_m(s,\ell)=\binom{m}{s}
S_{\le s}(m-s,\ell).
\]

The welfare of every partition in the second class is exactly

\[
W(s,\ell)=\frac{6s}{2s+1}+\ell.
\]

Here \(\ell=0\) is required when \(s=m\); otherwise all integer values \(\lceil (m-s)/s\rceil\le\ell\le m-s\) occur. The unconstrained optimal welfare is \(m+1\), attained by exactly \(m\) partitions, all Nash stable. The unique welfare-worst Nash-stable partition is the grand coalition, with welfare \(6m/(2m+1)\). Therefore

\[
\operatorname{PoS}(F_m)=1,\qquad
\operatorname{PoA}(F_m)=\frac{(m+1)(2m+1)}{6m}.
\]

In particular the price of anarchy grows linearly with \(m\) although the graph is a connected block graph of diameter two. The first Nash-stable counts for \(m=1,2,3,4,5\) are \(1,3,7,21,71\), respectively.

## Assumptions and scope

All \(2m+1\) vertices are distinct strategic agents. The graph is simple, undirected, and unweighted; the unique nonzero pairwise valuations are \(w_{uv}=1\) on edges. A coalition structure \(\pi\) is any set partition of vertices, without a connectivity restriction. For \(v\) in coalition \(C\), utility is exactly

\[
u_v(C)=\frac{|N(v)\cap C|}{|C|}.
\]

The denominator **includes the agent**. A unilateral Nash deviation moves one agent into another existing coalition or into a new singleton coalition, without veto by the destination coalition, and must **strictly** improve the mover's utility. Welfare is \(\sum_v u_v(\pi(v))\). The price-of-anarchy and price-of-stability ratios have the optimum welfare in their numerator. These definitions differ from modified fractional hedonic games, which divide by one fewer coalition member, and from additive social-distance games.

## Proof

**1. Petals cannot split in equilibrium.** If the endpoints \(a,b\) of one petal occupy distinct coalitions, at least one of them is not with the hub. That endpoint has no friend in its current coalition (its only neighbors are its mate and the hub), hence utility zero. Moving into the mate's coalition gives a strictly positive payoff, contradicting Nash stability. Therefore every petal's endpoints share a coalition. If the hub were alone, joining the coalition of any complete petal would give it positive utility, also contradicting stability. Consequently its coalition contains the hub and \(s\ge 1\) complete petals.

**2. Exactly one stability inequality survives.** Each of the \(s\) hub-coalition petals contributes two hub edges and one mate edge. The hub's utility is \(2s/(2s+1)\), and each of its petal agents gets \(2/(2s+1)\). An outside coalition containing \(t\ge1\) entire petals has size \(2t\), and each member gets \(1/(2t)\). If the hub joins that outside coalition its new utility is \(2t/(2t+1)\), a strict improvement precisely when \(t>s\). An outside petal agent joining the hub coalition would receive \(1/(2s+2)\), improving over \(1/(2t)\) precisely when \(t>s+1\). All other unilateral moves gain zero friend edges, and joining a singleton gives zero. Therefore there are no profitable unilateral deviations if and only if every outside block has \(t\le s\) petals. This proves necessity and sufficiency of the characterization, including ties at \(t=s\).

**3. Exact enumeration and welfare layers.** Choose the \(s\) hub petals in \(\binom ms\) ways, and partition the \(m-s\) remaining labeled petals into unlabeled blocks of size at most \(s\). The exact restricted Stirling numbers satisfy

\[
S_{\le s}(t,\ell)
=t!\sum_{\substack{\sum_{j=1}^{s}j c_j=t\\\sum_{j=1}^{s}c_j=\ell}}
\prod_{j=1}^{s}\frac{1}{(j!)^{c_j}c_j!}.
\]

Every outside coalition contributes welfare \(2t/(2t)=1\), independently of its block size; the hub coalition contributes \(2(3s)/(2s+1)\). Thus the exact welfare layer is \(6s/(2s+1)+\ell\). All feasible block-count values are attained because \(\ell\) positive integers between one and \(s\) can sum to \(m-s\) exactly when \(\ell\le m-s\le s\ell\).

**4. Unrestricted optimal welfare.** Consider an arbitrary partition, not assumed stable. Suppose the hub coalition contains \(s\) complete petals and \(r\) single endpoints whose mates lie outside. Its size is \(2s+r+1\) and it contains exactly \(3s+r\) graph edges, contributing welfare \(2(3s+r)/(2s+r+1)\). Of the remaining vertices only \(m-s-r\) complete petals can contribute an internal edge. Each outside coalition contributes welfare at most one: if it has \(t\) intact petals and \(z\) other endpoints, its welfare is \(2t/(2t+z)\le1\). Therefore overall welfare is bounded by

\[
W(\pi)\le m-s-r+\frac{2(3s+r)}{2s+r+1}.
\]

When \(s+r=0\) this is at most \(m\); when \((s,r)=(0,1)\) it is at most \(m\); when \((s,r)=(1,0)\) it is at most \(m+1\), with equality exactly if each other complete petal forms its own two-agent coalition; and when \(s+r\ge2\), the hub-coalition welfare is strictly below three, giving strictly less than \(m+1\). Thus the unique optimizer shapes consist of one complete triangle containing the hub and each other petal in its own pair coalition; there are exactly \(m\) labeled choices. Each optimizer is Nash stable by step 2, proving \(\operatorname{PoS}=1\).

**5. Worst equilibrium.** For \(s=m\), the grand coalition is Nash stable and has welfare \(6m/(2m+1)<3\). If \(s<m\), there is at least one outside coalition, so \(W(s,\ell)\ge 6s/(2s+1)+1\ge3\), with equality possible only for \(s=1\). Therefore the grand coalition is the unique welfare-minimizing equilibrium, proving the price-of-anarchy expression.

## Verification

The standalone \(\texttt{verify.py}\) enumerates every labeled coalition partition for \(m=1,2,3,4,5\), independently computes every agent's utility and every possible strict move by integer cross-multiplication, and compares the Nash counts and welfare extrema with the stated formulas. It evaluates \(700651\) complete partitions in total and passes all assertions, including the number of unrestricted optima and the uniqueness of the welfare-worst Nash partition. Run with `python verify.py` under Python 3 with no external dependencies. Exhaustive finite calculations are corroboration; the proof above establishes every integer \(m\ge1\).

## Relationship to prior work

Hanaka, Ikeyama and Ono (2023) give a general polynomial-time algorithm for utilitarian welfare maximization on unweighted block graphs and show that an optimal block-graph partition may be chosen with clique/star coalitions. Their theorem can address the optimum value on this graph but does not supply the exact Nash-stable structures, restricted Bell multiplicities, or equilibrium-by-equilibrium welfare spectrum. Bilò, Fanelli, Flammini, Monaco and Moscardelli (2018) establish general Nash existence for nonnegative fractional hedonic games, broad welfare bounds and results for other graph families; these general statements do not determine the exact friendship-graph enumeration. The earlier basic fraction-utility definition of Aziz and coauthors is retained unchanged. The present theorem is an explicit family-level classification, not a claim of general hardness, general algorithmic improvement or independent priority certification.

## Limitations

The claims require exactly triangular petals sharing one hub, unit symmetric friend weights, the self-inclusive utility denominator, unrestricted coalition connectivity, and strict unilateral Nash deviations. They need not extend to generalized windmills with larger petals, modified fractional hedonic games, weighted edges, group deviations, or coalitions required to be connected. The external novelty comparison is evidence-based rather than a formal proof of exhaustive publication priority; uncatalogued or uninspected specialist literature remains a residual risk.

## References

1. T. Hanaka, A. Ikeyama and H. Ono, *Maximizing Utilitarian and Egalitarian Welfare of Fractional Hedonic Games on Tree-like Graphs*, arXiv:2310.05139, first public version 2023-10-08, https://arxiv.org/abs/2310.05139.
2. V. Bilò, A. Fanelli, M. Flammini, G. Monaco and L. Moscardelli, *Nash Stable Outcomes in Fractional Hedonic Games: Existence, Efficiency and Computation*, Journal of Artificial Intelligence Research **62** (2018), 315–371, https://doi.org/10.1613/jair.1.11211.
3. H. Aziz, F. Brandl, F. Brandt, P. Harrenstein, M. Olsen and D. Peters, *Fractional Hedonic Games*, arXiv:1705.10116, https://arxiv.org/abs/1705.10116.
