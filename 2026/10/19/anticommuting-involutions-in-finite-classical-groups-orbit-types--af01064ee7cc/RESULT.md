# Anticommuting involutions in finite classical groups: orbit types and dihedral subgroup counts

## Finding

Let \(q\) be an odd prime power. For any of the finite classical matrix groups \(G\) specified below, define
\[
\mathcal A(G)=\{(S,T)\in G^2:S^2=T^2=I,\ ST=-TS\}.
\]
The pairs are **ordered**, both generators are involutions, and the displayed anticommutation is equality of matrices rather than a condition in the projective quotient. Their generated subgroup is dihedral of order eight, with center \(\{I,-I\}\). In particular, \(|\mathcal A(G)|/8\) counts subgroups isomorphic to this dihedral group whose central involution is \(-I\).

Here \(\mathrm{GL}_d(q)\) and \(\mathrm{SL}_d(q)\) act on \(\mathbb F_q^d\); \(\mathrm U_d(q)\) and \(\mathrm{SU}_d(q)\) act on a nondegenerate Hermitian space over \(\mathbb F_{q^2}\); \(\mathrm{Sp}_{d}(q)\) preserves a nondegenerate alternating form; and \(\mathrm O(V,B)\), \(\mathrm{SO}(V,B)\) preserve a nondegenerate symmetric bilinear form \(B\) on \(V\) over \(\mathbb F_q\). The special groups are determinant-one subgroups, not projective quotients.

**Theorem (complete pair census).** Every odd-dimensional group listed above has \(\mathcal A(G)=\varnothing\). For dimension \(d=2m\ge2\), write \(g_j=|\mathrm{GL}_j(q)|\), \(u_j=|\mathrm U_j(q)|\), and \(s_{2k}=|\mathrm{Sp}_{2k}(q)|\). Then:

1. In \(\mathrm{GL}_{2m}(q)\), there is exactly one simultaneous-conjugacy orbit and
\[|\mathcal A(\mathrm{GL}_{2m}(q))|=g_{2m}/g_m.\]
   In \(\mathrm{SL}_{2m}(q)\), there are no pairs if \(m\) is odd. If \(m\) is even, its pair set equals that of \(\mathrm{GL}_{2m}(q)\), but the one general-linear orbit splits into **exactly two** special-linear orbits of equal size.

2. In \(\mathrm U_{2m}(q)\), there is exactly one simultaneous-conjugacy orbit and
\[|\mathcal A(\mathrm U_{2m}(q))|=u_{2m}/u_m.\]
   In \(\mathrm{SU}_{2m}(q)\), there are no pairs if \(m\) is odd. If \(m\) is even, all unitary pairs lie in the special unitary group, where the unitary orbit splits into **exactly two** equally sized orbits.

3. In \(\mathrm{Sp}_{2m}(q)\), there are pairs if and only if \(m\) is even. For \(m=2k\ge2\), there is exactly one orbit and
\[|\mathcal A(\mathrm{Sp}_{4k}(q))|=s_{4k}/s_{2k}.\]

4. For the orthogonal group in dimension \(2m\), put \(\Delta=\det B\in\mathbb F_q^\times\). There are pairs **if and only if \(\Delta\) is a square**. In that case let \(W_{\square}\) and \(W_{\mathrm{ns}}\) be representatives of the two nondegenerate symmetric \(m\)-spaces distinguished by the square class of their Gram determinants. There are exactly two simultaneous \(\mathrm O(V,B)\)-orbits, one for each class, of respective sizes
\[
\frac{|\mathrm O(V,B)|}{|\mathrm O(W_{\square})|}
\quad\text{and}\quad
\frac{|\mathrm O(V,B)|}{|\mathrm O(W_{\mathrm{ns}})|}.
\]
   If \(m\) is odd, no pair belongs to \(\mathrm{SO}(V,B)\). If \(m\) is even and \(\Delta\) is a square, every pair lies in \(\mathrm{SO}(V,B)\) and **each orthogonal orbit splits into two equal special-orthogonal orbits**, yielding exactly four special-orthogonal orbits. Otherwise the special-orthogonal pair set is empty.

The possible orthogonal ambient Witt type is consequently sharp: a \(2m\)-dimensional orthogonal space supporting such pairs is split exactly when \(\chi_q((-1)^m)=1\), where \(\chi_q\) is the quadratic character of \(\mathbb F_q\). In particular, dimension divisible by four permits pairs only in the split orthogonal group; in dimension congruent to two modulo four the allowable group is split for \(q\equiv1\pmod4\) and nonsplit for \(q\equiv3\pmod4\).

In all nonempty cases the number of distinct embedded dihedral subgroups with central element \(-I\) is exactly **one eighth** of the corresponding displayed ordered-pair total. This is a count of subgroups, not conjugacy classes of subgroups.

## Assumptions and scope

