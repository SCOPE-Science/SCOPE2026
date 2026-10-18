# Universal row content of strong-divisibility binomial arrays

## Finding

Let \(U_1,U_2,\ldots\) be any sequence of positive integers satisfying
\[\gcd(U_a,U_b)=U_{\gcd(a,b)}\qquad(a,b\ge1).\]
Write \(U_0!=1\), \(U_n!=\prod_{j=1}^{n}U_j\) for \(n\ge1\), and
\[B_U(n,k)=\frac{U_n!}{U_k!\,U_{n-k}!}\qquad(0\le k\le n).\]
For every integer \(n\ge2\), the interior row content has the exact form
\[
\boxed{\gcd_{1\le k<n}B_U(n,k)
=\frac{\operatorname{lcm}(U_1,\ldots,U_n)}{\operatorname{lcm}(U_1,\ldots,U_{n-1})}
=\prod_{d\mid n}U_d^{\mu(n/d)}.}
\]
The generalized binomial coefficients are integers under the stated hypothesis. The rightmost expression, although displayed as a rational product, is therefore a positive integer.

More precisely, fix a prime \(p\) and, for each \(e\ge1\), let \(r_e\) be the least positive index satisfying \(p^e\mid U_{r_e}\), when such an index exists. Set
\[
k_p=\begin{cases}
\max\{r_e: r_e<n\text{ and }r_e\mid n\},&\text{if this set is nonempty},\\
1,&\text{otherwise}.
\end{cases}
\]
Then \(1\le k_p<n\), and this explicit column achieves the prime-adic minimum:
\[
\nu_p(B_U(n,k_p))=\min_{1\le k<n}\nu_p(B_U(n,k))
=\#\{e\ge1:r_e=n\}.
\]
The final set is finite, even if some \(r_e\) never exists.

## Assumptions and scope

The sequence is indexed from \(1\), takes **strictly positive integers**, and obeys the strong-gcd identity for **every** pair of positive indices. No linear recurrence, monotonicity, growth rate, or normalization \(U_1=1\) is needed. All products and gcds in the theorem are ordinary positive integer operations. The parameter \(n\) ranges over every integer \(n\ge2\); there are no endpoint columns in the gcd. The Möbius function \(\mu\) has its standard number-theoretic meaning.

## Proof

**Step 1: prime-power ranks.** Fix \(p\). For each \(e\ge1\) put \(S_e=\{j\ge1:p^e\mid U_j\}\). If nonempty, \(S_e\) is closed under gcd by strong divisibility. Moreover, \(j\in S_e\) and \(j\mid t\) imply \(t\in S_e\), because \(U_j\mid U_t\). If \(r_e=\min S_e\), then for each \(t\in S_e\), \(\gcd(r_e,t)\in S_e\); minimality forces \(\gcd(r_e,t)=r_e\). Thus
\[S_e=\{j:r_e\mid j\}.\]
Because \(S_{e+1}\subseteq S_e\), whenever both ranks exist we have \(r_e\mid r_{e+1}\). Consequently, for every \(j\ge1\),
\[\nu_p(U_j)=\sum_{e:r_e\text{ exists}}\mathbf1_{r_e\mid j},\]
with only finitely many nonzero summands for each \(j\).

