# A leading-digit obstruction for prime \(v\)-palindromes in even bases

## Finding

**Theorem.** Let \(b\ge2\) be an even integer and \(p\) a prime. Suppose that the most significant digit \(d\) of the base-\(b\) expansion of \(p\) is odd and satisfies \(2d\ge b\). Then \(p\) is not a \(v\)-palindrome in base \(b\). In particular, **there are no prime \(v\)-palindromes in base \(2\)**.

The conclusion uses the standard definition of \(v\)-palindromes: for the base-\(b\) reversal \(r_b(n)\), the conditions are \(b\nmid n\), \(r_b(n)\ne n\), and \(v(r_b(n))=v(n)\). This obstruction holds without a length bound or a restriction on the other digits.

## Assumptions and scope

For a prime \(q\), put \(v(q)=q\); for integer \(e\ge2\), put \(v(q^e)=q+e\); and extend \(v\) additively over coprime positive factors with \(v(1)=0\). Digit reversal means literal reversal of base-\(b\) digits, with leading zeros discarded. The number \(p\) in the theorem is any prime, and \(d\in\{1,\dots,b-1\}\) is the leading base-\(b\) digit. Base \(2\) has only leading digit \(1\); the even prime \(2\) fails the admissibility condition because its last binary digit is zero.

## Proof

**Arithmetic inequality.** We first prove that
\[
 v(m)\le m/2\qquad\text{for every odd composite }m\ge21.
\]
For every prime \(q\) and positive exponents \(e,f\), the prime-power definition gives
\[
 v(q^{e+f})\le v(q^e)+v(q^f).
\]
Indeed, for \(e=f=1\), this is \(q+2\le2q\); if exactly one exponent is one, the inequality follows from \(q\ge1\); if both exceed one, the right side is \(2q+e+f\), versus \(q+e+f\) on the left. Summing these primewise inequalities proves subadditivity \(v(ac)\le v(a)+v(c)\) for arbitrary positive integers \(a,c\).

For each prime power \(q^e\), \(v(q^e)\le q^e\), since this is equality at \(e=1\) and \(q+e\le eq\le q^e\) for \(e\ge2\). The inequality \(x+y\le xy\) for integers \(x,y\ge2\), iterated across distinct prime powers, therefore gives \(v(t)\le t\) for every positive integer \(t\).

Now factor an odd composite \(m\ge21\) as \(m=ac\) with odd integers \(3\le a\le c\). If \(a=3\), then \(c\ge7\); otherwise \(a,c\ge5\). In both cases \((a-2)(c-2)\ge4\), and hence \(a+c\le ac/2\). Consequently
\[
 v(m)=v(ac)\le v(a)+v(c)\le a+c\le m/2.
\]
The only positive odd composites below \(21\) are \(9\) and \(15\), for which \(v(9)=5\) and \(v(15)=8\).

**Reversal obstruction.** If \(p=2\), it cannot satisfy all three defining conditions: in base \(2\) its final digit is zero, while for every other even base its expansion has a single digit. Now assume \(p\) is an odd prime. Because \(b\) is even, the last base-\(b\) digit of \(p\) is odd and nonzero. Its reversal \(s=r_b(p)\) therefore has the same number \(L\) of base-\(b\) digits as \(p\), and its final digit is the odd leading digit \(d\) of \(p\). In particular \(s\) is odd. By the bounds on its digits,
\[
 p\ge d b^{L-1}\ge b^L/2,
 \qquad 1\le s\le b^L-1<2p.
\]
If \(s=p\), the required strict reversal inequality fails. If \(s\ne p\) is prime, then \(v(s)=s\ne p=v(p)\). If \(s\) is odd and composite with \(s\ge21\), then the preceding inequality gives \(v(s)\le s/2<p=v(p)\). The only remaining odd composite possibilities are \(s=9\) and \(s=15\). Since \(v(15)=8\) is not prime, it cannot equal \(v(p)=p\). For \(s=9\), equality would force \(p=5\). However, in even bases \(2\) and \(4\), the respective representations of \(5\) are \((101)_2\) and \((11)_4\), both unchanged by reversal; in every even base \(b\ge6\), \(5\) has a single digit and is also unchanged. Therefore \(r_b(5)\ne9\) for every even \(b\). All cases contradict the definition of a \(v\)-palindrome.

For \(b=2\), every odd prime has leading digit \(d=1\) satisfying \(2d\ge b\), and \(2\) is inadmissible. Hence there are no prime binary \(v\)-palindromes. \(\square\)

## Verification

Run `python3 verify.py` with Python 3's standard library. The checker verifies the odd-composite half-bound for every odd composite through \(400000\); checks all even bases from \(2\) through \(40\) and all odd primes below \(10000\) for the theorem's digit condition; and tests the binary-prime conclusion on the same finite range. It also verifies the known composite binary example \(175\), whose reversal is \(245\), with \(v(175)=v(245)=14\), and the known prime example in base \(16\), \(109\), whose leading digit is even and is therefore outside the theorem's hypotheses. Expected output is provided in `verification_output.txt`. These finite computations are **not** an infinite proof: the preceding argument supplies the unrestricted quantifiers.

## Relationship to prior work

Bispels, Boran, Miller, Sosis, and Tsai, *\(v\)-Palindromes: An Analogy to the Palindromes*, arXiv:2405.05267v1 (first publicly posted \(2024\)-\(04\)-\(24\)), Definition 2 and Problem 1, ask which bases admit prime \(v\)-palindromes. Their Table 1 records \(175\) as the smallest \(v\)-palindrome in base \(2\), while their examples of prime \(v\)-palindromes in bases \(16\) and \(276\) show that prime existence is genuinely base-dependent. The theorem here settles prime nonexistence for base \(2\) and establishes an infinite family of leading-digit exclusions in all even bases. It does **not** assert nonexistence in every even base.

Boran, Choi, Miller, Purice, and Tsai, *A characterization of prime \(v\)-palindromes*, arXiv:2307.00770v1 (2023), classify the possible prime \(v\)-palindromes in base \(10\) and establish the useful general inequality \(v(n)\le n\) (Lemma 2.7). Their base-\(10\) classification does not imply the present all-even-base statement; the stronger odd-composite inequality and reversal leading-digit comparison above give the additional obstruction. Tsai's arXiv:2111.10211v1 provides earlier definitions and context. No claim is made about uniqueness relative to all unindexed literature.

## Limitations

The leading digit must be odd and at least half the base, a sufficient obstruction rather than a full characterization for even bases other than \(2\). Prime \(v\)-palindromes do exist in some even bases (including \(16\)), so the theorem cannot be extended to all even-base primes. The method says nothing about prime \(v\)-palindromes in odd bases. The literature comparison cannot exclude unpublished or unindexed equivalent observations. No independent audit has been performed.

## References

1. C. Bispels, M. Boran, S. J. Miller, E. Sosis, D. Tsai, *\(v\)-Palindromes: An Analogy to the Palindromes*, arXiv:2405.05267v1 (posted 2024-04-24), https://arxiv.org/html/2405.05267v1 .
2. M. Boran, G. Choi, S. J. Miller, J. Purice, D. Tsai, *A characterization of prime \(v\)-palindromes*, arXiv:2307.00770v1 (2023), https://arxiv.org/html/2307.00770v1 .
3. D. Tsai, *\(v\)-palindromes: an analogy to the palindromes*, arXiv:2111.10211v1 (2021), https://arxiv.org/html/2111.10211v1 .
