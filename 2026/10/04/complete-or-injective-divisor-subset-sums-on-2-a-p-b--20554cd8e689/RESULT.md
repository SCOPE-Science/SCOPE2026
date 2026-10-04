# Complete-or-injective divisor subset sums on \(2^a p^b\)
## Finding
Let \(a,b\ge 1\), let \(p\) be an odd prime, put \(n=2^a p^b\), and set \(M=2^{a+1}-1\). If \(p\le 2^{a+1}\), every integer in \([0,\sigma(n)]\) is a sum of distinct divisors of \(n\). If \(p>2^{a+1}\), the subset-sum map from subsets of the divisors of \(n\) to their sums is injective; hence exactly \(2^{(a+1)(b+1)}\) integers in \([0,\sigma(n)]\) are representable and exactly \(\sigma(n)+1-2^{(a+1)(b+1)}\) are omitted. In particular, every non-practical integer of this two-prime-support form omits at least \(2^{a+1}-1\) values.

This gives an exact transition at the classical practical-number boundary. On the practical side the divisor subset sums fill one interval. Immediately beyond that boundary, there are no collisions at all: each represented integer has a unique representation by distinct divisors.

## Assumptions and scope
Let \(a,b\ge 1\) and let \(p\) be an odd prime. Write
\[
n=2^a p^b,\qquad M=1+2+\cdots+2^a=2^{a+1}-1.
\]
The positive divisors of \(n\) split into \(b+1\) layers
\[
\{p^j,2p^j,\ldots,2^a p^j\},\qquad 0\le j\le b.
\]
Within the \(j\)-th layer, every subset has sum \(c_jp^j\) for a unique coefficient \(c_j\in\{0,1,\ldots,M\}\), because binary expansion is unique. Thus divisor subsets are in bijection with digit vectors \((c_0,\ldots,c_b)\in\{0,\ldots,M\}^{b+1}\), and their sums are
\[
\sum_{j=0}^b c_jp^j.
\]

## Proof
For the coverage case, define \(T_j=M(1+p+\cdots+p^j)\). At level \(j=0\), the attainable sums are exactly \([0,M]\). Suppose the attainable sums through level \(j-1\) form \([0,T_{j-1}]\). Adding the \(j\)-th layer gives
\[
\bigcup_{c=0}^M [cp^j,cp^j+T_{j-1}].
\]
Consecutive intervals meet or overlap exactly when \(p^j\le T_{j-1}+1\). If \(p\le M+1=2^{a+1}\), then
\[
T_{j-1}+1-p^j=\frac{(M-p+1)(p^j-1)}{p-1}\ge0.
\]
Hence induction gives every sum in \([0,T_b]\). Since \(T_b=\sigma(n)\), the first assertion follows.

Now suppose \(p>2^{a+1}=M+1\). Then \(0\le c_j\le M<p\). If
\[
\sum_{j=0}^b c_jp^j=\sum_{j=0}^b d_jp^j
\]
with all \(c_j,d_j\in\{0,\ldots,M\}\), uniqueness of ordinary base-\(p\) expansion forces \(c_j=d_j\) for every \(j\). The binary representation inside each layer is itself unique, so the original divisor subsets are equal. Therefore the divisor-subset-sum map is injective.

There are \((M+1)^{b+1}=2^{(a+1)(b+1)}\) divisor subsets. Thus exactly that many integers in \([0,\sigma(n)]\) are represented, and the omitted count is
\[
H_b=\sigma(n)+1-2^{(a+1)(b+1)}
=M\frac{p^{b+1}-1}{p-1}+1-(M+1)^{b+1}.
\]
For \(b=1\),
\[
H_1=M(p-M-1)\ge M,
\]
because \(p>M+1\). Moreover
\[
H_{b+1}-H_b=M\bigl(p^{b+1}-(M+1)^{b+1}\bigr)>0.
\]
Hence every non-practical member of this family omits at least \(M=2^{a+1}-1\) values.

## Verification
A standalone checker enumerates divisor subsets for \(1\le a\le4\), \(1\le b\le2\), and odd primes below \(32\). It checks full interval coverage on the practical side and injectivity plus the exact omitted-count formula on the non-practical side. The checker is supplementary: the proof above is valid for all stated parameters.

## Relationship to prior work
Stewart and Sierpiński independently characterized practical numbers by the prime-factor inequality \(p_j\le1+\sigma(\prod_{i<j}p_i^{\alpha_i})\). Weingartner's introduction restates this criterion and, for the family here, it reduces to \(p\le2^{a+1}\). That classical theorem determines whether complete coverage occurs, but it does not state the complementary injectivity assertion or the exact number of represented and omitted subset sums proved here.

The closest located neighboring results concern exact equal-sum divisor partitions for \(2^a p\), practical-number criteria, and other two-prime-support divisor equations. None of those statements implies that every divisor subset sum is collision-free beyond the practical threshold. A residual literature risk remains because the full text of Stewart's 1954 paper was not available through the inspected open sources; its bibliographic metadata and the theorem as restated by Weingartner were inspected.

## Limitations
The theorem uses the binary divisor layers of \(2^a\). It does not claim an analogous complete-or-injective dichotomy for three or more distinct prime factors, nor for replacing the power of two by an arbitrary practical factor. The finite checker is not evidence for the infinite quantifiers beyond corroborating the exact formulas on small cases.

## References
1. Andreas Weingartner, *Practical Numbers and the Distribution of Divisors*, arXiv:1405.2585, first posted 11 May 2014; *Quarterly Journal of Mathematics* 66 (2015), 743–758, DOI 10.1093/qmath/hav006.
2. B. M. Stewart, *Sums of Distinct Divisors*, *American Journal of Mathematics* 76 (1954), 779–785, DOI 10.2307/2372651.
3. W. Sierpiński, *Sur une propriété des nombres naturels*, *Annali di Matematica Pura ed Applicata* 39 (1955), 69–74, DOI 10.1007/BF02410762.
