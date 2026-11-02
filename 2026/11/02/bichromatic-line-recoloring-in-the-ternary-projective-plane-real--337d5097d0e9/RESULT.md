# Bichromatic-line recoloring in the ternary projective plane realizes the Foster graph F468

## Finding

Let \(\mathcal P=\operatorname{PG}(2,3)\), the projective plane with thirteen points and thirteen lines of four points each. A labeled red–blue coloring is *admissible* when every line contains both colors. Let \(\mathcal R\) have all admissible colorings as vertices, with one edge for each recoloring of exactly one point that remains admissible. Colors are distinguished; simultaneous color exchange is not an identification.

**Theorem.** Every admissible coloring has six or seven red points. The six-point color classes are exactly the sets of six pairwise intersections of four lines in general position (no three concurrent). Consequently there are precisely \(468\) admissible colorings. The graph \(\mathcal R\) is connected, bipartite and cubic, with \(702\) edges, girth \(12\), and diameter \(13\). Indeed \(\mathcal R\) is isomorphic to the graph F468 in the classical Foster census of symmetric cubic graphs.

More structurally, let \(\mathcal Q\) be the family of \(234\) six-point complete-quadrilateral sets. Define \(H\) on \(\mathcal Q\) by \(Q\sim Q'\) exactly when \(Q\cap Q'=\varnothing\). Then \(H\) is isomorphic to Wong's graph (F234B) and \(\mathcal R\) is its canonical bipartite double cover. From every coloring, the numbers of colorings at distance \(0,1,\ldots,13\) are exactly
\[
(1,3,6,12,24,48,72,96,116,68,12,6,3,1).
\]
These are new statements about the *line-coloring recoloring model*. The abstract graphs F234B and F468, including their classical girth and diameter, are previously known and are not presented as newly discovered abstract graphs.

## Assumptions and scope

Everything concerns the unique Desarguesian plane of order three, with its thirteen labeled points and its complete family of thirteen four-point projective lines. The red–blue colorings have named colors. Adjacent colorings differ in exactly one point, and both endpoints must have two colors on every line. No assertion is made about planes of larger order or about recoloring that changes several points at once. The result belongs to finite graph configurations/reconfiguration (MSC 05C25).

A frame of four lines means four distinct lines with no three concurrent. Its six pairwise intersection points form what is called here a complete-quadrilateral six-set; this terminology does not identify a set with its complement.

## Proof

**Step 1: the only possible color-class sizes are six and seven.** Suppose \(S\) meets every line but contains no whole line. Such a set is a nontrivial blocking set. No such set has at most five points. Indeed, a line-free set with at most four points can be extended to a line-free five-set, since at each extension stage there are at most \(\binom{4}{3}\) forbidden completion points but at least nine outside points; meeting every line is preserved by extension. For a hypothetical five-set, write \(a_j\) for its number of lines with exactly \(j\) points, \(j=1,2,3\). Counting lines, incidences, and pairs gives
\[
a_1+a_2+a_3=13,\quad a_1+2a_2+3a_3=20,\quad a_2+3a_3=10,
\]
so \((a_1,a_2,a_3)=(9,1,3)\). Three distinct trisecants cannot each contain three points of a five-set: their pairwise intersections must belong to that set, and their union has at least six points (at least seven if concurrent). Thus \(|S|\ge6\). Both color classes are such sets, hence both have at least six points, and one has six while the other has seven.

**Step 2: identify six-point classes.** If \(|S|=6\), the same incidence equations are
\[
a_1+a_2+a_3=13,\quad a_1+2a_2+3a_3=24,\quad a_2+3a_3=15,
\]
which force \((a_1,a_2,a_3)=(6,3,4)\). Two of the four trisecants cannot be disjoint inside \(S\): otherwise their six points exhaust \(S\), and any third line meets each of these two lines in at most one point and thus contains at most two points of \(S\). Three trisecants cannot concur, since their union would contain at least seven points of \(S\). Hence the four trisecants form a frame, and their six intersections exhaust \(S\).

Conversely, let four lines form a frame, and put their six intersection points in \(S\). Each frame line contains exactly three points of \(S\). Any other line contains at most two points of \(S\): three such points would provide six incidences with the four frame lines, forcing two points on a common frame line and making the new line equal to that frame line. The four frame lines account for twelve of the fifteen pairs of points of \(S\); the remaining three pairs, corresponding to disjoint pairs of frame lines, lie on three distinct nonframe lines. These three lines are bisecants. After these four trisecants and three bisecants, the remaining six lines must each contain one point of \(S\), by the total incidence count \(6\cdot4=24\). Thus every line contains between one and three points of \(S\), so \(S\) defines an admissible coloring.

The projective linear group \(\operatorname{PGL}(3,3)\) has order \(5616\) and acts sharply transitively on ordered frames of four lines. Equivalently, their number is \(13\cdot12\cdot9\cdot4=5616\). Each unordered frame is counted \(4!=24\) times; every six-set uniquely recovers its four trisecants. Therefore \(|\mathcal Q|=5616/24=234\). Complementing the red class gives another \(234\) colorings, totaling \(468\).

