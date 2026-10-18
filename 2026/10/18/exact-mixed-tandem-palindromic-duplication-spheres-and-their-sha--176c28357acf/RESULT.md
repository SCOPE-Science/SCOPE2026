# Exact mixed tandem–palindromic duplication spheres and their sharp alphabet transition

## Finding

**Theorem.** Let \(\Sigma\) be any alphabet with \(q\ge 2\) symbols, let \(n\ge2\), and let \(w=w_0w_1\cdots w_{n-1}\in\Sigma^n\). At each position \(0\le i\le n-2\), one may duplicate the adjacent length-two factor either in its original order (tandem duplication) or in reversed order (palindromic duplication). Write \(\mathcal D(w)\) for the set of **distinct** length-\(n+2\) outputs obtained by exactly one of these operations. Then

\[
|\mathcal D(w)|=1+\sum_{i=0}^{n-3}\mathbf1_{w_i\ne w_{i+2}}+\sum_{i=0}^{n-2}\mathbf1_{w_i\ne w_{i+1}}-\sum_{i=0}^{n-4}\mathbf1_{\substack{w_i=w_{i+3},\ w_{i+1}=w_{i+2},\\w_i\ne w_{i+1}}}.
\]

An empty sum is zero. In particular, the final correction subtracts one precisely for each factor of the form \(abba\) with \(a\ne b\).

The following sharp extrema hold for every \(n\ge2\):

* For \(q\ge3\), the maximum is \(2n-2\). Equality holds exactly when every pair of source letters at distance one or two is distinct. The number of maximizing labeled words is \(q(q-1)(q-2)^{n-2}\).
* For \(q=2\), the maximum is \(n\). Its maximizing words are counted by

\[
M_n=2[z^{n-1}]\frac{z(1+z)^2}{1-z-z^2-z^3}.
\]

Thus \(M_n\) begins \(2,6,10,18,34,62,114,210,\ldots\) as \(n=2,3,4,5,6,7,8,9,\ldots\). If \(d_i=\mathbf1_{w_i\ne w_{i+1}}\) is the binary transition word of length \(n-1\), equality in the binary bound holds exactly when the transition word contains a one, every initial or terminal zero-run has length one, and every interior zero-run has length one or two. Absent zero-runs impose no restriction.

For a word chosen uniformly from \(\Sigma^n\), the mean mixed-sphere size is exactly

\[
\mathbb E|\mathcal D(W)|=1+\frac{(2n-3)(q-1)}q-\frac{\max(0,n-3)(q-1)}{q^3}.
\]

## Assumptions and scope

Indices start at zero. For a factor \(w_iw_{i+1}=ab\), a tandem operation inserts \(ab\) immediately following its occurrence, whereas a palindromic operation inserts \(ba\) immediately following its occurrence. No complement is applied. Distinct outputs are counted only once, even if several insertion sites or both mechanisms give the same output. The source word itself is not an output because **exactly one** length-two duplication is applied. The alphabet is arbitrary and finite; only equality and inequality of letters are used. There is no assumption that letters are random for the deterministic formula and extrema. The mean formula assumes independent uniform letters.

## Proof

Write \(T_i(w)=w_0\cdots w_{i+1}w_iw_{i+1}w_{i+2}\cdots w_{n-1}\) and \(P_i(w)=w_0\cdots w_{i+1}w_{i+1}w_iw_{i+2}\cdots w_{n-1}\), for \(0\le i\le n-2\).

**Lemma 1 (tandem outcomes).** For \(i<j\), \(T_i=T_j\) if and only if the factor from source indices \(i\) through \(j+1\) has period two. Indeed, remove the identical prefix up to index \(i+1\) and the identical suffix after source index \(j+1\). Comparing the intervening source/copy streams forces and is forced by \(w_t=w_{t+2}\) for every \(i\le t\le j-1\). Thus the equality classes of consecutive tandem positions are exactly runs of adjacent equalities \(T_i=T_{i+1}\iff w_i=w_{i+2}\). Consequently,

\[
|\{T_i\}|=1+\sum_{i=0}^{n-3}\mathbf1_{w_i\ne w_{i+2}}.
\]

**Lemma 2 (palindromic outcomes).** If \(w_i=w_{i+1}\), then \(P_i=T_i\). For distinct positions \(i<j\), equality \(P_i=P_j\) forces every symbol of \(w_i\cdots w_{j+1}\) to be identical: comparing the two shifted inserted streams in order first forces equality of the first two source symbols, and then propagates equality across the intervening span. In particular, all \(P_i\) for which \(w_i\ne w_{i+1}\) are pairwise different.

**Lemma 3 (cross-channel collisions).** Fix \(i\) with \(w_i\ne w_{i+1}\). There exists a tandem outcome identical to \(P_i\) if and only if \(i\le n-4\) and

\[
w_i=w_{i+3}\ne w_{i+1}=w_{i+2}.
\]

For sufficiency, the local source factor \(abba\), \(a\ne b\), becomes \(abbaba\) both when its first \(ab\) is palindromically duplicated and when its last \(ba\) is tandem duplicated; hence \(P_i=T_{i+2}\). For necessity, compare an equality \(P_i=T_j\). If \(j=i\), the two inserted blocks differ. If \(j=i+1\), comparing output coordinates \(i+2,i+3\) forces \(w_i=w_{i+1}\), a contradiction. If \(j<i\), the earlier tandem output has \(w_i\) at output coordinate \(i+2\), whereas the palindromic output has \(w_{i+1}\) there, another contradiction. Thus \(j\ge i+2\). At output coordinates \(i+2,i+3\), the palindromic result has symbols \(w_{i+1},w_i\) and the later tandem result has \(w_{i+2},w_{i+3}\). Their equality yields the stated \(abba\) condition. By Lemma 2, different nonconstant palindromic sites cannot count the same cross-channel collision.

