# Global perfect-matching forcing in the Heawood graph: seven edges, 8064 optima, thirty symmetry classes

## Finding

**Theorem.** Let \(H\) be the fourteen-vertex Heawood graph. A set \(F\subseteq E(H)\) is *globally forcing* if the maps \(M\mapsto M\cap F\), for all perfect matchings \(M\) of \(H\), take pairwise distinct values. Then

\[\operatorname{gf}(H)=7,\qquad |\{F:|F|=7,\ F\text{ is globally forcing}\}|=8064.\]

Under the full automorphism group \(\operatorname{Aut}(H)\) of order \(336\), the minimum sets form precisely \(30\) orbits: \(12\) of size \(168\) and \(18\) of size \(336\). Thus the stabilizer of an optimal set has order \(2\) in the first class and order \(1\) in the second.

**Short-cycle boundary.** Exactly \(812\) six-edge sets meet every one of the \(28\) conformal (nice) hexagons. They form five orbits of sizes \(56,84,168,168,336\); every such set fails to meet a conformal decagon. In particular, checking hexagons alone would incorrectly suggest a six-edge solution, but the longer alternating cycles force the minimum to seven.

## Assumptions and scope

The graph is finite, simple, undirected, and fixed up to isomorphism. An explicit realization has point vertices \(p_a\) and line vertices \(\ell_b\), where \(a,b\in\mathbb F_2^3\setminus\{0\}\). Adjacency is exactly \(p_a\sim\ell_b\) when the standard binary dot product \(a\cdot b=0\). Represent nonzero vectors by integers \(1,\ldots,7\), using three binary bits; number the \(21\) edges in increasing lexicographic order of the pair \((a,b)\), from index \(0\) to index \(20\). A subset is encoded by the nonnegative integer whose set binary positions are its edge indices. For example, decimal mask \(8795\) has selected indices \(0,1,3,4,6,9,13\) and is globally forcing.

A *perfect matching* covers each point and line vertex exactly once. The incidence edge test of a matching \(M\) on \(F\) is the set \(M\cap F\). The global forcing number is the smallest \(|F|\) making all tests different. A *nice cycle* is one for which deletion of all its vertices leaves a subgraph with a perfect matching; the symmetric difference of two perfect matchings is a disjoint union of alternating even cycles (while any common edges are excluded). The proof uses the complete finite graph and makes no claim about all cubic graphs, all projective planes, or asymptotic families.

## Proof

**Step 1: exact matching family and difference criterion.** Process point vertices in the order \(1,\ldots,7\). Recursively match each point to each available incident line, omitting already used lines. Every perfect matching has a unique seven-step path through this search. The finished recursion has \(24\) leaves, corroborated independently by Ryser inclusion-exclusion for the permanent of the \(7\)-by-\(7\) binary incidence matrix. Since every perfect matching uses exactly one edge at each point, this is exhaustive.

For any two distinct perfect matchings \(M,N\), their test patterns on \(F\) differ if and only if \(F\cap(M\triangle N)\ne\varnothing\). Thus a set is globally forcing precisely when it meets every member of the distinct family

\[\mathscr D=\{M\triangle N:M,N\text{ perfect},\ M\ne N\}.\]

There are \(\binom{24}{2}=276\) matching pairs but only \(178\) distinct difference edge sets. Their cardinalities and distinct multiplicities are \(6:28\), \(10:84\), \(12:42\), and \(14:24\). Every six-edge difference is the edge set of a nice hexagon; there are \(28\) of them. This criterion involves all \(178\) differences, not only elementary hexagons.

**Step 2: no global forcing set with six or fewer edges.** There are exactly \(\binom{21}{6}=54264\) six-edge candidates. Exhaustively test each for intersection with the \(28\) hexagons. Exactly \(812\) survive. Their five automorphism orbits have sizes \(56\), \(84\), \(168\), \(168\), and \(336\). In the canonical mask encoding one representative and a ten-edge difference mask disjoint from it for each orbit are:

| Six-edge representative | Orbit size | Disjoint nice decagon mask |
| ---: | ---: | ---: |
| 43284 | 56 | 788203 |
| 8779 | 84 | 810416 |
| 8908 | 168 | 1790003 |
| 9036 | 168 | 1790003 |
| 8781 | 336 | 810416 |

Each displayed decagon mask belongs to \(\mathscr D\), and its bitwise AND with its six-edge representative is zero. Automorphisms preserve \(\mathscr D\), so every member of each five-element orbit class also misses a ten-edge difference. Therefore none of the \(812\) survivors separates all matchings, and no six-edge global forcing set exists. Adding edges cannot destroy the separation property, so smaller forcing sets are also impossible.

**Step 3: sharpness and complete multiplicity.** Enumerate the \(\binom{21}{7}=116280\) seven-edge candidates and retain exactly those meeting every one of the \(178\) difference sets. Exactly \(8064\) pass. In particular, the edge-index subset \(\{0,1,3,4,6,9,13\}\) (mask \(8795\)) passes, establishing sharpness. A separate direct test that the \(24\) sets \(M\cap F\) are distinct agrees on every seven-edge candidate. This gives both the minimum and the exact multiplicity, without statistical sampling.

