# Projection derivations of finite-poset incidence algebras: Boolean cocycles and exact rank spectra

## Finding

Let \(P\) be any nonempty finite poset, \(k=\mathbb F_q\) any finite field, and \(A=I(P,k)\) its incidence algebra. Write \(\mathcal E(P)=\{(x,y):x<y\}\) and \(J=\operatorname{rad} A\). Define the **Boolean additive cocycles**
\[
\mathcal B(P,k)=\{\alpha:\mathcal E(P)\to\{0,1\}\subseteq k:\ \alpha(x,z)=\alpha(x,y)+\alpha(y,z)\text{ for all }x<y<z\}.
\]
Let \(w(\alpha)=|\{(x,y)\in\mathcal E(P):\alpha(x,y)=1\}|\). Extend every \(\alpha\) diagonally to the derivation \(\delta_\alpha\) by \(\delta_\alpha(E_{xx})=0\) and \(\delta_\alpha(E_{xy})=\alpha(x,y)E_{xy}\) for \(x<y\).

**Theorem.** The \(k\)-linear derivations \(D:A\to A\) with \(D^2=D\) are the disjoint \(1+J\)-conjugacy orbits of the \(\delta_\alpha\), for precisely \(\alpha\in\mathcal B(P,k)\). Every such orbit has size \(q^{w(\alpha)}\), and all its members have linear rank \(w(\alpha)\). Thus the **exact rank distribution** of idempotent derivations is
\[
\boxed{\ \sum_{\substack{D\in\operatorname{Der}_k(A)\\D^2=D}} T^{\operatorname{rank}_k D}
=\sum_{\alpha\in\mathcal B(P,k)}q^{w(\alpha)}T^{w(\alpha)}.\ }
\]
The theorem includes outer derivations. In characteristic two, \(\mathcal B(P,k)=Z^1(\Delta(P);\mathbb F_2)\), so the number of conjugacy orbits is
\[
2^{|P|-c+\beta_1(\Delta(P);\mathbb F_2)},
\]
where \(c\) denotes the number of connected components of \(\Delta(P)\), the order complex of \(P\), and \(\beta_1\) its first mod-two Betti number.

For the four-vertex height-two crown \(P=\{a,b\}<\{c,d\}\), no three-element chain exists. There are four independent strict intervals, yielding
\[
\boxed{\ (1+qT)^4\ }
\]
as the full rank polynomial in every characteristic. In characteristic two there are sixteen diagonal cocycles, eight of which represent nontrivial first cohomology, and \(81\) idempotent derivations over \(\mathbb F_2\). For a full chain with \(n\) vertices, the count is \(1+\sum_{j=1}^{n-1}\binom{n-1}{j}q^{j(n-j)}\) in characteristic two, and \(1+\sum_{j=1}^{n-1}q^{j(n-j)}\) in odd characteristic.

## Assumptions and scope

The poset is nonempty, finite and antisymmetric; it need not be connected, graded, or simply connected. The base is a field \(k\), and the counting statements require \(|k|=q<\infty\). Derivations are **ordinary associative, coefficient-linear** derivations and the equation \(D^2=D\) means composition of linear maps, not multiplication in the derivation Lie algebra. The conjugating group is \(U=1+J\) acting on derivations by \(D\mapsto\operatorname{Ad}(u)\circ D\circ\operatorname{Ad}(u)^{-1}\); equivalence is not conjugacy by all algebra automorphisms.

The incidence algebra has basis \(E_{xy}\) for \(x\le y\), with \(E_{xy}E_{uv}=\delta_{yu}E_{xv}\). Its radical \(J\) is spanned by the strict intervals. Let \(m=|\mathcal E(P)|\); then \(U\) has \(q^m\) elements.

## Proof

