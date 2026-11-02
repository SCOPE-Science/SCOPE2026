# Position balancing strictly lowers record counts conditioned on a permutation fixed point

## Finding
Let \(\pi\) be uniform on the permutations of \(\{1,\ldots,n\}\), \(n\ge2\). Write \(R(\pi)\) for its number of *left-to-right upper records*, counting the first entry. For \(1\le i\le n\), let \(R_i\) have the law of \(R(\pi)\) conditional on \(\pi(i)=i\). Define \(P_0(z)=1\) and \(P_r(z)=\prod_{h=0}^{r-1}(z+h)\) for integers \(r\ge1\).

**Exact conditional probability-generating function:** For every such \(n,i\),
\[
\mathbb E[z^{R_i}]=\frac{P_{n-1}(z)+(z-1)P_{i-1}(z)P_{n-i}(z)}{(n-1)!}.
\]

**Strict stochastic position-balancing law:** For every integer \(1\le i<n\) and every integer \(1\le t\le n\),
\[
\Pr(R_i\ge t)-\Pr(R_{i+1}\ge t)
=\frac{n-2i}{(n-1)!}[z^{t-1}]P_{i-1}(z)P_{n-i-1}(z).
\]
Thus \(R_i\) decreases in usual stochastic order as \(i\) approaches the center from the left, increases symmetrically thereafter, and satisfies \(R_i\overset d=R_{n+1-i}\). The ordering is strict for \(i<n/2\): at least one upper-tail inequality is strict. If \(n\) is even, the two central conditional laws coincide.

**Sharp distributional distances:** When \(1\le i<n/2\), the one-Wasserstein distance on integer counts and total-variation distance between adjacent conditional laws are exactly
\[
W_1(R_i,R_{i+1})=\frac{(n-2i)(i-1)!(n-i-1)!}{(n-1)!},
\]
\[
d_{\mathrm{TV}}(R_i,R_{i+1})
=\frac{n-2i}{(n-1)!}\max_{0\le k\le n-2}[z^k]P_{i-1}(z)P_{n-i-1}(z).
\]
Here \(W_1\) is the infimum of \(\mathbb E|X-Y|\) over all couplings with the indicated marginals, and \(d_{\mathrm{TV}}\) is the supremum difference of event probabilities.

**Moment consequences:** Put \(H_m=\sum_{h=1}^m1/h\). Then
\[
\mathbb E[R_i]=H_{n-1}+\binom{n-1}{i-1}^{-1},
\quad
\operatorname{Cov}(\mathbf1_{\{\pi(i)=i\}},R)
=\frac1n\left(\binom{n-1}{i-1}^{-1}-\frac1n\right).
\]
For \(n\ge5\), that covariance is positive at the first and last two positions and negative at every other position, although for the *total* fixed-point count \(F=\sum_i\mathbf1_{\{\pi(i)=i\}}\),
\[
\operatorname{Cov}(F,R)
=\frac1n\left(\sum_{k=0}^{n-1}\binom{n-1}{k}^{-1}-1\right)>0.
\]

## Assumptions and scope
All permutations are equally likely, the event \(\pi(i)=i\) has probability \(1/n\), and records are strict upper records in one-line order. No independence between the fixed-point event and records is assumed. All statements are exact for integers \(n\ge2\), with the explicitly stated ranges for indices and thresholds. The polynomial coefficient notation \([z^k]Q(z)\) means the coefficient of \(z^k\) in \(Q\), taken as zero when outside its degree range.

