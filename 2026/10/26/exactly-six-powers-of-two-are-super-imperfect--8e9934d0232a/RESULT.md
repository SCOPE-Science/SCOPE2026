# Exactly six powers of two are super-imperfect

## Finding
Let \(\beta\) be the multiplicative arithmetic function defined by \(\beta(1)=1\) and
\[
\beta(p^e)=p^e-p^{e-1}+\cdots+(-1)^e
=\frac{p^{e+1}+(-1)^e}{p+1}
\]
for primes \(p\) and integers \(e\ge1\). Call \(n\) **super-imperfect** when \(2\beta(\beta(n))=n\). Then, for every integer \(a\ge1\),
\[
2\beta(\beta(2^a))=2^a
\quad\Longleftrightarrow\quad
 a\in\{1,2,3,7,15,31\}.
\]
Equivalently, the complete set of super-imperfect powers of two is
\[
\{2,4,8,128,32768,2147483648\}.
\]
This does not classify super-imperfect integers that are not powers of two.

## Assumptions and scope
The input is an arbitrary *positive* exponent \(a\), with no upper bound. The function \(\beta\) is the alternating sum-of-divisors function, also called the square-totient function. A Fermat number is \(F_j=2^{2^j}+1\) for an integer \(j\ge0\). The proof uses elementary congruences, unique prime factorization, and the explicitly verifiable facts that \(F_0,\ldots,F_4\) are prime and \(F_5=641\cdot6700417\) is composite. No assumption is made about later Fermat numbers.

## Proof
**Step 1: odd inputs having \(\beta\)-value a power of two.** Let \(B\) be an odd positive integer. We claim that \(\beta(B)\) is a power of two if and only if \(B\) is a squarefree product of distinct Fermat primes (including the empty product \(B=1\)).

Indeed, by multiplicativity each factor \(\beta(p^e)\), for an odd prime \(p\mid B\), must itself be a power of two. For even \(e\ge2\), the alternating expression \(\beta(p^e)\) is an odd integer greater than one and cannot be a power of two. For odd \(e=2t+1\),
\[
\beta(p^{2t+1})=(p-1)(1+p^2+p^4+\cdots+p^{2t}).
\]
If \(t\ge1\), put \(R=\sum_{i=0}^{t}p^{2i}\). As \(p^2\equiv1\pmod8\), this valuation identity follows directly: write \(t+1=2^u v\) with \(v\) odd; the quotient \(1+x+\cdots+x^{v-1}\) is odd for odd \(x\), and in the factorization of \((x^{2^u}-1)/(x-1)\) the \(u\) factors \(x^{2^r}+1\) each have exactly one factor of two when \(x=p^2\). Hence
\[
\nu_2(R)=\nu_2(t+1).
\]
But \(R>t+1\ge2^{\nu_2(t+1)}\), so \(R\) has an odd factor greater than one. Thus only \(e=1\) is possible. In that case \(\beta(p)=p-1\) is a power of two precisely for primes \(p=2^s+1\) with \(s\ge1\) a power of two: if \(s\) possessed an odd factor \(d>1\), then \(2^s+1\) would be divisible by \(2^{s/d}+1\) strictly between one and itself. These primes are precisely the Fermat primes. The converse follows from \(\beta(F_j)=F_j-1=2^{2^j}\). In particular, for \(B\) as claimed and its set of Fermat indices \(J\),
\[
B=\prod_{j\in J}F_j,\qquad \beta(B)=2^{\sum_{j\in J}2^j}.
\]

**Step 2: reduce the original equation to a Fermat-digit identity.** For each \(a\ge1\), the odd integer \(B=\beta(2^a)\) equals
\[
B=\frac{2^{a+1}+(-1)^a}{3}.
\]
If \(2\beta(B)=2^a\), Step 1 and uniqueness of binary representation force
\[
B=\prod_{j\in J_a}F_j,
\qquad J_a=\{j\ge0:\text{the binary digit of }a-1\text{ at }j\text{ is }1\}.
\tag{1}
\]
Every \(F_j\) appearing in (1) must actually be prime. Conversely, if (1) holds with each appearing \(F_j\) prime, then the required iteration equation holds.

**Step 3: all even exponents except \(a=2\) are impossible.** If \(a\) is even and \(a\ge4\), then \(2^{a+1}\equiv0\pmod{16}\). Because division by three is valid modulo sixteen,
\[
B=\frac{2^{a+1}+1}{3}\equiv11\pmod{16}.
\]
Yet \(a-1\) is odd, so \(0\in J_a\) and the product (1) contains \(F_0=3\). The only further Fermat factor not congruent to one modulo sixteen is \(F_1=5\), while \(F_j\equiv1\pmod{16}\) for every \(j\ge2\). Therefore the right side of (1) is congruent to either \(3\) or \(15\pmod{16}\), a contradiction. At \(a=2\), \(B=3\) and \(\beta(B)=2\), giving a solution.

