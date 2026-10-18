# Local forcing-subset polynomials and alternating-cycle packing for every perfect matching of the four-cube

## Finding

Let \(Q_4\) be the four-dimensional binary hypercube. For every perfect matching \(M\), count the subsets of its edges that uniquely extend to a perfect matching, distinguishing such subsets by cardinality. The 272 matchings fall into exactly eight symmetry classes and these classes have eight different local forcing-subset polynomials. The same classification exhibits a sharp gap between the forcing number and the maximum number of vertex-disjoint alternating cycles, even though every matching has the previously known forcing number four.

Here is the complete classification. The polynomial associated with a row is \(c_4z^4+c_5z^5+c_6z^6+8z^7+z^8\). A cycle count distinguishes *edge sets* of alternating cycles, not merely vertex sets. The entries in the final column are the maximum numbers of pairwise vertex-disjoint alternating cycles.

| Symmetry orbit size | \(c_4\) | \(c_5\) | \(c_6\) | Alternating cycles | Maximum disjoint cycles |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 4 | 2 | 8 | 16 | 68 | 4 |
| 48 | 4 | 18 | 20 | 86 | 4 |
| 24 | 4 | 16 | 20 | 86 | 4 |
| 48 | 8 | 24 | 22 | 102 | 4 |
| 96 | 10 | 28 | 23 | 108 | 4 |
| 12 | 12 | 32 | 24 | 104 | 4 |
| 32 | 18 | 36 | 25 | 152 | 3 |
| 8 | 24 | 48 | 28 | 264 | 2 |

Summed over all 272 perfect matchings, the numbers of locally forcing edge subsets of sizes four through eight are, respectively,
\[
2552,\quad 7040,\quad6080,\quad2176,\quad272.
\]
All smaller coefficients vanish. Thus 232 matchings have disjoint-alternating-cycle packing number four, 32 have packing number three, and eight have packing number two. Every matching has forcing number four, so the maximum gap between that number and vertex-disjoint alternating-cycle packing is exactly two and is attained by exactly eight matchings.

## Assumptions and scope

The vertex set of \(Q_4\) is \(\{0,1\}^4\); two vertices are adjacent exactly when they differ in one coordinate. A perfect matching \(M\) comprises eight disjoint edges covering all sixteen vertices. A subset \(S\subseteq M\) is **forcing** for \(M\) if no other perfect matching contains every edge of \(S\). The local forcing-subset polynomial is
\[
P_M(z)=\sum_{\substack{S\subseteq M\S\text{ is forcing}}} z^{|S|}.
\]
This differs from the more common *forcing-number distribution* over matchings, which keeps only the smallest size for each matching. An \(M\)-alternating cycle is a simple cycle with matched and unmatched edges alternating; the cycle-packing parameter is the largest cardinality of a family of such cycles with disjoint vertex sets. The statements concern this finite graph only, not arbitrary-dimensional hypercubes.

## Proof

**Exhaustive perfect-matching enumeration.** Label vertices by the integers from zero to fifteen interpreted as binary vectors. The 32 unordered edges are exactly the pairs with XOR in \(\{1,2,4,8\}\). The recursion that selects the least uncovered vertex, pairs it with each uncovered neighbor, and recurses enumerates every perfect matching exactly once: any perfect matching must match the chosen vertex to exactly one of those neighbors. It generates precisely 272 distinct eight-edge sets, as separately confirmed by bipartite left-to-right enumeration using the even/odd parity classes (each of order eight).

**Unique-extension test.** For each of the 256 subsets \(S\subseteq M\), remove the endpoints of its selected edges. Its number of extensions is exactly the number of perfect matchings of the induced residual graph. The first program determines this by checking containment in all 272 perfect matchings. The independent program computes the extension count with the recurrence
\[
C(U)=\sum_{\substack{v\in U\uv\in E(Q_4)}} C(U\setminus\{u,v\}),\qquad C(\varnothing)=1,
\]
where \(u\) is the least vertex of nonempty \(U\) and \(C(U)=0\) if no pairing is possible. Because every perfect matching pairs \(u\) with one eligible neighbor, this is an exact recursion, not a heuristic. A subset is forcing precisely when \(C(V\setminus V(S))=1\). Both methods classify all \(272\cdot256=69632\) matching-subset pairs and agree on the eight polynomials, all zero below degree four.

