# Primitive square-zero witnesses for Lie commutators over finite chain rings

## Finding
For a finite commutative chain ring \(R\) with residue field \(\mathbb F_q\) of odd order and radical length \(n\ge2\), an exact formula counts ordered pairs \((X,Y)\) in \(\mathfrak{sl}_2(R)^2\) satisfying \(X^2=0\), \(X\notin\pi M_2(R)\), and \([X,Y]=Z\), for **each individual** target \(Z\). The first operand is a primitive, square-zero nilpotent; the second operand is unrestricted.

Write \(Z=\begin{psmallmatrix}c&a\\b&-c\end{psmallmatrix}\) and let \(F_R(Z)\) denote the number of such pairs. Then
\[
F_R(0)=q^n(q^{2n}-q^{2n-2}).
\]
For nonzero \(Z\), write \(Z=\pi^s Z_0\) with \(0\le s<n\), interpreting the primitive triple \((a_0,b_0,c_0)\) **modulo** \(\pi^{n-s}\). Set \(r=n-s\), \(\delta=c_0^2+a_0b_0\) in \(R/(\pi^r)\). Then
\[
\boxed{F_R(Z)=q^n(q^n-q^{n-1})q^s N_r(\delta).}
\]
The explicit integer \(N_r\) is
\[
N_r(\delta)=\begin{cases}
q^{\lfloor r/2\rfloor},&\delta=0,\\
2q^h,&v(\delta)=2h<r\text{ and }\overline{\pi^{-2h}\delta}\in(\mathbb F_q^\times)^2,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, the number of realizations may vanish on an entire nonsplit discriminant stratum, despite the existence of unrestricted traceless commutator representations.

## Assumptions and scope
A finite commutative chain ring is a finite local principal ideal ring with unique maximal ideal \((\pi)\) and chain \(R\supsetneq(\pi)\supsetneq\cdots\supsetneq(\pi^{n-1})\supsetneq(\pi^n)=0\). Its residue field has \(q\) elements, \(|R|=q^n\), and its valuation sends zero to \(n\). Assume \(q\) odd (so \(2\) is a unit). The integer \(n\ge2\) is arbitrary. For nonzero \(Z\), \(s\) is the minimum valuation of its three coordinates; \(Z_0\) is determined modulo \(\pi^{n-s}\). The formula for \(N_r\) uses valuation within the quotient of length \(r\). Its square test is invariant under a change of uniformizer, since the extracted valuation is even. The expression \(F_R(Z)\) counts actual ordered matrix pairs, not conjugacy classes or group commutators.

## Proof
**1. Primitive nilpotent parametrization.** If \(X^2=0\) and the reduction of \(X\) modulo \(\pi\) is nonzero, then that reduction is rank-one nilpotent. Pick a vector \(v\) whose image \(Xv\) is unimodular. The ordered pair \((Xv,v)\) reduces to a basis and hence is a basis over \(R\), in which \(X\) is the standard nonzero elementary nilpotent. Thus the image and kernel of \(X\) coincide with a free rank-one direct summand \(\ell\subset R^2\). Conversely, for each \(\ell\in\mathbb P^1(R)\), an isomorphism \(R^2/\ell\to\ell\) determines a unique primitive square-zero operator. There are \(|R^\times|=q^n-q^{n-1}\) choices per line and \(|\mathbb P^1(R)|=q^n+q^{n-1}\) lines. Consequently there are \(q^{2n}-q^{2n-2}\) permitted first operands.

**2. Adjoint image and multiplicity.** With \(E=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\), \(F=\begin{psmallmatrix}0&0\\1&0\end{psmallmatrix}\), and \(H=\begin{psmallmatrix}1&0\\0&-1\end{psmallmatrix}\), the commutators are \([E,F]=H\) and \([E,H]=-2E\). Hence \(\ker(\operatorname{ad}_E)=RE\), and \(\operatorname{im}(\operatorname{ad}_E)=RE\oplus RH\), precisely the set of \(Z\) satisfying \(\operatorname{tr}(EZ)=0\). Conjugation proves for every permitted \(X\) that the kernel has \(q^n\) points and the image equals \(\{Z:\operatorname{tr}(XZ)=0\}\). Each admissible \(X\) therefore contributes exactly \(q^n\) values of \(Y\) for a target in that image.

**3. Projective quadratic.** For \(\ell=R(u_1,u_2)\), \((u_1,u_2)\) primitive, a square-zero operator with image \(\ell\) is a unit multiple, in the appropriate line-coordinate, of \(\begin{psmallmatrix}-u_1u_2&u_1^2\\-u_2^2&u_1u_2\end{psmallmatrix}\). Its trace pairing with \(Z\) vanishes exactly when
\[
bu_1^2-2cu_1u_2-au_2^2=0.
\]
Thus \(F_R(Z)=q^n(q^n-q^{n-1})\) times the number of projective zeros of this quadratic. At \(Z=0\), all \(q^n+q^{n-1}\) lines qualify, giving the asserted zero fiber. Otherwise the equation reduces modulo \(\pi^{n-s}\), and the reduction \(\mathbb P^1(R)\to\mathbb P^1(R/(\pi^{n-s}))\) has exactly \(q^s\) lifts per point.

**4. Primitive quadratic roots.** Over \(R/(\pi^r)\), the reduced quadratic is primitive and has discriminant \(4(c_0^2+a_0b_0)=4\delta\). If \(\delta\) is a unit, the nonsingular projective roots modulo \(\pi\) are zero or two according to its square class; each lifts uniquely through the chain. If \(\delta\) is nonunit, the reduction is a nonzero square of a linear form over the residue field; all roots lie in one affine chart. Completing the square over the local ring (possible because \(2\) is a unit) reduces the equation bijectively to \(t^2=\delta\) up to a unit-square factor. For \(\delta=0\), the number of roots is \(q^{\lfloor r/2\rfloor}\). For valuation \(2h<r\), a root exists exactly when the unit residue of \(\pi^{-2h}\delta\) is a square, and there are exactly \(2q^h\) roots: two simple choices modulo \(\pi^{r-2h}\) and \(q^h\) lifts each. Odd valuation gives no square. These cases exhaust the possibilities and yield \(N_r\). Multiplying by the factors from steps 2–3 proves the theorem for every finite chain ring of odd residue characteristic.

## Verification
Run `python verify_nilpotent.py` with `verify.py` in the same directory. The code independently enumerates every permitted \(X\), every \(Y\), and every target \(Z\) over \(\mathbb F_3\), \(\mathbb F_3[t]/(t^2)\), \(\mathbb F_5\), \(\mathbb F_9\), and \(\mathbb Z/9\mathbb Z\). It compares every resulting fiber against the discriminant formula, including zero, nonsquare, ramified, and nilpotent target strata. All five configurations passed. Finite enumeration checks the code and small instances, not the universal statement, which follows from the proof above.

## Relationship to prior work
Stasinski's arXiv:1211.6872 proves qualitative trace-zero commutator realizability over principal ideal rings in full matrix algebras. Stasinski's arXiv:1607.07205 supplies a stronger qualitative **traceless-factor** theorem, including regular-factor considerations. Neither result counts fibers subject to a **primitive square-zero first operand**; unrestricted surjectivity does not imply the constrained, sometimes zero, fiber formulas here. The finite-chain-ring determinant counts of Choosuwan, Jitman and Udomkavanich (arXiv:1605.06826) concern all determinant fibers. Those counts can imply *unrestricted* cross-product fibers through a linear-minor reduction, so such unrestricted fibers are explicitly **not** claimed as new. Fixing the first operand to the primitive nilpotent cone imposes a quadratic trace-orthogonality condition not captured by the determinant-count reduction. Macedo–Savage (arXiv:1607.06411) concerns invariant polynomials on truncated multicurrent algebras, rather than the present finite-ring pointwise nilpotent-witness count.

## Limitations
Only fields of odd residue characteristic and finite commutative chain rings are covered, not even-characteristic rings, arbitrary finite rings, or group commutators. The first operand must reduce to a nonzero square-zero matrix; imprimitive square-zero matrices are excluded. Priority cannot be established definitively by mathematical-record searches, and independent mathematical audit has not been performed.

## References
- A. Stasinski, *Similarity and commutators of matrices over principal ideal rings*, arXiv:1211.6872 (first posted 2012-11-29).
- T. Choosuwan, S. Jitman, P. Udomkavanich, *Determinants of Matrices over Commutative Finite Principal Ideal Rings*, arXiv:1605.06826 (2016-05-22).
- A. Stasinski, *Commutators of trace zero matrices over principal ideal rings*, arXiv:1607.07205 (2016-07-25).
- A. Macedo, A. Savage, *Invariant polynomials on truncated multicurrent algebras*, arXiv:1607.06411 (2016-07-21).
