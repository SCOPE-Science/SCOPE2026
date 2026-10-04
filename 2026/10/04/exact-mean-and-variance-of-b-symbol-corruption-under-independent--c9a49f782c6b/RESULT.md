# Exact mean and variance of b-symbol corruption under independent substitutions
## Finding
Let \(n\ge b\ge1\). Each coordinate of a transmitted word is independently changed to a different symbol with probability \(p\in[0,1]\). Conditional on a change, the replacement symbol may follow any law. Let \(W_b\) be the cyclic \(b\)-symbol distance between the transmitted and received words, so \(W_b\) counts the cyclic length-\(b\) read windows containing at least one changed coordinate. Put \(r=1-p\). Define \(u_0=b\), and for \(1\le d\le n-1\),
\[
u_d=2b-\max\{0,b-d\}-\max\{0,b-(n-d)\}.
\]
Then
\[
\mathbb E W_b=n(1-r^b)
\]
and
\[
\operatorname{Var}(W_b)=n\left(\sum_{d=0}^{n-1}r^{u_d}-nr^{2b}\right).
\]
When \(n\ge2b\), this becomes
\[
\operatorname{Var}(W_b)=n\left(r^b+2\sum_{j=b+1}^{2b-1}r^j-(2b-1)r^{2b}\right).
\]
Hence, for fixed \(b\) and \(0<p<1\), the standard deviation is exactly proportional to \(\sqrt n\) throughout the regime \(n\ge2b\). The formulas are independent of alphabet size and of the conditional replacement distribution.

## Assumptions and scope
The read vector is cyclic: its \(i\)-th component is the consecutive block of length \(b\) beginning at coordinate \(i\), with indices modulo \(n\). A substitution is counted only when the symbol actually changes. The error indicators are independent Bernoulli variables with common parameter \(p\). No assumption is made on which different symbol is written after an error, because the \(b\)-symbol distance only records whether each read window changed.

The result covers all integers \(n\ge b\ge1\) and all \(p\in[0,1]\). It does not address dependent substitution locations, insertions, deletions, decoding failure probability, or code design.

## Proof
For each cyclic start \(i\), let \(Z_i\) indicate that the entire length-\(b\) window beginning at \(i\) contains no changed coordinate. Then
\[
W_b=n-\sum_{i=0}^{n-1}Z_i.
\]
A window is clean exactly when its \(b\) coordinates all avoid substitution, so \(\mathbb E Z_i=r^b\). Summing gives
\[
\mathbb E W_b=n(1-r^b).
\]

For two starts separated by cyclic offset \(d\), the event \(Z_i=Z_{i+d}=1\) is exactly the event that every coordinate in the union of the two length-\(b\) cyclic windows is unchanged. For \(d=0\), that union has size \(u_0=b\). For \(1\le d\le n-1\), the two windows overlap in
\[
\max\{0,b-d\}+\max\{0,b-(n-d)\}
\]
coordinates, so their union has size \(u_d\). Independence therefore gives
\[
\mathbb E(Z_iZ_{i+d})=r^{u_d}.
\]
Translation invariance on the cycle implies
\[
\operatorname{Var}\left(\sum_i Z_i\right)
=n\sum_{d=0}^{n-1}\left(r^{u_d}-r^{2b}\right),
\]
which is the stated general variance formula. Since subtracting from the constant \(n\) does not change variance, this is also \(\operatorname{Var}(W_b)\).

If \(n\ge2b\), two windows at offsets \(b\le d\le n-b\) are disjoint and contribute zero covariance. For offsets \(1\le d\le b-1\) and their reversals, the union sizes are \(b+d\). Substitution in the general formula yields the simplified expression.

## Verification
The accompanying `verify.py` reconstructs \(W_b\) directly from binary error patterns and compares exact Bernoulli-weighted first and second moments with the formulas using rational arithmetic. It exhausts every error pattern for all \(1\le b\le n\le9\) at four rational error probabilities. It also checks the simplified variance expression against the general formula for every \(1\le b\le50\) and every \(2b\le n\le120\). A successful replay prints `VERIFY_OK` together with the checked case counts.

## Relationship to prior work
Ding, Zhang, and Ge define the cyclic \(b\)-symbol read vector, \(b\)-distance, and \(b\)-weight, and study Singleton bounds and MDS \(b\)-symbol codes. Their definitions imply that, under substitutions, \(W_b\) is the number of read windows hit by at least one changed coordinate. The inspected open full text does not study stochastic substitution locations or derive moments of this random distance.

Song and Fujiwara study sphere-packing and Gilbert--Varshamov bounds for \(b\)-symbol read channels. Their accessible abstract describes coding bounds rather than stochastic moments. Full text was not available through the lawful access routes used for this review, so an unstated overlap inside that paper remains a specific residual risk.

Later work on \(b\)-symbol weight distributions, including Vega's treatment of semiprimitive irreducible cyclic codes, studies the distribution of \(b\)-weights within structured codes. That is a different distribution from the independent-substitution process here: the present theorem weights error supports by a Bernoulli product law and gives exact first and second moments for arbitrary \(n,b,p\).

## Limitations
The proof uses independence of substitution locations. With dependent errors, the pairwise clean-window probabilities need not equal powers of \(r\). The result gives the first two moments, not the full probability generating function. The originality comparison found no statement implying the theorem, but a differently phrased or unindexed treatment of cyclic Bernoulli window coverage could exist.

## References
1. B. Ding, T. Zhang, and G. Ge, “Maximum Distance Separable Codes for \(b\)-Symbol Read Channels,” arXiv:1609.09236v1, 29 September 2016; later Finite Fields and Their Applications 49 (2018), 180--197.
2. S. Song and T. Fujiwara, “Sphere Packing Bound and Gilbert-Varshamov Bound for \(b\)-Symbol Read Channels,” IEICE Transactions on Fundamentals E101.A(11) (2018), 1915--1924, DOI 10.1587/transfun.E101.A.1915.
3. G. Vega, “The \(b\)-symbol weight distributions of all semiprimitive irreducible cyclic codes,” Designs, Codes and Cryptography 91 (2023), 2213--2221, DOI 10.1007/s10623-023-01193-w.
