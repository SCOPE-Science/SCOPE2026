# The Pappus perfect-matching hexagon-flip graph is two alternating hexagon triangles

## Finding

Let \(P\) be the eighteen-vertex Pappus graph, represented as the incidence graph of the Pappus \((9_3)\) configuration. Define \(\mathcal F_6(P)\) to have every perfect matching of \(P\) as a vertex; two matchings are adjacent exactly when their symmetric difference is the edge set of **any simple six-cycle of the abstract graph**. No embedding or facial restriction is imposed.

Define \(T\) as follows. Take three nonadjacent hub vertices \(h_0,h_1,h_2\). For each unordered pair \(\{i,j\}\subseteq\{0,1,2\}\), with \(i<j\), add a disjoint cycle of length six, whose consecutive vertices are \(w_{ij,0},\ldots,w_{ij,5}\). Join \(h_i\) to the three even-indexed vertices and \(h_j\) to the three odd-indexed vertices of this cycle. Make no other edges.

**Theorem.** There is an exact graph isomorphism
\[
\mathcal F_6(P)\cong T\sqcup T.
\]
The two components are exactly the even and odd permutation-sign classes of the perfect matchings, relative to the indicated ordering of the nine points and nine lines. Thus \(P\) has \(42\) perfect matchings, \(21\) in each component, and \(\mathcal F_6(P)\) has \(72\) edges. Each component has three vertices of degree six, eighteen of degree three, radius four, and diameter four. Each component is therefore connected even though the whole flip graph is not.

## Assumptions and scope

Use nine points \(A,B,C,a,b,c,X,Y,Z\), numbered \(0,\ldots,8\), and the following nine lines in the displayed order:
\[
ABC,\quad abc,\quad AbX,\quad aBX,\quad AcY,\quad aCY,\quad BcZ,\quad bCZ,\quad XYZ.
\]
The incidence graph has one vertex per point and one per line; an edge means incidence. It is the standard Pappus Levi graph. A perfect matching is a bijection \(p:\{0,\ldots,8\}\to\{0,\ldots,8\}\) such that point \(i\) belongs to line \(p(i)\) for every \(i\). Its sign is \((-1)^{\operatorname{inv}(p)}\) where \(\operatorname{inv}(p)=|\{(i,j):i<j,\ p(i)>p(j)\}|\).

The theorem concerns **all** simple six-cycles of the abstract Pappus graph, not merely the nine faces of one toroidal embedding. It does not classify flip graphs for other configurations or for larger cycles.

## Proof

**1. Legal moves and parity.** For two distinct perfect matchings, the symmetric difference is a disjoint union of alternating even cycles. Its being precisely one six-cycle is equivalent to the two bijections differing on exactly three points. The three assigned lines must then undergo one of the two cyclic permutations. Conversely, rotating the assigned lines at any three distinct points gives an adjacent matching if and only if each new assignment remains an incidence edge. Such a move composes the matching permutation with a three-cycle, so its sign is unchanged. This is also consistent with the general sign lemma for one-factors in [1].

**2. Exhaustive finite classification.** From the listed line triples, construct the three-element incidence list for each of the nine points. The search `verify_incidence.py` tries every permitted unused line in increasing point order; consequently every perfect matching appears once and only once. It obtains exactly \(42\) matchings, \(21\) of each sign. For each matching it examines every unordered triple of points and both cyclic rotations of the three matched lines. The incidence predicate in Step 1 is necessary and sufficient, so this produces **every** flip edge and no extraneous edge. There are exactly \(72\) such edges. Graph traversal produces exactly two components, each of size \(21\), and each component lies in one sign class; equality of component and sign class follows because both sign classes have size \(21\).

**3. Graph isomorphism, not just counts.** In either computed component, precisely three vertices have degree six, and the other eighteen have degree three. None of the degree-six vertices are adjacent. Every degree-three vertex has exactly one degree-six neighbor. Deleting the three degree-six vertices leaves exactly three disjoint six-cycles. Along each remaining cycle, the adjacent hubs alternate between a fixed pair, and all three possible hub pairs occur exactly once. These *exhaustively checked adjacency properties* are precisely the edge specification of \(T\). Ordering the hubs arbitrarily and labeling the six vertices around each peripheral cycle gives the claimed isomorphism for both components.

**4. Distances.** The exact breadth-first search from each of the \(21\) vertices in each component reaches all \(21\) vertices and has maximum distance four. Thus each vertex has eccentricity four; both the radius and diameter equal four. Each \(T\) has eighteen peripheral hexagon edges and eighteen spokes, hence \(36\) edges; the two components together have \(72\) edges.

