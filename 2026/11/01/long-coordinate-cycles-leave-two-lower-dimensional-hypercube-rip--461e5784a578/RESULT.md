# Long coordinate cycles leave two lower-dimensional hypercube Rips complexes

## Finding
Let \(k\geq4\), \(f\geq0\), and \(n=k+f\). Give the binary cube \(Q_n=\{0,1\}^n\) Hamming distance, and put \(X_n=\operatorname{VR}_{\leq2}(Q_n)\). Let \(H\cong C_k\) cyclically permute the first \(k\) coordinates while fixing the remaining \(f\) coordinates. Then the **actual geometric fixed-point space** \(|X_n|^H\) admits a canonical finite triangulation which simplicially strongly collapses onto a disjoint union of two copies of \(X_f=\operatorname{VR}_{\leq2}(Q_f)\):

\[
|X_n|^H\simeq |X_f|\sqcup|X_f|.
\]

The collapse is a deformation retraction equivariant for the commuting action of the hyperoctahedral group on the \(f\) fixed coordinates and the involution complementing all \(k\) moved coordinates. The latter involution exchanges the two copies. For \(f=0\), interpret \(Q_0\) as a one-point metric space.

Consequently, for \(0\leq f\leq2\), the fixed space has homotopy type \(S^0\). For \(f\geq3\), it has two connected components, each homotopy equivalent to \(\bigvee^{c_f}S^3\), where

\[
c_f=\sum_{j=0}^{f-3}2^j\binom{j+3}{3}.
\]

In particular, the case \((k,f)=(4,3)\) gives two three-spheres up to homotopy, and \((k,f)=(4,4)\) gives two components each homotopy equivalent to a wedge of nine three-spheres.

## Assumptions and scope
A simplex of \(X_n\) is a finite set of binary strings with all pairwise Hamming distances at most two (inclusive scale). The action is the simplicial action of \(H\), and its fixed space is taken on the **geometric realization**, not just on the vertexwise fixed subset. The claim applies to every integer pair \(k\geq4\), \(f\geq0\), without an upper bound on either parameter. No conclusion is asserted for arbitrary coordinate permutations with several nontrivial cycles or for other Rips scales.

## Proof
**1. Canonical orbit triangulation.** If a finite group acts simplicially on a finite flag complex \(X\), the geometric fixed space has a canonical triangulation whose vertices correspond to group-orbits \(O\) of original vertices for which the full orbit is a simplex; a collection of these orbit vertices spans a simplex precisely when their union spans a simplex of \(X\). Indeed, every fixed point in a simplex has barycentric coefficients constant on each vertex orbit; these conditions cut the simplex into the convex hull of its orbit barycenters. The pieces agree on common faces. Because \(X_n\) is flag, pairwise compatibility of the admissible orbits determines this orbit complex.

**2. Classification of admissible cyclic orbits.** Write a binary word as \((u,y)\) with \(u\in\{0,1\}^k\) on the rotating coordinates and \(y\in Q_f\). Let \(w\) be the Hamming weight of \(u\), and let \(\sigma\) rotate its coordinates. Counting disagreements over all cyclic shifts gives the exact identity

\[
\frac1k\sum_{j=0}^{k-1}d_H(u,\sigma^j u)=\frac{2w(k-w)}k.
\]

If the orbit is a simplex of \(X_n\), each summand is at most two and the zero-shift summand is zero. Thus \(w(k-w)\leq k-1\). For \(k\geq4\), every \(2\leq w\leq k-2\) instead satisfies \(w(k-w)\geq2(k-2)\geq k\). Hence only weights \(0,1,k-1,k\) are possible. All four possibilities do give admissible orbits. For each \(y\in Q_f\), denote their orbit vertices by \(A_y\) (all zero), \(C_y\) (one one), \(D_y\) (one zero), and \(B_y\) (all one), respectively. These are all the orbit vertices.

**3. Exact orbit compatibility.** Put \(\delta=d_H(y,z)\). Comparing the *maximum* distance between representatives of two orbits gives the complete edge description for distinct orbit vertices:

- \(A_yA_z\) and \(B_yB_z\) occur exactly when \(\delta\leq2\).
- \(A_yC_z\) and \(B_yD_z\) occur exactly when \(\delta\leq1\).
- No other edges occur (in particular, no distinct \(C\)-orbits or distinct \(D\)-orbits are adjacent).

