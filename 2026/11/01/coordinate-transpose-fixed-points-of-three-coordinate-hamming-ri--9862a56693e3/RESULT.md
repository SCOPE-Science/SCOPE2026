# Coordinate-transpose fixed points of three-coordinate Hamming Rips complexes

## Finding
Let \(A\) be any alphabet of cardinality \(q\ge2\), let \(A^3\) have Hamming distance, and let \(\tau(a,b,z)=(b,a,z)\). For each real \(r\ge0\), form the inclusive Vietoris–Rips complex \(X_q(r)=\operatorname{VR}_{\le r}(A^3)\). Write \(F_q(r)=|X_q(r)|^{\langle\tau\rangle}\) for its **geometric**, rather than vertexwise, fixed-point space. Put
\[
B_q=\frac{(q-1)^2(q^2-2)}2.
\]
Then the entire homotopy filtration has the following four regimes:
\[
\boxed{
F_q(r)\simeq
\begin{cases}
\bigsqcup^{q^2}\{*\},&0\le r<1,\\
\bigsqcup^{q}\{*\},&1\le r<2,\\
\displaystyle\bigvee^{B_q}S^2,&2\le r<3,\\
\{*\},&r\ge3.
\end{cases}}
\]
All reduced integral homology is free. Its complete persistence barcode has \(q^2-q\) degree-zero intervals \([0,1)\), \(q-1\) degree-zero intervals \([0,2)\), and \(B_q\) degree-two intervals \([2,3)\), with no other reduced bars. Unreduced degree zero has in addition one infinite interval. The middle fixed locus is simply connected for every \(q\ge2\), despite potentially high-dimensional simplices. In particular, the numbers of two-spheres for \(q=2,3,4\) are \(1,14,63\).

## Assumptions and scope
The alphabet carries only its discrete equality metric; no field or group structure is required. A simplex of \(X_q(r)\) is a subset of vertices with all pairwise Hamming distances at most \(r\). The involution interchanges the first two **coordinate positions**, not alphabet symbols; it fixes the third coordinate. A geometric fixed point may lie in the interior of a simplex whose vertices are exchanged. All homotopies concern ordinary geometric realizations, and all bars have exact inclusive-birth, exclusive-death thresholds.

## Proof
**1. Canonical fixed-orbit triangulation.** For any involution of a finite simplicial complex, an invariant point has equal barycentric weights on the two vertices of every two-element orbit. Hence its geometric fixed space is naturally PL homeomorphic to the simplicial complex whose vertices are the involution's vertex orbits that individually span faces and whose faces are collections of orbits whose union spans a face. The homeomorphism sends each orbit vertex to the uniform barycenter of that orbit. This does not confuse the fixed space with the generally much smaller subcomplex induced by fixed vertices.

At radius two, the orbit vertices are
\[
d_{a,z}=\{(a,a,z)\},\qquad
p_{ab,z}=\{(a,b,z),(b,a,z)\},\quad a\ne b,
\]
with \(p_{ab,z}=p_{ba,z}\). There are \(q^2+q\binom q2=q^2(q+1)/2\) orbit vertices. Every orbit's internal Hamming diameter is at most two. Compare all pairs of original vertices in two orbits. For distinct suffixes \(z,w\), orbit vertices are adjacent in the fixed-orbit graph exactly when (i) both are the same diagonal letter \(d_{a,z},d_{a,w}\), or (ii) one is \(d_{a,w}\) and the other is \(p_{ab,z}\) with \(a\in\{a,b\}\). For equal suffixes, **every** pair of orbit vertices is adjacent. Two off-diagonal orbit vertices with different suffixes are never adjacent because the maximum first-two-coordinate distance across them equals two. These observations exhaust all possibilities by the additivity of the Hamming distance. The orbit complex is flag because its defining requirement is pairwise compatibility of the unions of orbits.

**2. A graph-shaped core.** Denote by \(K_q\) this fixed-orbit flag complex at radius two. For every suffix \(z\), let \(F_z\) be the full simplex on all orbit vertices with that suffix. For every letter \(a\) and suffix \(z\), let \(T_{a,z}\) be the full simplex on all \(q\) diagonal vertices \(d_{a,w}\) and on the \(q-1\) off-diagonal vertices \(p_{ab,z}\) with \(b\ne a\). Let \(B\subset K_q\) be the union of these \(q+q^2\) simplices.

