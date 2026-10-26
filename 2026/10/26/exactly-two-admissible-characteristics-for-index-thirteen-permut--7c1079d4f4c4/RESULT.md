# Exactly two admissible characteristics for index-thirteen permutation binomials

## Finding
For a prime \(p\), a positive integer \(m\), and \(q=p^m\), consider polynomials \(f(X)=X^r(X^s+a)\) over \(\mathbb F_q\), where \(r,s\geq1\) and \(a\in\mathbb F_q^\times\). Write \(g=\gcd(s,q-1)\), and let \(\mathcal P_{13}\) be the set of primes \(p\) for which some such polynomial is a permutation of some \(\mathbb F_{p^m}\) with \(g=13\). Then
\[
\boxed{\mathcal P_{13}=\{3,53\}.}
\]
This statement ranges over **every positive extension degree**, not just prime fields.

## Assumptions and scope
All fields are finite and commutative. No upper bound is imposed on \(m,r,s\). The exponent \(s\) satisfies \(\gcd(s,q-1)=13\), hence \(13\mid q-1\). We use the product, quotient, and inverse-power-sum identities of Tang and Fan [1] as published lemmas; their hypotheses are checked below. All additional finite modular exclusions are reproduced by the accompanying `verify_index13.py` using exact integer arithmetic.

## Proof
**1. Wendt reduction.** Proposition 2.2 of [1] implies that, when \(6\nmid g\), a characteristic admitting such a binomial divides
\[
W_g=\operatorname{Res}_X(X^g-1,(X+1)^g-1).
\]
The exact binomial-circulant determinant of order \(13\), computed by integer-preserving elimination, is
\[
W_{13}=487627751563388801409591
=3^6\cdot53^2\cdot79^2\cdot131^2\cdot521^2\cdot8191.
\]
All six factors are prime, so \(\mathcal P_{13}\subseteq\{3,53,79,131,521,8191\}\). This determinant and its factors are tabulated independently in [2,3]; the new assertion is which candidates are *realizable over any extension*.

**2. Two necessary inverse-power-sum conditions.** Suppose \(p\) is one of \(79,131,521,8191\) and a candidate binomial permutes \(\mathbb F_q\). Let
\[
t=(q-1)/13,\qquad u=s/13,\qquad uv\equiv1\pmod t,
\]
choose \(0\leq b<t\) with \(b\equiv rv\pmod t\), and put \(\zeta=(-a)^t\). By Lemmas 2.1 and 2.5 of [1], the map
\[
\psi(y)=y^b(y+a)^{13}\quad(y\in\mu_t)
\]
permutes the group of \(t\)-th roots of unity, and
\[
\zeta^{13}=1,\quad\zeta\ne1,\quad(\zeta-1)^{13}\in\{1,-1\}.
\]
For all four candidate primes \(p\equiv1\pmod{13}\), so every thirteenth root of unity in any extension already lies in \(\mathbb F_p\). Moreover \(t\geq(p-1)/13\geq6\) and \(p>26\), so the inverse-power-sum condition of Lemma 3.3 in [1] applies to both \(j=1\) and \(j=2\).

For any prime \(p>26\) let \(\tau=-13^{-1}\) in \(\mathbb F_p\). Define polynomials \(P_k(T,U,Y)\) through
\[
P_1=1,\qquad P_{k+1}=\bigl[(U-k)(Y-1)-kTY\bigr]P_k
+TY(Y-1)\partial_YP_k.
\]
Set \(b_j\equiv jb\pmod t\), \(0\leq b_j<t\), and \(U_j=t-b_j\). Lemma 3.3 yields the necessary equations
\[
P_{13}(\tau,U_1,\zeta)=0,
\qquad P_{26}(\tau,U_2,\zeta)=0
\quad\text{in }\mathbb F_p.
\]
Writing \(c=\lfloor2b/t\rfloor\in\{0,1\}\), the relation \(13t=q-1\equiv-1\pmod p\) gives
\[
U_2\equiv 2U_1+(1-c)13^{-1}\pmod p.
\]
Thus it suffices to check the first equation at every \(U_1\in\mathbb F_p\), and, for each root, the second equation for both values of \(c\).

**3. Exact exclusions.** The complete lists of \(\zeta\in\mathbb F_p\) satisfying the product conditions, followed by the complete root sets of \(P_{13}(\tau,U,\zeta)\) as a polynomial in \(U\), are

| \(p\) | \(\zeta\) and corresponding first-equation roots |
|---|---|
| \(79\) | \(18,22,62,65\): all empty |
| \(131\) | \(52,63,80,113\): all empty |
| \(521\) | \(101,421,422,423\): all empty |
| \(8191\) | \(2\): \(7564,7994\); \(4096\): \(840,1270\) |

