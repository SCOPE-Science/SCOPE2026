# A four-stratum class equation for five-generator Grassmann principal units

## Finding
Let \(q\) be any odd prime power, let \(V=\mathbb F_q^5\), and set \(E=\bigwedge_{\mathbb F_q}V\). Denote the positive-degree (augmentation) ideal by \(J=\bigoplus_{i=1}^{5}\bigwedge^iV\) and its principal-unit group by \(U=1+J\). Thus \(|U|=q^{31}\). For a positive integer \(s\), write \(c_s(U)\) for the number of conjugacy classes of exactly \(s\) elements. With \(D_q=(q-1){5\brack3}_q\), the **complete class-size distribution** is

\[
\begin{aligned}
c_1(U)&=q^{16},\\
c_{q^2}(U)&=q^{14}D_q,\\
c_{q^4}(U)&=q^{12}(q^{10}-1-D_q),\\
c_{q^8}(U)&=q^{18}(q^5-1),
\end{aligned}
\]

and \(c_s(U)=0\) for all other positive \(s\). Here \({5\brack3}_q=\prod_{i=0}^{2}(q^{5-i}-1)/(q^{3-i}-1)\) is a Gaussian binomial coefficient. Each of the four displayed multiplicities is positive.

In particular, the exact number of conjugacy classes and commuting probability are respectively

\[
k(U)=q^{16}+q^{14}D_q+q^{12}(q^{10}-1-D_q)+q^{18}(q^5-1),
\]
\[
\Pr_{g,h\in U}(gh=hg)=k(U)/q^{31}.
\]

The full unit group \(E^{\times}\cong\mathbb F_q^{\times}\times U\) has the same class-size support, with every class count multiplied by \(q-1\). For \(q=3\), the four class counts for sizes \(1,9,81,6561\) are, respectively, \(43046721,11574784980,30094440948,93755758338\); their sum is \(135468030987\).

## Assumptions and scope
The result concerns the multiplicative group \(1+J\) in the unital associative exterior algebra on **exactly five** generators, not the additive exterior algebra and not its algebra-automorphism group. The field has arbitrary odd prime-power cardinality, including nonprime fields. Conjugacy means internal conjugacy in \(U\), not conjugacy under the automorphism group of \(E\). The prime characteristic is required to be odd. The class-size distribution is exact; no asymptotic approximation is involved.

## Proof
**Step 1 (central-even factorization).** Write \(J_{\mathrm{ev}}=\bigwedge^2V\oplus\bigwedge^4V\) and \(E_{\mathrm{od}}=\bigwedge^1V\oplus\bigwedge^3V\oplus\bigwedge^5V\), of dimensions \(15\) and \(16\). Exterior supercommutativity gives centrality of \(1+J_{\mathrm{ev}}\), and \(s^2=0\) for each odd \(s\). Every \(g\in U\) admits a *unique* factorization \(g=(1+c)(1+s)\) with \(c\in J_{\mathrm{ev}}\), \(s\in E_{\mathrm{od}}\): choose \(c\) as the even positive-degree part of \(g-1\), then \(s=(1+c)^{-1}(g-1-c)\), which is odd. As central even factors cancel in comparisons, \((1+s)(1+t)=(1+t)(1+s)\) holds exactly when \(2st=0\), equivalent to \(st=0\) in odd characteristic.

**Step 2 (centralizer as a wedge-kernel).** Let \(\mu_s:E_{\mathrm{od}}\longrightarrow J_{\mathrm{ev}}\) be \(\mu_s(t)=st\), and set \(r(s)=\operatorname{rank}_{\mathbb F_q}\mu_s\). From Step 1 the centralizer has \(q^{15}q^{16-r(s)}=q^{31-r(s)}\) elements. Therefore the conjugacy-class size of \((1+c)(1+s)\) is exactly \(q^{r(s)}\). Each odd \(s\) occurs with exactly \(q^{15}\) choices of the central factor.

**Step 3 (nonzero linear term).** Write \(s=s_1+s_3+s_5\) by homogeneous degree. If \(s_1\ne0\), complete \(s_1\) to a basis of \(V\) and send its first vector to \(s\), leaving the remaining four degree-one generators unchanged. Because odd exterior elements square to zero and anticommute, this assignment induces a parity-preserving algebra automorphism; its invertible linear part ensures an inverse by the nilpotent-degree filtration. The induced automorphism conjugates wedge multiplication by \(s_1\) to multiplication by \(s\) on odd elements. Multiplication by a nonzero degree-one vector has image \(e_1\wedge\bigwedge^1\langle e_2,\ldots,e_5\rangle\oplus e_1\wedge\bigwedge^3\langle e_2,\ldots,e_5\rangle\), of dimension \(4+4=8\). Hence \(r(s)=8\). There are \((q^5-1)q^{10}q=(q^5-1)q^{11}\) odd elements in this stratum.

