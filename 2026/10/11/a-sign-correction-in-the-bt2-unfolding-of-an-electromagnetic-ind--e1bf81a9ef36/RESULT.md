# A sign correction in the BT2 unfolding of an electromagnetic-induction neuron model
## Finding
In the Bogdanov--Takens point \(BT_2\) calculation of Wen, Liu and Lu, the first-parameter sign in the constant term of equation (16) is inconsistent with the immediately preceding unfolding coefficients. The corrected local normal form is
\[
\dot\eta_1=\eta_2,
\]
\[
\dot\eta_2=-3.19889447\times10^8\,\bar\lambda_1
+1.99771215\times10^{10}\,\bar\lambda_2
+\eta_1^2
+\left(3.003345752\times10^5\,\bar\lambda_1-1.875860118\times10^7\,\bar\lambda_2\right)\eta_1
+s\eta_1\eta_2,
\]
to the displayed precision of the source. Equation (16) prints a positive coefficient on \(\bar\lambda_1\) in the constant term. That sign is the error; the remainder of the displayed reduced equation is not changed by this finding.

## Assumptions and scope
The claim concerns only the algebraic consistency of the published \(BT_2\) reduction near \((I_{ext},k_0)=(0.649385813300958,0.00912704116143242)\). It takes the paper's reported center-manifold coefficients and positive scaling constants as input. It does not independently rederive the \(BT_2\) point from the full four-dimensional conductance model, certify all numerical digits of the center-manifold calculation, or revalidate every bifurcation curve away from the local reduction.

## Proof
The paper gives
\[
\beta_1=-0.6956435964\lambda_1+43.44299811\lambda_2,
\qquad
\beta_2=0.2983460741\lambda_1-18.63440137\lambda_2,
\]
and reports \(a=4.537776612\times10^{-4}\) and \(b=0.4552873824\). Its normalization uses
\[
\bar\beta_1=\frac{b^4}{a^3}\beta_1,
\qquad
\bar\beta_2=\frac{b^2}{a^2}\beta_2.
\]
Both scale factors are positive. Therefore the coefficient of the first parameter in \(\bar\beta_1\) has the same negative sign as the coefficient in \(\beta_1\).

Replaying the displayed rounded data gives
\[
\frac{b^4}{a^3}(-0.6956435964)=-3.198894469717217\times10^8,
\]
\[
\frac{b^4}{a^3}(43.44299811)=1.997712149169358\times10^{10}.
\]
These agree, within the rounding inherited from the printed intermediate constants, with the coefficients printed just before Theorem 5.1. In particular, the sign is unambiguous.

There is a second, independent internal check. From the corrected constant term, \(\bar\beta_1=0\) has tangent
\[
\bar\lambda_1=62.4500798035\,\bar\lambda_2.
\]
The source's saddle-node formula has linear part
\[
-\bar\lambda_1+62.4500798\,\bar\lambda_2=0,
\]
which has the same tangent. If the positive sign printed in equation (16) were used literally, the tangent would instead be
\[
\bar\lambda_1=-62.4500798\,\bar\lambda_2,
\]
contradicting the source's own saddle-node curve. The homoclinic formula in the same theorem also retains the negative first coefficient. Hence the unique sign correction compatible with the paper's preceding derivation and its subsequent bifurcation curves is the negative sign stated above.

## Verification
The accompanying `verify.py` evaluates the normalization from the displayed decimal constants at high precision, checks the signs and coefficient magnitudes, reconstructs the normalized saddle-node polynomial from \(4\bar\beta_1-\bar\beta_2^2=0\), and verifies the positive tangent \(62.4500798\ldots\). It does not use a simulation or a fit.

## Relationship to prior work
The source paper develops the electromagnetic-induction endocrine-neuron model and explicitly analyzes \(BT_2\) using standard Bogdanov--Takens normal-form machinery. Carrillo, Verduzco and Delgado provide the general parameterized Bogdanov--Takens framework cited by the source; Kuznetsov gives standard bifurcation-theory background. Those general results do not contain the source-specific numerical unfolding coefficients or this sign comparison. Searches for the paper title, DOI, the distinctive coefficients, correction/erratum terminology, and equivalent saddle-node-tangent formulations located no public correction of equation (16). The closest indexed findings concern unrelated sign errors or other neuron normal forms and do not imply this source-specific correction.

## Limitations
The result is a correction to one displayed local normal-form coefficient, not a claim that the paper's qualitative numerical bifurcation diagram is wrong. Indeed, the source's listed saddle-node and homoclinic formulas already use the negative sign, so those formulas are internally consistent with the correction. An unindexed author note or later informal correction could reduce originality; none was found in the checked public sources. The checker uses the rounded constants printed in the paper, so it verifies the sign and displayed-scale arithmetic rather than hidden higher-precision source data.

## References
1. Q. Wen, S. Liu and B. Lu, “Firing patterns and bifurcation analysis of neurons under electromagnetic induction,” *Electronic Research Archive* 29 (2021), 3205--3226. DOI: 10.3934/era.2021034.
2. F. A. Carrillo, F. Verduzco and J. Delgado, “Analysis of the Takens--Bogdanov bifurcation on m-parameterized vector fields,” *International Journal of Bifurcation and Chaos* 20 (2010), 995--1005. DOI: 10.1142/S0218127410026277.
3. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd ed., Springer, 2004.
