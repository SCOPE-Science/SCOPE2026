# Exact anti-forcing witness profiles and the edge-disjoint deletion penalty of the dodecahedral graph

## Finding

For a perfect matching \(M\) of the twenty-vertex dodecahedral graph \(D\), write \(\operatorname{af}(D,M)\) for its minimum anti-forcing deletion cardinality. Requiring the deleted edges to be pairwise vertex-disjoint gives \(\operatorname{af}_{\perp}(D,M)\). There are exactly 36 perfect matchings in two automorphism orbits, with the following **complete minimum-witness census**:

| Matching orbit size | \(\operatorname{af}(D,M)\) | Number of minimum ordinary witnesses per \(M\) | \(\operatorname{af}_{\perp}(D,M)\) | Number of minimum disjoint witnesses per \(M\) |
| ---: | ---: | ---: | ---: | ---: |
| 30 | 4 | 8 | 8 | 4 |
| 6 | 5 | 22 | 8 | 5 |

Thus the ordinary and edge-disjoint anti-forcing polynomials are respectively
\[
P_D(t)=\sum_{M\in\mathcal P(D)}t^{\operatorname{af}(D,M)}=30t^4+6t^5,
\qquad
P_D^{\perp}(t)=\sum_{M\in\mathcal P(D)}t^{\operatorname{af}_{\perp}(D,M)}=36t^8.
\]
The 30-element orbit has a sharp edge-disjoint penalty of four additional deleted edges; the 6-element orbit has a penalty of three. Across all perfect matchings there are \(30\cdot8+6\cdot22=372\) minimum ordinary witnesses and \(30\cdot4+6\cdot5=150\) minimum edge-disjoint witnesses. The underlying spectrum \(\{4,5\}\) is already known in the literature and is not asserted to be new; the claimed contribution is the orbit-resolved witness multiplicity and the sharp independent-edge-deletion restriction.

## Assumptions and scope

Define \(D=GP(10,2)\) with vertices \(u_i,v_i\) for integers \(0\le i<10\), indices taken modulo 10, and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). This is the graph of the regular dodecahedron, with 20 vertices, 30 edges and degree three. A perfect matching contains ten pairwise vertex-disjoint edges covering all vertices. Let \(\mathcal P(D)\) denote the set of all perfect matchings.

For any \(M\in\mathcal P(D)\) and \(S\subseteq E(D)\setminus M\), \(S\) is an **anti-forcing witness** if the spanning graph \(D-S\) has exactly one perfect matching, namely \(M\). The ordinary anti-forcing number \(\operatorname{af}(D,M)\) minimizes \(|S|\) without further restriction. For the edge-disjoint restricted number \(\operatorname{af}_{\perp}(D,M)\), \(S\) must itself be a matching. Witness multiplicities count distinct edge subsets, not sequences of deletions and not equivalence classes of witnesses. All minima are taken over finite sets, and the theorem concerns only this named graph.

## Proof

**Exact uniqueness criterion.** For each fixed \(M\), enumerate every other perfect matching \(N\). Since \(S\cap M=\varnothing\), the original matching remains in \(D-S\). The alternative \(N\) survives precisely when \(S\cap(N\setminus M)=\varnothing\). Hence
\[
D-S\text{ has precisely the perfect matching }M\iff
\forall N\in\mathcal P(D)\setminus\{M\},\quad S\cap(N\setminus M)\ne\varnothing.
\]
This equivalence reduces the claim to an exhaustive, finite Boolean hitting-set calculation; it does not appeal to any unproved infinite classification.

**Perfect matchings and symmetry.** For any nonempty set of unmatched vertices, pick its least vertex and branch over every still-unmatched neighbor, then recurse. This constructs each perfect matching exactly once. The standard-library program `verify_orbits.py` implements this recurrence and obtains exactly 36 matchings. It independently enumerates all adjacency-preserving permutations by injective backtracking, giving 120 automorphisms. Their induced action on the 36 matchings has precisely two orbits, of sizes 30 and 6. Automorphisms preserve the cardinalities and multiplicities of ordinary and edge-disjoint witnesses, so one representative per orbit suffices for the first verification.

**Exhaustive minima and witness counts.** Each matching leaves 20 eligible nonmatching edges. For a representative of each orbit, `verify_orbits.py` checks **every** eligible \(k\)-subset in increasing \(k\), using the exact uniqueness criterion. Independently for each subset it also checks whether its edges have disjoint endpoints. For the size-30 orbit, there is no unrestricted witness of size below 4 and exactly eight of size 4; there is no disjoint witness of size below 8 and exactly four of size 8. For the size-6 orbit the corresponding numbers are five, 22, eight and five. This proves sharpness, including all negative lower-bound claims, because every smaller subset was considered. Symmetry propagates these counts to every matching. The displayed polynomials and totals follow by summing the two orbit contributions.

