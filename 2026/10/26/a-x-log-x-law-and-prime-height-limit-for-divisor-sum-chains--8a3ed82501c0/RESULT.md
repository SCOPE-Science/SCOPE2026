# A \(X/\log X\) law and prime-height limit for divisor-sum chains

## Finding
Let \(\sigma\) denote the sum-of-divisors function. For \(n\ge 1\), let \(S(n)=\{\sigma(d):d\mid n\}\), ordered by divisibility, and let \(a(n)\) be its antichain width. Define
\[
F(X)=\#\{pq\le X: p<q\text{ primes and }a(pq)=1\}.
\]
Then
\[
F(X)\sim \mathcal K\,\frac{X}{\log X},\qquad
\mathcal K=\sum_{p\text{ prime}}\frac{1}{p\varphi(p+1)}\in(0,\infty).
\]
Here \(\varphi\) is Euler's totient. For a uniformly selected qualifying semiprime \(N_X=P_XQ_X\le X\), with \(P_X<Q_X\), the pair \((P_X,N_X/X)\) converges jointly in law to independent random variables \((P,U)\), where \(U\) is uniform on \([0,1]\) and
\[
\Pr(P=p)=\frac{1}{\mathcal K p\varphi(p+1)}
\quad\text{for each prime }p.
\]
Equivalently, for each prime \(p\) and each \(0<t\le1\),
\[
\#\{q>p\text{ prime}:pq\le tX,\ a(pq)=1\}
\sim\frac{tX}{p\varphi(p+1)\log X}.
\]
In particular, among all squarefree semiprimes at most \(X\), the proportion with \(a(n)=1\) is asymptotic to \(\mathcal K/\log\log X\). In contrast to unrestricted semiprimes, the least prime factor of the conditioned population stays tight as \(X\to\infty\).

## Assumptions and scope
The variable \(X\) tends to infinity through positive real values. The integer \(n=pq\) has two distinct prime factors, ordered as \(p<q\). The constant \(\mathcal K\) is an absolutely convergent prime series. The claimed prime-factor distribution concerns the discrete topology on primes and the height variable \(n/X\) in \([0,1]\). It makes no assertion about semiprimes with repeated prime factors or about widths other than one.

## Proof
For \(p<q\),
\[
S(pq)=\{1,p+1,q+1,(p+1)(q+1)\}.
\]
The extremal elements divide or are divisible by each of the other elements. As \(p+1<q+1\), the two middle elements are comparable precisely when \(p+1\mid q+1\). Therefore
\[
a(pq)=1\quad\Longleftrightarrow\quad q\equiv-1\pmod{p+1}.
\]
This equivalence is already in Huber's Proposition 2.6; the theorem here concerns its quantitative and probabilistic consequences.

Fix a prime \(p\), and write \(F_p(X)\) for the number of admissible \(q>p\) with \(pq\le X\). For \(X\ge p^2\), the prime \(p\) itself lies in the residue class \(-1\pmod{p+1}\), so
\[
F_p(X)=\pi(X/p;p+1,-1)-1.
\]
Because \(\gcd(p+1,-1)=1\), the prime number theorem in fixed arithmetic progressions yields
\[
F_p(X)\sim \frac{X}{p\varphi(p+1)\log X}
\]
for each fixed \(p\). The same argument applied to \(tX\), with fixed \(t>0\), gives \(F_p(tX)\sim tX/[p\varphi(p+1)\log X]\).

