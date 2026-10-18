# The Heawood graph has strong rainbow connection four and an exact fresh-colour matching-repair spectrum

## Finding

**Theorem.** Let \(H\) denote the point-line incidence graph of the Fano projective plane, with a vertex for each of its seven points and seven lines and an edge for every incidence. Then its strong rainbow connection number is
\[
\operatorname{src}(H)=4.
\]
A *strong rainbow edge-colouring* assigns colours to edges so that, for every two distinct vertices, there is a shortest path (geodesic) whose edges have pairwise different colours.

More precisely, all proper edge-colourings with three named colours form eight classes modulo simultaneous permutations of the colour names, or 48 named colourings. In each class precisely seven nonincident point-line pairs have no rainbow geodesic; the seven pairs cover every point and every line exactly once. Across the eight classes each of the 28 nonincident point-line pairs appears as an obstruction exactly twice.

Fix **any** proper three-edge-colouring \(c\). For a matching \(M\subseteq E(H)\), define the *fresh-colour repair* \(c_M\) by recolouring every edge in \(M\) with a new fourth colour and leaving the other edges unchanged. The complete number of strongly rainbow repaired colourings at each matching size is

| \(\lvert M\rvert\) | All matchings | Successful fresh-colour repairs |
|:---:|---:|---:|
| 0 | 1 | 0 |
| 1 | 21 | 0 |
| 2 | 168 | 0 |
| 3 | 644 | 0 |
| 4 | 1,218 | 126 |
| 5 | 1,050 | 84 |
| 6 | 336 | 0 |
| 7 | 24 | 0 |

The successful-repair enumerator is therefore \(126t^4+84t^5\), independently of the choice of \(c\). In particular, among repairs leaving the original three colours untouched outside the newly coloured edges, exactly four edge recolourings are necessary and sufficient, even though recolouring six or seven disjoint edges never succeeds.

## Assumptions and scope

The graph is simple, undirected and has no loops. Use points \(p=0,\ldots,6\) and lines \(7+j\), where the point set of line \(j\) is \(\{j,j+1,j+3\}\pmod 7\). Each part of the bipartition has seven vertices, and every vertex has degree three. Write the 21 incidence edges as the lexicographically ordered pairs \((p,7+j)\). A colouring need not be assumed proper in the definition of strong rainbow connection; propriety is *forced* when there are three colours, as proved below.

All enumerations are exact, exhaustive finite enumerations, with explicit Python sources included. For the repair theorem the newly introduced colour is absent from \(c\), and the set recoloured to it must be a matching; no assertion is made about recolouring to pre-existing colours or altering more than one colour per selected edge.

## Proof

**(1) Geometry and distance reduction.** Distinct points share exactly one line, and distinct lines share exactly one point. Therefore \(H\) has girth six, and each same-part pair has a unique length-two geodesic. A point and line are at distance one when incident and distance three otherwise. Every nonincident pair has exactly three length-three geodesics, indexed by its three neighboring lines/points. There are 28 such pairs, accounting for all distance-three pairs; \(H\) has diameter three.

**(2) Any strong three-colouring must be proper.** If two distinct incident edges had the same colour, the unique two-edge geodesic between their other endpoints could not be rainbow. Hence every strong three-edge-colouring uses three different colours at each cubic vertex. In particular it is a proper three-edge-colouring, and every proper three-edge-colouring automatically passes all pairs at distance at most two. Strong rainbow testing thus reduces exactly to checking 28 nonincident point-line pairs.

**(3) Exhaustive classification of the three-colour obstructions.** Fix the colours \(0,1,2\) in ascending edge order at point 0; every named proper colouring has exactly one representative under global colour renaming. Visit each remaining incidence edge and assign one of \(0,1,2\), pruning immediately when an incident vertex repeats a colour. The exhaustive recursion in `fano_rainbow_1.py` obtains exactly eight leaves; the independently constructed binary-projective-plane factorization in `fano_rainbow_2.py` counts 24 perfect matchings, proves each complementary two-factor is a single 14-cycle, and obtains 48 named proper three-colourings. Both classify the 28 geodesic conditions and find seven failed pairs in each colouring. Each failed-pair set covers all seven points and all seven lines; counting its multiplicity across the eight normalizations gives exactly two failures per nonincidence.

For a compact complete certificate, the table below records, for each normalized three-colouring, the 21 colours in the incidence-edge ordering above and the seven obstructing line *indices* \(j=0,\ldots,6\) attached respectively to points \(p=0,\ldots,6\). Thus each seven-digit obstruction string lists the unique failed pair \((p,7+j)\) for each \(p\):

| Index | Proper three-colouring | Failed line-index string |
|:---:|:---|:---|
| 0 | `012102120210210021201` | `3405261` |
| 1 | `012102210201102201201` | `1356204` |
| 2 | `012120021201102102210` | `2451630` |
| 3 | `012120021210120021120` | `5246031` |
| 4 | `012201120102210120021` | `2635014` |
| 5 | `012201201120120120120` | `1234560` |
| 6 | `012210201120012102210` | `3641502` |
| 7 | `012210210102012201021` | `5304612` |

Since none of these three-colourings satisfies all distance-three pairs, \(\operatorname{src}(H)\ge4\).

**(4) Four-colour certificate.** In the same edge ordering the colour string

`312132130210210023201`

