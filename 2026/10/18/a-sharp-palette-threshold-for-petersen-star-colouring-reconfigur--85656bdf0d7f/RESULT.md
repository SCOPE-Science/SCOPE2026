# A sharp palette threshold for Petersen star-colouring reconfiguration

## Finding
Let \(P=KG(5,2)\) be the Petersen graph. Define \(\mathcal R_k^\star(P)\) to have as vertices all star vertex-colourings \(f:V(P)\to\{0,\ldots,k-1\}\), with distinct named colours; two colourings are adjacent exactly when they differ at one graph vertex and both satisfy the star constraint. Unused palette colours are permitted.

**Theorem.** The star chromatic number of \(P\) is \(\chi_\star(P)=5\). All \(7{,}680\) vertices of \(\mathcal R_5^\star(P)\) are isolated. With one extra named palette colour, \(\mathcal R_6^\star(P)\) is connected and has exactly \(341{,}280\) vertices and \(1{,}094{,}400\) edges. Its radius is \(14\) and its diameter is \(15\). Its complete degree distribution, written as degree: multiplicity, is
\[
3:14{,}400,\quad4:64{,}800,\quad6:108{,}000,\quad7:86{,}400,\quad8:21{,}600,\quad10:46{,}080.
\]
The complete eccentricity distribution is \(14:21{,}600\) and \(15:319{,}680\). In particular the minimum palette size permitting connectivity by star-preserving single-vertex recolourings is exactly \(6\).

## Assumptions and scope
The ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), ordered lexicographically, and two are adjacent if and only if disjoint. A star colouring is proper and contains no path on four distinct vertices whose vertex colours alternate between exactly two values; the path need not be induced. Every recolouring changes the value at exactly one vertex to a different value in the **same fixed palette**, without ever violating either condition. Named colours are never identified up to permutation in the theorem, even though symmetries are used to shorten exhaustive verification. A single-vertex recolouring that only changes a singleton colour name counts as an edge if the two colourings differ as named maps.

The theorem concerns this single finite graph. It does not concern edge star colourings, ordinary proper vertex-colouring reconfiguration, or the entire generalized Petersen family.

## Proof
**1. Complete finite sample space.** The graph has \(15\) edges and exactly \(60\) undirected simple paths of three edges (i.e. four distinct vertices), counted up to reversal. For each potential map \(f:V(P)\to\{0,\ldots,k-1\}\), validity is equivalent to the following finite conjunction: \(f(u)\ne f(v)\) for each of the \(15\) edges, and \((f(a),f(b),f(c),f(d))\) is not \((x,y,x,y)\) for any of the \(60\) paths \((a,b,c,d)\). The two verifier programs construct these objects directly from the defining disjointness relation.

The C++ checker visits the vertices in their stated order and tries all six values at each step. It prunes a partial assignment only when a fully assigned edge is monochromatic or a fully assigned four-vertex path is bicoloured. Both violations survive every extension, so induction on the assigned prefix proves that every valid total assignment and no invalid total assignment reaches the last recursion level. It enumerates exactly \(341{,}280\) valid maps with six available colour names. Every map uses either five or six distinct colours.

Independently, the Python checker enumerates all \(B_{10}=115{,}975\) set partitions of the ten vertices by placing each successive vertex in each existing block or a fresh singleton block. It tests the same mathematical validity condition, but over unordered colour classes instead of labelled colour vectors. Exactly \(64\) valid partitions have five nonempty colour classes, exactly \(410\) have six, and none has fewer than five. (It also records \(655,255,30,1\) valid partitions with seven, eight, nine, ten classes.) This independently proves \(\chi_\star(P)=5\). The number of named five-colour states is \(64\cdot5!=7{,}680\); the six-colour palette gives \(64\cdot6!+410\cdot6!=341{,}280\) states, since any five-block partition can inject its classes into the six-colour palette in \(6!\) ways.

**2. Exactly one-site transitions.** In a valid colouring, changing only the value at one vertex can create a violation only on an incident edge or a four-vertex path containing that vertex. Thus it suffices to check that finite list after each proposed move. The C++ program runs this complete local test for every alternative of each of the ten positions and every one of the \(341{,}280\) valid six-palette states. It finds the displayed degree counts and a degree sum of \(2{,}188{,}800\), giving \(1{,}094{,}400\) undirected edges by double counting. Restricted to the five named palette colours, the test finds no valid move from any of the \(7{,}680\) five-palette states: they are all isolated. The independent partition program recomputes the distribution by class moves, obtaining \(64\) five-block states, each with named six-palette degree \(10\), and \(410\) six-block states with degree counts \(3:20,4:90,6:150,7:120,8:30\); multiplying by \(6!\) gives exactly the theorem's distribution and edge count.

