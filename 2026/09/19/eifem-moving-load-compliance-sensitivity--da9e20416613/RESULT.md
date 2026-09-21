# Design-independent physical loads need a moving-load term in parameterized EIFEM compliance sensitivities

## Result

Consider a symmetric positive-definite fine-scale stiffness matrix
\(K(\mu)\in\mathbb R^{N\times N}\), a smooth full-column-rank reduced/inter-scale map
\(T(\mu)\in\mathbb R^{N\times r}\), and a **fixed physical load** \(F\in\mathbb R^N\).
Define
\[
K_c=T^TKT,\qquad F_c=T^TF,\qquad q=K_c^{-1}F_c,
\]
and the Galerkin reduced compliance
\[
J(\mu)=F_c(\mu)^Tq(\mu)=F_c^T K_c^{-1}F_c.
\]
For any scalar design parameter, the exact derivative is
\[
\boxed{
J'=2(F_c')^Tq-q^T K_c' q,
\qquad F_c'=T'^T F.
}
\]
Thus a design-independent fine-scale load does **not** in general induce a design-independent reduced load when the inter-scale map depends on the design.

For the parameterized EIFEM formulation of Rubio, Ferrer, Hernández, and Antolin (arXiv:2609.20053v1), Eq. (10) gives the coarse right-hand side as \(T^TF\), Sec. 3 parameterizes \(T(\mu)\), and Sec. 4.2 explicitly writes the general relation \(\widetilde F_c(\mu)=\widetilde T(\mu)^TF\). The subsequent choice to hold \(\widetilde F_c\) fixed because the fine-scale \(F\) is fixed therefore describes a different surrogate load model unless
\[
\boxed{T'^T F=0}
\]
for the design direction in question. Under the physical pullback \(F_c=T^TF\), the stiffness-only formula \(-q^T K_c'q\) omits the first term above.

## Residual form: a Pulay-type moving-space correction

Let
\[
y=Tq,\qquad r=F-Ky.
\]
Galerkin orthogonality gives \(T^Tr=0\). Expanding \(K_c'\) and \(F_c'\) yields
\[
\boxed{
J'=-y^T K' y+2r^T T'q.
}
\]
The second term is a moving-trial-space correction analogous in structure to a Pulay term: the residual is orthogonal to the current reduced space, but need not be orthogonal to the velocity of that space. This representation also gives the useful bound
\[
|J'+y^TK'y|\le 2\|r\|_2\,\|T'\|_2\,\|q\|_2.
\]
Hence a Hellmann--Feynman-like physical-stiffness derivative \(-y^TK'y\) becomes accurate when the Galerkin residual is small, whereas retaining the \(T'\)-contribution inside \(K_c'\) while dropping \(F_c'\) does not enjoy this cancellation.

## Exact-ROM coordinate-gauge obstruction

The omission is not merely a small reduced-order error. Let \(R(\mu)\in GL(r)\) be any smooth change of reduced coordinates and replace
\[
T\mapsto \widehat T=TR.
\]
Then
\[
\widehat K_c=R^TK_cR,\qquad \widehat F_c=R^TF_c,
\qquad \widehat q=R^{-1}q,
\]
so the physical reduced state \(Tq\), compliance \(J\), and the full derivative
\(2F_c'^Tq-q^TK_c'q\) are invariant.

By contrast, the stiffness-only quantity
\[
g_0=-q^TK_c'q
\]
is not invariant. Writing \(S=R'R^{-1}\), one obtains
\[
\boxed{
\widehat g_0=g_0-2q^TK_cSq.
}
\]
In particular, for the scalar gauge \(R(\mu)=e^{c\mu}I\),
\[
\boxed{
\widehat g_0=g_0-2cJ.
}
\]
Since \(c\) is arbitrary, a stiffness-only sensitivity can be changed by an arbitrarily large amount without changing the physical reduced space or reconstructed solution. The missing load term transforms by the opposite amount and restores invariance.

A concrete orthogonal example needs no rescaling. Take
\[
K=\operatorname{diag}(1,4),\qquad F=(1,1)^T,
\]
and let \(T(\mu)\) be the \(2\times2\) rotation matrix. The reduced model spans the full physical space for every \(\mu\), so it is exact and
\[
J=F^TK^{-1}F=\frac54
\]
is constant. At \(\mu=0\),
\[
K_c'=
\begin{pmatrix}0&3\\3&0\end{pmatrix},
\qquad q=(1,1/4)^T,
\]
so
\[
-q^TK_c'q=-\frac32,
\qquad
2(F_c')^Tq=\frac32,
\qquad
J'=0.
\]
Thus the omitted term can generate a nonzero apparent design gradient even with zero model-reduction error.

## A one-dimensional wrong-sign example

Let
\[
K=\operatorname{diag}(1,4),\qquad F=e_2,
\qquad T(\mu)=(\cos\mu,\sin\mu)^T,
\quad 0<\mu<\frac\pi2.
\]
Then
\[
K_c=1+3\sin^2\mu,\qquad F_c=\sin\mu,
\]
and
\[
J(\mu)=\frac{\sin^2\mu}{1+3\sin^2\mu}.
\]
Its exact derivative is
\[
\boxed{
J'=\frac{2\sin\mu\cos\mu}{(1+3\sin^2\mu)^2}>0.
}
\]
The stiffness-only derivative is instead
\[
\boxed{
g_0=-\frac{6\sin^3\mu\cos\mu}{(1+3\sin^2\mu)^2}<0.
}
\]
Hence the omitted reduced-load derivative can reverse the optimization direction. At \(\mu=\pi/4\),
\[
J'=0.16,\qquad g_0=-0.24,
\qquad 2(F_c')^Tq=0.40.
\]
A centered finite difference in the supplied verification artifact reproduces the \(0.16\) derivative.

## Practical correction and interpretation

There are two mathematically distinct models:

1. **Fixed physical load.** Keep \(F\) fixed, recompute \(F_c(\mu)=T(\mu)^TF\), and use
   \[
   J_j=2(T_j^TF)^Tq-q^T(K_c)_j q.
   \]
   In the parameterized EIFEM construction, \(T(\mu)\) is already represented by differentiable DEIM/Lagrange interpolation, so \(T_j^TF\) can be evaluated without an additional state or adjoint solve.

2. **Fixed reduced-coordinate load.** Prescribe a constant coarse vector \(F_c\) independently of \(T(\mu)^TF\). Then the stiffness-only derivative is the correct derivative of that surrogate problem, but it is not generally the pullback of one fixed fine-scale load as \(T\) changes.

The source-specific issue is therefore not that fixed coarse loads are forbidden; it is that fixed physical loading and fixed reduced-coordinate loading are not equivalent when the inter-scale map is design dependent.

## Limitations

This result is a correction/consistency test for the general sensitivity formulation, not a claim that the numerical benchmark designs in arXiv:2609.20053v1 are necessarily wrong. The omission is harmless for any design direction satisfying \(T_j^TF=0\); for example, a particular loading/mapping implementation could enforce this by construction. The paper's benchmark description does not establish that condition, and the present analysis does not inspect its implementation.

The Pulay analogy, parameter-dependent reduced bases, and the chain rule for a parameter-dependent right-hand side are established ideas and are not claimed as new. The contribution claimed here is the source-specific identification of the fixed-fine-load/fixed-coarse-load mismatch, the coordinate-gauge obstruction for the stiffness-only EIFEM sensitivity, and explicit exact-ROM and wrong-sign counterexamples.

## Reproducibility

`artifacts/verify_eifem_moving_load.py` evaluates the wrong-sign example, the exact-ROM orthogonal coordinate example, and the arbitrary scalar gauge shift. `artifacts/verification_output.txt` records the output.

## References

- R. Rubio, A. Ferrer, J. A. Hernández, P. Antolin, *Accelerating structural optimization via EIFEM: a ROM-based preconditioner*, arXiv:2609.20053v1, 2026. https://arxiv.org/abs/2609.20053
- N. J. Nair, M. Balajewicz, *Transported snapshot model order reduction approach for parametric, steady-state fluid flows containing parameter-dependent shocks*, International Journal for Numerical Methods in Engineering 117 (2019), 1234--1262. https://doi.org/10.1002/nme.5998
- A. Ruiz-Serrano, N. D. M. Hine, C.-K. Skylaris, *Pulay forces from localized orbitals optimized in situ using a psinc basis set*, Journal of Chemical Physics 136 (2012), 234101. https://doi.org/10.1063/1.4728026