We claim \(B\simeq K_{q,q}\), the complete bipartite graph with the two sets of \(q\) vertices corresponding to suffixes and letters. To prove this, use the displayed simplices as a cover of \(B\). Every nonempty intersection is a simplex and hence contractible, so the ordinary simplicial nerve theorem applies. In its nerve, the vertices \(t_{a,z}\) for a fixed \(a\) span a simplex; adjoining any single suffix vertex \(f_w\) to any face of that simplex again spans a simplex, because all relevant covering simplices contain \(d_{a,w}\). For distinct letters \(a\ne b\), the only intersections between their \(T\)-simplices are \(T_{a,z}\cap T_{b,z}=\{p_{ab,z}\}\). Consequently the only nerve simplex containing the edge \(t_{a,z}t_{b,z}\) is the triangle \(f_z t_{a,z}t_{b,z}\). Each such edge is a free face of its triangle, and collapsing all these triangle–edge pairs leaves the union, over letters \(a\), of complexes \(\Delta(\{t_{a,z}:z\in A\})*\{f_z:z\in A\}\), where the second factor is the discrete zero-dimensional complex. These \(q\) contractible pieces have pairwise intersection exactly the discrete set of \(q\) suffix vertices. Within each piece, matching every face containing a nonpreferred \(t_{a,z}\) against addition of a fixed preferred \(t_{a,z_0}\), while retaining all suffix vertices and their preferred edges, gives an elementary collapse relative to the suffix vertices onto the star of a new letter vertex. Thus the remaining nerve collapses onto the graph \(K_{q,q}\). This proves the claim, including \(\pi_1(B)\cong F_{(q-1)^2}\) and \(\chi(B)=2q-q^2\).

**3. The only cells outside the core.** Every clique not lying in some \(F_z\) or \(T_{a,z}\) is exactly one of the triangles
\[
\{p_{ab,z},d_{a,w},d_{b,w}\},\qquad a\ne b,\quad z\ne w,
\]
with unordered \(\{a,b\}\). Indeed, once a clique contains orbit vertices with different suffixes, the pairwise adjacency rules from step 1 force either a single diagonal letter (a \(T\)-clique) or exactly the two distinct diagonal letters in one suffix and their unique shared off-diagonal pair in another. No fourth vertex can be adjacent to all three vertices of such a triangle. Each of its three boundary edges belongs to \(B\), whereas the triangle does not. There are
\[
N_2=q(q-1)\binom q2=\frac{q^2(q-1)^2}{2}
\]
such distinct attached two-cells. Since \(B\) is homotopy equivalent to a graph, the homotopy-pushout property for cell attachments shows that \(K_q\) has the homotopy type of a two-dimensional CW complex.

**4. All loops vanish.** Under the equivalence \(B\simeq K_{q,q}\), the attaching loop of the triangle labelled by \((a,b,z,w)\) is the standard bipartite square \(f_z-t_a-f_w-t_b-f_z\). To see this without relying on an abstract label identification, note that its off-diagonal vertex belongs to \(F_z,T_{a,z},T_{b,z}\); its two diagonal vertices belong to \(F_w\) and their respective \(T\)-pieces. Homotopies inside those contractible simplices carry the three sides to exactly the four edges of the indicated square. Fix a base suffix \(z_0\) and base letter \(a_0\). The \((q-1)^2\) squares with \(z\ne z_0\) and \(a\ne a_0\), using \(w=z_0\), \(b=a_0\), normally generate \(\pi_1(K_{q,q})\): they are the fundamental cycles relative to a spanning tree consisting of all edges incident to either base vertex. Since all corresponding two-cells are attached, \(\pi_1(K_q)=0\).

**5. Integral homotopy and counts.** Cell attachment changes Euler characteristic by one per triangle, so
\[
\chi(K_q)=2q-q^2+\frac{q^2(q-1)^2}{2}
=1+B_q.
\]
A simply connected two-dimensional CW complex has zero reduced integral homology outside degree two and has free degree-two homology; its rank is \(\chi-1\). Representing an integral basis of \(H_2\) by sphere maps (Hurewicz) yields a homology equivalence from a wedge of \(B_q\) two-spheres, and the simply connected Whitehead theorem makes this a homotopy equivalence. Thus \(K_q\simeq\bigvee^{B_q}S^2\).

