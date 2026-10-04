# Fixed-prime-factor layers of exponential-perfect numbers
## Finding
For each fixed integer \(r\ge 3\), define
\[E_r(X)=\#\{n\le X:\sigma^{(e)}(n)=2n,\ \omega(n)=r\},\]
where an exponential divisor of \(n=\prod p_i^{a_i}\) has the form \(\prod p_i^{b_i}\) with \(b_i\mid a_i\), \(\sigma^{(e)}(n)\) is the sum of all exponential divisors, and \(\omega(n)\) is the number of distinct prime factors. Then
\[E_r(X)\sim \frac{X(\log\log X)^{r-3}}{36\,(r-3)!\,\log X}.\]
Also, \(E_2(X)=1\) for every \(X\ge36\). Consequently, for fixed \(r\ge3\),
\[\frac{E_{r+1}(X)}{E_r(X)}\sim\frac{\log\log X}{r-2}.\]

## Assumptions and scope
The integer \(r\) is fixed while \(X\to\infty\). The theorem concerns ordinary exponential-perfect numbers, not exponential-unitary perfect numbers. The published facts used are: exponential-perfect numbers split uniquely into a powerful exponential-perfect core times a coprime squarefree factor; for each fixed support size there are only finitely many powerful exponential-perfect cores; and the only exponential-perfect number with exactly two distinct prime factors is \(36\). The last classification is prior work and is not claimed here.

## Proof
Write
\[n=\prod_i p_i^{a_i},\qquad c=\prod_{a_i\ge2}p_i^{a_i},\qquad m=\prod_{a_i=1}p_i.\]
Then \(m\) is squarefree, \((c,m)=1\), and the factorization \(n=cm\) is unique. The function \(\sigma^{(e)}\) is multiplicative and \(\sigma^{(e)}(m)=m\) for squarefree \(m\). Hence
\[\sigma^{(e)}(n)=m\sigma^{(e)}(c),\]
so \(n\) is exponential-perfect if and only if \(c\) is exponential-perfect. Thus every exponential-perfect integer has a unique powerful exponential-perfect core.

There is no exponential-perfect prime power. Indeed, for \(n=p^a\) with \(a=1\), one has \(\sigma^{(e)}(n)=p\). If \(a\ge2\), every proper divisor \(d\) of \(a\) satisfies \(d\le a/2\), and therefore
\[\sigma^{(e)}(p^a)=p^a+\sum_{d\mid a,\ d<a}p^d<p^a+\sum_{j=1}^{\lfloor a/2\rfloor}p^j<2p^a.\]
So every powerful exponential-perfect core has at least two distinct prime factors.

Let \(\mathcal P_t\) be the set of powerful exponential-perfect integers with exactly \(t\) distinct prime factors. Straus and Subbarao's finiteness theorem, used explicitly in Hagis's density proof, gives that each \(\mathcal P_t\) is finite. The published two-prime classification gives
\[\mathcal P_2=\{36\}.\]
For a fixed integer \(k\ge1\) and a fixed integer \(c\), let \(S_k(Y;c)\) count squarefree \(m\le Y\) with \((m,c)=1\) and \(\omega(m)=k\). Landau's fixed-\(k\) almost-prime theorem, with exclusion of the finitely many primes dividing \(c\), gives
\[S_k(Y;c)\sim\frac{Y(\log\log Y)^{k-1}}{(k-1)!\log Y}.\]
The finite prime exclusions do not change the leading term: for \(k=1\) they remove only finitely many primes, and for \(k\ge2\) the excluded multiples contribute one fewer power of \(\log\log Y\).

By the unique core decomposition, for fixed \(r\ge3\),
\[E_r(X)=\sum_{t=2}^r\ \sum_{c\in\mathcal P_t} S_{r-t}(X/c;c),\]
where \(S_0(Y;c)\) is \(1\) when \(Y\ge1\) and \(0\) otherwise. The \(t=2\) term is the single core \(c=36\), so it equals
\[S_{r-2}(X/36;36)\sim\frac{X(\log\log X)^{r-3}}{36\,(r-3)!\log X}.\]
Every term with \(t\ge3\) has at most \(r-3\) squarefree primes. Since each \(\mathcal P_t\) is finite, their total is lower by at least one power of \(\log\log X\) when \(r\ge4\), and is \(O(1)\) when \(r=3\). This proves the stated asymptotic. The case \(r=2\) is exactly the published two-prime classification. Dividing the formulas for consecutive fixed values of \(r\) gives the ratio law.

## Verification
The accompanying checker computes \(\sigma^{(e)}\) directly from prime-exponent divisors for every integer up to \(500000\). It found \(4345\) exponential-perfect integers, verified the unique powerful-core decomposition for every one, found exactly \(36\) in the two-prime layer, and verified every tested member of the family \(36p\) with \(p\) prime and \(p\notin\{2,3\}\). Its output was:

`VERIFY_OK bound=500000 eperfect=4345 decomposed=4345 omega2=[36] cores=4 base36_omega3=1639 layers=2:1,3:1642,4:2146,5:542,6:14`

This finite computation is corroborative only. It does not prove the published two-prime classification, the finiteness theorem for powerful cores, or the asymptotic use of Landau's theorem.

## Relationship to prior work
Hagis proves a positive global density for all exponential-perfect numbers by decomposing them into squarefree multiples of powerful exponential-perfect cores. The same paper explicitly invokes the earlier theorem that only finitely many powerful exponential-perfect numbers have fewer than any prescribed number of distinct prime factors. The handbook of Sándor and Crstici records the earlier theorem of Hanumanthachari, Subrahmanya Sastri, and Srinivasan that \(36\) is the only exponential-perfect number with exactly two distinct prime factors. Those are inputs here, not originality claims.

The new statement refines the global density by fixing \(\omega(n)\). The global density theorem does not determine any fixed-support-size layer. Combining the unique core decomposition, fixed-support finiteness, the two-prime classification, and the fixed-\(k\) almost-prime asymptotic yields a hierarchy in which the two-prime core \(36\) dominates every fixed layer and forces the explicit consecutive-layer ratio.

## Limitations
The theorem is for fixed \(r\); no uniformity is claimed when \(r\) grows with \(X\). No effective error term is claimed. The full 1978 primary article containing the two-prime classification was located bibliographically but not materially read during verification; the exact classification was checked in the later handbook and sequence literature and was independently corroborated only to the finite checker bound. The theorem does not classify powerful exponential-perfect cores with three or more prime factors.

## References
1. P. Hagis, Jr., “Some results concerning exponential divisors,” *International Journal of Mathematics and Mathematical Sciences* 11 (1988), 343–349. DOI: 10.1155/S0161171288000407. First published 1987-02-09.
2. J. Sándor and B. Crstici, *Handbook of Number Theory II*, Kluwer/Springer, 2004, Chapter 1, p. 52. DOI: 10.1007/1-4020-2547-5.
3. J. Hanumanthachari, V. V. Subrahmanya Sastri, and V. Srinivasan, “On e-perfect numbers,” *The Mathematics Student* 46 (1978), 71–80.
4. OEIS A054979, “e-perfect numbers,” and OEIS A054980, “Primitive e-perfect numbers.”
5. The classical fixed-\(k\) almost-prime asymptotic of Landau.