**Step 2: carry decomposition.** For any \(d\ge1\) and \(0\le k\le n\) set
\[\varepsilon_d(n,k)=\left\lfloor\frac nd\right\rfloor
-\left\lfloor\frac kd\right\rfloor
-\left\lfloor\frac{n-k}{d}\right\rfloor\in\{0,1\}.\]
Summing the prime-power-rank indicators over the factorial products yields exactly
\[\nu_p(B_U(n,k))=\sum_{e:r_e\text{ exists}}\varepsilon_{r_e}(n,k).\]
This sum is nonnegative for every prime, proving \(B_U(n,k)\) is an integer. Only ranks \(r_e\le n\) can contribute. For every interior \(k\), if \(r_e=n\), then \(\varepsilon_{r_e}(n,k)=1\). It follows that
\[\nu_p(B_U(n,k))\ge E_p(n):=\#\{e:r_e=n\}.\]

**Step 3: simultaneous removal of all other prime-power levels.** If there is at least one rank strictly below \(n\) dividing \(n\), let \(k_p\) be the largest such rank. The chain \(r_e\mid r_{e+1}\) implies that each rank not exceeding \(k_p\) divides both \(k_p\) and \(n\), so its \(\varepsilon\) is zero. Every rank exceeding \(k_p\) is a multiple of \(k_p\). Since \(k_p\mid n\), the remainder of \(n\) upon division by any rank \(r_e>k_p\) is either zero or a positive multiple of \(k_p\). Thus its remainder cannot lie strictly between zero and \(k_p\). Equivalently, \(\varepsilon_{r_e}(n,k_p)=0\) unless \(r_e=n\), when it equals one. Ranks above \(n\) make no contribution.

If there is no proper rank dividing \(n\), set \(k_p=1\). Any rank \(r_e<n\) fails to divide \(n\) and necessarily exceeds one, so \(n\bmod r_e\ge1\), whence \(\varepsilon_{r_e}(n,1)=0\). Again \(r_e=n\) contributes exactly one and \(r_e>n\) contributes zero. In either case,
\[\nu_p(B_U(n,k_p))=E_p(n).\]
Taking the minimum over interior columns and then all primes gives the first claimed equality.

**Step 4: lcm jump and Möbius form.** Let \(L_n=\operatorname{lcm}(U_1,\ldots,U_n)\). By Step 1, the exponent of \(p\) in \(L_n\) is the number of levels \(e\) with \(r_e\le n\). Hence \(\nu_p(L_n/L_{n-1})\) counts exactly the levels with \(r_e=n\), namely \(E_p(n)\). This proves the first equality prime by prime. Finally, the known strong-divisibility factorization \(U_n=\prod_{d\mid n}(L_d/L_{d-1})\), with \(L_0=1\), yields by multiplicative Möbius inversion
\[L_n/L_{n-1}=\prod_{d\mid n}U_d^{\mu(n/d)}.\]
This proves the theorem.

## Verification

An independent exact-integer verifier is provided as `verify.py`; run `python3 verify.py`. Its output is

`VERIFY_OK: ordinary 72 rows; Gaussian 3 x 45 rows; Fibonacci 75 rows; synthetic chained-rank 90 rows and 7,921 independent gcd pairs`.

The verifier computes every interior binomial coefficient from integer factorial products and its row gcd, independently computes successive lcms, and compares the two. It also tests the prime-adic minimizing-column construction for ten selected primes in four sequence families. It tests the ordinary sequence \(U_n=n\), Gaussian sequences \(U_n=(q^n-1)/(q-1)\) for \(q\in\{2,3,5\}\), Fibonacci numbers, and a non-recurrence example specified by nested prime-power rank chains. Finite tests are checks of implementation and examples, **not** an infinite proof; Steps 1–4 are the proof.

## Relationship to prior work

Nowicki's 2013 preprint *Strong divisibility and lcm-sequences* characterizes the divisor-product factors of every strong divisibility sequence as its successive lcm quotients. The factorization and Möbius expression on the right are **previously known**; the claim here is the separate, exact identification of that factor with the gcd of every non-endpoint entry in the corresponding generalized-binomial row, together with an explicit column attaining the prime-adic minimum. Bousla and Farhi (2020) prove lcm identities for whole generalized-binomial rows and a **weighted** gcd identity involving \(B_U(n,k)\operatorname{lcm}(U_1,\ldots,U_k)\); those are different operations and do not state the unweighted row-content identity. The classical binomial prime-power criterion, the Fibonacci primitive-factor sequence (OEIS A061446), and cyclotomic evaluations of Gaussian binomial row content are all unified by the stated relationship, but the underlying primitive-factor values are not new.

For example, \(U_n=n\) gives the familiar row gcd equal to \(p\) at prime powers \(n=p^a\), and one otherwise. For Fibonacci \(U_n=F_n\), the row gcd equals the previously tabulated primitive factor \(\prod_{d\mid n}F_d^{\mu(n/d)}\). For integer \(q\ge2\), \(U_n=(q^n-1)/(q-1)\) yields \(\Phi_n(q)\) for every \(n\ge2\), where \(\Phi_n\) is the cyclotomic polynomial. These are specializations, not separately claimed findings.

## Limitations

The theorem is only asserted for positive-integer strong divisibility sequences, not arbitrary integer sequences whose generalized binomial coefficients happen to be integral. The prime-specific minimizing column may depend on \(p\); no claim is made that one interior column attains the gcd simultaneously for all primes. The first two identities were proved here; the divisor-product/lcm relation is established prior work. Closely related papers by Ando and Sato (1991, 1999) were identifiable but their full texts were not accessible in this check. Their possible implicit coverage, and unlocated formulations of the row-content identity, are residual originality risks. The risk of an unlocated equivalent theorem remains open.

## References

- A. Nowicki, *Strong divisibility and lcm-sequences*, arXiv:1310.2416v1, 9 October 2013, especially Theorem 2.1 and its examples. https://arxiv.org/pdf/1310.2416
- S. A. Bousla and B. Farhi, *Identités et estimations concernant le plus petit commun multiple de suites à forte divisibilité*, *Comptes Rendus Mathématique* 358 (2020), 481–487, especially Theorem 1, Corollary 2, Proposition 6. https://doi.org/10.5802/crmath.64
- S. Ando and D. Sato, *On p-adic complementary theorems between Pascal's triangle and the modified Pascal triangle*, *Fibonacci Quarterly* 38 (2000), 194–200, especially Section 5. https://www.fq.math.ca/Scanned/38-3/ando.pdf
- S. Ando and D. Sato, *On the Proof of GCD and LCM Equalities Concerning the Generalized Binomial and Multinomial Coefficients*, *Applications of Fibonacci Numbers* 4 (1991), 9–16. https://doi.org/10.1007/978-94-011-3586-3_2 (full text not inspected).
- S. Ando and D. Sato, *On the Generalized Binomial Coefficients Defined by Strong Divisibility Sequences*, *Applications of Fibonacci Numbers* 8 (1999). https://doi.org/10.1007/978-94-011-4271-7_1 (abstract only inspected).
- S. Ando and D. Sato, *On GCD-LCM Duality Between Pascal’s Pyramid and the Modified Pascal Pyramid*, *Fibonacci Quarterly* 43 (2005), 15–21. https://doi.org/10.1080/00150517.2005.12428387 (abstract only inspected).
- R. Nagpal and A. Snowden, *The module theory of divided power algebras*, 2016 manuscript, Section 2.7–2.8, particularly Proposition 2.10 and Examples 2.14–2.16. https://websites.umich.edu/~asnowden/papers/dp-061016.pdf
- OEIS A061446, primitive factors of Fibonacci numbers. https://oeis.org/A061446