**Step 4 (vanishing linear term).** If \(s_1=0\), then \(s=s_3+s_5\), and \(s\wedge t\) depends only on the degree-one part of \(t\) and the degree-three part \(s_3\): all other odd products have degree above five. Consequently \(r(s)=\operatorname{rank}(V\to\bigwedge^4V,\ v\mapsto s_3\wedge v)\). If \(s_3=0\), the rank is zero. If \(s_3\ne0\), choose a volume form and identify \(\bigwedge^3V\) with \(\bigwedge^2V^*\otimes\bigwedge^5V\). The associated alternating bilinear form has rank either two or four, and the wedge-multiplication map has the same rank. Rank two corresponds precisely to decomposable nonzero trivectors. Such a trivector spans \(\bigwedge^3 W\) for one unique three-dimensional subspace \(W\le V\); thus there are \(D_q=(q-1){5\brack3}_q\) choices. The remaining \(q^{10}-1-D_q\) nonzero trivectors give rank four. For every chosen \(s_3\), the degree-five term \(s_5\) is arbitrary, with \(q\) possibilities.

**Step 5 (count classes).** Multiply the numbers of odd elements in the four disjoint ranks \(0,2,4,8\) by \(q^{15}\) for central-even choices, obtaining the corresponding element multiplicities

\[
q^{16},\quad q^{16}D_q,\quad q^{16}(q^{10}-1-D_q),\quad q^{26}(q^5-1).
\]

Divide each by its conjugacy-class size \(1,q^2,q^4,q^8\), respectively. This yields the asserted class counts. Their class-size-weighted sum is \(q^{31}\), as required. The center consists precisely of the even positive-degree principal units times the top-degree odd units, so \(|Z(U)|=q^{16}\). The exact commuting probability follows from the class equation identity \(\#\{(g,h):gh=hg\}=|U|k(U)\). Finally \(E^{\times}\cong\mathbb F_q^{\times}\times U\), with its scalar factor central.

## Verification
The standalone \(verify_grassmann.py\) uses literal exterior-monomial multiplication and independent modular Gaussian elimination. Executing \(python3 verify_grassmann.py\) exhaustively enumerates all \(3^{10}=59049\) degree-three forms over \(\mathbb F_3\), giving ranks \(0,2,4\) with counts \(1,2420,56628\), as prescribed by the proof. It separately tests 180 odd-multiplication ranks, 80 actual multiplication-based group commuting conditions, and whole-group class-equation identities symbolically at field sizes \(3,5,7,9\). It terminates with `ALL_EXACT_CHECKS_PASSED`. The \(q=9\) check verifies integer formulas only, not extension-field multiplication. Finite checks corroborate but do not replace the all-odd-prime-power proof.

## Relationship to prior work
Domokos–Zubor analyze maximal commutative subalgebras and square-zero subspaces of exterior algebras. Bovdi–Leung give constructions of maximal commutative subalgebras, especially at odd generator counts. Bavula describes automorphisms, the even unit subgroup and inner automorphisms; those structural results underpin the naturality of studying \(U\), but do not state the explicit four-stratum internal conjugacy-class distribution above. Kaur–Prajapati–Prasad study simultaneous conjugacy invariants for other small-rank finite \(p\)-groups, not this exterior-algebra group. The finite-field class enumeration here uses the additional rank-two/rank-four classification of trivectors in five dimensions.

## Limitations
No classification is asserted for exterior algebras on six or more generators; higher alternating-form orbit types make that problem different. Characteristic two is explicitly excluded, since odd elements then commute and the group is abelian. The calculation does not classify group isomorphisms or irreducible characters. An equivalent unit-group class census in older literature cannot be ruled out conclusively by the inspected sources alone; independent literature verification remains advisable.

## References
1. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916 (initial posting 2014-03-12), Sections 2 and 7.
2. V. A. Bovdi and H.-H. Leung, *Maximal commutative subalgebras of a Grassmann algebra*, arXiv:1803.03457 (initial posting 2018-03-09), Sections 1–5.
3. V. V. Bavula, *The Jacobian map, the Jacobian group and the group of automorphisms of the Grassmann algebra*, arXiv:math/0703352 (initial posting 2007-03-12), Sections 1–3.
4. D. Kaur, S. K. Prajapati and A. Prasad, *Simultaneous Conjugacy Classes of Finite \(p\)-groups of rank at most five*, arXiv:2103.05234 (initial posting 2021-03-09), Sections 1–5.