**1. All derivations have a unique cocycle–inner decomposition.** Let \(e_x=E_{xx}\). The idempotent identity \(D(e_x)=D(e_x)e_x+e_xD(e_x)\) shows \(D(e_x)\in J\). Likewise the Peirce identity \(E_{xy}=e_xE_{xy}e_y\) shows \(D(E_{xy})\in J\) for every strict interval; hence \(D(J)\subseteq J\). The induced derivation of \(A/J\cong k^P\) therefore exists and vanishes. Set \(X=\sum_x D(e_x)e_x\in J\). The orthogonality equations for the \(e_x\) give \([X,e_x]=D(e_x)\) for every \(x\). Consequently \(D'=D-\operatorname{ad} X\) kills all \(e_x\). By the Peirce projections \(e_xD'(E_{xy})e_y=D'(E_{xy})\), each strict interval is an eigenvector, say \(D'(E_{xy})=\alpha(x,y)E_{xy}\). The equality \(E_{xy}E_{yz}=E_{xz}\) forces \(\alpha(x,z)=\alpha(x,y)+\alpha(y,z)\). Conversely every such additive cocycle defines a derivation, so \(D=\delta_\alpha+\operatorname{ad}X\).

The decomposition is unique: if \(\operatorname{ad}X\) kills all diagonal idempotents with \(X\in J\), then every off-diagonal entry of \(X\) vanishes, whence \(X=0\). It also shows \(D(A)\subseteq J\) for every \(k\)-linear derivation.

**2. Every idempotent derivation can be diagonalized by a radical unit.** Suppose \(D^2=D\). The kernel \(B=\ker D\) is a unital subalgebra: for \(a,b\in B\), the Leibniz rule gives \(D(ab)=0\). Since \(D(A)\subseteq J\), every \(a\in A\) is congruent to \(a-D(a)\in B\) modulo \(J\). Thus \(B\to A/J\) is onto and \(B\cap J\) is a nilpotent ideal of \(B\).

The standard complete orthogonal-idempotent lifting lemma for nilpotent ideals applies in \(B\): the primitive diagonal idempotents of \(k^P\) lift to pairwise orthogonal idempotents \(f_x\in B\) with \(\sum_x f_x=1\) and \(f_x\equiv e_x\pmod J\). This lifting holds without restrictions on the field characteristic (one may lift idempotents successively through the finite filtration by powers of \(B\cap J\)). Put \(u=\sum_x f_xe_x\). It is congruent to \(1\pmod J\) and satisfies \(ue_x=f_xu\). Therefore \(u\in U\) and \(f_x=ue_xu^{-1}\).

The conjugated derivation \(D_0=\operatorname{Ad}(u)^{-1}\circ D\circ\operatorname{Ad}(u)\) annihilates every \(e_x\), hence equals \(\delta_\alpha\) for an additive cocycle \(\alpha\). Its square is diagonal on \(E_{xy}\), so \(D_0^2=D_0\) holds exactly when \(\alpha(x,y)^2=\alpha(x,y)\), i.e. every value is \(0\) or \(1\). This proves existence of the asserted representatives.

**3. No two distinct cocycles are conjugate and orbit sizes are exact.** For \(u\in U\), a direct calculation gives
\[
\operatorname{Ad}(u)\,\delta_\alpha\,\operatorname{Ad}(u)^{-1}
=\delta_\alpha+\operatorname{ad}\bigl(-\delta_\alpha(u)u^{-1}\bigr).
\]
The correction lies in \(J\). By uniqueness of the cocycle–inner decomposition, radical-unit conjugation cannot change \(\alpha\). It fixes \(\delta_\alpha\) precisely when \(\operatorname{ad}(\delta_\alpha(u)u^{-1})=0\). The center of an incidence algebra consists of diagonal functions constant on connected components of its comparability graph, so \(Z(A)\cap J=0\). The stabilizer condition is therefore \(\delta_\alpha(u)=0\). Writing \(u=1+\sum_{x<y}u_{xy}E_{xy}\), this forces \(u_{xy}=0\) on exactly the \(w(\alpha)\) intervals with \(\alpha(x,y)=1\), leaving \(q^{m-w(\alpha)}\) units. Orbit–stabilizer gives \(q^{w(\alpha)}\). The diagonal endomorphism \(\delta_\alpha\) has rank \(w(\alpha)\), preserved by conjugacy; summing its orbit contributes \(q^{w(\alpha)}T^{w(\alpha)}\).