All scalars and matrices are in the indicated finite fields, and \(q\) is odd throughout. \(\mathrm{Sp}_{d}(q)\) is defined only for even \(d\), and the zero-dimensional trivial case is excluded. The Hermitian involution is \(a\mapsto a^q\) on \(\mathbb F_{q^2}\). Nondegenerate symmetric bilinear and quadratic forms are equivalent data in odd characteristic; \(\Delta\) is meaningful up to multiplication by a square. The two \(m\)-dimensional symmetric types are distinguished by determinant square class even when \(m\) is odd (their isometry groups then have the same order).

For explicit integer evaluation the standard order formulas are
\[
 g_j=\prod_{i=0}^{j-1}(q^j-q^i),\qquad
 u_j=q^{j(j-1)/2}\prod_{i=1}^j(q^i-(-1)^i),
\]
\[
 s_{2k}=q^{k^2}\prod_{i=1}^k(q^{2i}-1),
\]
\[
 |\mathrm O_{2k+1}(q)|=2q^{k^2}\prod_{i=1}^k(q^{2i}-1),\qquad
 |\mathrm O_{2k}^{\pm}(q)|=2q^{k(k-1)}(q^k\mp1)\prod_{i=1}^{k-1}(q^{2i}-1).
\]
In the orthogonal formula the denominator is evaluated using the isometry type of the indicated restricted form; the two types \(W_{\square},W_{\mathrm{ns}}\) need not respectively be the plus and minus types when \(m\) is even.

## Proof

**Step 1 (linear normal form).** Since the characteristic is not two, any involution \(S\) is diagonalizable with \(V=V_+\oplus V_-\), where \(V_\pm=\ker(S\mp I)\). The equation \(ST=-TS\) sends \(T(V_+)\) into \(V_-\), and conversely. As \(T\) is invertible and \(T^2=I\), it exchanges these spaces isomorphically. Therefore both have the same dimension \(m\), proving the odd-dimension obstruction. With \(\phi=T|_{V_+}:V_+\to V_-\), choose corresponding bases of \(V_+\) and \(V_-\). In those bases the pair has the canonical form
\[
 S=\begin{pmatrix}I_m&0\\0&-I_m\end{pmatrix},\qquad
 T=\begin{pmatrix}0&I_m\\I_m&0\end{pmatrix}.
\]
Conversely, these matrices are involutions and anticommute. Any invertible linear map commuting with both is \(\operatorname{diag}(h,h)\), with \(h\in\mathrm{GL}_m(q)\). This proves the general-linear orbit and its stabilizer.

**Step 2 (isometric normal form).** Suppose a nondegenerate Hermitian, alternating or symmetric form \(B\) is preserved by the two involutions. For \(x\in V_+\), \(y\in V_-\), invariance under \(S\) gives \(B(x,y)=B(Sx,Sy)=-B(x,y)\), hence \(B(x,y)=0\). Thus \(V_+\perp V_-\), and both restrictions are nondegenerate. Since \(T\) preserves \(B\), the map \(\phi\) above is an isometry. The normal form carries the form to \(B_W\oplus B_W\), for \(W=V_+\). Conversely, any isometry \((V,B)\cong(W,B_W)\perp(W,B_W)\) transports the canonical matrices to a valid pair. An isometry commuting with both has precisely the form \(\operatorname{diag}(h,h)\), where \(h\in\operatorname{Isom}(W)\). Hence simultaneously conjugate pairs are classified by the isometry types of such \(W\), and their orbit sizes are group-order/stabilizer-order ratios.

**Step 3 (forms and existence).** Nondegenerate Hermitian forms over \(\mathbb F_{q^2}\) have one isometry class in every dimension, so every \(m\ge1\) occurs and the stabilizer is \(\mathrm U_m(q)\). Nondegenerate alternating forms exist in dimension \(m\) precisely when \(m\) is even; there is one class and the stabilizer is \(\mathrm{Sp}_m(q)\). Nondegenerate symmetric forms in each positive dimension \(m\) have exactly two isometry classes indexed by their determinant square classes. For either choice the determinant of \(B_W\oplus B_W\) is a square. Conversely, all nondegenerate symmetric forms of dimension \(2m\) with square determinant are isometric, so both \(W\) types produce the given \(B\) exactly when \(\det B\) is a square. The standard even-dimensional Witt sign is \(\chi_q((-1)^m\det B)\), producing the asserted dependence on \(q\pmod4\). Orbit-stabilizer now gives the counts stated above.

