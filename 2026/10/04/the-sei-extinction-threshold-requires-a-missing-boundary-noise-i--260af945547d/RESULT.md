# The SEI extinction threshold requires a missing boundary-noise integrability condition
## Finding
For the one-dimensional boundary diffusion
\[
dZ(t)=rZ(t)\left(1-\frac{Z(t)}{K}\right)dt+Z(t)\left(\sigma_{11}+\sigma_{12}Z(t)\right)dB(t),
\]
with \(r,K,\sigma_{11},\sigma_{12}>0\), the invariant-density expression printed in Lemma 4.1 of Xu and Wang is normalizable on \((0,\infty)\) if and only if
\[
r>\frac{\sigma_{11}^2}{2}.
\]
Consequently, the extinction threshold \(R_0^E\) defined in Section 4 and Theorem 4.2 require at least this additional hypothesis. When \(r\le \sigma_{11}^2/2\), the displayed density cannot be normalized to a probability density, so the integral defining \(R_0^E\) is not defined as stated.

## Assumptions and scope
All four parameters \(r,K,\sigma_{11},\sigma_{12}\) are positive, as in the stochastic model. The conclusion concerns exactly the density displayed in Lemma 4.1 and the use of that density in the threshold and extinction theorem. It does not classify the boundary diffusion or the epidemic model in the excluded regime, and it does not claim that extinction fails there.

The earlier stationary-distribution result in Theorem 3.3 assumes
\[
\sigma_{11}^2+2K\sigma_{11}\sigma_{12}+K^2\sigma_{12}^2<2r,
\]
which is stronger than \(r>\sigma_{11}^2/2\). However, Section 4 begins a separate extinction analysis, and Lemma 4.1 and Theorem 4.2 do not state the Theorem 3.3 hypothesis. The correction therefore applies to Theorem 4.2 as printed rather than to parameter sets that independently satisfy the stronger Theorem 3.3 condition.

## Proof
Write the printed density, up to its normalization factor, as
\[
\pi(z)=Qz^q\left(\sigma_{11}+\sigma_{12}z\right)^h
\exp\!\left(\frac{C}{\sigma_{11}+\sigma_{12}z}\right),
\]
where
\[
q=-2+\frac{2r}{\sigma_{11}^2},\qquad
h=-2-\frac{2r}{\sigma_{11}^2},\qquad
C=\frac{2r(\sigma_{11}+K\sigma_{12})}{K\sigma_{11}\sigma_{12}}.
\]
As \(z\downarrow0\), both \((\sigma_{11}+\sigma_{12}z)^h\) and the exponential factor converge to finite positive constants. Hence
\[
\pi(z)\sim C_0z^{-2+2r/\sigma_{11}^2}
\]
for some \(C_0>0\). The endpoint criterion \(\int_0^\varepsilon z^a\,dz<\infty\) exactly when \(a>-1\) therefore gives
\[
\int_0^\varepsilon\pi(z)\,dz<\infty
\quad\Longleftrightarrow\quad
-2+\frac{2r}{\sigma_{11}^2}>-1
\quad\Longleftrightarrow\quad
r>\frac{\sigma_{11}^2}{2}.
\]
At equality the divergence is logarithmic; below equality it is a power divergence.

At the other endpoint, the powers add exactly:
\[
q+h=-4,
\]
and the exponential tends to one. Thus
\[
\pi(z)\sim C_\infty z^{-4}
\]
for some \(C_\infty>0\), which is integrable at infinity. Hence the condition at zero is both necessary and sufficient for normalization of the displayed density.

Lemma 4.1 states that a constant \(Q\) normalizes this density to total mass one without adding the condition above. Immediately afterward, Section 4 defines \(R_0^E\) using an integral against \(\pi\), and Theorem 4.2 assumes only \(R_0^E<0\) before using the same invariant law in its conclusion. Therefore, when \(r\le\sigma_{11}^2/2\), the theorem's displayed threshold lacks the probability density needed to define it. Adding \(r>\sigma_{11}^2/2\) repairs this domain defect at the level of Lemma 4.1 and the threshold definition.

## Verification
The standalone checker `verify.py` performs exact-rational endpoint checks. It verifies the identity \(q+h=-4\), verifies that the critical choice \(r=\sigma_{11}^2/2\) gives \(q=-1\), and checks the paper's extinction-example values \(r=1/2\), \(\sigma_{11}=3/5\), for which \(\sigma_{11}^2/2=9/50<1/2\). These finite checks support the algebra; the if-and-only-if statement itself follows from the endpoint asymptotics and the exact power-integrability criterion above.

## Relationship to prior work
Xu and Wang cite Liu, Jiang, Hayat, and Ahmad (2018) for Lemma 4.1. Publicly available bibliographic material confirms that the cited predecessor studies stationary distribution and extinction for nonlinear stochastic perturbations, but its full text was not available through the checked open sources. A later predator-prey paper by Zhang and Yang (2022) explicitly treats extinction and exponential ergodicity thresholds for a one-dimensional logistic system with nonlinear perturbations, showing that the boundary logistic classification is established literature. Neither inspected source states the source-specific conclusion here: that the particular density inserted into Xu and Wang's \(R_0^E\) is nonnormalizable on part of Theorem 4.2's printed parameter domain.

Searches of the source title, DOI, correction/erratum terms, the density-normalization condition, and semantically related database records found no published correction that supplies the missing condition to Theorem 4.2. The originality claimed here is therefore the theorem-domain diagnosis and its exact necessary-and-sufficient normalization condition for the displayed density, not the general fact that multiplicative noise can shift logistic persistence thresholds.

## Limitations
The result does not determine the long-time law of \(Z(t)\) when \(r\le\sigma_{11}^2/2\), and it does not prove or disprove epidemic extinction in that regime by another criterion. It also does not invalidate the paper's numerical extinction examples: their reported values \(r=0.5\) and \(\sigma_{11}=0.6\) satisfy the required inequality because \(0.5>0.18\). The cited 2018 predecessor could not be inspected in full text after public-access attempts; this leaves a residual bibliographic risk about whether that older paper states the boundary condition explicitly, but it does not alter the direct integrability calculation or the omission in the 2025 theorem statement.

## References
1. Z. Xu and L. Wang, “Stationary distribution and extinction of a stochastic SEI epidemic model with logistic growth and nonlinear perturbation,” *AIMS Mathematics* 10(12), 28488–28513 (2025), DOI 10.3934/math.20251254.
2. Q. Liu, D. Jiang, T. Hayat, and B. Ahmad, “Stationary distribution and extinction of a stochastic predator-prey model with additional food and nonlinear perturbation,” *Applied Mathematics and Computation* 320, 226–239 (2018), DOI 10.1016/j.amc.2017.09.030.
3. X. Zhang and Q. Yang, “Dynamical behavior of a stochastic predator-prey model with general functional response and nonlinear jump-diffusion,” *Discrete and Continuous Dynamical Systems - B* 27(6), 3155–3175 (2022), DOI 10.3934/dcdsb.2021177.
