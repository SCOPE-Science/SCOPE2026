# Exact reflection complexity of the increasing-run binary word

## Finding
For the infinite binary word
\[W=0^1 1^1 0^2 1^2 0^3 1^3\cdots=010011000111\cdots,\]
write \(\mathcal L_n(W)\) for its set of distinct contiguous length-\(n\) factors. Let \(p_W(n)=|\mathcal L_n(W)|\) and let \(r_W(n)\) be the number of equivalence classes under word reversal within \(\mathcal L_n(W)\). For every integer \(n\ge1\),
\[p_W(n)=\frac{n(n+1)}2+1,\qquad r_W(n)=\left\lceil\frac{n(n+1)}3\right\rceil+1.\]
In particular, \(W\) is aperiodic and
\[\lim_{n\to\infty}\frac{r_W(n)}{p_W(n)}=\frac23.\]
This furnishes a counterexample even after adding an aperiodicity hypothesis to the limit dichotomy in Conjecture 29 of Allouche, Campbell, Li, Shallit, and Stipulanti. The literal conjecture, without aperiodicity, already has a known periodic counterexample [2].

## Assumptions and scope
The alphabet is \(\{0,1\}\); the exponent notation \(0^k\) denotes a run of exactly \(k\) zeros, likewise for ones. The infinite word has alternating complete runs \(0^k\) then \(1^k\), for all \(k=1,2,\ldots\). Reflection equivalence means \(u\sim v\) exactly when \(u=v\) or \(u\) is the reverse of \(v\); a factor need not have its reverse in the language. Factor lengths are positive integers. The word is not recurrent: the length-three factor `010` appears only at the very beginning. Only the full language, not a different suffix language, is considered. The source's primary subject classification is 68R15.

## Proof
**1. Factor complexity.** Write a *change* for adjacent unequal symbols. Each complete run of \(W\), specifying both its symbol and its length, occurs exactly once. Thus a factor having at least two changes contains a complete internal run and has a unique occurrence; in particular, it cannot have two different right extensions.

Both constant words \(0^n\) and \(1^n\) are right-special: sufficiently long runs supply an extension by the same symbol, and a run endpoint supplies an extension by the other symbol. For \(a,b\ge1\), a factor \(0^a1^b\), with \(a+b=n\), is right-special if and only if \(a\le b\). Indeed, a right-extension by zero is possible just when the \(1\)-run has length \(b\) and the preceding \(0\)-run has sufficient length \(a\); and a right-extension by one always occurs in later, longer runs. Similarly, \(1^a0^b\) is right-special exactly when \(a<b\): a \(0\)-run of length \(b\) is preceded by a \(1\)-run of length \(b-1\). These alternatives exhaust all right-special factors, since two or more changes make a factor unique. Consequently the number of right-special length-\(n\) factors is
\[2+\left\lfloor\frac n2\right\rfloor+\left\lfloor\frac{n-1}2\right\rfloor=n+1.\]
Because the alphabet is binary and every factor has at least one right-extension, the right-special count is precisely \(p_W(n+1)-p_W(n)\). Starting with \(p_W(1)=2\) proves \(p_W(n)=n(n+1)/2+1\).

**2. Which factors have reverses?** Any factor with at least three changes has at least two complete adjacent interior runs. In \(W\), their lengths are nondecreasing. If the reverse factor also occurred, reversing the same list would force these interior lengths to be nonincreasing. Hence they must all be equal. The only adjacent equal-length complete runs in \(W\) are \(0^k1^k\); their reverse \(1^k0^k\) cannot appear as adjacent complete runs, since \(1^k\) is followed by \(0^{k+1}\). Thus a factor with three or more changes never occurs together with its reversal, even when the factor itself appears only once.

Constant factors are palindromes. For factors with one change, all \(0^a1^b\) and \(1^b0^a\) occur for positive \(a,b\), giving exactly \(n-1\) nontrivial reversal pairs of length \(n\). For factors with precisely two changes, \(0^a1^k0^b\), where \(a,b,k\ge1\), occurs precisely when \(a\le k\) and \(b\le k+1\); its reversal also occurs precisely when \(a,b\le k\). The analogous word \(1^a0^k1^b\) occurs precisely when \(a\le k-1\) and \(b\le k\), and both orientations occur precisely when \(a,b\le k-1\). Palindromes have \(a=b\) and contribute no reduction in the count of reversal classes. Every nonpalindromic two-change pair is uniquely counted by \(a<b\).

