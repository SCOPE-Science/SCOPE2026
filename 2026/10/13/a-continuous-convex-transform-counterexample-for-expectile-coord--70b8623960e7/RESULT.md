# A continuous convex-transform counterexample for expectile coordinates

## Finding

**Theorem.** There are bounded, absolutely continuous random variables \(X,Y\) with strictly increasing continuous distribution functions on their respective support intervals for which the ordinary convex transformation order \(F_X\le_c F_Y\) holds, yet the expectile-coordinate transformation \(e_Y\circ e_X^{-1}\) is not convex. In fact, one can take \(Y=X^2\), where \(X\) has an explicitly specified density that is strictly positive throughout \((0,2)\).

This disproves the general implication from ordinary convex transformation order to the expectile-based analogue described in Remark 6, equation (8), of Eberl and Klar [1]. In particular, their inequality (8) does not hold for all triples of expectile levels under the ordinary convex transformation order.

## Assumptions and scope

For an integrable, nonconstant real random variable \(Z\) and \(0<\alpha<1\), its \(\alpha\)-expectile \(e_Z(\alpha)\) is the unique real solution \(t\) of
\[
\alpha\,\mathbb E(Z-t)_+=(1-\alpha)\,\mathbb E(t-Z)_+.
\]
Write \(F_Z\) for the cumulative distribution function. The ordinary convex transformation order means that \(F_Y^{-1}\circ F_X\) is convex on the interior of the support of \(X\). For continuous, strictly increasing distribution functions, the proposed expectile analogue requires convexity of \(e_Y\circ e_X^{-1}\) on its domain, equivalently the three-level inequality in [1, Remark 6, (8)].

Here is the fully explicit construction. Fix \(\eta=10^{-6}\). Let \(J\) be uniform on \(\{0,1,2\}\). Conditional on \(J=j\), let \(H\) be uniform on
\[
I_0=[0,\eta],\qquad I_1=[1-\eta/2,1+\eta/2],\qquad I_2=[2-\eta,2].
\]
Independently let \(B\) be Bernoulli with \(\Pr(B=1)=\eta\), and let \(W\) be uniform on \([0,2]\). Define
\[
X=(1-B)H+BW,\qquad Y=X^2.
\]
The marginal density of \(X\) is
\[
f_X(x)=\frac{\eta}{2}\mathbf 1_{[0,2]}(x)
 +\frac{1-\eta}{3\eta}\sum_{j=0}^2\mathbf 1_{I_j}(x)
\]
(up to irrelevant values at interval endpoints). Thus \(f_X(x)\ge\eta/2>0\) for every \(0<x<2\). Both variables have bounded support and continuous, strictly increasing cdfs on their support intervals. The distribution of \(Y\) is likewise absolutely continuous.

## Proof

**1. Ordinary convex transformation order holds exactly.** The square map is continuous, strictly increasing, and convex on \([0,2]\). Since \(Y=X^2\) and \(F_X\) is continuous and strictly increasing on \([0,2]\),
\[
F_Y^{-1}(F_X(x))=x^2\quad(0<x<2).
\]
Therefore \(F_X\le_c F_Y\).

**2. An exact three-point obstruction.** Consider the limiting discrete pair \(J\) and \(V=J^2\). Let
\[
\alpha_1=\frac16,\qquad\alpha_2=\frac14,\qquad\alpha_3=\frac13.
\]
Directly solving the expectile equations gives
\[
(e_J(\alpha_1),e_J(\alpha_2),e_J(\alpha_3))
 =\left(\frac37,\frac35,\frac34\right),
\]
\[
(e_V(\alpha_1),e_V(\alpha_2),e_V(\alpha_3))
 =\left(\frac57,1,\frac65\right).
\]
For verification of these values, for \(0<t<1\) the expectile equation for \(J\) reduces to \(\alpha(3-2t)=(1-\alpha)t\), giving \(t=3\alpha/(1+\alpha)\). For \(V\), when \(0<t\le1\) it gives \(t=5\alpha/(1+\alpha)\); when \(1\le t<4\) it gives \(t=(1+3\alpha)/(2-\alpha)\).

The consecutive secant slopes of \(e_V\circ e_J^{-1}\) at these three levels are \(5/3\) and \(4/3\). Equivalently, its **concavity witness** is the strictly positive determinant
\[
D_0=\left(1-\frac57\right)\left(\frac34-\frac35\right)
-\left(\frac65-1\right)\left(\frac35-\frac37\right)
=\frac3{350}>0.
\]
A convex function at increasing abscissas must instead have the corresponding determinant nonpositive.

