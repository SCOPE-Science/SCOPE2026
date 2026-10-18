# Exact prime-power rank distributions for generalized Fibonacci sequences

## Finding

Fix an odd prime \(p\), an integer \(k\geq1\), and put \(q=p^k\). For every residue \(s\in\mathbb Z/q\mathbb Z\), define the generalized Fibonacci sequence by
\[
U_0(s)=0,\qquad U_1(s)=1,\qquad
U_{n+1}(s)=sU_n(s)-U_{n-1}(s)\quad(n\geq1),
\]
and its rank of apparition
\[
\rho_q(s)=\min\{n\geq1:U_n(s)\equiv0\pmod q\}.
\]
The rank always exists. Let \(\varphi\) denote Euler's totient function, let \(\nu_p(d)\) be the exponent of \(p\) in the positive integer \(d\), and put
\[
m_-={p-1\over2}p^{k-1},\qquad m_+={p+1\over2}p^{k-1},\qquad d^\circ={d\over p^{\nu_p(d)}}.
\]
Define, for every positive integer \(d\),
\[
B_{p,k}(d)=\varphi(d)\,\mathbf1_{\{d^\circ>1\}}
\left(\mathbf1_{\{d\mid m_-\}}+\mathbf1_{\{d\mid m_+\}}\right).
\]
Here \(\mathbf1\) is the indicator of a specified condition. Then the **complete exact rank distribution** is as follows.

