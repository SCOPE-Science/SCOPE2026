# Exact sign phase diagram for one negative and two quadratic Gaussian factors

## Finding
For a centered, nondegenerate Gaussian triple, the mixed-sign Gaussian product inequality comparing \(\mathbb E[|X_1|^{-s}X_2^2X_3^2]\) with the product of the three separate absolute moments can hold in either direction, even when all correlations are equal and strictly positive. The sign and equality cases admit an exact classification for every admissible covariance matrix, not just a bound.

Write \(a=\operatorname{Corr}(X_1,X_2)\), \(b=\operatorname{Corr}(X_1,X_3)\), \(c=\operatorname{Corr}(X_2,X_3)\), and \(0<s<1\). The normalized product difference is
\[
\Delta_s(a,b,c):=\frac{\mathbb E[|X_1|^{-s}X_2^2X_3^2]}{\mathbb E|X_1|^{-s}}-1
=2c^2-s(a^2+b^2+4abc-2a^2b^2)+s^2a^2b^2.
\]
In particular, the three-factor product inequality \(\mathbb E[|X_1|^{-s}X_2^2X_3^2]\le\mathbb E|X_1|^{-s}\) is true precisely when \(\Delta_s(a,b,c)\le0\); equality means \(\Delta_s=0\). This is a complete algebraic test for the entire positive-definite Gaussian correlation domain.

In the equicorrelated family \(a=b=c=\rho\in(-1/2,1)\), the direction has an especially sharp transition. If \(\rho<0\), then \(\Delta_s>0\) for all \(0<s<1\). If \(\rho>0\), define
\[
B_\rho=2+4\rho-2\rho^2,\qquad
s_*(\rho)=\frac{4}{B_\rho+\sqrt{B_\rho^2-8\rho^2}}.
\]
Then \(0<s_*(\rho)<1\), with \(\Delta_s>0\) below the threshold, \(\Delta_s=0\) at it, and \(\Delta_s<0\) above it. If \(\rho=0\), \(\Delta_s=0\) throughout. The result does not claim a corresponding classification for nonquadratic positive exponents.

## Assumptions and scope
The correlation matrix is
\[
R=\begin{pmatrix}1&a&b\\a&1&c\\b&c&1\end{pmatrix}\succ0.
\]
Equivalently, \(|a|,|b|,|c|<1\) and \(1+2abc-a^2-b^2-c^2>0\). The exponent satisfies \(0<s<1\), ensuring \(\mathbb E|X_1|^{-s}<\infty\). All three variables are standardized; arbitrary nonzero marginal standard deviations cancel after dividing by the corresponding separate moments. The equicorrelation interval is exactly \(-1/2<\rho<1\).

## Proof
Let \(Z=X_1\). Conditionally on \(Z=t\), the vector \((X_2,X_3)\) is Gaussian with means \((at,bt)\), marginal residual variances \(v_2=1-a^2\) and \(v_3=1-b^2\), and residual covariance \(u=c-ab\). These conditional residuals are centered and independent of \(Z\). By Isserlis' fourth-moment formula, odd centered moments vanish and
\[
\mathbb E[X_2^2X_3^2\mid Z=t]
=a^2b^2t^4+(a^2v_3+b^2v_2+4abu)t^2+v_2v_3+2u^2.
\]
For \(Z\) standard normal, the gamma recurrence for the absolute Gaussian moments gives, for \(0<s<1\),
\[
\frac{\mathbb E[|Z|^{-s}Z^2]}{\mathbb E|Z|^{-s}}=1-s,
\qquad
\frac{\mathbb E[|Z|^{-s}Z^4]}{\mathbb E|Z|^{-s}}=(1-s)(3-s).
\]
Substitute these two identities into the conditional fourth moment. The resulting normalized expectation is
\[
 a^2b^2(1-s)(3-s)+(1-s)[a^2(1-b^2)+b^2(1-a^2)+4ab(c-ab)]
 +(1-a^2)(1-b^2)+2(c-ab)^2.
\]
Collect coefficients of \(s\) and subtract the separate-moment product \(1\) to obtain \(\Delta_s(a,b,c)\) exactly as stated. No asymptotics or numerical approximation occurs here. Both directions and equality follow because \(\mathbb E|Z|^{-s}\) is strictly positive.

For equicorrelation \(a=b=c=\rho\), factor
\[
\Delta_s(\rho,\rho,\rho)=\rho^2F_\rho(s),\quad
F_\rho(s)=2(1-s)-4\rho s+2\rho^2s+\rho^2s^2.
\]
When \(-1/2<\rho<0\), each term in the last representation is nonnegative and the first is strictly positive. When \(0<\rho<1\), \(F_\rho(0)=2>0\) and \(F_\rho(1)=3\rho^2-4\rho<0\). Moreover
\[
F'_\rho(s)=-2-4\rho+2\rho^2(1+s)<0
\]
for \(0\le s\le1\), since \(2\rho^2(1+s)\le4\rho^2<4\rho\). Therefore exactly one threshold lies in \((0,1)\), and solving \(F_\rho(s)=0\) gives \(s_*(\rho)\). The independence case \(\rho=0\) is immediate.

## Verification
The included `verify.py` uses Python standard-library exact rational arithmetic to compare the conditional-Gaussian formula with the reduced quadratic for admissible rational correlation triples and rational exponents, including equicorrelated cases on both sides of the transition. The universal result is established by the preceding analytic conditional-moment proof; finite rational tests are reproducibility checks only.

## Relationship to prior work
Russell and Sun proved a universal reverse Gaussian product inequality in dimension two when the powers have opposite signs; their result does not compare one negative power with the product of two positive powers in dimension three. Ogasawara's work on structurally correlated mixed-sign moments provides inequality regimes for compound-symmetric and autoregressive matrices, but the inspected theorem and remarks do not provide the exact full-correlation sign/equality locus given above. Lan, Ouimet and Sun establish corrected general bounds through Schur complements and convex-order comparison, not an exact necessary-and-sufficient condition for this product against its three separate moments. The present identity directly distinguishes the two possible inequality directions and resolves their switching curve for the first equicorrelated three-factor quadratic case.

## Limitations
The positive powers are both exactly two. The criterion is not presented as a general mixed-sign Gaussian product theorem for arbitrary powers, dimensions, or singular covariance matrices. This is a self-review analytical finding, not independently audited. A 2025 paper on structural-correlation mixed-sign products was accessible through an author-hosted text rendering with severely garbled formula extraction; only unambiguously legible theorem descriptions and discussion were used for the comparison. Further independently curated bibliography checks could reveal a previously recorded equivalent special case.

## References
1. Oliver Russell and Wei Sun, *An Opposite Gaussian Product Inequality*, arXiv:2205.10231 (first public version, 20 May 2022), https://arxiv.org/abs/2205.10231, later Statistics & Probability Letters 191 (2022), 109656.
2. Haruhiko Ogasawara, *Gaussian product inequalities for absolute moments of mixed-sign orders using a series formula*, first public preprint 10 November 2024, https://www.researchgate.net/publication/385688052, later Communications in Statistics - Theory and Methods 55 (2026), 2762–2776.
3. Guolie Lan, Frédéric Ouimet and Wei Sun, *Results related to the Gaussian product inequality conjecture for mixed-sign exponents in arbitrary dimension*, arXiv:2505.09976, especially Theorems 1 and 2.
4. Isserlis' fourth-moment identity and the classical gamma-function recurrence for standard-normal absolute moments.
