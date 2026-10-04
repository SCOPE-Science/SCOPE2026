# The first multi-pair strongly pseudoperfect number of the form \(2^a p\)
## Finding
For \(a\ge1\) and an odd prime \(p\), set
\[
n=2^a p,\qquad M=2^{a+1}-1.
\]
For a subset \(I\subseteq\{0,\ldots,a\}\), define
\[
A_I=\sum_{i\in I}2^i,\qquad B_I=\sum_{i\in I}2^{a-i}.
\]
The complementary divisor pairs of \(n\) are
\[
(2^i,p2^{a-i})\qquad(0\le i\le a).
\]
Then \(n\) has a strongly pseudoperfect representation omitting exactly the pairs indexed by \(I\) if and only if
\[
p=\frac{M-A_I}{1+B_I}.
\]

This gives an exact finite binary criterion for the two-prime-support slice with odd-prime exponent one. Applying it at the bottom of the slice gives a sharp transition: the least nonperfect strongly pseudoperfect integer of the form \(2^a p\) whose representations require at least two omitted complementary divisor pairs is
\[
11776=2^9\cdot23.
\]
It has exactly one strongly pseudoperfect representation, with omitted pairs
\[
(16,736),\qquad(64,184).
\]
Equivalently, the omitted divisors are \(16,64,184,736\). Their sum is \(1000\), while \(\sigma(11776)=24552\), so the retained divisors sum to \(24552-1000=23552=2\cdot11776\).

Below \(11776\), the complete list of strongly pseudoperfect integers of the form \(2^a p\) is
\[
6,\ 28,\ 352,\ 496,\ 8128.
\]
The four values other than \(352\) are perfect. The number \(352=2^5\cdot11\) has a unique nonperfect representation and omits the single complementary pair \((8,44)\).

## Assumptions and scope
Here \(a\ge1\), \(p\) is an odd prime, and “strongly pseudoperfect” means that a subset \(S\) of the positive divisors of \(n\) satisfies both \(d\in S\iff n/d\in S\) and \(\sum_{d\in S}d=2n\). Thus every representation is a union of complementary divisor pairs. The cutoff statement concerns only integers with exactly two prime supports and odd-prime exponent one, namely \(2^a p\).

The literature anchor is Wang and Zelinsky's 2026 study of strongly pseudoperfect numbers. It gives the definition, lists \(352\) with the unique omitted pair \((8,44)\), and proves a Mersenne-prime rigidity theorem for the same \(2^k p\) shape. Aryan--Madhavani--Parikh--Slattery--Zelinsky (2024) separately classify the strongly 2-near-perfect subcase \(2^k p\), i.e. exactly one omitted complementary pair. The cutoff above identifies the first point where this one-pair regime is genuinely left.

## Proof
Because \(p\) is odd, the positive divisors of \(n=2^a p\) split into the \(a+1\) disjoint complementary pairs
\[
(2^i,p2^{a-i}),\qquad 0\le i\le a.
\]
A strongly pseudoperfect representation is therefore determined by the set \(I\) of omitted pairs. The total divisor sum is
\[
\sigma(n)=(2^{a+1}-1)(p+1)=M(p+1).
\]
If the pairs indexed by \(I\) are omitted, their total sum is
\[
\sum_{i\in I}(2^i+p2^{a-i})=A_I+pB_I.
\]
The retained divisors sum to \(2n=2^{a+1}p=(M+1)p\) exactly when
\[
M(p+1)-(A_I+pB_I)=(M+1)p.
\]
Cancelling and rearranging gives
\[
M-A_I=p(1+B_I),
\]
which is equivalent to
\[
p=\frac{M-A_I}{1+B_I}.
\]
Every step is reversible, proving the criterion.

For the cutoff, if \(2^a p\le11776\) and \(p\ge3\), then \(a\le11\). Hence every candidate is covered by the finite set of masks \(I\subseteq\{0,\ldots,a\}\) for \(1\le a\le11\), together with the single boundary case \((a,p)=(9,23)\). Exact integer enumeration of the criterion gives precisely
\[
(2^a p,I)=(6,\varnothing),(28,\varnothing),(352,\{3\}),(496,\varnothing),(8128,\varnothing),(11776,\{4,6\}).
\]
For \(I=\varnothing\), the criterion says \(p=2^{a+1}-1\), so those four cases are the standard even perfect numbers. The only nonperfect case below the boundary is \(352\), with one omitted pair. At the boundary, \(11776\) has only the mask \(I=\{4,6\}\), so its representation is unique and omits exactly two pairs. This proves the minimality and uniqueness statements.

## Verification
The accompanying `verify.py` uses only exact integer arithmetic and deterministic trial-division primality testing. It enumerates every mask for every \(1\le a\le11\), derives the only possible \(p\) from the criterion, filters to odd primes and \(2^a p\le11776\), and independently checks each retained divisor sum. It also separately enumerates all masks for \((a,p)=(9,23)\) to certify uniqueness. The expected terminal line is `VERIFY_OK candidates=6 boundary_representations=1`.

The exhaustive range is mathematically complete for the cutoff: \(a\ge12\) implies \(2^a p\ge3\cdot2^{12}=12288>11776\).

## Relationship to prior work
Wang and Zelinsky, *Strongly Pseudoperfect Numbers* (arXiv:2609.36068v1, 2026), define the paired-divisor condition, list \(352\) with its unique omitted pair \((8,44)\), and prove that if a strongly pseudoperfect number has shape \(2^k p\) with \(p\) Mersenne prime, then it is perfect. Their displayed table of the first even examples stops before \(11776\), and the paper does not state the cutoff or the general binary-mask criterion used here.

Aryan, Madhavani, Parikh, Slattery, and Zelinsky, *On 2-near perfect numbers* (INTEGERS 24 (2024), A61), classify strongly 2-near-perfect numbers of shape \(2^k p\). That result covers the one-pair case, including \(352\), but not representations omitting two or more complementary pairs. In particular, it does not imply the \(11776\) two-pair cutoff.

Targeted searches for the exact number, the \(2^a p\) two-pair cutoff, binary-mask formulations, and the pair \(352,11776\) found no prior statement of the theorem. Nearby database results concern other two-prime divisor-sum notions rather than strongly pseudoperfect paired representations.

## Limitations
The binary criterion is exact but does not give a closed-form classification for all \(a\): primality of the resulting quotient can remain difficult. The cutoff is only for the slice \(2^a p\) with \(p\) an odd prime; it says nothing about more general even strongly pseudoperfect numbers such as those with several odd prime factors or a higher power of the odd prime. The literature search cannot exclude unindexed or differently phrased prior observations.

## References
1. Audrey Wang and Joshua Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068v1 (2026), https://arxiv.org/abs/2609.36068.
2. Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery, and Joshua Zelinsky, *On 2-near perfect numbers*, INTEGERS 24 (2024), A61, DOI 10.5281/zenodo.12167628, https://math.colgate.edu/~integers/y61/y61.pdf.
