# Homotopy and affine symmetry of the Hesse noncover complex

## Finding
Let \(P=\mathbf F_3^2\) be the nine-point ternary affine plane, let \(\mathcal L\) be its twelve affine lines, and let
\[
K=\operatorname{NC}(P,\mathcal L)=\{\sigma\subseteq P:\text{there is a line }L\in\mathcal L\text{ with }\sigma\cap L=\varnothing\}.
\]
Then the integral homotopy type is
\[
K\simeq\bigvee^{11}S^3\vee S^4.
\]
Put \(G=\operatorname{AGL}_2(\mathbf F_3)=\mathbf F_3^2\rtimes\operatorname{GL}_2(\mathbf F_3)\), of order \(432\). Let \(\mathcal D\) be the four directions (parallel classes) of the affine plane; for a finite \(G\)-set \(T\), write \(\operatorname{Aug}(\mathbf Q[T])\) for the augmentation submodule of its permutation representation. If \(\delta(A,t)\) is \(+1\) for \(\det A=1\) and \(-1\) for \(\det A=2\), then
\[
\widetilde H_3(K;\mathbf Q)\cong_G\delta\otimes\bigl(\operatorname{Aug}(\mathbf Q[P])\oplus\operatorname{Aug}(\mathbf Q[\mathcal D])\bigr),
\qquad
\widetilde H_4(K;\mathbf Q)\cong_G\mathbf 1.
\]
In particular, the third-homology character of \(g=(A,t)\) is
\[
\chi_3(g)=\delta(g)\bigl(|P^g|+|\mathcal D^g|-2\bigr).
\]
There are no nonzero globally fixed rational classes in degree three, whereas degree four contains a single trivial class.

## Assumptions and scope
The point set is \(P=\{(x,y):x,y\in\{0,1,2\}\}\). Its lines are the twelve three-point solution sets of \(ax+by=c\) over \(\mathbf F_3\), with \((a,b)\ne(0,0)\). The simplicial complex is on the nine points, not on the twelve lines. A subset is a face if and only if it is disjoint from at least one entire affine line. The affine action preserves incidence and hence acts simplicially. Homology groups use integral coefficients unless indicated otherwise.

The selected foundational literature source for this investigation is Kim and Kim, arXiv:2101.01850v1, first posted January 6, 2021. Its bounds and tight-path/tight-cycle calculations are not taken as proofs of this Hesse-specific result.

## Proof
Order points lexicographically as \((0,0),(0,1),\ldots,(2,2)\), assign indices zero through eight, and form the facets \(P\setminus L\) for the twelve lines \(L\), sorted lexicographically by their sorted index triples. Sorting faces lexicographically within each dimension gives the face-vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(9,36,84,126,72,12).
\]
The supplied standalone script `verify.py` independently constructs all \(339\) nonempty faces directly from these twelve facets.

Consider the following explicit face-poset matching. Visit point indices in the order \((2,6,7,3,5,1,4,0,8)\). At each step, for every currently unmatched face \(\sigma\) not containing the chosen index \(v\), match \(\sigma\) with \(\sigma\cup\{v\}\) whenever both are currently unmatched. The resulting \(163\) disjoint matched Hasse edges leave exactly one vertex, eleven three-faces and one four-face critical, and no other critical cells. There are \(1260\) codimension-one face incidences. Orient unmatched incidences downward and matched incidences upward. Topological sorting processes all \(339\) faces, verifying the absence of any directed cycle. Forman's discrete-Morse theorem therefore gives a CW model consisting of one \(0\)-cell, eleven \(3\)-cells and one \(4\)-cell.

It remains important not to infer the attaching map merely from the critical-cell count. Here an explicit integral four-cycle settles it. Denote by \(F_i\) the zero-indexed lexicographically ordered four-dimensional simplices, and define \(z=\sum_i c_iF_i\), where the nonzero index-coefficient pairs are

```
(0,1),(1,-1),(2,1),(3,1),(4,-1),(5,1),(7,-1),
(9,1),(11,-1),(14,-1),(16,1),(18,-1),(22,1),(23,-1),
(25,-1),(28,1),(30,1),(31,1),(34,-1),(35,-1),(36,-1),
(37,1),(38,-1),(39,1),(42,-1),(43,1),(46,1),(47,-1),
(50,-1),(51,-1),(55,1),(56,1),(59,-1),(66,1),(67,-1),(68,1).
```

Use standard increasing-index orientation. Exact cancellation gives \(\partial z=0\). The integral four-cochain \(\phi\) taking value \(+1\) on each of \(F_0\) and \(F_6\), and zero elsewhere, vanishes on the boundaries of all twelve five-simplices, while \(\phi(z)=1\). Hence \(z\) is a primitive, nonboundary homology class. With only one Morse four-cell, the Morse four-boundary must therefore be zero. The integral reduced homology is \(\mathbf Z^{11}\) in degree three and \(\mathbf Z\) in degree four, and zero elsewhere. Moreover, the CW model is initially \(\bigvee^{11}S^3\) before the four-cell attachment. Its attaching map lies in \(\pi_3(\bigvee^{11}S^3)\cong\mathbf Z^{11}\), where the coordinate degrees equal the (zero) integral cellular boundary entries. All coordinates vanish, so the attaching map is nullhomotopic and the displayed integral wedge decomposition follows.

