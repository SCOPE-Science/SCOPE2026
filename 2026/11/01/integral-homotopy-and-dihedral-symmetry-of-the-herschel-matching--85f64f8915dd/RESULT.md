# Integral homotopy and dihedral symmetry of the Herschel matching complex

## Finding

Let \(H\) be the eleven-vertex Herschel graph, with explicit labeled edges given below. Its **ordinary matching complex** \(X=\mathcal M(H)\) has a vertex for each edge of \(H\) and a face for each set of mutually vertex-disjoint graph edges. The following are exact conclusions:

\[
X\simeq\bigvee^{12}S^3,
\qquad
\widetilde H_i(X;\mathbb Z)=
\begin{cases}\mathbb Z^{12}&i=3,\\0&i\ne3.\end{cases}
\]

The complete automorphism group is the dihedral group \(D_6\) of order twelve. Its action on third rational homology is

\[
\widetilde H_3(X;\mathbb Q)\cong\mathbf 1\oplus\chi_{--}\oplus3E_1\oplus2E_2.
\]

Here \(\chi_{--}\) is the one-dimensional character sending both a rotation generator \(r\) and a reflection generator \(s\) to \(-1\). The two-dimensional rational characters \(E_j\) have values \(2\cos(2\pi jk/6)\) on \(r^k\) and zero on reflections, for \(j=1,2\). The trace vectors, ordered by \(k=0,1,\ldots,5\), are

\[
(\chi(r^k))_k=(12,1,-3,-2,-3,1),
\quad
(\chi(sr^k))_k=(0,2,0,2,0,2).
\]

Averaging the character yields one full-group invariant. Thus

\[
\widetilde H_3(|X|/D_6;\mathbb Q)\cong\mathbb Q,
\qquad
\widetilde H_i(|X|/D_6;\mathbb Q)=0\quad(i\ne3).
\]

## Assumptions and scope

Define \(V(H)=\{0,1,\ldots,10\}\). The eighteen unoriented edges, in lexicographic order, are

```
(0,1) (0,3) (0,4) (1,2) (1,5) (1,6)
(2,3) (2,7) (3,8) (3,9) (4,5) (4,9)
(5,10) (6,7) (6,10) (7,8) (8,10) (9,10)
```

This is an explicit presentation of the standard Herschel graph; identifying the graph by this edge list prevents ambiguity about graph embeddings or vertex labels. All homotopy and integral homology assertions concern the finite abstract complex \(X\). The quotient assertion concerns rational homology of the geometric realization modulo the full finite group of simplicial automorphisms. It does **not** assert a homotopy classification of that quotient.

## Proof

**Exact face enumeration.** Index the graph edges by \(0,\ldots,17\). Represent every matching by its eighteen-bit incidence mask; add each graph edge only when it is disjoint from the previously selected edges. This generates every matching exactly once. There are precisely \(751\) nonempty simplices, with face numbers in dimensions zero through four

\[
(f_0,f_1,f_2,f_3,f_4)=(18,111,280,270,72).
\]

**An acyclic matching on the face poset.** Visit the eighteen graph-edge indices in increasing order. At index \(j\), pair each currently unpaired nonempty matching \(\sigma\) not containing \(j\) with \(\sigma\cup\{j\}\), if this is also an unpaired matching. This rule pairs \(367\) simplex pairs, leaving one critical vertex, two critical two-simplices, and fourteen critical three-simplices. For reproducibility, their masks are:

```
critical 2-cells: [4132,16404]
critical 3-cells: [10512,17672,17928,18512,18696,34336,49668,
                   66656,67680,74244,139524,163860,163876,163908]
```

Reverse the orientation of each matched cover relation in the face poset, leaving every unmatched relation directed from a higher-dimensional face to a codimension-one face. Exhaustive enumeration checks all \(2502\) cover relations; a topological ordering visits all \(751\) nonempty faces, proving the directed graph is acyclic. Forman's discrete Morse reduction therefore gives a CW complex with exactly the stated critical cells.

**Integral attaching degrees.** Give a simplex with increasing graph-edge indices its usual alternating orientation. For a matched lower two-face \(\sigma\) and matched upper three-face \(\tau\), the standard algebraic Morse projection solves \(\partial\tau=0\) for \(\sigma\), using the incidence number \(\pm1\), and recursively projects to the critical two-faces. Applying this projection to boundaries of the fourteen critical three-faces yields the following complete integral \(2\)-by-\(14\) Morse boundary matrix, displayed by columns:

