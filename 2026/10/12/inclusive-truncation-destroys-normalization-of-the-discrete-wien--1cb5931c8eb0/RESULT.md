# Inclusive truncation destroys normalization of the discrete Wiener-range law
## Finding
The source constructs integer-valued Wiener ranges by taking successive differences of the continuous range distribution. Write
\[
Z_T=\lfloor R_T\rfloor,\qquad
R_T=\sup_{0\le t\le T}W_t-\inf_{0\le t\le T}W_t,
\]
and denote the mass and CDF by
\[
p_T(r)=\Pr(Z_T=r),\qquad F_T(r)=\Pr(Z_T\le r),
\qquad r\in\mathbb Z_{\ge0},
\]
with the convention \(F_T(-1)=0\). In particular,
\[
p_T(r)=F_T(r)-F_T(r-1).
\]

Equation (3.2) of the 2026 article calls its bivariate product a truncated PMF on the **inclusive** integer rectangle
\[
a_i\le r_i\le b_i,\qquad i=1,2,
\]
but divides the mass for each coordinate by \(F_T(b_i)-F_T(a_i)\). On exactly that printed support the proposed expression is
\[
q_T(r_1,r_2)=
\prod_{i=1}^2\frac{p_T(r_i)}{F_T(b_i)-F_T(a_i)}.
\]
For integers \(0\le a_i<b_i\), summing over the entire support gives
\[
\boxed{
\sum_{r_1=a_1}^{b_1}\sum_{r_2=a_2}^{b_2}q_T(r_1,r_2)
=\prod_{i=1}^2
\frac{F_T(b_i)-F_T(a_i-1)}{F_T(b_i)-F_T(a_i)}
=\prod_{i=1}^2\left[1+
\frac{p_T(a_i)}{F_T(b_i)-F_T(a_i)}\right]>1.
}
\]
The same identity holds for any finite number of independent coordinates. Thus the printed inclusive truncation is **not a probability mass function**, although the untruncated PMF remains normalized.

The correct conditional law, still for the source's independent marginals, is
\[
\boxed{
q_T^*(r_1,r_2)=
\prod_{i=1}^2
\frac{p_T(r_i)}{F_T(b_i)-F_T(a_i-1)},
\qquad a_i\le r_i\le b_i.
}
\]
Its corresponding CDF within the support is
\[
\boxed{
Q_T^*(r_1,r_2)=
\prod_{i=1}^2
\frac{F_T(r_i)-F_T(a_i-1)}{F_T(b_i)-F_T(a_i-1)}.
}
\]
The printed truncated CDF in Eq. (3.4) instead subtracts \(F_T(a_i)\). It consequently assigns zero at the announced lower support point even though Eq. (3.2) assigns positive mass there. These are two manifestations of the same **inclusive-endpoint normalization mismatch**, not two independent claims.

This error is already substantial at the paper's own illustrative market bounds. Section 4 uses
\[
T=1,\qquad (a_1,b_1)=(2,8),\qquad (a_2,b_2)=(1,7).
\]
Numerical evaluation of the article's own continuous Wiener-range CDF series gives
\[
\begin{aligned}
\frac{F_1(8)-F_1(1)}{F_1(8)-F_1(2)}
&=16.8063254071891056\ldots,\\
\frac{F_1(7)-F_1(0)}{F_1(7)-F_1(1)}
&=5.1606866374234016\ldots.
\end{aligned}
\]
(The subscript \(1\) denotes the time horizon, not the asset.) Hence
\[
\boxed{\sum q_1=86.7321789530702266\ldots}
\]
for the full published bivariate rectangle. At its single lower-left cell,
\[
\boxed{q_1(2,1)=65.7651669084577193\ldots,}
\]
while the correct conditional law gives
\[
\boxed{q_1^*(2,1)=0.7582556751403938\ldots.}
\]
A value exceeding one for a single alleged atom rules out any interpretation of Eq. (3.2) as a valid probability assignment on its stated support.

