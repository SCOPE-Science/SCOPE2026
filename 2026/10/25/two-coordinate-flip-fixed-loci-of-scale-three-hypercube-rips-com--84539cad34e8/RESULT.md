# Two-coordinate flip fixed loci of scale-three hypercube Rips complexes form a cubical two-skeleton with sphere summands

## Finding

Let \(n\ge4\), let \(Q_n=\{0,1\}^n\) carry the Hamming metric, and let \(X_n=\operatorname{VR}_{\le3}(Q_n)\) denote its inclusive scale-three Vietoris–Rips complex. Let \(\tau\) flip precisely two coordinates. Put \(d=n-2\), and let \(C_d^{(2)}\) be the cubical two-skeleton of the standard \(d\)-cube. With \(s_d=2^{d-2}\binom d2\), the geometric fixed-point space satisfies the **integral homotopy equivalence**

\[
|X_n|^{\langle\tau\rangle}\simeq C_d^{(2)}\vee\bigvee^{s_d} S^3
\simeq \bigvee^{\,2^d-d2^{d-1}+s_d-1} S^2\vee\bigvee^{s_d}S^3.
\]

In particular, all reduced integral homology is free, concentrated in degrees two and three, with the indicated ranks. The two-sphere multiplicity is zero when \(n=4\), and positive for every \(n\ge5\). For \(n=2,3\), the same fixed locus is contractible (the low-dimensional boundary cases).

## Assumptions and scope

The simplicial complex includes a finite vertex set exactly when every Hamming distance is at most three. The involution is translation by a vector of Hamming weight two; its fixed points mean **geometric** fixed points after realization, not fixed original vertices. The cubes and their skeleta are ordinary finite cubical CW complexes. The dimension \(d\) is at least two in the asserted wedge formula. There is no claim about other Hamming scales, other weights, or a canonical splitting under the full automorphism group.

## Proof

**1. Orbit simplex model.** Every vertex orbit under \(\tau\) consists of a pair. A point of \(|X_n|\) is fixed precisely when its barycentric coordinates agree within each orbit and its support is an invariant simplex. Thus the fixed space is piecewise-linearly homeomorphic to the clique complex on compatible vertex orbits, where orbits are compatible if the union of both two-point orbits has diameter at most three.

Fix the first flipped coordinate to be zero in the unique orbit representative. Label its orbit by \((u,w)\), where \(u\in\{0,1\}\) is the second flipped coordinate and \(w\in\{0,1\}^{d}\) lists the unflipped coordinates. If two labels have outside Hamming distance \(h\), the largest distance between vertices in the corresponding two original orbits is \(h+2\) when their \(u\) entries agree and \(h+1\) when they disagree. Therefore distinct orbit vertices are adjacent exactly when

\[
(u=v\text{ and }h=1)\quad\text{or}\quad(u\ne v\text{ and }h\le2).
\]

**2. Cubical square blocks.** For every two-dimensional coordinate square \(F\) in the \(d\)-cube, let \(B_F\) be the induced orbit-clique subcomplex on all \((u,w)\) with \(w\) a corner of \(F\). In either \(u\)-layer the graph on these four corners is a four-cycle; between the two layers all cross edges occur. Consequently

\[
B_F=C_4*C_4\cong S^1*S^1\cong S^3
\]

as a triangulated sphere. Every clique in the orbit graph is contained in a square block. Indeed, in each layer a clique has at most two vertices, necessarily endpoints of a cube edge. One opposite-layer point compatible with both endpoints lies within a coordinate square containing that edge. If both layers contribute edges, their four endpoints have pairwise cross-distances at most two; parallel such edges are equal or opposite edges of a square, and different-direction such edges lie in a common square. The cases with at most one vertex in each layer also lie in a square, since every cube vertex and every pair at Hamming distance at most two belong to some square when \(d\ge2\).