**Step 4: orbit classification.** The automorphisms preserving the two point/line parts are the \(168\) invertible linear transformations \(a\mapsto Aa\), accompanied by the dual action \(b\mapsto A^{-T}b\). Their compositions with the point-line interchange generate \(336\) distinct automorphisms. Conversely, an automorphism preserving the bipartition induces a collineation of the Fano plane; its action is determined by the images of an ordered basis, giving at most \(7\cdot6\cdot4=168\) possibilities. Interchange doubles the bound, so these are all automorphisms.

Act with all \(336\) edge permutations on each seven-edge candidate, remove its orbit, and repeat until all candidates are partitioned. The exact result is \(12\) orbits of size \(168\) and \(18\) of size \(336\), totaling \(8064\). The file `orbit_representatives.csv` supplies the \(30\) orbit masks, cardinalities, and their seven edge indices. No equivalence between two distinct listed orbits remains: each representative was chosen as the numerically least remaining mask and its complete orbit was removed.

## Verification

The complete standard-library program `verify.py` independently builds the edge list and matching family, computes the permanent using Ryser's formula, constructs all \(178\) distinct difference masks, enumerates all \(54264\) six-edge and \(116280\) seven-edge candidate subsets, and checks the signatures again by an independent predicate. It exhausts the \(336\) explicitly represented automorphisms and partitions both the \(812\) hexagon transversals and \(8064\) optimum sets. Every loop is over a stated finite exhaustive set; no timeout, heuristic optimizer, extrapolation, or externally sourced classification table is used. Run `python3 verify.py` from the package directory with Python 3.10 or later; `orbit_representatives.csv` is optional human-readable reference data generated and separately compared to the verified orbit list at package creation.

The check reports \(24\) matchings, a Ryser permanent of \(24\), \(178\) distinct difference masks, \(812\) six-edge hexagon transversals all blocked by decagons, \(8064\) seven-edge global forcing sets, \(336\) automorphisms, and the complete two orbit-size distributions. Exhaustive finite enumeration proves an exact finite theorem here; it is not an argument about arbitrary graph orders.

## Relationship to prior work

The global forcing concept was originally also called *total forcing of perfect matchings*. Earlier work of Vukičević and Sedlar introduced this setting for grids, and Vukičević–Došlić and Došlić computed it for grids, complete graphs, and benzenoid classes. Zhang's 2011 survey (§5.1) summarizes these results and the general cyclomatic upper and information lower bounds. Here those bounds give \(\lceil\log_2 24\rceil=5\le\operatorname{gf}(H)\le21-14+1=8\), not the exact answer \(7\) or its \(8064\) multiplicity. Zhang–Zhang (2020, §2, Lemma 2.7) give the general nice-cycle transversal criterion, which motivates but does not enumerate the distinct Heawood transversals.

Ye–Zhang's archived paper (first submitted 2009-08-11) treats the Heawood graph as a distinguished Pfaffian brace and analyzes embeddings, polyhex graphs, and matching structure. It does not report the global forcing number or the multiplicities of globally forcing edge sets. Lei–Yeh–Zhang (2014) treat *anti-forcing a chosen matching*, with a different quantifier from separating every perfect matching at once. The known values \(24\) perfect matchings and \(28\) hexagons alone do not imply the decagon obstruction, the exact minimum, or the orbit census.

## Limitations

The determination is exhaustive for this one graph; it does not prove a general formula for global forcing numbers of cubic cages, nor a general complexity claim. The 2007 original grid-paper PDF was located, but its available text extraction was incomplete; the independently readable 2011 survey and the full 2020 open preprint support the specific comparisons described. A priority risk remains from unindexed earlier computational enumerations or alternative terminology, despite direct searches for global/total forcing, nice-cycle transversals, and matching-distinguishing edge sets. The 2009-08-11 date is the verified first public date of the cited archival **seed paper**, not a claim about publication timing of this theorem.

## References

1. Dong Ye and Heping Zhang, *Embeddings of Pfaffian Braces and Polyhex Graphs* (first arXiv version, 11 August 2009), arXiv:0908.1506v1, https://arxiv.org/abs/0908.1506v1 . Later expanded as *Face-width of Pfaffian Braces and Polyhex Graphs on Surfaces* (2013 version), https://arxiv.org/pdf/0908.1506 .
2. Damir Vukičević and Tomislav Došlić, *Global forcing number of grid graphs*, Australasian Journal of Combinatorics 38 (2007), 47–62, https://ajc.maths.uq.edu.au/pdf/38/ajc_v38_p047.pdf .
3. Tomislav Došlić, *Global forcing number of benzenoid graphs*, Journal of Mathematical Chemistry 41 (2007), 217–229, DOI:10.1007/s10910-006-9056-2.
4. Heping Zhang, *Forcing on Perfect Matchings: A Survey*, MATCH Communications in Mathematical and in Computer Chemistry 66 (2011), 93–136, §5.1, https://match.pmf.kg.ac.rs/electronic_versions/Match66/n1/match66n1_93-136.pdf .
5. Hongchuan Lei, Yeong-Nan Yeh, and Heping Zhang, *Anti-forcing numbers of perfect matchings of graphs*, arXiv:1406.3796v1 (15 June 2014), https://arxiv.org/abs/1406.3796 .
6. Yaxian Zhang and Heping Zhang, *Relations between global forcing number and maximum anti-forcing number of a graph*, arXiv:2009.05746v1 (12 September 2020), https://arxiv.org/pdf/2009.05746 .
