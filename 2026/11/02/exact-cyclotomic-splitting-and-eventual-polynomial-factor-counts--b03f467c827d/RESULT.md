# Exact cyclotomic splitting and eventual polynomial factor counts for monomial preimages

## Finding
Let \(K\) be any number field, let \(d\ge2\) be an integer, and let \(\alpha\in K\) be a root of unity of exact order \(m\ge1\). Let \(a_n(K,d,\alpha)\) be the number of monic irreducible factors of \(X^{d^n}-\alpha\) over \(K\), for \(n\ge1\). Put \(F=\mathbb Q(\alpha)=\mathbb Q(\zeta_m)\). Then
\[
a_n(K,d,\alpha)=\sum_{\substack{r\ge1\\ r/\gcd(r,d^n)=m}}[K\cap\mathbb Q(\zeta_r):F]. \tag{1}
\]
In particular, \(a_n(K,d,\alpha)\) depends on \(K\) only through its finite cyclotomic subfield \(E=K\cap\mathbb Q^{\mathrm{cyc}}\): it equals \(a_n(E,d,\alpha)\) for every \(n\).

Put \(P=\{p:p\mid d,\ p\nmid m\}\), \(s=|P|\), and \(b_p=\nu_p(d)\). Let \(H=K\cap\bigcup_{j\ge1}\mathbb Q(\zeta_{m d^j})\), a finite extension of \(F\). The factor count is **exactly a polynomial in \(n\) for all sufficiently large integers \(n\)**, of degree \(s\) and leading coefficient
\[
[H:F]\prod_{p\in P}b_p. \tag{2}
\]
In particular, when \(P\) is empty, the eventual constant factor count is exactly \([H:F]\). Moreover,
\[
\lim_{n\to\infty}\frac{a_n(K,d,\alpha)}{a_n(F,d,\alpha)}=[H:F]. \tag{3}
\]

If \(K=\mathbb Q(\zeta_M)\) with \(m\mid M\), all levels have the closed formula
\[
a_n(K,d,\alpha)=
\prod_{\substack{p\mid d\\p\mid m}}p^{\min(\nu_p(M)-\nu_p(m),\,n\nu_p(d))}
\prod_{\substack{p\mid d\\p\nmid m}}
\left[p^{\min(\nu_p(M),\,n\nu_p(d))}
+\max(0,n\nu_p(d)-\nu_p(M))\varphi(p^{\nu_p(M)})\right]. \tag{4}
\]
Here \(\varphi(1)=1\) and empty products are one.

## Assumptions and scope
A number field is a finite extension of \(\mathbb Q\). All field intersections occur in a fixed algebraic closure. The field \(\mathbb Q^{\mathrm{cyc}}\) is the union of the cyclotomic number fields. The polynomial \(X^{d^n}-\alpha\) is separable, so counting with or without multiplicities is identical. The order \(m=1\) (that is, \(\alpha=1\)) is included. There are no congruence assumptions on \(d\) or \(m\), and no Galois assumption on \(K/\mathbb Q\).

## Proof
**1. A root-order orbit formula.** Fix \(n\ge1\) and write \(D=d^n\). If \(\beta^D=\alpha\) and \(\beta\) has exact order \(r\), then \(r/\gcd(r,D)=m\). Conversely, whenever this equality holds, exactly \(\varphi(r)/\varphi(m)\) primitive roots of order \(r\) satisfy \(\beta^D=\alpha\): the power map on primitive roots maps onto primitive roots of order \(m\), and all fibers have the same size. These roots form one orbit over \(F\), as shown in Tucker--Zhu's root-order proof.

The cyclotomic field \(L_r=\mathbb Q(\zeta_r)\) is Galois over \(\mathbb Q\). Every primitive \(r\)-th root generates \(L_r\). Consequently, the group \(\operatorname{Gal}(KL_r/K)\) acts **freely** on the \(\varphi(r)/\varphi(m)\) roots in this order stratum. Every orbit has size
\[
[KL_r:K]=[L_r:K\cap L_r]
=\frac{\varphi(r)}{[K\cap L_r:\mathbb Q]}.
\]
The number of orbits, equivalently irreducible factors, in the stratum is therefore \([K\cap L_r:F]\). Summing over all admissible \(r\) proves (1). Since every \(L_r\) is cyclotomic, \(K\cap L_r=E\cap L_r\), proving the field-dependence assertion.

**2. Prime-power parametrization.** With \(D=d^n\), the admissible \(r\)'s are precisely
\[
r=m\prod_{\substack{p\mid d\\p\mid m}}p^{n b_p}
\prod_{p\in P}p^{t_p},\qquad 0\le t_p\le n b_p.
\tag{5}
\]
This parametrization is bijective, including when a prime divides \(m\) but not \(d\).

**3. Finite conductor and the eventual polynomial.** The finite abelian extension \(E/\mathbb Q\) lies in a cyclotomic field \(\mathbb Q(\zeta_C)\); choose such a positive integer \(C\) divisible by \(m\). Write \(c_p=\nu_p(C)\). The classical cyclotomic intersection identity gives
\[
E\cap\mathbb Q(\zeta_r)=E\cap\mathbb Q(\zeta_{\gcd(C,r)}). \tag{6}
\]
Choose an integer \(N\ge1\) so that \(n b_p\ge c_p\) for \(p\in P\) and \(\nu_p(m)+n b_p\ge c_p\) for each \(p\mid d\) also dividing \(m\), whenever \(n\ge N\). In formula (5), the intersection degree then depends on \(t_p\) only through the capped coordinates \(u_p=\min(t_p,c_p)\), independently of \(n\). Denote this degree by \(w(u)\), where \(0\le u_p\le c_p\).

