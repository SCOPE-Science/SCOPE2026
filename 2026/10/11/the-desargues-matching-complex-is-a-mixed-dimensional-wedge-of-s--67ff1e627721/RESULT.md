# The Desargues matching complex is a mixed-dimensional wedge of spheres

## Finding

Let \(D\) be the twenty-vertex Desargues graph, equivalently the generalized Petersen graph \(GP(10,3)\) or the bipartite Kneser graph \(H(5,2)\). Let \(\operatorname{Match}(D)\) be its ordinary matching complex: the simplicial complex whose vertices are the thirty edges of \(D\) and whose faces are sets of pairwise vertex-disjoint edges. Then
\[
\boxed{\operatorname{Match}(D)\simeq \bigvee^{5}S^{5}\ \vee\ \bigvee^{45}S^{6}.}
\]
In particular, the only nonzero reduced integral homology groups are \(\widetilde H_5\cong\mathbb Z^5\) and \(\widetilde H_6\cong\mathbb Z^{45}\). The conclusion is a homotopy equivalence, not merely a computation of homology over a field.

## Assumptions and scope

Write \(U\) for the lexicographically ordered two-element subsets and \(V\) for the lexicographically ordered three-element subsets of \(\{0,1,2,3,4\}\). The twenty vertices are the elements of \(U\sqcup V\). An edge joins \(u\in U\) to \(v\in V\) exactly when \(u\subset v\); index these thirty edges lexicographically, first by index in \(U\), then by index in \(V\), starting with zero. This defines \(H(5,2)\) without reference to a drawing. The bundled verification program additionally checks an explicit bijection to the generalized Petersen graph \(GP(10,3)\).

All homotopy types are those of geometric realizations of finite simplicial complexes. The assertion concerns ordinary matchings in this one graph, not the discrete Morse complex, the complex of perfect matchings alone, nor a uniform statement about generalized Petersen graphs.

## Proof

**Finite face set.** An edge-matching is a bitmask on the thirty indexed graph edges. Recursion over edge inclusion, allowing an edge only when both endpoints are unused, enumerates precisely \(113{,}192\) faces including the empty face. The numbers of faces of cardinalities zero through ten are
\[
(1,30,375,2540,10155,24486,34945,27840,11040,1720,60).
\]
This is exhaustive because every decision either excludes the next indexed edge or includes it if compatible with previously included edges.

**Acyclic matching.** Process potential simplicial vertices in the following zero-based index order, displayed as literal input data:

`24,11,9,0,5,6,7,16,14,26,18,27,20,19,28,17,23,21,29,2,25,1,22,4,3,8,15,12,13,10`.

At each stage, among currently unpaired faces, pair each face not containing that vertex with its one-vertex extension whenever both remain available. Temporarily include the empty face for this deterministic procedure, and then discard the unique pair involving the empty face; its singleton upper partner becomes a critical zero-cell. On the ordinary nonempty face poset there are exactly \(56{,}567\) matched covers and exactly one critical zero-cell, eight critical five-cells, and forty-eight critical six-cells, with no others. Orient each matched Hasse cover upward and all other covers downward. A complete topological sort of the resulting digraph visits all \(113{,}191\) nonempty faces across \(680{,}370\) incidences. Thus the matching is acyclic, and Forman's theorem provides a CW complex with precisely these critical cells.

**Integral attaching degrees.** Order each oriented simplex by increasing indexed graph edge. The signed simplicial boundary deletes its successive vertices with signs \(+1,-1,+1,\ldots\). For a matched lower face \(\lambda\) with upper mate \(\mu\), eliminate \(\lambda\) from the cellular chain complex by cancelling the unit incidence of \(\mu\): in the resulting chain quotient, the boundary relation from \(\mu\) expresses \(\lambda\) as a signed combination of its other codimension-one faces. Recursion down the acyclic gradient relation expresses the boundary of each critical six-cell in the eight critical five-cells. This computes the integral cellular Morse boundary \(B:\mathbb Z^{48}\to\mathbb Z^8\).