**Automorphism and orbit classification.** Coordinate bit-flips followed by permutations of the four coordinates produce 384 distinct automorphisms. These are all automorphisms: the image of the zero vector and the permutation of its four neighbors determine an automorphism, and the square structure recursively determines every remaining vertex. Therefore the automorphism group has order 384. Acting on each enumerated matching and comparing edge masks partitions all 272 matchings into eight disjoint orbits of the sizes displayed in the table; the eight distinct forcing polynomials verify the orbits cannot be merged. The accompanying JSON certificate specifies a representative by eight indices into a canonical 32-edge ordering, together with the complete numerical profile.

**Alternating cycles and disjoint packing.** Fix \(M\). Every connected component of \(M\triangle N\), where \(N\) is another perfect matching, is an even \(M\)-alternating cycle. Conversely, exchanging the chosen/unselected edges of one such cycle produces another perfect matching, so every alternating cycle appears among the components of these 272 symmetric differences. The first verifier records *cycle edge masks*, using vertex masks only for disjointness, and exhaustively tests all collections of at most four disjoint cycles (four is an upper bound because every such cycle uses at least four of the sixteen vertices). A second verifier directly searches simple alternating cycles and independently performs vertex-mask dynamic programming for their maximum packing. Both compute all 272 profiles and give the table above.

Each forcing subset must intersect the matched edges of every alternating cycle; otherwise switching that cycle preserves all selected edges and gives a different perfect matching. This proves the general inequality that cycle-packing number cannot exceed forcing number, and the table verifies strictness for 40 matchings, with the largest gap two.

## Verification

The package contains two standalone Python programs requiring only the standard library and a JSON representative certificate. Run from the package directory:

```sh
python3 verify_q4_automorphisms.py q4_orbit_certificate.json
python3 verify_q4_extension_dp.py q4_orbit_certificate.json
```

The first program enumerates 272 matchings, 384 graph automorphisms, eight orbits, every local forcing subset, and the alternating cycles arising from matching symmetric differences. The second independently constructs matchings through the bipartition, uses a vertex-subset completion recurrence (9,955 memoized residual states in the executed check), directly traverses alternating cycles, and checks the same eight-orbit certificate. Both completed without discrepancy. The certificate includes the complete canonical edge ordering, all eight matching representatives and their profiles. These finite checks are exhaustive because of the recursions and coverage arguments above; they make no claim about higher-dimensional cubes.

## Relationship to prior work

Pachter and Kim analyzed forcing matchings on square grids and the matching-forcing viewpoint; the planar bipartite setting motivates comparison with vertex-disjoint alternating-cycle packing. Riddle and Adams–Mahdian–Mahmoodian established results on hypercube forcing numbers. In particular, Che and Chen's 2011 survey reports that every perfect matching of the four-cube has forcing number four. Therefore the uniform value four, the count of 272 perfect matchings, and the fact that the forcing-number distribution is concentrated at four are **not** presented as new.

The additional classification here retains *all* forcing subsets within each matching, identifies the eight complete automorphism orbits, and counts/optimizes alternating cycles in each orbit. An ordinary matching polynomial, an aggregate forcing-number distribution and these eight local subset polynomials count different objects, so the former statements do not imply the latter enumeration. Literature searches did not locate an exact eight-orbit local-polynomial-and-packing classification, but that absence is not proof of priority.

## Limitations

An independent mathematical audit has not been performed. This is a complete finite result for \(Q_4\) only; the supplied programs establish its counts and orbit coverage, not a general hypercube theorem. The exact original 2004 hypercube forcing-spectrum article was not accessible in full through the available lawful routes; its abstract and the later detailed survey were compared, leaving a residual possibility that supplemental or unindexed prior literature contains finer data. A separate scholarly priority assessment may be needed before publication.

## References

1. L. Pachter and P. Kim, *Forcing matchings on square grids*, Discrete Mathematics, 1998. DOI: 10.1016/S0012-365X(97)00266-5.
2. M. Riddle, *The minimum forcing number for the torus and hypercube*, Discrete Mathematics, 2002. DOI: 10.1016/S0012-365X(01)00228-X.
3. J. Adams, M. Mahdian and E. Mahmoodian, *On the forced matching numbers of bipartite graphs*, Discrete Mathematics, 2004. DOI: 10.1016/j.disc.2002.10.002.
4. Z. Che and Z. Chen, *Forcing on Perfect Matchings — A Survey*, MATCH Communications in Mathematical and in Computer Chemistry 66 (2011), 93–136, Theorem 3.39.
5. OEIS A005271, number of perfect matchings of the hypercube.
