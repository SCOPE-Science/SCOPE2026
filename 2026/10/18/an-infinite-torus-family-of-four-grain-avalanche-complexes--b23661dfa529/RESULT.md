# An infinite torus family of four-grain avalanche complexes

## Finding
For all integers \(d\geq3\) and \(n\geq2d+5\), let \(\overrightarrow C_n\) be the directed cycle with arrows \(i\to i+1\) on \(\mathbb Z/n\mathbb Z\). Initialize one chip at each vertex in \(\{0,1,d,d+1\}\) and zero elsewhere, and use synchronous out-degree-one sandpile firing. The resulting avalanche simplicial complex satisfies
\[
\mathcal A(\overrightarrow C_n,c_0)\searrow T_{n,d}\cong T^2,
\]
where \(T_{n,d}\) is an explicitly defined triangulated torus and the arrow represents **exactly \(2n\) elementary simplicial collapses**. Consequently its reduced integral homology is \(\mathbb Z^2\) in degree one, \(\mathbb Z\) in degree two, and zero otherwise. The integral cup product \(H^1\smile H^1\to H^2\) is nonzero. These complexes are **not** homotopy equivalent to any wedge of spheres.

## Assumptions and scope
The state is binary and has exactly four chips. The firing threshold is the out-degree (one), and all unstable vertices fire simultaneously. No vertex is a sink. A simplicial face is any nonempty subset of a firing support at some time; the empty face is understood. The integers satisfy \(d\geq3\) and \(n\geq2d+5\), with every index reduced modulo \(n\). No assertion is made for other parameters, asynchronous dynamics, or other initial chip configurations.

## Proof
**Firing-set orbit.** Each occupied vertex sends its sole chip to its successor and receives a chip from its predecessor, so the state is translated by one vertex per step. Its distinct firing sets are precisely
\[
 F_i=\{i,i+1,i+d,i+d+1\},\qquad i\in\mathbb Z/n\mathbb Z.
\]
The four elements of every set are distinct. Each set is a maximal three-simplex; there are \(n\) distinct such facets.

**Unique outer diagonal.** The six pairwise differences inside a facet, up to sign modulo \(n\), have absolute representatives \(1\), \(d-1\), \(d\), and \(d+1\). The parameter bounds ensure that all these classes are distinct as unoriented cyclic steps: \(1<d-1<d<d+1<n/2\). The step \(d+1\) occurs in a facet only along the edge \(e_i=\{i,i+d+1\}\); since these are distinct edges for distinct \(i\), \(e_i\) belongs to the unique tetrahedron \(F_i\). In particular \(T_i=\{i,i+1,i+d+1\}\), which contains \(e_i\), is a free codimension-one face of \(F_i\).

**First \(n\) collapses.** Remove the elementary pair \((T_i,F_i)\) for each \(i\). No such pair affects another free triangle or tetrahedron. Next, \(e_i\) occurs in the remaining complex only in the triangle \(U_i=\{i,i+d,i+d+1\}\). Therefore \((e_i,U_i)\) is an elementary collapse for every \(i\); removing these \(n\) pairs gives \(2n\) elementary collapses in total. The remaining facets are precisely
\[
 A_i=\{i,i+1,i+d\},\qquad B_i=\{i+1,i+d,i+d+1\},\qquad i\in\mathbb Z/n\mathbb Z.
\]
In particular, the initial face vector \((f_0,f_1,f_2,f_3)=(n,4n,4n,n)\) becomes \((n,3n,2n,0)\). Each prescribed deletion removes exactly its listed two faces; it does not invoke a non-elementary quotient.

