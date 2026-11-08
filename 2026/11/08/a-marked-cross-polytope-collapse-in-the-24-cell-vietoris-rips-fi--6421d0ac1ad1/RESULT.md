# A marked cross-polytope collapse in the 24-cell Vietoris–Rips filtration

## Finding
Let \(R\subset\mathbb R^4\) be the 24-element type-\(D_4\) root set consisting of all coordinate permutations of \((\pm1,\pm1,0,0)\), with all independent signs, and let \(K_r=\operatorname{VR}_{\le r}(R)\) for ambient Euclidean distance. Put
\[
B=\{(\pm1,\pm1,0,0)\}\cup\{(0,0,\pm1,\pm1)\}\subset R.
\]
**Marked-collapse theorem.** The inclusion \(K_2[B]\hookrightarrow K_2\) is a *simple-homotopy equivalence*: \(K_2\) admits a sequence of exactly 752 elementary simplicial collapses onto the induced subcomplex \(K_2[B]\), which is the boundary of a four-dimensional cross-polytope. Consequently this inclusion is an integral homology isomorphism in every degree; in degree three, the oriented fundamental class of this particular embedded 16-cell is a primitive generator of \(H_3(K_2;\mathbb Z)\cong\mathbb Z\). By coordinate permutation, the same is true for each of the three partitions of the four coordinate positions into two unordered pairs.

For completeness, the entire inclusive Euclidean filtration has integral homotopy types
\[
K_r\simeq\begin{cases}
\text{24 discrete points},&0\le r<\sqrt2,\\
\bigvee^{23}S^2,&\sqrt2\le r<2,\\
S^3,&2\le r<\sqrt6,\\
S^{11},&\sqrt6\le r<2\sqrt2,\\
\ast,&r\ge2\sqrt2.
\end{cases}
\]
Its nonzero reduced integral persistent homology comprises precisely 23 degree-zero intervals \([0,\sqrt2)\), 23 degree-two intervals \([\sqrt2,2)\), one degree-three interval \([2,\sqrt6)\), and one degree-eleven interval \([\sqrt6,2\sqrt2)\). These barcode multiplicities were already available as numerical homology information; the specific *embedded simplicial collapse and primitive geometric representative* are the substantive contribution here.

## Assumptions and scope
There are exactly 24 distinct points. The Vietoris–Rips convention is inclusive: a nonempty vertex set spans a simplex precisely when every pair has Euclidean distance at most \(r\). No metric on the one-skeleton is substituted for the Euclidean metric. The marked 16-cell uses the prescribed coordinate pairing \(\{1,2\}\,|\,\{3,4\}\). Other coordinate pairings follow by symmetry, not from a simultaneous equivariant collapse. Every homotopy and persistence claim refers to these exact finite vertex sets with integral coefficients unless explicitly indicated otherwise.

## Proof
**Distance shells.** All roots have squared norm two, so for distinct \(u,v\in R\), \(\|u-v\|^2=4-2\langle u,v\rangle\). The inner products are \(1,0,-1,-2\), occurring in respectively 96, 72, 96, 12 unordered pairs. Therefore the only nonzero critical Euclidean distances are \(\sqrt2,2,\sqrt6,2\sqrt2\). These claims are also checked exactly by `verify.py`.

**First nontrivial stage.** At \(r=\sqrt2\), the edges join exactly roots of inner product one. There are 96 edges, 96 triangles, and no tetrahedra, so the flag complex is the two-skeleton of the convex regular 24-cell. One can see the latter directly: its 24 octahedral three-faces are cut out by the supporting equations \(\pm x_i=1\) (eight faces) and \(\pm x_1\pm x_2\pm x_3\pm x_4=2\) (sixteen faces, independent signs). Each has six vertices and eight triangular faces, and each of the 96 triangular faces belongs to two octahedral cells. These cell boundaries form the boundary \(S^3\) of the convex 24-cell. The two-skeleton is simply connected, since attaching cells of dimension at least three does not change the fundamental group. Its cellular chain groups in degrees two and three show \(H_2\cong\mathbb Z^{23}\): the 24 top-dimensional octahedral cells have one integral top-dimensional relation, and \(H_3(S^3)=\mathbb Z\). A basis for \(\pi_2\) via Hurewicz gives a homology equivalence from \(\bigvee^{23}S^2\), hence a homotopy equivalence by the simply connected homological Whitehead theorem.

**The marked collapse at the middle stage.** At \(r=2\), the allowable pairs are exactly those with nonnegative inner product. Exact clique enumeration gives the face vector by dimensions zero through five:
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(24,168,480,600,288,24),
\]
thus 1,584 nonempty faces. The induced eight-vertex subcomplex on \(B\) omits precisely its four antipodal edges and has face vector \((8,24,32,16)\): it is a fourfold join of two-point sets, the boundary \(S^3\) of a 16-cell.

