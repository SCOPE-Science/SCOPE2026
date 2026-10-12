# First branching of odd-prime completions for strongly pseudoperfect binary supports

## Finding

Call a positive integer \(N\) *strongly pseudoperfect* when a set \(S\) of positive divisors of \(N\) is closed under \(d\mapsto N/d\) and satisfies \(\sum_{d\in S}d=2N\). For every integer \(a\ge1\), let
\[
P_a=\{p:p\text{ is an odd prime and }2^a p\text{ is strongly pseudoperfect}\}.
\]
The first exponent having at least two distinct prime completions is exactly \(a=9\), and
\[
P_9=\{23,179\}.
\]
The complete initial profile is
\[
(P_1,P_2,\ldots,P_9)
=(\{3\},\{7\},\varnothing,\{31\},\{11\},\{127\},\varnothing,\varnothing,\{23,179\}).
\]
The two initial branches are not merely repeated witnesses of the same number. At \(a=9\), the completion \(p=179\) has a witness formed from all ten reciprocal divisor pairs except one; the completion \(p=23\) has a witness omitting precisely two pairs.

## Assumptions and scope

Throughout, \(p\) is an odd prime and \(a\) is a positive integer, so the divisors of \(N=2^ap\) are precisely \(2^i\) and \(2^i p\) for \(0\le i\le a\). A *prime completion* is a distinct prime \(p\), not a count of witness subsets. The assertion of first occurrence is global in all preceding exponents, but only uses a finite exact exhaustive calculation at \(1\le a\le9\); it does not describe the later prime-completion counts.

## Proof

Write \(M=2^{a+1}\). Because the reciprocal involution pairs \(2^i\) with \(2^{a-i}p\), any reciprocal-closed divisor subset is uniquely determined by binary choices \(\epsilon_i\in\{0,1\}\) for \(0\le i\le a\). Define
\[
x=\sum_{i=0}^a\epsilon_i2^i,\qquad
y=\sum_{i=0}^a\epsilon_i2^{a-i}.
\]
The selected divisor sum is \(x+py\), whereas twice the number is \(Mp\). Thus strong pseudoperfectness is exactly
\[
x+py=Mp.
\]
The reverse-digit identity \(y=\operatorname{rev}_{a+1}(x)\) is an equality of integers, where the reversal includes all \(a+1\) bits. Since \(0\le y\le M-1\), its denominator \(M-y\) is always positive, and the equation has the unique possible completion
\[
p=\frac{x}{M-\operatorname{rev}_{a+1}(x)}.
\]
For a positive sum, \(x\ge1\); also \(x\le M-1\), so \(3\le p\le M-1\) whenever the completion is an odd prime. Conversely, every integral odd-prime value of this fraction produces a reciprocal-closed divisor witness by selecting the corresponding pairs. This is a necessary-and-sufficient characterization with no hidden completeness assumption.

It therefore suffices, for each \(1\le a\le9\), to test every integer \(1\le x<2^{a+1}\), reverse its \(a+1\)-bit expansion, test the single exact divisibility relation, and recognize prime completions by a deterministic sieve to \(2^{a+1}-1\). The complete resulting table is:

| \(a\) | All qualifying odd primes \(p\) |
|---:|:---|
| \(1\) | \(3\) |
| \(2\) | \(7\) |
| \(3\) | none |
| \(4\) | \(31\) |
| \(5\) | \(11\) |
| \(6\) | \(127\) |
| \(7\) | none |
| \(8\) | none |
| \(9\) | \(23,179\) |

A second exact enumeration does not use digit reversal: for each prime \(3\le p<2^{a+1}\), it constructs the subset-sum generating product
\[
\prod_{i=0}^a\left(1+T^{2^i+2^{a-i}p}\right)
\]
and tests whether its coefficient of \(T^{2^{a+1}p}\) is positive. Both independently specified exact algorithms give the same table.

For explicit witnesses at \(a=9\), with \(M=1024\), take \(x=895\) for \(p=179\). Its ten-bit set of ones is
\[
I_{179}=\{0,1,2,3,4,5,6,8,9\},
\]
so exactly the index \(7\) is omitted. Here \(\operatorname{rev}_{10}(895)=1019\) and \(895/(1024-1019)=179\). For \(p=23\), choose \(x=943\), with
\[
I_{23}=\{0,1,2,3,5,7,8,9\},
\]
so indices \(4,6\) are omitted. Now \(\operatorname{rev}_{10}(943)=983\) and \(943/(1024-983)=23\). In each case the witness is explicitly
\[
S_p=\bigcup_{i\in I_p}\{2^i,\,2^{9-i}p\}.
\]
The two sets contain only divisors of \(2^9p\), are closed under complement divisors, and satisfy the required exact sum \(2^{10}p\). Since the table exhausts every smaller exponent, the first branching exponent is \(9\).

## Verification

The included standalone standard-library verifier `artifacts/verify.py` implements two independent finite decision procedures: quotient enumeration over all binary masks and direct dynamic-programming subset sums over every possible odd prime and exponent \(1\le a\le9\). It checks the complete table, recomputes the explicit reciprocal-pair witnesses, confirms primality by a deterministic sieve, and verifies each witness sum and involutive closure using exact integers. The saved replay in `artifacts/replay.txt` contains the success marker. The finite enumeration proves the first-occurrence assertion because a closed-form lemma supplies an exhaustive bounded domain.

## Relationship to prior work

Wang and Zelinsky's *Strongly Pseudoperfect Numbers* (arXiv:2609.36068) develops new families and restrictions for the same symmetric-divisor notion. The earlier paper of Aryan, Madhavani, Parikh, Slattery, and Zelinsky studies the narrower strongly \(2\)-near-perfect property, under which only one reciprocal divisor pair may be omitted. Its Proposition 5 already covers the \(p=179\) branch at exponent \(9\); it does not cover \(p=23\), which needs two omitted pairs, nor certify that no earlier exponent has two distinct prime completions. OEIS A334405 includes the single value \(11776=2^9\cdot23\) in its published list through \(30324\), but does not provide a complete list to the necessary global cutoff \(2^9(2^{10}-1)\). The present finding is the first-exponent, complete-fiber statement, not a claim that either individual known integer was newly discovered.

## Limitations

The result does not classify all exponents beyond \(9\), give an asymptotic for the number of prime completions, or establish infinite multiplicity. The full text of the recent Wang–Zelinsky preprint could not be retrieved during the literature check; only the publication metadata and abstract were accessible. This creates a residual risk of an unindexed prior discussion of the same first-branching invariant, which the available exact-claim searches did not reveal. An independent review has not been performed.

## References

1. Audrey Wang and Joshua Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068v1 (first public version 2026-09-28).
2. V. Aryan, D. Madhavani, S. Parikh, I. Slattery, and J. Zelinsky, *On 2-Near Perfect Numbers*, INTEGERS 24 (2024), A61, especially Section 4 and Table 3, DOI:10.5281/zenodo.12167628.
3. OEIS A334405, *Strongly pseudoperfect numbers*, especially its b-file through the value \(30324\), checked October 2026.
