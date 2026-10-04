# Infinite-mean Adam conditioning under Gaussian initialization, with a sharp two-dimensional floor
## Finding

A dense-block diagnostic in Adam-mini studies Adam as an instantaneous diagonal preconditioner. For a Hessian block \(H\), an initialization \(x\), and
\[
g=Hx,
\]
it sets
\[
D_x
=
\operatorname{diag}
\left(
\frac1{|g_1|},
\ldots,
\frac1{|g_d|}
\right)
\]
because the diagnostic uses
\[
v=g\odot g.
\]
Its effectiveness is measured through the spectral singular-value condition number
\[
K(x)
=
\kappa_2(D_xH)
=
\frac{\sigma_{\max}(D_xH)}
{\sigma_{\min}(D_xH)}.
\]

Two exact facts hold.

First, let
\[
H\in\mathbb R^{d\times d}
\]
be any invertible matrix with
\[
d\ge2,
\]
and let
\[
x\sim N(0,\sigma^2 I_d),
\qquad
\sigma>0.
\]
Then every coordinate of \(g=Hx\) is nonzero almost surely, so \(K(x)\) is finite almost surely, but
\[
\mathbb E[K(x)]
=
\infty.
\]
Thus the unregularized Gaussian-initialization condition-number diagnostic has no finite population mean.

Second, in two dimensions the best condition number attainable by changing the initialization has a closed form. Let
\[
H
=
\begin{bmatrix}
a&c\\
c&b
\end{bmatrix}
\succ0,
\]
and define its row norms
\[
r_1
=
\sqrt{a^2+c^2},
\qquad
r_2
=
\sqrt{b^2+c^2}.
\]
Define the absolute row correlation
\[
\rho
=
\frac{|c|(a+b)}
{r_1r_2}.
\]
Positive definiteness gives
\[
0\le\rho<1.
\]
Then
\[
\inf_{x:\,(Hx)_1(Hx)_2\ne0}
\kappa_2(D_xH)
=
\sqrt{
\frac{1+\rho}{1-\rho}
}.
\]
The infimum is attained exactly when
\[
\frac{|(Hx)_1|}
{|(Hx)_2|}
=
\frac{r_1}{r_2}.
\]

This yields a sharp orientation barrier. For
\[
H_\kappa
=
\frac12
\begin{bmatrix}
\kappa+1&\kappa-1\\
\kappa-1&\kappa+1
\end{bmatrix},
\qquad
\kappa\ge1,
\]
the eigenvalues are \(1\) and \(\kappa\), and
\[
\rho
=
\frac{\kappa^2-1}
{\kappa^2+1}.
\]
Therefore
\[
\inf_x
\kappa_2(D_xH_\kappa)
=
\kappa.
\]
No admissible initialization can make this instantaneous Adam preconditioner improve the original condition number.

By contrast, for the axis-aligned matrix
\[
H
=
\operatorname{diag}(1,\kappa),
\]
one has
\[
\rho=0
\]
and the best attainable condition number is exactly
\[
1.
\]

More generally, rotating a fixed spectrum continuously interpolates between these extremes. If
\[
H_{\kappa,\theta}
=
Q_\theta
\operatorname{diag}(1,\kappa)
Q_\theta^\top,
\]
then
\[
\rho_\theta^2
=
\frac{
(\kappa^2-1)^2\sin^2(2\theta)
}{
4\kappa^2
+
(\kappa^2-1)^2\sin^2(2\theta)
}.
\]
Hence the best attainable instantaneous Adam conditioning increases monotonically with
\[
|\sin(2\theta)|
\]
from \(1\) at an axis-aligned spectrum to \(\kappa\) at a \(45^\circ\) rotation.

## Assumptions and scope

The object analyzed here is exactly the unregularized instantaneous preconditioner used in the Adam-mini random-quadratic diagnostic:
\[
D_{\mathrm{Adam}}
=
\operatorname{Diag}(1/\sqrt v),
\qquad
v=g\odot g,
\qquad
g=Hx.
\]

This is not a theorem about full Adam or Adam-mini training dynamics. It does not include momentum history, exponential averaging of second moments, bias correction, or a positive denominator regularizer.

The Gaussian theorem requires only a nondegenerate isotropic Gaussian initialization. Its scale is irrelevant because multiplying \(x\) by a nonzero scalar multiplies every diagonal entry of \(D_x\) by the same reciprocal scalar, which leaves \(\kappa_2(D_xH)\) unchanged.

The two-dimensional sharp formula assumes \(H\) is symmetric positive definite. The infinite-mean theorem itself only requires \(H\) to be invertible.

