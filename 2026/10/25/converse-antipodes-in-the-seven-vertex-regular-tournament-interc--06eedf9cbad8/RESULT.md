# Converse antipodes in the seven-vertex regular-tournament interchange graph

## Finding

Let \(\mathcal T\) consist of all labeled tournaments on the fixed set \(\{0,\ldots,6\}\) with outdegree three at each vertex. Let \(\mathcal G\) have \(\mathcal T\) as vertices, with \(T\sim U\) when \(U\) is obtained from \(T\) by reversing all three arrows of one directed triangle. Then \(\mathcal G\) is connected, has \(2640\) vertices, is \(14\)-regular, and has \(18480\) undirected edges. Its radius is \(8\) and diameter \(9\).

There are exactly three relabeling orbits. Writing \(s_T(j)=|\{U\in\mathcal T:d_{\mathcal G}(T,U)=j\}|\), their full distance profiles are:

| Orbit size | \(\bigl(s_T(0),\ldots,s_T(\operatorname{ecc}(T))\bigr)\) | Converse distance | Farthest points |
|---:|---|---:|---:|
| 240 | \((1,14,91,343,749,871,476,92,3)\) | 7 | 3 |
| 720 | \((1,14,91,336,721,822,485,147,22,1)\) | 9 | 1 |
| 1680 | \((1,14,91,340,739,853,483,113,6)\) | 7 | 6 |

Consequently there are precisely \(360\) unordered distance-nine pairs. **They are exactly the pairs \(\{T,T^{\mathrm{op}}\}\)** from the middle orbit, where \(T^{\mathrm{op}}\) reverses all \(21\) arrows. In particular, the unique farthest configuration from \(T\) exists exactly in that orbit and is \(T^{\mathrm{op}}\).

This orbit also has an intrinsic small-subtournament characterization: for every four-vertex subset of \(T\), count its directed cyclic triangles. The frequency vectors for counts \(0,1,2\) across the 35 four-subsets are respectively \((0,14,21)\), \((7,0,28)\), and \((3,8,24)\) on the orbits of sizes \(240,720,1680\). Thus the unique-converse-antipode property holds exactly when **no induced four-vertex subtournament contains precisely one cyclic triangle**.

## Assumptions and scope

All tournaments are **labeled** on \(\{0,\ldots,6\}\). A directed triangle is a cyclically directed three-vertex subdigraph. Reversal is allowed only for such a triangle; it preserves every vertex's outdegree, hence stays in \(\mathcal T\). No other multi-edge reversal is an edge of \(\mathcal G\). Distances are shortest legal reversal sequences. The converse tournament reverses every arc, not merely one triangle. Isomorphism under permutations of the seven labels is used only to reduce the exhaustive distance computation from all vertices to three representatives.

## Proof

This is an exact finite theorem proved by an exhaustive terminating algorithm, supplemented by an independent state-enumeration and all-roots computation. The two standalone pure-Python programs `verify_bitmask.py` and `verify_recursive.py` accompany this statement, with their recorded outputs. The following gives the complete, reproducible exhaustion argument, including why no state, edge, or distance is omitted.

**Encoding and completeness.** List the \(21\) unordered pairs \((i,j)\) with \(i<j\) lexicographically. A \(21\)-bit integer \(m\) encodes precisely one labeled tournament: bit \((i,j)\) is 1 iff the arrow is \(i\to j\). Conversely every labeled tournament yields exactly one integer in \(\{0,\ldots,2^{21}-1\}\). For each vertex \(i\), count its arcs pointing toward larger labels whose bits are 1 and its arcs pointing toward smaller labels whose bits are 0. The tournament is regular iff every one of these seven integers is \(3\). Iterating every one of the \(2^{21}\) masks with this exact integer test yields exactly \(2640\) admissible masks; therefore none has been omitted or duplicated.

**Exact adjacency.** For \(i<j<k\), let \(a,b,c\) be the bits for \((i,j),(i,k),(j,k)\). The induced triangle is cyclic precisely when \((a,b,c)=(1,0,1)\) or \((0,1,0)\). In either case, reversing its three arcs is exactly the XOR operation \(m\mapsto m\oplus(2^a+2^b+2^c)\), where superscripts here refer to the bit *positions*. The program tests all \(\binom73=35\) triples for every admissible mask and constructs precisely the legal neighbors. Its assertions verify that each of the \(2640\) vertices has exactly \(14\) distinct neighbors, that every neighbor remains admissible, and that adjacency is symmetric. Indeed each regular tournament has exactly \(\binom73-7\binom32=14\) cyclic triangles, because each transitive triangle has a unique source and every source has three outneighbors. Summing degrees gives \(2640\cdot14/2=18480\) undirected edges.