Label its rows \(e_0,\ldots,e_7\) by the eight critical five-cell bitmasks in increasing order and its columns from zero to forty-seven by increasing six-cell bitmask. Exact computation gives only twenty-five nonzero matrix entries. Every column is an integer combination of the three independent vectors
\[
a=e_0-e_1,\qquad b=e_3,\qquad c=e_6-e_7.
\]
Moreover columns with indices two, nine and thirty-six are respectively exactly \(a\), \(b\) and \(c\). Consequently \(\operatorname{im}B=\mathbb Za\oplus\mathbb Zb\oplus\mathbb Zc\), a primitive rank-three direct summand of \(\mathbb Z^8\). Thus the integral Smith invariant factors of \(B\) are \((1,1,1)\), with all remaining diagonal entries zero.

**From degrees to homotopy.** The five-skeleton of the Morse CW complex is \(\bigvee^8 S^5\). Because \(\pi_5(\bigvee^8S^5)\cong\mathbb Z^8\), each six-cell attaching map is completely specified, up to homotopy, by its integer degree column. Integral changes of basis in these domain and target free groups are realized by homotopy equivalences of wedges of five-spheres. Smith reduction therefore turns the attaching maps into three degree-one maps to distinct five-sphere summands and forty-five null maps. The three degree-one maps yield contractible five-/six-cell pairs; the other maps attach six-spheres trivially. The remaining CW complex is precisely \(\bigvee^5S^5\vee\bigvee^{45}S^6\), proving the assertion.

## Verification

Run `python3 verify_desargues_homotopy.py` in the directory containing this file. The program uses only Python's standard library, reconstructs both graph encodings and their isomorphism, enumerates every matching, generates the acyclic face-poset pairing, checks all \(680{,}370\) oriented Hasse incidences, recursively computes every signed integral Morse boundary column, and verifies the three primitive degree directions and the three explicit unit columns. Success prints `DESARGUES_HOMOTOPY_VERIFY_OK`. No probabilistic tests or floating-point rank approximations are used. The face vector also gives reduced Euler characteristic \(40=-5+45\).

## Relationship to prior work

A previously published calculation for the very same graph established only the mod-two reduced homology ranks five in degree five and forty-five in degree six; its proof explicitly left integral torsion, attaching maps and homotopy type undecided. Those ranks are consistent with this result, but do not imply the integral sphere-wedge classification. The present construction supplies the missing integral attaching matrix and homotopy argument.

Donovan and Scoville's matching-complex theorems treat paths, cycles and Dutch windmill graphs, not the Desargues graph. A published exact wedge result for the ordinary matching complex of the Möbius–Kantor graph \(GP(8,3)\) concerns a different graph and contains no uniform formula covering \(GP(10,3)\). Kozlov's discrete Morse and simple-homotopy methods provide background rather than this parameter-specific calculation. The graph is the middle-level graph \(H(5,2)\), so chessboard-complex terminology and line-graph independence-complex terminology were also considered in the comparison.

## Limitations

This is an exact finite classification for one graph. It does not classify the matching complexes of all cubic bipartite graphs or all generalized Petersen graphs, and it does not establish an equivariant homotopy splitting under the Desargues graph's automorphism group. Originality is assessed against inspected public literature and research records; unindexed or unpublished equivalent calculations cannot be categorically excluded. The verified proof requires the complete finite reconstruction of the stated Morse matching and its signed boundary; Betti numbers alone would not prove the homotopy claim.

## References

1. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613v1 (first public 2005-03-28), primary MSC 57Q10.
2. D. N. Kozlov, *Discrete Morse Theory for free chain complexes*, arXiv:cs/0504090v1 (first public 2005-04-21).
3. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1 (first public 2022-07-27), especially the matching-complex section and the discrete-Morse theorem.
4. *Mod-2 homology of the Desargues matching complex*, published published-finding corpus result `2026/10/4/SCOPE-mod-2-homology-of-the-desargues-matching-complex--91609797437d`, checked for exact scope.
5. *The Möbius–Kantor matching complex is a mixed-dimensional sphere wedge*, published published-finding corpus result `2026/10/4/SCOPE-the-m-bius-kantor-matching-complex-is-a-mixed-dimensional-sphere--4bfded76792e`, checked as a neighboring-graph comparison.