**5. Independent graph encoding.** The separate script `verify_lcf.py` starts instead from the standard LCF presentation \([5,7,-7,7,-7,-5]^3\) of the Pappus graph, constructs the full eighteen-vertex graph and enumerates arbitrary graph-theoretic perfect matchings by uncovered-vertex branching. It separately lists all eighteen simple six-cycles and generates moves via symmetric difference of edge bitmasks. It independently reproduces \(42\) states, \(72\) moves, two components of size \(21\), the degree multiplicities, and both diameters. The standard equivalence of the LCF and incidence representations is recorded in [4].

The finite enumeration is a complete proof because all relevant objects have been enumerated by bijective, terminating branches over nine points or eighteen vertices; no sampling, asymptotic inference, or unbounded search is involved.

## Verification

With Python 3, without nonstandard packages, execute `python3 verify_incidence.py` and `python3 verify_lcf.py` beside this document. Compare their complete printed JSON values with `incidence_output.json` and `lcf_output.json`. Both programs contain assertions for the completeness-sensitive claims. The incidence script tests the three-hub/six-cycle construction; the LCF script independently tests the graph-theoretic switch relation. The reported properties were replayed from the actual embedded program paths.

## Relationship to prior work

Abreu, Diwan, Jackson, Labbate and Sheehan [1, Lemma 2.1 and Proposition 3.3] established the sign relation for one-factors and that the Pappus graph has two types of complementary \(2\)-factors: a Hamilton cycle and three disjoint six-cycles. We claim neither result as new. Abreu, Labbate and Sheehan [2] further treated the Pappus graph among irreducible pseudo-\(2\)-factor-isomorphic Levi graphs; Goedgebeur [3] revisited the family during an exhaustive counterexample search. These sources do not state the abstract six-cycle-flip graph's component isomorphism.

There is related resonance-graph literature on graphs embedded in surfaces and toroidal polyhexes, especially [5] and [6], where a flip is restricted to a **chosen embedded hexagonal face**. That model is not the present graph's unrestricted switch across all simple six-cycles: the Pappus graph has eighteen simple six-cycles, whereas a standard toroidal hexagonal embedding uses nine faces. Results about matching connectivity for a fixed face system do not imply the isomorphism above. The ordinary matching and perfect-matching complexes also encode simplices rather than the adjacency defined here. Search and implication comparisons are documented in `AUDIT.json`.

## Limitations

The isomorphism and all numerical assertions are exact for the fixed abstract Pappus graph, with no claim about larger cubic graphs or arbitrary toroidal polyhexes. A complete mathematical literature priority review is inherently limited by indexing and vocabulary: an unlocated equivalent under a different switch terminology could exist. All cycles are taken in the abstract graph, and changing to a fixed toroidal embedding changes the move set. The checks are reproducible computations plus finite combinatorial justification, not independent external certification.

## References

[1] M. Abreu, A. A. Diwan, B. Jackson, D. Labbate and J. Sheehan, *Pseudo 2-Factor Isomorphic Regular Bipartite Graphs*, J. Combin. Theory Ser. B 98 (2008), 432–442, doi:10.1016/j.jctb.2007.08.006; author manuscript https://maths.qmul.ac.uk/~bill/pseuRESUBMIT.pdf.

[2] M. Abreu, D. Labbate and J. Sheehan, *Irreducible pseudo 2-factor isomorphic cubic bipartite graphs*, arXiv:1002.1891v1 (public 2010-02-09), https://arxiv.org/pdf/1002.1891.

[3] J. Goedgebeur, *A counterexample to the pseudo 2-factor isomorphic graph conjecture*, arXiv:1412.3350v1 (public 2014-12-10), https://arxiv.org/html/1412.3350v2.

[4] E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html (LCF presentation and abstract incidence identity).

[5] L. Liang and H. Zhang, *The resonance graphs of nanotubes and toroidal polyhexes*, arXiv:2609.19766v1 (public 2026-09-17), https://arxiv.org/html/2609.19766 (Definitions 2.1 and Theorems 2.18, 5.3).

[6] N. Tratnik and D. Ye, *Resonance Graphs and Perfect Matchings of Graphs on Surfaces*, arXiv:1710.00761v1 (public 2017-10-02), https://arxiv.org/pdf/1710.00761 (Definitions of \(R(G;\mathcal F)\) for designated even embedded faces).
