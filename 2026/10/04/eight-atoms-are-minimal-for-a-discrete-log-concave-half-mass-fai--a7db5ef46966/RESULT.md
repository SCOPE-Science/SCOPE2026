# Eight atoms are minimal for a discrete log-concave half-mass failure at an integer mean
## Finding
Let \(X\) be an integer-valued random variable with a log-concave probability mass function and finite contiguous support. If \(\mathbb E[X]\in\mathbb Z\) and the support has at most seven points, then
\[
\Pr\{X\le \mathbb E[X]\}\ge \frac12.
\]
The support cutoff is sharp. There is a log-affine law on \(\{1,\ldots,8\}\) with mean \(6\) and lower-tail mass below one half. Specifically, let \(r>0\) be the unique positive root of
\[
2r^7+r^6-r^4-2r^3-3r^2-4r-5=0
\]
and set
\[
\Pr\{X=j\}=\frac{r^j}{\sum_{i=1}^{8}r^i},\qquad 1\le j\le 8.
\]
Then \(\mathbb E[X]=6\), \(r=1.370544100408968\ldots\), and
\[
\Pr\{X\le6\}=0.4915269002932845\ldots<\frac12.
\]
Thus eight is the smallest support cardinality for which the half-mass-at-the-integer-mean bound can fail within finite discrete log-concave laws.

## Assumptions and scope
A probability mass function \(p\) on \(\mathbb Z\) is log-concave here when its positive support is an integer interval and \(p_j^2\ge p_{j-1}p_{j+1}\) at every interior index. The finding concerns finite support and an integer mean. It does not assert a \(1/2\) bound for larger supports, noninteger means, or distributions outside discrete log-concavity.

Translation does not change either support cardinality or the event \(\{X\le\mathbb E[X]\}\), so a support of cardinality at most seven may be placed inside \(\{1,\ldots,N\}\) with \(N\le7\).

## Proof
Fix an integer threshold \(k\) and a finite ambient interval. Consider the log-concave laws satisfying \(\mathbb E[X]\le k\). The half-space localization theorem for discrete log-concave probability sequences says that extreme points of the convex hull of this class are log-affine on a contiguous subinterval: their masses are proportional to \(r^j\) for some \(r>0\). Since \(P\mapsto P(X\le k)\) is linear, its minimum over the original class equals its minimum over the convex hull, and applying the extreme-point theorem to its negative reduces the problem to those truncated geometric laws.

Take one such law on \(\{a,\ldots,b\}\). If \(b\le k\), its lower-tail probability is one; if \(a>k\), the mean constraint is impossible. Otherwise write \(L=b-a+1\) and \(s=k-a+1\). For masses proportional to \(r^j\) on \(\{1,\ldots,L\}\), differentiation with respect to \(\log r\) gives
\[
\frac{d}{d\log r}\mathbb E_r[X]=\operatorname{Var}_r(X)>0,
\]
while
\[
\frac{d}{d\log r}\Pr_r\{X\le s\}
 =\operatorname{Cov}_r(\mathbf 1_{\{X\le s\}},X)<0
\]
whenever both sides of the threshold have positive mass. Hence, under \(\mathbb E_r[X]\le s\), the smallest lower-tail probability occurs at the unique parameter with \(\mathbb E_r[X]=s\). The cases \(s=1\) or a singleton support are trivial, so it remains to check \(2\le s\le L-1\).

At mean \(s\), the parameter \(r\) is the unique positive root of
\[
M_{L,s}(r):=\sum_{j=1}^{L}(j-s)r^{j-1}=0.
\]
Uniqueness follows again from strict monotonicity of the mean. Moreover,
\[
\Pr_r\{X\le s\}-\frac12
=\frac{H_{L,s}(r)}{2\sum_{j=0}^{L-1}r^j},
\qquad
H_{L,s}(r):=\sum_{j=0}^{s-1}r^j-\sum_{j=s}^{L-1}r^j.
\]
Therefore only the sign of \(H_{L,s}\) at the unique root of \(M_{L,s}\) is needed.

For every pair \(3\le L\le7\) and \(2\le s\le L-1\), the standalone exact-rational verifier brackets the unique positive root of \(M_{L,s}\) by bisection and bounds \(H_{L,s}\) throughout that bracket using an exact derivative bound. It certifies \(H_{L,s}>0\) for all fifteen pairs. This finite list is exhaustive after the localization reduction, so the support-at-most-seven statement is a proof rather than a sampling experiment.

For \((L,s)=(8,6)\), the same exact calculation certifies \(H_{8,6}(r)<0\). Here
\[
M_{8,6}(r)=-5-4r-3r^2-2r^3-r^4+r^6+2r^7,
\]
which is the displayed witness polynomial, and the negative sign of \(H_{8,6}\) proves the strict half-mass failure.

## Verification
Run `python3 verify.py`. The verifier uses only Python's standard library and exact rational arithmetic for all sign certificates. It checks every reduced pair \((L,s)\) for \(L\le7\), checks the eight-point witness \((8,6)\), and verifies the witness polynomial coefficients. Its terminal line is `VERIFY_OK`.

The displayed decimal values are explanatory only. They are not used to certify either the integer mean or the strict inequalities.

## Relationship to prior work
Alqasem, Aravinda, Marsiglietti, and Melbourne prove the general discrete log-concave bound \(\Pr\{X\le\mathbb E[X]\}\ge e^{-1}\) when the mean is integral, and they explicitly exhibit a log-affine counterexample on \(\{1,\ldots,8\}\) with mean \(6\) for the stronger \(1/2\) bound. Their paper also recalls the extreme-point reduction to truncated geometric distributions. The present finding identifies the previously unstated support threshold: the cited eight-point example is minimal because every support of cardinality at most seven satisfies the half-mass bound.

The localization step itself is due to Marsiglietti and Melbourne, who characterize log-affine sequences as extreme points of log-concave probability sequences in a half-space slice of the simplex. The new part is the support-cardinality cutoff and its exhaustive exact sign analysis, not the localization theorem or the existence of the eight-point family.

## Limitations
The argument uses a published finite-dimensional localization theorem as a premise; it is not reproved here. The result is a sharp support-size boundary, not a characterization of all eight-point counterexamples or a best lower-tail constant for each support size. Targeted database and literature searches found no prior statement of the seven-versus-eight cutoff, but literature search cannot establish absolute uniqueness.

## References
1. A. Alqasem, H. Aravinda, A. Marsiglietti, and J. Melbourne, *On a Conjecture of Feige for Discrete Log-Concave Distributions*, arXiv:2208.12702, first public 2022-08-26; SIAM Journal on Discrete Mathematics 38 (2024), 93–102, DOI:10.1137/22M1539514.
2. A. Marsiglietti and J. Melbourne, *Geometric and Functional Inequalities for Log-Concave Probability Sequences*, arXiv:2004.12005, first public 2020-04-24; Discrete & Computational Geometry 71 (2024), 556–586, DOI:10.1007/s00454-023-00528-7.