## Proof
**(1) Removing the conditioned fixed point.** Conditional on \(\pi(i)=i\), remove this entry and standardize the remaining entries to obtain a uniform permutation \(\sigma\) of size \(m=n-1\). Let \(R'\) count the records of \(\sigma\). For each position before \(i\), inserting the value \(i\) does not affect record status. For positions after \(i\), insertion also leaves record statuses unchanged: if the earlier \(i-1\) values contain one larger than \(i\), the inserted value cannot raise the running maximum; otherwise those earlier values are exactly all labels smaller than \(i\), so every later value is larger than \(i\). Either way, inserting \(i\) cannot change the record status of any subsequent value. Thus only the inserted position itself can contribute a new record.

The inserted value is an upper record if and only if the \(i-1\) values before it are precisely \(\{1,\ldots,i-1\}\). Call this event \(B\). We therefore have the pointwise identity \(R=R'+\mathbf1_B\). Moreover \(\Pr(B)=\binom{m}{i-1}^{-1}\). Conditional on \(B\), the standardized prefix and suffix of \(\sigma\) are independent uniform permutations of respective lengths \(a=i-1\) and \(b=n-i\), and every suffix value exceeds every prefix value. Their record counts add. The classical record-count generating polynomial for a uniform permutation of size \(r\) is \(P_r(z)/r!\), including \(r=0\). Hence
\[
\mathbb E[z^{R'}]=\frac{P_m(z)}{m!},\qquad
\mathbb E[z^{R'}\mathbf1_B]=\frac{P_a(z)P_b(z)}{m!}.
\]
Substitution into \(z^{R'+\mathbf1_B}=z^{R'}+(z-1)z^{R'}\mathbf1_B\) gives the first displayed generating function. For completeness, the classical polynomial follows inductively by inserting a new smallest value into a uniform permutation: only one of the \(r\) insertion positions creates a new record, leading to \(P_r(z)=(z+r-1)P_{r-1}(z)\).

**(2) Adjacent position subtraction.** Write \(Q_i(z)=P_{i-1}(z)P_{n-i}(z)\). Because \(P_{r+1}(z)=(z+r)P_r(z)\),
\[
Q_i(z)-Q_{i+1}(z)=(n-2i)P_{i-1}(z)P_{n-i-1}(z).
\]
The conditional probability-generating functions therefore differ by \((z-1)(n-2i)P_{i-1}P_{n-i-1}/m!\). If \(A_k\) are the coefficients of the product \(P_{i-1}P_{n-i-1}\), extended by zeros, the mass-function difference at integer \(k\) is \((n-2i)(A_{k-1}-A_k)/m!\). Summing from \(k=t\) upward telescopes to the claimed upper-tail difference. Every coefficient of the product is nonnegative; it has a positive coefficient whenever its degree is positive. This proves all stochastic comparisons, strictness and central equality. Symmetry follows immediately from \(Q_i(z)=Q_{n+1-i}(z)\).

**(3) The distances.** If \(i<n/2\), every upper-tail difference is nonnegative. The integer one-Wasserstein identity \(W_1(X,Y)=\sum_{t\in\mathbb Z}|\Pr(X\ge t)-\Pr(Y\ge t)|\) therefore gives the coefficient sum \(\frac{n-2i}{m!}P_{i-1}(1)P_{n-i-1}(1)\), which equals the stated factorial expression. For total variation, the product polynomial has only real nonpositive zeros. Its finite nonzero coefficient sequence is unimodal by Newton's inequalities (the monomial boundary cases are immediate). Therefore \(A_{k-1}-A_k\) changes sign at most once, and the positive mass of its signed first difference equals \(\max_k A_k\). This gives the exact total-variation formula, without supposing normality or asymptotics.

**(4) The moments.** Differentiate the generating function at \(z=1\). Since \(P_m(1)=m!\) and \(P_m'(1)/m!=H_m\), we obtain \(\mathbb E[R_i]=H_{n-1}+1/\binom{n-1}{i-1}\). Unconditionally \(\mathbb E[R]=H_n\). The covariance identity follows from the event probability \(1/n\); sum over positions for \(F\). For \(n\ge5\), \(\binom{n-1}{i-1}<n\) precisely at the two positions closest to each endpoint, so the covariance signs have the stated classification. The covariance for \(F\) is positive because the two endpoint binomial reciprocals already sum to two.

## Verification
The accompanying standalone `checker.py` uses Python 3 standard-library integer and rational arithmetic. Executing `python checker.py` produced: `PASS: 193,404 exact arithmetic assertions; exhaustive permutations n=2..9; polynomial laws n=2..80.` The verifier independently enumerates permutations and conditional counts through size nine, checks the displayed polynomial law and symmetry through size 80, and confirms every adjacent upper-tail, Wasserstein and total-variation expression in that finite range. The proof above, not this finite computation, establishes the unbounded assertions.

## Relationship to prior work
The record-count polynomial and elementary fixed-point counting are classical; they are not claimed as new. Diaconis, Evans and Graham study fixed points and adjacent unseparated pairs, a different second statistic. Gnedin and Gorin develop measures conditioned on record statistics, but not the specified fixed-position conditioning and stochastic comparisons. Brändén and Claesson place left-to-right maxima, fixed points and strong fixed points in a common mesh-pattern framework, without deriving the position-balancing tail identity. Kim and Stanton derive a joint continued fraction involving *strong* fixed points and records, but a strong fixed point imposes a strictly stronger condition than \(\pi(i)=i\). The new point assessed here is the all-threshold position-dependent stochastic law and the exact quantitative distances, rather than its classical constituent enumerations.

## Limitations
The model is uniformly random permutations; fixed-point-conditioned ordering need not extend to nonuniform permutation laws. A fixed point and a strong fixed point are different events. The result is exact for one specified fixed position; no simultaneous conditioning on several fixed positions is asserted. Literature comparisons do not establish exhaustive historical priority, and related results implicit in other permutation-statistics approaches remain a residual possibility. Independent external validation has not been performed.

## References
- P. Diaconis, S. N. Evans and R. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Statistics Technical Report 822 (publicly listed August 1, 2013), https://statistics.berkeley.edu/tech-reports/822 .
- A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, arXiv:1202.3680 (2012), https://arxiv.org/abs/1202.3680 .
- P. Brändén and A. Claesson, *Mesh patterns and the expansion of permutation statistics as sums of permutation patterns*, arXiv:1102.4226 (2011), https://arxiv.org/abs/1102.4226 .
- J. S. Kim and D. Stanton, *The Combinatorics of Associated Laguerre Polynomials*, arXiv:1501.03880 (2015), https://arxiv.org/abs/1501.03880 .
- S. Gutmann and collaborators, *Conditional Probability of Derangements and Fixed Points*, arXiv:2201.04181 (2022), https://arxiv.org/abs/2201.04181 .
- FindStat, statistic St000221, number of strong fixed points, https://www.findstat.org/StatisticsDatabase/St000221/ .
