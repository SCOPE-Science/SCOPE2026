# Nauru-graph anti-forcing spectrum and the hidden split of two-factor profiles

## Finding

Let \(G=GP(12,5)\) be the Nauru graph. Its vertices are \(u_i,v_i\) for \(i\in\mathbb Z/12\mathbb Z\); its edges are \(u_i u_{i+1}\), \(v_i v_{i+5}\), and \(u_i v_i\), with subscripts modulo \(12\). A perfect matching \(M\) is a set of twelve pairwise disjoint edges meeting every vertex once. Define \(\operatorname{af}(G,M)\) to be the least cardinality of \(S\subseteq E(G)\setminus M\) such that \(G-S\) has the unique perfect matching \(M\). Let \(\tau(M)\) be the multiset of lengths of cycles in the complementary two-factor \(G-M\), and let \(b(M)\) be the number of minimum-cardinality anti-forcing sets for \(M\).

There are exactly \(120\) perfect matchings, with the following complete eight-orbit profile. The column \(r\) is the number of matchings, \(a=\operatorname{af}(G,M)\), and \(b=b(M)\).

| \(\tau(M)\) | \(r\) | \(a\) | \(b\) |
|---|---:|---:|---:|
| \((6,6,6,6)\) | 3 | 8 | 1092 |
| \((6,18)\), first orbit | 12 | 6 | 207 |
| \((6,18)\), second orbit | 24 | 6 | 24 |
| \((8,8,8)\) | 6 | 5 | 36 |
| \((8,16)\) | 18 | 6 | 28 |
| \((10,14)\) | 36 | 6 | 176 |
| \((12,12)\) | 3 | 6 | 60 |
| \((24)\) | 18 | 7 | 640 |

Consequently, the anti-forcing polynomial is
\[
A_G(t)=6t^5+93t^6+18t^7+3t^8,
\]
and there are exactly \(25{,}092\) ordered pairs \((M,S)\) with \(M\) a perfect matching and \(S\) a minimum anti-forcing set for \(M\). On this graph the two-factor cycle-length partition determines the anti-forcing **number**, but does **not** determine the number of optimum deletion sets: both distinct orbits with \(\tau(M)=(6,18)\) have \(a=6\), yet their optimum deletion-set counts are \(207\) and \(24\).

## Assumptions and scope

The graph is the simple, unweighted, fully labeled generalized Petersen graph described above. Edges are undirected; deleting \(S\) leaves the twelve edges of \(M\) untouched. Two-factor lengths are ordinary numbers of vertices in the connected cycles of the spanning 2-regular graph \(G-M\). The count \(b(M)\) distinguishes edge subsets on this fixed labeled graph; no quotient by automorphisms is taken. This is a finite exact classification for \(GP(12,5)\), not an assertion about all generalized Petersen graphs or all cubic bipartite graphs.

## Proof

**1. Complete finite sample space.** Write the 36 edges in ascending lexicographic order after identifying \(u_i=i\), \(v_i=12+i\). Algorithm `NAURU_VERIFY_EXHAUSTIVE.py` enumerates all perfect matchings recursively: at any stage choose the smallest uncovered vertex and branch over every possible incident edge whose other endpoint is still uncovered. The first choice in a perfect matching is forced to appear in exactly one such branch, so induction proves exhaustiveness and uniqueness. It produces 120 distinct matchings. Independently, `NAURU_VERIFY_CERTIFICATE.py` uses the bipartition \(\{u_i:i\text{ even}\}\cup\{v_i:i\text{ odd}\}\) and its complement and enumerates all bijective assignments respecting the graph's edges; it also produces exactly 120 matchings.

**2. Exact anti-forcing criterion.** For a fixed matching \(M\), an external-edge set \(S\) leaves \(M\) unique precisely when
\[
S\cap(N\setminus M)\ne\varnothing\qquad\text{for every perfect matching }N\ne M.
\]
This is an immediate equivalence: \(N\) survives deletion exactly when it uses no edge of \(S\); because \(S\cap M=\varnothing\), the displayed difference is sufficient. Thus minimum anti-forcing sets are exactly minimum transversals of a finite explicit family of edge subsets. The exhaustive checker examines each subset of the 24 external edges of cardinalities \(0,1,\ldots\) until it finds feasible sets; all candidates of the first feasible cardinality are counted. Inclusion-minimal constraints may be substituted because a larger constraint is redundant if a contained one must be hit. This produces the profile in the finding.