```
(1,0), (-1,1), (-1,1), (0,-1), (-1,1), (0,0),
(1,-1), (1,0), (1,0), (-1,0), (-1,0), (0,-1),
(-1,0), (0,0)
```

Its first and fourth columns form a determinant \(-1\) minor. Hence, after integral cellular changes of basis, the two degree-two cells are cancelled against two degree-three cells. There are no critical one-cells or cells of dimension above three. More precisely, before those cancellations the two-skeleton is \(S^2\vee S^2\) (with one zero-cell); the fourteen three-cell attaching maps are determined by their degrees because \(\pi_2(S^2\vee S^2)\cong\mathbb Z^2\). The unimodular minor makes two attaching maps a basis, so the resulting CW homotopy type is exactly \(\bigvee^{12}S^3\), not merely a complex with the same Betti numbers.

**Full symmetry character.** Enumerating degree-preserving adjacency-compatible permutations of the eleven graph vertices gives exactly twelve graph automorphisms. In the displayed labeling, choose

```
r=(6,10,5,1,7,8,9,4,0,2,3)
s=(0,3,2,1,4,9,8,7,6,5,10)
```

where a tuple lists the image of vertices \(0,\ldots,10\). Direct substitution establishes the dihedral relations and generation of all twelve automorphisms. For each automorphism, a matching simplex fixed setwise contributes its orientation sign multiplied by \((-1)^{\dim\sigma}\) to the ordinary simplicial Lefschetz number \(L(g)\). The homotopy classification above implies \(L(g)=1-\operatorname{tr}(g|\widetilde H_3(X;\mathbb Q))\). Computing these signs over all faces yields the stated trace vectors. Inner products with the six irreducible rational characters of \(D_6\) give multiplicities \((1,0,0,1,3,2)\) for the characters \((\mathbf1,\chi_{+-},\chi_{-+},\chi_{--},E_1,E_2)\). Finally, the rational homology of the quotient of a finite simplicial \(D_6\)-complex equals the invariant subspace, by averaging chains over this finite group; the trivial constituent appears exactly once.

## Verification

The supplied standalone Python program `verify_herschel.py` uses only the standard library. Run from its own directory with `python verify_herschel.py`. It re-enumerates every face, the full Hasse diagram, the exact integral Morse boundary, every graph automorphism, every signed Lefschetz trace, and the rational irreducible multiplicities; assertions fail if any expected certificate condition is violated. The included `verification_output.txt` records the output of that exact program. As an auxiliary cross-check, full simplicial boundary matrices (without Morse reduction) have ranks \((17,94,186,72)\) in degrees one through four over each of \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), agreeing with twelve third-dimensional generators. These finite-field checks do not establish torsion-freeness; the integral Morse attaching matrix does.

## Relationship to prior work

Jonsson's decision-tree and discrete-Morse framework [1] motivates exact topological calculations for graph complexes. Its worked matching-complex cases concern complete graphs, not this polyhedral graph. Bayer, Goeckner and Jelić Milutinović [2] investigate matching complexes that are homology manifolds, which does not determine this twelve-sphere wedge. Bayer, Jelić Milutinović and Vega [3] prove a wedge theorem for outerplanar graphs, whereas the Herschel graph is three-connected and planar but not outerplanar; its exact sphere multiplicity and symmetry module are not consequences of that theorem. The canonical labeled graph construction is described in [4]. Closely related previously published computations concern the **independence complex of the Herschel graph itself** and matching complexes of other polyhedral graphs; the former is not \(\mathcal M(H)=\operatorname{Ind}(L(H))\), and the latter have different edge-adjacency structures. No checked theorem implies the present combined homotopy and full dihedral-character assertion.

## Limitations

The result applies to this explicitly labeled finite graph and to the full rational character, not the integral representation lattice. It does not classify the homotopy type or fundamental group of the orbit space, nor provide a theorem for all polyhedral or non-Hamiltonian graphs. An equivalent result in unindexed literature remains possible. The computational certificate and mathematical argument have not undergone an independent external audit.

## References

[1] Jakob Jonsson, *Optimal Decision Trees on Simplicial Complexes*, Electronic Journal of Combinatorics **12** (2005), R3, DOI: 10.37236/1900; originally made public 2005-01-07.

[2] Margaret Bayer, Bennet Goeckner, and Marija Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328 (2019).

[3] Margaret Bayer, Marija Jelić Milutinović, and Julianne Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (first version 2024).

[4] SageMath graph generators, `HerschelGraph`, https://github.com/sagemath/sage/blob/develop/src/sage/graphs/generators/smallgraphs.py .
