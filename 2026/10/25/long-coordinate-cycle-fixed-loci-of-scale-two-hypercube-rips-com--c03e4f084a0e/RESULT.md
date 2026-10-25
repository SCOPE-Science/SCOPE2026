# Long-coordinate-cycle fixed loci of scale-two hypercube Rips complexes

## Finding
For every pair of integers \(k\ge4\) and \(m\ge0\), write \(n=k+m\). On the binary Hamming cube \(Q_n=\{0,1\}^n\), let \(\rho\) rotate the first \(k\) coordinates by one position and fix the final \(m\). Put
\[
X_{k,m}=\operatorname{VR}_{\le2}(Q_n),\qquad
Y_m=\operatorname{VR}_{\le2}(Q_m).
\]
The two fixed-vertex subcomplexes whose first \(k\) bits are respectively \(0^k\) and \(1^k\) are disjoint copies of \(Y_m\). Their inclusion gives a **strong deformation retract**
\[
|Y_m|\sqcup|Y_m|\ \hookrightarrow\ |X_{k,m}|^{\langle\rho\rangle}.
\]
In particular the fixed locus has precisely two path components. The convention \(Q_0=\{()\}\) makes the statement valid for \(m=0\).

By the integral homotopy classification of Adamaszek and Adams, for \(m\ge3\) each component has homotopy type
\[
\bigvee^{c_m}S^3,\qquad
c_m=\sum_{0\le j<i<m}(j+1)\bigl(2^{m-2}-2^{i-1}\bigr).
\]
For \(0\le m\le2\), each component is contractible. At \(m=3\), the fixed locus is two disjoint three-spheres.

## Assumptions and scope
All complexes are **abstract finite flag complexes**, and the Rips distance convention is inclusive, \(d_H\le2\). Geometric fixed points refer to the fixed subset of the actual simplicial geometric realization, not the complex induced by fixed vertices, the orbit-space quotient, nor the invariant subspace of an ambient homology group. The cyclic rotation acts on exactly one block of length \(k\ge4\), with \(m\ge0\) untouched coordinates. All retractions and homotopy equivalences are topological; the proof works integrally and is independent of a coefficient field.

## Proof
**1. A simplicial model for fixed points.** For a finite group acting simplicially on a finite complex \(K\), an invariant point in a face has equal barycentric coefficients on vertices belonging to each group orbit. Therefore \(|K|^G\) is naturally piecewise-linearly homeomorphic to the realization of an orbit complex \(T\): its vertices are group orbits of original vertices whose unions are simplices, and a collection of these orbit-vertices spans a simplex exactly when the union of their underlying orbits spans a simplex of \(K\). The homeomorphism sends an orbit-vertex to the barycenter of its underlying orbit. This follows directly from uniqueness of barycentric coefficients and disjointness of distinct orbits. We apply it to \(K=X_{k,m}\) and \(G=\langle\rho\rangle\).

**2. Classification of permissible orbit-vertices.** A binary word of length \(k\) and Hamming weight \(w\) has
\[
\sum_{j=0}^{k-1}d_H(u,\rho^j u)=2w(k-w),
\]
because every ordered pair of coordinates is sampled exactly once as the cyclic shift varies. If a rotation orbit is a simplex at scale two, then each of the \(k-1\) nonidentity shifts has distance at most two, so
\[
2w(k-w)\le2(k-1).
\]
For \(2\le w\le k-2\), the left side is at least \(4(k-2)>2(k-1)\) since \(k\ge4\). Hence \(w\) belongs to \(\{0,1,k-1,k\}\). Conversely the all-zero and all-one strings give singleton orbits, and all \(k\) rotations of a weight-one or weight-\(k-1\) string have mutual distance at most two, so all four cases occur. The unchanged \(m\)-bit string is constant along each orbit.

Denote the four permissible orbit-vertices indexed by \(z\in Q_m\) as \(A_z\) (zero block), \(B_z\) (one block), \(U_z\) (weight-one block), and \(V_z\) (weight-\(k-1\) block).

