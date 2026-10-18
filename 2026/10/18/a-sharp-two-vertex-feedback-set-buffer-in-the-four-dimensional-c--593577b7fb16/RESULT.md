# A sharp two-vertex feedback-set buffer in the four-dimensional cube

## Finding

Let \(Q_4\) be the graph on \(\{0,1\}^4\) whose edges join binary words differing in exactly one coordinate. A feedback vertex set is a subset \(S\) such that \(Q_4-S\) is a forest. For \(k\geq 0\), let \(\mathcal T_k\) have as vertices *all* feedback vertex sets of cardinality at most \(k\), with an edge when exactly one vertex is added or removed. Then the minimum feedback-set size is \(6\), and there are exactly eight minimum sets. These eight sets are isolated in \(\mathcal T_6\).

The first two nontrivial capacity levels are completely determined:
\[
\mathcal T_7\cong 8K_{1,10}\sqcup 928K_1,
\qquad
|V(\mathcal T_8)|=5106,
\qquad |E(\mathcal T_8)|=9152,
\]
where \(\mathcal T_8\) is **connected**. Its vertex counts by cardinality \(6,7,8\) are respectively \(8,1008,4090\), and its edges link the cardinality layers in quantities \(80\) (from \(6\) to \(7\)) and \(9072\) (from \(7\) to \(8\)). Thus precisely **two additional allowable vertices** are necessary and sufficient to reconfigure *every* feedback vertex set of size at most eight, including any pair of minimum sets, by single additions and deletions.

The eight minimum sets have a canonical parity description. Write \(E\) and \(O\) for the even- and odd-parity vertices, each of cardinality eight; let \(\bar u\) denote the bitwise complement of \(u\). The complete collection is
\[
\{E\setminus\{u,\bar u\}:u\in E\}
\ \cup\
\{O\setminus\{u,\bar u\}:u\in O\},
\]
with each distinct set counted once. For different minimum sets \(A,B\), their distance inside \(\mathcal T_8\) is exactly \(4\) if they lie in the same parity family and exactly \(12\) otherwise. There are twelve unordered same-family pairs and sixteen opposite-family pairs.

## Assumptions and scope

All graphs are finite, simple, undirected and unweighted. Vertices of \(Q_4\) are encoded by integers \(0,\ldots,15\) using four binary bits, and adjacent integers differ in exactly one bit. A legal transition toggles membership of exactly one vertex and must leave a feedback vertex set; the capacity bound applies at every intermediate step. In particular, exchange of one selected vertex for another requires two transitions (first add then remove), and no temporary capacity beyond \(k\) is allowed. Claims concern only \(Q_4\), and there is no higher-dimensional assertion.

## Proof

**Minimum-set classification.** The cube has sixteen vertices, is four-regular and has thirty-two edges. If \(S\) is removed, the complement on \(16-|S|\) vertices has \(32-4|S|+e(S)\) edges, where \(e(S)\) is the number of edges induced by \(S\). Any forest on \(16-|S|\) vertices has at most \(15-|S|\) edges. Hence \(3|S|\geq17+e(S)\), which excludes \(|S|\leq5\). When \(|S|=6\), necessarily \(e(S)\leq1\).

Suppose \(|S|=6\) and it intersects both parity classes. A single vertex has four neighbors in the other class; two distinct same-parity vertices have at least six distinct neighbors; and three distinct same-parity vertices have at least seven distinct neighbors. For the last assertion, otherwise two vertices of the opposite parity would be nonadjacent to all three. But the sets of same-parity vertices nonadjacent to those two vertices have an intersection of at most two: their neighborhoods are disjoint when antipodal and overlap in two when at Hamming distance two. Consequently, parity splits \((2,4),(3,3),(4,2)\) yield \(e(S)\geq2\). The only possible mixed split with \(e(S)\leq1\) is \((1,5)\) or \((5,1)\), and it forces \(e(S)=1\).

For a split \((1,5)\), let \(u\) be the single selected even vertex. To have only one induced edge, the selected odd vertices must be all four odd nonneighbors of \(u\) together with exactly one neighbor. Thus the three unselected odd vertices are three distinct neighbors \(u\oplus e_i\) of \(u\). The three other common neighbors \(u\oplus e_i\oplus e_j\) of each pair of these odd vertices remain unselected; they form with the three odd vertices an induced six-cycle in \(Q_4-S\). This contradicts acyclicity. The \((5,1)\) case is symmetric. Thus a six-vertex feedback set lies entirely in one parity class.

Its complement consists of the entire opposite class together with two same-parity vertices \(u,v\). If \(u,v\) have Hamming distance two, their two common neighbors induce a four-cycle; if they are antipodal, their neighborhoods are disjoint, and the complement is the disjoint union of two four-leaf stars. The latter are the only valid choices: four omitted antipodal pairs per parity class, eight sets in total.

