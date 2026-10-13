# Exact \(\Omega(n)\le2\) classification and phase transition for \(b\sigma(n)=an+k\)

## Finding
Let \(a>b\ge1\) be coprime integers, let \(k\ne0\) be an integer, and put
\[
c=a-b,\qquad T=ab-ck.
\]
Let \(\sigma(n)\) be the sum of the positive divisors of \(n\), and let \(\Omega(n)\) count prime factors with multiplicity. Among integers \(n\ge2\) with \(\Omega(n)\le2\), all solutions of
\[
b\sigma(n)=an+k
\]
are given exactly as follows.

For a prime solution \(n=p\), one must have
\[
cp=b-k.
\]
Thus the prime branch contains the single candidate \(p=(b-k)/c\), retained exactly when it is a positive prime integer.

For a prime-square solution \(n=p^2\), one must have
\[
cp^2-bp+k-b=0.
\]
Equivalently, with
\[
\Delta=b^2+4c(b-k),
\]
the prime-square branch consists exactly of prime integer roots
\[
p=\frac{b\pm\sqrt{\Delta}}{2c}.
\]

For a squarefree semiprime solution \(n=pq\) with distinct primes \(p<q\), one has the exact factorization
\[
(cp-b)(cq-b)=T.
\]
Hence, if \(T\ne0\), the squarefree semiprime solutions are in bijection with unordered integer factor pairs \(\{u,v\}\) satisfying
\[
uv=T,
\]
for which
\[
\frac{u+b}{c}\quad\text{and}\quad\frac{v+b}{c}
\]
are distinct positive primes.

There is a sharp finite/infinite transition. The set of solutions with \(n\ge2\) and \(\Omega(n)\le2\) is finite for every parameter triple except when
\[
(a,b,k)=(r+1,r,r(r+1))
\]
for a prime \(r\). In that exceptional family the complete low-multiplicity solution set is
\[
\{rq:q\text{ prime},\ q\ne r\},
\]
and therefore its counting function is exactly
\[
\pi(x/r)-\mathbf 1_{r^2\le x}.
\]
In particular it is asymptotic to \(x/(r\log x)\) for fixed \(r\).

## Assumptions and scope
The parameters satisfy \(a>b\ge1\), \(\gcd(a,b)=1\), and \(k\ne0\). The theorem classifies only nontrivial integers \(n\ge2\) with \(\Omega(n)\le2\). It makes no assertion about solutions with \(\Omega(n)\ge3\).

The low-\(\Omega\) restriction is the first multiplicative layer in which the equation has genuinely two-prime behavior: every admissible \(n\) is a prime, a prime square, or a product of two distinct primes. The exceptional infinite family is not imposed in advance; it is forced by the vanishing of the factorization constant \(T\).

## Proof
Because \(n\ge2\) and \(\Omega(n)\le2\), exactly three shapes are possible.

If \(n=p\) is prime, then \(\sigma(p)=p+1\), so
\[
b(p+1)=ap+k.
\]
Rearranging gives
\[
(a-b)p=b-k,
\]
which is the claimed prime criterion.

If \(n=p^2\), then \(\sigma(p^2)=p^2+p+1\), so
\[
b(p^2+p+1)=ap^2+k.
\]
With \(c=a-b\), this is exactly
\[
cp^2-bp+k-b=0.
\]
The quadratic formula gives the stated discriminant and roots, and retaining only positive prime integers is both necessary and sufficient.

Now let \(n=pq\) with distinct primes \(p<q\). Since \(\sigma(pq)=(p+1)(q+1)\), the equation becomes
\[
b(p+1)(q+1)=apq+k.
\]
After collecting terms,
\[
cpq-b(p+q)=b-k.
\]
Multiplying by \(c\) and adding \(b^2\) gives
\[
(cp-b)(cq-b)
=c\bigl(cpq-b(p+q)\bigr)+b^2
=c(b-k)+b^2
=ab-ck
=T.
\]
Every algebraic step is reversible. Thus, when \(T\ne0\), every squarefree semiprime solution produces an integer factor pair of \(T\), and every factor pair for which the two reconstructed quantities are distinct positive primes produces a solution. Since a nonzero integer has finitely many divisors, this branch is finite.

