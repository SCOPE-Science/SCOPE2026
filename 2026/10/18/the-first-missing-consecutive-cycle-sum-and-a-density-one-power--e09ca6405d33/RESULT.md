# The first missing consecutive-cycle sum and a density-one power-of-two law

## Finding
Label the cycle of length \(n\) consecutively by \(1,2,\ldots,n\) in cyclic order. A connected vertex-set sum is the sum of a nonempty cyclic interval, including the full cycle. Write \(T_n=n(n+1)/2\), and let \(\mu(n)\) be the smallest integer in \([1,T_n]\) that is **not** such a sum. Existence for \(n\ge8\) follows from Marotti–Needleman's incompleteness theorem.

Put \(P(n)=2^{1+\lfloor\log_2 n\rfloor}\), the least power of two strictly greater than \(n\). For every \(n\ge8\),

\[
\mu(n)=P(n)\quad\Longleftrightarrow\quad n\ne 2^r\ (r\in\mathbb Z_{\ge0})\ \text{and}\ P(n)-n\notin\{j(j+1)/2:j\ge1\}.
\]

In every other case \(\mu(n)>P(n)\). Define \(E(X)=\#\{8\le n\le X:\mu(n)>P(n)\}\). Then \(E(X)=O(\sqrt X)\), so the first missing sum equals the next power of two for natural density one of all integers \(n\). At dyadic endpoints, for every integer \(M\ge4\),

\[
E(2^M)=M-2+\sum_{m=4}^M\left\lfloor\frac{\sqrt{2^{m+2}-7}-1}{2}\right\rfloor
=(2+\sqrt2)2^{M/2}+O(M).
\]

## Assumptions and scope
All vertices have their positive integer labels in increasing cyclic order, not in an arbitrary permutation. Connected subsets can wrap across the edge joining labels \(n\) and \(1\). Powers of two in the definition of \(P(n)\) are **strictly above** \(n\). The smallest missing value is sought only in \([1,T_n]\). The statements apply for \(n\ge8\) and do not assert an explicit formula for \(\mu(n)\) in the exceptional cases.

## Proof
**Consecutive-sum lemma.** Every positive integer other than a power of two is a sum of at least two consecutive positive integers. Indeed, write \(s=2^eu\) with odd \(u>1\). If \(u\le2^{e+1}\), take \(u\) terms centered at \(2^e\), starting at \(2^e-(u-1)/2\ge1\). Otherwise take \(2^{e+1}\) terms beginning at \((u-2^{e+1}+1)/2\ge1\). Their sums are \(s\). Conversely, an odd number of at least three consecutive positive integers has a nontrivial odd divisor (its length), and a positive even number of consecutive integers has the form \(d(2a+2d-1)\) with an odd factor at least three. Hence no power of two has such a representation.

If a sum of at least two positive consecutive integers equals \(s\) and has last entry \(b\), its last two entries sum to \(2b-1\), so \(b\le(s+1)/2\). For \(s\le2n\), necessarily \(b\le n\), and the representation uses a standard (nonwrapping) arc of the labeled cycle. In addition, powers of two at most \(n\) are singleton-arc sums. Since every positive integer below \(P(n)\) is either a power of two at most \(n\) or a non-power of two at most \(2n\), **every value below \(P(n)\) is represented**.

The value \(P(n)\) itself is a power of two exceeding \(n\); it is neither a singleton sum nor a nonwrapping sum of length at least two. If \(n\) is a power of two, \(P(n)=2n\), and the wrapping arc \(\{n-1,n,1\}\) has sum \(2n\). If \(n\) is not a power of two, \(n<P(n)<2n\). A wrapping arc contains both \(n\) and \(1\). If it also includes \(n-1\), its sum is at least \(2n\), too large. Thus a wrapping arc with sum \(P(n)\) must consist exactly of \(n\) and an initial prefix \(1,\ldots,j\), for some \(j\ge1\); its sum is \(n+j(j+1)/2\). Conversely, when \(P(n)-n=j(j+1)/2\), the inequality \(P(n)-n<n\) ensures \(j\le n-2\) for \(n\ge8\), giving such a proper wrapping arc. This proves the exact first-gap characterization, using the aforementioned existence of at least one missing sum.

For the exceptional-count formula, partition integers into dyadic blocks \(2^{m-1}<n<2^m\) and their power-of-two endpoints. Within the block \(P(n)=2^m\). For each triangular \(T_j=j(j+1)/2\) with \(1\le T_j<2^{m-1}\) there is exactly one exceptional \(n=2^m-T_j\). The number of these \(j\) is \(\left\lfloor(\sqrt{2^{m+2}-7}-1)/2\right\rfloor\). The endpoints \(8,16,\ldots,2^M\) contribute \(M-2\). This proves the exact formula. Each block contributes \(2^{m/2}+O(1)\) exceptions, so summing the geometric progression gives \((2+\sqrt2)2^{M/2}+O(M)\) and also \(E(X)=O(\sqrt X)\) for arbitrary \(X\).

## Verification
A standalone Python script, `verify.py`, independently constructs all cyclic interval sums, checks the first-gap criterion for every \(8\le n\le256\), and tests the exact exception count at dyadic endpoints through \(256\). The infinite result follows from the proof, not this finite check.

## Relationship to prior work
Marotti and Needleman prove that the naturally labeled consecutive-sum cycle is not sum-complete for \(n\ge8\), provide constructions of represented values, and ask for finer descriptions of the representable sums. The classical consecutive-integer characterization, often attributed to Sylvester, controls all nonwrapping arcs up to twice the cycle length. The new classification additionally handles the wrapping arcs at the first possible gap and counts the exceptional cycle orders with square-root accuracy.

## Limitations
The theorem classifies when the **first** gap occurs at \(P(n)\), not the first missing value in exceptional cases, the complete set of missing values, or arbitrary reorderings of the labels. Its originality remains subject to the possibility of an earlier unindexed or implicit derivation from standard consecutive-sum theory.

## References
1. J. Marotti and J. Needleman, *Consecutive Cycle Sums*, arXiv:2610.08889v1 (first publicly posted 2026-10-06), https://arxiv.org/abs/2610.08889.
2. J. J. Sylvester, classical characterization of sums of consecutive positive integers, as described and referenced in Marotti–Needleman, Section 2.