**6. Remaining scales and persistence.** For \(0\le r<1\) only the \(q^2\) diagonal singleton orbits are permitted and none are joined. For \(1\le r<2\) the same vertices form \(q\) disjoint simplices, one for each fixed diagonal letter. Radius two gives the just-proved wedge, and at radius three the ambient complex is a full simplex, so its fixed-orbit complex is a full simplex. Inclusions merge the \(q^2\) components first into \(q\), then into one; the second homology is present only at radius two. The asserted complete reduced and unreduced integral persistence barcodes follow, with no unresolved extension problems.

## Verification
Run `python3 verify_hamming_swap.py`. This standalone standard-library checker reconstructs the original metric orbit partitions and tests **every cross-orbit original point pair** at radius two. It verifies the proof's orbit adjacency criterion rather than taking it as input. Next it enumerates every simplex in the resulting flag complexes for \(q=2,3,4\), calculates every reduced mod-two boundary rank, and obtains only degree-two Betti numbers \(1,14,63\). The respective face vectors, indexed by simplex size, are \((6,12,8)\), \((18,90,153,90,27,3)\), and \((40,348,1000,1372,1344,952,496,180,40,4)\). It independently identifies every core face and exactly the \(q(q-1)\binom q2\) omitted bridge triangles; the core has only reduced degree-one mod-two rank \((q-1)^2\) at each tested size. It separately checks all scale-zero and scale-one component counts and confirms that the radius-three orbit graph is complete. It prints `VERIFY_OK` with the three Betti ranks. Finite computations corroborate the theorem but do not prove the all-alphabet homotopy classification: steps 1–6 supply the unrestricted argument.

## Relationship to prior work
Bendersky, Elia and Grbić (first public May 1, 2026) study cohomology and connectivity of **binary** Hamming Vietoris–Rips complexes without identifying geometric fixed-point homotopy types. Galetto, Montaño and Wellner (June 18, 2026) determine hyperoctahedral representations on ordinary homology of binary hypercube Rips complexes; their theorem is neither a fixed-space homotopy classification nor a nonbinary result. The 2026 published calculation *Complete Vietoris–Rips persistence of the ternary three-cube* determines the **ambient** scale-two homotopy type \(\bigvee^{46}S^3\), not the coordinate-swap fixed space; the present fixed space for the same \(q=3\) metric complex is \(\bigvee^{14}S^2\). Antolín Camarena and Carnero Bravo's work on categorical products of complete graphs treats ambient independence-complex homotopy, not the present involution's geometric fixed loci. In fact \(\operatorname{VR}_{\le2}(A^3)\) is the independence complex of the categorical product of three \(K_q\) graphs; this alternate description is explicitly included in the overlap comparison. Earlier calculations of fixed-point complexes for **binary** coordinate permutations or **alphabet translations** do not imply the uniform coordinate-transposition theorem for arbitrary \(q\), since these actions have different vertex orbits and different cross-orbit metric constraints.

## Limitations
Only three Hamming coordinates, the involution exchanging the first two, and a uniform finite alphabet are classified. The homotopy equivalences are nonequivariant (the fixed space has no remaining specified action). The proof does not determine homotopy types of ambient nonbinary Rips complexes, their integral symmetry representations, or general actions exchanging more coordinates. Algebraic independence or absolute historical uniqueness is not claimed; a structurally equivalent unindexed fixed-locus calculation remains a residual originality risk. No independent mathematical audit is claimed.

## References
1. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705, first posted 2026-05-01, https://arxiv.org/abs/2605.00705 (main theorem, Sections 1–2; full manuscript publicly accessible).
2. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1, 2026-06-18, https://arxiv.org/abs/2606.20784 (main theorem, Sections 1–2, specifically restricted to binary hypercube homology representations).
3. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, first posted 2023-07-23, https://arxiv.org/abs/2307.12401 (ambient three-factor categorical product context).
4. *Complete Vietoris–Rips persistence of the ternary three-cube*, published 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-vietoris-rips-persistence-of-the-ternary-three-cube--62d7487289d8 (ambient ternary calculation; entire available RESULT.md compared).
