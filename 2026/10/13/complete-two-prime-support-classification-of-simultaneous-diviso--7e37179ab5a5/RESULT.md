# Complete two-prime-support classification of simultaneous divisor-sum primality
## Finding
Write \(\sigma\) for the ordinary sum of positive divisors, \(\varphi\) for Euler's totient, and \(\omega(n)\) for the number of distinct prime factors of \(n\). Define the Fermat numbers
\[
F_j=2^{2^j}+1\qquad(j\ge0).
\]

**Theorem.** For every integer \(n>2\) with \(\omega(n)\le2\), the two integers
\[
\sigma(n-1),\qquad \sigma(\varphi(n))
\]
are simultaneously prime if and only if exactly one of the following conditions holds:

* \(n=10\);
* \(n=F_j\) is prime and \(2^{2^j+1}-1\) is prime, for an integer \(j\ge0\).

In particular, \(10\) is the **only composite** solution supported on at most two distinct primes. The prime cases within the verified range are \(3,5,17,65537\); the theorem neither presumes that these are all Fermat primes nor that they are all prime solutions.

A structural consequence of the theorem's reduction is that any other composite solution, if one exists, has the form
\[
n=2\prod_{j\in S}F_j,
\]
where \(S\subseteq\{1,2,\ldots\}\) is finite, \(|S|\ge2\), every \(F_j\) is prime, and the integer
\[
1+\sum_{j\in S}2^j
\]
is prime. This is a necessary condition, not an existence assertion.

## Assumptions and scope
Primality means ordinary positive-integer primality; \(1\) is not prime. The classification includes every prime power, all semiprimes, and all integers with arbitrarily high exponents supported on at most two primes. It makes no claim of completeness for \(\omega(n)\ge3\).

The exact simultaneous-primality sequence is OEIS A270414, publicly introduced on 16 March 2016. Its conjectural description as a single composite exception together with certain prime terms motivates isolating the first entire composite prime-support layer.

## Proof
We first establish a standard structural lemma, including the exponent restriction needed below.

**Prime divisor-sum lemma.** If \(t>1\) and \(\sigma(t)\) is prime, then \(t=q^e\) for some prime \(q\) and integer \(e\ge1\); moreover, \(e+1\) is prime. In particular, if \(e\) is odd, then \(e=1\).

Indeed, if \(t\) had two distinct prime factors, multiplicativity of \(\sigma\) would express \(\sigma(t)\) as a product of two integers greater than \(1\). For \(t=q^e\), write
\[
\sigma(q^e)=\frac{q^{e+1}-1}{q-1}.
\]
If \(e+1\) were composite, choose a proper divisor \(d\) with \(1<d<e+1\). Then \((q^d-1)/(q-1)\), strictly between \(1\) and \(\sigma(q^e)\), would divide \(\sigma(q^e)\), contradicting primality. Thus \(e+1\) is prime. If \(e\) is odd, the even prime \(e+1\) must equal \(2\).

Suppose \(n>2\) satisfies both required primalities. Since \(\varphi(n)\) is even and \(\sigma(\varphi(n))\) is prime, the lemma forces
\[
\varphi(n)=2^K\qquad(K\ge1).
\]
If an odd prime \(p\) divided \(n\) to exponent at least \(2\), then \(p\mid\varphi(n)\), which is impossible. Therefore each odd prime factor of \(n\) has exponent \(1\), and \(p-1\) is a power of \(2\). If \(p=2^d+1\) is prime, then \(d\) must be a power of \(2\): otherwise the factorization of \(X^r+1\) for odd \(r>1\) makes \(2^d+1\) composite. Consequently
\[
n=2^a\prod_{j\in S}F_j,
\]
where \(a\ge0\), the \(F_j\) occurring in the finite set \(S\) are distinct primes, and each occurs once.

**Odd composites.** If \(n\) were odd and composite, \(|S|\ge2\). Since \(n-1\) is even and \(\sigma(n-1)\) is prime, the lemma would require
\[
n-1=2^b\qquad(b\ge1).
\]
But expanding \(\prod_{j\in S}(1+2^{2^j})\) produces exactly \(2^{|S|}\) distinct nonzero binary digits: each subset of \(S\) determines a different binary exponent \(\sum_{j\in T}2^j\). Thus \(n\) has at least four nonzero binary digits, whereas \(2^b+1\) has exactly two. Contradiction.

**Even multiples of four.** If \(a\ge2\), then \(n-1\equiv3\pmod4\). By the lemma \(n-1=q^e\) for an odd prime \(q\). Its residue modulo \(4\) forces \(q\equiv3\pmod4\) and \(e\) odd, so the exponent restriction gives \(e=1\). Therefore
\[
\sigma(n-1)=q+1=n,
\]
which is composite. Contradiction. The case \(n=2\) is excluded by hypothesis and in any event satisfies \(\sigma(\varphi(2))=1\). Every composite candidate is hence \(n=2\prod_{j\in S}F_j\), with \(S\ne\varnothing\).

