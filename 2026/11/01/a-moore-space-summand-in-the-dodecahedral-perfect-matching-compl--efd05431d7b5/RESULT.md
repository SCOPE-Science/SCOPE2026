# A Moore-space summand in the dodecahedral perfect-matching complex

## Finding
Let \(D=\operatorname{GP}(10,2)\) be the dodecahedral graph and \(\mathcal P(D)\) its perfect-matching complex, whose facets are the edge sets of perfect matchings. With \(M(\mathbb Z/2,2)=S^2\cup_{2}e^3\) denoting the three-dimensional Moore space obtained by attaching a three-cell by a degree-two map, there is an integral homotopy equivalence
\[
\boxed{\mathcal P(D)\simeq M(\mathbb Z/2,2)\vee\bigvee^{20}S^3.}
\]
In particular,
\[
\widetilde H_j(\mathcal P(D);\mathbb Z)\cong
\begin{cases}\mathbb Z/2\mathbb Z,&j=2,\\\mathbb Z^{20},&j=3,\\0,&\text{otherwise}.\end{cases}
\]
This complex is not homotopy equivalent to a wedge of spheres, because its integral homology has nonzero torsion.

## Assumptions and scope
All graphs are finite, undirected, simple. Write vertices as \(u_i=i\) and \(v_i=10+i\) for \(0\le i<10\), indices reduced modulo ten. The graph has the thirty edges \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+2}\}\), one edge of each type for every \(i\). These are the edges of the standard dodecahedral graph \(\operatorname{GP}(10,2)\). The simplicial complex \(\mathcal P(D)\) has graph edges as vertices and a subset \(F\) as a face exactly when a perfect matching \(Q\) exists with \(F\subseteq Q\). The only homotopy classification asserted is for this particular graph.

## Proof
**Exact finite input.** Index graph edges by lexicographically sorted endpoint pairs, from zero through twenty-nine. Exhaustive recursion on the least unmatched graph vertex enumerates exactly thirty-six perfect matchings. Their downward closure comprises 30,504 faces including the empty face, with face vector in dimensions zero through nine
\[
(30,375,2180,5790,8352,7440,4320,1620,360,36).
\]
Independently, an edge-order recursion enumerates all 111,376 ordinary graph matchings and checks inclusion in one of the perfect matchings; precisely 30,504, including the empty matching, extend. The complete enumeration algorithms and the deterministically sorted edge list are contained in `verify_dodeca_pmc.py`.

**Acyclic reduction.** On the poset of *nonempty* faces, for each edge-coordinate in increasing order, pair every still-unpaired face not containing that coordinate with the face obtained by adding it, when both remain; then remove those two faces from later stages. The resulting 15,231 disjoint covering pairs are acyclic: orient each ordinary covering relation downward and each matched relation upward; topological sorting visits all 30,503 nonempty faces through 163,650 oriented Hasse incidences. Exactly one critical zero-cell, ten critical two-cells, and thirty critical three-cells remain. Forman's theorem supplies a homotopy-equivalent CW complex with only these cells.

**Exact integral boundary certificate.** Order critical cells by the integers encoding their edge-subset masks. The cellular differential from the thirty critical three-cells to the ten critical two-cells is the integral matrix \(B\) with ten rows and thirty columns. It is reconstructed by the signed gradient-path recursion in `verify_dodeca_pmc.py`, and its 300 exact entries, row and column labels, and edge order are displayed in `boundary_certificate.json`. There are 34 entries equal to \(-1\), 231 equal to zero, and 35 equal to \(+1\). Gaussian elimination over \(\mathbb F_2\) gives rank nine. The submatrix in all ten rows and columns indexed
\[
(0,2,4,5,6,7,8,10,11,26)
\]
has **integer determinant two**, checked by fraction-free Bareiss elimination. Consequently \(B\) has rank ten over \(\mathbb Q\). Its ten nonzero Smith invariant factors have product dividing two, because that product is the greatest common divisor of its maximal minors. Exactly nine invariant factors are odd, because the reduction modulo two has rank nine. Thus the invariant factors, in divisibility order, are exactly
\[
(1,1,1,1,1,1,1,1,1,2).
\]
No other cellular differentials are possible in the reduced CW model. Thus the second reduced integral homology is \(\operatorname{coker}(B)\cong\mathbb Z/2\mathbb Z\), and the third is \(\ker(B)\cong\mathbb Z^{20}\).

**Passage from homology to homotopy.** The reduced CW model has one vertex and no one-cells. Its two-skeleton is therefore \(\bigvee^{10}S^2\), and its thirty three-cell attaching maps lie in
\[
\pi_2\!\left(\bigvee^{10}S^2\right)\cong\mathbb Z^{10}.
\]
The matrix \(B\) records precisely those attaching classes, not merely their homological shadows: this follows from the Hurewicz isomorphism in degree two. Integer changes of basis on the two-spheres are realized by homotopy self-equivalences of the wedge, and elementary changes among three-cell attaching maps are realized by cellular handle slides. The Smith diagonal form therefore splits off nine contractible two/three-cell pairs, one degree-two three-cell attached to a two-sphere, and twenty trivially attached three-cells. This gives the displayed Moore-space-and-spheres homotopy equivalence.

## Verification
Run `python3 verify_dodeca_pmc.py` using the Python 3 standard library. It checks all face enumerations, matching pairs and Hasse incidences, computes the exact integral Morse boundary by signed face incidence, verifies the rank and minor witnesses, and independently computes full simplicial mod-two boundary ranks in degrees one through nine. The latter produce mod-two Betti numbers one in degree two and twenty-one in degree three, with all other positive-degree Betti numbers zero, as predicted by universal coefficients for the integral groups above. Compare stdout with `verification_output.txt`, and compare the documented matrix and critical masks with `boundary_certificate.json`.

## Relationship to prior work
Bayer–Jelić Milutinović–Vega introduced this exact definition of perfect-matching complexes and classified selected honeycomb families [1]. Chandrakar–Singh classified polygonal-line tilings and narrow grid families [2]. The dodecahedral graph is neither a honeycomb graph of those specified families nor a polygonal-line tiling. Its 36 perfect matchings are independently known [3]; that counting result does not determine this complex's topology. A published exact homotopy classification of the **ordinary** dodecahedral matching complex concerns all graph matchings rather than just those extendible to perfect matchings [4], so it does not imply this result. The nontrivial order-two class distinguishes the result from the torsion-free wedge types in [1] and [2].

## Limitations
The proof is exact but depends on a finite, reproducible integral discrete-Morse certificate; it is not a purely conceptual argument for why two-torsion occurs. No claim of a first-ever torsion example is made, no general theorem for cubic graphs or Platonic graphs is asserted, and no equivariant homotopy statement is established. An equivalent result outside the inspected literature or an unindexed source cannot be ruled out solely by searches. No independent external audit or mathematical peer review has been performed.

## References
[1] M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803 (first posted 2022-09-06); Electronic Journal of Combinatorics 30 (2023), #P2.45. https://arxiv.org/abs/2209.02803

[2] H. Chandrakar, A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809 (first posted 2024-07-08); Annals of Combinatorics (2025). https://arxiv.org/abs/2407.05809

[3] *Number of perfect matchings of the dodecahedron*, MathOverflow mathematical discussion (2015), establishing 36 matchings. https://mathoverflow.net/questions/192159/number-of-perfect-matchings-of-the-dodecahedron

[4] *The dodecahedral matching complex is a wedge of five 5-spheres and 117 6-spheres*, published research record (2026-10-11), concerning the ordinary matching complex rather than the perfect-matching subcomplex.
