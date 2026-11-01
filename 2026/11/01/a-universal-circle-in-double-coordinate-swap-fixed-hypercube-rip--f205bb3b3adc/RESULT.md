# A universal circle in double-coordinate-swap fixed hypercube Rips complexes

## Finding
For every integer \(n\ge4\), equip \(Q_n=\{0,1\}^n\) with Hamming distance, and write \(X_n=\operatorname{VR}_{\le2}(Q_n)\) for the inclusive Vietoris–Rips complex. Let \(s\) exchange positions \(1,2\) and \(t\) exchange positions \(3,4\). There is an *equality of geometric fixed-point subsets* of \(|X_n|\):
\[
|X_n|^{\langle st\rangle}=|X_n|^{\langle s,t\rangle}=:F_n.
\]
Furthermore \(F_n\) is connected and
\[
\pi_1(F_n)\cong H_1(F_n;\mathbb Z)\cong\mathbb Z.
\]
The natural map deleting the last \(n-4\) coordinates on admissible orbit barycenters gives a simplicial retraction \(F_n\to F_4\). The complex \(F_4\) collapses to a pentagon and hence is homotopy equivalent to \(S^1\). No assertion is made about higher homotopy groups of \(F_n\) for general \(n\).

## Assumptions and scope
A face of \(X_n\) is any nonempty subset of binary words having all pairwise Hamming distances at most \(2\). All fixed spaces refer to the geometric realization, not the subcomplex on pointwise fixed vertices. For a finite group acting simplicially, its geometric fixed locus has the canonical orbit-barycenter triangulation: vertices are barycenters of group orbits of original vertices that themselves form simplices; orbit vertices span a new simplex precisely if their union is a simplex of the original complex. This follows by writing fixed barycentric coordinates as equal coefficients on each vertex orbit.

Write \(m=n-4\), \(W=\{0,1\}^m\), and label binary words by the two initial bit pairs and a suffix \(w\in W\). The admissible orbits are
\[
A_{ab,w}=\{(aa,bb,w)\},\quad
C_{b,w}=\{(01,bb,w),(10,bb,w)\},\quad
D_{a,w}=\{(aa,01,w),(aa,10,w)\},
\]
where \(a,b\in\{0,1\}\). Every other orbit under \(st\) has its two members Hamming distance \(4\), so cannot occur in an invariant simplex. Under \(\langle s,t\rangle\), the same three types are exactly the admissible orbits; all remaining four-element orbits have diameter \(4\). Thus the two orbit-barycenter triangulations agree face-for-face, proving the asserted *equality*.

## Proof
**1. Compatible orbit pairs.** Put \(d=d_H(w,z)\). Within each fixed block \(A_{ab,*}\), vertices \(A_{ab,w}\) and \(A_{ab,z}\) are adjacent if and only if \(d\le2\). Between distinct fixed blocks, adjacency occurs only when \(w=z\) and exactly one of \(a,b\) changes, in which case the edge is called a *rung*. Each \(C_{b,w}\) is adjacent among fixed vertices precisely to \(A_{0b,z},A_{1b,z}\) with \(d\le1\); each \(D_{a,w}\) is adjacent to \(A_{a0,z},A_{a1,z}\) with \(d\le1\). No two distinct \(C\)-vertices are adjacent, and no two distinct \(D\)-vertices are adjacent. The only \(C\)--\(D\) adjacencies are \(C_{b,w}D_{a,w}\) with equal suffix. All of these assertions follow directly by maximizing Hamming distance between words in the two proposed vertex orbits. The resulting orbit complex is a flag complex by the diameter-two definition.

**2. Four fixed blocks and their fundamental group.** Let \(K\subset F_n\) be the induced subcomplex on the \(A\)-vertices. Each of its four fixed blocks is \(\operatorname{VR}_{\le2}(Q_m)\); the blocks are connected by four parallel families of rungs, one edge per suffix for each edge in the square of \((a,b)\)-labels. For \(m=0\), a fixed block is a point. For \(m\ge1\), each such complex is simply connected: every distance-two edge can be replaced, across a filled triangle, by a two-step path in the ordinary cube graph. Every edge loop in the cube graph reduces by square moves because the standard cubical \(m\)-cube is contractible, and each square's four vertices span a tetrahedron in \(\operatorname{VR}_{\le2}(Q_m)\). Hence, by the fundamental-group form of the graph-of-spaces theorem (or van Kampen), \(\pi_1(K)\) is free of rank \(4\cdot2^m-3\), represented by its four bundles of rungs.

