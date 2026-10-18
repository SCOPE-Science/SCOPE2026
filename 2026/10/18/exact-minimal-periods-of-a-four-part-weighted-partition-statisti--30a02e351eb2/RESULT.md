# Exact minimal periods of a four-part weighted partition statistic at moduli coprime to six

## Finding

For each integer \(n\ge0\), set
\[
a(n)=\sum_{\substack{\lambda_1\ge\lambda_2\ge\lambda_3\ge\lambda_4\ge1\\\lambda_1+\lambda_2+\lambda_3+\lambda_4=n}}
\sum_{1\le i<j\le4}\lambda_i\lambda_j.
\]
The sum is zero if no partition exists. For each integer \(m\ge2\) with \(\gcd(m,6)=1\), the least positive integer \(T\) satisfying \(a(n+T)\equiv a(n)\pmod m\) **for every \(n\ge0\)** is
\[
\boxed{T(m)=\begin{cases}12m,&5\nmid m,\\60m,&5\mid m.\end{cases}}
\]
Consequently the exact least pure periods modulo prime powers \(p^r\) for \(r\ge1\) are \(12p^r\) for primes \(p\ge7\), and \(12\cdot5^{r+1}\) for \(p=5\).

## Assumptions and scope

A partition is a weakly decreasing list of four positive integers. The weight is its second elementary symmetric polynomial (sum of all six pairwise products), and each partition is counted once. The modulus may be any integer at least two coprime to six. A pure period means periodicity from \(n=0\), not just eventual periodicity. The theorem does not specify periods when the modulus is divisible by two or three.

Write \(F(q)=\sum_{n\ge0}a(n)q^n\) in the formal power-series ring over the integers. Let
\[
\begin{aligned}
P(q)={}&6+15q+34q^2+57q^3+95q^4+121q^5+146q^6\\
&+126q^7+106q^8+72q^9+50q^{10}+25q^{11}+11q^{12},\\
N(q)={}&q^4P(q),\\
D(q)={}&(q-1)^6(q+1)^4(q^2+1)^3(q^2+q+1)^3.
\end{aligned}
\]
The denominator has constant coefficient one, degree 22, and numerator degree 16.

## Proof

**1. Exact generating function.** Every partition of the specified type has unique slack variables \(y_i\in\mathbb Z_{\ge0}\), \(1\le i\le4\), such that \(\lambda_j=1+\sum_{i=j}^4y_i\); its size is \(4+\sum_{i=1}^4i y_i\). Direct expansion gives
\[
\sum_{1\le r<s\le4}\lambda_r\lambda_s
=6+3\sum_{i=1}^4i y_i
+\sum_{1\le i<j\le4}i(j-1)y_i y_j
+\sum_{i=1}^4\binom{i}{2}y_i^2.
\]
The independent geometric sums \(\sum_{y\ge0}x^y=(1-x)^{-1}\), \(\sum_{y\ge0}yx^y=x(1-x)^{-2}\), and \(\sum_{y\ge0}y^2x^y=x(1+x)(1-x)^{-3}\) give
\[
F(q)=\frac{q^4}{\prod_{i=1}^4(1-q^i)}
\left(6+3\sum_{i=1}^4i\frac{q^i}{1-q^i}
+\sum_{1\le i<j\le4}i(j-1)\frac{q^{i+j}}{(1-q^i)(1-q^j)}
+\sum_{i=1}^4\binom{i}{2}\frac{q^i(1+q^i)}{(1-q^i)^2}\right).
\]
Clearing denominators and collecting powers, without division by any integer, gives the exact identity \(D(q)F(q)=N(q)\), with the displayed integer polynomials. Reproducible polynomial operations for this identity are in `verify.py`.

**2. Coprimality at every prime at least five.** Let \(\Phi_1=q-1\), \(\Phi_2=q+1\), \(\Phi_3=q^2+q+1\), and \(\Phi_4=q^2+1\). Division of \(P\) by these cyclotomic factors has constant remainders, respectively,
\[
864,\quad32,\quad6,\quad-12.
\]
These are all units modulo every prime \(p\ge5\). Also \(q^4\) is coprime to each cyclotomic factor because their constant terms are units. Hence \(\gcd(N,D)=1\) in \(\mathbb F_p[q]\) for all \(p\ge5\). Moreover \(N(1)=864\) is a unit modulo every power of any such prime.

**3. Existence of the periods.** Fix \(p\ge5\), \(r\ge1\), and work modulo \(p^r\). Put \(U(q)=1-q^{12}\). Since \(U\) contains each of \(\Phi_1,\Phi_2,\Phi_3,\Phi_4\) once, the polynomial \(D\) divides \(U^6\) over \(\mathbb Z[q]\). Set \(s=r\) if \(p\ge7\), and \(s=r+1\) if \(p=5\). Binomial expansion gives
\[
1-q^{12p^s}=1-(1-U)^{p^s}
=\sum_{j=1}^{p^s}(-1)^{j-1}\binom{p^s}{j}U^j.
\]
For \(1\le j\le5\), \(\binom{p^s}{j}\) is divisible by \(p^r\): if \(p\ge7\), the identity \(\binom{p^s}{j}=p^s\binom{p^s-1}{j-1}/j\) suffices; if \(p=5\), its denominator removes at most one factor of five. Terms with \(j\ge6\) are multiples of \(U^6\), hence of \(D\). Therefore in \((\mathbb Z/p^r\mathbb Z)[q]\), the polynomial \(D\) divides \(1-q^{T_p}\), where \(T_p=12p^s\).