For \(p=8191\), the values of \(P_{26}(\tau,2U+(1-c)13^{-1},\zeta)\) at \(c=0,1\), respectively, are

| \((\zeta,U)\) | \(c=0\) | \(c=1\) |
|---|---:|---:|
| \((2,7564)\) | 3849 | 862 |
| \((2,7994)\) | 4023 | 3293 |
| \((4096,840)\) | 6586 | 8046 |
| \((4096,1270)\) | 1724 | 7698 |

Each entry is nonzero modulo \(8191\). The verifier computes all admissible \(\zeta\), exhaustively checks **all** \(U\in\mathbb F_p\), and independently evaluates the surviving second-equation cases by the generating-function identity (8) of [1]. Hence none of \(79,131,521,8191\) belongs to \(\mathcal P_{13}\), irrespective of extension degree.

**4. Existence in characteristic \(53\).** Over \(\mathbb F_{53}\), let \(f(X)=X^3(X^{13}+2)\). Since \(\gcd(13,52)=13\), its index is \(13\). The quotient group \(\mu_4=\{1,23,30,52\}\) maps under \(y\mapsto y^3(y+2)^{13}\) to \(\{30,23,1,52\}\) in the displayed order, with no repetitions. Since \(\gcd(3,13)=1\), Lemma 2.5 of [1] proves \(f\) is a permutation (also checked directly on all \(53\) elements).

**5. Existence in characteristic \(3\).** Write \(K=\mathbb F_3[\alpha]/(\alpha^3-\alpha-1)\), a field with \(27\) elements because the cubic has no root in \(\mathbb F_3\). Direct reduction modulo the cubic gives \(\alpha^{13}=(\alpha+1)^{13}=(\alpha-1)^{13}=1\). Define \(f(X)=X(X^{13}+\alpha)\). For each nonzero \(x\in K\), \(x^{13}\in\{1,-1\}\), so \(f\) multiplies each of the two cosets of the subgroup of order \(13\) by an element of that subgroup, bijectively. Together with \(f(0)=0\), this proves permutation. Again \(\gcd(13,26)=13\). All \(27\) evaluations are reproduced by the verifier.

The Wendt reduction and four exclusions, followed by the two witnesses, prove the theorem. \(\square\)

## Verification
Run `python3 verify_index13.py` with Python 3 and no third-party packages. The verifier recomputes the exact integer determinant and prime factorization, tests all product-condition roots and all first-equation residues (19,306 evaluations), checks the eight nonzero second-equation residues and cross-validates them with an independent rational-series formula, and enumerates both finite-field witnesses. Successful execution ends with `CERTIFICATE_OK first_tests= 19306 second_tests= 8`. All computations use exact arithmetic; the extension-independent conclusion follows from the proved reduction, not from a finite sampling of extension fields.

## Relationship to prior work
Tang and Fan [1] established finite admissible-characteristic sets, computed them for indices at most \(10\), and treated index \(11\) over prime fields. It supplies the general lemmas used here but does not give \(\mathcal P_{13}\). The classical determinant sequence [2] and its factor table [3] give the candidate factors but cannot distinguish realizable primes. Fan [4] classifies a different family of binomials with exponents tied to an explicit subfield index, including a coprime-index case; that result is not an unrestricted fixed-index-thirteen characteristic classification.

## Limitations
The theorem classifies characteristics allowing *at least one* index-thirteen permutation binomial, not the permutation binomials themselves in characteristics \(3\) and \(53\). The argument uses established inverse-power-sum lemmas from [1] and a finite exact certificate; it is not an independent reproof of those lemmas. It determines existence over some extension, not existence in every extension. Independent mathematical validation has not been performed.

## References
1. Zhichao Tang and Xiang Fan, *Wendt's Determinant and Finiteness of Prime Characteristics for Permutation Binomials*, arXiv:2610.18584v1, first posted 2026-10-13, https://arxiv.org/html/2610.18584v1 .
2. OEIS A048954, *Wendt determinant of \(n\)-th circulant matrix*, https://oeis.org/A048954 .
3. Gérard P. Michon, *Factorization of Wendt's Determinant*, https://w.numericana.com/data/wendt.htm .
4. Xiang Fan, *A Complete Classification of Permutation Binomials of the Form \(X^r(X^{q-1}+a)\) over Finite Fields*, arXiv:2609.20354v1, first posted 2026-09-17, https://arxiv.org/abs/2609.20354 .