**4. The mod-two topological formula.** In characteristic two the Boolean subset \(\{0,1\}\) is a copy of \(\mathbb F_2\), and the displayed additive condition is exactly the vanishing of the simplicial \(1\)-coboundary on every \(2\)-simplex of \(\Delta(P)\). Thus \(\mathcal B(P,k)=Z^1(\Delta(P);\mathbb F_2)\), an \(\mathbb F_2\)-vector space of dimension \(\operatorname{rank}d^0+\beta_1=|P|-c+\beta_1\). No division by two is used in the other parts of the proof.

## Verification

The standalone `check.py` reconstructs the strict-interval basis and multiplication of each incidence algebra. It enumerates every additive cocycle and every radical inner perturbation, forms the actual linear derivation matrix, computes \(D^2\) and its rank by finite-field elimination, and compares the observed rank histogram to the theorem's Boolean-cocycle sum. All twelve complete configurations pass, including the extension field \(\mathbb F_4\), the disconnected poset, and the discrete poset. The exact recorded output is `check_output.txt`; run `python3 check.py` with the Python standard library. The largest computation examines \(6,561\) candidate derivations for a four-element poset over \(\mathbb F_3\).

The finite checks are corroborative: the arbitrary-poset, arbitrary-finite-field theorem rests on the preceding algebraic proof.

## Relationship to prior work

The derivation decomposition into inner and additive-cocycle contributions is classical, notably Baclawski (1972), and is **not** claimed as new. The 2024 structural decomposition of Krylov–Tuganbaev (Theorem 4 and its finite-poset corollary) is likewise acknowledged. Cheng–Jing provide archival triangular-algebra derivation context, and cohomology of posets is independently classical. The proposed contribution is the nonlinear condition \(D^2=D\), its complete radical-unit orbit classification and exact rank-weight enumerator, including non-exact cocycles. These are not statements of the cited decompositions themselves; they require lifting diagonal idempotents inside \(\ker D\) and calculating stabilizers.

A related count of commuting diagonalizable **algebra elements** in incidence algebras does not imply this derivation classification: its elements are not derivations, and outer cocycles are not generally inner commutators. Full historical priority requires independent literature review, especially for general results on semisimple derivations or grading classifications that might imply this theorem.

## Limitations

The result counts coefficient-linear associative derivations on finite-poset incidence algebras, not arbitrary nonlinear/additive maps, general preorders, or derivations of other triangular algebras. Orbits are under radical units, not under the full automorphism group. In odd characteristic the Boolean cocycles are not generally a linear vector space, and the mod-two Betti-number orbit count is not asserted in that characteristic. No claim about nonreduced scheme structure is made. This verification is not an independent mathematical audit, and an overlooked stronger historical theorem could subsume the claimed originality.

## References

1. Kenneth Baclawski, *Automorphisms and derivations of incidence algebras*, Proceedings of the American Mathematical Society 36 (1972), 351–356, DOI:10.1090/S0002-9939-1972-0313133-8.
2. Xuehan Cheng and Wu Jing, *On Jordan Derivations of Triangular Algebras*, arXiv:0706.1942v1, publicly available 2007-06-13.
3. Brent Everitt and Paul Turner, *Cellular cohomology of posets with local coefficients*, arXiv:1406.3476v1.
4. Érica Z. Fornaroli and Mykola Khrypchenko, *Skew derivations of incidence algebras*, arXiv:2307.08439v1.
5. Piotr Krylov and Askar Tuganbaev, *Derivations of Incidence Algebras*, Mathematics 12 (2024), article 999, DOI:10.3390/math12070999.
