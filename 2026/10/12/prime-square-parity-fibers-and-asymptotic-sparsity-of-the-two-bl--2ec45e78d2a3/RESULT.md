# Prime-square parity fibers and asymptotic sparsity of the two-block odd partition function

## Finding
Let \(a(n)\) be the signed number of partitions of the positive integer \(n\) into exactly two distinct part sizes, each appearing an odd number of times: the representation \(n=(2u+1)x+(2v+1)y\), where \(1\le x<y\) and \(u,v\ge0\), receives sign \((-1)^{u+v}\). For every \(n\ge1\), write uniquely \(n=2^t m\), where \(t\ge0\) and \(m\) is odd. Let \(\chi_8(s)\) denote the real character of conductor \(8\), equal to \(+1\) when odd \(s\equiv1,7\pmod8\), and to \(-1\) when \(s\equiv3,5\pmod8\).

**Exact parity classification.** If \(m=s^2\) is a square, then
\[
a(n)\equiv1\pmod2\quad\Longleftrightarrow\quad
\begin{cases}
\chi_8(s)=-1,&t=0\text{ or }1,\\
\chi_8(s)=+1,&t\ge2.
\end{cases}
\]
If \(m\) is not a square, then
\[
a(n)\equiv1\pmod2
\quad\Longleftrightarrow\quad
m=p^{4j+1}r^2,
\]
for some integer \(j\ge0\), odd prime \(p\equiv3\text{ or }5\pmod8\), and positive odd \(r\) satisfying \(p\nmid r\). The prime \(p\) and integer \(j\) are then unique, and this nonsquare criterion does not depend on \(t\).

**Prime-scale support.** In particular, the counting function for odd coefficients has the exact leading asymptotic
\[
\#\{1\le n\le X:\ a(n)\equiv1\pmod2\}
\sim\frac{\pi^2}{8}\frac{X}{\log X}
\qquad(X\to\infty).
\]
Thus the parity-one coefficients have natural density zero but occur on a scale comparable to the primes.

## Assumptions and scope
The argument applies to all positive integers \(n\), with no unproved conjecture. It invokes the exact arithmetic identity for \(a(n)\) established in Merca's paper arXiv:2609.33770v1, elementary multiplicativity of divisor sums, and the classical prime number theorem in reduced residue classes modulo \(8\). The formula is a parity theorem and an asymptotic for the number of odd coefficients, not a claim about their exact size or sign. The source was publicly posted on 2026-09-27 (UTC); its primary MSC is 11P81.

## Proof
**1. Exact coefficient formula.** Write \(\sigma(n)=\sum_{d\mid n}d\), and \(\lambda(n)=\sum_{d\mid n}\chi_4(d)\), where \(\chi_4\) is the nonprincipal character modulo \(4\) and \(\sigma(x)=0\) if \(x\) is not a positive integer. Merca's Theorem 1.1 gives, for every \(n\ge1\),
\[
a(n)=\frac{\sigma(n)-\lambda(n)}4-\frac{\sigma(n/2)}2+\sigma(n/4).
\tag{1}
\]
For odd \(m\), this becomes \(4a(m)=\sigma(m)-\lambda(m)\). It also implies, by inserting the divisor sums of \(2^t m\),
\[
a(2m)=a(m),\qquad
a(2^t m)=a(m)+(2^{t-1}-1)\sigma(m)\quad(t\ge2).
\tag{2}
\]
This identity is also stated in the later arXiv:2610.05020v1; here it is obtained directly from (1).

**2. The key prime-power congruence.** For every odd prime \(p\) and integer \(e\ge0\),
\[
\sigma(p^e)-\lambda(p^e)
\equiv4\,\mathbf{1}_{p\equiv3,5\ (\mathrm{mod}\ 8)}
\left\lceil\frac e2\right\rceil\pmod8.
\tag{3}
\]
Indeed, for \(p\equiv1\pmod4\), \(\lambda(p^e)=e+1\). If \(p\equiv1\pmod8\), each \(p^i\equiv1\pmod8\); if \(p\equiv5\pmod8\), the terms \(p^i\) alternate between \(1\) and \(5\) modulo \(8\), and exactly \(\lceil e/2\rceil\) of the \(e+1\) terms are \(5\). For \(p\equiv3\pmod4\), \(\lambda(p^e)=1\) when \(e\) is even and \(0\) when \(e\) is odd. When \(p\equiv3\pmod8\), paired powers are \(1,3\) modulo \(8\), giving difference \(4\lceil e/2\rceil\); when \(p\equiv7\pmod8\), powers alternate \(1,7\) and the difference vanishes modulo \(8\). This covers all odd primes, including \(e=0\).