**3. Stability under the explicit full-support smoothing.** For any integrable random variables \(A,C\) defined on the same probability space, the expectile scores
\[
S_\alpha(t;A)=\mathbb E\bigl[\alpha(A-t)_+-(1-\alpha)(t-A)_+\bigr]
\]
are decreasing in \(t\), with a decrease of at least \(\min(\alpha,1-\alpha)\) per unit increase of \(t\). Moreover, for fixed \(t\), the scores are Lipschitz in the observation with coefficient \(\max(\alpha,1-\alpha)\). Comparing their unique zeroes therefore gives the deterministic coupling inequality
\[
|e_A(\alpha)-e_C(\alpha)|
\le\frac{\max(\alpha,1-\alpha)}{\min(\alpha,1-\alpha)}\,\mathbb E|A-C|.
\]
At our three levels the ratio is at most \(5\).

Our construction couples \(X\) to \(J\) so that \(|H-J|\le\eta\), \(|W-J|\le2\), and hence \(\mathbb E|X-J|\le3\eta\). Since both lie in \([0,2]\), \(|X^2-J^2|\le4|X-J|\), whence \(\mathbb E|Y-V|\le12\eta\). Consequently, for each \(i\in\{1,2,3\}\),
\[
|e_X(\alpha_i)-e_J(\alpha_i)|\le15\eta,
\qquad |e_Y(\alpha_i)-e_V(\alpha_i)|\le60\eta.
\]

Write \(u_i=e_X(\alpha_i)\) and \(v_i=e_Y(\alpha_i)\), and define
\[
D=(v_2-v_1)(u_3-u_2)-(v_3-v_2)(u_2-u_1).
\]
Each adjacent \(u\)-difference differs from its discrete counterpart by at most \(30\eta\), and each adjacent \(v\)-difference by at most \(120\eta\). Expanding the two products and using the exact discrete differences gives
\[
|D-D_0|\le
30\eta\left(\frac27+\frac15\right)
+120\eta\left(\frac3{20}+\frac6{35}\right)
+7200\eta^2
=\frac{372}{7}\eta+7200\eta^2.
\]
For \(\eta=10^{-6}\), this is strictly smaller than \(3/350\). Therefore \(D>0\). Also, the adjacent \(u\)-differences are strictly positive: their discrete values are \(6/35\) and \(3/20\), each greater than \(30\eta\). The three increasing points \((u_i,v_i)\) thus have **decreasing** secant slope, contradicting convexity of \(e_Y\circ e_X^{-1}\). This completes the proof. \(\square\)

## Verification

The accompanying standalone exact-arithmetic script `verification/check.py` recomputes all three discrete expectiles from their balance equations, the slope reversal and determinant \(D_0\), the perturbation constants, and the final strict rational inequality. Run `python3 verification/check.py`; it has no third-party dependencies. The script checks finite rational identities only; the quantified continuous-distribution conclusion rests on the preceding analytic Lipschitz and support arguments.

## Relationship to prior work

Eberl and Klar [1, Definition 1(iii)] recall van Zwet's convex transformation order; their equation (4) identifies inverse expectile functions as the cdfs of expectile-transformed distributions. Their Theorem 5 proves preservation of a **scalar, symmetric-level** expectile-skewness inequality. Remark 6 then introduces a stronger all-triples comparison, identifies it with convexity of the expectile-coordinate transformation, and does not establish that it follows from the ordinary convex transformation order. The counterexample here resolves that proposed implication negatively. It does not contradict Theorem 5, because the violated three levels are not symmetric around one half.

Eberl and Klar [2] develop expectile-based skewness measures and conventional convex-transform comparisons but do not furnish the three-level counterexample above. The conclusion is a separation of two stochastic orders, not a failure of the scalar skewness monotonicity established in [1].

## Limitations

The example is deliberately a full-support but discontinuous-density mixture. No assertion is made about smooth, log-concave, unimodal, or unbounded-support densities, nor about all convex transformations or all expectile triples. The point-mass calculation alone would not meet continuous-cdf hypotheses; the explicit smoothing and quantitative stability estimate are essential. The result is a mathematical non-implication, not a classification of all comparable distributions. Bibliographic priority beyond the inspected literature is not independently established.

## References

[1] A. Eberl and B. Klar, *Stochastic orders and measures of skewness and dispersion based on expectiles*, Statistical Papers **64** (2023), 509–527. First public preprint: 13 August 2021, arXiv:2108.06138. DOI: 10.1007/s00362-022-01331-x. Full-text Remark 6 and equation (8): https://link.springer.com/article/10.1007/s00362-022-01331-x.

[2] A. Eberl and B. Klar, *Expectile-based measures of skewness*, Scandinavian Journal of Statistics **49** (2022), 373–399. DOI: 10.1111/sjos.12518. https://onlinelibrary.wiley.com/doi/full/10.1111/sjos.12518.
