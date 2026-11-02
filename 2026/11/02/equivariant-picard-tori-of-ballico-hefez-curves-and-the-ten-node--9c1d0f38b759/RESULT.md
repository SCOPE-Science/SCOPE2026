# Equivariant Picard tori of Ballico–Hefez curves and the ten-node sextic

## Finding
Let \(q=p^r\geq2\), and let \(B_q\subset\mathbb P^2_{\mathbb F_q}\) be the Ballico–Hefez curve, the image of
\[
\nu:[s:t]\longmapsto[s^{q+1}:s^qt+st^q:t^{q+1}].
\]
Put \(\delta=q(q-1)/2\), and let \(G=\operatorname{PGL}_2(\mathbb F_q)\), acting on \(B_q\) through its projective automorphisms. The following assertions hold as statements about algebraic group schemes, not only their rational points.

1. The connected generalized Jacobian is an \(\mathbb F_q\)-torus of dimension \(\delta\), with a (noncanonical) decomposition
\[
\operatorname{Pic}^0(B_q)\simeq
\left(R^1_{\mathbb F_{q^2}/\mathbb F_q}\mathbb G_m\right)^\delta.
\]
Geometric Frobenius acts by \(-1\) on each rank-one character-lattice factor.
2. Write \(\Omega=\bigl(\mathbb P^1(\mathbb F_{q^2})\setminus\mathbb P^1(\mathbb F_q)\bigr)/\langle x\mapsto x^q\rangle\), a set of \(\delta\) two-element Frobenius orbits. Over \(\overline{\mathbb F}_q\), the integral character lattice \(M=X^*(\operatorname{Pic}^0(B_q))\) is the **oriented signed permutation lattice** of \(G\) on \(\Omega\). For a stabilizer \(H\) of any \(\omega\in\Omega\), \(H\) is the normalizer of a nonsplit torus, a dihedral group of order \(2(q+1)\); with \(\varepsilon:H\to\{\pm1\}\) recording whether its element exchanges the two branches,
\[
M\simeq\operatorname{Ind}_H^G\mathbb Z_{\varepsilon}.
\]
3. **The scheme-theoretic fixed subgroup is independent of \(q\):**
\[
\boxed{\operatorname{Pic}^0(B_q)^G\simeq\mu_2\quad\text{over }\mathbb F_q.}
\]
For \(p=2\), this is the nonreduced group scheme \(\mu_2\), although it has only the identity geometric point.
4. In the distinguished degree-six case \(q=5\), \(G\cong\mathfrak S_5\), and its action on the rank-ten rational character lattice has the exact irreducible decomposition
\[
\boxed{M\otimes_{\mathbb Z}\mathbb Q\simeq
S^{(3,1,1)}\oplus S^{(2,1,1,1)},}
\]
where the summands have dimensions \(6\) and \(4\), respectively.

## Assumptions and scope
All curves and groups are considered over \(\mathbb F_q\), with \(q\) an arbitrary prime power at least two. Their geometric normalizations and characters are taken after extending scalars to an algebraic closure. The notation \(\operatorname{Pic}^0\) denotes the connected identity component of the Picard scheme of the singular *projective curve itself*. The fixed subgroup in part 3 is scheme-theoretic, under the constant finite group \(G\). The representation in part 4 is in characteristic zero on the **integral torus character lattice** tensored with \(\mathbb Q\), not an assertion about semisimplicity of a characteristic-five module.

## Proof
**Normalization and singular branch data.** The normalization morphism \(\nu:\mathbb P^1\to B_q\) is unramified and identifies precisely \(t\) and \(t^q\) for \(t\in\mathbb F_{q^2}\setminus\mathbb F_q\); each resulting singularity is an ordinary node. Indeed, on the affine chart \(s=1\), the coordinates \(t+t^q\) and \(t^{q+1}\) are the coefficients of the monic quadratic \((X-t)(X-t^q)\). Equal images with unequal parameters force conjugacy and then \(t^{q^2}=t\). Distinct tangent lines follow from the nonzero differential in the given parametrization. The point at infinity is smooth. Thus there are exactly \(\delta\) rational nodes with conjugate degree-two normalization branches, and normalization has genus zero. This recovers the published nodal description; no novelty is attributed to it.