For instance, two one-hot moving words can be distance two, so distinct \(C\)-orbit vertices have maximal distance \(2+\delta>2\); a one-hot word and a complementary one-hot word can be distance \(k>2\). The other assertions follow directly from their moving-block distances. Thus the fixed orbit complex has precisely two disjoint components, on the vertex sets \(\{A_y,C_y\}\) and \(\{B_y,D_y\}\).

**4. Explicit collapse.** The neighbors of \(C_y\) are exactly \(A_z\) with \(\delta=d_H(y,z)\leq1\). They span a simplex with \(A_y\), since every two such \(z\) differ in at most two positions. In particular, \(C_y\) is dominated by \(A_y\) in the flag complex, so deleting \(C_y\) is a simplicial strong collapse. Similarly, \(D_y\) is dominated by \(B_y\). Deleting every \(C_y,D_y\) leaves the induced complex on \(A\)- and \(B\)-vertices, exactly two disjoint copies of \(\operatorname{VR}_{\leq2}(Q_f)\).

There is also a canonical simultaneous simplicial retraction sending \(C_y\mapsto A_y\), \(D_y\mapsto B_y\) and fixing \(A_y,B_y\). For each simplex, its image-union is again a simplex by the compatibility description; hence this retraction is contiguous to the identity and yields a deformation retraction. It commutes with every Hamming isometry of the fixed coordinate block and with complementation of the moved block, which swaps the \(A,C\) and \(B,D\) components. This proves the claimed residual equivariance.

**5. Homotopy types and the sharp boundary.** The spaces \(\operatorname{VR}_{\leq2}(Q_f)\) are contractible for \(0\leq f\leq2\). For \(f\geq3\), Adamaszek and Adams prove their homotopy equivalence to a wedge of \(c_f\) three-spheres, with the stated sum for \(c_f\); applying their theorem separately to the two components proves the classification. The bound \(k\geq4\) is sharp in general: for \(k=3,f=0\), the four admissible orbit vertices form a chordless four-cycle, so the fixed space is \(S^1\), not two contractible components.

## Verification
The standalone script `checker.py` independently generates the cyclic orbits from binary strings, tests the diameter constraint, checks every pairwise orbit compatibility against the asserted adjacency classification, and checks all dominated-vertex inclusions. It passes \(28\) parameter pairs (\(4\leq k\leq8\), \(0\leq f\leq4\), and three additional larger-cycle pairs), covering \(648\) admissible orbit vertices and \(2448\) orbit-compatibility edges. The separate script `lefcheck.py` enumerates original Rips simplices in six small cases and evaluates the **signed simplicial Lefschetz trace** directly; it matches the fixed-space Euler characteristic, including the distinct \(k=3,f=0\) boundary case. Run `python checker.py` and `python lefcheck.py` in the directory containing the standalone scripts. These finite tests do not establish the infinite statement; Steps 1–5 do.

## Relationship to prior work
Adamaszek and Adams (2021 preprint, 2022 publication) establish the ordinary homotopy type of \(\operatorname{VR}_{\leq2}(Q_f)\); that sphere-wedge classification is used **as prior work** in Step 5, not claimed as new. Galetto, Montaño and Wellner (first public June 18, 2026) determine rational homology representations for hypercube Rips complexes under the full hyperoctahedral group, including scale two, but their results concern the homology of the **ambient** complex rather than the geometric fixed-space homotopy type. A character calculation determines a fixed-space Euler characteristic, not the two-component strong-collapse model or the componentwise homotopy types. Bendersky, Elia and Grbić (May 1, 2026 preprint) study ambient cohomological invariants and connectivity, rather than these geometric cyclic fixed spaces. The direct orbit classification and equivariant reduction above address the resulting geometric gap.

## Limitations
The fixed-space identification is a homotopy equivalence after a simplicial strong collapse, not a PL homeomorphism to two copies of the smaller Rips complex; only the canonical orbit triangulation is PL-homeomorphic to the geometric fixed space. The formula for \(c_f\) and the ambient smaller-cube homotopy type are previously known. This does not classify arbitrary subgroups of the hyperoctahedral group or all Rips filtration levels. An equivalent treatment in unindexed literature is not logically excluded; independent mathematical validation has not been performed.

## References
1. F. Galetto, J. Montaño, and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first public 2026-06-18), https://arxiv.org/abs/2606.20784.
2. M. Adamaszek and H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040 (first public 2021-03-01), https://arxiv.org/abs/2103.01040; J. Applied and Computational Topology 6 (2022), 177–192.
3. M. Bendersky, S. Elia, and J. Grbić, *Cohomological properties of the Vietoris--Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (first public 2026-05-01), https://arxiv.org/abs/2605.00705.
