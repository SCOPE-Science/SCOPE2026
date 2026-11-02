# Uniform shortest-path profiles of optimal identifying-code exchanges on the four-cube

## Finding
Let \(Q_4\) be the four-dimensional binary cube. The graph \(\mathcal E\) of minimum radius-one identifying codes of \(Q_4\), adjacent when one sensor is exchanged for another, has exactly \(960\) vertices and \(4320\) edges. It is connected and regular of degree \(9\). From **every** vertex the numbers of vertices at distances \(0,1,\ldots,7\) are, respectively,
\[
(1,9,35,132,300,338,130,15).
\]
Consequently \(\operatorname{rad}(\mathcal E)=\operatorname{diam}(\mathcal E)=7\). The minimum identifying codes split into three orbits under the automorphisms of \(Q_4\), of sizes \(192,384,384\). Thus these three geometrically distinct classes have the same entire distance profile.

The unordered-pair counts at exchange distances \(1,\ldots,7\) are
\[
(4320,16800,63360,144000,162240,62400,7200),
\]
which sum to \(\binom{960}{2}=460320\).

## Assumptions and scope
The graph \(Q_4\) has the sixteen vertices \(\{0,1\}^4\); two are adjacent when their Hamming distance is one. For every vertex \(v\), its closed radius-one ball \(B(v)\) consists of \(v\) and its four neighbors. A set \(C\) is an identifying code precisely when all sixteen intersections \(B(v)\cap C\) are **nonempty and pairwise distinct**. A code is minimum when its cardinality is least among all identifying codes. In \(\mathcal E\), vertices are precisely the minimum codes; two are adjacent if they have exactly six elements in common. Thus a move replaces exactly one selected cube vertex by a different unselected cube vertex while retaining the identifying property.

The statement concerns this fixed labelled sixteen-vertex graph and its finite collection of optimal codes, not all hypercubes or other notions of locating or locally identifying codes. The known minimum cardinality \(7\) is not a novelty claim; it is independently established by exhaustive enumeration below.

## Proof
This is a finite exhaustive proof with completely specified enumerations, supplied as two executable certificates. The necessary logic reduces the conclusions to counts over explicitly bounded finite ranges; the certificate programs implement those ranges without sampling.

**Exhaustive identification.** Number the vertices by integers \(0,\ldots,15\), with four-bit binary representation, and encode a code \(C\) by
\[
M(C)=\sum_{v\in C}2^v.
\]
For each \(v\), form the sixteen-bit closed-ball mask \(b_v\), whose set bits are exactly \(v\) and \(v\oplus 2^i\) for \(0\le i<4\). The sixteen code-signatures are the masks \(M(C)\mathbin{\&}b_v\). The defining identifying condition is equivalent, in both directions, to requiring every signature to be nonzero and all sixteen signatures to be distinct. Testing each integer \(M\) in the inclusive interval \(0\le M<65536\) therefore tests **every** subset exactly once. `verification/direct_all_pairs.py` performs this enumeration and verifies that no code has fewer than seven elements and precisely \(960\) codes have seven elements.

**Exhaustive exchanges.** For each enumerated size-seven code, range over each of its seven selected vertices and each of its nine unselected vertices. Toggle those two positions and retain the resulting code if and only if it appears in the complete size-seven-code dictionary. Every legal exchange is encountered, and only legal exchanges are included. The program checks the resulting undirected graph is 9-regular with exactly \(4320\) edges. Since the graph has only \(960\) vertices, breadth-first search from each of the 960 starts exhausts every potentially reachable configuration. Each BFS reaches all 960 vertices, and each produces the distance histogram \((1,9,35,132,300,338,130,15)\). BFS correctness follows by induction on path length: the first discovery of a vertex gives its minimum number of exchange edges from the source. Therefore the claimed shortest-path distribution, radius, diameter, and unordered-pair counts are exact.

