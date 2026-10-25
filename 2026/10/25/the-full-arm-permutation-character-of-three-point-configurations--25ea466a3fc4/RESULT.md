# The full arm-permutation character of three-point configurations on a star

## Finding
For every integer \(m\ge3\), the symmetric group \(\mathfrak S_m\) permuting the arms of the star graph \(S_m\) acts on the rational first homology of the **unordered collision-free three-point configuration space**
\[
X_m=\operatorname{UConf}_3(|S_m|)
=\{\{x_1,x_2,x_3\}\subset |S_m|:x_i\ne x_j\text{ for }i\ne j\}.
\]
Writing \(c_j(\sigma)\) for the number of length-\(j\) cycles of \(\sigma\in\mathfrak S_m\), its complete character is
\[
\boxed{\chi_m(\sigma)=1-c_1(\sigma)+\binom{c_1(\sigma)}2+2\binom{c_1(\sigma)}3-c_2(\sigma)-c_3(\sigma).}
\]
In particular,
\[
\dim_{\mathbb Q}H_1(X_m;\mathbb Q)=\frac{(m-2)(m-1)(2m+3)}6,
\qquad H_1(X_m;\mathbb Q)^{\mathfrak S_m}=0.
\]
The nonequivariant rank and free fundamental-group property are previously known; the finding is the **natural action of all arm permutations and its absence of invariant rational cycles**.

## Assumptions and scope
The star \(S_m\) consists of one central vertex and \(m\) closed arms, each an interval meeting the others only at the center. Arm permutations act by the evident graph homeomorphisms. All points in a configuration must be distinct; no collision is permitted, and particles are indistinguishable. The result is about the rational representation of the arm-permutation group \(\mathfrak S_m\), not the particle-label permutation group. Statements apply uniformly to every finite integer \(m\ge3\). The source convention \(c_j(\sigma)\) counts disjoint cycles of length exactly \(j\), including fixed points for \(j=1\).

## Proof
**1. A natural finite cubical model.** Subdivide every arm once, writing \(o\) for the central vertex, \(a_i\) for the newly inserted vertex, and \(b_i\) for the leaf. Each arm has edges \(p_i=[o,a_i]\) and \(q_i=[a_i,b_i]\). The unordered Abrams discrete configuration complex \(D_m\) has a \(k\)-cube for every unordered set of three open vertices/edges whose *closed* cells are pairwise disjoint, with one cube coordinate per chosen graph edge. Its inclusion into \(X_m\) is a homotopy equivalence: every simple path between distinct vertices of valence unequal to two has at least two edges, the sufficient-subdivision condition for three particles, and the tree has no cycles. The inclusion is canonical and commutes with all arm permutations; therefore it induces an isomorphism of \(\mathfrak S_m\)-homology representations (no equivariant choice of discrete-Morse matching is assumed).

**2. Higher rational homology vanishes.** Since the tree has precisely one essential vertex, the radial-tree theorem of Farley and Sabalka identifies \(\pi_1(X_m)\) as free and supplies a CW model of dimension at most one. The configuration space is connected. Thus \(H_k(X_m;\mathbb Q)=0\) for all \(k\ge2\), and the action on \(H_0\) is trivial. If \(\operatorname{STr}(\sigma;D_m)\) denotes the alternating signed cellular trace, the Hopf trace formula gives
\[
\chi_m(\sigma)=1-\operatorname{STr}(\sigma;D_m).
\]
For a fixed cubical cell, the cellular action sign is the parity of the permutation induced on its oriented edge-coordinate factors; nonfixed cells give zero trace.

**3. All fixed-cell contributions.** Introduce a formal variable \(z\) recording the number of particles. For configurations **without** any central edge \(p_i\), the central vertex is either unoccupied or occupied, giving \(1+z\). On one arm there are exactly five choices of compatible local cells: empty (weight 1), vertex \(a_i\) or \(b_i\) (each weight \(z\)), both vertices (weight \(z^2\)), and the distal edge \(q_i\) (signed weight \(-z\)). Their signed sum is \(1+z+z^2\).

For an orbit of \(\ell\) arms under \(\sigma\), all local choices must repeat around the orbit. Choosing all distal edges contributes \((-1)^\ell\) from cubical dimension and \((-1)^{\ell-1}\) from cycling those edge coordinates, hence total sign \(-1\). The complete orbit factor therefore is \(1+z^\ell+z^{2\ell}\). With \(c_\ell=c_\ell(\sigma)\), the contribution of cells with no central edge is
\[
[z^3](1+z)\prod_{\ell\ge1}(1+z^\ell+z^{2\ell})^{c_\ell}.
\]

