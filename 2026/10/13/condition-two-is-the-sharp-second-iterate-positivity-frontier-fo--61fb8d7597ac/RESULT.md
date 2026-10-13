# Condition two is the sharp second-iterate positivity frontier for the Barzilai–Borwein interval
## Finding
Consider
\[
f(x)=\frac12x^{\mathsf T}Ax-b^{\mathsf T}x,
\]
where \(A=A^{\mathsf T}>0\) is a Stieltjes matrix and \(b\ge0\). Start from \(x^{(0)}=0\) with one exact-line-search gradient step
\[
x^{(1)}=\alpha_0b,
\qquad
\alpha_0=\frac{b^{\mathsf T}b}{b^{\mathsf T}Ab}.
\]
From \(s_0=x^{(1)}-x^{(0)}\) and \(y_0=\nabla f(x^{(1)})-\nabla f(x^{(0)})\), define the long and short Barzilai–Borwein steps
\[
\alpha_1^{\mathrm L}=\frac{s_0^{\mathsf T}s_0}{s_0^{\mathsf T}y_0},
\qquad
\alpha_1^{\mathrm S}=\frac{s_0^{\mathsf T}y_0}{y_0^{\mathsf T}y_0}.
\]
Choose any second stepsize
\[
\alpha_1\in[\alpha_1^{\mathrm S},\alpha_1^{\mathrm L}].
\]
If
\[
\kappa(A)=\frac{\lambda_{\max}(A)}{\lambda_{\min}(A)}\le2,
\]
then both \(x^{(1)}\) and \(x^{(2)}\) are componentwise nonnegative for every dimension, every \(b\ge0\), and every choice in the full BB interval.

This constant is sharp. For every \(\kappa>2\), one two-dimensional diagonal positive definite quadratic with a strictly positive right-hand side makes the second iterate negative in one coordinate for **every** choice between the short and long BB steps. Hence dimension two and iteration two are jointly minimal for this positivity loss.

## Assumptions and scope
All statements use exact real arithmetic, an SPD Stieltjes Hessian, zero initial point, and an exact line search only for the warm-start step. The second step may be either classical BB endpoint or any stepsize between them. The statement concerns coordinatewise nonnegativity of the raw unconstrained iterate; it does not concern projected BB methods, later iterates, nonsymmetric matrices, or inexact line searches.

Write
\[
\mu=\lambda_{\min}(A),\qquad L=\lambda_{\max}(A).
\]
A Stieltjes matrix has nonpositive off-diagonal entries, so once a shift \(\theta I-A\) has nonnegative diagonal it is entrywise nonnegative.

## Proof
Because \(x^{(0)}=0\), the initial gradient is \(-b\), and exact line search gives
\[
\alpha_0=\frac{b^{\mathsf T}b}{b^{\mathsf T}Ab},
\qquad
x^{(1)}=\alpha_0b\ge0.
\]
Moreover
\[
s_0=\alpha_0b,
\qquad
y_0=\alpha_0Ab.
\]
Therefore
\[
\alpha_1^{\mathrm L}
=\frac{b^{\mathsf T}b}{b^{\mathsf T}Ab}
=\alpha_0,
\qquad
\alpha_1^{\mathrm S}
=\frac{b^{\mathsf T}Ab}{b^{\mathsf T}A^2b}.
\]
Cauchy--Schwarz gives \(\alpha_1^{\mathrm S}\le\alpha_1^{\mathrm L}\).

For any \(\alpha_1\) in this interval,
\[
\begin{aligned}
x^{(2)}
&=x^{(1)}-\alpha_1\nabla f(x^{(1)})\\
&=\alpha_0b+\alpha_1(b-\alpha_0Ab)\\
&=\alpha_0\alpha_1(\theta I-A)b,
\end{aligned}
\]
where
\[
\theta=\frac1{\alpha_0}+\frac1{\alpha_1}.
\]
Since \(\alpha_1\le\alpha_1^{\mathrm L}=\alpha_0\),
\[
\theta\ge\frac2{\alpha_0}
=2\frac{b^{\mathsf T}Ab}{b^{\mathsf T}b}
\ge2\mu.
\]
If \(L/\mu\le2\), then \(\theta\ge L\). Hence \(\theta I-A\) is entrywise nonnegative: its off-diagonal entries are \(-a_{ij}\ge0\), and its diagonal entries satisfy \(\theta-a_{ii}\ge\theta-L\ge0\). Therefore \(x^{(2)}\ge0\).