**Step 3: all legal recolorings.** A six-red-point coloring cannot recolor a red point blue, by Step 1. Of the seven blue points, four are the unique missing points on the four frame lines. Recoloring any of those would make its frame line monochromatic. Recoloring any of the other three is legal: no line then becomes all red, and removing a blue point cannot create an all-blue line. Every six-red-point coloring therefore has exactly three neighbors, each with seven red points. Complementation gives the same degree for seven-red-point colorings. Hence \(\mathcal R\) is cubic and bipartite, with \(468\cdot3/2=702\) edges.

For \(Q,Q'\in\mathcal Q\), disjointness means that exactly one point lies outside \(Q\cup Q'\). Moving that point from blue to red changes the configuration with red set \(Q\) into the configuration with blue set \(Q'\). This is reversible and identifies \(\mathcal R\) exactly with the canonical bipartite double of the disjointness graph \(H\) on \(\mathcal Q\).

**Step 4: identify the known symmetric graphs.** Since the projective group is transitive on frames, it is transitive on \(V(H)\). The stabilizer of one unordered frame has order \(24\), induces the full permutation action on its four frame lines, and is transitive on its three legal neighbors. (The last finite statement is checked explicitly, without a graph-isomorphism package, in `verify_quadrilateral_frames.py`: all invertible \(3\)-by-\(3\) matrices over \(\mathbb F_3\) modulo scalar are examined.) Consequently \(H\) is an arc-transitive cubic graph on \(234\) vertices.

An exhaustive breadth-first and cycle check in the two independent included incidence models establishes that \(H\) is connected, nonbipartite, and has girth \(12\) and diameter \(8\). The complete census of symmetric cubic graphs through order \(768\), tabulated by Conder and Nedela, lists exactly two at order \(234\): F234A (bipartite, girth \(6\)) and F234B (nonbipartite, girth \(12\), diameter \(8\)). Therefore \(H\cong\mathrm{F234B}\), Wong's graph. The same source identifies its connected bipartite double cover with F468. This proves \(\mathcal R\cong\mathrm{F468}\).

The included exhaustive graph traversal verifies that all \(468\) roots of \(\mathcal R\) have the stated thirteen-step distance profile and diameter \(13\), and checks girth \(12\). All finite enumerations have precisely specified domains and reproducible implementations.

## Verification

Run `python3 verify_coloring_flip.py` and `python3 verify_quadrilateral_frames.py` using only Python's standard library. The first constructs the plane from normalized vectors in \(\mathbb F_3^3\), checks all \(8192\) named two-colorings, and reconstructs the complete flip graph and the complete quadrilateral-disjointness graph; breadth-first searches from every vertex check their distances and girths. The second independently constructs the plane by its nine affine points and four points at infinity, enumerates all \(715\) four-line choices, establishes the \(234\) complete quadrilaterals and their line-intersection spectra, and checks legal moves, connectivity, the odd-cycle obstruction, and projective frame-stabilizer neighbor transitivity by full matrix enumeration. Both scripts terminate with explicit success markers. No unspecified dataset, external service, randomized seed, or prior result file is required.

## Relationship to prior work

Conder and Nedela, *A more detailed classification of symmetric cubic graphs* (freely accessible author's preprint; journal version *A refined classification of symmetric cubic graphs*, 2009), already identify F234B as Wong's graph and F468 as its bipartite double cover, and tabulate the two symmetric cubic graphs of order \(234\), with their girths and diameters. This theorem does **not** claim the abstract graph classification, symmetries or their metric invariants as novel. What is offered is the explicit equivalence of those graphs with the feasible one-point recoloring dynamics of line-bichromatic colorings of \(\operatorname{PG}(2,3)\), including the geometric characterization by all \(234\) projective complete quadrilaterals.

Relevant background on classical projective quadrilaterals includes Brown (1960). The graph-census paper has been examined in the sections concerning Wong's graph, F468, and the complete tables, not merely by title. An exact result about this coloring interpretation was not located in the targeted literature searches or accessible research-record comparisons, but absence from search results does not prove historical novelty.

## Limitations

This is a theorem about a single natural finite incidence geometry. No generalization to all projective planes or other prescribed line sizes is claimed. The graph-isomorphism identification uses the published complete symmetric-cubic census; its independent metric checks are finite exact enumerations. An earlier equivalent description of F234B by disjoint complete quadrilaterals, or a direct interpretation as a point-coloring graph, may exist under historical terminology; inaccessible or unindexed sources remain an originality risk. No independent scholarly audit has been undertaken.

## References

1. M. D. E. Conder and R. Nedela, *A more detailed classification of symmetric cubic graphs*, author's full-text preprint, https://www.math.auckland.ac.nz/~conder/preprints/symmcubictypes.pdf . Journal version: *A refined classification of symmetric cubic graphs*, Journal of Algebra **322** (2009), 722–740, https://doi.org/10.1016/j.jalgebra.2009.03.011 .
2. M. Conder and P. Dobcsányi, *Trivalent symmetric graphs up to 768 vertices*, Journal of Combinatorial Mathematics and Combinatorial Computing **40** (2002), 41–63; census used as historical underlying classification.
3. W. J. Wong, *Determination of a class of primitive permutation groups*, Mathematische Zeitschrift **99** (1967), 235–246, https://doi.org/10.1007/BF01112454 ; original group-theoretic context for the named graph.
4. W. G. Brown, *Hesse's theorem for a quadrilateral whose sides touch a conic*, Canadian Mathematical Bulletin **3** (1960), 221–223, https://doi.org/10.4153/CMB-1960-027-0 ; classical projective quadrilateral geometry.