A cell can contain at most one central edge because distinct central edges share the vertex \(o\). For such a cell to be fixed by \(\sigma\), that edge must belong to a fixed arm. There are \(c_1\) choices. The chosen central edge has signed weight \(-z\); the only compatible additional local vertex on that arm is \(b_i\), giving \(1+z\). On every other arm the previous orbit factors apply. Thus the contribution of cells containing a central edge is
\[
-[z^3]\,c_1z(1+z)(1+z+z^2)^{c_1-1}
\prod_{\ell\ge2}(1+z^\ell+z^{2\ell})^{c_\ell}.
\]
Combining the two cases gives a finite **exact** signed fixed-cell enumerator. Since only degrees at most three matter, every arm orbit of length at least four contributes its constant term. Direct coefficient extraction gives
\[
\operatorname{STr}(\sigma;D_m)
=c_1-\binom{c_1}{2}-2\binom{c_1}{3}+c_2+c_3.
\]
Subtracting from the trace 1 on \(H_0\) proves the character formula for **all** \(m\ge3\) and all permutations, not merely for those tested computationally.

**4. Rank and the invariant subspace.** For the identity permutation, \(c_1=m\) and \(c_2=c_3=0\). The formula simplifies to
\[
1-m+\binom m2+2\binom m3=\frac{(m-2)(m-1)(2m+3)}6.
\]
Over characteristic zero the fixed-subspace dimension is the average character. Uniform permutations of \(m\) letters satisfy
\[
\mathbb E\binom{c_1}{k}=\frac1{k!}\quad(k\le m),
\qquad \mathbb E c_2=\frac12,\quad\mathbb E c_3=\frac13\quad(m\ge3).
\]
Therefore
\[
\dim H_1(X_m;\mathbb Q)^{\mathfrak S_m}
=1-1+\frac12+\frac{2}{6}-\frac12-\frac13=0.
\]
All steps use identities valid for every integer in the stated range.

## Verification
The included executable Python 3 source `verify_star_three.py` enumerates every unordered triple of pairwise closure-disjoint original vertices/edges of the two-edge-per-arm graph. It independently constructs each permutation action on cells and evaluates the actual orientation sign of every fixed cell, not the generating polynomial. Connectivity of the zero/one-cell graph is checked, the integer Euler characteristic is compared with the known first Betti rank, and cellular Lefschetz traces are compared with the theorem. Exhaustive automorphism checks cover all 6, 24 and 120 permutations for \(m=3,4,5\), while one representative of every conjugacy class is additionally checked for \(m=6,7\). The 41 tested conjugacy classes, 150 exhaustive small-group elements, and `VERIFY_OK` output are recorded in `verify_star_three_output.txt`. These are finite corroborations, not a proof of infinitely many cases; the coefficient and homology argument above supplies the general proof.

## Relationship to prior work
Farley and Sabalka's original public 2004 preprint (2005 journal publication), particularly Section 4, Corollary 4.2 and Theorem 4.3, gives the free-group/homotopy framework and nonequivariant first Betti rank for radial trees. An and Maciazek's geometric presentation of braid groups gives generators and relations for stars (especially Section 3.2, Proposition 2 and Lemma 1), but the inspected statements do not give the complete natural character of arm permutations on unordered three-particle first homology. Lütgehetmann studies representation stability as arms are appended for *ordered* configurations; the inspected stability theorem does not specialize to this all-permutation explicit unordered character. Wawrykow studies ordered star configurations and particle-stabilization generators/relations, not the present \(\mathfrak S_m\) arm character. Related known nonequivariant classifications, including hard-core star configurations at positive separation, recover the rank but not the symmetry action. The present result is the full explicit character refinement. No uniqueness or absolute novelty follows merely from unsuccessful searches.

## Limitations
The result is only for **three unordered distinct points on an unweighted topological star** and the natural arm-permutation group. It does not describe integral lattice structure, ordered-particle actions, four or more particles, or length-dependent metric-spacing persistence. A character determines the rational representation up to isomorphism in characteristic zero, but it does not present an explicit integral cycle basis. The novelty comparison covers the inspected literature and database records; equivalent unindexed work or a derivation from an uninspected stronger theorem cannot be categorically excluded. Scientific assessment is not independent certification.

## References
1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539, first publicly posted 2004-10-25; Algebr. Geom. Topol. 5 (2005), 1075–1109. https://arxiv.org/abs/math/0410539
2. D. Lütgehetmann, *Representation Stability for Configuration Spaces of Graphs*, arXiv:1701.03490 (2017). https://arxiv.org/abs/1701.03490
3. B. H. An and T. Maciazek, *Geometric presentations of braid groups for particles on a graph*, arXiv:2006.15256 (2020); Comm. Math. Phys. 384 (2021), 1109–1140. https://arxiv.org/abs/2006.15256
4. N. Wawrykow, *Homology generators and relations for the ordered configuration space of a star graph*, arXiv:2401.13821 (2024). https://arxiv.org/abs/2401.13821