**Step 4 (special groups and precise orbit splitting).** In every canonical block form, both \(S\) and \(T\) have determinant \((-1)^m\). Therefore they belong to the determinant-one subgroups exactly when \(m\) is even. For a normal subgroup \(H\unlhd G\), an orbit \(G/C_G(S,T)\) on pairs contained in \(H^2\) splits into \([G:H C_G(S,T)]\) distinct \(H\)-orbits. For \(G=\mathrm{GL}_{2m}(q)\), determinants of stabilizer elements \(\operatorname{diag}(h,h)\) are precisely \((\mathbb F_q^\times)^2\); the index is two as \(q\) is odd. For the unitary group, determinants of \(\mathrm U_m(q)\) range over all norm-one scalars, a cyclic group of order \(q+1\); stabilizer determinants are their squares, again an index-two subgroup. In the orthogonal group, a stabilizer element \(\operatorname{diag}(h,h)\) has determinant \((\det h)^2=1\). Thus its determinant image is trivial, so each orthogonal orbit splits into two special-orthogonal orbits. Equal orbit sizes follow since \(H\) is normal and of finite index two (in the orthogonal case) or the two cosets of the stabilizer-determinant image have equal size (in the linear and unitary cases).

**Step 5 (dihedral subgroups).** We have \((ST)^2=-I\), so \(ST\) has order four, \(S\) has order two and \(S(ST)S=(ST)^{-1}\). Hence \(\langle S,T\rangle\) is dihedral of order eight and its central involution is \(-I\). Every such embedded subgroup has exactly four noncentral involutions (reflections), and for each one there are exactly two reflections anticommuting with it. Thus each subgroup is counted exactly eight times among ordered pairs. Division by eight is exact.

## Verification

The standalone Python file `verify_pairs.py` independently enumerates all matrices in \(\mathrm{GL}_2(\mathbb F_3)\), \(\mathrm{GL}_2(\mathbb F_5)\), and the orthogonal groups preserving the identity form in dimension two over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\). It counts involution pairs using multiplication rather than using orbit formulas. An explicit implementation of \(\mathbb F_9\) enumerates \(\mathrm U_2(3)\), tests the Hermitian relations, verifies the anticommuting count and checks the determinant-square image has index two.

A separate enumeration of all \(130\) two-dimensional subspaces of \(\mathbb F_3^4\) finds \(90\) nondegenerate planes for a symplectic form, giving \(90\cdot24=2160\) pairs in \(\mathrm{Sp}_4(3)\). For the symmetric identity form it finds \(72\) split and \(18\) nonsplit nondegenerate planes. Their respective isometry-group orders \(4\) and \(8\) give \(72\cdot4+18\cdot8=432\) pairs in \(\mathrm O_4^+(3)\). The checker prints `ALL_EXACT_CHECKS_PASSED` when all assertions hold.

Other exact examples include \(|\mathcal A(\mathrm{GL}_2(3))|=24\), \(|\mathcal A(\mathrm U_2(3))|=24\), \(|\mathcal A(\mathrm{Sp}_4(3))|=2160\), and \(|\mathcal A(\mathrm O_4^+(3))|=432\). These finite checks are independent cross-checks, **not** the proof for general \(m\) and \(q\).

## Relationship to prior work

Taylor and Vinroot (arXiv:1708.05246v1, 17 August 2017) enumerate involutions of finite orthogonal groups and determinant-one subgroups. Their Section 4.1 counts single involutions by the types of their two eigenspaces; it does not state a rank- or type-refined simultaneous count of ordered involution pairs obeying \(ST=-TS\). De Franceschi (arXiv:2008.12651v1, 28 August 2020) classifies semisimple conjugacy and centralizer structures in all principal finite classical families; the isotypic centralizer information is prior and is used here as background. Its Section 4.2 does not give the pairwise anticommutation constraints or the determinant-one orbit splitting of their simultaneous stabilizers.

The argument also uses standard elementary classification of nondegenerate forms, well known independently of these sources. The claim is **not** that the standard group orders, normal forms for single involutions, finite-field form classification, or generic orbit-stabilizer are new. The complete coupled \(ST=-TS\) pair census, its uniform comparison across four isometry types, the special-subgroup orbit splits, and the resulting embedded-dihedral subgroup counts are the scoped results.

## Limitations

The statement is restricted to odd characteristic, actual involutive lifts and the full or determinant-one matrix groups listed above. It neither counts all commuting projective involutions nor classifies dihedral subgroup conjugacy classes, spinor-norm subgroups, or Omega subgroups. The exact orbit census is an elementary consequence of a simultaneous eigenspace-isometry argument; equivalent presentations in literature on dihedral representations and projective involutions may exist. Independent review of the novelty and general proof has not yet been performed. The computations only test the stated finite cases.

## References

1. G. K. Taylor and C. R. Vinroot, *On involutions and indicators of finite orthogonal groups*, arXiv:1708.05246v1 (2017-08-17), https://arxiv.org/html/1708.05246v1, especially Section 4.1.
2. G. De Franceschi, *Centralizers and conjugacy classes in finite classical groups*, arXiv:2008.12651v1 (2020-08-28), https://arxiv.org/html/2008.12651v1, especially Theorem 4.2.1 and Section 4.1.
