# Complete positive-start phase diagram for optimized two-step stiff integrators

## Finding
Let \(0\le\kappa<1\), \(z>0\), and set
\[
D=(3-\kappa)(1+\kappa),\quad
A=\frac{4(1-\kappa^2-\kappa z)}{D+2z},\quad
B=\frac{(1-3\kappa)(1+\kappa)+2\kappa^2z}{D+2z}.
\]
For *every* strictly positive pair \((y_0,y_1)\), apply the constant-step scalar-decay recurrence
\[
y_{n+2}=Ay_{n+1}-By_n,\qquad n\ge0.
\]
Write \(w=y_1/y_0>0\). The set of ratios giving \(y_n\ge0\) for **all** integers \(n\ge0\) has the following complete classification. Define
\[
z_c=\frac{1+\kappa}{2(1-\kappa)},\qquad
z_a=\frac{1-\kappa^2}{\kappa}\ (\kappa>0),\qquad
z_b=\frac{(3\kappa-1)(1+\kappa)}{2\kappa^2}\ (\kappa>1/3),
\]
and, wherever the discriminant is nonnegative,
\[
\lambda_-=\frac{A-\sqrt{A^2-4B}}2,\qquad
\lambda_+=\frac{A+\sqrt{A^2-4B}}2.
\]

1. **\(0\le\kappa\le1/3\):** for \(0<z\le z_c\), precisely \(w\ge\lambda_-\) works; for \(z>z_c\), no positive ratio works.
2. **\(1/3<\kappa<1/2\):** every \(w>0\) works for \(0<z\le z_b\); precisely \(w\ge\lambda_-\) works for \(z_b<z\le z_c\); no positive ratio works above \(z_c\).
3. **\(\kappa=1/2\):** every \(w>0\) works for \(0<z\le3/2\); no positive ratio works for \(z>3/2\). At \(z=3/2\), every solution becomes zero after two steps.
4. **\(1/2<\kappa<1\):** every \(w>0\) works for \(0<z\le z_a\); precisely the *single tuned ratio* \(w=\lambda_+>0\) works for \(z_a<z<z_b\); no positive ratio works for \(z\ge z_b\).

Consequently the sharp interval \(0<z\le U(\kappa)\) on which **every** strictly positive two-step history remains nonnegative is determined by
\[
U(\kappa)=\begin{cases}
0,&0\le\kappa\le1/3,\\
\dfrac{(3\kappa-1)(1+\kappa)}{2\kappa^2},&1/3<\kappa\le1/2,\\
\dfrac{1-\kappa^2}{\kappa},&1/2\le\kappa<1.
\end{cases}
\]
It has the **unique maximizer** \(\kappa=1/2\), with \(U(1/2)=3/2\). The isolated positive-eigenmode strip for \(\kappa>1/2\) shows that positivity can survive beyond the all-start threshold, but only on a zero-width set of starting ratios: every positive perturbation away from that exact ratio eventually loses nonnegativity.

