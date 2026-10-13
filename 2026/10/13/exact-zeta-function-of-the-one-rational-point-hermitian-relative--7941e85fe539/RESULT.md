# Exact zeta function of the one-rational-point Hermitian relatives

## Finding

Let \(p\) be any prime, let \(f\geq1\), put \(s=p^f\) and \(q=s^2\), and let \(\eta\in\mathbb F_q\setminus\mathbb F_s\). For the smooth plane curve
\[
 C_\eta:\quad X^{s+1}+\eta Y^{s+1}+Y^sZ+YZ^s=0
 \quad\subset\mathbb P^2_{\mathbb F_q},
\]
its zeta function over \(\mathbb F_q\) has the **exact numerator**
\[
 P_{C_\eta}(T)
 = (1+sT)^{s^2/p-s}
   \left(\sum_{j=0}^{p-1}(-sT)^j\right)^{s^2/p}.
\]
Thus \(Z(C_\eta/\mathbb F_q,T)=P_{C_\eta}(T)/((1-T)(1-qT))\). This polynomial depends only on \(s\) and \(p\), not on \(\eta\). Equivalently, for **every** integer \(n\geq1\),
\[
 \#C_\eta(\mathbb F_{q^n})=
 \begin{cases}
 q^n+1+s(-s)^n,&p\nmid n,\\
 q^n+1-s(s-1)(-s)^n,&p\mid n.
 \end{cases}
\]
The curve becomes isomorphic over \(\mathbb F_{q^p}\) to the classical Hermitian curve. For \(p\nmid n\), all point-count deviations are given by a single power \((-s)^{n+1}\), rather than the full genus contribution.

## Assumptions and scope

The characteristic \(p\) is unrestricted, including \(p=2\). The parameter \(\eta\) must lie outside \(\mathbb F_s\); the case \(\eta\in\mathbb F_s\) is Hermitian and has a different zeta numerator. The curve is smooth: the three partial derivatives of its equation are \(X^s\), \(\eta Y^s+Z^s\), and \(Y^s\), which cannot vanish simultaneously at a projective point. Its degree is \(s+1\) and genus \(g=s(s-1)/2\). We use the geometric-Frobenius convention in which the number of points equals \(q^n+1\) minus the trace on \(H^1\).

## Proof

**1. Base-field point count.** The only point on \(Y=0\) is \([0:0:1]\). For an \(\mathbb F_q\)-point with \(Y\ne0\), normalize \(Y=1\). Both \(X^{s+1}\) and \(Z^s+Z\) lie in \(\mathbb F_s\), whereas \(\eta\) does not, giving a contradiction. Thus
\[
 \#C_\eta(\mathbb F_q)=1.
\]

**2. Exact descent of a Hermitian isomorphism.** Let
\[
 H:\quad X^{s+1}+Y^sZ+YZ^s=0.
\]
Choose \(c\) in an algebraic closure with \(c^s+c=-\eta\); its existence follows since this separable polynomial has degree \(s\). Replacing \(Z\) by \(Z+cY\) turns the defining equation of \(C_\eta\) into that of \(H\). Applying the \(s\)-power map to the equation for \(c\) and subtracting gives
\[
 c^q-c=\delta:=\eta-\eta^s\ne0,
 \qquad \delta^s+\delta=0.
\]
Consequently \(c^{q^n}=c+n\delta\), so the isomorphism is defined over \(\mathbb F_{q^p}\), and the corresponding Frobenius descent automorphism of \(H\) is a choice of \(u_\delta\) or \(u_\delta^{-1}\), where
\[
 u_\delta(X,Y,Z)=(X,Y,Z+\delta Y).
\]
It is an \(\mathbb F_q\)-automorphism of \(H\) of exact order \(p\). Both choices yield the same trace and characteristic polynomial below.

**3. Frobenius on the Hermitian curve.** The norm and trace maps \(\mathbb F_q\to\mathbb F_s\) show directly that \(H\) has exactly \(s^3+1\) \(\mathbb F_q\)-points. This equals the Weil upper bound \(q+1+2gs\). Hence every eigenvalue of its Frobenius on \(H^1_{\mathrm{\acute et}}(H_{\overline{\mathbb F}_q},\mathbb Q_\ell)\) is \(-s\), for any auxiliary prime \(\ell\ne p\). We do not need to assume this operator is diagonalizable: it commutes with every \(\mathbb F_q\)-automorphism and has this sole eigenvalue on each invariant direct summand.

**4. Conjugate nontrivial powers.** For each \(a\in\mathbb F_q^\times\),
\[
 D_a(X,Y,Z)=(X,aY,a^{-s}Z)
\]
is an automorphism of \(H\), and
\[
 D_au_\delta D_a^{-1}=u_{\delta a^{-(s+1)}}.
\]
The norm map \(a\mapsto a^{s+1}\) surjects onto \(\mathbb F_s^\times\). Therefore every \(u_\delta^j\), with \(j=1,\ldots,p-1\), is conjugate to \(u_\delta\), even over \(\mathbb F_q\).