**3. Multiplication modulo eight.** Let \(m=\prod_{p\mid m}p^{e_p}\) be odd. Since both \(\sigma\) and \(\lambda\) are multiplicative and (3) makes each local difference divisible by \(4\), expanding the product and discarding products of two local differences (multiples of \(16\)) gives
\[
a(m)\equiv
\sum_{p\mid m}
\mathbf{1}_{p\equiv3,5\ (\mathrm{mod}\ 8)}
\left\lceil\frac{e_p}{2}\right\rceil
\prod_{\substack{q\mid m\\q\ne p}}\lambda(q^{e_q})
\pmod2.
\tag{4}
\]
For an odd prime \(q\), \(\lambda(q^f)\) is odd if and only if \(f\) is even. Consequently, if two distinct exponents in \(m\) are odd, every summand in (4) is even. If exactly one exponent \(e_p\) is odd, only the term indexed by that \(p\) can survive, and it survives precisely when \(p\equiv3,5\pmod8\) and \(\lceil e_p/2\rceil\) is odd, that is, \(e_p\equiv1\pmod4\). If all exponents are even, put \(m=s^2\). Formula (4) reduces to the parity of the sum of \(e_p/2\) over primes \(p\equiv3,5\pmod8\), which equals \((1-\chi_8(s))/2\) modulo \(2\). This proves the odd-index classification.

**4. The powers of two.** For odd \(m\), \(\sigma(m)\) is odd exactly when \(m\) is a perfect square: in \(\sigma(m)=\prod_{p^{e}\parallel m}(1+p+\cdots+p^e)\), each factor has parity \(e+1\). From (2), the parity for \(t=1\) agrees with that for \(t=0\); for every \(t\ge2\), the multiplier \(2^{t-1}-1\) is odd, so the parity toggles exactly in the square branch. This proves the full classification.

**5. Counting.** Put \(N(X)=\#\{n\le X:a(n)\equiv1\pmod2\}\). The square-odd-part branch \(n=2^t s^2\) contributes \(O(\sqrt X)\). In the nonsquare branch, summing \(n=2^t p^{4j+1}r^2\) over \(j\ge1\) gives \(O(\sqrt X)\), since \(\sum_{j\ge1}\sum_{p\ge3}p^{-(4j+1)/2}<\infty\). The omitted condition \(p\nmid r\) for \(j=0\) costs at most \(O(\sqrt X)\), by writing \(r=pu\) and using the convergent series \(\sum_p p^{-3/2}\).

Let \(\Pi_-(y)\) count primes \(p\le y\) with \(p\equiv3,5\pmod8\). The preceding reductions yield
\[
N(X)=\sum_{t\ge0}\sum_{\substack{r\ge1\\r\ \mathrm{odd}}}
\Pi_-\!\left(\frac{X}{2^t r^2}\right)+O(\sqrt X).
\tag{5}
\]
By the prime number theorem in arithmetic progressions, \(\Pi_-(y)\sim y/(2\log y)\). Set \(w=2^t r^2\). On the terms \(w\le X^{1/3}\), the bound \(\Pi_-(X/w)\ll X/(w\log X)\) allows dominated convergence with summable weights \(w^{-1}\); each fixed weight contributes asymptotically \(X/(2w\log X)\). Terms with \(w>X^{1/3}\) contribute at most \(X\sum_{w>X^{1/3}}w^{-1}=O(X^{5/6})\), because
\[
\sum_{t\ge0}\sum_{r\ \mathrm{odd},\ 2^t r^2>X^{1/3}}\frac{1}{2^t r^2}=O(X^{-1/6}).
\]
The leading constant is therefore
\[
\frac12\sum_{t\ge0}2^{-t}
\sum_{r\ \mathrm{odd}}r^{-2}
=\frac12\cdot2\cdot\frac{\pi^2}{8}=\frac{\pi^2}{8},
\]
proving the asserted asymptotic and completing the proof.

## Verification
Run `python3 verify_parity.py` without third-party dependencies. It independently evaluates the original signed partition definition through index 220, computes the published divisor formula and compares its parity with the new classification at every index through 300000, and checks the local congruence (3) at 1232 odd-prime/exponent pairs. The recorded output is in `verification_output.txt`. The local checks and finite coefficient census are corroboration; they are not an infinite proof. The asymptotic uses a classical analytic theorem rather than numerical extrapolation.

## Relationship to prior work
Merca, arXiv:2609.33770v1, Theorem 1.1 supplies the previously known arithmetic formula (1), positivity, a theta-factorization, and a congruence modulo three. It does not state the prime-power modulo-eight decomposition, the all-index exact parity fibers, or their prime-scale counting constant. Merca, arXiv:2610.05020v1, supplies the dyadic relation (2) and congruences modulo odd primes but not the parity support or asymptotic. Previously reported classifications of fixed small values of \(a(n)\) are different: classifying the entire infinite parity-one set and its density is not implied by enumerating the fibers at values below five. The Dirichlet-character and prime-number-theorem inputs are classical and are not claimed as new. An equivalent argument in unindexed literature remains possible.

## Limitations
The asymptotic gives only the leading term, not an explicit effective error or bounds on the first index realizing every admissible form. The exact parity classification does not claim any stronger two-adic valuation, and does not establish new congruences for different partition statistics. The sole source of the starting exact coefficient formula is published work. Independent external audit is not asserted.

## References
1. M. Merca, *The two-block odd partition function*, arXiv:2609.33770v1 (2026-09-27), Theorem 1.1 and Sections 1–5. https://arxiv.org/html/2609.33770v1
2. M. Merca, *Dyadic Structure of the Two-Block Odd Partition Function and Theta-Weighted Congruences for pod(n)*, arXiv:2610.05020v1 (2026-10-04), Sections 1–7. https://arxiv.org/html/2610.05020v1
3. Classical prime number theorem in arithmetic progressions modulo eight; classical evaluation \(\sum_{r\ \mathrm{odd}}r^{-2}=\pi^2/8\).
