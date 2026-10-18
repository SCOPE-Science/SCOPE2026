# No prime \(v\)-palindromes in the first four positional bases

## Finding
For every positional base \(b\in\{2,3,4,5\}\), **there is no prime \(v\)-palindrome in base \(b\)**. Explicitly, if \(p\) is prime, \(b\nmid p\), and its base-\(b\) digit reversal \(r_b(p)\) is different from \(p\), then
\[
v(r_b(p))\ne v(p)=p.
\]
Thus the first four bases are completely excluded from the prime case of the base-classification problem proposed in the literature. The assertion is not that these bases have no \(v\)-palindromes at all: they have composite examples.

## Assumptions and scope
For a positive integer \(n=\prod_{i}q_i^{e_i}\), with distinct prime \(q_i\), define the arithmetic function
\[
v(n)=\sum_{e_i=1}q_i+\sum_{e_i\ge2}(q_i+e_i),\qquad v(1)=0.
\]
For \(b\ge2\) and digits \(a_{L-1}\ne0\), write \(n=\sum_{i=0}^{L-1}a_i b^i\) and \(r_b(n)=\sum_{i=0}^{L-1}a_i b^{L-1-i}\). A base-\(b\) \(v\)-palindrome must satisfy \(b\nmid n\), \(n\ne r_b(n)\), and \(v(n)=v(r_b(n))\). There are no assumptions on the digit length of a prime \(p\). The four bases in the theorem are the entire claim; no conclusion for other bases is asserted.

## Proof
**Divisor-sum estimate.** For every prime \(q\) and every positive integer \(s\),
\[
v(qs)\le q+v(s).
\]
When \(q\nmid s\), this is additivity. When \(q\mid s\), the new \(q\)-power increases its contribution by \(2\) at exponent \(1\), and by \(1\) thereafter, always at most \(q\). By induction, \(v(s)\le s\): this is equality for prime \(s\); for composite \(s=qt\) with \(q,t\ge2\), use \(v(qt)\le q+v(t)\le q+t\le qt\). Consequently, for composite \(n=qs\) with prime \(q\) and \(s\ge2\),
\[
v(n)\le q+s.
\]
If every prime divisor of \(n\) is at least \(d\), then \(q,s\ge d\) and
\[
v(n)\le q+s\le\frac{qs}{d}+d=\frac nd+d,
\]
because \((q-d)(s-d)\ge0\). In particular, a composite odd \(n\) satisfies \(v(n)\le n/3+3\), and a composite \(n\) coprime to \(6\) satisfies \(v(n)\le n/5+5\). An even composite \(n\) satisfies \(v(n)\le n/2+2\).

Fix a prime \(p\) and an admissible base. Put \(r=r_b(p)\), \(L\) for the number of digits, and \(M=b^{L-1}\). Since \(v(p)=p\), if \(r\) is prime, equality \(v(r)=p\) implies \(r=p\), which is explicitly excluded. We may therefore assume \(r\) is composite. Since \(b\nmid p\), the least significant digit is nonzero, so \(M\le r<bM\).

**Base \(2\).** Apart from the excluded prime \(p=2\), \(p\) is odd, so \(r\) is odd. For \(L\ge4\), \(M\ge8\), and
\[
v(r)\le r/3+3<2M/3+3<M+1\le p.
\]
All primes with fewer than four binary digits are \(2,3,5,7\). The first is a multiple of the base, and each of \(3,5,7\) is its own binary reversal.

**Base \(3\).** The prime \(p=3\) is excluded and \(p=2\) is one digit. For other primes, \(p\) is odd. Modulo \(2\), both \(p\) and \(r\) equal the digit sum, so \(r\) is odd. Modulo \(3\), \(r\) equals the original leading ternary digit, which is \(1\) or \(2\); hence \(3\nmid r\). If \(L\ge3\), then \(M\ge9\); since \(M\) is odd and \(p\) odd, \(p\ge M+2\). Thus
\[
v(r)\le r/5+5<3M/5+5<M+2\le p
\]
(the strict middle inequality holds for \(M\ge9\)). For \(L\le2\) the remaining primes are \(5\) and \(7\), whose ternary reversals are each other; their \(v\)-values are unequal.

