# Exact reflection complexity of binary power-indicator sequences

## Finding
For each integer \(b\ge 2\), let \(X^{(b)}=(x_j)_{j\ge 0}\) be the one-sided binary word with \(x_j=1\) precisely when \(j=b^k\) for an integer \(k\ge 0\), and \(x_j=0\) otherwise. Let \(r_b(n)\) be the number of its distinct length-\(n\) factors after identifying each factor with its reversal.

Put \(d_m=(b-1)b^m\). For every \(m\ge 2\) and every integer \(d_m\le n<d_{m+1}\), writing \(s=n-d_m\) and \(h=d_{m-1}\), the **exact** formula is
\[
r_b(n)=\left\lceil\frac n2\right\rceil+b^{m-1}+2+
\min\left\{h,\left\lceil\frac s2\right\rceil\right\}.
\]
An explicit finite-sum expression given below also computes every shorter length. For the binary-base case, \(r_2(0)=1\), \(r_2(1)=2\), \(r_2(2)=3\), \(r_2(3)=5\), and for every \(n\ge4\),
\[
r_2(n)=2\left\lceil\frac n2\right\rceil+2.
\]
For every integer \(b\ge2\), the precise normalized lower and upper accumulation bounds are
\[
\liminf_{n\to\infty}\frac{r_b(n)}n=\frac12+\frac{1}{b(b-1)},\qquad
\limsup_{n\to\infty}\frac{r_b(n)}n=\frac12+\frac{b}{(b-1)(b+2)}.
\]
Thus the normalized complexity converges to \(1\) when \(b=2\), and does not converge when \(b\ge3\). In particular, for \(b=3\), its liminf is \(2/3\) and its limsup is \(4/5\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); a factor is a contiguous block appearing at any nonnegative starting position. Reversal-equivalent factors are counted once even if only one orientation occurs. All bases \(b\ge2\), all nonnegative factor lengths, and the half-open blocks \(d_m\le n<d_{m+1}\) with integer \(m\ge2\) are included. No claim about nonintegral bases, multidimensional words, or arbitrary lacunary supports is made.

## Proof
**1. Count distinct factors without identifying reversals.** The ones occur at \(1,b,b^2,\ldots\), with strictly increasing consecutive distances \(d_k=(b-1)b^k\). For every \(n\ge1\), exactly \(n+1\) factors contain at most one \(1\): the all-zero word and the \(n\) words having one \(1\). Each occurs because arbitrarily long zero runs separate sufficiently distant ones.

Any factor containing at least two \(1\)'s contains a unique first pair of consecutive ones, at positions \(b^k\) and \(b^{k+1}\). The distance \(d_k\) uniquely determines \(k\), so different such pairs cannot produce the same factor. For \(k=0\), the allowed starts are \(0\) and \(1\). For \(k\ge1\), the allowed starts are the \(d_{k-1}\) positions strictly after \(b^{k-1}\) and not after \(b^k\). Requiring the factor to contain \(b^{k+1}\) yields, for integer \(n\ge1\),
\[
c_0(n)=\min\{2,(n-d_0)_+\},\qquad
c_k(n)=\min\{d_{k-1},(n-d_k)_+\}\quad(k\ge1),
\]
where \(z_+=\max(0,z)\). These are numbers of distinct factors whose first two ones are that pair. Hence the ordinary factor complexity is
\[
p_b(n)=n+1+\sum_{k\ge0}c_k(n).
\]
All sums in this proof are finite because \(d_k\to\infty\).

**2. Identify precisely which factors pair with their reversals.** The one-one factors create exactly \(\lfloor n/2\rfloor\) nontrivial reversal pairs. A factor containing at least three ones has strictly increasing successive distances between its ones. Its reversed word has these distances in strictly decreasing order; this cannot occur as a factor of \(X^{(b)}\). Thus only exactly-two-one factors can make further reversal pairs.

For a pair at distance \(d_k\), any exactly-two-one factor has the form
\[
0^\ell 1 0^{d_k-1}1 0^{t-\ell},\qquad t=n-d_k-1.
\]
The maximum number of leading zeros is \(P_0=1\) for the first pair and \(P_k=d_{k-1}-1\) for \(k\ge1\). The maximum trailing zeros is \(Q_k=d_{k+1}-1\), which exceeds \(P_k\). The factor and its reversal both appear exactly when \(0\le\ell\le P_k\) and \(0\le t-\ell\le P_k\). Consequently the number of these factors having a factor reversal is
\[
B_k(n)=\max\{0,\min(P_k,t)-\max(0,t-P_k)+1\}\quad(d_k<n).
\]
Their allowable left-zero counts form an interval symmetric under \(\ell\leftrightarrow t-\ell\), so there are precisely \(\lfloor B_k(n)/2\rfloor\) nontrivial reversal pairs. This proves the **all-length finite-sum formula**
\[
r_b(n)=n+1+\sum_{d_k<n}c_k(n)-\left\lfloor\frac n2\right\rfloor
-\sum_{d_k<n}\left\lfloor\frac{B_k(n)}2\right\rfloor\qquad(n\ge1),
\]
with \(r_b(0)=1\). In the first sum, the cases \(k=0\) and \(k\ge1\) use the definitions above.

