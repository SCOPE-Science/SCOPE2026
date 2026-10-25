# Exact repair factors for two consecutive Stirling-number sequences

## Finding
Let \(S(N,k)\) denote the Stirling number of the second kind. For each integer \(k\ge 1\), put \(a^{(k)}_n=S(n+k-1,k)\) for every integer \(n\ge 1\). Define the repair factor \(F(k)\) as the smallest positive integer \(m\) for which
\[
 n\mid m\sum_{d\mid n}\mu(n/d)a^{(k)}_d\qquad\text{for all integers }n\ge1.
\]
For the two consecutive indices \(k=12\) and \(k=13\), this minimum exists and is exactly
\[
\boxed{F(12)=F(13)=13860=2^2\cdot3^2\cdot5\cdot7\cdot11.}
\]
The positivity condition for periodic-point counts also holds for both scaled sequences, so this is the exact smallest multiplier making either sequence realizable as periodic-point counts. The numerical values appeared previously as *hypothetical* repair factors; the contribution is an all-index proof, including a finite, reproducible prime-power certificate.

## Assumptions and scope
All indices are positive integers unless otherwise stated. The arithmetic function \(\mu\) is the ordinary Möbius function. Congruences are in the integers. For each prime \(p\), \(v_p(b)\) denotes its exponent in a positive integer \(b\). No assertion about \(F(k)\) for \(k\notin\{12,13\}\) is made. The basic Stirling identity is
\[
 k!a^{(k)}_n=\sum_{j=1}^k c_{k,j}j^n,\qquad c_{k,j}=(-1)^{k-j}\binom{k}{j}j^{k-1}.
\]
We use the standard Dold criterion: a nonnegative integer sequence is a periodic-point-count sequence exactly when its Möbius transform is nonnegative and divisible by its index.

## Proof
**1. Reduction to prime powers.** For an integer-valued sequence \((u_n)_{n\ge1}\), the divisibility \(n\mid\sum_{d\mid n}\mu(n/d)u_d\) for all \(n\) is equivalent to
\[
 u_{p^rt}\equiv u_{p^{r-1}t}\pmod{p^r}
\]
for every prime \(p\), integer \(r\ge1\), and integer \(t\ge1\) coprime to \(p\). The forward implication follows by Möbius inversion in the divisors of \(t\); the reverse follows by grouping the Möbius sum into differences indexed by divisors of \(t\). Apply this to \(u_n=ma^{(k)}_n\), where \(m=13860\).

For any integer \(j\ge1\), the difference \(j^{p^rt}-j^{p^{r-1}t}\) is divisible by \(p^r\). For \(p\nmid j\) this follows from Euler's theorem, and for \(p\mid j\) from the elementary valuation of the two powers (the case \(r=1\) also follows from Fermat). Consequently, use also the integral-power identity
\[
 (k-1)!a^{(k)}_n=\sum_{j=1}^k(-1)^{k-j}\binom{k-1}{j-1}j^{n+k-2}.
\]
Since \(m/(k-1)!\) is \(p\)-adically integral for every prime outside \(\{2,3,5\}\) when \(k=12\) or \(13\), the required congruence holds automatically at all such primes. This includes \(7\) and \(11\), whose factors occur in \(m\), and \(13\), which does not divide \((k-1)!\).

**2. Finite certificate at the remaining primes.** For \(p\in\{2,3,5\}\), define
\[
 h_p=v_p(k!)-v_p(m),\qquad
 Q_{j,r,t}=\frac{j^{p^rt}-j^{p^{r-1}t}}{p^r}\in\mathbb Z.
\]
For both \(k\), the respective \(h_p\) are \(8,3,1\). By the displayed Stirling identity, the entire prime-power requirement is equivalent to
\[
 \sum_{j=1}^k c_{k,j}Q_{j,r,t}\equiv0\pmod{p^{h_p}}.
 \tag{*}
\]
Set \(P_p=(p-1)p^{h_p}\) and \(R_p=h_p+3\). The certificate checks \((*)\) for \(1\le r\le R_p\) and \(1\le t\le2P_p\) with \(p\nmid t\). Its exact parameters are

| Prime \(p\) | \(h_p\) | \(P_p\) | \(R_p\) |
| --- | ---: | ---: | ---: |
| \(2\) | \(8\) | \(256\) | \(11\) |
| \(3\) | \(3\) | \(54\) | \(6\) |
| \(5\) | \(1\) | \(20\) | \(4\) |

The checker in `verify.py` computes each quotient modulo \(p^{h_p}\) using powers modulo \(p^{r+h_p}\), rather than attempting any floating-point or truncated infinite calculation. All cells pass for each of the two values of \(k\).