The breakdown becomes unbounded in the high-frequency setting motivating the discretization. For one coordinate with bounds \([0,1]\), the printed assignment is
\[
q_T(0)=\frac{p_T(0)}{p_T(1)}
=\frac{\Pr(R_T<1)}{\Pr(1\le R_T<2)}.
\]
Brownian scaling gives \(R_T\overset d=\sqrt T\,R_1\), so
\[
\boxed{q_T(0)\longrightarrow\infty\qquad(T\downarrow0),}
\]
although the correct conditional mass \(p_T(0)/(p_T(0)+p_T(1))\) tends to one.

There is a quantitative bound: by the reflection principle, if \(R_T\ge1\), at least one of the absolute positive or negative Brownian extremes reaches \(1/2\). Thus
\[
\Pr(R_T\ge1)
\le4\bigl[1-\Phi(1/(2\sqrt T))\bigr]
\le4e^{-1/(8T)},
\]
where \(\Phi\) is the standard normal CDF. Therefore
\[
\boxed{q_T(0)\ge\frac14e^{1/(8T)}-1,}
\]
which is a positive and exponentially increasing lower bound for all sufficiently small \(T\). For two independent identically truncated coordinates the printed mass at the origin is the square of \(q_T(0)\).

At \(T=0.1\), direct series evaluation gives
\[
\begin{aligned}
p_T(0)&=0.9937383929996926728\ldots,\\
p_T(1)&=0.0062616059844558914\ldots,
\end{aligned}
\]
so the published probability of the zero cell is \(158.70343733965314\ldots\) for one coordinate, while the correct conditional probability is \(0.99373839400918\ldots\). The bivariate published mass at \((0,0)\) is about \(25186.781\), and its total mass on \(\{0,1\}^2\) is about \(25505.188\).

## Assumptions and scope
The result uses the source's independent Wiener-range marginals, each at an observation time \(T>0\), and finite integer inclusive bounds \(0\le a_i<b_i\). The bivariate statement is exactly the case of Eq. (3.2); the finite-dimensional product is its direct independent extension.

For each integer \(r\ge0\), the Brownian range falls in \([r,r+1)\) with positive probability. This follows from full support of Wiener measure on continuous paths: a small open tube around a path having range strictly inside that interval has positive probability. Thus all displayed denominators are positive, and the claimed strict inequality holds.

The printed formula would be a valid conditional PMF **if** its support were changed to the left-open integer set \(\{a_i+1,\ldots,b_i\}\), but the article explicitly specifies the inclusive interval \([a_i,b_i]\) and includes the endpoint \(a_i\). Alternatively, keeping the announced support requires the corrected denominator and CDF displayed above.

The result concerns the **probabilistic formula as printed** and not inaccessible analysis software or the economic validity of a Brownian model for prices.

## Proof
For any integer-valued random variable with mass \(p\) and cumulative distribution function \(F\), telescoping yields
\[
\sum_{r=a}^{b}p(r)=F(b)-F(a-1).
\]
The printed denominator is
\[
D=F(b)-F(a)=\sum_{r=a+1}^{b}p(r).
\]
Thus the sum of the printed marginal truncated masses is
\[
\sum_{r=a}^{b}\frac{p(r)}D
=\frac{D+p(a)}D=1+\frac{p(a)}D>1.
\]
Independence multiplies these factors over coordinates. Dividing instead by \(D+p(a)\) is precisely conditioning on \(a\le Z\le b\), yielding the corrected PMF and CDF.

For the short-time result, Wiener scaling establishes \(R_T\overset d=\sqrt T R_1\). Since \(R_1\) is finite and positive almost surely, \(\Pr(R_T<1)\to1\) and \(\Pr(1\le R_T<2)\to0\), with the latter positive for every \(T>0\). The quotient diverges.

For the exponential lower bound, note that \(R_T\ge1\) implies \(\sup_{0\le t\le T}|W_t|\ge1/2\). The union bound and reflection principle give
\[
\Pr\bigl(\sup_{0\le t\le T}|W_t|\ge1/2\bigr)
\le4\Pr(W_T\ge1/2)
\le4e^{-1/(8T)}.
\]
Writing \(u_T=4e^{-1/(8T)}\), one has \(p_T(0)\ge1-u_T\) and \(p_T(1)\le u_T\), whence
\[
\frac{p_T(0)}{p_T(1)}\ge\frac{1-u_T}{u_T}
=\frac14e^{1/(8T)}-1.
\]
This completes the proof.

