# Sharp gradient-norm safety frontier inside Armijo sufficient decrease

## Finding
Consider the SPD quadratic
\[
f(x)
=
\frac12x^{\mathsf T}Ax-b^{\mathsf T}x,
\qquad
A=A^{\mathsf T}>0,
\]
with
\[
\kappa
=
\frac{\lambda_{\max}(A)}
{\lambda_{\min}(A)}.
\]
At a point with nonzero gradient
\[
g=Ax-b,
\]
perform a steepest-descent step
\[
x^+=x-\alpha g,
\qquad
\alpha>0,
\]
that satisfies the classical Armijo condition
\[
f(x-\alpha g)
\le
f(x)-\sigma\alpha\|g\|_2^2,
\qquad
0<\sigma<\frac12.
\]

The exact worst one-step gradient-norm factor is
\[
\boxed{
\sup
\frac{\|g^+\|_2^2}{\|g\|_2^2}
=
\max
\left\{
1,\;
4\sigma-3+
\frac{(1-\sigma)^2(\kappa+1)^2}{\kappa}
\right\}.
}
\]
The supremum ranges over all dimensions, all SPD matrices of condition number \(\kappa\), all nonzero current gradients, and all positive steps satisfying Armijo.

Therefore every accepted steepest-descent step is guaranteed to satisfy
\[
\|g^+\|_2\le\|g\|_2
\]
if and only if
\[
\boxed{
\sigma
\ge
\left(
\frac{\kappa-1}{\kappa+1}
\right)^2.
}
\]
Equivalently, for fixed \(\sigma\),
\[
\boxed{
\kappa
\le
\frac{1+\sqrt{\sigma}}
{1-\sqrt{\sigma}}.
}
\]

For example, with the common theoretical choice
\[
\sigma=\frac14,
\]
universal gradient-norm safety holds exactly through
\[
\kappa=3.
\]
At
\[
\kappa=4
\]
there is already a two-dimensional accepted step that increases the gradient norm.

The obstruction occurs in an ordinary backtracking implementation, not only among abstract admissible steps. For any prescribed first trial length \(s_0>0\), choose
\[
A=
\frac{(1-\sigma)(\kappa+1)}
{\kappa s_0}
\operatorname{diag}(1,\kappa)
\]
and
\[
g=
\begin{pmatrix}
\sqrt{\kappa}\\
1
\end{pmatrix}.
\]
Then the first trial
\[
\alpha=s_0
\]
satisfies the Armijo inequality at equality and realizes the sharp unsafe factor whenever that factor exceeds one.

A rational witness is
\[
\sigma=\frac14,
\qquad
\kappa=4,
\qquad
s_0=1,
\]
with
\[
A=
\operatorname{diag}
\left(
\frac{15}{16},
\frac{15}{4}
\right),
\qquad
b=0,
\qquad
x=
\begin{pmatrix}
32/15\\
4/15
\end{pmatrix}.
\]
Then
\[
g=
\begin{pmatrix}
2\\
1
\end{pmatrix}
\]
and the unit trial satisfies Armijo exactly. The objective falls from
\[
\frac{34}{15}
\]
to
\[
\frac{61}{60},
\]
while
\[
g^+
=
\begin{pmatrix}
1/8\\
-11/4
\end{pmatrix}
\]
and
\[
\frac{\|g^+\|_2^2}{\|g\|_2^2}
=
\frac{97}{64}.
\]

## Assumptions and scope
The theorem concerns exact arithmetic, real SPD quadratics, the ordinary negative-gradient search direction, and the monotone Armijo sufficient-decrease rule. The step need only satisfy Armijo; it need not satisfy a Wolfe curvature condition.

The condition number is spectral. Scaling \(A\) by a positive scalar leaves \(\kappa\) unchanged and is used in the equality construction to make any prescribed initial backtracking trial length attain the sharp endpoint.

The theorem controls one accepted step. It does not claim that every later step of a particular backtracking sequence attains the bound, nor does it classify nonquadratic objectives, finite precision, non-Euclidean gradient norms, preconditioned directions, or Wolfe-type line searches.

When the maximum displayed in the theorem equals one, that value is a supremum approached by arbitrarily small accepted steps. On the unsafe branch, equality is attained by the two-dimensional construction.

## Proof
For a quadratic,
\[
f(x-\alpha g)-f(x)
=
-\alpha\|g\|_2^2
+
\frac{\alpha^2}{2}g^{\mathsf T}Ag.
\]
Define the Rayleigh quotient
\[
q
=
\frac{g^{\mathsf T}Ag}
{\|g\|_2^2}.
\]
The Armijo condition is therefore equivalent to
\[
\alpha q\le2(1-\sigma).
\]
Put
\[
t=\alpha q.
\]
The new gradient is
\[
g^+=(I-\alpha A)g,
\]
so
\[
\frac{\|g^+\|_2^2}{\|g\|_2^2}
=
1-2t+Kt^2,
\]
where
\[
K
=
\frac{
\|g\|_2^2\,g^{\mathsf T}A^2g
}{
(g^{\mathsf T}Ag)^2
}.
\]

