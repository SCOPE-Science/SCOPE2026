# Exact progression laws and forbidden classes for noncyclic squarefree semiprimes

## Finding
For each fixed integer \(m\ge1\) and \(0\le c<m\), let \(B_{m,c}(X)\) count distinct primes \(p<q\) satisfying
\[
pq\le X,\qquad p\mid(q-1),\qquad pq\equiv c\pmod m.
\]
These are precisely the squarefree semiprimes \(pq\) for which \(\gcd(pq,\varphi(pq))>1\), i.e. those that are not cyclic group orders. Define, for each prime divisor \(p\) of \(m\),
\[
h_p=m/p,\qquad d_p=\gcd(p,h_p),\qquad L_p=\operatorname{lcm}(p,h_p).
\]
With \(\mathbf1_E\) denoting the indicator of a condition, put
\[
K_{m,c}=\frac{\mathbf1_{\gcd(c,m)=1}}{\varphi(m)}\sum_{\substack{p\text{ prime}\\p\nmid m}}\frac1{p(p-1)}
+\sum_{\substack{p\mid m,\ p\text{ prime}\\p\mid c,\ \gcd(c/p,h_p)=1\\c/p\equiv1\ (\mathrm{mod}\ d_p)}}\frac1{p\varphi(L_p)}.
\]
The prime series converges absolutely. The asymptotic formula is
\[
B_{m,c}(X)=\bigl(K_{m,c}+o(1)\bigr)\frac X{\log X}
\qquad(X\to\infty).
\]
In particular, \(K_{m,c}>0\) if and only if either \(\gcd(c,m)=1\), or \(\gcd(c,m)=p\) for a prime \(p\) such that \(p^2\nmid m\) or \(c/p\equiv1\pmod p\). In every excluded class there is an exact finite cutoff:
\[
B_{m,c}(X)=B_{m,c}(m^2)\quad\text{whenever }X>m^2.
\]
Thus the permitted classes have positive \(X/\log X\) counts, whereas the remaining classes admit no sufficiently large example. Among unit residues the leading constant is independent of \(c\).

For example, modulo \(9\), the class \(3\) has constant \(1/6\), but no such product greater than \(81\) can be congruent to \(6\). Modulo \(8\), the classes \(2\) and \(6\) each have constant \(1/4\), while classes \(0\) and \(4\) contain none beyond \(64\).

## Assumptions and scope
All moduli \(m\) are fixed as \(X\to\infty\); no uniformity as \(m\) grows is asserted. Primes satisfy \(p<q\); repeated-prime squares are excluded. The totient \(\varphi\) is Euler's function, with \(\varphi(1)=1\), and the usual conventions on congruences modulo \(1\) apply. In the coefficient, the sum over \(p\mid m\) is only over prime divisors. The statement includes \(m=1\), where the second sum is empty.

## Proof
**1. Reduction to one divisibility direction.** For primes \(p<q\), \(\varphi(pq)=(p-1)(q-1)\). Neither \(q\mid(q-1)\) nor \(q\mid(p-1)\); also \(p\nmid(p-1)\). Therefore
\[
\gcd(pq,\varphi(pq))>1\iff p\mid(q-1).
\]

**2. Fixed smaller prime not dividing the modulus.** Fix \(p\nmid m\). If \(\gcd(c,m)=1\), the two congruences
\[
q\equiv1\pmod p,\qquad q\equiv cp^{-1}\pmod m
\]
select one reduced residue class modulo \(mp\), by the Chinese remainder theorem. The prime number theorem in arithmetic progressions, with this modulus fixed, gives
\[
\#\{q>p:q\le X/p,\ q\text{ in this class}\}
\sim\frac{X}{p\varphi(mp)\log X}
=\frac{X}{\varphi(m)p(p-1)\log X}.
\]
If \(\gcd(c,m)>1\), a prime \(q\) contributing to \(pq\equiv c\pmod m\) must divide \(m\), hence \(q\le m\) and \(pq<m^2\). These exceptional pairs cannot affect the leading term.

**3. Fixed smaller prime dividing the modulus.** Fix prime \(p\mid m\), and put \(h=m/p\). For \(pq\equiv c\pmod m\), it is necessary that \(p\mid c\); then the condition is equivalent to
\[
q\equiv c/p\pmod h,\qquad q\equiv1\pmod p.
\]
These congruences are compatible precisely when \(c/p\equiv1\pmod{\gcd(p,h)}\). When \(\gcd(c/p,h)=1\), they determine one reduced class modulo \(\operatorname{lcm}(p,h)\), contributing
\[
\frac{X}{p\varphi(\operatorname{lcm}(p,h))\log X}\,(1+o(1)).
\]
If \(\gcd(c/p,h)>1\), the only possible primes \(q\) divide \(h\), hence \(q\le m\) and \(pq<m^2\). An incompatible pair of congruences has no solutions. Summing over the finitely many prime divisors of \(m\) gives the second term of \(K_{m,c}\).

