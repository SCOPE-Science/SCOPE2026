# Opposite-sign Milstein corrections reduce the printed SIRS scheme to strong order one-half
## Finding
Huang, Du, and Liang state that their numerical experiments use the Milstein method and cite Higham's formulation. In Model (4.1), each diagonal diffusion coefficient has the form \(g_i(x)=-q_i x\), where \(q_i>0\). Equation (4.3), however, prints the stochastic Taylor correction with a minus sign:
\[
-\frac12 q_i^2X_i^n\bigl((\Delta W_i^n)^2-h\bigr).
\]
For \(g_i(x)=-q_i x\), one has \(g_i(x)g_i'(x)=q_i^2x\), so the Milstein correction required by the cited formula is instead
\[
+\frac12 q_i^2X_i^n\bigl((\Delta W_i^n)^2-h\bigr).
\]
The sign difference is not merely cosmetic. On the scalar multiplicative-noise equation \(dX_t=-qX_t\,dW_t\), the printed-sign recurrence has exact root-mean-square strong order \(1/2\), while the correct-sign Milstein recurrence has order \(1\).

## Assumptions and scope
Let \(q>0\), \(X_0>0\), \(T>0\), \(N\in\mathbb N\), and \(h=T/N\). Let \(Z_1,\ldots,Z_N\) be independent standard normal variables and set \(r=q^2h\). The exact solution of \(dX_t=-qX_t\,dW_t\) is
\[
X_T=X_0\exp\left(-qW_T-\frac12q^2T\right).
\]
The printed-sign recurrence is
\[
X_{n+1}^-=X_n^-\left[1-q\sqrt h Z_{n+1}-\frac12q^2h(Z_{n+1}^2-1)\right].
\]
This scalar equation is used only as an exact convergence test for the sign pattern appearing in Eq. (4.3). The finding does not claim that the authors' executable code, which was not inspected, used the printed sign.

## Proof
For one step define
\[
M_-(Z)=1-\sqrt r Z-\frac r2(Z^2-1),\qquad E(Z)=\exp(-\sqrt r Z-r/2).
\]
Standard Gaussian moments give
\[
\mathbb E[M_-(Z)^2]=1+r+\frac{r^2}{2},\qquad
\mathbb E[E(Z)^2]=e^r,
\]
and exponential tilting gives
\[
\mathbb E[M_-(Z)E(Z)]=1+r-\frac{r^2}{2}.
\]
Independence over the \(N\) steps therefore yields the exact identity
\[
\mathbb E|X_N^- - X_T|^2
=X_0^2\left[(1+r+r^2/2)^N+e^{Nr}-2(1+r-r^2/2)^N\right].
\]
Because \(r=q^2h\) and \(N=T/h\),
\[
N\log(1+r+r^2/2)=q^2T+O(h^2),
\]
while
\[
N\log(1+r-r^2/2)=q^2T-q^4Th+O(h^2).
\]
Substitution gives
\[
\mathbb E|X_N^- - X_T|^2
=2X_0^2e^{q^2T}q^4Th+O(h^2),
\]
so the root-mean-square error is \(\Theta(h^{1/2})\).

For comparison, the correct-sign multiplier
\[
M_+(Z)=1-\sqrt r Z+\frac r2(Z^2-1)
\]
satisfies
\[
\mathbb E[M_+(Z)^2]=\mathbb E[M_+(Z)E(Z)]=1+r+\frac{r^2}{2}.
\]
Hence
\[
\mathbb E|X_N^+ - X_T|^2
=X_0^2\left[e^{Nr}-(1+r+r^2/2)^N\right]
=\frac16X_0^2e^{q^2T}q^6Th^2+O(h^3),
\]
which is root-mean-square order \(1\).

## Verification
The accompanying `verify.py` evaluates the exact finite-step formulas at decreasing step sizes and checks that the printed-sign mean-square error divided by \(h\) converges to \(2e^{q^2T}q^4T\), whereas the correct-sign mean-square error divided by \(h^2\) converges to \(e^{q^2T}q^6T/6\). It also checks positivity of both exact error expressions on the tested mesh sequence.

The source PDF was inspected at Section 4, where Model (4.1) has diffusion terms \(-\varepsilon\sigma_iX_i\,dB_i\) and Eq. (4.3) prints a negative second-order correction for all three coordinates. Higham's Eq. (6.1), which the source cites as reference [33], has the correction \(+\frac12gg'((\Delta W)^2-h)\).

## Relationship to prior work
Higham's 2001 article supplies the standard Milstein formula and the classical distinction between strong order \(1/2\) for Euler–Maruyama and strong order \(1\) for Milstein. That general formula immediately determines the correct sign once the source diffusion field is differentiated. The additional statement here is the source-specific diagnosis together with an exact finite-horizon error law for the opposite-sign recurrence, showing quantitatively that the printed sign loses the first-order Milstein property on the canonical multiplicative-noise test.

Searches for the source DOI, title, Eq. (4.3), the phrases “Milstein correction sign” and “opposite-sign Milstein,” and equivalent geometric-noise formulations did not locate a publication stating this source-specific error law. Existing records concerning the same SIRS article address different issues: disease-free pathwise convergence and the correlated-noise covariance equation, not its numerical Milstein recurrence.

## Limitations
This finding is about the recurrence as printed in Eq. (4.3). No author simulation code was located and inspected, so the result does not establish that the figures were generated with the wrong sign. It also does not invalidate the article's analytical extinction, persistence, or stochastic-sensitivity theorems. The exact \(h^{1/2}\) result is proved for the scalar multiplicative-noise test; for the full nonlinear SIRS system the verified statement is the sign mismatch in the local Milstein correction.

## References
1. J. Huang, J. Du, H. Liang, “Dynamics and stochastic sensitivity technique of a stochastic SIRS epidemic model,” *AIMS Mathematics* 11 (2026), 6720–6743. DOI: 10.3934/math.2026278. See Section 4, Model (4.1), Eq. (4.3), and reference [33].
2. D. J. Higham, “An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations,” *SIAM Review* 43 (2001), 525–546. DOI: 10.1137/S0036144500378302. See Eq. (6.1).