For \(n\ge N\), partition each coordinate \(0\le t_p\le n b_p\) into its \(c_p\) values \(t_p<c_p\) and its \(n b_p-c_p+1\) values \(t_p\ge c_p\). Equation (1) becomes the **explicit finite polynomial**
\[
a_n(K,d,\alpha)=\sum_{S\subseteq P}\left(\prod_{p\in S}(n b_p-c_p+1)\right)
\sum_{\substack{0\le t_q<c_q\\q\in P\setminus S}}w(u),\quad u_p=\begin{cases}c_p,&p\in S,\\t_p,&p\notin S.\end{cases} \tag{7}
\]
A sum over an empty index family is interpreted in the standard way; in particular when \(c_q=0\), every term with \(q\notin S\) vanishes. The term \(S=P\) is the only summand of degree \(s\), and its positive coefficient is \(w((c_p)_{p\in P})\prod b_p\). Since the chosen \(N\) saturates the fixed prime exponents in (5), \(w((c_p))=[H:F]\). This proves (2) and the eventual-constant case. Tucker--Zhu show \(a_n(F,d,\alpha)=\prod_{p\in P}(n b_p+1)\); comparing leading terms yields (3), also for \(s=0\).

**4. The cyclotomic closed form.** If \(K=\mathbb Q(\zeta_M)\), then \(K\cap\mathbb Q(\zeta_r)=\mathbb Q(\zeta_{\gcd(M,r)})\). Hence the summand of (1) equals \(\varphi(\gcd(M,r))/\varphi(m)\). Substituting (5), Euler's totient multiplicativity factors the sum prime by prime. For \(p\mid m\), the local factor equals \(p^{\min(\nu_p(M)-\nu_p(m),n b_p)}\). For \(p\nmid m\), putting \(e=\nu_p(M)\) and \(L=n b_p\), the local sum is
\[
\sum_{t=0}^{L}\varphi(p^{\min(e,t)})=p^{\min(e,L)}+\max(0,L-e)\varphi(p^e).
\]
This proves (4).

**5. Two different kinds of field dependence.** For \(m=2,d=6\), the pure cubic field \(K=\mathbb Q(\sqrt[3]{2})\) has \(E=\mathbb Q\): any nontrivial abelian subfield would, by prime degree, equal \(K\), whereas this cubic field is not normal. Thus \(a_n(K,6,-1)=n+1\), exactly the rational count. In contrast, for \(K=\mathbb Q(\zeta_{24})\), formula (4) gives \(a_n(K,6,-1)=2^{\min(2,n)}(2n+1)\). For the quadratic field \(K=\mathbb Q(\sqrt{-15})\), \(m=1,d=15\), the quadratic character is supported jointly at \(3\) and \(5\); one obtains \(a_n(K,15,1)=(n+1)^2+n^2\). The latter shows that a general abelian subfield need not have a prime-by-prime product count.

## Verification
Running `python3 verify.py` with standard Python 3 independently counts Galois-group orbits of roots on small cyclotomic levels and compares them against (4): 624 distinct modulus/degree/level combinations pass. It also checks six quadratic-subfield instances, including the jointly supported quadratic character of discriminant \(-15\), five nonstandard choices of primitive target \(\alpha\), and the exact initial transients. Output:

```
VERIFY_OK independent_cyclotomic_orbits= 624 quadratic_subfield_orbits=6 nonstandard_targets=5 closed_formula=PASS transient_and_eventual_polynomial=PASS
```

These finite tests corroborate the formula; the unrestricted result follows from the field-theoretic argument above, not extrapolation from them.

## Relationship to prior work
Tucker and Zhu (2026), Theorem 2.1(iii), determine the exact count over \(F=\mathbb Q(\alpha)\), and bounds between that count and its multiple by \([K:F]\). Their proof identifies the admissible root orders. Formula (1) refines their bound to an exact arbitrary-number-field splitting formula, while (2), (3) and (7) determine the eventual polynomial and its sharp cyclotomic leading constant. Their published Theorem 2.1 does not state these exact field-intersection counts or the polynomial. Jones and Levy (2017) introduce the underlying stability framework and characterize bounded factor counts; no exact general number-field polynomial count for these root-of-unity monomial preimages was found there. The classical cyclotomic Galois and intersection identities used above are not themselves claimed as new.

## Limitations
This concerns monomial maps, root-of-unity targets, and number fields only. No analogous formula is claimed for general rational maps, non-root-of-unity targets, or positive-characteristic fields. The conductor-dependent threshold \(N\) is sufficient and need not be minimal. The derivation builds on a published root-order classification and standard cyclotomic Galois theory; an earlier implicit or unindexed use of the resulting exact polynomial remains a priority risk. The result has not undergone independent mathematical audit.

## References
1. Thomas J. Tucker and Zheng Zhu, *A Counterexample to the Eventual Stability Conjecture*, arXiv:2610.28688v1, submitted 20 October 2026, especially Theorem 2.1 and its root-order proof. https://arxiv.org/html/2610.28688v1
2. Rafe Jones and Alon Levy, *Eventually stable rational functions*, International Journal of Number Theory 13 (2017), 2299--2318, arXiv:1603.00673v2, especially Sections 1 and 3.4. https://arxiv.org/html/1603.00673v2