**4. Controlling the unfixed primes.** For \(p<q\le X/p\) with \(p\mid(q-1)\), write \(q=1+kp\). Then \(k<X/p^2\), so the total contribution from \(p>X^{1/3}\) is bounded by
\[
\sum_{p>X^{1/3}}\frac X{p^2}=O(X^{2/3})=o(X/\log X).
\]
For \(Y<p\le X^{1/3}\), with \(p\nmid m\) and unit \(c\), the Brun–Titchmarsh inequality applied to the single class modulo \(mp\), at height \(X/p\), yields, for sufficiently large \(X\) depending on fixed \(m\),
\[
\#\{q\}\ll_m\frac{X}{p(p-1)\log X}.
\]
Summing this over \(p>Y\) contributes \(O_m\bigl(X/(Y\log X)\bigr)\), since \(\sum_{p>Y}1/[p(p-1)]=O(1/Y)\). All \(p\mid m\) have already been treated individually. Fixing \(Y\), applying the prime number theorem to the finitely many remaining \(p\), and then sending \(Y\to\infty\), proves the full asymptotic and its convergent leading constant.

**5. Exact support.** If \(\gcd(c,m)=1\), any fixed prime \(p\nmid m\) supplies a positive summand. Otherwise, a positive coefficient requires a prime \(p\mid m\) satisfying the step-3 conditions. The condition \(\gcd(c/p,m/p)=1\) is equivalent to \(\gcd(c,m)=p\). The remaining compatibility is automatic if \(p^2\nmid m\), and equals \(c/p\equiv1\pmod p\) if \(p^2\mid m\). This proves the stated if-and-only-if classification. In any unsupported class, a putative pair with \(pq>m^2\) has \(q>m\), hence \(q\nmid m\); steps 2 and 3 show such a pair would force one of the positive coefficient conditions, a contradiction. Therefore no such pair exists beyond the given cutoff.

## Verification
The standalone `verify.py` uses a prime sieve and integer arithmetic to check the progression-support equivalences for every \(1\le m\le77\). It checks \(35{,}890\) qualifying prime-pair incidences for moduli up to \(74\), verifies the stated forbidden-class cutoff on selected moduli, and enumerates counts through \(X=2{,}000{,}000\). The command `python verify.py` reports `VERIFY_OK`. Finite enumeration is not the source of the infinite asymptotic: that part rests on the prime number theorem in fixed arithmetic progressions and the Brun–Titchmarsh bound.

## Relationship to prior work
Cohen's 2025 study of cyclic numbers explicitly raises the question of their distribution over arithmetic progressions. The present theorem treats a different, sharply defined subfamily: the *noncyclic* squarefree semiprimes, identifying exact forbidden residue classes. It does not solve the distribution problem for all cyclic numbers. Ibarra's 2026 work concerns Sophie Germain cyclic numbers and a subadditivity counterexample, not this semiprime count. Crisan and Erban analyze unrestricted semiprime counts without the simultaneous divisor relation \(p\mid(q-1)\) and progression restriction. The related Duffinian semiprime criterion involves divisibility of a *sum-of-divisors* value, hence a different congruence \(q\equiv-1\pmod p\); a known relative-density result for that family does not supply this all-moduli constant and support law.

## Limitations
Only fixed moduli are covered. The theorem counts neither all composite noncyclic numbers nor cyclic semiprimes. The prime-series constant is explicit but generally not an elementary finite expression. An exhaustive search of all historical literature is not available; an unindexed general theorem on constrained prime pairs may imply the result. No claim of optimal quantitative error or uniformity in the modulus is made.

## References
1. J. E. Cohen, *Conjectures about Primes and Cyclic Numbers*, Journal of Integer Sequences **28** (2025), Article 25.4.7, published August 7, 2025. https://cs.uwaterloo.ca/journals/JIS/VOL28/Cohen/cohen41.html ; arXiv:2508.08335.
2. J. A. Ibarra, *A counterexample to a subadditivity conjecture of Cohen for Sophie Germain cyclic numbers*, arXiv:2607.09793, first posted July 9, 2026. https://arxiv.org/abs/2607.09793.
3. D. Crisan and R. Erban, *On the counting function of semiprimes*, Integers **21** (2021); arXiv:2006.16491. https://arxiv.org/abs/2006.16491.
4. Brun–Titchmarsh theorem and the classical prime number theorem in arithmetic progressions, in their standard fixed-modulus forms.