**Exclusion of \(3\).** Put
\[
K=\sum_{j\in S}2^j.
\]
Then \(\varphi(n)=2^K\) and
\[
\sigma(\varphi(n))=2^{K+1}-1.
\]
If \(0\in S\), the integer \(K\) is odd. Since a prime Mersenne number \(2^{K+1}-1\) requires its exponent \(K+1\) to be prime, the even exponent \(K+1\) must equal \(2\). Hence \(K=1\) and \(S=\{0\}\), giving \(n=6\), but \(\sigma(5)=6\) is composite. Thus \(0\notin S\).

**The two-prime layer.** If \(n\) is composite and \(\omega(n)\le2\), the only remaining form is \(n=2F_j\) for some \(j\ge1\). Then
\[
n-1=2^{2^j+1}+1=2^b+1,\qquad b=2^j+1\ge3,
\]
with \(b\) odd. As \(2^b\equiv-1\pmod3\), this integer is divisible by \(3\). The prime divisor-sum lemma therefore forces
\[
2^b+1=3^e.
\]
Since \(b\ge3\), reduction modulo \(8\) gives \(3^e\equiv1\pmod8\), so \(e=2h\) is even. Thus
\[
(3^h-1)(3^h+1)=2^b.
\]
The two factors are positive powers of \(2\) differing by \(2\). The only such pair is \((2,4)\), so \(3^h=3\), \(h=1\), and \(b=3\). It follows that \(j=1\) and \(n=10\). Conversely,
\[
\sigma(10-1)=\sigma(9)=13,
\qquad
\sigma(\varphi(10))=\sigma(4)=7,
\]
and both values are prime.

**Prime inputs.** If \(n=p\) is prime, then \(\varphi(p)=p-1\), and the simultaneous condition is simply that \(\sigma(p-1)\) is prime. For odd \(p\), \(p-1\) is even, so the lemma gives \(p-1=2^e\). Such a prime \(p\) is exactly a Fermat prime \(F_j\), with \(e=2^j\), and
\[
\sigma(p-1)=2^{2^j+1}-1.
\]
This is prime exactly under the stated additional condition. We have exhausted every \(n>2\) with \(\omega(n)\le2\), proving the theorem. The necessary structural condition on any further composite follows from the same reductions and the primality-required exponent \(K+1\).

## Verification
The attached standalone `verify.py` computes \(\varphi(n)\), \(\sigma(n)\), distinct-prime counts, and a primality sieve independently for all
\[
3\le n\le1{,}000{,}000.
\]
For every integer in this range with \(\omega(n)\le2\), it compares direct simultaneous primality with the theorem's explicit classification. The complete directly observed simultaneous-primality set, even without the support restriction, is
\[
\{3,5,10,17,65537\}.
\]
This finite computation corroborates but does not replace the unrestricted proof.

## Relationship to prior work
OEIS A270414 is the **exact predicate** studied here. Its entry records the composite exception \(10\), prime examples, and a conjectural global description; its finite search information does not prove the unrestricted two-prime-support result. OEIS A270413 records \(\sigma(n-1)\) prime and OEIS A062514 records \(\sigma(\varphi(n))\) prime separately. OEIS A249759 concerns the prime inputs and their Fermat/Mersenne requirements. None of these inspected entries supplies the simultaneous-primality theorem for all composite integers with \(\omega(n)\le2\).

Cohen's 1997 primary paper treats the Mąkowski–Schinzel inequalities and equations for \(\sigma(\varphi(n))\), including products of Fermat primes, but it does not impose primality of \(\sigma(n-1)\) or classify the intersection. Luca and Pomerance (2002) likewise study the size and distribution of \(\sigma(\varphi(n))\), not this exact joint prime predicate.

Targeted searches by the original sequence identifier, both simultaneous-primality expressions, the Fermat prime reductions, and the uniqueness of \(10\) in the first composite support layer found no equivalent or stronger proved statement. This is evidence of a specific literature gap, not a proof of worldwide uniqueness.

## Limitations
The theorem does **not** assert that \(10\) is the unique composite solution without a prime-support restriction. The existence of prime solutions involving hypothetical additional Fermat primes is left conditional. The structural necessity for \(\omega(n)\ge3\) does not classify or construct that layer. An equivalent elementary argument could occur in an unindexed note or discussion.

## References
1. OEIS Foundation, A270414, “Numbers \(m\) such that \(\sigma(m-1)\) and \(\sigma(\varphi(m))\) are both primes,” original author date 16 March 2016, https://oeis.org/A270414.
2. OEIS Foundation, A270413, numbers with \(\sigma(n-1)\) prime, https://oeis.org/A270413.
3. OEIS Foundation, A062514, numbers with \(\sigma(\varphi(n))\) prime, https://oeis.org/A062514.
4. OEIS Foundation, A249759, prime inputs with \(\sigma(p-1)\) prime, https://oeis.org/A249759.
5. G. L. Cohen, “On a conjecture of Mąkowski and Schinzel,” *Colloquium Mathematicum* **74** (1997), 1–8, DOI 10.4064/cm-74-1-1-8.
6. F. Luca and C. Pomerance, “On some problems of Mąkowski–Schinzel and Erdős concerning the arithmetical functions \(\varphi\) and \(\sigma\),” *Colloquium Mathematicum* **92** (2002), DOI 10.4064/cm92-1-10.