**Orbits, distances, and antipodes.** Each of the \(7!\) permutations of labels induces an explicitly computed permutation (possibly complementing individual ordered-edge bits) on all \(21\) positions. Applying all such permutations to a representative, and marking its orbit before taking the next unused representative, exhausts the \(2640\) masks in exactly three orbits of sizes \(240,720,1680\). Label permutations preserve legal reversal and hence all distances. Breadth-first search from one representative of each orbit visits all \(2640\) vertices, proving connectivity, and produces exactly the three distance profiles in the Finding table. The largest nonempty shell gives eccentricities \(8,9,8\); thus the global radius and diameter are \(8\) and \(9\). Complementing the 21-bit tournament mask gives its converse. Looking up this mask in the exact distance map gives converse distances \(7,9,7\). The middle orbit's final shell contains one vertex, necessarily its converse; all other orbits have eccentricity \(8\). Thus precisely \(720/2=360\) unordered pairs are at distance nine, exactly the stated converse pairs.

**Four-subset characterization.** Each of the 35 four-vertex subsets contains four triples. Apply the same exact cyclic-triangle bit test to those four triples and accumulate, by representative, a histogram indexed by the number of cyclic triangles. The three histograms are \((0,14,21)\), \((7,0,28)\), and \((3,8,24)\). Since permutations preserve induced subtournament type, these histograms characterize the three classes and in particular isolate the middle class as the one with zero four-sets containing exactly one cyclic triangle. This proves the intrinsic restatement of the antipode result.

**Independent replay.** `verify_recursive.py` constructs the \(2640\) regular tournaments *without* scanning 21-bit integers. It recursively assigns adjacency-row bitsets subject to exact eventual outdegree three, directly reverses cyclic triangles by toggling six directed adjacency entries, and runs a breadth-first search independently from **all 2640 roots** rather than orbit representatives. It reproduces the same three shell profiles, the total of 360 unordered distance-nine pairs, and the fact that each such pair consists of converse tournaments. Thus the orbit method's transitive distance reduction is independently checked, while the first checker by itself remains a complete proof because its finite loops exhaust the stated spaces.

## Verification

Execute `python3 verify_bitmask.py` and `python3 verify_recursive.py` in a directory containing these two scripts. Python 3.10 or newer is sufficient; no external packages, network access, or extra files are needed. The programs terminate with `PASS` after comprehensive assertions and print the values above. The outputs are also recorded in `verify_bitmask_output.txt` and `verify_recursive_output.txt`. The first output includes SHA-256 digests of canonical sorted vertex and edge encodings as additional reproducibility checks; they are not substitutes for the enumeration's proof of completeness. Every mask, arrow test, directed-triangle reversal and breadth-first search uses exact finite integer arithmetic.

## Relationship to prior work

Ryser's classical connectivity-by-directed-triangle-reversals theorem, and the tournament interchange-graph framework of Brualdi and Li, concern tournaments with the same score sequence. In particular, their framework already implies that the graph considered here is connected; connectivity itself is **not claimed as novel**. Guiduli, Gyárfás, Thomassé and Weidl (1998), especially their discussion of triangle reversals and interchange-graph diameter, obtain general results and bounds; their general upper bound for the seven-vertex setting is not an exact metric classification. Work by Kannan, Tetali and Vempala (1999) concerns mixing/generation of tournaments with prescribed scores. The 2009 hypercube characterization of *minimum-score* tournament interchange graphs applies to a different score regime, and the 2025 Coxeter generalization addresses different interchange families.

The contribution assessed here is the **exact three-orbit shortest-path metric, the distinction between eccentricities eight and nine, and the converse-antipode characterization**. The known enumeration of three unlabeled seven-vertex regular tournaments is used but not treated as new. Prior sources, particularly the original Brualdi–Li chapter, remain a potential publication-priority risk if they contain unindexed exact small-order tables.

## Limitations

The theorem is restricted to regular labeled tournaments of order **exactly seven** with directed-three-cycle reversal moves. It does not establish analogous radii or antipodal behavior for order nine or any infinite family. Its mathematical correctness is an exhaustive finite proof with fully disclosed checkers; it is not a formal proof-assistant certificate. Earlier and otherwise unindexed literature may contain equivalent descriptions; the original Brualdi–Li full text was not obtained. Only the stated computations and source material were checked. Independent external audit has not been performed.

## References

- R. A. Brualdi and Q. Li, “The interchange graph of tournaments with the same score vector,” in *Progress in Graph Theory* (1984), pp. 128–151.
- B. Guiduli, A. Gyárfás, S. Thomassé and P. Weidl, “2-Partition-Transitive Tournaments,” *Journal of Combinatorial Theory, Series B* **72** (1998), 181–196, doi:10.1006/jctb.1997.1806. Full text: https://users.renyi.hu/~gyarfas/Cikkek/85_2partitiontranstourn.pdf.
- R. Kannan, P. Tetali and S. Vempala, “Simple Markov-chain algorithms for generating bipartite graphs and tournaments,” *Random Structures & Algorithms* **14** (1999), 293–308, doi:10.1002/(SICI)1098-2418(199907)14:4<293::AID-RSA1>3.0.CO;2-G.
- W.-K. Chen, G. J. Chang and S.-L. Wang, “The Interchange Graphs of Tournaments with Minimum Score Vectors Are Exactly Hypercubes,” *Graphs and Combinatorics* **25** (2009), doi:10.1007/s00373-008-0818-4.
- Kolesnik, Mitchell and Przybyłowski, “Coxeter Interchange Graphs” (2025), doi:10.1007/s00026-025-00768-9.