**Step 4: a missing binary digit rules out an odd exponent.** For odd \(a\), \(a-1\) is even, hence \(0\notin J_a\). The case \(a=1\) yields \(B=1\), a solution. Suppose \(a\ge3\) and let \(h\ge1\) be the highest binary position in \(a-1\). We show that every position \(1,\ldots,h\) must be present.

Otherwise take the smallest omitted \(j\) with \(1\le j<h\). Then all positions \(1,\ldots,j-1\) are present, and \(h\ge j+1\), so \(a+1\ge 2^h+2>2^j\). Set \(M=2^{2^j+1}\) and \(P=\prod_{i=1}^{j-1}F_i\) (an empty product is one). Every factor \(F_i\) with \(i>j\) is \(1\pmod M\). Thus (1) would imply
\[
B\equiv P\pmod M.\tag{2}
\]
On the other hand, the Fermat product identity gives
\[
3PF_j=\prod_{i=0}^{j}F_i=2^{2^{j+1}}-1,
\]
so \(PF_j\equiv-3^{-1}\pmod M\). Since \(a+1\ge 2^j+1\), the formula for \(B\) gives \(B\equiv-3^{-1}\pmod M\). But \(F_j=1+2^{2^j}\) and \(P\) is odd; hence
\[
PF_j-P=P\,2^{2^j}\not\equiv0\pmod{2^{2^j+1}}.
\]
This contradicts (2). Thus no binary position \(1,\ldots,h\) can be missing, and
\[
a-1=2+4+\cdots+2^h=2^{h+1}-2,
\qquad a=2^{h+1}-1.
\]
Consequently every odd-exponent solution has \(a=2^k-1\) for some \(k\ge1\).

**Step 5: exact finite elimination and sufficiency.** If \(a=2^k-1\), then the Fermat product identity yields
\[
\beta(2^a)=\frac{2^{2^k}-1}{3}=\prod_{j=1}^{k-1}F_j.
\]
The factorization criterion from Step 1 holds precisely when all of \(F_1,\ldots,F_{k-1}\) are prime: the Fermat numbers are pairwise coprime, and no composite Fermat number can split into prime Fermat numbers with other indices. The numbers \(F_1=5\), \(F_2=17\), \(F_3=257\), and \(F_4=65537\) are prime; \(F_5=4294967297=641\cdot6700417\) is composite. Thus exactly \(k\in\{1,2,3,4,5\}\) work. Combined with the even case \(a=2\), these are precisely the six asserted exponents. \(\square\)

## Verification
The standalone Python standard-library checker `verify.py` tests the values for all \(1\le a\le24\), checks the five needed Fermat primalities by trial division, verifies the factorization of \(F_5\), checks the valuation lemma on 144 example pairs, and exercises the missing-digit congruence on 113 odd exponents and the even-exponent congruence on 99 exponents. Expected output begins `VERIFY_OK`. The infinite classification is proved by Steps 1–5; no finite computation substitutes for it.

## Relationship to prior work
Tóth's archival survey (arXiv:1111.4842, publicly posted 2011-11-21; 2014 revision) introduces the super-imperfect condition as Problem 1, and proves exactly which integers of the special form \(2^{2^k-1}\) qualify (Section 7 proposition and Section 8 proof). That result does **not** rule out all other powers \(2^a\). The present additional converse uses the binary digits of \(a-1\), a prime-power obstruction for odd arguments of \(\beta\), and a congruence modulo sixteen. OEIS A200758 lists the same six known super-imperfect numbers and repeats Tóth's special-family theorem, but does not provide this unrestricted classification within the powers-of-two family. Thus the new mathematical statement is exclusion of **every other exponent** \(a\ge1\), not rediscovery of the six listed examples.

## Limitations
This settles only the powers-of-two subfamily of the open problem; other even or odd super-imperfect numbers may exist. The originality comparison is based on inspected primary full text, the cited sequence entry, available indexed research summaries and targeted literature searches; unindexed or inaccessible equivalent work remains possible. All proof steps are elementary; the independent audit has not been performed.

## References
1. László Tóth, *A survey of the alternating sum-of-divisors function*, arXiv:1111.4842v1 (2011-11-21), revised v2 (2014-01-27), Section 7, Proposition and Problem 1; Section 8, proof. https://arxiv.org/abs/1111.4842 ; https://arxiv.org/pdf/1111.4842
2. OEIS Foundation, A200758, *Superimperfect numbers*, entry and comments. https://oeis.org/A200758
3. Chris Caldwell, *Fermat numbers*, The Prime Glossary, for background on the Fermat-number family. https://t5k.org/glossary/page.php?sort=FermatNumber