For \(p\geq5\),
\[
\boxed{\#\{s\bmod p^k:\rho_{p^k}(s)=d\}
=B_{p,k}(d)+2p^{k-1}\mathbf1_{\{d=p^k\}}.}
\]
For the exceptional prime \(p=3\),
\[
\boxed{\#\{s\bmod3^k:\rho_{3^k}(s)=d\}
=B_{3,k}(d)+2\mathbf1_{\{d=3\}}
+\sum_{a=2}^{k}4\cdot3^{a-2}\mathbf1_{\{d=3^a\}}.}
\]
The sum is empty when \(k=1\). Every count not listed by these formulas is zero. For example, the seven nonzero counts modulo \(49\), written as \((d,\#s)\), are \((2,1),(3,2),(4,2),(14,6),(21,12),(28,12),(49,14)\).

## Assumptions and scope

The parameter \(s\) ranges over **every** residue class, including classes for which the discriminant \(s^2-4\) vanishes modulo \(p\). Neither irreducibility nor coprimality of the discriminant to \(p\) is assumed. Only odd primes are considered. This is a classification of the *first zero index* of the second-kind recurrence, not of the orbit period of a first-kind Chebyshev map. The upper bound \(\rho_{p^k}(s)\leq p^k+1\) is known, and also follows from the classification.

## Proof

**1. Polynomial identities.** Introduce the companion trace sequence \(V_0(s)=2\), \(V_1(s)=s\), \(V_{n+1}(s)=sV_n(s)-V_{n-1}(s)\). For a formal invertible \(z\) with \(s=z+z^{-1}\), the Laurent identities
\[
U_n(s)={z^n-z^{-n}\over z-z^{-1}},\qquad V_n(s)=z^n+z^{-n}
\]
are identities after cross-multiplication and hence yield polynomial identities over \(\mathbb Z[s]\). In particular, for positive \(a,b\),
\[
U_{ab}(s)=U_a(s)U_b(V_a(s)),\qquad V_{ab}(s)=V_b(V_a(s)). \tag{1}
\]
If \(t\equiv2\epsilon\pmod p\) with \(\epsilon=\pm1\), the recurrence gives
\[
U_n(t)\equiv\epsilon^{n-1}n\pmod p. \tag{2}
\]

**2. Nonsingular parameters.** Suppose \(p\nmid s^2-4\). In the split case the roots \(z,z^{-1}\) of \(X^2-sX+1\) lie in \(\mathbb Z/p^k\mathbb Z\); in the nonsplit case they lie in its unramified quadratic extension and have norm one. Hensel lifting applies because the roots are distinct modulo \(p\). In either case \(z-z^{-1}\) is a unit, so the first identity of step 1 gives
\[
\rho_{p^k}(s)=\operatorname{ord}(z^2). \tag{3}
\]
The possible root groups are respectively cyclic of orders \((p-1)p^{k-1}\) and \((p+1)p^{k-1}\). Their prime-to-\(p\) parts come from the finite-field unit or norm-one group; their principal-unit parts are cyclic of order \(p^{k-1}\) by the odd-prime logarithm, also in the norm-one subgroup. Squaring maps each group onto a cyclic subgroup of respective orders \(m_-\) and \(m_+\). In a cyclic group, precisely \(\varphi(d)\) elements have order \(d\) if \(d\) divides the group order, and none otherwise.

A root \(z\) is singular modulo \(p\) precisely when \(z\equiv\pm1\), equivalently when the prime-to-\(p\) part of \(\operatorname{ord}(z^2)\) equals \(1\). Thus the nonsingular roots are exactly those with \(d^\circ>1\). Each admissible pair of roots \(z,z^{-1}\) maps to one trace \(s\). The squaring map has a kernel of size two, so its two preimages per squared root balance the inversion quotient. Equivalently, among all roots with squared-root order \(d\) there are \(2\varphi(d)\) elements, which give exactly \(\varphi(d)\) traces. The two cases are disjoint because the discriminant has opposite quadratic characters. This proves the contribution \(B_{p,k}(d)\).

**3. Singular parameters for \(p\geq5\).** Write \(s\equiv2\epsilon\pmod p\). Polynomial evaluation yields
\[
U_p(2\epsilon)=p,\qquad
U'_p(2\epsilon)=\epsilon^{p-2}{p(p^2-1)\over6},\qquad
V_p(2\epsilon)=2\epsilon,\qquad V'_p(2\epsilon)=p^2.
\]
For \(p\geq5\), Taylor expansion at \(2\epsilon\) shows that every \(t\equiv2\epsilon\pmod p\) satisfies
\[
U_p(t)\equiv p\pmod{p^2},\qquad
V_p(t)\equiv2\epsilon\pmod{p^2}. \tag{4}
\]
Repeated application of (1) and (4) gives \(\nu_p(U_{p^j}(s))=j\) for all \(j\geq1\). If \(n=p^jm\) with \(p\nmid m\), equation (1), followed by (2), says the extra factor \(U_m(V_{p^j}(s))\) is a unit. Therefore
\[
\nu_p(U_n(s))=\nu_p(n),\qquad\rho_{p^k}(s)=p^k.
\]
There are exactly \(2p^{k-1}\) singular traces modulo \(p^k\), which yields the stated extra term.

**4. Singular parameters for \(p=3\).** For \(s\equiv\pm2\pmod3\) put \(e=\nu_3(s^2-1)\), interpreting \(e=\infty\) when \(s=\pm1\) exactly. Here \(U_3(s)=s^2-1\) and \(V_3(s)=s^3-3s\). If \(s\equiv\epsilon\pmod3\), then \(V_3(s)\equiv-2\epsilon\pmod9\); if \(t\equiv\pm2\pmod9\), then \(V_3(t)\equiv t\pmod9\) and \(U_3(t)\equiv3\pmod9\). Hence equation (1) implies
\[
\nu_3(U_{3^j}(s))=e+j-1\quad(j\geq1),
\qquad \nu_3(U_{3^jm}(s))=e+j-1\quad(3\nmid m).
\]
For \(j=0\), equation (2) shows that no index prime to three vanishes. Consequently
\[
\rho_{3^k}(s)=3^{\max\{1,k-e+1\}},
\]
where for \(e\geq k\) (including infinity) the exponent is interpreted as \(1\). Exactly two singular traces satisfy \(e\geq k\), namely \(s\equiv\pm1\pmod{3^k}\). For each \(1\leq j<k\), exactly \(4\cdot3^{k-j-1}\) traces have \(e=j\), giving rank \(3^{k-j+1}\). Relabeling by \(a=k-j+1\) yields the exceptional distribution above.

Steps 2–4 exhaust the \(p^k\) parameter classes and prove both formulas for every odd prime and every positive exponent. \(\square\)

## Verification

Run `python3 verify.py` in the directory containing this document. The script independently enumerates first zero indices by direct modular recurrence for every parameter in 25 prime-power rings of size at most 1300, including characteristic three through \(3^6\). It compares all exact rank multiplicities against the closed formulas; a successful run prints `VERIFY_OK rings=25 parameters=4815`. This finite computation is supplementary: the universally quantified claim is proved in the preceding section, not inferred from the tests.

## Relationship to prior work

Park, *Arithmetic properties of generalized Fibonacci sequences* (arXiv:1407.8086v1, 2014), Theorem 19, treats the eigenvalue-order description for prime moduli and on page 15 explicitly proposes relating the rank modulo prime powers to the parameter. The formulas above address that question for the fixed second parameter \(-1\), with an explicit treatment of discriminant-zero classes. Amdeberhan–Chen–Moll–Sagan (arXiv:1306.6511) introduce related polynomial and valuation questions. Gassert (arXiv:1209.4396) analyzes first-kind Chebyshev dynamics over finite fields. Panraksa–Tangboonduangjit (arXiv:2605.04417) count fixed and periodic points of first-kind Chebyshev maps modulo odd prime powers, using related split/nonsplit units, but study a different orbit invariant. The present rank distribution is an evaluated first-zero classification, not an assertion that these established group-theoretic tools are new.

## Limitations

The theorem does not address the prime \(2\), the second recurrence parameter other than \(-1\), or the complete periods of the companion matrix. The relation of the exact first-zero classification to any unpublished or unindexed general root-count theorem remains to be evaluated independently. This document reports a mathematical argument and finite checker, not an independent audit.

## References

1. S. Park, *Arithmetic properties of generalized Fibonacci sequences*, arXiv:1407.8086v1 (first posted 2014-07-30), especially Theorem 19 and the question following Theorem 21.
2. T. Amdeberhan, X. Chen, V. H. Moll and B. E. Sagan, *Generalized Fibonacci polynomials and Fibonomial coefficients*, arXiv:1306.6511 (2013).
3. T. Alden Gassert, *Chebyshev action on finite fields*, arXiv:1209.4396 (2012).
4. C. Panraksa and A. Tangboonduangjit, *Fixed-point lifting and ghost periodic points for Chebyshev polynomials modulo odd prime powers*, arXiv:2605.04417 (2026), Sections 2–5.
