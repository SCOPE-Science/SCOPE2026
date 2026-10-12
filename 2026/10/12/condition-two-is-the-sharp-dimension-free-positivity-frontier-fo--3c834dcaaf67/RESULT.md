# Condition two is the sharp dimension-free positivity frontier for exact-line-search steepest descent

## Finding
Consider
\[
f(x)=\frac12x^{\mathsf T}Ax-b^{\mathsf T}x,
\qquad
A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
\qquad
0<\mu\le\lambda_i\le L,
\qquad
b\ge0,
\]
and start exact-line-search steepest descent from \(x_0=0\):
\[
r_k=b-Ax_k,\qquad
\alpha_k=\frac{r_k^{\mathsf T}r_k}{r_k^{\mathsf T}Ar_k},
\qquad
x_{k+1}=x_k+\alpha_k r_k.
\]
Let
\[
\kappa=\frac L\mu.
\]

Then:

1. If \(\kappa\le2\), every iterate is componentwise nonnegative in every dimension.
2. In dimension two, every iterate is componentwise nonnegative for every \(\kappa\).
3. For every \(\kappa>2\), there is a three-dimensional positive diagonal quadratic with \(b>0\) whose second iterate has a negative coordinate.

Hence \(2\) is the sharp dimension-free conditioning boundary for positivity, while dimension three and iteration two are jointly minimal for sign loss.

## Assumptions and scope
The Hessian is positive and diagonal in the coordinate system in which nonnegativity is tested. The right-hand side is componentwise nonnegative and the starting point is the origin. The line search is exact and arithmetic is exact.

A coordinate with \(b_i=0\) remains zero, so the proof may restrict to active coordinates with \(b_i>0\). Their exact solution coordinates are
\[
x_i^\star=\frac{b_i}{\lambda_i}>0.
\]

The theorem does not claim the same boundary for nondiagonal symmetric positive-definite matrices, projected gradient methods, inexact line searches, or nonzero starting points.

## Proof
For an active coordinate define
\[
z_{k,i}=\frac{r_{k,i}}{b_i}
=
1-\frac{x_{k,i}}{x_i^\star}.
\]
The update gives
\[
z_{k+1,i}=(1-\alpha_k\lambda_i)z_{k,i},
\qquad
z_{0,i}=1.
\]

Whenever \(r_k\ne0\),
\[
\alpha_k^{-1}
=
\frac{r_k^{\mathsf T}Ar_k}{r_k^{\mathsf T}r_k}
\in[\mu,L].
\]
Thus
\[
0\le\alpha_k\lambda_i\le\frac L\mu=\kappa.
\]
If \(\kappa\le2\), every multiplier satisfies
\[
-1\le1-\alpha_k\lambda_i\le1.
\]
Inductively, \(|z_{k,i}|\le1\), and therefore
\[
x_{k,i}=x_i^\star(1-z_{k,i})\ge0.
\]

Now suppose \(n=2\), with
\[
A=\operatorname{diag}(a,c)
\]
and residual
\[
r=(u,v)^{\mathsf T}.
\]
If \(a=c\), or if one active residual component vanishes, the active problem terminates immediately. Otherwise put
\[
D=au^2+cv^2.
\]
One exact step gives
\[
r^+
=
\frac{(c-a)uv}{D}
\begin{pmatrix}v\\-u\end{pmatrix}.
\]
A second exact step gives
\[
r^{++}=\gamma r,
\]
where
\[
\gamma=
\frac{(c-a)^2u^2v^2}
{(au^2+cv^2)(av^2+cu^2)}.
\]
Moreover,
\[
(au^2+cv^2)(av^2+cu^2)-(c-a)^2u^2v^2
=
ac(u^2+v^2)^2>0,
\]
so \(0\le\gamma<1\).

Starting from \(r_0=b\ge0\), homogeneity gives
\[
r_{2m}=\gamma^m b.
\]
Consequently
\[
x_{2m}=A^{-1}(b-r_{2m})=(1-\gamma^m)x^\star\ge0.
\]
The exact step length at each even residual equals \(\alpha_0\), hence
\[
x_{2m+1}
=
(1-\gamma^m)x^\star+\gamma^m x_1\ge0.
\]
Thus every two-dimensional iterate is nonnegative for every condition number.

