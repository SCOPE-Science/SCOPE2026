# Sharp mean-square stability frontier for two-client Loopless SVRG
## Finding

Consider the two-component scalar finite sum
\[
f_\sigma(x)=\frac{\mu(1+\sigma h)}{2}x^2-\sigma c x,
\qquad
\sigma\in\{-1,+1\},
\]
where
\[
\mu>0,\qquad 0\le h<1,
\]
and \(c\) is arbitrary. Uniform averaging gives
\[
f(x)=\frac{\mu}{2}x^2,
\]
so the unique minimizer is \(x^\star=0\). When \(c\ne0\), the individual component gradients do not vanish at \(x^\star\).

Run the original Loopless SVRG update with uniform component sampling and the standard two-sample refresh probability
\[
p=\frac12.
\]
Thus, at step \(k\),
\[
g_k=\nabla f_{\sigma_k}(x_k)-\nabla f_{\sigma_k}(w_k)+\nabla f(w_k),
\]
\[
x_{k+1}=x_k-\eta g_k,
\]
and independently
\[
w_{k+1}=
\begin{cases}
x_k,&\text{with probability }1/2,\\
w_k,&\text{with probability }1/2.
\end{cases}
\]
Put
\[
\alpha=\eta\mu.
\]

The exact mean-square stability frontier is
\[
0<\alpha<\alpha_\star(h),
\]
where
\[
\alpha_\star(h)
=
\frac{1+\sqrt{9+32h^2}}{2(1+4h^2)}.
\]
More precisely, the homogeneous state recursion for \((x_k,w_k)\) is exponentially stable in mean square if and only if this inequality holds. At
\[
\alpha=\alpha_\star(h)
\]
the second-moment operator has eigenvalue \(1\), while for larger positive \(\alpha\) it is not Schur stable.

The frontier is independent of \(c\). It satisfies
\[
\alpha_\star(0)=2
\]
and
\[
\lim_{h\uparrow1}\alpha_\star(h)=\frac{1+\sqrt{41}}{10}.
\]

For this family the component smoothness constant is
\[
L=\mu(1+h).
\]
The source theorem's sufficient rule
\[
\eta\le\frac{1}{6L}
\]
therefore becomes
\[
\alpha\le\frac{1}{6(1+h)},
\]
which is strictly inside the exact scalar mean-square stability region.

## Assumptions and scope

The result uses exactly two scalar components, uniform component sampling, constant stepsize, no regularizer, and refresh probability \(p=1/2\), which is the source paper's standard choice \(p=1/n\) when \(n=2\). The reference point is updated to the current pre-step iterate \(x_k\), as in the original Loopless SVRG algorithm.

The two component curvatures are \(\mu(1-h)\) and \(\mu(1+h)\), both positive because \(h<1\). The offset \(c\) may be nonzero, so the example need not satisfy interpolation.

Mean-square stability here means Schur stability of the exact linear recursion for second moments of the two-state random system. Equivalently, every square-integrable initial state has second moments decaying geometrically. The standard initialization \(x_0=w_0\) is included.

No statement is made about higher-dimensional noncommuting Hessians, nonquadratic objectives, minibatching, nonuniform sampling, other refresh probabilities, or proximal variants.

## Proof

The component gradients are
\[
\nabla f_\sigma(x)=\mu(1+\sigma h)x-\sigma c.
\]
The offset cancels from the variance-reduced estimator:
\[
g_k
=
\mu x_k+\sigma_k\mu h(x_k-w_k).
\]
Hence the dynamics do not depend on \(c\).

Define
\[
e_k=x_k-w_k,
\qquad
A=1-\alpha,
\qquad
d=\alpha h.
\]
For a sampled sign \(\sigma_k\),
\[
x_{k+1}=A x_k-\sigma_k d e_k.
\]
If the snapshot is refreshed, then \(w_{k+1}=x_k\), so
\[
e_{k+1}=-\alpha x_k-\sigma_k d e_k.
\]
If it is not refreshed, then \(w_{k+1}=w_k\), so
\[
e_{k+1}=-\alpha x_k+(1-\sigma_k d)e_k.
\]