**Identify the torus.** Triangulate the standard square grid on \(\mathbb R^2\) by splitting each unit square along the diagonal from \((a+1,b)\) to \((a,b+1)\). Label the lattice vertex \((a,b)\) by \(a+db\pmod n\). The label map has kernel
\[
 L=\{(a,b)\in\mathbb Z^2 : a+db\equiv0\pmod n\},
\]
a full-rank subgroup of index \(n\). The two triangles in each square descend exactly to \(A_i\) and \(B_i\); after reindexing \(B_{i-1}\), this is precisely the published cyclic torus triangulation \(T_{n,1,d-1}\) of Datta and Upadhyay [3, Example 1]. Since \(n\geq2d+5\) and \(d\geq3\), the six displacement classes \(\pm1\), \(\pm d\), and \(\pm(d-1)\) are distinct modulo \(n\), so each quotient vertex has six different grid neighbors and each square's vertices are distinct. Moreover the two triangle orbits are pairwise distinct: an \(A_i\) has edge steps \(1,d-1,d\), and the same holds for \(B_i\), but their unique \(d\)-step edges begin at \(i\) and \(i+1\) respectively; at a fixed such edge the third vertices lie on opposite sides in the grid. Thus this quotient is an honest finite simplicial triangulation (not a degenerate \(\Delta\)-complex). Its geometric realization is \(\mathbb R^2/L\), a two-torus. Equivalently, its connected vertex links are six-cycles, every edge is incident to two triangles, and its globally oriented square triangulation gives an orientable closed surface with Euler characteristic zero.

**Cohomological obstruction.** Elementary collapses preserve homotopy type, integral homology, and cup products. The torus has \(H^*(T^2;\mathbb Z)\) equal to the exterior algebra on two degree-one generators, whose product generates \(H^2(T^2;\mathbb Z)\). A connected wedge of spheres has vanishing products of positive-degree reduced cohomology classes, so the avalanche complex cannot be a wedge of spheres.

## Verification
The standalone `check_avalanche_torus.py` reconstructs the exact synchronous dynamics and its orbit of firing sets, enumerates all faces, independently applies every prescribed elementary-collapse pair by checking the **unique maximal coface condition**, and compares the survivor to the two-triangle-per-square quotient. For \(d=3,\dots,12\) and \(2d+5\leq n\leq2d+23\), it independently tests all \(190\) instances: initial and final face vectors, triangle uniqueness, edge incidences, six-cycle vertex links, and coherent orientability. Running `python3 check_avalanche_torus.py` reports the verified case count and terminates without dependencies. The all-parameter conclusion rests on the preceding combinatorial and lattice proof, **not** on finite testing.

## Relationship to prior work
Riihimäki and Smith [1] define the avalanche simplicial complex and classify several directed-path and directed-cycle initial states, including consecutive-chip blocks (Theorem 3.21) and certain three-chip supports (Proposition 3.23). Their discussion explicitly raises the existence of an avalanche complex which is not homotopy equivalent to a wedge of spheres. The two-separated-adjacent-pairs four-chip orbit is different: it has a nonzero integral cup product. The **target** is not a new torus triangulation: it is exactly Datta and Upadhyay's previously published \(T_{n,1,d-1}\) [3, Example 1]. What is new is the identification and explicit collapse of the **four-chip sandpile avalanche complex** onto this known torus. Related cyclic triangulations appear in Lutz [2]. Neither earlier geometric source asserts this avalanche construction, introduced in 2026.

## Limitations
The proof applies only within its stated parameter range. The target torus itself is explicitly known as \(T_{n,1,d-1}\) in Datta–Upadhyay (2004); only its realization as a four-chip avalanche complex with the stated collapse is advanced here. The finite checker independently verifies representative finite parameters but does not certify other parameters in place of the proof. Published-record searches cannot exclude unindexed or inaccessible equivalent constructions; independent review remains outstanding.

## References
[1] H. Riihimäki and J. P. Smith, *Avalanche homology of digraphs via sandpile dynamics*, arXiv:2606.26786v1 (first posted June 25, 2026), https://arxiv.org/abs/2606.26786.

[2] F. H. Lutz, *Equivelar and d-Covered Triangulations of Surfaces. II. Cyclic Triangulations and Tessellations*, arXiv:1001.2779, https://arxiv.org/abs/1001.2779 (earlier cyclic torus triangulations).

[3] B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:math/0403433, https://arxiv.org/abs/math/0403433 (Example 1 defines the identical target torus triangulation \(T_{n,1,d-1}\)).