**3. Coning the moving-vertex links.** Add the \(C_{b,w}\) vertices first. No two such vertices are adjacent, so each one attaches a cone over its link in \(K\). That link contains, for every suffix \(z\) with \(d_H(z,w)\le1\), both \(A_{0b,z}\) and \(A_{1b,z}\), together with their horizontal rung. Within each of the two fixed blocks, these link vertices form a simplex. Thus the link is connected and contains a loop running along the horizontal rung at \(w\), the cube-edge paths to \(w\oplus e_i\) in each block, and the reverse horizontal rung at \(w\oplus e_i\). Coning imposes the relation identifying those two horizontal rungs after the standard transport through the simply connected blocks. Since the suffix cube is connected, all horizontal rungs in a given bundle become equivalent. No new fundamental-group generator is introduced by any such connected-link cone.

Next add the \(D_{a,w}\) vertices. They are pairwise nonadjacent, and their links in the current complex are connected (already their fixed-vertex portion consists of two simplices joined by vertical rungs). Their cones similarly identify vertical rungs with suffixes \(w\) and \(w\oplus e_i\). There are again no new fundamental-group generators. The resulting \(\pi_1(F_n)\) is therefore a quotient of the fundamental group of the four-vertex square with one edge per side, namely \(\mathbb Z\). This step only asserts *generation by a single cyclic class*, not that any additional relations are absent.

**4. A surviving circle and exactness.** On the orbit complex, delete the suffix: send \(A_{ab,w}\mapsto A_{ab,0}\), \(C_{b,w}\mapsto C_{b,0}\), and \(D_{a,w}\mapsto D_{a,0}\). Every admissible union of original vertex orbits remains admissible after projection because discarding coordinates cannot increase Hamming distance. Hence this is a simplicial retraction \(p:F_n\to F_4\), with right inverse the suffix-zero inclusion. Direct enumeration of \(F_4\) gives eight vertices, sixteen edges and eight triangles. Eight elementary triangle–edge collapses followed by three edge–vertex collapses leave a five-edge cycle. In lexicographic orbit labels (listed by the standalone verifier), the triangle–edge pairs are
\[
(02,012),(01,013),(03,035),(12,124),(24,247),(35,356),(46,467),(56,567),
\]
followed by three leaf-pairs. Thus \(\pi_1(F_4)\cong\mathbb Z\). Since \(p\) splits the inclusion on fundamental groups, \(\pi_1(F_n)\) surjects onto \(\mathbb Z\); combined with its being a quotient of \(\mathbb Z\), this forces \(\pi_1(F_n)\cong\mathbb Z\). The integral \(H_1\) follows by abelianization. All quantifiers include \(m=0\).

## Verification
The self-contained program `check_fixed_double_swap.py` reconstructs orbit partitions under \(\langle st\rangle\) and \(\langle s,t\rangle\) separately and checks identical admissible orbit collections for \(4\le n\le8\). It enumerates the corresponding clique complexes, computes first homology over \(\mathbb F_2\) by exact boundary elimination, and verifies the explicit eleven-pair collapse of \(F_4\) to a pentagon. The sample face counts are \(32,124,492,1984,8032\) nonempty simplices for \(n=4,5,6,7,8\), respectively. These finite computations are consistency checks, **not** the proof of the unbounded claim; Steps 1–4 establish that claim.

## Relationship to prior work
Galetto, Montaño and Wellner determine characteristic-zero representations of the hyperoctahedral group on the *ambient* homology of \(\operatorname{VR}_{\le r}(Q_n)\), especially \(r=2\), but their stated results do not determine the fundamental group of geometric fixed-point spaces for a double transposition. Adamaszek and Adams determine the ambient scale-two homotopy type as a wedge of three-spheres; in particular, the ambient space is simply connected. The surviving fundamental circle is therefore genuinely fixed-locus topology, not inherited as an ambient fundamental-group class. Previously indexed geometric fixed-point results for a **single** coordinate transposition or coordinate-flip involution do not imply the intersection fixed under two independent transpositions.

## Limitations
The theorem describes the geometric fixed sets for one specific action on the inclusive scale-two binary cube filtration. It does not classify the complete higher integral homology, higher homotopy groups, or fixed loci for arbitrary coordinate permutations or filtration scales. The claim of originality is best-knowledge only; unindexed equivalent treatments remain possible. No independent mathematical validation is claimed.

## References
- Federico Galetto, Jonathan Montaño and Zoe Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1, first publicly posted 2026-06-18, https://arxiv.org/abs/2606.20784 .
- Michał Adamaszek and Henry Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, first posted 2021-03-01, https://arxiv.org/abs/2103.01040 .