**3. Collapse the finite sums on each geometric interval.** Fix \(m\ge2\) and \(d_m\le n<d_{m+1}\), set \(s=n-d_m\), \(h=d_{m-1}\). Then \(c_0(n)=2\), \(c_k(n)=d_{k-1}\) for \(1\le k<m\), \(c_m(n)=\min(h,s)\), and all later contributions vanish. The geometric sum is \(\sum_{k=1}^{m-1}d_{k-1}=b^{m-1}-1\), so
\[
p_b(n)=n+b^{m-1}+2+\min(h,s).
\]
For \(k<m\), \(B_k(n)=0\), except possibly \(b=2\), \(m=2\), \(n=4\), \(k=0\), when \(B_0(4)=1\) and its contribution to the number of reversal **pairs** is still zero. For \(k=m\), the above exact interval-counting formula simplifies to
\[
B_m(n)=\max\{0,\min(s,2h-s)\}.
\]
A direct check of the three ranges \(0\le s\le h\), \(h\le s\le2h\), and \(s\ge2h\) gives
\[
\min(h,s)-\left\lfloor\frac{B_m(n)}2\right\rfloor
=\min\left(h,\left\lceil\frac s2\right\rceil\right).
\]
Subtracting the \(\lfloor n/2\rfloor\) one-one reversal pairs proves the stated closed formula. For \(b=2\), one has \(h=2^{m-1}\) and \(0\le s<2h\), so the last minimum is simply \(\lceil s/2\rceil\) and the closed form reduces to \(2\lceil n/2\rceil+2\). Direct application of the all-length sum gives the four initial values.

**4. Compute the exact accumulation bounds.** Set \(u=n/d_m\) for the uniquely determined \(m\). As \(m\to\infty\), \(1\le u<b\). Uniformly in this interval, the exact formula implies
\[
\frac{r_b(n)}n=\frac12+
\frac{\frac1{b(b-1)}+\min\{\frac1b,\frac{u-1}{2}\}}{u}+O(1/n).
\]
For \(b\ge3\), the continuous right-hand profile increases from \(u=1\) to \(u=1+2/b\) and decreases until \(u=b\). Its equal endpoint minima are \(\frac12+\frac1{b(b-1)}\), and its peak is \(\frac12+\frac{b}{(b-1)(b+2)}\). The corresponding integer lengths can be chosen within \(O(1)\) of each scaled location, so both extrema are genuine accumulation values. For \(b=2\), the profile is constant \(1\). These evaluations prove both limits and their convergence claims.

## Verification
Run the standalone standard-library script `verify.py` with Python 3. The script independently enumerates reversal-equivalence classes among factors of a long explicit prefix for bases \(2\) through \(7\), for lengths \(1\) through \(140\). It compares those counts with the all-length formula and with the geometric-block closed formula wherever applicable. The finite-prefix bound used in the script exceeds every relevant adjacent-power pair and includes long isolated-one and zero intervals at all tested lengths. These finite comparisons check the arithmetic and boundary cases, but do not prove the quantified infinite theorem; the proof above does.

## Relationship to prior work
Allouche, Campbell, Li, Shallit, and Stipulanti introduced reflection complexity and proved in their Theorem 55 that reflection complexity is effectively regular for an automatic word. The power-indicator word here is \(b\)-automatic: the base-\(b\) representation of each one-position is exactly a leading \(1\) followed only by zeros. That general regularity theorem does **not** state the explicit formula or the sharp nonconvergent accumulation slopes proved here. The inspected applications of that paper evaluate other automatic words, such as Thue–Morse and paperfolding.

Krawchuk and Rampersad studied cyclic and related reversal complexity for other words; cyclic-conjugacy equivalence is distinct from the reversal equivalence counted here. Dvořáková and Pelantová subsequently developed global structural results and minimum-growth characterizations for reflection complexity; those do not supply the present power-indicator evaluation.

## Limitations
The proof concerns the exact sparse geometric support \(\{b^k:k\ge0\}\) and integer bases \(b\ge2\). It does not establish analogous formulas for perturbed powers or unions of lacunary supports. A search and inspection of relevant named articles did not reveal an identical result, but absence from inspected literature is not a proof of historical priority. Finite tests are separate from the infinite proof.

## References
1. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, and M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302, first posted 13 June 2024, https://arxiv.org/abs/2406.09302 . Theorem 55 and Section 8, especially automatic-sequence evaluations.
2. C. Krawchuk and N. Rampersad, *Cyclic Complexity of Some Infinite Words and Generalizations*, Integers 18A (2018), https://math.colgate.edu/~integers/sjs12/sjs12.pdf .
3. L. Dvořáková and E. Pelantová, *Reflection on the Reflection Complexity*, Theory of Computing Systems 70 (2026), Article 35, https://doi.org/10.1007/s00224-026-10278-7 .