**3. Why the finite certificate covers all indices.** Fix one of these primes, suppress subscripts, and write \(h=h_p\), \(P=P_p\), \(R=R_p\). For \(p\nmid j\), Euler's theorem modulo \(p^{r+h}\) shows that \(Q_{j,r,t}\pmod{p^h}\) is periodic in \(t\) with period \(P\). For \(p\mid j\), that quotient is zero modulo \(p^h\) as soon as \(p^{r-1}t\ge r+h\). The numerical parameters above satisfy \(p^{r-1}(P+1)\ge r+h\) for all \(1\le r\le R\). Thus a test at every \(1\le t\le2P\), \(p\nmid t\), covers *every* positive coprime \(t\): if \(t>P\), reduce it to its representative in \((P,2P]\), where every nonunit contribution vanishes and every unit contribution agrees.

It remains to extend \(r\) beyond \(R\). For \(p\nmid j\), write \(A=j^{p^{r-1}t}\) and \(Q=Q_{j,r,t}\); the exact binomial expansion yields
\[
 Q_{j,r+1,t}=A^{p-1}Q+\sum_{i=2}^p
 \binom pi p^{ri-r-1}A^{p-i}Q^i.
\]
For \(r\ge2\), \(A^{p-1}\equiv1\pmod{p^{r-1}}\) by Euler's theorem (also valid for \(p=2\) with the exponent shown). Each term in the sum is divisible by \(p^{r-1}\); for the final \(i=p\) term this follows from \((p-1)r-1\ge r-1\). Therefore
\[
 Q_{j,r+1,t}\equiv Q_{j,r,t}\pmod{p^{r-1}}.
\]
For \(p\mid j\), both normalized quotients are zero modulo \(p^h\) once \(r\ge R\), since \(p^{r-1}\ge r+h\) for the tabulated values. As \(R-1\ge h\), every congruence checked at \(r=R\) propagates to all greater \(r\). Thus \((*)\) holds at all prime-power indices. This proves \(F(k)\mid13860\) for both indices.

**4. Sharpness.** For any \(n\ge1\), define
\[
 D_k(n)=\sum_{d\mid n}\mu(n/d)S(d+k-1,k),\qquad
 e_k(n)=\frac{n}{\gcd(n,D_k(n))}.
\]
Every repair factor is divisible by \(e_k(n)\). Exact integer evaluation gives the following five denominator witnesses for each \(k\):

| \(k\) | \(n\) giving denominator \(4\) | \(n\) giving \(9\) | \(n\) giving \(5\) | \(n\) giving \(7\) | \(n\) giving \(11\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(12\) | \(8\) | \(9\) | \(5\) | \(7\) | \(11\) |
| \(13\) | \(4\) | \(9\) | \(5\) | \(7\) | \(11\) |

Their least common multiple is \(4\cdot9\cdot5\cdot7\cdot11=13860\), so \(13860\mid F(k)\), giving equality.

**5. Positivity.** The Stirling recurrence implies \(a^{(k)}_{n+1}\ge k a^{(k)}_n\). For \(n\ge2\),
\[
 D_k(n)\ge a^{(k)}_n-\sum_{d=1}^{n-1}a^{(k)}_d
 \ge a^{(k)}_n\left(1-\frac1{k-1}\right)>0.
\]
Also \(D_k(1)=1\). Multiplication by the positive repair factor preserves positivity. The Dold criterion now supplies the claimed periodic-point interpretation.

## Verification
Run `python3 verify.py` with Python 3 and its standard library. The script computes all finite cells for both \(k\), using integer modular powers and exact binomial coefficients. It separately reconstructs Stirling numbers via their defining recurrence, computes exact Möbius transforms at the ten sharpness witnesses, and checks their reduced denominators. Expected conclusion: `ALL CERTIFICATES PASS`. The finite grid proves the infinite theorem **only in conjunction with** the period and lifting arguments in the proof; an unchecked large index is not itself tested directly.

## Relationship to prior work
Miska and Ward [1] prove the general almost-realizability bound \(F(k)\mid(k-1)!\). Section 4, Table 1, gives 13860 for \(k=12\) and \(k=13\) but explicitly labels all table entries as *hypothetical*, obtained through a finite computation. OEIS A341617 [2] reproduces those numerical candidates and separately warns that finite computations cannot prove the actual repair factors. Therefore neither the number 13860 nor its appearance twice is new as numerical data. The present result replaces these two empirical entries by universal congruence proofs and supplies a finite-to-infinite test suited to their missing high powers of \(2,3,5\).

## Limitations
The proof concerns exactly two fixed values of \(k\), not a closed formula for all repair factors. The finite verification must be accompanied by the elementary periodicity and lifting lemmas; it does not independently prove the result. Existing unpublished, unindexed, or embedded derivations could affect historical priority. No independent mathematical audit has been performed.

## References
[1] P. Miska and T. Ward, *Stirling number and periodic points*, arXiv:2102.07561v2, first public 2021-02-15, especially Theorem 7 and Section 4, https://arxiv.org/html/2102.07561v2.

[2] OEIS Foundation, *A341617: Repair factors for Stirling numbers of the second kind*, https://oeis.org/A341617, including its empirical-status notes.