## Assumptions and scope
For the scalar equation \(y'=-\lambda y\), assume \(\lambda,h>0\), \(z=h\lambda\), constant step \(h\), exact-arithmetic evaluation, and the optimized second-order, two-step A-stable \(L(\kappa)\)-stable implicit multistep coefficients of Jensen–Ketcheson–Lóczi, Corollary 4.2 (2026):
\[
(\alpha_0,\alpha_1,\alpha_2)=\left(\frac{1-3\kappa}{3-\kappa},\frac{-4(1-\kappa)}{3-\kappa},1\right),\quad
(\beta_0,\beta_1,\beta_2)=\frac{(2\kappa^2,4\kappa,2)}{(3-\kappa)(1+\kappa)}.
\]
The update \(\sum_{j=0}^2\alpha_j y_{n+j}=h\sum_{j=0}^2\beta_j(-\lambda y_{n+j})\) is equivalent to the stated recurrence. The two positive starting values are *independently chosen* and need not lie on the exact solution curve. A zero future iterate is allowed.

## Proof
**1. Exact parameter ordering.** The characteristic polynomial is \(p(t)=t^2-At+B\), with
\[
A^2-4B=\frac{4(1+\kappa)^3[(1+\kappa)-2(1-\kappa)z]}{(D+2z)^2}.
\]
Thus its roots are distinct real for \(z<z_c\), equal real at \(z=z_c\), and nonreal conjugate for \(z>z_c\). The sign of \(A\) changes at \(z_a\) when \(\kappa>0\). The sign of \(B\) changes at \(z_b\) when \(\kappa>1/3\); for \(0\le\kappa\le1/3\), \(B>0\) at every positive \(z\). Exact subtraction gives
\[
z_b-z_a=\frac{(1+\kappa)^2(2\kappa-1)}{2\kappa^2},\qquad
z_c-z_b=\frac{(1+\kappa)(2\kappa-1)^2}{2\kappa^2(1-\kappa)}.
\]
The endpoint \(\kappa=1/2\) has \(z_a=z_b=z_c=3/2\) and \(A=B=0\). For smaller parameters with \(\kappa>1/3\), the ordering is \(z_b<z_c<z_a\); for larger parameters it is \(z_a<z_b<z_c\). The discriminant is strictly negative above \(z_c\).

**2. Elementary positive-start lemma.** For real coefficients \(A,B\) and \(y_0=1,y_1=w>0\), consider \(y_{n+2}=Ay_{n+1}-By_n\). If \(A\ge0\), \(B\le0\), all iterates are nonnegative by induction. If \(A>0\), \(B>0\), and there are real characteristic roots \(0<\lambda_-\le\lambda_+\), then all iterates are nonnegative exactly when \(w\ge\lambda_-\). For distinct roots, the solution is \(c_+\lambda_+^n+c_-\lambda_-^n\), with \(c_+=(w-\lambda_-)/(\lambda_+-\lambda_-)\). If \(w<\lambda_-\), the negative coefficient of the dominant root eventually dominates; if \(\lambda_-\le w\le\lambda_+\), both coefficients are nonnegative; if \(w>\lambda_+\), regroup as \(\lambda_+^n+c_-(\lambda_-^n-\lambda_+^n)>0\) with \(c_-<0\). For a repeated positive root \(\lambda\), the formula \(y_n=\lambda^n[1+n(w/\lambda-1)]\) yields exactly \(w\ge\lambda\).

If \(A<0,B<0\), the characteristic roots satisfy \(\lambda_-<0<\lambda_+<|\lambda_-|\). The negative dominant-root contribution causes a negative iterate for *every* positive \(w\ne\lambda_+\), whereas \(w=\lambda_+\) gives \(y_n=\lambda_+^n>0\). If \(A\le0,B\ge0\), except \(A=B=0\), already \(y_2=Aw-B<0\) (or \(y_2=0\) followed by a negative term in a degenerate boundary); in the present parameter family no problematic degenerate boundary of that kind occurs. Finally, nonreal conjugate roots \(re^{\pm i\theta}\) give \(y_n/r^n=\cos(n\theta)+c\sin(n\theta)\); some nonnegative integer \(n\) gives a negative value, because either the angles are dense modulo \(2\pi\) or their finite equally spaced orbit has average zero and includes the positive value at \(n=0\).

**3. Apply sign changes.** The exact orderings in Step 1 reduce the parameter ranges to the four cases in the Finding, using Step 2. At \(\kappa=1/2,z=3/2\), \(A=B=0\) and hence \(y_n=0\) for \(n\ge2\) independently of the positive starting history. In the case \(1/2<\kappa<1\), the interval \(z_a<z<z_b\) has \(A<0,B<0\), and hence only the positive eigenhistory survives.

**4. Optimality.** For \(1/3<\kappa<1/2\), differentiation gives \(z_b'(\kappa)=(1-\kappa)/\kappa^3>0\). For \(1/2<\kappa<1\), \(z_a'(\kappa)=-(1+\kappa^2)/\kappa^2<0\). Both branches attain \(3/2\) at \(\kappa=1/2\), establishing the unique optimum.

## Verification
Run `python VERIFY.py` with Python 3.10 or later and SymPy 1.12 or later. The verifier independently recomputes the coefficient-to-recurrence conversion, discriminant factorization, parameter-order inequalities and zero-at-endpoint algebra exactly, and replays representative startup cases with high-precision decimal exponentials. Its finite tests are supplementary, not proofs of the continuous parameter or infinite-index assertions; the proof above addresses those quantifiers. The machine-checked source and standalone script are included with this result.

## Relationship to prior work
Jensen–Ketcheson–Lóczi (2026), Corollary 4.2, establishes the optimized A-stable \(L(\kappa)\)-stable coefficients; it does **not** state the positive-start classification. General analyses of monotonicity-preserving implicit two-step methods (Hundsdorfer–Ruuth–Spiteri, 2002; Hundsdorfer–Mozartova–Spijker, 2010) address method coefficients and boundedness/monotonicity under different start models, including selected Runge–Kutta starts. Earlier special results for the same recent optimized family give the positive-decay threshold with a *backward-Euler* starter and, separately, a single exactly started parameter \(\kappa=3/5\). Those are single-history tests and do not characterize **all** positive starts, the half-line of admissible ratios, or the singleton eigenmode strip. The present claim does not assert that the classical quadratic-root solution formula is new; its contribution is the complete sharp specialization and startup-robustness phase diagram for the recently optimized numerical family.

## Limitations
The theorem concerns one positive scalar decay rate, constant steps, all-index nonnegativity and exact arithmetic. It gives no nonlinear SSP guarantee, positivity of a matrix propagator, a practical way to initialize at the isolated eigenratio without prior spectral knowledge, finite-precision protection, or an error estimate. The claim of originality is a literature comparison, not a proof of worldwide priority. A closely related uninspected archival paper or an unstated consequence of a general two-step theorem could reduce novelty.

## References
- T. Jensen, L. Lóczi and D. I. Ketcheson, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1 (first public October 15, 2026), especially Corollary 4.2 and equation (25). https://arxiv.org/abs/2610.22685
- W. H. Hundsdorfer, S. J. Ruuth and R. J. Spiteri, *Monotonicity-preserving linear multistep methods*, CWI Report MAS-R0210 (2002), especially Section 3.3. https://ir.cwi.nl/pub/4231/04231D.pdf
- W. Hundsdorfer, A. Mozartova and M. N. Spijker, *Stepsize restrictions for boundedness and monotonicity of multistep methods* (2010), especially Section 6.2. https://ir.cwi.nl/pub/16707/16707B.pdf
