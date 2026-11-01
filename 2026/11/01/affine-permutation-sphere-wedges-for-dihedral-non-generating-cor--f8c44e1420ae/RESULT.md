# Affine permutation sphere wedges for dihedral non-generating cores

## Finding

For every integer \(n\ge3\), let \(G=D_{2n}=\langle r,s\mid r^n=s^2=1,\;srs=r^{-1}\rangle\), let \(\Phi=\Phi(G)\) be its Frattini subgroup, and let \(C(G)\) be the simplicial complex on \(G\setminus\Phi\) whose faces are all sets generating proper subgroups of \(G\). Put \(m=\operatorname{rad}(n)=\prod_{p\mid n}p\), and \(k=\omega(n)\), the number of distinct prime divisors.

**Theorem.** There is an \(\operatorname{Aut}(G)\)-equivariant homotopy equivalence
\[
 |C(G)|\simeq_{\operatorname{Aut}(G)} \bigvee_{j\in\mathbb Z/m\mathbb Z}S^{k-1},
\]
where the right-hand side is the based wedge of \(m\) spheres, and an automorphism \(\alpha_{a,b}:r\mapsto r^a,\ s\mapsto r^bs\), with \(\gcd(a,n)=1\), sends the summand indexed by \(j\) to that indexed by \(aj+b\pmod m\), preserving its chosen orientation. For \(k=1\), the wedge means a discrete space of \(m+1\) points (one fixed basepoint and \(m\) permuted points).

In particular, **as an integral automorphism module**,
\[
\widetilde H_{k-1}(C(G);\mathbb Z)\cong\mathbb Z[\mathbb Z/m\mathbb Z],
\qquad \widetilde H_i(C(G);\mathbb Z)=0\quad(i\ne k-1),
\]
where the right-hand lattice has the affine permutation action. The trace of \(\alpha_{a,b}\) on rational reduced homology is \(d=\gcd(a-1,m)\) when \(d\mid b\), and is zero otherwise. The invariant submodule has rank one.

## Assumptions and scope

All groups and complexes are finite. Here \(D_{2n}\) has exactly \(2n\) elements, and \(n\ge3\) excludes the exceptional abelian presentation at \(n=2\). The Frattini core omits the cone vertices belonging to \(\Phi(G)\); the unreduced non-generating complex with those vertices reinstated is contractible. The homotopy statement is **equivariant**, not merely an isomorphism of homology groups. The integer coefficients and orientation choices are essential.

## Proof

**1. Maximal subgroups and the Frattini subgroup.** Every proper maximal subgroup of \(G\) is either the rotation subgroup \(R=\langle r\rangle\), or
\[
 M_{p,i}=\langle r^p,r^i s\rangle
 \quad(p\mid n\text{ prime},\ i\in\mathbb Z/p\mathbb Z).
\]
Indeed, a subgroup containing a reflection has the form \(\langle r^d,r^i s\rangle\) for a divisor \(d\mid n\), and it is maximal precisely when \(d\) is prime. A subgroup lacking reflections is contained in \(R\). Hence
\[
\Phi(G)=R\cap\bigcap_{p\mid n}\bigcap_{i\bmod p} M_{p,i}=\langle r^m\rangle.
\]
The automorphisms of \(G\) are exactly \(\alpha_{a,b}\) as in the theorem; they fix \(R\) and act on maximal-subgroup labels by \(M_{p,i}\mapsto M_{p,ai+b}\).

**2. Equivariant nerve.** Cover \(C(G)\) by the maximal simplices on \(M\setminus\Phi\), with \(M\) running through the maximal subgroups. The cover is invariant under \(\operatorname{Aut}(G)\). Every nonempty intersection is a simplex; every stabilizer of such an intersection fixes its barycenter. Therefore the equivariant nerve lemma applies: \(C(G)\) has the same \(\operatorname{Aut}(G)\)-homotopy type as its cover nerve \(K\). A subset of maximal-subgroup vertices is a face of \(K\) exactly when the intersection of those subgroups contains an element outside \(\Phi\).

**3. The precise nerve.** For each prime \(p\mid n\), write \(V_p=\{M_{p,i}:i\in\mathbb Z/p\mathbb Z\}\). Let \(I\) be a set of maximal-subgroup vertices. If \(I\) omits all of \(V_p\) for at least one prime \(p\), then its common rotation subgroup contains \(\langle r^{m/p}\rangle\), which is strictly larger than \(\Phi\), so \(I\) is a nerve face. If every prime block is represented, the common rotations are exactly \(\Phi\). An element outside \(\Phi\) then survives the intersection precisely if no \(R\) is selected and, for each \(p\), exactly one label \(M_{p,i_p}\) is selected: a surviving reflection \(r^js\) must satisfy \(j\equiv i_p\pmod p\) for every \(p\). The Chinese remainder theorem gives exactly one such \(j\pmod m\) for each tuple \((i_p)_p\). These are **all** faces of \(K\).

