# Exact Zumkeller partition multiplicity in the upper two-prime strip
## Finding
Let \(a\ge 1\), let \(p\) be an odd prime satisfying
\[
2^a<p\le 2^{a+1}-1,
\]
and let \(b\ge 1\) be odd. For \(n=2^a p^b\), the number of unordered partitions of the divisor set of \(n\) into two complementary subsets having the same sum is exactly
\[
2^{(b-1)/2}.
\]

A partition here is unordered: interchanging its two blocks does not create a new partition.

## Assumptions and scope
Write \(S=2^{a+1}-1\). The divisors of \(n\) are \(2^i p^j\) with \(0\le i\le a\) and \(0\le j\le b\). The hypothesis \(2^a<p\le S\) is the upper half of the known two-prime-support Zumkeller range. The result counts all equal-sum divisor bipartitions in this strip; it does not assert the same formula when \(p\le 2^a\).

## Proof
First orient a partition by naming its blocks \(A\) and \(B\). For each \(j\in\{0,\ldots,b\}\), let \(x_j\) be the sum of those powers \(2^i\), \(0\le i\le a\), for which \(2^i p^j\in A\). Every integer in \(0,1,\ldots,S\) has a unique binary representation using the powers \(1,2,\ldots,2^a\), so choosing the divisors of \(A\) at level \(p^j\) is equivalent to choosing one integer \(x_j\in[0,S]\).

Set \(y_j=2x_j-S\). Then each \(y_j\) is odd and satisfies \(|y_j|\le S\). Equality of the two block sums is equivalent to
\[
\sum_{j=0}^b y_j p^j=0.
\]
Conversely, every vector of odd integers \(y_j\) in \([-S,S]\) satisfying this equation determines one oriented equal-sum partition, because \(x_j=(S+y_j)/2\) is an integer in \([0,S]\) and has a unique binary expansion.

Since \(p>2^a\), we have \(S<2p\) and \(S+1<2p\). Reducing the displayed equation modulo \(p\) gives \(p\mid y_0\). Because \(y_0\) is odd, nonzero, and \(|y_0|<2p\), there is a sign \(\varepsilon_0\in\{-1,1\}\) such that
\[
y_0=-\varepsilon_0p.
\]
After division by \(p\), reduction modulo \(p\) gives \(p\mid(y_1-\varepsilon_0)\). The difference \(y_1-\varepsilon_0\) is even, hence any nonzero multiple of the odd prime \(p\) occurring here has absolute value at least \(2p\). But
\[
|y_1-\varepsilon_0|\le S+1<2p,
\]
so \(y_1=\varepsilon_0\). Thus the first two terms cancel exactly.

Dividing the remaining equation by \(p^2\) and repeating the same argument shows inductively that for every \(0\le k\le (b-1)/2\),
\[
y_{2k}=-\varepsilon_kp,\qquad y_{2k+1}=\varepsilon_k,
\]
where each \(\varepsilon_k\in\{-1,1\}\) is free. Conversely, every such sign choice satisfies the equal-sum equation, because each adjacent pair contributes zero. Hence there are exactly \(2^{(b+1)/2}\) oriented partitions.

Swapping \(A\) and \(B\) negates every \(y_j\), equivalently every \(\varepsilon_k\). No oriented partition is fixed by this swap. Therefore every unordered partition corresponds to exactly two oriented partitions, and the unordered count is
\[
2^{(b+1)/2}/2=2^{(b-1)/2}.
\]

## Verification
The accompanying `verify.py` independently enumerates the bounded signed-coefficient equation for several small values in the asserted strip and checks the formula. It also checks an example below the strip, \(2^3\cdot7^3\), where the count is \(6\), not \(2\); this confirms that the upper-strip hypothesis is mathematically substantive rather than cosmetic. Running the checker prints `VERIFY_OK`.

## Relationship to prior work
Rao and Peng introduced and studied Zumkeller numbers in arXiv:0912.0052 (first posted 2009-12-01). Their practical-number criterion implies existence for \(2^a p^b\) in the relevant odd-exponent range, but it does not enumerate all divisor bipartitions.

Mahanta, Saikia, and Yaqubi later gave the explicit existence characterization: \(2^a p^b\) is Zumkeller exactly when \(p\le2^{a+1}-1\) and \(b\) is odd. Their theorem and proof construct a partition but do not state an exact formula for the number of partitions. The present result refines that existence theorem on the natural upper subinterval \(2^a<p\le2^{a+1}-1\) by classifying every oriented partition there.

A published-result database search found a closest partition-count result for the special case \(b=1\), where the count is \(1\) throughout this upper strip. The formula above recovers that case and extends the multiplicity count to every odd exponent.

## Limitations
The proof uses the strict inequality \(S+1<2p\), so it does not classify partition multiplicities when \(p\le2^a\). Counts can be larger there; for example, the checker finds six unordered partitions for \(2^3\cdot7^3\). Literature and database searches can miss obscure equivalent formulations, so the originality assessment should be read together with the explicit source comparisons in the review files.

## References
1. K. P. S. Bhaskara Rao and Y. Peng, “On Zumkeller Numbers,” arXiv:0912.0052, first version 2009-12-01; later *Journal of Number Theory* 133 (2013), 1135–1155, DOI 10.1016/j.jnt.2012.09.020.
2. P. J. Mahanta, M. P. Saikia, and D. Yaqubi, “Some properties of Zumkeller numbers and k-layered numbers,” *Journal of Number Theory* 217 (2020), 218–236, DOI 10.1016/j.jnt.2020.05.003.