**Independent complete computation.** `verify_direct.py` uses a second, LCF-defined presentation of the dodecahedron and an explicit 20-vertex isomorphism to the generalized Petersen presentation. It represents both matchings and deletion sets by bitmasks, independently enumerates all 36 perfect matchings, and, **for each of the 36 matchings separately**, enumerates all deletion subsets through cardinality 8, with no use of the orbit reduction. Its hitting tests are based on bitmasks of \(N\setminus M\). The independently observed profile multiplicities are exactly 30 and 6, with the same witness counts. Both methods reproduce the reported totals; their executable source and exact expected outputs are embedded with this result.

For further explicit existence evidence in the indexed vertex coordinates \(u_i=i\), \(v_i=10+i\): one size-30 orbit matching is
\(\{(0,1),(2,3),(4,5),(6,7),(8,18),(9,19),(10,12),(11,13),(14,16),(15,17)\}\).
Its size-four ordinary witness is \(\{(0,9),(0,10),(4,14),(10,18)\}\), whereas an eight-edge disjoint witness is \(\{(0,9),(1,11),(6,16),(7,8),(10,18),(12,14),(13,15),(17,19)\}\).
For a size-six orbit matching, use \(\{(0,1),(2,3),(4,14),(5,6),(7,8),(9,19),(10,12),(11,13),(15,17),(16,18)\}\), with size-five witness \(\{(0,9),(0,10),(6,7),(7,17),(10,18)\}\), and size-eight disjoint witness \(\{(0,9),(1,2),(3,13),(4,5),(6,7),(8,18),(11,19),(14,16)\}\).

## Verification

Execute `python3 verify_orbits.py` and `python3 verify_direct.py` in the directory containing the standalone files; both require only the Python standard library. Their outputs are stored in `verify_orbits.out` and `verify_direct.out`. The first ends in `VERIFY_OK`, the second in `INDEPENDENT_VERIFY_OK`. Neither success token substitutes for the exhaustive scope of the tests, which is established by the explicit enumeration and the uniqueness equivalence above. The LCF-to-Petersen isomorphism is checked in the second program. The enumerations are exact integer and finite-set operations with no random samples, floating-point tolerances, or external data dependencies.

## Relationship to prior work

Lei, Yeh and Zhang (2014) introduced the anti-forcing number of a **specified** perfect matching and its equivalent alternating-cycle hitting description; these definitions and generic inequalities are prior work. Yang, Zhang and Lin (2015) proved that every fullerene has graph-level anti-forcing number at least four, exhibited a four-deletion certificate for the dodecahedral fullerene and proved that a four-edge anti-forcing set in a fullerene is not a matching. Deng and Zhang (2016) studied broader maximum anti-forcing bounds. Han, Zhou and Wang (2023) **already reported the exact anti-forcing spectrum \([4,5]\) for the twenty-vertex fullerene** (and computed spectra for lower-order fullerenes). None of these facts is proposed here as novel. The additional, checked claim is the per-orbit count of minimum witnesses and, in particular, the exact **eight-deletion** threshold when the removed edges must be pairwise nonincident, including its counts. The published dodecahedral matching-complex homotopy calculations concern a different invariant and do not imply the anti-forcing certificate counts merely from their stated results.

## Limitations

The theorem is an exact finite computation supported by a complete exhaustive algorithm, not a new bound or classification for all fullerenes. The proof requires the stated graph presentation; no inference to other fullerenes is asserted. Literature searches and examination of the relevant sections of the primary sources found no previous statement of the joint orbit-resolved restricted/unrestricted witness census, but unindexed work or unreported numerical tables may overlap. Independent external validation has not been performed.

## References

1. H. Lei, Y.-N. Yeh and H. Zhang, *Anti-forcing numbers of perfect matchings of graphs*, arXiv:1406.3796v1 (first posted 2014-06-15), https://arxiv.org/abs/1406.3796.
2. Q. Yang, H. Zhang and Y. Lin, *On the anti-forcing number of fullerene graphs*, arXiv:1503.01900v1 (first posted 2015-03-06), https://arxiv.org/abs/1503.01900.
3. H. Deng and H. Zhang, *Extremal anti-forcing numbers of perfect matchings of graphs*, arXiv:1607.05392v1 (2016), https://arxiv.org/abs/1607.05392.
4. H. Han, Y. Zhou and Y. Wang, *Continuity of Matching Forcing Spectra and Anti-Forcing Spectra for Lower-Order Fullerenes*, *Advances in Applied Mathematics* 12 (2023), 1173–1187, https://doi.org/10.12677/aam.2023.123119.