For sharpness, fix \(\kappa>2\) and put
\[
t=\frac{\kappa}{2},
\qquad
A_\kappa=\operatorname{diag}(1,t,\kappa),
\qquad
b_\varepsilon=(1,1,\varepsilon)^{\mathsf T}.
\]
Let
\[
m_\varepsilon=\alpha_0^{-1}
=
\frac{1+t+\kappa\varepsilon^2}{2+\varepsilon^2}
\]
and
\[
n_\varepsilon=\alpha_1^{-1}
=
\frac{r_1^{\mathsf T}A_\kappa r_1}{r_1^{\mathsf T}r_1}.
\]
Then
\[
(x_2)_3
=
\varepsilon
\frac{m_\varepsilon+n_\varepsilon-\kappa}
{m_\varepsilon n_\varepsilon}.
\]
As \(\varepsilon\downarrow0\), the first line search is governed by the two equally weighted curvatures \(1\) and \(t\), so
\[
m_\varepsilon\longrightarrow\frac{1+t}{2}.
\]
At that limiting step, the two low-mode residuals have equal magnitude and opposite sign, hence their squared weights are equal and
\[
n_\varepsilon\longrightarrow\frac{1+t}{2}.
\]
Therefore
\[
m_\varepsilon+n_\varepsilon-\kappa
\longrightarrow
1+t-\kappa
=
1-\frac{\kappa}{2}<0.
\]
The denominator remains positive, so continuity gives \((x_2)_3<0\) for all sufficiently small \(\varepsilon>0\).

Because \(x_0=0\) and \(x_1=\alpha_0b_\varepsilon>0\), iteration two is the first possible sign failure. The two-dimensional theorem proves that dimension three is minimal.

## Verification
The embedded `verify.py` uses exact rational arithmetic.

For
\[
A=\operatorname{diag}(1,2,4),
\qquad
b=(1,1,1/10)^{\mathsf T},
\]
it reconstructs
\[
\alpha_0=\frac{201}{304},
\qquad
r_1=
\left(
\frac{103}{304},
-\frac{49}{152},
-\frac{25}{152}
\right)^{\mathsf T},
\qquad
\alpha_1=\frac{22713}{39817},
\]
and
\[
x_2=
\left(
\frac{646416}{756523},
\frac{5777343}{12104368},
-\frac{3353283}{121043680}
\right)^{\mathsf T}.
\]
The third coordinate is strictly negative while the exact solution is strictly positive.

The verifier also checks the two-dimensional two-step residual-scaling identity on an exact rational instance and replays additional exact line-search steps. These computations corroborate the displayed formulas; the universal statements are proved analytically above.

## Relationship to prior work
De Klerk, Glineur, and Taylor give an exact worst-case analysis of gradient descent with exact line search for smooth strongly convex functions. Their method statement is the same exact-line-search gradient iteration used here, and their quadratic discussion records the classical sharp objective contraction factor. Their Section 2.1 records orthogonality of successive gradients, while Example 1.3 gives an explicit two-mode quadratic trajectory.

Those results concern objective accuracy and rate. They do not imply componentwise sign preservation: a norm or objective can contract while an individual coordinate crosses zero. The two-mode trajectory in their Example 1.3 is a special worst-case construction around a zero minimizer, rather than a cone-invariance theorem for all positive diagonal right-hand sides.

The present result classifies a coordinatewise feasibility property. It gives an all-dimensional sufficient condition, proves unconditional two-dimensional safety, and shows that every conditioning level above the sharp boundary already permits a three-dimensional second-iterate sign failure.

Targeted searches for exact-line-search steepest descent together with positive-orthant invariance, nonnegative iterates, componentwise monotonicity, diagonal positive quadratics, and Cauchy-method positivity did not locate an implication-equivalent theorem.

## Limitations
Diagonal structure is essential to the normalized-coordinate proof. A nondiagonal symmetric positive-definite matrix mixes spectral and coordinate directions, so the result does not classify Stieltjes matrices or arbitrary positive-definite systems.

The theorem assumes the zero start and an exact line search. Different starts or line-search errors can alter the sign geometry.

The conditioning bound \(2\) is a dimension-free frontier, not a statement that all problems with \(\kappa>2\) fail. Every two-dimensional problem remains safe for arbitrary conditioning.

Residual originality risk remains that older steepest-descent or stationary-iteration literature may encode the same cone-invariance statement under different terminology. The highly relevant full text inspected here supplies the objective-rate and orthogonality theory but not the positivity classification.

## References
1. E. de Klerk, F. Glineur, and A. B. Taylor, “On the worst-case complexity of the gradient method with exact line search for smooth strongly convex functions,” arXiv:1606.09365, first public version 2016-06-30. The preprint lists AMS classification 90C25 first; later published in Optimization Letters, DOI 10.1007/s11590-016-1087-4.