**3. Exhaustive distances with justified symmetry reduction.** Permuting the five ground-set elements is an automorphism of \(KG(5,2)\), and every global permutation of the six colour names is an automorphism of the recolouring graph. Normalizing colour names by order of first appearance produces exactly \(474\) unlabelled valid partitions. Each represents exactly \(6!=720\) named six-palette states, whether it has five or six nonempty blocks. The \(120\) induced ground-set permutations split those \(474\) partitions into precisely \(11\) orbits: sizes \(10,24,30\) for five-block partitions and \(20,30,30,30,60,60,60,120\) for six-block partitions. Both programs independently verify this orbit census.

The C++ program performs breadth-first search in the **full named-colour reconfiguration graph**, not merely the partition quotient, starting from a representative of each of the \(11\) orbits. A state is encoded injectively in base six, and a BFS generates every legal one-vertex substitution on demand. Every one of the \(11\) searches visits all \(341{,}280\) valid named states, proving connectivity. Ten representatives have eccentricity \(15\); one representative, belonging to a six-block orbit with \(30\) partitions, has eccentricity \(14\). Graph automorphisms preserve distances; hence exactly \(30\cdot720=21{,}600\) named states have eccentricity \(14\), and all remaining \(319{,}680\) have eccentricity \(15\). The radius and diameter follow. The completed exhaustive recursions, orbit construction and BFS certificates establish exact finite conclusions rather than estimates from partial sampling.

## Verification
The reproducible, self-contained programs are `labeled_check.cpp` and `partition_check.py`, with recorded outputs `labeled_output.txt` and `partition_output.txt`. Use a C++17 compiler and Python 3 standard library:

```
g++ -O3 -std=c++17 labeled_check.cpp -o labeled_check
./labeled_check
python3 partition_check.py
```

Both programs contain their own executable assertions. The C++ program constructs and traverses all named six-palette states, checks the five-palette obstruction, obtains degrees, counts undirected edges, computes automorphism orbits and runs eleven complete BFS traversals. The Python program independently generates set partitions instead of labelled vectors, evaluates the star predicate from scratch, checks all possible block moves and verifies the degree and symmetry orbit counts. Their independent counts agree. Finite completeness follows from the recursion and exhaustive BFS logic detailed in the proof; logs by themselves are not the proof.

## Relationship to prior work
Albertson, Chappell, Kierstead, Kündgen and Ramamurthi (2004) define star vertex colouring and prove general upper bounds and structural properties, including a seven-colour bound for subcubic graphs. Their full open article, including its sections on colourings, proofs and questions, does not establish the Petersen star-recolouring connectivity threshold or the named-state radius/diameter. Chen, Raspaud and Wang (online 2012) sharpen the existence bound for all subcubic graphs to six, but existence of a colouring does not entail connectivity under star-preserving local moves.

Johnson, Kratsch, Kratsch, Patel and Paulusma (arXiv 2014) study one-vertex recolouring for **ordinary proper colourings**, without forbidding two-coloured four-vertex paths. Their graph and distance results do not imply the present constrained recolouring graph. Hojny and Pfetsch (2015 open preprint; 2016 journal) study a polytope for star-colourable induced subgraphs, rather than the local recolouring geometry; their fully accessible preprint has no Petersen-specific result. The closest available mathematical-record and historical comparisons show neighbouring colouring and recolouring invariants but no statement covering the present joint threshold, counts and distances. This comparison is not a guarantee of publication priority.

## Limitations
The result is an exact finite classification for the Petersen graph and the precise move rule stated above; it gives no general family theorem, mixing-time bound, or Kempe-change classification. The distance certificate is computationally exhaustive and depends on correct implementation of explicit finite predicates; it is supported by an independently constructed partition census, but the second checker does not independently repeat all eleven full named-state BFS distance computations. An equivalent result in unindexed literature or inaccessible full text cannot be ruled out.

## References
1. M. O. Albertson, G. G. Chappell, H. A. Kierstead, A. Kündgen, R. Ramamurthi, “Coloring with no 2-Colored P4's,” *Electronic Journal of Combinatorics* 11 (2004), R26. First public date 2004-03-31. DOI: https://doi.org/10.37236/1779 . Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r26/pdf/ .
2. M. Chen, A. Raspaud, W. Wang, “6-Star-Coloring of Subcubic Graphs,” *Journal of Graph Theory* 72 (2013), 128–145; online 2012-06-01. DOI: https://doi.org/10.1002/jgt.21636 .
3. M. Johnson, D. Kratsch, S. Kratsch, V. Patel, D. Paulusma, “Finding Shortest Paths between Graph Colourings,” *Algorithmica* 75 (2016), 295–321; preprint 2014-03-25. https://arxiv.org/abs/1403.6347 .
4. C. Hojny, M. E. Pfetsch, “A Polyhedral Investigation of Star Colorings,” *Discrete Applied Mathematics* 208 (2016), 59–78. DOI: https://doi.org/10.1016/j.dam.2016.03.003 ; open preprint (January 2015): https://optimization-online.org/wp-content/uploads/2015/01/4759.pdf .
