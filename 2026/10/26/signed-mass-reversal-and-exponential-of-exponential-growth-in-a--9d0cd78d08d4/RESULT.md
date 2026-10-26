# Signed mass reversal and exponential-of-exponential growth in a two-stage positive deferred-correction step

## Finding

Consider the bounded two-compartment exchange system
\[
\dot u=a(v-u),\qquad \dot v=a(u-v),\qquad (u(0),v(0))=(x,y),
\]
where \(a,x,y>0\). Its exact flow is strictly positive and conserves \(m=x+y\) for all positive times. Apply the two-node Gauss–Lobatto version of the Stable Positive Integral Deferred Correction (SPIDeC) method with **exactly one correction sweep**, the second-order SPIDeC-GL(2) specialization defined in Pezzella (2026). Put \(r=y/x\) and \(s=ah\), with arbitrary positive step \(h\).

For every \(s>0\), its predictor and corrected endpoint are strictly positive. Their total masses \(M_0(s)\) and \(M_1(s)\) satisfy the following **complete nonequilibrium large-step and small-step statements** whenever \(r\ne1\):

1. The predictor strictly increases mass, \(M_0(s)>m\), for **every** positive \(s\), and
   \[
   \lim_{s\to\infty}\frac{\log(M_0(s)/m)}s
      =\max\{r,r^{-1}\}-1.
   \]
2. The single corrected endpoint has a **negative** mass defect at all sufficiently small positive steps:
   \[
   M_1(s)-m=-\frac{m(r-1)^4}{12r^2}\,s^3+O_{x,y}(s^4).
   \]
   In contrast, its mass grows on an **exponential-of-exponential scale** as the step tends to infinity:
   \[
   \boxed{\lim_{s\to\infty}
    \frac{\log(M_1(s)/m)}{s\exp\bigl(s|r-r^{-1}|\bigr)}
    =\frac12\min\{r,r^{-1}\}>0.}
   \]
   Consequently at least one finite positive step has exactly zero corrected mass defect, with strict mass loss at small steps and arbitrarily large mass creation at large steps. No uniqueness of a zero is claimed.

If \(r=1\), both numerical endpoints instead equal the initial equilibrium exactly for every \(s>0\).

A concrete exact example is \(x=2\), \(y=1\), \(a=1\): the corrected values after one step are
\[
 u_1=2\exp\!\left(\frac h4e^{3h/2}-\frac{3h}4\right),\qquad
 v_1=\exp\!\left(he^{-3h/2}\right).
\]
The exact mass is always \(3\), whereas the numerical mass already exceeds \(10^4\) at \(h=2\), despite both numerical components being positive.

## Assumptions and scope

All statements concern exact real arithmetic, one step, a positive exchange rate, positive initial components, fixed two-node Gauss–Lobatto quadrature nodes \(0\) and \(1\), and exactly one explicit correction sweep. The per-capita logarithmic rates are evaluated at the previous sweep's nodes as specified in the original SPIDeC construction. The primary subject is numerical integration of an ordinary differential-equation initial-value problem (MSC2020 65L05).

The true solution is
\[
 u(t)=\frac m2+\frac{x-y}{2}e^{-2at},\qquad
 v(t)=\frac m2-\frac{x-y}{2}e^{-2at};
\]
its components remain in \((0,m)\), and the mass remains exactly \(m\).

## Proof

**Step 1: exact numerical stages.** For the two interpolation nodes \(0,1\), the integrated Lagrange weights at the final node are \(Q_{1,0}=Q_{1,1}=1/2\). For each positive vector \(w=(u,v)\), define its componentwise logarithmic rates
\[
 g_1(w)=a(v/u-1),\qquad g_2(w)=a(u/v-1).
\]
The source's predictor and its first correction sweep are therefore, component by component,
\[
 (u_p,v_p)=(xe^{h g_1(x,y)},ye^{h g_2(x,y)}),
 \qquad (u_1,v_1)=\left(
 x e^{\frac h2[g_1(x,y)+g_1(u_p,v_p)]},
 y e^{\frac h2[g_2(x,y)+g_2(u_p,v_p)]}\right).
\]
With \(R=v_p/u_p\), direct substitution gives
\[
 R=r\exp\bigl(s(r^{-1}-r)\bigr),\quad
 u_1=x\exp\bigl(\tfrac s2(r+R-2)\bigr),\quad
 v_1=y\exp\bigl(\tfrac s2(r^{-1}+R^{-1}-2)\bigr).
\]
These equalities prove positive stage values for every finite \(s>0\) and are the formulas used in all subsequent steps.

**Step 2: the predictor always overproduces mass.** Its total is
\[
 M_0(s)=x e^{s(r-1)}+y e^{s(r^{-1}-1)}.
\]
The weighted mean of the two exponents is zero, since
\(x(r-1)+y(r^{-1}-1)=0\). Strict convexity of the exponential, with both weights positive, therefore gives \(M_0(s)>x+y\) whenever \(r\ne1\). In the same case exactly one exponent is positive, and it dominates as \(s\to\infty\). Dividing its logarithm by \(s\) yields \(\max\{r,r^{-1}\}-1\).

