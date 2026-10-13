# Complete semiprime classification of divisor-sum divisibility by the totient multiple

## Finding
For every integer \(n>1\) with exactly two prime factors counted with multiplicity, the divisibility
\[
\sigma(n)\mid n\varphi(n)
\]
holds exactly for \(n=6\), and for
\[
n=pq,\qquad p\ge3\text{ prime},\quad q=p(p-1)-1\text{ prime}.
\]
Here \(\sigma\) is the sum of positive divisors and \(\varphi\) is Euler's totient. No prime square satisfies the divisibility. The theorem is an unconditional classification, but it does not assert infinitely many primes \(p\) with \(p(p-1)-1\) prime.

## Assumptions and scope
A semiprime is a positive integer with exactly two prime factors counted with multiplicity, hence \(n=p^2\) or \(n=pq\) for primes \(p<q\). We use the standard identities \(\sigma(pq)=(p+1)(q+1)\), \(\varphi(pq)=(p-1)(q-1)\), \(\sigma(p^2)=p^2+p+1\), and \(\varphi(p^2)=p(p-1)\). Divisibility always means exact integer divisibility.

## Proof
If \(n=p^2\), then \(\gcd(p^2+p+1,p)=1\). Thus divisibility of \(p^3(p-1)=n\varphi(n)\) by \(p^2+p+1\) would force \(p^2+p+1\mid p-1\), which is impossible since \(p^2+p+1>p-1\).

Now take distinct primes \(p<q\). If \(p=2\), the condition is \(3(q+1)\mid2q(q-1)\). In particular \(q+1\mid2q(q-1)\), and reducing modulo \(q+1\) yields \(q+1\mid4\). Since \(q\ge3\), this gives \(q=3\); indeed \(\sigma(6)=12\) divides \(6\varphi(6)=12\).

Suppose both primes are odd. Put
\[
A=(p+1)/2,\qquad B=(q+1)/2.
\]
The desired divisibility becomes precisely
\[
AB\mid pq(A-1)(B-1). \tag{1}
\]
Since \(\gcd(B,q(B-1))=1\), condition (1) implies \(B\mid p(A-1)\). Similarly \(\gcd(A,p(A-1))=1\) gives \(A\mid q(B-1)\). Because \(q>A\) is prime, \(\gcd(q,A)=1\), so \(A\mid B-1\).

We have \(B>A>A-1\), \(B\mid p(A-1)\), and \(\gcd(p,A-1)=1\). Thus \(B=pd\) for some positive divisor \(d\mid A-1\). Reducing \(A\mid B-1\) modulo \(A\), using \(p=2A-1\equiv-1\pmod A\), gives \(A\mid d+1\). As \(1\le d\le A-1\), necessarily \(d=A-1\). Consequently
\[
q=2B-1=2p(A-1)-1=p(p-1)-1.
\]

Conversely, let odd primes \(p<q\) satisfy \(q=p(p-1)-1\). Then \(B=p(A-1)\), so \(B\mid p(A-1)\). Also \(B\equiv1\pmod A\), whence \(A\mid B-1\). Finally \(\gcd(A,B)=1\) because \(B=p(A-1)\), \(p\equiv-1\pmod A\), and \(\gcd(A,A-1)=1\). Therefore the two divisibilities combine to give (1), proving \(\sigma(pq)\mid pq\varphi(pq)\). This proves both directions for every semiprime.

## Verification
Run the included standalone `verify.py` with Python 3. It tests every semiprime \(n\le500000\), including prime squares, and checks predicted versus actual divisibility using integer arithmetic. It independently tests all prime-generated pairs with \(p\le3000\). Its successful result is:

`VERIFY_OK limit= 500000 semiprimes_checked= 109685 hits= [6, 15, 95, 287, 1199, 4607, 23519, 28799, 101567, 223199, 296207, 352799] p_leq= 3000 family_prime_pairs= 108`

The proof, not the finite test, establishes the unbounded classification.

## Relationship to prior work
OEIS A066995 (first recorded January 27, 2002) defines precisely \(\sigma(n)\mid n\varphi(n)\) and lists numerous examples, including semiprimes \(6,15,95,287\), but does not present this full prime-polynomial classification. OEIS A001599 concerns the related but distinct harmonic-divisor condition \(\sigma(n)\mid n\tau(n)\), and OEIS A011775 concerns divisibility in the opposite direction \(n\mid\varphi(n)\sigma(n)\). Neither condition yields this equivalence. Literature and mathematical-record searches for the exact equation and the polynomial prime-pair criterion found no covering result; unindexed earlier work remains a possibility.

## Limitations
Only integers with exactly two prime factors counted with multiplicity are classified. The theorem does not classify numbers with three or more prime factors, and it neither proves nor disproves infinitude of primes \(p\) for which \(p(p-1)-1\) is prime. External novelty and correctness have not been independently audited.

## References
1. OEIS A066995, “Numbers \(n\) such that \(\sigma(n)\) divides \(n\varphi(n)\),” original entry January 27, 2002, https://oeis.org/A066995.
2. OEIS A001599, “Harmonic or Ore numbers,” https://oeis.org/A001599.
3. OEIS A011775, “Numbers \(n\) such that \(n\) divides \(\varphi(n)\sigma(n)\),” https://oeis.org/A011775.
