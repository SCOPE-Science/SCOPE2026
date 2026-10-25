# Rigidity of efficient edge domination in generalized Petersen graphs \(GP(n,2)\)

## Finding

**Classification theorem.** For every integer \(n\geq5\), the generalized Petersen graph \(G=GP(n,2)\) admits a dominating induced matching (also called an efficient edge dominating set) if and only if \(5\mid n\). If \(n=5t\), it admits **exactly five** such matchings, namely the cyclic shifts \(M_j\), \(0\leq j<5\), of
\[
M_0=\{u_{5r+1}v_{5r+1},\;u_{5r+3}u_{5r+4},\;v_{5r}v_{5r+2}:0\leq r<t\}.
\]
Each matching has \(3n/5\) edges. The five matchings partition \(E(G)\).

**Consequences.** For \(5\mid n\), the saturation number (the smallest cardinality of a maximal matching) is \(s(G)=3n/5\), and the five sets above are **all** smallest maximal matchings. Every strong edge coloring of \(G\) using five colors consists exactly of these five matchings as its color classes; thus the optimal strong five-edge-coloring is unique up to permutation of colors. For \(5\nmid n\), a strong five-edge-coloring does not exist. In particular, the strong chromatic index is five exactly when \(5\mid n\); no claim about its exact value otherwise is made.

## Assumptions and scope

The graph \(GP(n,2)\), for an integer \(n\geq5\), has vertices \(u_i,v_i\) with indices in \(\mathbb Z/n\mathbb Z\), and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\) for all indices \(i\). These are respectively outer, spoke, and inner edges. A matching is *induced* if no edge joins endpoints of distinct matching edges. It is *edge dominating* if every edge is in or incident to a matching edge; an induced edge-dominating matching is a *dominating induced matching* (DIM). A strong edge coloring is one in which each color class is an induced matching. A maximal matching is edge dominating. Vertex names in the theorem use the outer-cycle convention; some publications interchange the letters \(u\) and \(v\).

## Proof

**1. Vertex states.** Let \(M\) be a DIM. Color a vertex black if it is covered by \(M\) and white otherwise. A black vertex has exactly one black neighbor, its partner in \(M\), and a white vertex has all neighbors black. Conversely, any black/white coloring with these two local properties induces a DIM consisting of all black-to-black edges. This follows directly from the definitions: black-to-black edges are disjoint and have no cross-edge; an edge with a white endpoint meets the unique matching edge covering its black endpoint.

**2. Outer-cycle gaps.** Two adjacent outer vertices cannot be white, so consecutive outer white vertices in cyclic order have a distance of at least two. Three consecutive outer black vertices cannot occur, because their central vertex would have two black neighbors. The outer cycle cannot be all black or all white. Therefore every clockwise gap between consecutive white outer vertices is of length exactly two or three.

**3. Alternation of gaps.** Fix a white outer vertex \(u_i\). Its spoke neighbor \(v_i\) is black. Because \(u_i\) is white, the black vertex \(v_i\) must have precisely one black neighbor among \(v_{i-2}\) and \(v_{i+2}\). If the next outer white occurs at \(i+2\), then \(v_{i+2}\) is black (it neighbors white \(u_{i+2}\)); if the next white occurs at \(i+3\), then \(u_{i+1}\) and \(u_{i+2}\) are black and matched to one another along the outer edge, forcing \(v_{i+2}\) to be white. Hence \(v_{i+2}\) is black exactly when the next gap is two. Applying the analogous argument in the backward direction, \(v_{i-2}\) is black exactly when the preceding gap is two. Exactly one of the preceding and following gaps is therefore two; the other is three. The cyclic gap word alternates between two and three.

In particular, its number of gaps is even, and summing them gives \(n=5t\). Up to rotating the indices, the outer white positions are precisely those congruent to \(0\) or \(2\) modulo five. There are exactly five possible rotations (they are distinct).

**4. Uniqueness and construction.** Once the colors on the outer cycle are fixed, the inner color at \(v_i\) is forced: it is black when \(u_i\) is white; if \(u_i\) is black and both outer neighbors are white, its only possible black partner is \(v_i\), which must be black; otherwise \(u_i\) is already paired along the outer cycle and \(v_i\) must be white. Thus there is at most one DIM per outer-white pattern, hence at most five.