**Symmetry classification.** The cube automorphism group acts on vertices by \(x\mapsto t\oplus \sigma(x)\), where \(t\in\{0,1\}^4\) and \(\sigma\) permutes the four bit coordinates. Every such map preserves all closed neighborhoods, so it preserves both identifying codes and their exchange adjacency. There are \(16\cdot24=384\) such automorphisms. For every as-yet-unclassified minimum code, the second certificate enumerates its entire orbit under those 384 maps and removes that orbit from the finite 960-code set. Exactly three orbits remain, of sizes \(192,384,384\). Its independently reconstructed code and exchange graph also gives the same breadth-first-search distance histogram from one representative of **each** orbit. Since graph automorphisms preserve distances, the three representative calculations alone imply the uniform histogram for every code. This yields an independent check of the full all-source metric enumeration.

## Verification
Run either standalone file with Python 3 from the artifact root:

```
python3 verification/direct_all_pairs.py
python3 verification/independent_orbits.py
```

The first program enumerates all \(65536\) subsets using bitmask signatures, reconstructs the 960-code exchange graph, and tests **all 960 breadth-first-search sources**. It prints `DIRECT_ALL_PAIRS_PASS` and the exact distance counts.

The second independently enumerates sensor 7-tuples and tests identification using tuples of *sensor indices* visible to each cube vertex, rather than bitmask intersections. It checks all smaller subset cardinalities, computes the full cube automorphism group and its three orbits, reconstructs exchanges using set replacement, and runs shortest-path search at the three orbit representatives. It prints `INDEPENDENT_ORBIT_CERTIFICATE_PASS`. These programs share neither their identifying-code test representation nor their adjacency generation. Both passed when executed from the packaged paths. Their assertions cover the counts, connectivity and distances claimed, and the second independently verifies the symmetry argument.

## Relationship to prior work
Classical work on binary-Hamming-space identifying codes already determines the optimal size for the four-cube; the minimum size seven is background. Honkala, Hudry and Lobstein (2015), *On the number of optimal identifying codes in a twin-free graph*, investigate the possible abundance of optimal identifying codes in general graphs and provide construction-based bounds. Its accessible full text was examined, including the introduction, the general constructions, main results, and references: it does not determine the specific four-cube exchange metric.

Honkala, Hudry and Lobstein, *On the ensemble of optimal identifying codes in a twin-free graph* (first online June 30, 2015), explicitly connect ensembles of optimal identifying codes with **induced subgraphs of Johnson graphs**. Their abstract states a realization result: arbitrary prescribed families of fixed-size subsets can arise as optimal codes in specially constructed graphs. That general realization result by itself specifies neither the family of minimum codes in the fixed graph \(Q_4\) nor its distance histogram, orbit sizes, regularity, or radius. The complete text of that closely relevant paper could not be accessed for a definitive whole-document comparison, so an equivalent particular calculation therein is a residual risk. No examined accessible prior statement was shown to imply the complete claim above.

## Limitations
This is a mathematically finite classification with complete executable exhaustive certificates, not a closed-form formula for arbitrary cube dimension. It does not establish that no historically unpublished or unindexed enumeration reaches the same conclusions. The closely relevant 2015/2016 ensemble paper could be assessed from its accessible abstract and bibliographic context, but not its entire subscription text. No independent scholarly audit has been performed. The certificates can be rerun with standard Python; they do not constitute an external formal proof-assistant verification.

## References
1. I. Honkala, O. Hudry and A. Lobstein, *On the ensemble of optimal identifying codes in a twin-free graph*, Cryptography and Communications 8 (2016), 139–153; first online 2015-06-30. DOI: 10.1007/s12095-015-0148-3. Primary MSC 05C69.
2. I. Honkala, O. Hudry and A. Lobstein, *On the number of optimal identifying codes in a twin-free graph*, Discrete Applied Mathematics 180 (2015), 111–119. DOI: 10.1016/j.dam.2014.08.020. Author-distributed full text: https://biblio.telecom-paristech.fr/cgi-bin/download.cgi?id=14984.
3. I. Charon, G. Cohen, O. Hudry and A. Lobstein, *New identifying codes in the binary Hamming space*, European Journal of Combinatorics 31 (2010). DOI: 10.1016/j.ejc.2009.03.032.
