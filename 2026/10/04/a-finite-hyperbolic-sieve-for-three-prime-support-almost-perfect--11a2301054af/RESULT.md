# A finite hyperbolic sieve for three-prime-support almost perfect numbers
## Finding
Let \(r,\alpha,\beta\ge 1\), let \(p<q\) be odd primes, and suppose \(n=2^r p^\alpha q^\beta\) is almost perfect, so \(\sigma(n)=2n-1\). Put \(A=2^{r+1}\). Then \(p,q>A\) and \[(p-A)(q-A)\le A(A-1)-1.\] Consequently \(p\le 2A-3\) and \[q\le A+\left\lfloor\frac{A(A-1)-1}{p-A}\right\rfloor\le A^2-1.\] Thus, for each fixed \(r\), only finitely many ordered odd-prime supports can occur, independently of the exponents \(\alpha,\beta\).

## Assumptions and scope
Here \(\sigma(m)\) is the sum of the positive divisors of \(m\), and an almost perfect number satisfies \(\sigma(m)=2m-1\). The theorem is conditional: it gives necessary restrictions on any almost perfect integer having exactly the three prime supports \(2,p,q\). It does not assert that any such integer exists. The exponents \(lpha\) and \(eta\) are arbitrary positive integers; the proof does not need the stronger known fact that the odd part of a non-power-of-two even almost perfect number is a square.

## Proof
Set \(N=p^lpha q^eta\) and \(A=2^{r+1}\). Multiplicativity of \(\sigma\) and the almost-perfect identity give
\[
(A-1)\sigma(N)=AN-1.
\]
Hence the sum \(s(N)=\sigma(N)-N\) of the proper divisors of \(N\) is
\[
s(N)=rac{N-1}{A-1}.
\]
Because \(N/p\) is a proper divisor and there are other positive proper divisors, \(s(N)>N/p\). Therefore \(p>A-1\). Since \(p\) is odd and \(A\) is even, \(p>A\). The same argument gives \(q>A\).

The exact abundancy of \(N\) is
\[
rac{\sigma(N)}N=rac{AN-1}{(A-1)N}.
\]
For a finite prime power, \(\sigma(p^lpha)/p^lpha<p/(p-1)\), and similarly for \(q\). Thus
\[
rac{AN-1}{(A-1)N}<rac p{p-1}rac q{q-1}.
\]
After cross multiplication, define
\[
D=(A-1)Npq-(AN-1)(p-1)(q-1)>0.
\]
Direct expansion yields
\[
D=Nigl(A(p+q-1)-pqigr)+(p-1)(q-1).
\]
Let \(K=A(p+q-1)-pq\). If \(K\le-1\), then \(N>(p-1)(q-1)\) gives \(D<0\), a contradiction. Hence \(K\ge0\). In fact \(K\) is odd, because \(A(p+q-1)\) is even while \(pq\) is odd, so \(K\ge1\). Therefore
\[
pq\le A(p+q-1)-1,
\]
which is equivalent to
\[
(p-A)(q-A)\le A(A-1)-1.
\]

Write \(x=p-A\) and \(y=q-A\). Both are positive odd integers and \(y\ge x+2\). If \(x\ge A-1\), then \(xy\ge(A-1)(A+1)=A^2-1>A^2-A-1\), contradicting the hyperbolic bound. Thus \(x\le A-3\), or \(p\le2A-3\). Solving the hyperbolic bound for \(q\) gives
\[
q\le A+\left\lfloorrac{A(A-1)-1}{p-A}ightfloor,
\]
and \(p-A\ge1\) gives \(q\le A^2-1\).

## Verification
The proof is symbolic and covers every parameter in the stated range. The accompanying `verify.py` checks the key algebraic equivalence and the derived prime bounds over \(14815\) admissible prime pairs for \(1\le r\le7\). It also performs a supplementary search over \(1\lelpha,eta\le4\); no exact almost-perfect example occurs there. This finite computation is corroborative only and is not used to prove the infinite theorem.

## Relationship to prior work
Antalan and Dris treat non-power-of-two even almost perfect numbers in full text and record the structural form \(2^r b^2\), together with the established lower bound \(2^{r+1}<b\). Their paper also develops abundancy bounds for the odd part. The present statement instead isolates the first support size beyond the two-prime-support deficient-perfect classification and obtains a joint inequality on the two odd primes; for fixed \(r\), it makes their possible support finite independently of the exponents.

Tang, Ren, and Li determine all deficient-perfect numbers with at most two distinct prime factors. That result does not cover the three-prime-support family considered here. Antalan's earlier non-almost-perfect criterion excludes an odd prime divisor at most \(2^{r+1}-1\); the proof above recovers the strict lower side and adds the upper hyperbolic coupling between the two odd primes.

## Limitations
The theorem is only a necessary condition and does not settle existence. It does not bound the exponents \(lpha,eta\), and it is specific to exactly two odd prime supports. Focused searches and inspection of the closest full text found no equivalent joint hyperbolic inequality, but search failure is not a proof of novelty; older or differently phrased literature may contain an equivalent observation.

## References
1. J. R. M. Antalan and J. A. B. Dris, “Some New Results On Even Almost Perfect Numbers Which Are Not Powers Of Two,” arXiv:1602.04248v1 (2016).
2. M. Tang, X.-Z. Ren, and M. Li, “On near-perfect and deficient-perfect numbers,” *Colloquium Mathematicum* 133 (2013), 221–226, DOI 10.4064/cm133-2-8.
3. J. R. M. Antalan, “Why Even Almost Perfect Numbers Should not be Divisible by 3? A Non-Almost Perfect Criterion for Even Positive Integers,” *AIP Conference Proceedings* 1602 (2014), 881–885, DOI 10.1063/1.4882588.