A positive denominator regularizer changes the conclusion. Replacing \(1/|g_i|\) by a bounded quantity such as \(1/(|g_i|+\varepsilon)\) removes the singularity at \(g_i=0\), so the literal infinite-mean statement does not apply.

## Proof

We first prove the exact two-dimensional lower envelope.

Write
\[
\Delta
=
ab-c^2
>
0.
\]
Because \(H\) is invertible, the map
\[
x\mapsto g=Hx
\]
is onto. Thus the ratio
\[
t
=
\frac{|g_1|}{|g_2|}
\]
can take any value in
\[
(0,\infty).
\]

Condition number is unchanged by multiplying the whole matrix by a positive scalar. Therefore
\[
\kappa_2(D_xH)
=
\kappa_2
\left(
\begin{bmatrix}
1&0\\
0&t
\end{bmatrix}
H
\right).
\]
Set
\[
A_t
=
\begin{bmatrix}
1&0\\
0&t
\end{bmatrix}
H.
\]
Its squared Frobenius norm and determinant are
\[
\|A_t\|_F^2
=
r_1^2+t^2r_2^2,
\]
and
\[
|\det A_t|
=
t\Delta.
\]

Let
\[
K(t)
=
\kappa_2(A_t).
\]
For a nonsingular \(2\times2\) matrix,
\[
K(t)+\frac1{K(t)}
=
\frac{
\sigma_{\max}(A_t)^2+\sigma_{\min}(A_t)^2
}{
\sigma_{\max}(A_t)\sigma_{\min}(A_t)
}
=
\frac{\|A_t\|_F^2}{|\det A_t|}.
\]
Hence
\[
K(t)+\frac1{K(t)}
=
\frac{r_1^2}{t\Delta}
+
\frac{t r_2^2}{\Delta}.
\]
Since
\[
K\mapsto K+K^{-1}
\]
is strictly increasing for
\[
K\ge1,
\]
minimizing \(K(t)\) is equivalent to minimizing the displayed right-hand side. The arithmetic-geometric mean inequality gives the unique minimizer
\[
t_\star
=
\frac{r_1}{r_2},
\]
with minimum
\[
\frac{2r_1r_2}{\Delta}.
\]

Now
\[
r_1^2r_2^2
-
c^2(a+b)^2
=
(ab-c^2)^2
=
\Delta^2.
\]
Therefore
\[
\frac{\Delta}{r_1r_2}
=
\sqrt{1-\rho^2},
\]
so at the optimum
\[
K_\star+\frac1{K_\star}
=
\frac2{\sqrt{1-\rho^2}}.
\]
The solution with
\[
K_\star\ge1
\]
is
\[
K_\star
=
\sqrt{
\frac{1+\rho}{1-\rho}
}.
\]

For the \(45^\circ\)-rotated family \(H_\kappa\), the two row norms are equal and direct substitution gives
\[
\rho
=
\frac{\kappa^2-1}{\kappa^2+1}.
\]
The formula above then gives
\[
K_\star=\kappa.
\]
For a diagonal \(H\), one has \(c=0\), hence \(\rho=0\) and \(K_\star=1\).

For the general rotated spectrum, direct multiplication of
\[
Q_\theta
\operatorname{diag}(1,\kappa)
Q_\theta^\top
\]
gives
\[
c^2(a+b)^2
=
\frac{
(\kappa^2-1)^2
}{
4
}
\sin^2(2\theta),
\]
and
\[
r_1^2r_2^2
=
\kappa^2
+
\frac{
(\kappa^2-1)^2
}{
4
}
\sin^2(2\theta),
\]
which proves the stated formula for \(\rho_\theta\).

We now prove the infinite-mean statement in every dimension
\[
d\ge2.
\]

Fix the first row \(h_1^\top\) of \(H\). Choose a unit vector \(z\) satisfying
\[
h_1^\top z=0.
\]
Such a vector exists because \(d\ge2\). Since \(H\) is invertible,
\[
C^2
:=
\sum_{j=2}^d
(h_j^\top z)^2
>
0.
\]

Let
\[
A=D_xH.
\]
Its spectral norm is at least the Euclidean norm of its first row:
\[
\|A\|_2
\ge
\frac{\|h_1\|_2}{|g_1|}.
\]
On the event
\[
1\le |g_j|\le2
\qquad
\text{for every }
j=2,\ldots,d,
\]
we also have
\[
\sigma_{\min}(A)
\le
\|Az\|_2
\le
C.
\]
Consequently, on this event,
\[
\kappa_2(A)
\ge
\frac{\|h_1\|_2}{C|g_1|}.
\]

