# A scale-dilation counterexample to CDNCEx dispersive ordering
## Finding
Pandey and Kundu's Theorem 3.13 on conditional dynamic negative cumulative extropy (CDNCEx) is false. Let \(X_1,X_2\) be independent exponential random variables with common rate \(\lambda=\log 2\), and define \(Y_i=2X_i\) for \(i=1,2\). Then each \(Y_i\) is larger than \(X_i\) in the dispersive order used by the theorem, and both CDNCEx components of \(\mathbf X\) are strictly increasing in their own threshold. Nevertheless, at \((t_1,t_2)=(2,2)\),
\[
\mathcal{CJ}^{\mathbf Y}_i(2,2)-\mathcal{CJ}^{\mathbf X}_i(2,2)
=\frac{19}{12\log 2}-\frac{20}{9}>0,
\qquad i=1,2.
\]
Thus the asserted conclusion \(\mathbf X\geq_{\mathrm{CDNCEx}}\mathbf Y\) fails.

More generally, if \(Y_i=c_iX_i\) with \(c_i>0\), then the definition gives the exact scaling laws
\[
\mathcal{CJ}^{\mathbf Y}_1(t_1,t_2)
=c_1\mathcal{CJ}^{\mathbf X}_1(t_1/c_1,t_2/c_2),
\qquad
\mathcal{CJ}^{\mathbf Y}_2(t_1,t_2)
=c_2\mathcal{CJ}^{\mathbf X}_2(t_1/c_1,t_2/c_2).
\]
The factor \(c_i\) is the obstruction to the claimed implication.

## Assumptions and scope
For a nonnegative bivariate random vector \(\mathbf X=(X_1,X_2)\) with joint distribution function \(F\), the first CDNCEx component is
\[
\mathcal{CJ}^{\mathbf X}_1(t_1,t_2)
=\frac12\int_0^{t_1}
\left[1-\left(\frac{F(x_1,t_2)}{F(t_1,t_2)}\right)^2\right]dx_1,
\]
with the analogous formula for the second component. The counterexample uses independent, absolutely continuous, nonnegative components, so all denominators are positive for positive thresholds. It targets only the dispersive-order implication in Theorem 3.13; no claim is made about the paper's other stochastic-order results.

The source defines \(Y\geq^D X\) through an increasing dilation \(Y=\psi(X)\) satisfying \(\psi'(x)\geq1\). Here \(\psi(x)=2x\), so the stated dispersive-order hypothesis holds componentwise.

## Proof
Independence reduces either CDNCEx component to the univariate dynamic negative cumulative extropy
\[
J_\lambda(t)=\frac12\int_0^t
\left[1-\left(\frac{1-e^{-\lambda x}}{1-e^{-\lambda t}}\right)^2\right]dx.
\]
Direct integration gives
\[
J_\lambda(t)
=\frac t2-
\frac{t-\frac{3}{2\lambda}+\frac{2e^{-\lambda t}}{\lambda}-\frac{e^{-2\lambda t}}{2\lambda}}
{2(1-e^{-\lambda t})^2}.
\]
Differentiating under the integral, or differentiating this closed form and simplifying, yields
\[
J_\lambda'(t)
=\frac{\lambda e^{-\lambda t}}{(1-e^{-\lambda t})^3}
\int_0^t(1-e^{-\lambda x})^2dx>0
\]
for every \(t>0\). Hence the monotonicity hypothesis of Theorem 3.13 is satisfied.

For \(Y_i=2X_i\), a change of variables in the defining integral gives
\[
\mathcal{CJ}^{\mathbf Y}_i(t_1,t_2)=2J_\lambda(t_i/2),
\qquad
\mathcal{CJ}^{\mathbf X}_i(t_1,t_2)=J_\lambda(t_i).
\]
At \(\lambda=\log2\), exact substitution gives
\[
J_\lambda(1)=\frac{5}{4\log2}-\frac32,
\qquad
J_\lambda(2)=\frac{11}{12\log2}-\frac79.
\]
Therefore
\[
2J_\lambda(1)-J_\lambda(2)
=\frac{19}{12\log2}-\frac{20}{9}
=\frac{57-80\log2}{36\log2}>0.
\]
The last inequality is elementary: the cubic Taylor lower bound gives \(e^{7/10}>1+7/10+(7/10)^2/2+(7/10)^3/6>2\), so \(\log2<7/10<57/80\). Thus both CDNCEx components of \(\mathbf Y\) are strictly larger at \((2,2)\), contradicting \(\mathbf X\geq_{\mathrm{CDNCEx}}\mathbf Y\).

The mechanism is visible directly in the published proof. After the substitution \(y_1=\psi_1(x_1)\), its integral contains the nonnegative integrand multiplied by \(\psi_1'(x_1)\). Since the same paper's dispersive-order definition states \(\psi_1'(x_1)\geq1\), dropping that factor cannot justify an upper bound; the displayed comparison is in the wrong direction at that step.

## Verification
The exact symbolic formulas above prove the claim. The accompanying dependency-free checker evaluates the same closed forms at high precision, verifies positivity of the exact difference, and separately certifies the rational Taylor bound used to show \(\log2<7/10\). Its output is supplementary and is not used as a substitute for the analytic proof.

The general dilation identity follows directly from the CDNCEx definition by setting \(y_i=c_ix_i\). It also agrees with the affine transformation law stated earlier in the motivating paper.

## Relationship to prior work
Pandey and Kundu introduced the vector-valued CDNCEx measure, its associated stochastic order, and Theorem 3.13 asserting that componentwise dispersive domination together with increasing CDNCEx implies the reverse CDNCEx order. Their earlier affine-transformation theorem records the scale factor that drives the counterexample, but the paper does not state this contradiction or a counterexample to Theorem 3.13.

Tahmasebi and Toomaj introduced negative cumulative extropy and conditional negative cumulative extropy in the univariate setting. Searches for the exact implication, its dilation specialization, and equivalent negative-cumulative-extropy/dispersive-order formulations did not locate a prior counterexample or corrected theorem.

## Limitations
This result refutes the stated implication; it does not classify additional hypotheses under which a dispersive-order implication for CDNCEx might hold. The construction uses independent exponential components and a common dilation by two, which is sufficient for a counterexample but does not describe all failure mechanisms. Older equivalent observations under different terminology remain a residual literature risk.

## References
A. Pandey and C. Kundu, “On the study of bivariate and conditional dynamic negative cumulative extropy,” Probability in the Engineering and Informational Sciences, published online 7 April 2026, DOI 10.1017/S0269964826100242.

S. Tahmasebi and A. Toomaj, “On negative cumulative extropy with applications,” Communications in Statistics - Theory and Methods, published online 18 October 2020, DOI 10.1080/03610926.2020.1831541.
