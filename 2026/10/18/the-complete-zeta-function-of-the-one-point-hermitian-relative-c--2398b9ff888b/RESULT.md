# The complete zeta function of the one-point Hermitian-relative curve

## Finding

Fix a prime \(p\), an integer \(r\geq 1\), and \(s=p^r\). Put \(q=s^2\), and let \(\eta\in\mathbb F_q\setminus\mathbb F_s\). For the smooth projective plane curve
\[
C_\eta:\quad X^{s+1}+\eta Y^{s+1}+Y^sZ+YZ^s=0
\]
over \(\mathbb F_q\), the Hasse--Weil zeta function \(Z(C_\eta,T)=P(C_\eta,T)/((1-T)(1-qT))\) has numerator
\[
\boxed{P(C_\eta,T)=\prod_{a\in\mathbb F_s^\times}\left(1+s\psi(a)T\right)^s
=\frac{\left(1-(-sT)^p\right)^{s^2/p}}{(1+sT)^s},}
\]
where \(\psi:\mathbb F_s\to\mathbb C^\times\) is any nontrivial additive character. The quotient on the right is an integer polynomial, of degree \(s(s-1)\). Equivalently, for **every** integer \(n\geq1\),
\[
\boxed{\#C_\eta(\mathbb F_{q^n})=s^{2n}+1-s(-s)^n\begin{cases}s-1,&p\mid n,\\-1,&p\nmid n.\end{cases}}
\]
These formulas are independent of \(\eta\). In particular, the unique-point property \(\#C_\eta(\mathbb F_q)=1\) is accompanied by an exact periodic spectrum over all extension fields. Over \(\mathbb F_{q^p}\), the curve is isomorphic to the Hermitian curve and reaches the Hasse--Weil **upper** bound for odd \(p\), or the **lower** bound for \(p=2\).

## Assumptions and scope

All fields are perfect finite fields; \(s=p^r\) is a prime power with \(r\geq1\), including characteristic two. For finite-field point counts, \(\mathbb F_{q^n}\) is the unique degree-\(n\) extension of \(\mathbb F_q\) inside an algebraic closure, with \(\eta\) viewed through the canonical inclusion. The displayed plane equation defines a smooth curve: its partial derivatives are \(X^s\), \(\eta Y^s+Z^s\), and \(Y^s\), which have no common projective zero. Its genus is \(g=s(s-1)/2\). The source classification identifies it, up to \(\mathbb F_q\)-projective equivalence, with the Hermitian-relative class having exactly one \(\mathbb F_q\)-point.

## Proof

**1. Reduction to an additive twist.** Let \(H\) denote the smooth Hermitian curve
\[
H:\quad X^{s+1}+Y^sZ+YZ^s=0.
\]
Choose \(\delta\) in an algebraic closure satisfying \(\delta^s+\delta=-\eta\). Then \([X:Y:Z]\mapsto[X:Y:Z-\delta Y]\) identifies \(C_\eta\) with \(H\), because substituting \(Z-\delta Y\) into the equation of \(H\) gives the equation of \(C_\eta\). Applying the \(s\)-power map to the defining equation of \(\delta\) and subtracting yields
\[
\delta^q-\delta=\eta-\eta^s=:b.
\]
As \(\eta\notin\mathbb F_s\), \(b\ne0\), while \(b^s+b=0\). Write \(U=\{u\in\mathbb F_q:u^s+u=0\}\), an additive group of order \(s\). On \(H\), the maps
\[
\tau_u:[X:Y:Z]\longmapsto[X:Y:Z+uY]\quad(u\in U)
\]
are automorphisms defined over \(\mathbb F_q\). The coordinate identification intertwines \(q\)-Frobenius on \(C_\eta\) with \(\tau_b\circ F_H\) on \(H\). Since \(\tau_b^p=1\), this twist becomes trivial over \(\mathbb F_{q^p}\).

**2. Scalar Frobenius spectrum on the Hermitian curve.** In the affine chart \(Y=1\), the equation of \(H\) is \(z^s+z=-x^{s+1}\). Every \(x\in\mathbb F_q\) has \(x^{s+1}\in\mathbb F_s\), and the trace map \(z\mapsto z^s+z\) is onto \(\mathbb F_s\) with fibers of size \(s\). There is one point at infinity, so
\[
\#H(\mathbb F_q)=s^3+1=q+1+2gs.
\]
By the Weil bounds and equality of the sum of the \(2g\) Frobenius eigenvalues with \(-2gs\), every eigenvalue on \(H^1_{\mathrm{\acute et}}(H_{\overline{\mathbb F}_q},\mathbb Q_\ell)\) is \(-s\), for any \(\ell\ne p\). We require only the eigenvalues, not diagonalizability.

**3. Every nontrivial translation character occurs equally often.** The invariant rational function \(x=X/Y\) induces a degree-\(s\) map \(H\to\mathbb P^1\). Its function-field extension has precisely the \(s\) translations \(\tau_u\) as Galois group. Thus \(H/U\simeq\mathbb P^1\). Over a coefficient field containing the \(p\)-th roots of unity, the \(U\)-representation on first \(\ell\)-adic cohomology is semisimple, and its invariant part is
\[
H^1(H)^U\simeq H^1(H/U)=H^1(\mathbb P^1)=0.
\]
For every \(c\in\mathbb F_s^\times\), choose \(t\in\mathbb F_q^\times\) of norm \(t^{s+1}=c\). The automorphism \(\alpha_t:[X:Y:Z]\mapsto[tX:Y:cZ]\) preserves \(H\) and satisfies \(\alpha_t\tau_u\alpha_t^{-1}=\tau_{cu}\). Since \(\mathbb F_s^\times\) acts transitively on the nontrivial characters of \(U\), all \(s-1\) nontrivial character spaces in \(H^1(H)\) have the same dimension. Their total dimension is \(2g=s(s-1)\), hence each has dimension \(s\).

**4. Twisted eigenvalues and extension counts.** The \(q\)-Frobenius \(F_H\) commutes with \(U\), as every translation is defined over \(\mathbb F_q\). On a nontrivial character space \(W_\chi\) of dimension \(s\), the operator \(\tau_b\) acts by the scalar \(\chi(b)\) and all eigenvalues of \(F_H\) are \(-s\). Consequently, all eigenvalues of the twisted Frobenius on \(W_\chi\) are \(-s\chi(b)\). As \(b\ne0\), the values \(\chi(b)\) over nontrivial \(\chi\) enumerate \(\{\psi(a):a\in\mathbb F_s^\times\}\). This proves the product formula for \(P(C_\eta,T)\). Since each \(p\)-th root of unity occurs exactly \(s/p\) times among \(\psi(a)\) with \(a\in\mathbb F_s\),
\[
\prod_{a\ne0}(1+s\psi(a)T)=\frac{(1-(-sT)^p)^{s/p}}{1+sT};
\]
raising to the \(s\)-th power yields the claimed integer polynomial. Finally, the character orthogonality identity
\[
\sum_{a\in\mathbb F_s^\times}\psi(na)=\begin{cases}s-1,&p\mid n,\\-1,&p\nmid n\end{cases}
\]
and the Weil trace formula give the count for every \(n\geq1\). This completes the proof.

## Verification

The accompanying standalone `verify.py` computes the field arithmetic as polynomial quotients over \(\mathbb F_p\), checks all nonzero elements are units, chooses a coefficient in the quadratic subfield outside the base subfield, and directly counts solutions to \(z^s+z=-x^{s+1}-\eta\) with the unique projective point at infinity. It checks \(p=2,3,5\), both \(r=1\) and \(r=2\), and extension degrees up to four. Example counts are \(\#C(\mathbb F_4)=1\), \(\#C(\mathbb F_{16})=9\) for \(s=2\); \(\#C(\mathbb F_9)=1\), \(\#C(\mathbb F_{81})=109\), \(\#C(\mathbb F_{729})=892\), and \(\#C(\mathbb F_{6561})=6805\) for \(s=3\); and \(\#C(\mathbb F_{25})=1\), \(\#C(\mathbb F_{625})=751\) for \(s=5\). These independent finite checks support, but do not replace, the proof for arbitrary \(p,r,n\).

## Relationship to prior work

Homma and Kim's earlier classification, including the public WAIFI 2026 account and the WCC 2026 paper followed by arXiv:2610.09672, supplies the distinguished one-point Hermitian-relative class and its plane equation. In particular, the one-point count and the projective equivalence of parameters are already established there. The **new claim is strictly the uniform Hasse--Weil numerator and its equivalent counts over every finite extension**, derived from the explicit unipotent Frobenius twist and the full cohomological translation-character multiplicity.

Bouw, Ho, Malmskog, Scheidler, Srinivasan, and Vincent investigate zeta functions for related Artin--Schreier curves with many automorphisms (arXiv:1410.7031, especially Theorem 1.8.4). Their displayed results concern different, untwisted equations over the relevant splitting fields and do not give this one-point Hermitian-relative spectrum. Generic twist and additive-character methods are classical: originality attaches to their complete, explicit application to this newly classified one-point family, **not** to those methods themselves.

## Limitations

No assertion is made about zeta functions of other Hermitian-relative equivalence classes, automorphism-group classification, or independent audit. One closely related 2026 projective-equivalence classification is accessible through its abstract but not its complete chapter text; a previously unindexed equivalent formula or an implicit general twist table is a remaining literature risk. The finite checker tests only small fields; the quantified result rests on the proof above. The curve's geometric supersingularity follows already from its geometric Hermitian isomorphism and is not claimed as a separate discovery.

## References

1. M. Homma and S. J. Kim, *Classification of Hermitian-Relative Curves up to Projective Equivalence*, WAIFI 2026, Lecture Notes in Computer Science 16611, pp. 95--110, first online May 31, 2026. DOI: 10.1007/978-3-032-27574-5_7.
2. M. Homma and S. J. Kim, *Rational points and inflexions on Hermitian-relative curves*, WCC 2026 extended abstract, presented June 11, 2026; https://wcc2026.inria.fr/assets/final_versions/WCC2026_paper_17.pdf ; also arXiv:2610.09672v1, October 7, 2026 (Theorem 7).
3. M. Homma and S. J. Kim, *Relatives of the Hermitian curve*, arXiv:2402.14192 (February 22, 2024).
4. I. Bouw, K. Ho, B. Malmskog, R. Scheidler, S. Srinivasan, and C. Vincent, *Zeta functions of a class of Artin--Schreier curves with many automorphisms*, arXiv:1410.7031 (Theorem 1.8.4).