For \(n=5t\), assign outer vertices white in residue classes \(0,2\), black in \(1,3,4\), and inner vertices black in \(0,1,2\), white in \(3,4\), modulo five. Each black vertex has exactly one black neighbor and each white vertex has only black neighbors; this can be checked using the three specified edge families, with indices modulo five. The black-to-black edges are exactly the three classes in \(M_0\). Rotating produces five distinct DIMs, establishing the classification. Each consists of \(t\) edges of each of the outer, spoke, and inner types. The five rotations traverse every residue class of each edge type once, so they partition all \(3n\) edges.

**5. Saturation and coloring.** Every edge of a simple cubic graph has exactly four adjacent edges, so any maximal matching of \(G\) contains at least \(|E(G)|/5=3n/5\) edges, since the closed edge neighborhoods of its members cover all edges. The constructed DIM attains this bound for \(5\mid n\). If a maximal matching attains the bound, its closed edge neighborhoods of five edges must be pairwise disjoint. In particular no edge joins endpoints of two selected edges; hence the matching is induced and so is one of the five classified DIMs.

Every strong edge coloring of a cubic graph needs at least five colors: a chosen edge and its four incident-neighbor edges are pairwise at edge-distance at most two. With five colors, these five edges must have all distinct colors. Therefore for any edge, its closed edge neighborhood contains exactly one occurrence of each color, and each color class is a DIM. The five distinct DIMs already partition \(E(G)\), giving a strong five-coloring when \(5\mid n\). Conversely, a strong five-coloring would supply a DIM and thus force \(5\mid n\). Finally, any five-coloring must use the five classified DIMs as its color classes, proving uniqueness up to relabeling.

## Verification

The infinite classification follows from the symbolic local-state argument above; no finite enumeration is used to infer the theorem for untested orders. Two independent standard-library Python programs provide redundant, reproducible checks:

- `verify_exact_cover.py` independently represents each edge as a row that covers its closed edge neighborhood, exhaustively solves the resulting exact-cover problem for every integer \(5\leq n\leq30\), and compares solutions with the five predicted rotations, including exact edge partition.
- `verify_local_states.py` instead enumerates admissible cyclic binary outer-state words and checks each resulting full vertex coloring for every integer \(5\leq n\leq20\). The two implementations use different search spaces and criteria.

Run both using `python3 verify_exact_cover.py` and `python3 verify_local_states.py` in the directory containing these files. The included `exact_cover_output.txt` and `vertex_states_output.txt` reproduce the observed output; the terminal markers are `EXACT_COVER_OK` and `VERTEX_STATES_OK`, respectively.

## Relationship to prior work

The existence of a DIM with \(3n/5\) edges for \(GP(n,2)\) when \(5\mid n\) **is already established** explicitly in Observation 7 of *Dominating induced matchings and other graph parameters* (2024), and is not claimed to be new. The 2018 paper *Strong edge chromatic index of the generalized Petersen graphs* reports chromatic-index values for \(1\leq k\leq3\); those numerical values are likewise not claimed to be new. The present contribution is the exhaustive five-class DIM **uniqueness** theorem, the classification of all smallest maximal matchings, and uniqueness (up to color permutation) of the strong five-coloring for this infinite family. The 2014 fullerene-saturation literature gives a related extremal context but does not supply this all-orders classification. Comparison with accessible results for other matching complexes concerns distinct invariants, not a covering result.

## Limitations

The theorem is restricted to the family \(GP(n,2)\) and says nothing about the exact strong chromatic index when \(5\nmid n\), except that it exceeds five. The 2018 chromatic-index paper could be checked from its published abstract and subsequent citations but its full text was not obtained; it remains a material possibility that an equivalent uniqueness observation appears there or in unindexed material. No independent external validation or publication-priority certification has been performed.

## References

1. *Dominating induced matchings and other graph parameters*, 2024, doi:10.1080/09728600.2024.2342310, especially Observation 7, https://www.tandfonline.com/doi/full/10.1080/09728600.2024.2342310.
2. Z. Yang and B. Wu, *Strong edge chromatic index of the generalized Petersen graphs*, Applied Mathematics and Computation 321 (2018), 431–441, doi:10.1016/j.amc.2017.10.047.
3. M. Chen, L. Miao and S. Zhou, *Strong Edge Coloring of Generalized Petersen Graphs*, Mathematics 8 (2020), article 1265, doi:10.3390/math8081265.
4. V. Andova, F. Kardoš and R. Škrekovski, *Sandwiching saturation number of fullerene graphs*, arXiv:1405.2197, first made public 2014-05-09.