**Picard torus and arithmetic descent.** For an integral nodal curve \(C\) whose normalization is \(\mathbb P^1\), a degree-zero invertible sheaf pulls back to a trivial sheaf. At each node it is reconstructed by identifying the two one-dimensional fibers of that trivial sheaf. A common change of trivialization cancels in each gluing ratio. Therefore \(\operatorname{Pic}^0(C_{\bar k})\simeq\mathbb G_m^{\#\operatorname{nodes}}\). At a rational node whose branches are exchanged by quadratic Frobenius, the descent involution sends a gluing ratio to its inverse. Its torus is \(R_{\mathbb F_{q^2}/\mathbb F_q}\mathbb G_m/\mathbb G_m\), isomorphic via \(z\mapsto z/z^q\) to the norm-one torus \(R^1_{\mathbb F_{q^2}/\mathbb F_q}\mathbb G_m\). As all nodes are rational, the product decomposition follows, and Frobenius acts as \(-1\) on \(M\).

**Automorphism action and stabilizers.** The full projective automorphism group is the published \(G\cong\operatorname{PGL}_2(\mathbb F_q)\). It acts on normalization parameters by fractional linear transformations over \(\mathbb F_q\); consequently it permutes the nodal pairs \(\{t,t^q\}\). Pullback of a gluing parameter acts by the same permutation, with inversion precisely if its ordered pair of branches is reversed. The action of \(G\) on \(\mathbb P^1(\mathbb F_{q^2})\setminus\mathbb P^1(\mathbb F_q)\) is transitive: the stabilizer of a geometric nonrational parameter is the image of \(\mathbb F_{q^2}^{\times}\) acting by multiplication on the two-dimensional \(\mathbb F_q\)-vector space \(\mathbb F_{q^2}\), modulo \(\mathbb F_q^{\times}\), and has order \(q+1\). Its normalizer adds a Frobenius-semilinear involution sending the parameter to its conjugate. Hence the unordered-pair stabilizer \(H\) has order \(2(q+1)\), contains a cyclic subgroup of index two fixing both branches, and is dihedral. The lattice is exactly \(\operatorname{Ind}_H^G\mathbb Z_{\varepsilon}\).

**Fixed subgroup, including characteristic two.** For a diagonalizable group with character lattice \(M\), taking scheme-theoretic fixed points under a finite constant group corresponds to taking coinvariants \(M_G=M/\langle gm-m\rangle\), *without dividing by the group order*. Induction and transitivity give
\[
M_G\simeq(\mathbb Z_{\varepsilon})_H\simeq\mathbb Z/(2),
\]
because some element of \(H\) exchanges branches. Thus the fixed diagonalizable subgroup is \(D(\mathbb Z/2)=\mu_2\) in every characteristic. Since quadratic Frobenius acts by \(-1\) on \(M\), it acts trivially on the coinvariants modulo two, so this identification descends to \(\mathbb F_q\). When \(p=2\), \(\mu_2\) is infinitesimal and must not be replaced by the trivial group scheme.

**The ten-node sextic.** For \(q=5\), \(G=\operatorname{PGL}_2(\mathbb F_5)\cong\mathfrak S_5\). A nonsplit torus is cyclic of order six, so under the abstract isomorphism its generator has cycle type \((3)(2)\) in \(\mathfrak S_5\). Its normalizer \(H\) is \(\mathfrak S_3\times\mathfrak S_2\), and \(\varepsilon\) is the sign of the \(\mathfrak S_3\) factor: its kernel is the subgroup \(C_3\times C_2\) of order six. Consequently the rational lattice is
\[
\operatorname{Ind}^{\mathfrak S_5}_{\mathfrak S_3\times\mathfrak S_2}
(\operatorname{sgn}_3\boxtimes\mathbf 1_2).
\]
By the Pieri rule \(s_{(1,1,1)}s_{(2)}=s_{(3,1,1)}+s_{(2,1,1,1)}\), giving the stated dimensions and irreducible decomposition.

## Verification
Run `python verify_bh_picard.py` with Python 3 and no third-party packages. For \(q=2,3,5\), the program enumerates every projective fractional-linear transformation, constructs all degree-two Frobenius pairs, computes the signed permutation action, and checks transitivity plus the stabilizer's equal numbers of signs. It verifies the coinvariant presentation \(\mathbb Z/2\) for these samples. For \(q=5\) it also computes the character's self-inner-product \(2\), consistent with the two distinct rational irreducibles established by Pieri theory. The unrestricted result is the proof above; finite enumeration is not used as an infinite proof.

## Relationship to prior work
Fukasawa–Homma–Kim (arXiv:1108.4227, first public version 2011-08-22), especially Theorem 2.2 and Corollary 2.4, give the parametrization, nodal geometry, rational-point counts and zeta function. Hoang–Shimada (arXiv:1402.3372, first version 2014-02-14), Proposition 1.3 and its proof, give the full projective automorphism group. Ballico (2014), Proposition 1, identifies the curve with the seminormal gluing of all degree-two Frobenius orbits on \(\mathbb P^1\). These are essential antecedents, not new contributions. The present explicit equivariant integral Picard character lattice, uniform scheme-theoretic fixed subgroup, and ten-node sextic representation decomposition are the additional claims.

## Limitations
The result concerns only the connected Picard group of the particular singular curve and its projective automorphism action. It does not classify G-linearized line bundles, Picard groups of cyclic branched covering surfaces, nor their Néron–Severi lattices. The norm-one factors and associated point-count implications follow readily from previously known nonsplit nodal geometry; novelty is not claimed for those facts separately. The conclusion on fixed points concerns group schemes, not just rational points. Although available relevant prior full texts and mathematical research records did not locate an equivalent complete equivariant statement, older general treatments of equivariant generalized Jacobians may imply some of its components; historical-priority verification remains independent.

## References
1. S. Fukasawa, M. Homma, S. J. Kim, *Rational curves with many rational points over a finite field*, arXiv:1108.4227 (first public version 2011-08-22), especially §2, Theorem 2.2 and Corollary 2.4. https://arxiv.org/abs/1108.4227
2. H. T. Hoang, I. Shimada, *On Ballico-Hefez curves and associated supersingular surfaces*, arXiv:1402.3372 (first public version 2014-02-14), especially Propositions 1.3–1.4. https://arxiv.org/abs/1402.3372
3. E. Ballico, *Singular curves over a finite field and with many points*, International Journal of Pure and Applied Mathematics 95 (2014), 223–232, especially Proposition 1 and its normalization construction. https://www.ijpam.eu/contents/2014-95-2/8/8.pdf
4. M. Rosenlicht, *Generalized Jacobian varieties*, Annals of Mathematics 59 (1954), 505–530 (classical Picard-gluing framework; no new theorem attributed).