Because \(D(0)=1\), writing \((1-q^{T_p})=D(q)Q(q)\) modulo \(p^r\) and using \(DF=N\) gives \((1-q^{T_p})F=NQ\). Here \(\deg Q\le T_p-22\), while \(\deg N=16\), so \(\deg(NQ)<T_p\). Thus coefficient comparison implies \(a(n+T_p)\equiv a(n)\pmod{p^r}\) for all \(n\ge0\).

**4. Necessity of the full period.** Let \(T\) be any positive pure period modulo \(p^r\). Then \((1-q^T)F(q)\) is a polynomial of degree less than \(T\), and so \(D\) divides \(N(1-q^T)\) modulo \(p^r\). Reducing modulo \(p\) and applying coprimality from Step 2 gives \(D\mid(1-q^T)\) over \(\mathbb F_p[q]\). Since the roots of \(\Phi_3\) and \(\Phi_4\) in an algebraic closure of \(\mathbb F_p\) have exact orders three and four for \(p\ge5\), it follows that \(12\mid T\).

Now substitute \(q=1+t\), and reduce modulo both \(p^r\) and \(t^6\). The polynomial \(D(1+t)\) is zero in this truncated ring, while \(N(1+t)\) is invertible there because its constant term is the unit \(864\). Consequently
\[
1-(1+t)^T\equiv0\pmod{(p^r,t^6)},
\]
which means \(p^r\mid\binom{T}{j}\) for every \(1\le j\le5\). The case \(j=1\) yields \(p^r\mid T\). If \(p=5\), then \(5\mid T\) and the identity
\[
\binom{T}{5}=\frac{T}{5}\binom{T-1}{4}
\]
with \(\binom{T-1}{4}\equiv1\pmod5\) yields \(\nu_5(\binom T5)=\nu_5(T)-1\); therefore \(5^{r+1}\mid T\). Thus every period is divisible by \(12p^r\) for \(p\ge7\), or \(12\cdot5^{r+1}\) for \(p=5\). Step 3 supplies these periods, proving minimality.

**5. Arbitrary moduli coprime to six.** By the Chinese remainder theorem, a positive integer is a pure period modulo \(m\) exactly when it is a period modulo every prime-power divisor of \(m\). The least one is the least common multiple of the proved prime-power periods. As all prime divisors are at least five, this lcm equals \(12m\) when \(5\nmid m\) and \(60m\) when \(5\mid m\).

## Verification

Run `python3 verify.py` with a standard Python installation. It reconstructs the exact numerator identity from the independent slack-variable rational expression using integer polynomial arithmetic; independently enumerates all four-part partitions through size 74 and compares all 75 coefficients; then checks both periodicity and lack of any proper-divisor period across ten sample moduli, including \(5\), \(7\), \(25\), \(49\), \(35\), and \(125\). The expected final output line is `VERIFIED`. These finite tests support the derived algebra, but do not themselves prove the universal result; Steps 1–5 do.

## Relationship to prior work

Ballantine, Beck, and Merca (first public preprint 2024-08-23, arXiv:2408.13346v1) introduce the same four-part statistic, conjecture a linear recurrence, and provide a conjectural table of minimal periods. Their proved Theorem 2 establishes congruences only for moduli \(2\), \(3\), and \(4\). This result proves all entries at moduli coprime to six in that table and determines every prime-power case \(p\ge5\), including the exceptional factor of five at prime five. Standard minimum-period results of Nijenhuis–Wilf and Kwong cited there concern the *unweighted* restricted partition function, not the present second elementary-symmetric weight. The reduction to a rational series and the use of binomial divisibility are classical tools; the claimed new content is the exact weighted numerator, its cyclotomic noncancellation, and the resulting complete least-period formula for this domain. No publication-priority claim is made.

## Limitations

No least-period formula is asserted for moduli divisible by two or three. The proof is specific to partitions of fixed length four weighted by their second elementary symmetric polynomial. Exact periodicity is proved from index zero. A general periodicity theorem might furnish a different route to the upper bound, and unidentified literature might contain the precise specialization; the present claim of originality is confined to inspected sources. No independent audit has been performed.

## References

1. C. Ballantine, G. Beck, M. Merca, *Partitions and elementary symmetric polynomials—an experimental approach*, arXiv:2408.13346v1, first posted 2024-08-23, https://arxiv.org/abs/2408.13346.
2. C. Ballantine, G. Beck, M. Merca, same work, *Ramanujan Journal* 66, article 34 (2025), DOI:10.1007/s11139-024-01001-6, https://link.springer.com/article/10.1007/s11139-024-01001-6.
3. A. Nijenhuis, H. S. Wilf, *Periodicities of partition functions and Stirling numbers modulo p*, *Journal of Number Theory* (1987), cited in Reference 2.
4. Y. H. H. Kwong, *Minimum periods of partition functions modulo M*, *Utilitas Mathematica* 35, 3–8 (1989), cited in Reference 2.