**3. All edges of the orbit complex.** A union of two allowed orbits is a simplex precisely if *every* cross-orbit Hamming distance is at most two. For distinct orbit-vertices, this occurs exactly in the following cases:
\[
\begin{array}{c|c}
\text{types}&\text{condition on }z,z'\\\hline
A_z,A_{z'}\text{ or }B_z,B_{z'}&d_H(z,z')\le2\\
A_z,U_{z'}\text{ or }B_z,V_{z'}&d_H(z,z')\le1.
\end{array}
\]
There are no other edges. Indeed the maximum rotated-block distance between any two distinct weight-one rotations is two; thus \(U_z,U_{z'}\) is impossible for \(z\ne z'\), and likewise for \(V\). Every pair of weight-one and weight-\(k-1\) orbits has a cross pair at distance \(k>2\). An all-zero block is at distance at least \(k-1>2\) from a weight-\(k-1\) block or the all-one block; the complementary cases are symmetric. These observations exhaust all types. Since the original Rips complex is flag, the orbit complex is flag too: pairwise compatible orbit-unions have mutually compatible vertices, so their total union is a simplex.

It follows that \(T\) has two disconnected subcomplexes. The first consists of the full subcomplex \(Y_m\) on \(\{A_z\}\) together with, for each \(z\in Q_m\), one additional cone vertex \(U_z\) whose link is the full simplex on
\[
B_1(z)=\{z'\in Q_m:d_H(z,z')\le1\}.
\]
The second is identical with \(B,V\) replacing \(A,U\). The ball \(B_1(z)\) spans a simplex of \(Y_m\) by the triangle inequality, since any two of its vertices have distance at most two. No simplex contains two distinct cone vertices.

**4. Explicit strong retraction.** On orbit-vertices of \(T\), fix \(A_z,B_z\) and set
\[
r(U_z)=A_z,\qquad r(V_z)=B_z.
\]
The edge classification shows this is a simplicial retraction onto the disjoint union of the two base copies of \(Y_m\). In fact, for every simplex \(\sigma\) of \(T\), the union \(\sigma\cup r(\sigma)\) is itself a simplex: if a cone vertex occurs, the other vertices belong to its simplex \(B_1(z)\), which contains its anchor. The linear interpolation \(H_t(x)=(1-t)x+t|r|(x)\), taken in each common simplex of the geometric realization, is therefore a continuous homotopy, fixes the target pointwise throughout, and ends at \(|r|\). Transporting this homotopy across the orbit-barycenter homeomorphism gives the asserted strong deformation retraction of the geometric fixed locus.

**5. Component homotopy types.** Each \(Y_m\) is connected (including \(m=0\)); for \(m\le2\) it is a full simplex. For \(m\ge3\), the previously established scale-two hypercube Rips theorem provides the stated integer three-sphere wedge count. In the first noncontractible case \(m=3\), antipodal pairs are the only nonedges, so \(Y_3\) is the boundary of a four-dimensional cross polytope, homeomorphic to \(S^3\).

## Verification
The standalone dependency-free program `verify_fixed_rotation.py` enumerates the actual cyclic orbits of every vertex of \(Q_{k+m}\) for 19 parameter pairs: \(k=4\) with \(0\le m\le4\), \(k=5,6\) with \(0\le m\le3\), and \(k=7,8\) with \(0\le m\le2\). It directly determines which orbits individually span Rips simplices and which distinct pairs of permissible orbits have a simplex union; it then compares all these pairs against the two-layer cone model and checks the retraction/identity contiguity edge-by-edge. Across these cases it recognizes 300 allowable orbit-vertices and checks 4,274 pairs, ending with `VERIFY_OK`. This is a finite consistency test; the preceding all-parameter argument is the proof. The companion `verify.log` gives the individual counts.

## Relationship to prior work
The equivariant-cohomology study of Adams and collaborators (2024) explicitly proposes hyperoctahedral Rips equivariance as an open direction; it does not classify the finite coordinate-rotation fixed loci here. Galetto, Montaño and Wellner (2026) compute rational homology representations of hypercube Rips complexes under the entire hyperoctahedral symmetry group at small scales; their representation-theoretic conclusions do not determine the geometric fixed-point homotopy type of this subgroup. Bendersky, Elia and Grbić (2026) study connectivity and cohomological classes of hypercube Rips complexes rather than geometric fixed subspaces. Adamaszek and Adams (2021) establish the ordinary scale-two homotopy type of each \(Y_m\); that theorem supplies only the *component* homotopy type here, not the two-component equivariant fixed-locus decomposition. The current theorem identifies a sharp simplification for coordinate cycles of length at least four, which is absent from these statements.

## Limitations
This result is restricted to an inclusive scale of two and a single cyclic permutation on one coordinate block. It does not classify the action of arbitrary permutations with several nontrivial cycles, the quotient of the ambient Rips space by the cyclic group, or the homology-invariant subspace of the ambient action. No independent scientific validation or comprehensive universal priority certification has been performed; equivalent unindexed work could exist. The explicit finite checks do not substitute for the general proof.

## References
1. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, originally submitted 2026-06-18, https://arxiv.org/abs/2606.20784.
2. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705, https://arxiv.org/abs/2605.00705.
3. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, https://arxiv.org/abs/2103.01040.
4. H. Adams, E. Lagoda, M. Moy, N. Sadovek and A. De Saha, *Persistent equivariant cohomology*, arXiv:2408.17331, https://arxiv.org/abs/2408.17331.