**3. Independent upper-and-lower certificates.** The machine-readable `NAURU_CERTIFICATE.json` records eight perfect-matching representatives, their target values, one upper-set of \(a\) external edges for each, and \(a\) explicit alternating cycles with pairwise disjoint sets of edges outside \(M\). The independent checker verifies that deleting each upper-set destroys every other one of the 120 perfect matchings. For each packed cycle it checks alternating incidence, degree two at every cycle vertex, and connectedness; it checks disjointness of all packed **external** edge sets. Any anti-forcing set must hit each packed cycle, and one external edge cannot hit two of them. This supplies the lower bound \(a\), while the upper set supplies equality, with no reliance on optimization-solver status.

The same certificate contains 120 explicit permutations of the 24 vertices partitioned among those eight representatives. Each is checked to be a bijection preserving the **entire** 36-edge set and carrying its representative to its indicated perfect matching. The indicated targets exhaust the independently enumerated 120 matchings without duplication. Hence these eight representatives and their lower/upper certificates prove the exact anti-forcing number for every matching. Finally, for each representative the checker independently tests all \(\binom{24}{a}\) deletion candidates of size \(a\) against all other matchings, obtaining its value \(b\); automorphisms preserve this count, proving the displayed orbit-size multiplication and \(25{,}092\) total.

## Verification

Run from the directory containing the three named artifacts:

```sh
python NAURU_VERIFY_EXHAUSTIVE.py
python NAURU_VERIFY_CERTIFICATE.py NAURU_CERTIFICATE.json
```

The two scripts use only the Python standard library and contain their own graph and matching constructions. The first exhaustively searches deletion subsets for **all** matchings. The second reconstructs matchings through a bipartite assignment and checks explicit alternating-cycle packings, external-edge hitting sets and automorphism witnesses. The exact outputs are recorded in `NAURU_EXHAUSTIVE_OUTPUT.json` and `NAURU_CERTIFICATE_OUTPUT.json`; both report the same eight-row refined profile and total of \(25{,}092\). The certificate can be checked without a mixed-integer solver or a graph-isomorphism package. Internal numerical optimization was used only to *discover* witnesses, not to validate the theorem.

## Relationship to prior work

Lei, Yeh and Zhang (arXiv:1406.3796, first public 2014-06-15) establish the anti-forcing definition and the alternating-cycle hitting-set characterization; these are not claimed as new. Their plane-bipartite minimax result cannot directly establish a nonplanar toroidal graph's exact values. Deng and Zhang (arXiv:1607.05392, first public 2016-07-19) give broad anti-forcing bounds and spectra for polygonal chains, not this graph's eight-orbit spectrum. The Nauru graph's classical construction, automorphisms, toroidal nature and name are independently documented by Eppstein and standard graph references. The exact Nauru anti-forcing polynomial, optimum-set multiplicities, and the \((6,18)\) split are the claims under assessment, not general anti-forcing theory.

## Limitations

This is a computationally certified finite theorem with exhaustive algorithms and explicit lower/upper witnesses, not a symbolic infinite-family theorem. The full calculation is feasible because there are only 120 perfect matchings. The two-factor partition alone is not proved to determine anti-forcing numbers in any wider graph class. Publication priority has not been independently established against every unindexed or inaccessible source, especially specialized generalized-Petersen anti-forcing reports. The full 2025 survey was not inspected, so it cannot be treated as noncovering evidence.

## References

1. H. Lei, Y.-N. Yeh and H. Zhang, *Anti-forcing numbers of perfect matchings of graphs*, arXiv:1406.3796 (first submitted 15 June 2014), https://arxiv.org/abs/1406.3796.
2. K. Deng and H. Zhang, *Extremal anti-forcing numbers of perfect matchings of graphs*, arXiv:1607.05392 (first submitted 19 July 2016), https://arxiv.org/abs/1607.05392.
3. D. Eppstein, *The many faces of the Nauru graph*, 12 December 2007, bibliographic date corroborated in *Twenty years of blogging* (2025), https://11011110.github.io/blog/2025/07/20/twenty-years-blogging.html.
4. E. W. Weisstein, *Nauru Graph*, MathWorld, https://mathworld.wolfram.com/NauruGraph.html (consulted 2026; includes historical references).
5. Y. Zhang, X. He, Q. Liu and H. Zhang, *Forcing, anti-forcing, global forcing and complete forcing on perfect matchings of graphs: A survey*, Discrete Applied Mathematics (2025), doi:10.1016/j.dam.2025.06.022 (abstract and bibliography only consulted).
