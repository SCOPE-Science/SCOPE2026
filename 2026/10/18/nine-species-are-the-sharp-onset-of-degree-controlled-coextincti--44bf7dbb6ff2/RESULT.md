# Nine species are the sharp onset of degree-controlled coextinction-variance reversals

## Finding

Consider a simple bipartite incidence network with \(m\ge1\) plant species, \(n\ge1\) pollinator species, no isolated vertices, and no other ecological interactions. Each pollinator independently disappears with the same probability \(q\in(0,1)\). A plant is counted as secondarily extinct precisely when *all* its pollinators disappear. Let \(Z_G(q)\) be the number of secondarily extinct plants in network \(G\).

Two networks are **degree-matched** when they have the same numbers of plants and pollinators and the same *multisets* of degrees on both sides of the bipartition. Consequently their mean plant extinction counts agree for every \(q\).

**Sharp threshold.** If \(m+n\le8\), for every degree-matched pair \(G,H\), the sign of
\[
\operatorname{Var}(Z_G(q))-\operatorname{Var}(Z_H(q))
\]
is constant or zero as \(q\) ranges over \((0,1)\). At total order \(m+n=9\), even when both networks are connected, the sign can reverse exactly once.

The connected witness has four plants and five pollinators. With pollinators labeled \(a,b,c,d,e\), the four plant neighborhoods are
\[
G:\quad \{a\},\ \{a,b\},\ \{b,c,d\},\ \{b,c,e\},
\]
\[
H:\quad \{a\},\ \{b,c\},\ \{a,b,c\},\ \{a,d,e\}.
\]
Both plant-degree multisets are \((1,2,3,3)\), and both pollinator-degree multisets are \((1,1,2,2,3)\). For every \(q\in(0,1)\),
\[
\mathbb E Z_G(q)=\mathbb E Z_H(q)=q+q^2+2q^3,
\]
whereas
\[
\boxed{\operatorname{Var}(Z_G(q))-\operatorname{Var}(Z_H(q))
=2q^2(1-q)^2(1-2q).}
\]
Thus \(G\) has higher variance for \(0<q<1/2\), the variances tie at \(q=1/2\), and \(H\) has higher variance for \(1/2<q<1\). For example, at \(q=1/4\) the variance pair is \((399/1024,363/1024)\); at \(q=3/4\) it is \((1839/1024,1875/1024)\).

## Assumptions and scope

All bipartite graphs are finite, simple, and have no isolated vertices; vertices within each guild may be relabeled. All pollinator losses are mutually independent and identically distributed. Plants require at least one surviving pollinator, without demographic feedback, compensatory rewiring, or cascading secondary losses among pollinators. The random variable counts plant species, not abundance or ecosystem function. Degree matching requires both guilds' multisets, not merely common connectance or total edge count. The minimality assertion holds even if disconnected competitors are permitted; the first witness happens to be connected.

## Proof