assigns colours \(0,1,2,3\) and is proper. It is obtained from the index-0 three-colouring by assigning the fresh fourth colour to the four disjoint edges \((0,7)\), \((1,8)\), \((2,9)\), and \((5,12)\). Enumerating all three geodesics for each of the 28 nonincident pairs verifies that at least one has three different colours. Propriety handles distance-two pairs, and incidence handles distance-one pairs. The second verifier independently checks every one of the 91 unordered vertex pairs via a breadth-first distance computation and a rainbow shortest-path search. Therefore \(\operatorname{src}(H)\le4\), proving equality.

**(5) Complete sharp fresh-colour repair census.** Any successful colouring obtained from a three-colouring by assigning one fresh fourth colour to some edges must recolour a matching: otherwise two adjacent new-colour edges would violate the uniquely geodesic distance-two condition. For each of the eight normalized three-colourings, enumerate *all* edge subsets by size \(0\le k\le7\), retain those with 2\(k\) distinct endpoints, and test the 28 point-line geodesic conditions. This gives exactly the two columns in the table under Finding for every normalized class. No matching exceeds size seven because the graph has fourteen vertices. A separate implementation from the seven binary-projective lines enumerates the same repair counts for all 48 named proper three-edge-colourings. Hence the displayed repair polynomial and four-edge minimum are exhaustive, with no assumption of representative typicality.

## Verification

Both provided programs require only Python 3 and the standard library. Run `python3 fano_rainbow_1.py` and `python3 fano_rainbow_2.py` in the directory containing the supplied files. Their recorded exact output is included in `fano_rainbow_1.out` and `fano_rainbow_2.out`, respectively. Each program asserts all critical counts; the first derives the Fano plane from a cyclic difference set, whereas the second derives it independently from \(\mathbf F_2^3\) and recovers colourings via 1-factorizations. The latter explicitly enumerates shortest rainbow walks for all vertex pairs in its upper-bound certificate.

Proof validity depends on finite exhaustion of the 21-edge state space *after* normalization and properness reduction, not on a heuristic optimisation, a partial sample, or an extrapolation beyond this graph. Exact Python source files, not preexisting output alone, supply executable enumeration details.

## Relationship to prior work

Chartrand, Johns, McKeon and Zhang (2008) introduced strong rainbow connection and established values for several graph families; their full paper treats the Petersen graph and complete multipartite graphs but does not give this Heawood result or its repair spectrum. Caro et al. (2008) studied ordinary rainbow connection. These invariants must not be conflated with rainbow three-*connectivity*, which demands three internally disjoint rainbow paths and which was studied for the Heawood graph by Chartrand et al. (2007) and Balbuena et al. (2018). In particular their six-or-seven-colour bounds concern a distinct invariant and neither prove nor contradict \(\operatorname{src}(H)=4\).

The fact that Heawood has 24 perfect matchings and eight edge three-colourings modulo palette permutation is previously recorded in the established graph tables and is not claimed as original here. The added claims are the exact *geodesic obstruction design*, the strong-four-colour bound with a reproducible certificate, and especially the complete nonmonotone fourth-colour matching-repair spectrum. Public mathematical-record and literature searches located no covering proof or tabulation for these statements.

## Limitations

This is a result for the single canonical Fano-plane incidence graph, not for incidence graphs of all projective planes or arbitrary cages. The exhaustive classification is exact within the defined fresh-colour matching repair model only, and establishes no theorem about arbitrary recolouring transformations. The 2007 cage article is not openly available in full; its later documented results address rainbow three-connectivity, but possible unindexed earlier computations of one component of this result cannot be ruled out. The 2023 general integer-programming treatment may contain computational examples not inspected completely. Originality is therefore a reasoned comparison rather than a proof of worldwide uniqueness. No external independent audit has been performed.

## References

1. G. Chartrand, G. L. Johns, K. A. McKeon and P. Zhang, *Rainbow connection in graphs*, Mathematica Bohemica 133 (2008), 85–98, DOI: 10.21136/MB.2008.133947. Full text: https://dml.cz/bitstream/handle/10338.dmlcz/133947/MathBohem_133-2008-1_8.pdf.
2. Y. Caro, A. Lev, Y. Roditty, Z. Tuza and R. Yuster, *On rainbow connection*, Electronic Journal of Combinatorics 15 (2008), R57, published 18 April 2008, DOI: 10.37236/781.
3. G. Chartrand, G. L. Johns, K. A. McKeon and P. Zhang, *On the rainbow connectivity of cages*, Congressus Numerantium 184 (2007), 209–222 (full text not obtained).
4. C. Balbuena, J. A. Fresán, D. González-Moreno and M. Olsen, *Rainbow connectivity of Moore cages of girth 6*, Discrete Applied Mathematics 250 (2018), DOI: 10.1016/j.dam.2018.04.020.
5. J. Cervantes-Ojeda et al., *Rainbow Connectivity Using a Rank Genetic Algorithm: Moore Cages with Girth Six*, Journal of Applied Mathematics (2019), DOI: 10.1155/2019/4073905.
6. J. Žerovnik's compiled Heawood graph data page, https://jaanos.github.io/tables/graphs/Heawood.html (matching and factorization counts are prior data).
7. D. Mildebrath and I. V. Hicks, *An integer program and new lower bounds for computing the strong rainbow connection numbers of graphs*, arXiv:2006.02988, subsequent Networks publication, DOI: 10.1002/NET.22031 (general algorithm, full Heawood-example comparison not completed).