## Verification
Run `python verify_wiener_truncation.py` with Python 3 and the open-source `mpmath` package. The standalone checker reproduces the source's Wiener-range CDF series at high precision, its marginal and joint inclusive-support mass sums, and the corrected conditional masses. It compares 80-term and 100-term evaluations, computes a rigorous positive-series remainder bound at the largest evaluated grid endpoint, and checks finite-grid summations directly. It prints the values for the paper's actual \(T=1\) bounds and the high-frequency illustration \(T=0.1\).

Finite numerical checks do not establish the general theorem. The arbitrary-bound result follows from telescoping, and the short-time divergence and exponential lower bound follow from Wiener scaling and the reflection principle.

## Relationship to prior work
The 2026 source, **Alharbi and El-Hadidy**, explicitly defines the mass by successive discrete CDF differences (Eq. (2.1)), proves normalization for the untruncated independent joint model (Theorem 1), and then gives Eq. (3.2) with the lower endpoint included but a denominator that omits that endpoint. Its Eq. (3.4) repeats the endpoint choice in the CDF. The concrete bounds \([2,8]\) and \([1,7]\) come from the source's market illustration.

The 2025 **Alraddadi–El-Hadidy** multivariate Wiener-range work derives **continuous** double truncation on \([a,b]\). Its \(F(b)-F(a)\) denominator is valid for a continuous density, because a single endpoint has zero probability. It does not imply that the same denominator normalizes the 2026 **discrete** inclusive support: the latter has strictly positive mass at \(a\).

The 2018 online **El-Hadidy–Alfreedi** study addresses deletion of an *interior interval* from a Wiener-range domain. Its accessible abstract and bibliographic record concern a different truncation operation; the complete publisher full text was inaccessible during this comparison. The general fact that an integer-inclusive truncated distribution uses \(F(b)-F(a-1)\) is elementary and is not asserted as a new general theorem.

Targeted searches of the 2026 DOI, equation, discrete support aliases, missing-endpoint normalization, multivariate rectangular truncation, and small-time Wiener-range probability inflation did not locate a published source-specific correction. The accepted contribution is the **exact diagnosis of the new model on its stated support**, its very large numerical discrepancy on the article's own applied bounds, and an explicit unbounded small-time failure in the high-frequency regime.

## Limitations
Nothing here challenges the proper normalization of the **untruncated** Wiener-range law. Nor does the result show that every figure, reported fit, or implementation used Eq. (3.2) literally: source code was not inspected.

Changing the stated truncation support to \((a_i,b_i]\) makes the original denominator appropriate but changes the modeled event and discards all lower-endpoint observations. Retaining the published **inclusive** event requires the corrected formulas.

The 2018 methodological predecessor's full text remained inaccessible; a prior unindexed correction is also possible. These are residual originality risks, not alternatives to the exact normalization proof.

## References
1. S. A. Alharbi and M. A. A. El-Hadidy, “A multivariate discrete Wiener range distribution with truncation: Theory, reliability properties, and applications to constrained financial markets,” *AIMS Mathematics* 11 (2026), 3563–3593, doi:10.3934/math.2026146. Eqs. (2.1), (2.3), (3.2), (3.4); Section 4.
2. R. M. Alraddadi and M. A. A. El-Hadidy, “A multivariate model for the Wiener process range, with statistical properties under stochastic volatility,” *AIMS Mathematics* 10 (2025), 22023–22052, doi:10.3934/math.2025980. Section 2.1 and Eq. (2.5).
3. M. A. A. El-Hadidy and A. A. Alfreedi, “Internal truncated distributions: Applications to Wiener process range distribution when deleting a minimum stochastic volatility interval from its domain,” *Journal of Taibah University for Science* 13 (2019), 201–215, doi:10.1080/16583655.2018.1555020. Published online 2018.
