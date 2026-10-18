# The Cartier congruence lattice and nonpolyhedral nef cone of the terminal cubic-elliptic fourfold

## Finding

Let \(E\subset\mathbf P^2_{\mathbf C}\) be \(u^3+v^3+w^3=0\), with origin \([0:-1:1]\), and let \(\rho[u:v:w]=[\zeta u:v:w]\), where \(\zeta\) is a primitive cube root of unity. Let \(A=E^4\), with diagonal \(\rho\)-action, and \(X=A/\langle\rho\rangle\). Put \(R=\mathbf Z[\zeta]\) and \(\pi=1-\zeta\). This is the terminal fourfold constructed by Ajit (arXiv:2610.09270v1).

Under the product principal polarization, \(\operatorname{NS}(A)\cong\operatorname{Herm}_4(R)\). The image of pullback on numerical Cartier classes is precisely

\[
\pi_X^*\operatorname{NS}(X)/\mathrm{tors}\;=\;\{H\in\operatorname{Herm}_4(R): H\equiv0\pmod\pi\}.
\]

Here the pullback image is interpreted inside the torsion-free lattice \(\operatorname{NS}(A)\); the displayed notation means the image of \(\operatorname{NS}(X)\) modulo torsion. The index of this lattice in \(\operatorname{NS}(A)\) is **\(3^{10}=59049\)**. In particular \(\rho(X)=16\).

Over \(\mathbf R\), numerical pullback identifies \(N^1(X)_{\mathbf R}\) with \(\operatorname{Herm}_4(\mathbf C)\). Both the nef and pseudo-effective cones are exactly the cone of positive-semidefinite Hermitian matrices. For every Cartier class represented by \(H\),

\[
D_H^4=8\det H.
\]

The cone has infinitely many distinct rational rank-one extremal rays. Consequently \(X\) is **not a Mori dream space**. More sharply, if \(v\in R^4\) is primitive and \(H_v=vv^*\), the primitive rank-one class \(H_v\) does not descend to a Cartier bundle on \(X\), whereas \(3H_v\) does. Its least positive Cartier multiple is exactly three.

## Assumptions and scope

The base field is \(\mathbf C\), and the group action, origin, and product principal polarization are as specified. Matrices are Hermitian over \(R\) with involution \(\zeta\mapsto\zeta^2\); \(v^*\) denotes conjugate transpose. Reduction modulo \(\pi\) identifies the involution with the identity and yields a symmetric matrix over \(\mathbf F_3\). The theorem concerns Cartier numerical classes on the singular projective variety \(X\), not arbitrary Weil divisor classes, and says nothing about the separate smooth resolution constructed in the source.

## Proof

**1. Hermitian Néron–Severi lattice.** The elliptic curve has endomorphism ring \(R\), and its degree-one symmetric polarization \(P=\mathcal O_E(O)\) identifies \(E\) with its dual. The product polarization \(\Theta=P^{\boxtimes4}\) gives the standard Rosati identification \(\operatorname{NS}(A)\simeq\operatorname{End}(A)^{\dagger=1}=\operatorname{Herm}_4(R)\), a free abelian group of rank \(4+2\binom42=16\). In addition to the four diagonal generators, it is generated over \(\mathbf Z\) by differences of rank-one classes \(vv^*\), taking \(v=e_i+e_j\) and \(v=e_i+\zeta e_j\). Each \(vv^*\) is the class of \(f_v^*P\), where \(f_v(t_1,\ldots,t_4)=\sum_j\overline{v_j}t_j\); the conjugation choice just fixes the matrix convention. Scalar \(\rho\) fixes all these line bundles under pullback because it commutes with \(f_v\), and therefore acts trivially on \(\operatorname{NS}(A)\).

**2. Stabilizer characters.** The fixed-point set is \(F=A[\pi]\simeq\mathbf F_3^4\). Ajit's Section 4.1 calculates the normalized fiber character for \(P\) at \(s\in E[\pi]\) to be \(\zeta^{s^2}\); the character can be normalized to one at the origin by twisting the linearization. Since \(f_v\) sends \(F\) to the linear form \(\ell_v(t)=\sum_j\bar v_jt_j\pmod\pi\), the fixed-fiber character of \(f_v^*P\) is \(\zeta^{\ell_v(t)^2}\). Tensor products, duals, and the rank-one generators therefore supply a \(\rho\)-invariant representative \(L_H\) of any \(H\in\operatorname{Herm}_4(R)\), with a normalized linearization whose fiber character at \(t\in F\) is

\[
\chi_{H,t}(\rho)=\zeta^{q_H(t)},\qquad q_H(t)=t^{\mathsf T}\overline Ht\in\mathbf F_3,
\]

where \(\overline H\) denotes reduction modulo \(\pi\), not complex conjugation. The identity follows on rank-one generators by \(\ell_v(t)^2=t^{\mathsf T}\overline{vv^*}t\), hence on their integer span.

**3. All numerically equivalent representatives.** Any invariant line bundle numerically equivalent to \(L_H\) is \(L_H\otimes N\), with \(N\in\operatorname{Pic}^0(A)^\rho\). By the \(\rho\)-equivariant principal polarization, these are precisely the 81 degree-zero classes corresponding to \(a\in A[\pi]=F\). They are represented by \(T_a^*\Theta\otimes\Theta^{-1}\). At \(t\in F\), its fiber character is \(\zeta^{q_\Theta(t+a)-q_\Theta(t)}\), where \(q_\Theta(t)=\sum_i t_i^2\). The exponent equals \(2a\cdot t+\sum_i a_i^2\), an affine-linear function. Varying the linearization by one of the three group characters changes only the constant term. Thus **the quadratic part of \(q_H\) is independent of the representative and linearization**.