For equivariance, the same four-cycle \(z\) is fixed in homology by four affine transformations generating \(G\): the linear transformations with matrices
\[
\begin{pmatrix}2&0\\0&1\end{pmatrix},\quad
\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
and translation by \((1,0)\). In the prescribed lexicographic ordering of oriented five-simplices \(E_i\), the differences \(g_*(z)-z\) are respectively the boundaries of the integral five-chains

```
E_11;
E_8+E_9;
E_9;
E_0+E_1+E_3-E_5-E_7+E_9.
```

Each identity is checked coefficient-by-coefficient. The four transformations generate all \(432\) affine permutations of the nine points, as a separate group-closure enumeration confirms. Since \(H_4(K;\mathbf Z)\cong\mathbf Z\), these boundary witnesses prove that the complete affine group acts trivially on degree-four homology.

For each affine transformation, compute the signed simplicial Lefschetz number \(L(g)\) as the alternating sum of signs of the induced permutations on setwise-fixed oriented faces. The exact enumeration over all \(432\) group elements verifies
\[
2-L(g)=\delta(g)\bigl(|P^g|+|\mathcal D^g|-2\bigr).
\]
By the rational Lefschetz trace formula and the just-proved triviality of degree-four homology, \(L(g)=1-\chi_3(g)+1\). Therefore the character of \(\widetilde H_3\) agrees with the character of the displayed determinant-twisted sum of two augmentation representations for every group element. Semisimplicity of rational finite-group representations proves the rational module isomorphism.

## Verification
Run `python3 verify.py` from an extracted package directory using Python's standard library. It checks the definition of all twelve lines; generation of all \(339\) faces; the full \(1260\)-incidence Morse acyclicity graph; the primitive integral top-cycle/cochain pairing; four explicit signed integral homology-action witnesses; complete group generation; and the trace identity for each of the \(432\) affine automorphisms. `EXPECTED.txt` contains the exact reference output. Separately, `verify_alt.py` computes all simplicial boundary ranks independently modulo four primes, with output in `EXPECTED_ALT.txt`; those modular ranks corroborate the integral proof but are not substituted for it. The source code is part of this package and is intended to be inspected and rerun; its output is not an independent external certification.

## Relationship to prior work
Kim and Kim, *Domination numbers and noncover complexes of hypergraphs* (arXiv:2101.01850v1, 2021), define this noncover construction, prove broad homological bounds, and classify tight-path and tight-cycle hypergraphs. The affine-plane line hypergraph is neither of those families, and their general bounds and Alexander duality do not specify the exact homotopy type or affine character computed here. Santhanam, Shukla and Singh, *Bounds for the collapsibility number of a simplicial complex and non-cover complexes of hypergraphs* (arXiv:2211.10607v1, 2022), prove collapsibility bounds; no exact affine-plane representation is asserted by the inspected statements. The Hesse incidence structure is the unique affine plane of order three and also defines a no-three-on-a-line cap complex. Under Alexander duality, the latter is related to the present complex, but none of the inspected prior sources gives the combined wedge decomposition and full \(432\)-element rational character.

The published finite-geometry literature also considers graph-metric Rips complexes of affine point-line *incidence* graphs and neighborhood complexes of projective *nonincidence* graphs. These are different simplicial complexes with different vertex/face definitions; a homotopy classification of either one does not, without an additional identified reduction, establish this noncover complex's affine module. That distinction was explicitly included in the comparison.

## Limitations
This is an exact result for the order-three affine plane, not a general classification of finite affine planes. The representation statement concerns rational homology and does not determine its full integral \(G\)-lattice or an equivariant homotopy splitting. The nondetection of an equivalent published result is limited to the sources and searches documented in `AUDIT.json`; it is not a uniqueness proof. A separate independent audit has not been performed.

## References
1. J. Kim and M. Kim, *Domination numbers and noncover complexes of hypergraphs*, arXiv:2101.01850v1 (first public version, 2021-01-06), https://arxiv.org/abs/2101.01850.
2. R. Santhanam, S. Shukla and A. Singh, *Bounds for the collapsibility number of a simplicial complex and non-cover complexes of hypergraphs*, arXiv:2211.10607v1 (first public version, 2022-11-19), https://arxiv.org/abs/2211.10607.
3. M. A. Henning and A. Yeo, *Affine Planes and Transversals in 3-Uniform Linear Hypergraphs*, Graphs and Combinatorics (2021), doi:10.1007/s00373-021-02285-x. This gives independent incidence-hypergraph motivation, not an asserted topological classification.