It remains to analyze \(T=0\). A squarefree semiprime solution would satisfy
\[
(cp-b)(cq-b)=0.
\]
Hence \(cp=b\) or \(cq=b\). Because
\[
\gcd(c,b)=\gcd(a-b,b)=\gcd(a,b)=1,
\]
the divisibility \(c\mid b\) forces \(c=1\). The prime equal to \(b/c\) is then \(b\), so \(b\) itself must be prime. The identity \(T=0\) now forces
\[
k=ab=b(b+1).
\]
Conversely, if \(b=r\) is prime, \(a=r+1\), and \(k=r(r+1)\), then for every prime \(q\ne r\),
\[
r\sigma(rq)=r(r+1)(q+1)=(r+1)rq+r(r+1),
\]
so \(rq\) is a solution.

There are no additional low-multiplicity solutions in this exceptional family. The prime criterion would require a negative prime, while the prime-square equation becomes
\[
p^2-rp+r^2=0,
\]
whose discriminant is \(-3r^2<0\). Thus the exceptional family consists exactly of \(rq\) with \(q\ne r\) prime. Counting such \(q\le x/r\) gives
\[
\pi(x/r)-\mathbf 1_{r^2\le x},
\]
and the prime number theorem yields the stated asymptotic.

## Verification
The bundled program `verify.py` independently enumerates coprime parameter pairs \(a>b\ge1\), nonzero shifts \(k\), and all \(n\le1000\) with \(\Omega(n)\le2\) over a finite regression range. It compares direct evaluation of \(b\sigma(n)=an+k\) against a classifier constructed from the prime branch, quadratic prime-square branch, signed factor pairs of \(T\), and the \(T=0\) exceptional family.

The finite computation is only a regression test. The proof above is symbolic and has no numerical cutoff.

## Relationship to prior work
Kwan and Miller define
\[
S(a,b;k)=\{n:b\sigma(n)=an+k\}
\]
for \(k\ne0\), \(a>b\ge1\), and \(\gcd(a,b)=1\), and prove a counting dichotomy for the full solution set. Their Proposition 2.7 gives an asymptotic main term when a regular family exists and an \(O(b^2x^{2/3+o(1)})\) bound otherwise. The present result asks a different exact question: it completely classifies the first two multiplicative layers \(\Omega(n)\le2\), identifies a divisor-pair parametrization when \(T\ne0\), and proves that exactly one parameter family has infinitely many low-multiplicity solutions.

Pomerance's 1975 paper studies the special equations \(\sigma(n)=hn+t\) and their congruence classes, including regular infinite families and density bounds. Those results motivate the regular/sporadic viewpoint but do not state the generalized \(b\sigma(n)=an+k\) low-\(\Omega\) factorization or its finite/infinite boundary.

Davis, Klyve, and Kraght numerically study the special difference \(\sigma(n)-2n\), and OEIS A087998 records the least solution of \(\sigma(x)=2x+2m\) for each listed \(m\). These sources concern special parameter slices and do not imply the all-parameter classification above.

## Limitations
The result does not classify \(\Omega(n)\ge3\), nor does it improve the global counting exponent for sporadic solutions. The originality search covered the focal full text, the classical Pomerance source, the special \(b=1\) difference literature, a relevant sequence database, exact-form web searches, semantic mathematical-result searches, and the available prior result ledger. An unindexed older note could still contain the elementary semiprime factorization independently.

## References
1. C.-H. Kwan and S. J. Miller, *On the Within-Perfect Numbers*, arXiv:2406.06892v1; *Quarterly Journal of Mathematics* 75 (2024), 1415–1427, DOI:10.1093/qmath/haae052.
2. C. Pomerance, *On the congruences \(\sigma(n)\equiv a\pmod n\) and \(n\equiv a\pmod{\varphi(n)}\)*, *Acta Arithmetica* 26 (1975), 265–272, DOI:10.4064/aa-26-3-265-272.
3. N. Davis, D. Klyve, and N. Kraght, *On the difference between an integer and the sum of its proper divisors*, *Involve* 6 (2013), 493–504, DOI:10.2140/involve.2013.6.493.
4. OEIS A087998, least \(x\) satisfying \(\sigma(x)=2x+2m\).