Let
\[
X_k=\mathbb E[x_k^2],
\qquad
Y_k=\mathbb E[x_ke_k],
\qquad
Z_k=\mathbb E[e_k^2].
\]
Averaging over the independent sampled sign and refresh coin gives the exact deterministic recursion
\[
\begin{bmatrix}
X_{k+1}\\
Y_{k+1}\\
Z_{k+1}
\end{bmatrix}
=
N
\begin{bmatrix}
X_k\\
Y_k\\
Z_k
\end{bmatrix},
\]
with
\[
N=
\begin{bmatrix}
A^2&0&d^2\\
-A\alpha&A/2&d^2\\
\alpha^2&-\alpha&1/2+d^2
\end{bmatrix}.
\]

Write \(H=h^2\). The characteristic polynomial is
\[
P(\lambda)=\lambda^3+c_1\lambda^2+c_2\lambda+c_3,
\]
where
\[
c_1=-(1+H)\alpha^2+\frac52\alpha-2,
\]
\[
c_2=
-\frac32H\alpha^3+\frac32H\alpha^2
-\frac12\alpha^3+2\alpha^2-\frac{11}{4}\alpha+\frac54,
\]
and
\[
c_3=
\frac{\alpha-1}{4}
\left[(\alpha-1)^2+2H\alpha^2\right].
\]
Direct substitution gives the decisive Jury quantity
\[
P(1)
=
\frac{\alpha}{4}
\left[
2+\alpha-(1+4H)\alpha^2
\right].
\]
The positive root of the bracket is exactly
\[
\alpha_\star(h)
=
\frac{1+\sqrt{9+32H}}{2(1+4H)}.
\]

It remains to verify that no other unit-circle crossing occurs first. For a monic real cubic, the Jury conditions can be written as
\[
|c_3|<1,
\]
\[
P(1)>0,
\]
\[
1-c_1+c_2-c_3>0,
\]
and
\[
J:=1-c_2+c_1c_3-c_3^2>0.
\]

Assume
\[
0<\alpha<\alpha_\star(h).
\]
Then
\[
F:=2+\alpha-(1+4H)\alpha^2>0.
\]
In particular,
\[
0<\alpha<2
\]
and
\[
H<
H_{\max}(\alpha)
:=
\frac{2+\alpha-\alpha^2}{4\alpha^2}.
\]

First,
\[
c_3=
\frac{\alpha-1}{4}
\left[(\alpha-1)^2+2H\alpha^2\right].
\]
For \(0<\alpha\le1\), using \(H<1\) makes its modulus strictly below one. For \(1<\alpha<2\), the bound \(H<H_{\max}\) gives
\[
(\alpha-1)^2+2H\alpha^2
<
\frac{\alpha^2-3\alpha+4}{2},
\]
and therefore again \(|c_3|<1\).

Next,
\[
1-c_1+c_2-c_3
=
\frac{
18-24\alpha+15\alpha^2-3\alpha^3
+12H\alpha^2-8H\alpha^3
}{4}.
\]
For \(0<\alpha\le3/2\), the coefficient of \(H\) is nonnegative, so the expression is bounded below by its value at \(H=0\):
\[
\frac{3(3-\alpha)\bigl[(\alpha-1)^2+1\bigr]}{4}>0.
\]
For \(3/2<\alpha<2\), the expression decreases with \(H\), so using \(H<H_{\max}\) reduces the check to
\[
-\frac{\alpha^3-10\alpha^2+25\alpha-24}{4}>0.
\]
The cubic in the numerator has its only critical point in this interval at \(\alpha=5/3\), where it equals \(-148/27\), and it is negative at both endpoints; hence the displayed Jury quantity is positive.