**Base \(4\).** For \(L\ge4\), put \(M\ge64\) and let \(a\in\{1,2,3\}\) be the first digit. If \(a\) is odd, then \(r\) is odd. Since \(4\equiv1\pmod3\), reversal preserves the digit sum modulo \(3\), so \(3\nmid r\) for every prime \(p>3\). Consequently,
\[
v(r)\le r/5+5<4M/5+5<M+1\le p.
\]
If \(a=2\), then \(r\) is even and \(p\ge2M+1\). We have \(v(r)\le r/2+2<2M+2\). Since \(p\) is odd, equality \(v(r)=p\) would force \(p=2M+1\); then the base-\(4\) digits of \(p\) are \(2,0,\ldots,0,1\), so \(r=M+2\) and \(v(r)\le M/2+3<2M+1=p\), a contradiction. The finitely many primes \(p<64\) not divisible by \(4\) are exactly those checked independently by the complete finite certificate in `verify.py`.

**Base \(5\).** The primes \(2,3\) are single-digit and \(5\) is excluded. For prime \(p>5\), both \(p\) and \(r\) are odd because \(5\) is odd, while \(5\equiv-1\pmod3\) gives \(r\equiv(-1)^{L-1}p\pmod3\), so \(3\nmid r\). Suppose \(L\ge3\), so \(M\ge25\) is odd. The composite bound implies
\[
p=v(r)\le r/5+5<M+5.
\]
Since \(p\ge M+1\) is odd, equality would require \(p=M+d\) for \(d\in\{2,4\}\). Its reversal is then \(r=dM+1\). Yet
\[
v(r)\le(dM+1)/5+5<M+d=p
\]
for both \(d=2,4\) and every \(M\ge25\), contradiction. The remaining prime candidates \(p<25\), other than \(5\), are \(2,3,7,11,13,17,19,23\). The first two are one-digit; the others occur in prime reversal pairs \((7,11)\), \((13,17)\), and \((19,23)\), so none has matching \(v\)-value without being a palindrome.

These cases exhaust all prime candidates in the four bases and prove the theorem.

## Verification
Run `python3 verify.py` from this package. The script independently checks every required small-prime exception (\(32\) prime/base cases in total), including the base-\(4\) composite reversals; it then cross-checks every eligible prime below \(40000\) in each of the four bases. It also confirms the universal divisor-sum estimates on all composite integers up to \(10000\). All tests return `VERIFIED`. Only the listed small-prime enumerations are proof dependencies; the long-range scans are checks, not the basis for the theorem.

## Relationship to prior work
Tsai's *v-palindromes: an analogy to the palindromes* (arXiv:2111.10211v1, public November 17, 2021) defines the base-dependent notion and states Conjecture 13, asserting the absence of prime \(v\)-palindromes in general bases. Its Table 1 provides the least (composite) examples in the first four bases, but no classification of the primes in those bases. The 2024 paper by Bispels and collaborators (arXiv:2405.05267v1) corrects the global perspective by exhibiting prime examples in some higher bases and poses as Problem 1 which bases admit primes. The 2023 paper by Boran and collaborators (arXiv:2307.00770v1) characterizes the decimal case; it does not imply the result for bases \(2\)–\(5\). This proof resolves the first four bases of the 2024 base question using a uniform prime-factor lower-bound observation and explicit radix constraints. Earlier indexed research on ordinary numeral palindromes and their counting functions concerns a different invariant.

## Limitations
No claim is made that base \(6\) is the first base admitting a prime \(v\)-palindrome, or that a prime exists in every base outside the four treated here. Nonprime \(v\)-palindromes do exist in these bases. The conclusion is a deterministic proof, not an extrapolation from finite computation. Independent external evaluation and publication-priority assessment have not been performed; an unindexed general result could subsume the four-base theorem.

## References
1. D. Tsai, *v-palindromes: an analogy to the palindromes*, arXiv:2111.10211v1 (November 17, 2021), https://arxiv.org/abs/2111.10211.
2. C. Bispels, M. Boran, S. J. Miller, E. Sosis, and D. Tsai, *v-Palindromes: An Analogy to the Palindromes*, arXiv:2405.05267v1 (April 24, 2024), https://arxiv.org/abs/2405.05267; *PUMP Journal of Undergraduate Research* 7 (2024), 186–206.
3. M. Boran, G. Choi, S. J. Miller, J. Purice, and D. Tsai, *A characterization of prime v-palindromes*, arXiv:2307.00770v1 (July 3, 2023), https://arxiv.org/abs/2307.00770.