For each plant \(i\), write \(N_i\) for its nonempty set of neighboring pollinators and \(d_i=|N_i|\). Its extinction indicator \(I_i\) satisfies \(\Pr(I_i=1)=q^{d_i}\). For distinct plants, both die exactly when the union of their pollinators disappears. Independence therefore gives
\[
\operatorname{Cov}(I_i,I_j)
=q^{|N_i\cup N_j|}-q^{d_i+d_j},
\]
and hence the exact identity
\[
\operatorname{Var}(Z_G(q))=
\sum_i q^{d_i}(1-q^{d_i})+
2\sum_{i<j}\left(q^{|N_i\cup N_j|}-q^{d_i+d_j}\right).
\tag{1}
\]
The expected count \(\sum_iq^{d_i}\) depends only on plant degrees. For a degree-matched pair, all terms of (1) except the positive union-size terms cancel. Put
\[
h_k(G)=\#\{\{i,j\}:i<j,\ |N_i\cup N_j|=k\}.
\]
Then
\[
\operatorname{Var}(Z_G(q))-\operatorname{Var}(Z_H(q))
=2\sum_{k=0}^n \big(h_k(G)-h_k(H)\big)q^k.
\tag{2}
\]
Call the polynomial on the right without the factor two \(F(q)\). Since all plant neighborhoods are nonempty, \(F(0)=0\). Since both histograms have \(\binom m2\) pairs, \(F(1)=0\). Moreover,
\[
\sum_{i<j}|N_i\cup N_j|
=(m-1)\sum_i d_i-\sum_{a=1}^n\binom{c_a}{2},
\]
where \(c_a\) are pollinator degrees. Degree matching implies \(F'(1)=0\). Consequently
\[
F(q)=q(1-q)^2Q(q),\qquad \deg Q\le n-3,
\tag{3}
\]
with the zero-polynomial convention when the degree bound is negative.

When \(m\le2\), the pair-union histogram is determined by the degrees on both sides: for two plants the intersection size equals the number of degree-two pollinators. Therefore the variance curves of degree-matched networks coincide. When \(n\le3\), (3) makes \(Q\) constant or zero, so the variance difference cannot change sign in \((0,1)\).

With \(m+n\le8\), the only remaining possible bipartition sizes (plants, pollinators) are \((3,4),(4,4),(3,5)\). A complete finite classification enumerates every ordered \(m\)-tuple of nonzero \(n\)-bit pollinator-neighborhood masks, discards tuples with an unused pollinator, groups incidence matrices by the two sorted degree multisets, and records their possible pair-union histograms. For each distinct pair of histograms in one group, sort the histogram tuples lexicographically and compute its difference quotient \(Q=F/[q(1-q)^2]\). The **entire** possible set of nonzero quotient coefficient tuples (in ascending powers) is:

| Plants, pollinators | Nonzero quotient tuples \((Q_0,Q_1,\ldots)\) | Matrices; degree groups; histogram comparisons |
|---|---|---|
| \((3,4)\) | \((0,-1),(-1,-1)\) | \(2161;33;5\) |
| \((4,4)\) | \((0,-1),(0,-2),(-1,-1),(-1,0),(-1,1),(-2,-2),(-1,-2)\) | \(41503;103;48\) |
| \((3,5)\) | \((0,0,-1),(0,-1,-1),(-1,-1,-1),(0,-1,0),(0,-1,-2)\) | \(16081;64;17\) |

Every listed \(Q\) is strictly negative for \(q\in(0,1)\). In particular, the only tuple with a positive coefficient is \((-1,1)\), representing \(-(1-q)<0\). Reversing the histogram order only reverses the sign; it never creates a crossing. The enumeration is exhaustive because there are exactly \((2^n-1)^m\) nonzero-row labeled incidence matrices before excluding unused pollinators, and the total with all columns used is independently checked by inclusion-exclusion:
\[
\sum_{j=0}^n(-1)^j\binom nj(2^{n-j}-1)^m.
\tag{4}
\]
The accompanying executable reproduces the table, applies (4), and verifies the exact polynomial divisions. This proves impossibility through eight total species.

For the nine-species witness, the six unordered plant-pair union sizes are
\[
G:(2,4,4,4,4,4),\qquad H:(3,3,3,3,5,5).
\]
Substituting these into (2) gives
\[
2(q^2-4q^3+5q^4-2q^5)=2q^2(1-q)^2(1-2q),
\]
so the strict sign reversal is exact. An inspection of the nonzero incidences shows that both graphs are connected. This proves the sharp threshold.

## Verification

Run `python3 verify_coextinction_variance.py` with Python 3 (standard library only). The program exhaustively enumerates the three residual small bipartition sizes, checks the independent inclusion-exclusion matrix counts, computes every degree-matched histogram comparison, and checks the short exact quotient lists above. It separately evaluates all \(2^5=32\) pollinator-failure subsets of each witness graph using rational arithmetic and verifies their first and second moments against (1). Actual replay produced \(2161,41503,16081\) incidence matrices, respectively, with \(5,48,17\) histogram comparisons, and all checks passed. No sampling, floating-point root tests, or truncated search is used for the finite claims.

## Relationship to prior work

Memmott, Waser, and Price (2004) study simulated removal of pollinators and resulting secondary losses of plants under the rule that a plant disappears after its final pollinator disappears. The present exact independent-loss model is a probability-parameter version of that simple topological extinction rule. Their paper analyzes decline curves and ecological redundancy, not an exact comparison of second moments for identical degree multisets.

Campbell, Yang, Shea, and Albert (2012) investigate fragility, nestedness, and degree-controlled network features in a more elaborate dynamic Boolean model. Their degree-preserving null-model comparisons do not imply (2) or the nine-species minimality theorem. Bane and coauthors (2018) study distributions of a different cumulative robustness statistic under sequential knockouts and changing failure thresholds; that reported change of rankings is not a statement about the instantaneous variance \(\operatorname{Var}(Z(q))\) of this independent-loss process. These are non-equivalent models and observables.

## Limitations

This is a sharp theorem within one precisely defined, static and independent-loss model. It does not assert that nine species is the minimal size for other extinction mechanisms or that real-world pollinator failures are independent. It does not rank long-term robustness, extinction cascades, or any ecological objective besides the second moment considered here. The simple expectation equality follows from degree matching; the nontrivial contribution is the **strictly reversed variance ranking at different loss probabilities, with an exact first possible size**. Bibliographic priority beyond the inspected literature requires independent checking, particularly against graph-reliability formulations using alternate terminology.

## References

- Memmott, J., Waser, N. M., and Price, M. V. (2004), “Tolerance of pollination networks to species extinctions,” *Proceedings of the Royal Society B* 271, 2605–2611, DOI `10.1098/rspb.2004.2909`. First public online date recorded as 6 December 2004 in the accessible article.
- Campbell, C., Yang, S., Shea, K., and Albert, R. (2012), “Topology of plant-pollinator networks that are vulnerable to collapse from species extinction,” *Physical Review E* 86, 021924, DOI `10.1103/PhysRevE.86.021924` (accepted manuscript available).
- Bane, M. S., Pocock, M. J. O., and James, R. (2018), “Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness,” *Ecology and Evolution*, DOI `10.1002/ece3.4529` (open full text).