**4. Equivariant sphere model.** Let \(L\) be the subcomplex on \(\bigcup_p V_p\) consisting of sets omitting at least one prime block. This is invariant under all automorphisms. Let \(B=R*L\), the cone on \(L\) with apex \(R\). This is an invariant, equivariantly contractible subcomplex (the apex is fixed pointwise by every automorphism). The preceding paragraph shows that \(K\) is obtained from \(B\) by adjoining precisely the \(m\) simplices
\[
 T_j=\{M_{p,j\bmod p}:p\mid n\},\qquad j\in\mathbb Z/m\mathbb Z,
\]
each of dimension \(k-1\), whose entire boundary lies in \(B\). The equivariant quotient map \(K\to K/B\) is a homotopy equivalence by the equivariant cofibration lemma (the subcomplex \(B\) contracts through the invariant cone to its globally fixed apex). The quotient is a wedge of \(m\) spheres of dimension \(k-1\) if \(k\ge2\); for \(k=1\) it is a discrete space with \(m+1\) points. The action \(T_j\mapsto T_{aj+b}\) preserves the ordering of vertices by the underlying prime \(p\), and hence preserves the relative orientations. This proves the equivariant statement and the integral module description.

**5. Character.** A basis vector indexed by \(j\) is fixed by \(\alpha_{a,b}\) exactly when \((a-1)j\equiv-b\pmod m\). This linear congruence has \(\gcd(a-1,m)\) solutions if that number divides \(b\), and none otherwise. The affine translations act transitively on \(\mathbb Z/m\mathbb Z\), giving one invariant direction.

## Verification

The standalone Python script `verify.py` independently enumerates dihedral subgroups for \(n\le12\); constructs all stated maximal subgroups as concrete element sets; checks Frattini intersections, every nerve face and every affine image; and checks Euler characteristics and trace formulas for fifteen parameters including \(n=30,42,60\). Running `python verify.py` completes with `ALL_VERIFY_OK`. The program is a **finite cross-check** and is not used to justify the universal quantifiers of the theorem; those are proved above.

## Relationship to prior work

Dupont García's 2026 Frattini-core theorem gives a general nonequivariant reduction to the proper subgroup lattice for noncyclic groups; its explicit equivariant homology calculations and projective-geometry description focus on finite prime-power groups. The present proof uses the published Frattini framework as context but computes an explicit all-dihedral equivariant homotopy model, including the integral affine permutation representation, for arbitrary \(n\). In some powers-of-two cases, the earlier prime-group results already imply the underlying homology dimensions; no novelty is asserted for those special numerical ranks.

Cameron's 2024 paper introduced broader group-associated complexes and motivated their symmetry-sensitive study. General subgroup-lattice shellability results of Shareshian and earlier subgroup-lattice topology can already imply nonequivariant sphere-wedge phenomena for solvable groups; the assertion here is the **explicit equivariant realization**, including sphere labels, integral orientation action, and character, not a claim that the mere existence of a nonequivariant wedge is unknown.

## Limitations

The classification applies to dihedral groups of order \(2n\), \(n\ge3\), and to the Frattini core rather than the full cone-shaped non-generating complex. It does not compute the full automorphism group of the abstract simplicial complex (which may exceed the group-induced action), and it does not extend to arbitrary generalized dihedral groups. The proof invokes standard equivariant nerve and equivariant cofibration lemmas. An equivalent unindexed equivariant computation is a residual literature risk. No independent validation has yet been performed.

## References

1. L. A. Dupont García, *Frattini Geometry of Non-Generating Complexes: Symmetry, Homology and Betti Numbers*, arXiv:2610.10296v1 (first public 2026-10-07), especially Sections 3–5.
2. P. J. Cameron, *Simplicial complexes defined on groups*, arXiv:2410.22260v1 (2024-10-29).
3. J. Shareshian, *On the shellability of the order complex of the subgroup lattice of a finite group*, Transactions of the AMS (2001), DOI:10.1090/S0002-9947-01-02730-1 (abstract-level comparison for subgroup-lattice shellability).
