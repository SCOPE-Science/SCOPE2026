# Integral homotopy of the ordinary Morse complex of the three-cube
## Finding
Let \(Q_3\) be the graph on \(\{0,1\}^3\) with an edge joining strings differing in exactly one coordinate. Let \(\mathcal M(Q_3)\) be the ordinary simplicial complex of acyclic graph vertex–edge incidence matchings. Then
\[
\boxed{\mathcal M(Q_3)\simeq\bigvee^{4}S^5\vee\bigvee^{139}S^6.}
\]
In particular,
\[
\widetilde H_k(\mathcal M(Q_3);\mathbb Z)\cong
\begin{cases}
\mathbb Z^4,&k=5,\\
\mathbb Z^{139},&k=6,\\
0,&\text{otherwise}.
\end{cases}
\]
This strengthens the previously established mod-\(2\) homology calculation for this same complex to a complete integral homotopy classification.

## Assumptions and scope
The cube has vertex set \(\{0,1,\ldots,7\}\), where the integers encode three-bit strings, and its twelve unoriented edges are the pairs \(\{u,v\}\) with \(u<v\) and Hamming distance one. A primitive Morse-complex vertex is the pairing of a graph vertex \(u\) with an incident edge \(\{u,v\}\). Encode it as the directed arrow \(u\to v\). Thus there are 24 primitive vertices, ordered by lexicographically increasing unoriented edge, with both arrow directions consecutive.

A set of primitive vertices is a face exactly when each graph vertex is used as a tail at most once, each graph edge is used at most once, and the selected arrows contain no directed cycle. This is precisely a compatible acyclic discrete vector field on the one-dimensional simplicial complex \(Q_3\). Orient simplices by increasing primitive indices. All homotopy equivalences are of ordinary geometric realizations. The claim is for this particular graph and the **ordinary** Morse complex, not the pure Morse complex of maximal fields.

## Proof
**Exhaustive finite model.** For each of the eight graph vertices, choose either no outgoing arrow or one of its three outgoing arrows. Discard a selection if two choices use opposite directions of the same graph edge or if the selected directed graph contains a directed cycle. This visits every possible face exactly once. The resulting 23,625 faces including the empty face have nonempty face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)
=(24,240,1296,4080,7488,7424,3072).
\]
The independent graph-Laplacian rooted-forest enumeration gives \(\det(L+tI)=t(t+2)^3(t+4)^3(t+6)\), reproducing these coefficients.

**Acyclic matching.** Process the 24 primitive vertices in increasing order. At each stage, among faces not yet paired, pair each face not containing the current primitive vertex with the face obtained by inserting it, provided both are unpaired faces. This is a deterministic collection of 11,701 reduced face pairs, including the empty-face/singleton pair. Remove that one pair to obtain an ordinary discrete-Morse matching on nonempty faces, with the singleton left critical. All other pairs remain unchanged. A topological sort of the augmented Hasse diagram, with matched incidences directed upward and unmatched incidences downward, visits all 23,625 faces and checks all 124,200 codimension-one incidences. Consequently the ordinary matching is acyclic too. Its critical simplices are exactly one vertex, 44 five-simplices and 179 six-simplices, with none in other dimensions.

By the cellular discrete-Morse theorem the complex has a CW model with one zero-cell, 44 five-cells and 179 six-cells. Its five-skeleton is \(\bigvee^{44}S^5\). All six-cell attaching maps lie in
\[
\pi_5\!\left(\bigvee^{44}S^5\right)
\cong H_5\!\left(\bigvee^{44}S^5;\mathbb Z\right)
\cong\mathbb Z^{44},
\]
where the first isomorphism is Hurewicz. Thus the integer attaching-degree matrix determines these maps up to homotopy; there are no additional attaching invariants at this dimension.