**Capacity six and seven.** Distinct minimum sets from the same parity family have intersection size four; minimum sets from opposite parity families are disjoint. In particular no two minimum sets differ in one vertex exchange. Every minimum set has ten seven-vertex supersets, all feedback sets by monotonicity, and no seven-vertex set contains two distinct minimum sets. Because every legal capacity-seven edge joins a six-vertex set to a seven-vertex set, each minimum set is the center of a separate eleven-vertex star. The exact seven-vertex census, proved by either exhaustive verifier below, is \(1008\); the remaining \(1008-80=928\) seven-vertex states are isolated. Capacity six therefore consists of eight isolates, and capacity seven has exactly the stated \(936\) components.

**Capacity eight.** An exhaustive finite certificate builds all feedback sets of sizes six, seven and eight and their single-toggle adjacency graph. Both independently implemented verifiers compute the exact layer counts \((8,1008,4090)\), edge-layer counts \((80,9072)\) and a single component containing all \(5106\) states. Checker `check_edges.py` generates all \(2^{16}\) vertex masks and detects induced cycles by union-find on the thirty-two cube edges. Checker `check_cartesian.py` constructs the isomorphic graph \(C_4\square C_4\) from Gray-coded cycle coordinates, enumerates relevant cardinality classes, recognizes forests by iterative leaf removal, and obtains components by a separately coded disjoint-set procedure. These are finite exhaustive verifications, not statistical experiments; complete code and outputs are included.

For the distances, same-parity minimum sets differ in four vertices, giving a four-transition lower bound; adding the two new vertices first and removing the two old vertices gives equality within capacity eight. Opposite-parity minimum sets are disjoint, giving a twelve-transition lower bound. The following twelve legal toggles realize equality between the representatives \(E\setminus\{0,15\}=\{3,5,6,9,10,12\}\) and \(O\setminus\{1,14\}=\{2,4,7,8,11,13\}\):

```
+2, +7, -6, +4, -5, +11, -3, +8, -10, +13, -9, -12
```

Every intermediate set has cardinality six, seven or eight and an acyclic complement (directly checked by both programs). Hypercube automorphisms act transitively on ordered pairs of minimum sets from different parity families: translations fix a representative omitted antipodal pair, and coordinate permutations move any opposite-parity omitted pair to any other. Therefore all sixteen cross-family pairs admit twelve-step paths. The independent all-pairs breadth-first searches in the two verifiers recover precisely twelve same-family pairs at distance four and sixteen cross-family pairs at distance twelve.

## Verification

Run `python3 check_edges.py` and `python3 check_cartesian.py` separately with Python 3.10 or later, using only the standard library. Each prints one deterministic JSON object followed by `VERIFY_OK`; the files `check_edges.out` and `check_cartesian.out` record their outputs. The two JSON objects coincide on all fields, including the complete ordered list of the eight minimum-set bitmasks, cardinality layers, layer-edge counts, component profiles and optimal-pair distance distributions. The first checker performs a BFS from each minimum set and reaches all 5106 capacity-eight states; the second reaches all states using an independently constructed Cartesian-square graph and a different acyclicity test.

## Relationship to prior work

The classical feedback-set problem for hypercubes was studied by Focardi, Luccio and Peleg [1]; obtaining the minimum size alone is not asserted as novel. Bousquet and collaborators [2] study feedback-set reconfiguration, proving structural connectivity results for specified subcubic graph classes and exhibiting hardness for bounded-degree planar classes. Those general results do not determine the sharp capacity transition or shortest optimal-set transformations for the nonplanar, four-regular graph \(Q_4\). The assertion here is the specific exact capacity-six, -seven and -eight transition together with the corresponding optimal-set pair-distance dichotomy, not any general complexity classification.

## Limitations

The connectivity of the capacity-eight graph and the seven-/eight-vertex census are established by exact finite enumeration, accompanied by two executable independent implementations, rather than a parameterized theorem for all hypercubes. The earlier 1999 hypercube research report and the entirety of the 2000 publisher PDF could not be inspected; their titles and accessible abstracts concern minimum feedback-set bounds, and finer unpublished tables cannot be excluded. The complete 2023 publisher PDF was also not available, although its indexed detailed theorem statements and section descriptions were compared. Unindexed or unpublished equivalent computations remain a residual originality risk. No external independent audit is claimed.

## References

[1] R. Focardi, F. L. Luccio and D. Peleg, *Feedback vertex set in hypercubes*, Information Processing Letters 76 (2000), 1–5. DOI: 10.1016/S0020-0190(00)00127-7. The institutional publication record dates the article 20 November 2000; an earlier 1999 research-report listing has no verified day of first release.

[2] N. Bousquet, F. Hommelsheim, Y. Kobayashi, M. Mühlenthaler and A. Suzuki, *Feedback vertex set reconfiguration in planar graphs*, Theoretical Computer Science 979 (2023), 114188. DOI: 10.1016/j.tcs.2023.114188.