We now maximize \(K\) at fixed condition number. Let
\[
\mu=\lambda_{\min}(A),
\qquad
L=\lambda_{\max}(A).
\]
After normalizing \(\|g\|_2=1\), write
\[
q=g^{\mathsf T}Ag,
\qquad
r=g^{\mathsf T}A^2g.
\]
Every
\[
\lambda\in[\mu,L]
\]
satisfies
\[
(\lambda-\mu)(L-\lambda)\ge0,
\]
hence
\[
\lambda^2
\le
(\mu+L)\lambda-\mu L.
\]
Averaging over the spectral weights of \(g\) gives
\[
r
\le
(\mu+L)q-\mu L.
\]
Therefore
\[
K
=
\frac{r}{q^2}
\le
\frac{(\mu+L)q-\mu L}{q^2}.
\]
The scalar right-hand side is maximized at
\[
q=
\frac{2\mu L}{\mu+L},
\]
and its maximum is
\[
K_{\max}
=
\frac{(\mu+L)^2}{4\mu L}
=
\frac{(\kappa+1)^2}{4\kappa}.
\]
Equality requires only the two endpoint eigenspaces, with spectral weights
\[
\frac{L}{\mu+L}
\quad\text{and}\quad
\frac{\mu}{\mu+L}.
\]

For fixed \(K\), the function
\[
h(t)=1-2t+Kt^2
\]
is convex. Since an Armijo-admissible positive step satisfies
\[
0<t\le2(1-\sigma),
\]
its supremum over this interval is the larger of the limiting value \(1\) as \(t\downarrow0\) and the endpoint value. Maximizing the endpoint over \(K\le K_{\max}\) gives
\[
\sup h
=
\max
\left\{
1,\;
1-4(1-\sigma)
+
4(1-\sigma)^2K_{\max}
\right\},
\]
which simplifies to the claimed formula.

Universal gradient-norm nonexpansion holds exactly when the endpoint value is at most one:
\[
2(1-\sigma)K_{\max}\le2.
\]
Substituting \(K_{\max}\) yields
\[
(1-\sigma)(\kappa+1)^2\le4\kappa,
\]
or equivalently
\[
\sigma
\ge
\left(
\frac{\kappa-1}{\kappa+1}
\right)^2.
\]

For sharpness, fix an initial backtracking trial \(s_0>0\) and let
\[
A=
\gamma\operatorname{diag}(1,\kappa),
\qquad
\gamma=
\frac{(1-\sigma)(\kappa+1)}
{\kappa s_0},
\]
with
\[
g=
\begin{pmatrix}
\sqrt{\kappa}\\
1
\end{pmatrix}.
\]
The spectral weights of \(g\) are precisely the endpoint equality weights. Its Rayleigh quotient is
\[
q=\frac{2(1-\sigma)}{s_0}.
\]
Thus
\[
\alpha=s_0
\]
gives
\[
t=2(1-\sigma),
\]
so the first trial is accepted at Armijo equality and simultaneously attains \(K_{\max}\).

The rational example follows by setting
\[
\sigma=\frac14,
\qquad
\kappa=4,
\qquad
s_0=1.
\]
Direct substitution gives the values stated in the finding.

## Verification
The embedded `verify.py` replays the rational witness exactly. It checks the Armijo equality, the objective decrease, the new gradient, and the squared gradient-norm ratio
\[
\frac{97}{64}.
\]

It also checks the endpoint construction symbolically through exact rational instances and verifies algebraically that the safety condition
\[
\sigma
\ge
\left(
\frac{\kappa-1}{\kappa+1}
\right)^2
\]
is equivalent to endpoint nonexpansion.

The all-dimensional moment bound is proved analytically. Finite replay is corroborative only.

## Relationship to prior work
Classical Armijo backtracking is designed around sufficient decrease of the objective. Ahookhosh and Ghaderi state the standard monotone rule
\[
f(x_k+\alpha_kd_k)
\le
f(x_k)+\sigma\alpha_k g_k^{\mathsf T}d_k,
\qquad
0<\sigma<\frac12,
\]
with a geometrically reduced trial sequence, and emphasize that the accepted function values decrease monotonically. Those facts are prior work.

Nocedal, Sartenaer, and Zhu study the Euclidean gradient norm for exact-line-search steepest descent on SPD quadratics. Their Theorem 4.1 gives the one-step squared gradient bound
\[
\frac{\|g^+\|_2^2}{\|g\|_2^2}
\le
\frac{(\kappa-1)^2}{4\kappa}
\]
for the exact line-search step, and consequently the classical monotonicity frontier
\[
\kappa\le3+2\sqrt2.
\]
That exact-line-search result is prior work.

The present theorem treats the larger family of inexact steps admitted by Armijo sufficient decrease and introduces the Armijo parameter into the sharp gradient-norm safety law. In the formal boundary limit
\[
\sigma\uparrow\frac12,
\]
the longest Armijo-admissible step approaches the exact line-search scale in the sharp two-mode construction, and the formula reduces to the classical exact-line-search bound.

Targeted searches using Armijo, sufficient decrease, gradient-norm monotonicity, conditioning, steepest descent, and quadratic aliases did not locate the \(\sigma\)-dependent safety frontier or the sharp first-trial backtracking construction.

## Limitations
The theorem covers Armijo sufficient decrease alone. A Wolfe curvature condition can exclude long accepted steps and may yield a different sharp gradient-norm frontier.

The result is exact for quadratics and does not assert the same formula for general strongly convex smooth functions.

The global supremum permits arbitrary scaling of \(A\), which is essential when realizing the sharp endpoint at a prescribed backtracking trial length while keeping the condition number fixed.

The line-search literature is extensive, so an older equivalent statement under terminology such as gradient-related descent, sufficient-decrease gradient oscillation, or Kantorovich bounds remains the principal originality risk.

## References
1. M. Ahookhosh and S. Ghaderi, “On efficiency of nonmonotone Armijo-type line searches,” Optimization Online 4488, first public posting 2014-08-10.
2. J. Nocedal, A. Sartenaer, and C. Zhu, “On the Behavior of the Gradient Norm in the Steepest Descent Method,” Computational Optimization and Applications 22 (2002), 5–35. DOI 10.1023/A:1014897230089.