**Integral attaching degrees.** For a matched lower five-face \(s\) with paired six-face \(t\), replace \(s\) by the signed sum of all other five-facets of \(t\), with coefficient \(-[t:s]^{-1}\); a five-face matched above a four-face projects to zero, while critical five-faces project to the corresponding standard basis vector. Recursing through the acyclic gradient paths gives a \(44\)-by-\(179\) signed integer matrix of attaching degrees, with 195 nonzero entries. Exact integer row/column unit pivots (permutations, sign changes, and integral multiples) reduce it to a diagonal containing forty ones and an otherwise zero rectangle. A separate exact Smith-normal-form computation yields the same forty unit invariants. Therefore the image is a primitive direct summand of rank forty, without torsion.

Unimodular changes of basis on the 44 five-spheres are induced by self-homotopy equivalences of their wedge. Elementary operations on the 179 six-cell attaching maps are realized by cellular slides. The forty degree-one attachments cancel forty five-spheres against forty six-cells. The remaining cells attach nullhomotopically, giving four five-spheres and 139 six-spheres, as asserted.

## Verification
The standalone file `verify_homotopy.py` uses only Python's standard library. Run `python3 verify_homotopy.py` from its directory. It regenerates all faces, checks the complete codimension-one Hasse diagram and acyclicity, recomputes signed gradient-path integer degrees, reduces the degree matrix by actual unimodular operations, and independently obtains the full mod-\(2\) simplicial boundary ranks
\[
(1,23,217,1079,3001,4487,2933)
\]
in dimensions zero through six (with the augmented dimension-zero boundary). The replay checks the face counts, forty unit pivots, and mod-\(2\) Betti ranks four and 139. A separate independent Smith-normal-form computation on the generated matrix confirmed the forty unit invariant factors.

## Relationship to prior work
Chari and Joswig introduced discrete Morse complexes and identify graph discrete vector fields with oriented rooted forests. Kozlov's integral algebraic discrete-Morse reduction gives a standard derivation of the signed critical-cell differential used here. Donovan, Lin, and Scoville determine the homotopy types for other graph families, including trees with suitable leaves and caterpillars; these do not encompass the cubic cube graph. Scoville and Zaremsky give general connectivity bounds for the Morse complex, not the present complete homotopy classification.

The closest indexed **exact same-object calculation** is the published record *Mod-\(2\) homology of the cube-graph Morse complex is concentrated in degrees \(5\) and \(6\)* (published-finding corpus, 2026), which determined the above face counts and mod-\(2\) Betti ranks. That record explicitly leaves integral torsion and homotopy type undetermined; equality of mod-\(2\) Betti numbers does not imply integral torsion-freeness, much less a wedge decomposition. The present claim supplies integral attaching-map data and the full homotopy equivalence. Courtney's thesis on directed forest complexes of Cayley graphs is a plausible equivalent-framework source, but its full text could not be inspected; this remains an explicit bibliographic risk.

## Limitations
The computation proves the classification only for \(Q_3\), not arbitrary hypercubes \(Q_d\). It supplies a reproducible finite proof and a same-model review, not independent external certification. The directed-forest thesis and unindexed literature could conceivably contain an equivalent result. No general formula for higher-dimensional cubes or canonical, symmetry-equivariant wedge splitting is asserted.

## References
1. M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234v1 (first public 2000-11-28), https://arxiv.org/abs/math/0011234.
2. D. N. Kozlov, *Discrete Morse Theory for free chain complexes*, arXiv:cs/0504090v1 (first public 2005-04-21), https://arxiv.org/abs/cs/0504090.
3. C. Donovan, M. Lin, and N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440v1 (2019), https://arxiv.org/abs/1909.11440.
4. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481v1 (2020), https://arxiv.org/abs/2004.10481.
5. K. Courtney, *The Directed Forest Complex of Cayley Graphs*, master's thesis, Boise State University, 2020, https://doi.org/10.18122/td/1684/boisestate.
6. *Mod-\(2\) homology of the cube-graph Morse complex is concentrated in degrees \(5\) and \(6\)*, public published-finding corpus mathematics record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-cube-graph-morse-complex-is-concentrated-i--3861de13b7e0.