The accompanying exact certificate `collapse_pairs.json` specifies 752 ordered pairs of faces \((\tau,\sigma)\), in the lexicographically sorted vertex numbering reconstructed in `verify.py`. For each pair, the verifier reconstructs the *current* face set, verifies \(\tau\subset\sigma\) with codimension one, that \(\sigma\) is the **unique current immediate coface** of \(\tau\), and removes precisely those two faces. Neither face belongs to the target. After all 752 pairs, the 80 faces left are exactly the induced subcomplex on \(B\). The uniqueness test makes every pair an elementary simplicial collapse, so the certificate is a finite constructive simple-homotopy proof, not a homology-only experiment. Its conclusion also implies that the inclusion of the marked four-dimensional cross-polytope boundary induces an isomorphism on integral degree-three homology, making its fundamental cycle primitive.

**Last stages.** At \(r=\sqrt6\), the only missing edges are the twelve disjoint pairs \(\{v,-v\}\), so the entire flag complex is the join of twelve copies of \(S^0\), namely \(S^{11}\). At \(r=2\sqrt2\), all edges are present and the complex is the full simplex, hence contractible. Between the four critical distances no simplices are added. The asserted persistence intervals follow: positive-degree homology appears in mutually different degrees in consecutive nontrivial stages, so all adjacent inclusion maps on those groups are zero; at scale zero reduced degree-zero homology has rank 23 and becomes zero at \(\sqrt2\).

## Verification
The files `collapse_pairs.json` and `verify.py` are a standalone proof certificate and verifier requiring only the Python 3 standard library. Execute `python verify.py` from their common directory. The program regenerates the 24 integer roots and all cliques at the first two thresholds, checks the exact distance multiplicities, constructs the 24 octahedral facets and their triangle incidences, checks each one of the 752 free-face removals against the evolving full complex, and checks that the remaining induced complex is the fourfold join of two-point sets. It independently computes mod-two boundary ranks in the first two stages, as a corroboration rather than a substitute for integral homotopy proof. The reproducible output is preserved in `verification_output.txt` and ends in `VERIFY_OK`.

The certificate uses every one of the 1,584 nonempty faces at scale two: exactly 1,504 are removed in pairs, and 80 remain. No infinite conclusion is inferred from finite sampling: the theorem's domain is the explicitly finite 24-vertex set, and every possible simplex at the relevant scales is enumerated by exact integer comparisons.

## Relationship to prior work
Saleh, Titz Mite and Witzel (first arXiv version 28 February 2023) determine the Vietoris–Rips homotopy types of five ordinary three-dimensional Platonic solids. Their introduction remarks that analogous four-dimensional regular-polytope cases other than the 120-cell are easy, but gives no explicit 24-cell-to-16-cell elementary collapse or marked integral generator in the examined result. Consequently *the unmarked sphere labels alone are not asserted to be novel*. Saleh's 2023 dissertation, Chapter 4, section 4.2, page 73, already tabulates ranks 23, 1, 1 in degrees 2, 3, 11 for the 24-cell's three nontrivial stages, and identifies the first 23 classes with its octahedral cells. The table does **not** exhibit a simple-homotopy equivalence onto a fixed induced 16-cell. The present result strengthens that numerical information by a fully specified elementary-collapse sequence and a canonical geometric representative of the middle-stage integral generator.

The regular 24-cell's decomposition into three eight-vertex 16-cell subsets is itself classical and is not claimed as new. The relevant point is that the *Vietoris–Rips complex at the middle Euclidean threshold actually simplicially collapses* onto each selected induced 16-cell subcomplex, a substantially more precise statement than its existence as a subset or a matching Betti number.

## Limitations
The collapse sequence is finite and explicit, not a short uniform symbolic sequence, and it is not claimed to be equivariant under the full automorphism group. No general type-\(D_d\) statement for other dimensions is asserted. A full literature census cannot exclude equivalent results in unindexed sources, especially descriptions using root-system, spherical-building, or 16-cell terminology. Independent external validation of this certificate has not been performed.

## References
1. Nada Saleh, Thomas Titz Mite, Stefan Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388, first public submission 2023-02-28; https://arxiv.org/abs/2302.14388 .
2. Nada Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, doctoral dissertation, Justus Liebig University Giessen (2023), §4.2, p. 73; https://d-nb.info/1375949942/34 .
3. Dmitry Kozlov, *Organized Collapse: An Introduction to Discrete Morse Theory*, Graduate Studies in Mathematics 207 (2020), the elementary simplicial collapse framework. The finite certificate here uses elementary collapses directly.