To justify summation over \(p\), divide at \(X^{1/3}\). For \(p\le X^{1/3}\), Brun–Titchmarsh bounds primes in this progression by
\[
F_p(X)\le \frac{2X/p}{\varphi(p+1)\log((X/p)/(p+1))}
\le \frac{7X}{p\varphi(p+1)\log X}
\]
for all sufficiently large \(X\); the constant \(7\) is inessential. For \(X^{1/3}<p\le\sqrt X\), every permitted \(q>p\) has the form \(q=p+j(p+1)\) with an integer \(j\ge1\), so
\[
F_p(X)\le \frac{X}{p(p+1)},\qquad
\sum_{X^{1/3}<p\le\sqrt X}F_p(X)=O(X^{2/3}).
\]
Finally, the elementary bound \(\varphi(m)\ge\sqrt{m/2}\) implies
\[
0<\mathcal K=\sum_p\frac1{p\varphi(p+1)}<\infty.
\]
For fixed \(B\), the finite sum over primes \(p\le B\) has the required main term. The two tail bounds imply
\[
\limsup_{X\to\infty}\frac{\log X}{X}
\sum_{p>B}F_p(X)
\le7\sum_{p>B}\frac1{p\varphi(p+1)}\xrightarrow[B\to\infty]{}0.
\]
Thus \(F(X)\sim\mathcal K X/\log X\).

Dividing the fixed-prime formula for \(F_p(tX)\) by \(F(X)\) gives, for each fixed prime \(p\) and \(0\le t\le1\),
\[
\Pr(P_X=p,\ N_X/X\le t)\longrightarrow
\frac{t}{\mathcal K p\varphi(p+1)}.
\]
The masses on the right sum to one over all primes. The tail estimates supply tightness of \(P_X\), so these rectangle probabilities imply joint weak convergence and independence of the discrete prime limit from the uniform height limit. Landau's semiprime counting formula (the squarefree case of two prime factors) gives
\[
\#\{pq\le X:p<q\text{ primes}\}\sim\frac{X\log\log X}{\log X},
\]
and division yields the final relative proportion. For any fixed \(B\), ordinary semiprimes with least prime factor \(\le B\) have count \(O_B(X/\log X)\), hence their proportion tends to zero; this proves the asserted contrast in least-prime behavior.

## Verification
The included standard-library script `verify.py` checks the poset-width equivalence against direct pairwise divisibility of all divisor-sum values for every prime pair with product at most \(10000\). It independently compares direct prime-pair enumeration with congruence enumeration at bounds \(100\), \(1000\), and \(10000\), and reports the count and scaled count through \(10^7\), together with the partial prime sum for \(p<100000\). Execution: `python3 verify.py`. Its expected terminator is `VERIFY_OK`. These finite experiments are consistency checks only; infinite asymptotics follow from the proof above.

## Relationship to prior work
Huber (2026), Proposition 2.6, proves the fixed-semiprime chain criterion \(p+1\mid q+1\), and investigates possible widths and their realizability. The present claim neither reproves that criterion as new nor strengthens his general width-spectrum theorem. It instead counts its semiprime realizations and identifies a joint limiting law for least prime factor and normalized height. Koukoulopoulos (2009) studies existence and distribution of divisors of shifted primes in intervals, using prime-distribution methods; his theorems do not state the particular weighted semiprime chain count or joint law. General fixed-modulus prime distribution and Brun–Titchmarsh supply the analytic ingredients.

## Limitations
The error is \(o(X/\log X)\), with no effective explicit rate or uniformity for varying prime thresholds claimed. The normalization is for squarefree semiprimes only, not arbitrary integers or general divisor-sum posets. The calculation is based on classical prime distribution theorems and may be implicitly derivable from an earlier general shifted-prime counting result; independent priority review is not supplied. The numerical partial sum is not a rigorously rounded value of the infinite constant.

## References
- Felix Huber, *Antichains among Divisor Sums of Divisors*, arXiv:2610.02264, first public version October 1, 2026, especially Proposition 2.6 and Sections 3 and 7. https://arxiv.org/abs/2610.02264
- Dimitris Koukoulopoulos, *Divisors of shifted primes*, arXiv:0905.0163, first public version May 1, 2009, Sections 1–4. https://arxiv.org/abs/0905.0163
- The prime number theorem in arithmetic progressions, Brun–Titchmarsh inequality, and Landau's fixed-factor semiprime asymptotic, used in their standard forms.