**3. The common edge thickening.** For every cube edge \(e\), let \(B_e\) be the induced subcomplex on its two endpoints in both layers. All four orbit vertices form a three-simplex \(B_e\cong\Delta^3\). For a cube vertex \(v\), the two orbit vertices form \(B_v\cong\Delta^1\). Set \(A=\bigcup_e B_e\). Each square block intersects \(A\) in its four edge tetrahedra arranged cyclically; write this intersection \(L_F\). Adjacent tetrahedra meet along an edge \(B_v\), while opposite tetrahedra are disjoint. Thus \(L_F\simeq S^1\). Distinct square blocks intersect only in \(B_e\), \(B_v\), or the empty set, so all their intersections lie in \(A\).

There is a concrete strong deformation retraction of \(A\) onto the cube graph \(C_d^{(1)}\): map each orbit vertex \((u,w)\) to \(w\), section the graph by sending each \(w\) to the midpoint of its two orbit vertices, and interpolate linearly inside the tetrahedron \(B_e\). The homotopy is coherent on intersections. Its restriction to \(L_F\) retracts onto the perimeter of \(F\).

**4. One sphere per square.** Attach square blocks \(B_F\cong S^3\) to \(A\) in any order. As any two square blocks intersect inside \(A\), the attaching intersection for each successive block is exactly \(L_F\simeq S^1\). The map \(L_F\hookrightarrow B_F\) is nullhomotopic because \(B_F\cong S^3\) is simply connected. The homotopy-pushout splitting for such a null attachment gives

\[
Y\cup_{L_F}B_F\simeq (Y\cup_{L_F}\operatorname{Cone}(L_F))\vee S^3,
\]

where \(Y\) is the complex assembled from \(A\) and earlier blocks. Under the retraction of \(A\), each cone attaches a two-cell along the boundary loop of the corresponding cubical square. After all \(s_d\) square blocks, these cones reconstruct the entire cubical two-skeleton \(C_d^{(2)}\), with an independent \(S^3\) summand from every square.

**5. Two-skeleton rank.** The cubical two-skeleton is simply connected because higher-dimensional cube cells do not affect the fundamental group and the full cube is contractible. Being two-dimensional and simply connected, it is homotopy equivalent to a wedge of two-spheres. Its numbers of vertices, edges and squares are, respectively, \(2^d\), \(d2^{d-1}\) and \(s_d=\binom d2 2^{d-2}\). Euler characteristic gives exactly \(2^d-d2^{d-1}+s_d-1\) two-spheres. This proves the asserted integral homotopy and homology classifications. When \(n=2,3\), the direct orbit-clique complexes are simplices and hence contractible.

## Verification

Run `python3 verify.py` in a directory containing the attached verifier. It uses only the Python standard library, constructs the orbit graph both from original Hamming-distance pairs and from the symbolic adjacency rule, enumerates all cliques, verifies square coverage and all local square/edge face counts, and independently computes the complete reduced mod-two homology by column elimination. It checks \(4\le n\le9\), obtaining \((\beta_2,\beta_3)=(0,1),(1,6),(7,24),(31,80),(111,240),(351,672)\). These finite computations do not establish the universal homotopy assertion; the cubical-block and homotopy-pushout proof does.

## Relationship to prior work

The scale-three hypercube Rips complexes themselves were classified nonequivariantly by Feng, and Bendersky–Elia–Grbić developed a cohomological framework for the same family. Galetto–Montaño–Wellner determine the complete rational hyperoctahedral homology representation at scale three. Such representations control rational Lefschetz data, but they do not determine the homotopy types of the **geometric fixed-point subspaces**. The result here is a space-level, integral splitting for the natural two-coordinate translation involution; it does not assert a new description of the original Rips complex or its ordinary rational representation.

## Limitations

The construction is for a single involution and a single inclusive scale, not for a simultaneous fixed locus of a larger subgroup. The wedge decomposition is nonequivariant with respect to any remaining symmetries. Published-research overlap checks reduce but cannot eliminate the possibility of equivalent uncatalogued descriptions. No independent validation is asserted.

## References

- M. Bendersky, S. Elia, J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (first posted May 1, 2026), especially introduction and Sections 2–4.
- F. Galetto, J. Montaño, Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1 (first posted June 18, 2026), Main Theorem and Section 6.
- Z. Feng, *Homotopy types of Vietoris-Rips complexes of Hypercube Graphs*, arXiv:2305.07084 (first posted May 11, 2023).
- M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first posted March 1, 2021).