Because
\[
x\sim N(0,\sigma^2I_d)
\]
and \(H\) is invertible,
\[
g=Hx
\]
has a nonsingular Gaussian density that is continuous and strictly positive everywhere. Hence there are constants
\[
\delta>0,
\qquad
m>0
\]
such that the joint density is at least \(m\) on the compact box
\[
|g_1|\le\delta,
\qquad
1\le g_j\le2
\quad
(j=2,\ldots,d).
\]
Integrating the lower bound for the condition number over this box gives a positive constant times
\[
\int_{-\delta}^{\delta}
\frac{du}{|u|},
\]
which diverges. Therefore
\[
\mathbb E[K(x)]
=
\infty.
\]

The same local singularity also explains why
\[
\sup_x K(x)=\infty:
\]
one gradient coordinate can approach zero while the others stay bounded away from zero.

## Verification

The accompanying `verify.py` independently checks the algebraic identities used by the proof.

For randomly generated \(2\times2\) SPD matrices, it compares the closed-form floor
\[
\sqrt{(1+\rho)/(1-\rho)}
\]
with a direct singular-value condition number at the predicted row-equilibrating scaling.

It checks the \(45^\circ\)-rotated family for multiple values of \(\kappa\), verifies that its floor equals the original condition number, checks the diagonal floor \(1\), and verifies the orientation formula.

It also constructs gradient vectors with one coordinate tending to zero and confirms the predicted reciprocal growth of the condition number. This finite calculation is only a transcription guard for the tail mechanism; the divergence of the Gaussian expectation is proved analytically above.

## Relationship to prior work

The Adam-mini paper explicitly studies
\[
D_{\mathrm{Adam}}
=
\operatorname{Diag}(1/\sqrt v)
\]
with
\[
v=g\odot g,
\qquad
g=H_bx,
\]
on random positive-definite Hessian blocks and Gaussian Xavier-style initializations. It measures effectiveness using
\[
\kappa(D_{\mathrm{Adam}}H_b)/\kappa(H_b),
\]
reports poorer behavior as dense blocks are produced by rotating eigenvectors, and identifies a lower bound on
\[
\kappa(D_{\mathrm{Adam}}H_b)
\]
as an open theoretical direction.

Das, Agarwal, Sanghavi, and Dhillon analyze Adam's preconditioning effect on quadratic objectives and show that non-diagonal Hessians can erase or reverse Adam's conditioning advantage. Their theory uses Adam dynamics and Jacobi-type condition quantities rather than the instantaneous random preconditioner above; the inspected paper does not give the Gaussian infinite-mean law or the exact two-dimensional initialization envelope.

Classical diagonal-scaling theory, including Demmel's one-sided scaling results, provides broader context for optimizing
\[
\kappa_2(DH)
\]
over positive diagonal \(D\). The deterministic two-dimensional row-equilibration formula here is consistent with that scaling perspective. The Adam-specific contribution is to identify the exact set of scalings generated by \(D_x\), derive the sharp orientation barrier in the source diagnostic, and show that its prescribed Gaussian initialization induces an infinite first moment for the resulting condition number.

Focused published-record searches for Adam instantaneous preconditioning, Gaussian-initialization condition-number tails, two-dimensional row-scaling envelopes, and equivalent dense-rotation barriers did not identify the combined statement.

## Limitations

The infinite mean is a property of the unregularized diagnostic
\[
D_x=\operatorname{diag}(1/|Hx|).
\]
A positive denominator regularizer truncates the singularity and makes the literal expectation finite.

The exact deterministic lower envelope is proved only in two dimensions. General optimal one-sided diagonal scaling is a broader matrix-scaling problem.

The result concerns conditioning of one instantaneous preconditioned Hessian, not optimization convergence or training loss.

An infinite population mean does not imply that every finite sample is large. It means that mean-based summaries of the unregularized Gaussian diagnostic have a heavy singular tail and lack a finite population target.

## References

1. Yushun Zhang, Congliang Chen, Ziniu Li, Tian Ding, Chenwei Wu, Diederik P. Kingma, Yinyu Ye, Zhi-Quan Luo, and Ruoyu Sun, “Adam-mini: Use Fewer Learning Rates To Gain More,” arXiv:2406.16793v1, 2024.
2. Rudrajit Das, Naman Agarwal, Sujay Sanghavi, and Inderjit S. Dhillon, “Towards Quantifying the Preconditioning Effect of Adam,” arXiv:2402.07114v1, 2024.
3. James Demmel, “Nearly Optimal Block-Jacobi Preconditioning,” SIAM Journal on Matrix Analysis and Applications 44(1), 2023, DOI 10.1137/22M1504901.