Combining the tandem outcomes, the distinct nonconstant palindromic outcomes, and exactly these cross-channel coincidences proves the sphere-size identity.

For \(q\ge3\), both positive sums are bounded by \(n-2\) and \(n-1\), respectively, while the correction is nonnegative. Thus \(|\mathcal D(w)|\le2n-2\). Equality forces all distance-one and distance-two comparisons to be unequal, which simultaneously makes the correction zero. Conversely this condition gives equality. There are \(q\) choices for the first symbol, \(q-1\) for the second, and \(q-2\) for each subsequent symbol; this proves the stated count, including \(n=2\).

For \(q=2\), let \(m=n-1\) and set \(d_i=\mathbf1_{w_i\ne w_{i+1}}\), for \(0\le i<m\). The binary alphabet implies \(\mathbf1_{w_i\ne w_{i+2}}=\mathbf1_{d_i\ne d_{i+1}}\), and an \(abba\) factor corresponds exactly to a block \(101\) in \(d\). Therefore

\[
|\mathcal D(w)|=1+\#1(d)+\#\{i:d_i\ne d_{i+1}\}-\#101(d).
\]

Its difference from \(n=m+1\) is \(\#0(d)-\#\{i:d_i\ne d_{i+1}\}+\#101(d)\). If \(d\) is identically zero, this difference is \(m>0\). Otherwise decompose its zeros into maximal runs. A zero-run of length \(\ell\) at one boundary contributes \(\ell-1\) to the difference. An interior zero-run contributes \(\ell-2+\mathbf1_{\ell=1}\), which is zero exactly for lengths one and two, and strictly positive for larger lengths. Every contribution is nonnegative. This proves the sharp bound \(|\mathcal D(w)|\le n\) and the asserted precise maximizer criterion. In particular, the all-ones transition word attains equality.

It remains to count binary maximizers. A permitted nonzero transition word is uniquely a possible leading zero, followed by a positive run of ones, then zero or more pairs consisting of an interior zero-run of length one or two and a positive run of ones, then a possible trailing zero. Its generating function by transition-word length is

\[
(1+z)\frac{z}{1-z}\sum_{j\ge0}\left((z+z^2)\frac{z}{1-z}\right)^j(1+z)=\frac{z(1+z)^2}{1-z-z^2-z^3}.
\]

Each binary transition word has exactly two preimages \(w\) (the choice of \(w_0\)), proving the coefficient formula. Finally, the expectation follows from linearity: each one-step inequality has probability \((q-1)/q\), and each specific length-four factor is \(abba\) with unequal letters with probability \((q-1)/q^3\).

## Verification

The standalone exhaustive checker `verify.py` forms the literal set of both output types for every word in the following finite ranges: binary sources of lengths two through twelve, ternary sources of lengths two through nine, four-symbol sources of lengths two through seven, and five-symbol sources of lengths two through six. In total it tests 79,073 source words. For every word it compares the exact cardinality, every potential nonconstant palindrome-to-tandem collision, and the relevant extremal criterion. For each length and alphabet it checks the maximum, exact count of maximizing words, and the rational mean. The checker reports `MIXED_PAL_TANDEM_LENGTH2_PASS` with 79,073 words and 355,650 nonconstant palindromic insertion sites. These checks are finite corroboration of the unrestricted proof, not an extrapolation from finite cases. Run with `python3 verify.py`; no dependencies beyond the Python standard library are required.

## Relationship to prior work

Lenz, Wachter-Zeh, and Yaakobi [1] define tandem and palindromic duplications and give separate single-error sphere-size formulae (including a zero-error center). Their palindromic length-two analysis concerns coincidences **within** the palindromic mechanism. The present identity counts the **union of exactly-one tandem and palindromic descendants**, where the additional \(abba\) cross-mechanism collision and its extremal consequences require separate analysis. Zeraatpisheh, Esmaeili, and Gulliver [2] study constructions for duplication-correcting codes and mixed duplication mechanisms but do not provide this source-wise union formula in the inspected coding sections. Yohananov and Schwartz [3] analyze capacities and palindromic/reverse-complement codes, not the combined one-step tandem/palindromic sphere-size distribution. Related publicly indexed results on tandem-only source confusability, multiple palindromic duplications, and tandem lengths one versus two concern different observations and do not imply the union or the binary tribonacci extremal classification.

## Limitations

The theorem concerns a **single** duplication of a source factor of **exact length two**. It is not an assertion about repeated errors, reverse-complement copying, general block lengths, correcting-code optimum sizes, or channel capacity. The mathematical proof is self-contained; independent expert validation has not been performed. The literature comparison covers located and materially inspected sources but cannot exclude an equivalent identity expressed in unindexed or differently named literature.

## References

[1] A. Lenz, A. Wachter-Zeh, and E. Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, arXiv:1707.00052 (first posted 2017-06-30). https://arxiv.org/abs/1707.00052

[2] M. Zeraatpisheh, M. Esmaeili, and T. A. Gulliver, *Construction of Duplication Correcting Codes*, IEEE Access (2020), DOI:10.1109/ACCESS.2020.2995812. https://doi.org/10.1109/ACCESS.2020.2995812

[3] L. Yohananov and M. Schwartz, *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*, arXiv:2312.00394 (first posted 2023-12-01). https://arxiv.org/abs/2312.00394