Set \(T(m)=\#\{(a,b)\in\mathbb{Z}^2:1\le a<b,\ a+2b\le m\}\). The first type contributes \(T(n)\) distinct two-change reversal pairs; the second contributes \(T(n-1)\). Each nontrivial reversal pair reduces the number of reflection classes by one. Therefore
\[p_W(n)-r_W(n)=(n-1)+T(n)+T(n-1).\]

**3. Exact pair enumeration.** Substituting \(b=a+1+t\) with \(a\ge1\) and \(t\ge0\) gives the ordinary generating function
\[\sum_{m\ge0}T(m)z^m=\frac{z^5}{(1-z)(1-z^2)(1-z^3)}.\]
Hence, interpreting the left side at \(n=0\) as zero,
\[\sum_{n\ge0}\big((n-1)_++T(n)+T(n-1)\big)z^n
=\frac{z^2}{(1-z)^2}+\frac{z^5(1+z)}{(1-z)(1-z^2)(1-z^3)}
=\frac{z^2}{(1-z)^2(1-z^3)}.\]
The coefficient of \(z^n\) in the last expression is \(\lfloor n(n+1)/6\rfloor\): its successive coefficient differences are \(\lfloor(n+2)/3\rfloor\), starting from zero. Thus
\[p_W(n)-r_W(n)=\left\lfloor\frac{n(n+1)}6\right\rfloor.\]
Substituting the factor-complexity formula yields
\[r_W(n)=\frac{n(n+1)}2+1-\left\lfloor\frac{n(n+1)}6\right\rfloor=\left\lceil\frac{n(n+1)}3\right\rceil+1,\]
where the final equality follows because \(n(n+1)\) is even.

**4. Aperiodicity and limit.** There are arbitrarily long runs of both letters. An eventually periodic word containing infinitely many occurrences of both letters has a bounded run length after its preperiod. Thus \(W\) is not eventually periodic. Taking the quotient of the exact quadratic formulas gives \(2/3\).

## Verification
Run `python3 verify_run_reflection.py` with the Python standard library. It enumerates every factor and reversal orbit at lengths \(1\) through \(140\) from finite prefixes containing all possible length-\(n\) factors; it independently checks the precise right-special sets through length \(85\) and the generating-function coefficient identity through length \(1000\). The expected printed line is:

`VERIFY_OK n=1..140 exact-factors/reversal-orbits n=1..85 right-special-sets n=1..1000 arithmetic-identity`

The finite checks corroborate the statements; the unrestricted quantifiers rest on the preceding combinatorial proof.

## Relationship to prior work
Allouche--Campbell--Li--Shallit--Stipulanti [1, Conjecture 29] propose that whenever \(\lim r(n)/p(n)\) exists it belongs to \(\{1/2,1\}\). Dvořáková--Pelantová [2, Section 6] point out a periodic counterexample with limit \(2/3\) and explain valid positive cases with aperiodicity *and a language closed under reversal*. The present word is aperiodic and its language is not reversal-closed, so neither their periodic example nor their reversal-closed positive theorem covers the precise present construction. This result does not reassert priority over the already-known periodic disproof: its additional contribution is an exact aperiodic binary example disproving the natural aperiodic repair, with all-length factor and reflection formulas.

## Limitations
The counterexample is not uniformly recurrent, its language is not reversal-closed, and no claim is made about analogous ratios for uniformly recurrent or reversal-closed sequences. A finite verifier cannot certify the all-length assertions independently of the proof. Publication-priority uncertainty remains for unindexed equivalent descriptions of this increasing-run word. Independent validation has not been performed.

## References
[1] J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302, first posted 2024-06-13, Conjecture 29; https://arxiv.org/abs/2406.09302 .

[2] L. Dvořáková, E. Pelantová, *Reflection on the Reflection Complexity*, *Theory of Computing Systems* 70, article 35 (2026), Section 6, https://doi.org/10.1007/s00224-026-10278-7 .
