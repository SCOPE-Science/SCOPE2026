# The unique collision of \(n\tau(n)\) among \(3\)-almost-primes

## Finding
Let \(\tau(n)\) denote the number of positive divisors of \(n\), and let \(\Omega(n)\) denote the number of prime factors of \(n\), counted with multiplicity. Define
\[
D(n)=n\tau(n).
\]
For all positive integers \(m,n\) with \(\Omega(m)\le3\) and \(\Omega(n)\le3\),
\[
D(m)=D(n)
\]
implies either \(m=n\) or
\[
\{m,n\}=\{18,27\}.
\]
Thus \(D\) is injective on integers with \(\Omega\le2\), and its restriction to integers with \(\Omega\le3\) has exactly one non-singleton fiber:
\[
18\tau(18)=18\cdot6=108=27\cdot4=27\tau(27).
\]

## Assumptions and scope
The statement concerns positive integers. The bound \(\Omega(n)\le3\) counts prime factors with multiplicity. The possible factorization types are \(1\), \(p\), \(p^2\), \(pq\), \(p^3\), \(p^2q\), and \(pqr\), with distinct letters denoting distinct primes. No assertion is made for inputs with four or more prime factors counted with multiplicity.

## Proof
Assume \(m<n\) and \(D(m)=D(n)\). Then
\[
\frac{n}{m}=\frac{\tau(m)}{\tau(n)}>1,
\]
so \(\tau(m)>\tau(n)\). For \(\Omega\le3\), the possible divisor counts are \(1,2,3,4,6,8\). Since \(n>m\), the case \(\tau(n)=1\) is impossible. Hence \((\tau(m),\tau(n))\) is one of
\[
(3,2),(4,2),(4,3),(6,2),(6,3),(6,4),(8,2),(8,3),(8,4),(8,6).
\]

For \((3,2)\), \(m=p^2\) and \(n=3p^2/2\). Integrality forces \(p=2\), giving \(n=6\), not prime. The pairs \((4,2)\), \((6,2)\), and \((8,2)\) are impossible because \(n=2m\), \(3m\), or \(4m\) is composite.

For \((4,3)\), \(n=4m/3\). If \(m=p^3\), integrality forces \(p=3\), giving \(n=36\) and \(\tau(n)=9\). If \(m=pq\), one prime is \(3\), so \(m=3r\) and \(n=4r\); its divisor count is \(4\) for \(r=2\) and \(6\) otherwise, never \(3\).

For \((6,3)\), \(m=p^2q\) with distinct primes and \(n=2m\). Then \(n\) has at least two distinct prime divisors, while divisor count \(3\) characterizes a prime square.

For \((6,4)\), write \(m=p^2q\) with distinct primes. Since \(n=3m/2\), the prime \(2\) divides \(m\). If \(p=2\), then \(m=4q\) and \(n=6q\), whose divisor count is \(6\) when \(q=3\) and \(8\) otherwise. If \(q=2\), then \(m=2p^2\) and \(n=3p^2\). For \(p=3\) this gives \((m,n)=(18,27)\); for \(p\ne3\), \(\tau(n)=6\). Thus this case yields precisely the claimed collision.

For \((8,3)\), \(m=pqr\) is squarefree and \(n=8m/3\), so \(3\mid m\). If \(2\mid m\), then \(m=6r\) and \(n=16r\), with \(\tau(n)=10\); otherwise \(n=8pq\), with \(\tau(n)=16\). For \((8,4)\), \(n=2m\); its divisor count is \(12\) if \(2\mid m\) and \(16\) otherwise. For \((8,6)\), \(n=4m/3\), so \(3\mid m\); if \(2\mid m\), then \(m=6r\) and \(n=8r\), with \(\tau(n)=8\), while otherwise \(m=3pq\) and \(n=4pq\), with \(\tau(n)=12\).

All possibilities are exhausted, leaving only \(18\leftrightarrow27\).

## Verification
`case_table.json` records the ten strict divisor-count pairs. `verify.py` independently enumerates all \(n\le10^6\) with \(\Omega(n)\le3\), computes \(n\tau(n)\), and checks every fiber. It returns `VERIFY_OK limit=1000000 low_omega_inputs=539387 nontrivial_fibers={108: [18, 27]}`. This finite computation is a regression check only; the proof above is cutoff-free.

## Relationship to prior work
Noppakaew and Pongsriiam introduced \(D(n)=n\tau(n)\) as Example 9 in *Product of Some Polynomials and Arithmetic Functions*. They exhibited the collision family \(D(18a)=D(27a)\) for \(\gcd(a,6)=1\), and their Theorem 13 proves injectivity of \(n^a\tau(n)^b\) on squarefree integers. Those statements do not classify collisions among repeated-prime inputs with \(\Omega\le3\). OEIS A338382, A338384, and A338385 record repeated and primitive values, beginning with the \(18,27\) collision, but do not state the low-\(\Omega\) uniqueness theorem proved here.

## Limitations
The theorem is a low-almost-prime classification. It does not classify primitive collisions globally, does not address fibers containing numbers with \(\Omega\ge4\), and does not claim that \(108\) is the only primitive common value in general.

## References
1. P. Noppakaew and P. Pongsriiam, “Product of Some Polynomials and Arithmetic Functions,” *Journal of Integer Sequences* 26 (2023), Article 23.9.1, Example 9 and Theorem 13. Published November 2, 2023.
2. OEIS A038040, values of \(n\tau(n)\).
3. OEIS A338382, repeated values of \(n\tau(n)\).
4. OEIS A338384, primitive repeated values for \(n\tau(n)\).
5. OEIS A338385, primitive pairs for \(n\tau(n)\).
