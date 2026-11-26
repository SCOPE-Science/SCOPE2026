# Exact covariances with higher-order crossings and nestings in random matchings

## Finding

Let \(M\) be a uniform perfect matching of the linearly ordered set \([2n]\), \(n\ge3\). Let \(C_r\) and \(N_r\) count, respectively, the subsets of \(r\) arcs that are mutually crossing and those that are completely nested. An arc is written from its smaller to its larger endpoint. In either pattern all the left endpoints precede all the right endpoints; the right endpoints occur in the same order for a crossing and in reverse order for a nesting. Set \(p_r=1/(2r-1)!!\). Then for \(3\le r\le n\),

\[
\mathbb E C_r=\mathbb E N_r=\binom nr p_r,\qquad
\operatorname{Cov}(C_2,N_r)=-\binom nr p_r\frac{r(r-1)}6.
\]

For comparison the crossing covariance, in all these orders, is
\[
\operatorname{Cov}(C_2,C_r)=\binom nr p_r\frac{r(r-1)(n+r+1)}{3(2r+1)}.
\]

Thus the two covariances have strictly opposite signs. The nesting covariance for \(r=3\) is \(-\binom n3/15\). The contribution is the all-order nesting formula, including the exact cancellation for pairs sharing just one arc, and the all-order sign comparison. The \(r=3\) crossing covariance is an existing edge–triangle identity and is included only for comparison; the formula extends that comparison to \(r\ge4\).

## Assumptions and scope

The probability measure is uniform on the \((2n-1)!!\) perfect matchings, and crossing means that two pairs of endpoints alternate. The variables count subsets of arcs, not the maximum crossing or nesting order. For \(N_r\), noncrossing subsets that are not completely nested do not count.

## Proof

Give each of the \(n\) labeled arcs two independent uniform endpoints in \((0,1)\). Rank all endpoints and forget the labels: each matching has exactly \(2^n n!\) labeled rank orders, so the matching is uniform. For a fixed set \(S\) of \(r\) labels, the induced pairing on its \(2r\) endpoints is likewise uniform. Exactly one ranked pairing realizes each pattern, giving \(p_r\) and the two means. A prescribed pair crosses with probability \(1/3\).

Condition on either pattern on \(S\). For an arc of \(S\) with endpoint rank difference \(d\), an independent outside arc crosses it if exactly one outside endpoint lies between its endpoints. The \(\binom{2r+2}{2}\) choices of the two outside ranks in the combined order are equally likely, independently of the labeled order on \(S\). There are \(d\) gaps between the inside arc's endpoints and \(2r+1-d\) gaps outside, so the conditional probability is
\[
\frac{d(2r+1-d)}{\binom{2r+2}{2}}.
\]
For a complete crossing all gaps in rank are \(d=r\), giving \(r/(2r+1)\). For a complete nesting they are \(d_j=2r+1-2j\), \(1\le j\le r\). Label symmetry places each distinguished arc uniformly among the nesting ranks. Since \(\sum_{j=1}^r (2r+1-2j)(2j)=r(r+1)(2r+1)/3\), the average crossing probability in the nesting case is exactly \(1/3\).

In the covariance with the pattern indicator on \(S\), a crossing pair disjoint from \(S\) contributes zero by independence. There are \(r(n-r)\) pairs sharing one label with \(S\). Their contributions per pair are \(p_r[r/(2r+1)-1/3]\) in the crossing case and zero in the nesting case. The \(\binom r2\) contained pairs are forced to cross in the crossing case and forced not to cross in the nesting case; their contributions per pair are \(2p_r/3\) and \(-p_r/3\), respectively. Sum over all \(\binom nr\) sets \(S\). In the crossing case the bracket simplifies to \(r(r-1)(n+r+1)/(3(2r+1))\); in the nesting case it is \(-r(r-1)/6\). These expressions are nonzero with opposite signs, including at \(r=n\) when there are no one-label overlaps.

## Verification

The accompanying `verify.py` checks exact rational means and covariances by enumeration for \(3\le n\le6\) and every \(3\le r\le n\). These finite checks are supplementary; the overlap decomposition proves the formulas for all stated parameters.

## Relationship to prior work

- [An exact edge–triangle correlation gap in random chord intersection graphs](https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-an-exact-edge-triangle-correlation-gap-in-random-chord-intersect--7b9f44348870) gives \(\operatorname{Cov}(X_n,T_n)=n(n-1)(n-2)(n+4)/315\), where \(X_n=C_2\) and \(T_n=C_3\). This is exactly the \(r=3\) crossing formula above; it is not part of the new claim. The overlap calculation here treats arbitrary crossing order and, crucially for the sign comparison, complete nesting, which is not identifiable from an independent set in the intersection graph alone.
- Chen, Deng, Du, Stanley and Yan, [*Crossings and Nestings of Matchings and Partitions*](https://arxiv.org/abs/math/0501230), study the symmetry of the maximum crossing and nesting orders. That symmetry does not give the covariances of the subset counts considered here.
- Kasraoui and Zeng, [*Distribution of crossings, nestings and alignments of two edges in matchings and partitions*](https://arxiv.org/abs/math/0601081), study joint distributions of the two-arc statistics. No novelty is claimed here for \(r=2\).
- Acan, [*On a uniformly random chord diagram and its intersection graph*](https://arxiv.org/abs/1501.01489), relates crossings to cliques and nests to a subset of the independent sets. First moments and maximum pattern sizes do not provide the two displayed cross-covariances.

## Limitations

This is an exact covariance calculation for uniform perfect matchings and the two specified patterns. It does not give their joint distribution, concentration bounds, or results for partial or weighted matchings. The comparison with identified precedents does not establish absolute priority for the formulas outside the known cases.