For sharpness, fix \(\kappa>2\) and take
\[
A=\operatorname{diag}(1,\kappa),
\qquad
b=(1,\varepsilon)^{\mathsf T},
\qquad
t=\varepsilon^2>0.
\]
The reciprocal warm-start step and reciprocal short BB step are
\[
\frac1{\alpha_0}=\frac{1+\kappa t}{1+t},
\qquad
\frac1{\alpha_1^{\mathrm S}}=\frac{1+\kappa^2t}{1+\kappa t}.
\]
Thus the largest possible shift \(\theta\) over the BB interval occurs at the short endpoint and satisfies
\[
(\theta_{\mathrm S}-\kappa)(1+t)(1+\kappa t)
=\kappa^2t^2+(\kappa+1)t+2-\kappa.
\]
The quadratic on the right is negative for
\[
0<t<t_*(\kappa),
\qquad
 t_*(\kappa)=
\frac{\sqrt{4\kappa^3-7\kappa^2+2\kappa+1}-(\kappa+1)}{2\kappa^2}.
\]
Because \(\kappa>2\), this interval is nonempty. For such \(t\), \(\theta_{\mathrm S}<\kappa\). Every interval choice has \(\alpha_1\ge\alpha_1^{\mathrm S}\), hence \(1/\alpha_1\le1/\alpha_1^{\mathrm S}\) and \(\theta\le\theta_{\mathrm S}<\kappa\). The second coordinate of
\[
\alpha_0\alpha_1(\theta I-A)b
\]
is therefore strictly negative. One dimension cannot fail because both BB steps reduce to the reciprocal scalar curvature and recover the exact minimizer.

For the exact witness
\[
A=\operatorname{diag}(1,4),
\qquad b=(1,1/10)^{\mathsf T},
\]
we have
\[
\alpha_0=\alpha_1^{\mathrm L}=\frac{101}{104},
\qquad
\alpha_1^{\mathrm S}=\frac{26}{29}.
\]
At the short endpoint,
\[
x^{(2)}=
\left(\frac{3007}{3016},-\frac{4871}{30160}\right)^{\mathsf T},
\]
and at the long endpoint,
\[
x^{(2)}=
\left(\frac{10807}{10816},-\frac{4949}{27040}\right)^{\mathsf T}.
\]
The preceding shift argument proves negativity for every intermediate interval choice, not merely these two endpoints.

## Verification
The analytic proof supplies the universal quantifiers and the sharp family. The accompanying exact-rational script independently replays the warm-start formulas, the long/short BB steps, the factorization of \(x^{(2)}\), the polynomial sign condition for the witness, and both endpoint iterates. It is corroborative only; no finite computation is used to prove the theorem for all dimensions or all \(\kappa\).

## Relationship to prior work
Barzilai--Borwein spectral gradient steps and their delayed-curvature interpretation are classical. Birgin, Martínez, and Raydan review the BB iteration and note that on SPD quadratics the long BB step used at the next iteration is the previous Cauchy exact-line step. Later spectral-gradient literature treats both long and short BB steps and convex combinations between them, with convergence and objective behavior as the main invariants.

A closely related published result gives \(\kappa=2\) as the sharp objective-monotonicity frontier for steps chosen in the BB interval after an exact-line warm start. Objective monotonicity and coordinatewise nonnegativity are not implication-equivalent: an iterate can stay in the nonnegative orthant while increasing the objective, or leave the orthant while decreasing it. The present theorem instead identifies an entrywise Stieltjes mechanism, proves positivity for the whole interval when \(\kappa\le2\), and gives a single two-dimensional family that defeats every interval choice when \(\kappa>2\).

The motivation is also distinct from projected spectral-gradient methods for nonnegative problems. Those methods enforce feasibility by projection or modify the spectral step. Here the raw unconstrained BB step is classified before any projection is applied.

## Limitations
Only the second post-warm-start iterate is classified. Later BB dynamics are nonlinear because each spectral step depends on delayed secant data and are not covered. The exact-line warm start is essential to the closed formulas. The theorem is for symmetric positive definite Stieltjes matrices; no claim is made for general SPD matrices, nonsymmetric \(M\)-matrices, or arbitrary cones.

The BB literature is large. Focused searches did not locate an implication-equivalent coordinatewise theorem, but older spectral-gradient or monotone-iteration work under different terminology remains a residual originality risk.

## References
1. E. G. Birgin, J. M. Martínez, and M. Raydan, *Spectral Projected Gradient Methods: Review and Perspectives*, Journal of Statistical Software 60(3), 2014, DOI: 10.18637/jss.v060.i03.
2. J. Barzilai and J. M. Borwein, *Two-Point Step Size Gradient Methods*, IMA Journal of Numerical Analysis 8(1), 1988, 141--148, DOI: 10.1093/imanum/8.1.141.
3. Y. Dai, Y. Huang, and X. Liu, *A Family of Spectral Gradient Methods for Optimization*, Computational Optimization and Applications 74, 2019, 43--65, DOI: 10.1007/s10589-019-00107-8.