For the final Jury quantity, direct algebra gives
\[
J(\alpha,0)
=
\frac{
(\alpha+3)(1+2\alpha-\alpha^2)\bigl[(\alpha-1)^3+2\bigr]
}{16}>0
\]
for \(0<\alpha<2\), and
\[
J\bigl(\alpha,H_{\max}(\alpha)\bigr)
=
\frac{
\alpha(11-2\alpha-\alpha^2)
(\alpha^3-4\alpha^2+7\alpha+4)
}{64}>0.
\]
Moreover,
\[
\frac{\partial^2 J}{\partial H^2}
=
-\frac{\alpha^4(\alpha-1)(\alpha+1)}{2}.
\]
Thus for \(1\le\alpha<2\), \(J\) is concave in \(H\), so positivity at the two endpoints implies positivity throughout the allowed interval. For \(0<\alpha<1\),
\[
\frac{\partial J}{\partial H}
=
-\frac{\alpha^2(\alpha-1)}{4}
\left[
2H\alpha^3+2H\alpha^2+\alpha^3-4\alpha-2
\right].
\]
The bracket is at most its value at \(H_{\max}\),
\[
\frac{(\alpha+2)(\alpha^2-2\alpha-1)}{2}<0,
\]
so \(J\) decreases with \(H\); its minimum is again the positive endpoint value at \(H_{\max}\).

All Jury conditions therefore hold exactly when \(P(1)>0\), which for positive \(\alpha\) is
\[
0<\alpha<\alpha_\star(h).
\]
At equality, \(P(1)=0\), so \(1\) is an eigenvalue of the second-moment operator. Above the positive root, \(P(1)<0\), which is incompatible with Schur stability. This proves the exact frontier.

## Verification

The accompanying `verify.py` reconstructs the random scalar update and the exact second-moment matrix. It checks, using rational arithmetic, that one step of explicit branch enumeration agrees with the matrix recursion and that
\[
\det(I-N)
=
\frac{\alpha}{4}
\left[
2+\alpha-(1+4h^2)\alpha^2
\right].
\]
It also evaluates all four cubic Jury conditions over a dense deterministic grid on both sides of the analytic threshold.

These computations are algebra and transcription guards. The exact stability claim follows from the moment recursion and the analytic Jury argument above.

## Relationship to prior work

Kovalev, Horváth, and Richtárik introduced the loopless form of SVRG in which a coin flip replaces the deterministic outer loop. Their algorithm uses the same estimator as above, updates \(x_{k+1}\) first, and refreshes the reference to the pre-step iterate \(x_k\). They recommend \(p=1/n\) as a simple choice and prove linear convergence under a sufficient stepsize condition \(\eta\le1/(6L)\).

Qian, Qu, and Richtárik later generalized Loopless SVRG to arbitrary sampling and composite problems. Their Algorithm 1 preserves the same pre-step snapshot refresh and their strongly convex theorem again uses a sufficient stepsize bounded by an expected-smoothness constant.

The present result asks a different, exact question on the smallest heterogeneous finite sum that retains snapshot staleness and variance reduction: what is the complete mean-square stability region? The answer is the closed-form frontier above. Targeted searches for Loopless SVRG quadratic stability, second-moment spectral radii, exact stepsize ceilings, and two-component models did not identify this formula or an implication covering it.

## Limitations

The theorem fixes \(n=2\), uniform component sampling, and the standard \(p=1/2\) refresh rule. It does not classify arbitrary \(p\), minibatches, nonuniform sampling, or proximal terms.

The Hessians commute because the problem is scalar. Higher-dimensional quadratics with noncommuting component Hessians can have different second-moment behavior.

The result concerns mean-square stability, not transient monotonicity of every sample path.

The exact frontier is derived for the original pre-step snapshot refresh \(w_{k+1}=x_k\). Variants that refresh to \(x_{k+1}\) have a different moment operator and are not covered.

Targeted literature and database searches cannot exclude an equivalent calculation under older stochastic-approximation or switched-system terminology; that remains the principal originality risk.

## References

1. Dmitry Kovalev, Samuel Horváth, and Peter Richtárik, “Don’t Jump Through Hoops and Remove Those Loops: SVRG and Katyusha are Better Without the Outer Loop,” arXiv:1901.08689v1, 2019.
2. Xun Qian, Zheng Qu, and Peter Richtárik, “L-SVRG and L-Katyusha with Arbitrary Sampling,” Journal of Machine Learning Research 22(112), 2021.
