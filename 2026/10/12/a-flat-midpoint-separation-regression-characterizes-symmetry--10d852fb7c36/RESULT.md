# A flat midpoint–separation regression characterizes symmetry

## Finding

Let \(X_1,X_2\) be independent and identically distributed real-valued random variables. Assume their common moment generating function is finite on an open interval containing \(0\), and write
\[
\mu=\mathbb E X_1,
\qquad
A=\frac{X_1+X_2}{2},
\qquad
R=|X_1-X_2|.
\]

Then
\[
\boxed{
\mathbb E[A\mid R]=\mu\quad\text{almost surely}
}
\tag{1}
\]
if and only if the parent law is centrally symmetric about \(\mu\):
\[
\boxed{
X_1-\mu\overset d=\mu-X_1.
}
\tag{2}
\]

Thus, within the local-mgf class, the sample midpoint is mean-independent of the two-observation range exactly for symmetric parent laws.

The result is strictly weaker than independence of midpoint and range. The criterion asks only for a constant conditional mean, not factorization of the joint law.

For finite-support distributions the moment-generating-function assumption is automatic.

## Assumptions and scope

The parent distribution may be discrete, continuous, or mixed. No density or positivity assumption is imposed.

The moment generating function is assumed finite on some interval
\[
(-\delta,\delta)
\]
with \(\delta>0\). This ensures local differentiability and uniqueness of the moment generating function.

The result is for a sample of size two. It characterizes central symmetry from a first conditional moment and should not be confused with classical normal characterizations based on full independence of sample mean and range for larger samples.

## Proof

Center the variables:
\[
Z_i=X_i-\mu,
\qquad i=1,2,
\]
and let
\[
M(t)=\mathbb E e^{tZ_1}.
\]

Suppose first that the parent law is centrally symmetric. Then
\[
(Z_1,Z_2)\overset d=(-Z_1,-Z_2).
\]
Under this global sign change,
\[
|Z_1-Z_2|
\]
is unchanged while
\[
Z_1+Z_2
\]
changes sign. Therefore, for every bounded measurable \(h\),
\[
\mathbb E\!
\left[
(Z_1+Z_2)h(|Z_1-Z_2|)
\right]
=0.
\]
This is equivalent to
\[
\mathbb E[Z_1+Z_2\mid |Z_1-Z_2|]=0,
\]
which is exactly (1).

Conversely, assume (1). Then
\[
\mathbb E[Z_1+Z_2\mid |Z_1-Z_2|]=0.
\tag{3}
\]
Choose \(t\) sufficiently close to zero that the exponential moments used below are finite. Since
\[
\cosh(t(Z_2-Z_1))
\]
is a measurable function of \(|Z_1-Z_2|\), equation (3) gives
\[
\mathbb E[(Z_1+Z_2)\cosh(t(Z_2-Z_1))]=0.
\tag{4}
\]

By exchangeability of \((Z_1,Z_2)\), swapping the coordinates leaves \(Z_1+Z_2\) unchanged but changes the sign of \(Z_2-Z_1\). Hence
\[
\mathbb E[(Z_1+Z_2)\sinh(t(Z_2-Z_1))]=0.
\tag{5}
\]
Adding (4) and (5),
\[
\mathbb E[(Z_1+Z_2)e^{t(Z_2-Z_1)}]=0.
\tag{6}
\]

Independence factors the two terms in (6):
\[
M'(-t)M(t)+M(-t)M'(t)=0.
\tag{7}
\]
Because moment generating functions are positive on their real domain, divide by
\[
M(t)M(-t).
\]
With
\[
K(t)=\log M(t),
\]
equation (7) becomes
\[
K'(t)+K'(-t)=0.
\tag{8}
\]
But
\[
\frac{d}{dt}\bigl(K(t)-K(-t)\bigr)
=K'(t)+K'(-t),
\]
so (8) shows that \(K(t)-K(-t)\) is constant near zero. At \(t=0\) it is zero. Therefore
\[
M(t)=M(-t)
\]
for all \(t\) in a neighborhood of zero.

The moment generating functions of \(Z_1\) and \(-Z_1\) thus agree on a neighborhood of zero. By uniqueness of moment generating functions,
\[
Z_1\overset d=-Z_1,
\]
proving (2).

The differentiation in (7) is justified by working on a slightly smaller interval inside the given open interval of exponential integrability.

## Verification

The accompanying checker performs an exact finite census over all probability laws with strictly increasing support of size two through five chosen from
\[
\{-3,-2,-1,0,1,2,3\},
\]
and positive integer weights from \(\{1,2,3\}\), normalized to probabilities.

For each law it computes, in exact rational arithmetic, the conditional mean of
\[
X_1+X_2
\]
given each attainable value of \(|X_1-X_2|\). It tests whether that conditional mean is constant and independently tests whether the support and masses are centrally symmetric about the mean.

Across \(9072\) laws, exactly \(396\) satisfy the flat conditional-mean property, and exactly the same \(396\) laws are symmetric.

The census is supplementary. The theorem for arbitrary distributions in the stated class follows from the moment-generating-function argument above.

## Relationship to prior work

Huang and Su study characterizations based on regression assumptions involving order statistics. Their 2013 paper develops conditional expectations for sums of variables based on specified order statistics; the inspected full text does not state the two-observation absolute-separation criterion above.

Their earlier paper treats regression assumptions involving adjacent order statistics. Its inspected full text gives several distributional characterizations from linear regressions of neighboring order statistics, but not conditioning a sample sum or midpoint on the absolute pair difference.

Akhundov, Balakrishnan, and Nevzorov study characterizations involving the midrange and related statistics. The accessible abstract describes conditional regressions of linear combinations of central order statistics and a Student distribution characterization. The full article was not available for decisive comparison, so it remains an explicit originality risk.

Hu and Lin prove a modern normal characterization from independence of sample mean and range, under positivity and continuity assumptions and sample size at least three. That result is stronger in the dependence condition and different in conclusion: full independence characterizes normality, whereas the present two-observation mean-independence criterion characterizes central symmetry.

## Limitations

The converse uses local existence of the moment generating function. The criterion may remain true under weaker transform or integrability assumptions, but no such extension is claimed.

The result establishes central symmetry, not independence of midpoint and range and not normality.

The sample size is exactly two. For larger samples, conditioning on the range loses the direct two-variable transform factorization used here.

Older characterization literature involving midranges and order-statistic regressions is extensive. The inaccessible full text of the midrange paper noted above remains the main residual originality risk.

## References

1. J. S. Huang and N. C. Su, “Characterizations based on regression assumptions of order statistics,” *Statistics* 48 (2014), 122–131, DOI 10.1080/02331888.2013.825961; published online 2013-09-12.
2. J. S. Huang and N. C. Su, “Characterizations based on certain regression assumptions of adjacent order statistics,” *Statistics & Probability Letters* 80 (2010), 1812–1818, DOI 10.1016/j.spl.2010.07.010.
3. I. Akhundov, N. Balakrishnan, and V. B. Nevzorov, “New Characterizations by Properties of Midrange and Related Statistics,” *Communications in Statistics—Theory and Methods* 33, DOI 10.1081/STA-200039063.
4. W. Hu and G. D. Lin, “Characterizations of the Normal Distribution via the Independence of the Sample Mean and the Feasible Definite Statistics with Ordered Arguments,” arXiv:2112.06152, first submitted 2021-12-12.