**Step 3: the corrected small-step sign.** Substitute the expression for \(R\) into the two exponentials in Step 1. With \(d=r^{-1}-r\), their exponents expand as
\[
 \begin{aligned}
 \log(u_1/x)&=s(r-1)+\tfrac{rd}{2}s^2+\tfrac{rd^2}{4}s^3+O_r(s^4),\\
 \log(v_1/y)&=s(r^{-1}-1)-\tfrac{d}{2r}s^2+\tfrac{d^2}{4r}s^3+O_r(s^4).
 \end{aligned}
\]
Expanding their exponentials and collecting terms, the coefficients of \(s\) and \(s^2\) in \(M_1(s)-m\) cancel exactly, while the cubic coefficient factors as
\[
 -x\frac{(r-1)^4(r+1)}{12r^2}
 =-m\frac{(r-1)^4}{12r^2}.
\]
This is strictly negative for every fixed \(r>0\), \(r\ne1\), so the corrected endpoint loses mass for all sufficiently small positive steps. The Taylor identities are also independently checked by symbolic algebra in `verify.py`.

**Step 4: exact large-step growth.** When \(0<r<1\), let \(d=r^{-1}-r>0\). The exact exponents from Step 1 obey
\[
 \log u_1=\log x+\tfrac{sr}{2}e^{ds}+\tfrac{s(r-2)}2,
 \qquad
 \log v_1=\log y+\tfrac{s}{2r}e^{-ds}+\tfrac{s(r^{-1}-2)}2.
\]
Thus \(\log u_1\sim\frac{sr}{2}e^{ds}\), whereas \(\log v_1=O(s)\). In particular \(u_1/v_1\to\infty\), so \(\log M_1(s)=\log u_1+o(1)\). Dividing by \(s e^{ds}\) gives \(r/2\). For \(r>1\), interchange the two compartments (equivalently replace \(r\) by \(r^{-1}\)), obtaining \(1/(2r)\). These are exactly the two cases of the boxed limit. Since \(M_1(s)\) is continuous, is below \(m\) for sufficiently small \(s>0\), and eventually diverges above \(m\), the intermediate value theorem guarantees at least one positive crossing.

**Step 5: equilibrium case.** If \(r=1\), both per-capita rates vanish and all displayed predictor/corrector stages equal \((x,y)\) identically.

## Verification

`verify.py` reproduces the predictor/correction from the differential vector field, algebraically compares it with the closed forms, verifies the four Taylor coefficients through degree three with exact symbolic simplification, checks the predictor coefficient, and performs high-precision sign and logarithmic-asymptotic diagnostics on multiple fixed positive ratios. Run `python verify.py` with Python 3.10+, SymPy and mpmath. Its reported execution result is **324 successful symbolic and finite assertions**. The proof in the preceding section, not finite sampling, establishes the universal conclusions.

## Relationship to prior work

Pezzella's 2026 article defines SPIDeC through a componentwise exponential Volterra discretization and proves unconditional positive stages (Theorem 3.1) and exact integration of scalar/diagonal linear equations (Theorem 5.1). Its Gauss–Lobatto second-order specialization with one correction sweep is precisely the method examined here. The source does not state the signed mass-reversal and exponential-of-exponential transfer-system formula. Its diagonal linear semigroup result does **not** imply a result for non-diagonal Markov generators; its nonlinear contractivity results require additional dissipativity hypotheses.

Öffner and Torlo's 2019/2020 modified-Patankar deferred-correction approach enforces mass conservation by a different, flux-weighted discretization. Torlo, Öffner and Ranocha (2021) investigate stability problems of Patankar-type schemes on a related two-compartment exchange equation, but their update mechanisms are not the componentwise exponential SPIDeC sweep analyzed here. Öffner, Redle and Torlo (2026) again develop mass-conservative modified-Patankar deferred correction in a different balance-law setting. These results motivate checking conservation separately from positivity and do not directly imply the new exact asymptotic statement.

## Limitations

The result does not show that the SPIDeC algorithm is generally unstable, nor that the original paper claims mass conservation: neither implication is asserted. It does not apply to modified Patankar schemes, other node sets, more correction sweeps, a converged collocation solve, non-exchange systems, or floating-point overflow behavior. It does not prove uniqueness or monotonicity of the finite mass-defect crossing. The large-step limit fixes the initial ratio before allowing the step to grow; no uniform estimate near equilibrium is claimed. Literature search and source comparison cannot exclude every earlier unpublished or specialized equivalent.

## References

1. M. Pezzella, *Stable Positive Integral Deferred Correction Methods for Positive Dynamical Systems*, arXiv:2606.29523, first public June 28, 2026. https://arxiv.org/abs/2606.29523
2. P. Öffner and D. Torlo, *Arbitrary high-order, conservative and positive preserving Patankar-type deferred correction schemes*, arXiv:1905.09237, first public May 22, 2019. https://arxiv.org/abs/1905.09237
3. D. Torlo, P. Öffner and H. Ranocha, *Issues with Positivity-Preserving Patankar-type Schemes*, arXiv:2108.07347, first public August 16, 2021. https://arxiv.org/abs/2108.07347
4. P. Öffner, M. Redle and D. Torlo, *High-order positivity-preserving well-balanced schemes: combining flux globalization with modified Patankar deferred correction methods*, arXiv:2610.21857, first public October 15, 2026. https://arxiv.org/abs/2610.21857