By the finite-quotient descent criterion (Ajit, Lemma 3.1), a representative descends precisely when its stabilizer character is trivial at every \(t\in F\). An affine-linear function cannot cancel a nonzero homogeneous quadratic form on \(\mathbf F_3^4\): evaluation at \(t\) and \(-t\), followed by subtraction and addition, separates its linear and quadratic parts, and a quadratic form whose values vanish identically has zero symmetric matrix because the characteristic is not two. Thus descent is possible if and only if \(\overline H=0\). Conversely, when \(\overline H=0\), the constructed \(L_H\) already has trivial fixed-fiber characters and descends. This proves the exact pullback image.

**4. Index and volume.** A Hermitian matrix reduces to a symmetric matrix over \(R/(\pi)=\mathbf F_3\). Each of the four diagonal and six off-diagonal coordinates can be prescribed independently by the rank-one generators. The reduction is therefore surjective onto the ten-dimensional space \(\operatorname{Sym}_4(\mathbf F_3)\), and its kernel has index \(3^{10}\). Riemann–Roch on \(A\) gives \((\pi_X^*D_H)^4=24\det H\). Since \(\deg(\pi_X)=3\), the projection formula yields \(D_H^4=8\det H\). For Ajit's specified polarization, the isogeny matrix has determinant \(\pi^2\); hence \(\det H=9\) and the formula recovers the already-known \(D^4=72\).

**5. The nef cone and Mori-dream obstruction.** On the abelian variety \(A\), \(H\) is ample exactly when its associated Hermitian form is positive definite; taking closures gives the positive-semidefinite nef cone. Conversely, a negative direction contains arbitrarily close rational directions represented by vectors in \(R^4\), giving an elliptic subcurve of negative degree; thus no other matrices are nef. A finite surjective pullback preserves and detects ampleness and nefness. Every effective divisor on an abelian variety is nef, so the pseudo-effective cone is contained in the nef cone; the reverse inclusion follows by closure of the ample cone. The same equalities descend numerically to \(X\) under the finite quotient. The matrices \(vv^*\) span rank-one extreme rays of the positive-semidefinite cone. For example \(v=(1,n,0,0)\) for integers \(n\ge0\) gives infinitely many distinct rational extremal rays. All \(3vv^*\) are pullbacks of Cartier classes by the congruence criterion, while \(vv^*\) is not because its first diagonal entry is one modulo \(\pi\). Finally \(H^1(X,\mathcal O_X)=H^1(A,\mathcal O_A)^\rho=0\), and \(X\) is \(\mathbf Q\)-factorial, but a Mori dream space must have rational polyhedral nef cone. Hence \(X\) is not one.

## Verification

The standalone dependency-free script `verify.py` works over \(\mathbf F_3\). It independently constructs the evaluation vectors of all ten quadratic coordinate functions and the five affine coordinate functions on all 81 fixed points. It computes rank ten for the quadratic span and rank fifteen for their sum; therefore no nonzero quadratic residue can be affine-linear. It also reduces the originating paper's isogeny matrix, verifies the vanishing of its Hermitian Gram matrix modulo \(\pi\), and checks the nine-point totally isotropic image. Run `python3 verify.py` and require `VERIFY_OK`. These finite calculations corroborate exact algebraic arguments; they are not substitutes for the Rosati identification, descent criterion, or numerical cone proof.

## Relationship to prior work

Ajit, *Counterexamples to the Ambro–Kawamata effective non-vanishing conjecture* (arXiv:2610.09270v1, first public October 7, 2026), constructs \(X\), its 81 terminal singularities, the ample Cartier counterexample, and the stabilizer character calculation. His Section 3 descent lemma and Section 4.1 fiber formula are crucial input; the example, its non-vanishing failure and the degree \(D^4=72\) are **not** new here. The standard Rosati description of the Néron–Severi group of a polarized product is also known. The additional determination is the *entire* congruence sublattice of Cartier classes, its index, the full nef and pseudo-effective cones, and their Mori-dream consequence, obtained by including all degree-zero twists and all Hermitian classes.

Hu–Keel's Mori dream space criterion and the general polyhedrality of nef cones on Mori dream spaces are standard; the non-Mori-dream statement is an application to this particular terminal quotient rather than a new characterization of all such varieties.

## Limitations

The result is proved over \(\mathbf C\); the positive-characteristic construction of the originating paper is not addressed. The congruence lattice concerns numerical Cartier classes, not the integral class group of Weil divisors nor the full Picard torsion. The cone identification is numerical; it does not assert a finite presentation of any Cox ring. The exact novelty assessment is relative to the inspected full preprint and targeted published-record searches: a stronger theorem on Picard descent for scalar finite quotients could subsume the classification under other language, and independent literature review remains outstanding.

## References

1. Rahul Ajit, *Counterexamples to the Ambro–Kawamata effective non-vanishing conjecture*, arXiv:2610.09270v1 (October 7, 2026), especially Sections 3 and 4; https://arxiv.org/html/2610.09270v1.
2. D. Mumford, *Abelian Varieties*, 2nd edition (1974), corrected reprint (2008), standard theory of endomorphisms, duality and polarizations.
3. Y. Hu and S. Keel, *Mori dream spaces and GIT*, Michigan Math. J. 48 (2000), 331–348.
4. M. C. Brambilla, O. Dumitrescu, E. Postinghel and L. J. Santana Sánchez, *Duality and polyhedrality of cones for Mori dream spaces*, Math. Z. 309 (2025), article 69; https://doi.org/10.1007/s00209-025-03699-6.