**5. Determine the entire cyclic representation.** Denote by \(U\) the induced action of \(u_\delta\) on \(H^1\), a vector space of dimension \(d=2g=s(s-1)\). From the descent in step 2, the Frobenius for \(C_\eta\) has the same trace as the product of Frobenius for \(H\) with \(U\) or \(U^{-1}\). Since Frobenius for \(H\) has sole eigenvalue \(-s\) on every \(U\)-eigenspace, and \(U\) has order \(p\), the base-field count from step 1 yields
\[
 q=\operatorname{Tr}(\mathrm{Frob}_{C_\eta}|H^1)
   =-s\operatorname{Tr}(U),
 \qquad \operatorname{Tr}(U)=-s.
\]
(The trace of \(U^{-1}\) agrees with that of \(U\) by conjugacy.) The same conjugacy gives \(\operatorname{Tr}(U^j)=-s\) for every nonzero residue \(j\bmod p\). In characteristic zero, the representation of the cyclic group of order \(p\) is semisimple. Fourier inversion of these \(p\) traces shows that the eigenvalue \(1\) occurs with multiplicity
\[
 m_0=\frac{d-s(p-1)}p=\frac{s^2}p-s,
\]
and **every nontrivial \(p\)-th root of unity** occurs with multiplicity
\[
 m_j=\frac{d+s}p=\frac{s^2}p\qquad(1\le j<p).
\]
Both are nonnegative integers because \(s\) is divisible by \(p\).

**6. Zeta numerator and every extension count.** Write \(\zeta_p\) for a primitive \(p\)-th root of unity. The eigenvalue multiset for Frobenius on \(C_\eta\) is \(-s\) with multiplicity \(m_0\), together with \(-s\zeta_p^j\) with multiplicity \(m_j\) for each \(1\le j<p\). Thus
\[
 P_{C_\eta}(T)=(1+sT)^{m_0}
   \prod_{j=1}^{p-1}(1+s\zeta_p^j T)^{m_j}
   =(1+sT)^{s^2/p-s}
     \left(\sum_{j=0}^{p-1}(-sT)^j\right)^{s^2/p}.
\]
For \(p\nmid n\), the sum of the nontrivial \(p\)-th roots raised to the \(n\)-th power equals \(-1\), giving total Frobenius trace \((-s)^n(m_0-m_j)=(-s)^{n+1}\). For \(p\mid n\), all \(p\)-th roots raised to the \(n\)-th power equal \(1\), giving trace \(s(s-1)(-s)^n\). Substitution into the Weil trace formula proves both displayed point counts for every \(n\ge1\).

## Verification

The accompanying pure-Python file `check_zeta.py` enumerates points directly over \(\mathbb F_4\), \(\mathbb F_{16}\), \(\mathbb F_9\), and \(\mathbb F_{81}\), including construction of valid \(\eta\) in the proper quadratic subfields. It returns counts \(1,9,1,109\), respectively, agreeing with the theorem for \((s,n)=(2,1),(2,2),(3,1),(3,2)\). It also checks the cyclic multiplicity and trace identities for six prime powers. Execute `python3 check_zeta.py` in the directory containing this result and the checker. These finite tests are consistency checks only; the infinite assertion follows from the six proof steps.

## Relationship to prior work

Homma and Kim (2026, WCC conference proceedings, Theorem 1.1) introduce and characterize exactly the displayed \(C_\eta\) as the class of Hermitian-relative curves with one base-field rational point. Their classification concerns rational-point and inflexion counts over the base field, not the complete zeta numerator. Their earlier paper (2024 preprint, later 2026 publication) proves geometric equivalence of Hermitian relatives and uses roots-of-unity Frobenius eigenvalues to deduce a congruence for base-field point counts (Theorem 2.3); its argument does not identify the present characteristic-\(p\) descent order or eigenvalue multiplicities. The exact cyclic descent and resulting all-extension-point formula are the additional conclusions here. General Hermitian-curve Frobenius facts and finite-group character decomposition are standard ingredients, not independent novelty claims.

## Limitations

This determines only the one-rational-point family \(\eta\notin\mathbb F_s\), not the zeta functions of all Hermitian-relative curves. It does not determine the isogeny decomposition of the Jacobian, its endomorphism algebra, or the complete moduli classification. A related 2026 projective-equivalence classification chapter could not be checked in full and may contain implicit overlap; no assertion of exhaustive bibliographic novelty or independent verification is made. The earlier paper studies general zeta eigenvalues and is explicitly recognized as an input.

## References

1. M. Homma and S. J. Kim, *Rational points and inflexions on Hermitian-relative curves*, WCC 2026 conference manuscript, dated 30 April 2026, publicly disseminated for WCC 2026 (8–12 June 2026); Theorem 1.1. https://wcc2026.inria.fr/assets/final_versions/WCC2026_paper_17.pdf
2. M. Homma and S. J. Kim, *Relatives of the Hermitian curve*, arXiv:2402.14192, initially posted 22 February 2024; Theorem 2.3 and its zeta-theoretic proof. https://arxiv.org/pdf/2402.14192
3. M. Homma and S. J. Kim, *Classification of Hermitian-Relative Curves up to Projective Equivalence*, in *Arithmetic of Finite Fields*, LNCS 16611 (2026), 95–110, DOI:10.1007/978-3-032-27574-5_7 (bibliographic comparison; full chapter not inspected).
