# A binary-gap rank bound for two-prime Egyptian fractions
## Finding
Let \(p\) be any odd prime. Suppose positive integers \(x_1,\ldots,x_R\) satisfy
\[
1=\sum_{i=1}^R \frac{1}{x_i},
\]
every prime divisor of every \(x_i\) lies in \(\{2,p\}\), and both \(2\) and \(p\) divide at least one denominator. Then
\[
R\ge \lfloor \log_2 p\rfloor+2.
\]
This is strictly stronger than the lower bound \(R\ge \ln(2p)\) asked for in Question 5.3 of Czenky--McGovern--Plavnik--Rowell--Watkins. The bound is attained whenever \(p=2^{2^n}+1\) is prime, so on every Fermat-prime support the minimum rank is exactly \(2^n+2\).

## Assumptions and scope
The notion of a solution is that of Definition 2.1 of the cited paper: denominators may repeat, each denominator has the form \(2^a p^b\) with nonnegative integer exponents, and each of the two primes appears in at least one denominator. No squarefreeness or bound on the exponents is assumed. The proof applies to every odd prime \(p\). It concerns the minimum possible rank, not the number of solutions or their largest denominator.

## Proof
Let \(r\) be the number of terms whose denominator is not divisible by \(p\). These denominators are pure powers of \(2\). Put
\[
S=\sum_{p\nmid x_i}\frac1{x_i}.
\]
Because at least one denominator is divisible by \(p\), positivity gives \(S<1\).

We first use a dyadic gap lemma: if \(S\) is a sum of \(r\) reciprocals of powers of \(2\) and \(S<1\), then
\[
1-S\ge 2^{-r}.
\]
For \(r=0\) this is immediate. Otherwise write the \(r\) terms as \(2^{-a_j}\), take \(A=\max_j a_j\), and set \(N=2^A S\). Then \(N\) is an integer with \(0\le N<2^A\). Before carrying, \(N\) is represented as a sum of \(r\) powers of \(2\); binary carrying cannot increase the number of nonzero binary digits. Hence the binary popcount of \(N\) is at most \(r\). If \(r\le A\), the largest integer below \(2^A\) with at most \(r\) nonzero binary digits is
\[
2^{A-1}+2^{A-2}+\cdots+2^{A-r}=2^A-2^{A-r},
\]
so \(1-S\ge2^{-r}\). If \(r>A\), then \(N\le2^A-1\), giving \(1-S\ge2^{-A}>2^{-r}\). This proves the lemma.

There are \(R-r\) remaining terms, and each has denominator divisible by \(p\), so each reciprocal is at most \(1/p\). Therefore
\[
2^{-r}\le1-S=\sum_{p\mid x_i}\frac1{x_i}\le\frac{R-r}{p}.
\]
Since \(R-r\) is an integer,
\[
R\ge r+\left\lceil\frac{p}{2^r}\right\rceil. \tag{1}
\]
Let \(k=\lfloor\log_2 p\rfloor\), so \(2^k<p<2^{k+1}\). If \(r\ge k+1\), the right side of (1) is at least \(k+2\). If \(r=k\), then \(1<p/2^k<2\), so (1) again gives \(R\ge k+2\). Finally, if \(r\le k-1\), write \(d=k-r\ge1\). Since \(p/2^r>2^d\),
\[
\left\lceil\frac p{2^r}\right\rceil\ge2^d+1,
\]
and hence
\[
R\ge k-d+2^d+1=k+1+(2^d-d)\ge k+2.
\]
Thus \(R\ge\lfloor\log_2p\rfloor+2\).

For comparison, \(\lfloor\log_2p\rfloor+2>\log_2(2p)>\ln(2p)\) for \(p>1\), so the requested natural-logarithmic lower bound follows strictly.

For sharpness, let \(p=2^k+1\) be a Fermat prime, where \(k=2^n\). Then
\[
1=\sum_{j=1}^k\frac1{2^j}+\frac1p+\frac1{2^k p}.
\]
Indeed, the dyadic sum is \(1-2^{-k}\), while the last two terms sum to \(2^{-k}\). This gives a rank \(k+2=2^n+2\) solution, matching the lower bound.

## Verification
The accompanying `verify_rank_bound.py` uses exact integer and rational arithmetic. It checks the discrete inequality behind (1) over a broad finite range, verifies the rank lower bound against every prime/rank pair in Table 4 of the cited paper, exhaustively checks the dyadic gap lemma for small multisets, and verifies the Fermat-support identity for the five known Fermat primes. These finite checks are sanity tests only; the infinite statement is established by the proof above.

## Relationship to prior work
Czenky, McGovern, Plavnik, Rowell and Watkins tabulate the lowest observed ranks for supports \(\{2,p\}\), fit logarithmic growth numerically, and explicitly ask in Question 5.3 whether \(\ln(p)\), or even \(\ln(2p)\), can be proved as a lower bound and improved. Their Proposition 4.5 supplies explicit Fermat-prime constructions, including the base-rank identity used above for the known Fermat primes. The binary-gap argument proves a stronger universal lower bound and, combined with the explicit identity, turns those Fermat-prime constructions into exact minimum-rank statements.

Targeted searches using the paper's terminology, the equivalent two-prime-support formulation, and the explicit bound found no checked source stating \(R\ge\lfloor\log_2p\rfloor+2\) or an implication that yields it. This is evidence relative to the inspected literature, not a claim that every publication or unpublished manuscript has been exhaustively searched.

## Limitations
The theorem treats supports \(\{2,p\}\). It does not establish an analogous bound for arbitrary odd-prime pairs \(\{p,q\}\), which is the second part of Question 5.3. Equality is proved for Fermat-prime supports; the equality cases for general \(p\) are not classified. Independent audit has not been performed.

## References
1. A. Czenky, E. McGovern, J. Plavnik, E. C. Rowell, and A. Watkins, *Egyptian fractions for few primes*, arXiv:2507.03727v1, 4 July 2025. Relevant items: Definition 2.1, Table 4, Proposition 4.5, Question 5.3.
2. P. Bruillard and E. C. Rowell, *Modular categories, integrality and Egyptian fractions*, Proceedings of the American Mathematical Society 140 (2012), 1141--1150; arXiv:1012.0814. Background motivation for restricted Egyptian-fraction problems.
