# Zero-mode bottlenecks change optimal local Acc-Sinkhorn tuning for rectangular transport

## Finding

The following theorem gives the **unique rate-optimal fixed parameter** for the two-state Acc-Sinkhorn method on positive rectangular entropic transport problems whenever the column dimension exceeds the row dimension by at least two. In contrast to the previously analyzed two-atom, single-nongauge-mode case, the obligatory zero modes change the optimal tuning for weakly coupled plans.

Let \(\Pi\in\mathbb R_{++}^{m\times n}\) be the positive entropy-regularized optimal transport plan with unit-mass marginals \(a\in\mathbb R_{++}^{m}\), \(b\in\mathbb R_{++}^{n}\), where \(m\ge 2\) and \(n\ge m+2\). Put
\[
J=\operatorname{diag}(b)^{-1}\Pi^{\mathsf T}\operatorname{diag}(a)^{-1}\Pi,
\qquad L=\max\bigl(\operatorname{spec}(J)\setminus\{1\}\bigr).
\]
Here eigenvalues are counted on the quotient by the constant-vector direction, and \(0\le L<1\). In particular, zero is a nongauge eigenvalue of \(J\).

For fixed \(0<\mu<1\), write \(\alpha=\sqrt{2\mu}\) and let \(\mathcal A_{\alpha}\) be the two-state fixed-point map in Xu and Chen's Algorithm 1. All these maps have locally exponentially attracting fixed points on the gauge quotient. Their **linearized asymptotic state contraction factor** is \(R(\alpha)=\rho(D\mathcal A_{\alpha})<1\). It has a unique minimizer \(\alpha_*\):
\[
\alpha_*=
\begin{cases}
(\sqrt5-1)/2,&L=0,\\[2pt]
\dfrac{-1+\sqrt L+\sqrt{L+2\sqrt L+5}}2,&0<L<1/4,\\[5pt]
\alpha_C(L),&1/4\le L<1,
\end{cases}
\]
where \(\alpha_C(L)\in(0,1]\) is the unique solution of
\[
(\alpha_C+3)L+\alpha_C^2+\alpha_C-1
=2\sqrt L(1+\alpha_C).
\]
The exact optimum is
\[
\boxed{R(\alpha_*)=\frac{\sqrt L}{1+\alpha_*}},
\]
with value zero at \(L=0\). At \(L=1/4\), the two positive-\(L\) formulas meet at \(\alpha_*=1\) and \(R=1/4\).

**New rectangular effect.** If \(0<L<1/4\), the optimum balances a real zero-mode eigenvalue against a complex-conjugate top-mode pair. It is strictly smaller than the single-mode critical-damping parameter \(\alpha_C(L)\), and using that single-mode parameter gives a strictly larger rectangular-state spectral radius. If \(L\ge1/4\), the upper mode determines the optimum and the parameter equals \(\alpha_C(L)\). The complete endpoint rule is exact for every allowed positive plan, and every \(L\in[0,1)\) is realized by an explicit positive \(2\times4\) plan.

For comparison, ordinary normalized Sinkhorn has linearized factor \(L\). The optimized two-state factor is strictly **worse** for \(0<L<1/4\), equal at \(L=1/4\), and strictly better for \(1/4<L<1\). This threshold is already present in the prior two-atom analysis; the independent new conclusion is the rank-nullity-driven change of optimal parameter below it.

## Assumptions and scope

The plan \(\Pi\) has strictly positive entries and prescribed positive marginals of equal total mass one. The underlying Gibbs kernel is strictly positive, so all log-potential maps are smooth. Dimensions are \(m\ge2\), \(n\ge m+2\). All statements concern the exact normalized column-potential update on \(\mathbb R^n/\operatorname{span}\{\mathbf1\}\), and the fixed-parameter inner iteration, not the homotopy outer loop.

Write \(S\) for the normalized Sinkhorn update. With \(d=1+\alpha\), the source's Algorithm 1 becomes
\[
 x^+=(w+S(x))/d,\qquad
 w^+=(w+(\alpha^2-2)x^++2S(x^+))/d.
\]
At the optimal gauge-fixed log potential \(x_*\), \(S(x_*)=x_*\) and the two-state fixed point is \((x_*,\alpha x_*)\). The linearized spectral factor means the spectral radius of this finite-dimensional derivative; defective roots can produce polynomial transient factors, so it is not generally a prefactor-one norm bound.

## Proof

**1. Derivative, positivity, and forced zero directions.** Differentiating the row-correct-then-column-correct Sinkhorn step at the balanced plan gives, on column-potential equivalence classes,
\[
 DS(x_*)=J=\operatorname{diag}(b)^{-1}\Pi^{\mathsf T}\operatorname{diag}(a)^{-1}\Pi.
\]
Its similarity transform by \(\operatorname{diag}(b)^{1/2}\) is symmetric positive semidefinite. It has eigenvalue one in the constant direction; strict positivity of \(\Pi\) makes all nongauge eigenvalues less than one. Since \(\operatorname{rank}(J)\le m\) and \(n\ge m+2\), at least one zero eigenvalue persists after removing the constant direction. Consequently the quotient eigenvalues lie in \([0,L]\), with both endpoints present.

**2. Exact two-state modal polynomial.** Differentiating both updates and restricting to a nongauge mode of \(J\) with eigenvalue \(\lambda\) gives
\[
 M_{\alpha,\lambda}=
 \begin{pmatrix}
 \lambda/d&1/d\\
 \lambda(\alpha^2-2+2\lambda)/d^2&(\alpha^2+\alpha-1+2\lambda)/d^2
 \end{pmatrix}.
\]
Its characteristic polynomial is
\[
 p_{\alpha,\lambda}(z)=z^2-
 \frac{(\alpha+3)\lambda+\alpha^2+\alpha-1}{d^2}\,z
 +\frac{\lambda}{d^2}.
\]
All nongauge roots lie strictly inside the unit disk for every \(0<\alpha<\sqrt2\) and \(0\le\lambda<1\). Indeed, the three real quadratic Schur conditions follow from \(1-\lambda/d^2>0\) and
\[
 1-\operatorname{tr}M+\det M=
 \frac{(\alpha+2)(1-\lambda)}{d^2}>0,\qquad
 1+\operatorname{tr}M+\det M=
 \frac{2\alpha^2+3\alpha+(\alpha+4)\lambda}{d^2}>0.
\]
Smoothness gives local exponential attraction for each fixed parameter.

**3. Only endpoint modes affect the spectral radius.** For any \(r>0\), both roots of \(p_{\alpha,\lambda}\) have modulus at most \(r\) if and only if
\[
 \frac{\lambda}{d^2}\le r^2,
 \qquad r^2\pm r\operatorname{tr}(M_{\alpha,\lambda})+
 \frac{\lambda}{d^2}\ge0.
\]
For fixed \(\alpha,r\), all three inequalities are affine in \(\lambda\). Thus if they hold at \(0,L\), they hold throughout \([0,L]\). Because both endpoints occur,
\[
 R(\alpha)=\max\{\rho(M_{\alpha,0}),\rho(M_{\alpha,L})\}.
\]
In particular the zero mode has radius
\[
 \rho(M_{\alpha,0})=
 \frac{|\alpha^2+\alpha-1|}{(1+\alpha)^2},
\]
while the product of the two top-mode eigenvalues is \(L/d^2\). Thus \(R(\alpha)\ge\sqrt L/d\).

**4. Zero-mode balancing for \(0<L<1/4\).** Put \(t=\sqrt L\), and define the positive root \(\alpha_B\) of \(\alpha^2+\alpha-1=t(1+\alpha)\), namely the middle formula above. For \(t<1/2\), \(\alpha_B<1\). At \(\alpha_B\), the zero-mode eigenvalue has modulus \(t/d\), while the top-mode discriminant is strictly negative, hence its two eigenvalues have common modulus \(t/d\). The discriminant sign follows by substituting the balance identity: it is equivalent to \((\alpha_B+3)t<(1+\alpha_B)\), which follows from \((1+\alpha_B)^2-(\alpha_B+3)(\alpha_B^2+\alpha_B-1)=(1-\alpha_B)(\alpha_B+2)^2>0\). Every \(\alpha<\alpha_B\) has the strictly larger determinant lower bound \(t/(1+\alpha)\). Every \(\alpha>\alpha_B\) has strictly larger zero-mode radius because \((\alpha^2+\alpha-1)/(1+\alpha)^2\) increases with derivative \((\alpha+3)/(1+\alpha)^3>0\) after the balancing point. Uniqueness follows. At \(L=0\), the only quotient mode is zero; its radius is minimized uniquely at \(\alpha=(\sqrt5-1)/2\), where the derivative is nilpotent.

**5. Top-mode critical damping for \(1/4\le L<1\).** With \(t=\sqrt L\), set
\[
 H(\alpha,t)=(\alpha+3)t^2-2t(1+\alpha)+\alpha^2+\alpha-1.
\]
The function strictly increases in \(\alpha\) because \(\partial_\alpha H=(1-t)^2+2\alpha>0\). For \(t>1/2\), its values at \(\alpha=0\) and \(\alpha=1\) have opposite signs, giving a unique zero \(\alpha_C\in(0,1)\); at \(t=1/2\) it has unique zero \(\alpha_C=1\). There the top-mode polynomial has repeated positive root \(r_C=t/(1+\alpha_C)\). Furthermore its zero-mode radius does not exceed \(r_C\): writing \(g=(\alpha_C+3)t/(1+\alpha_C)\), the positive quadratic branch gives \(1\le g\le3\), and the critical identity yields \((\alpha_C^2+\alpha_C-1)/(t(1+\alpha_C))=2-g\), of modulus at most one. For any \(\alpha<\alpha_C\), the top-mode determinant bound \(t/(1+\alpha)>r_C\) applies. For \(\alpha>\alpha_C\), the scaled polynomial evaluation
\[
 h(\alpha)=(1+\alpha)^2p_{\alpha,L}(r_C)
\]
vanishes at \(\alpha_C\), has negative derivative there because \(h'(\alpha_C)=r_C[2t-(2\alpha_C+1+t^2)]<0\), and has negative second derivative \(h''(\alpha)=2r_C(r_C-1)<0\). Thus \(h(\alpha)<0\) for all \(\alpha>\alpha_C\); a positive real root of the top-mode polynomial exceeds \(r_C\). Hence \(\alpha_C\) uniquely minimizes \(R\).

**6. Comparison and sharp realization.** At \(0<t<1/2\), \(\alpha_B<1\) gives \(R_*=t/(1+\alpha_B)>t^2=L\). At \(t=1/2\), equality holds. At \(t>1/2\), writing \(s=\sqrt{1-\alpha_C}\in(0,1)\), the critical equation yields \(t=(1+s-s^2)/(2-s)\) and
\[
 t(1+\alpha_C)-1=
 \frac{s(1-s)(3-s^2)}{2-s}>0,
\]
so \(R_*<L\). For explicit sharpness take \(m=2,n=4\), \(a=(1/2,1/2)\), \(b=(1/4,1/4,1/4,1/4)\), and for \(t\in[0,1)\) let
\[
 \Pi_t=\frac18
 \begin{pmatrix}
 1+t&1+t&1-t&1-t\\
 1-t&1-t&1+t&1+t
 \end{pmatrix}.
\]
Its quotient Sinkhorn spectrum is exactly \(\{t^2,0,0\}\). Choosing Gibbs kernel \(K=\Pi_t\) makes it the positive balanced entropic plan, realizing every \(L=t^2\in[0,1)\).

## Verification

The included standalone program `verify_acc_sinkhorn.py` (Python with NumPy) tests the source's two-state update, modal trace/determinant in exact rational arithmetic, all Schur identities, endpoint dominance, global parameter minimax on finite grids, forced zero modes, strict baseline comparisons, and finite-difference Jacobians of both the nonlinear Sinkhorn map and the two-state update. It passed **27,178 deterministic checks**. The complete theorem is proved analytically above; finite grids and numerical differentiation are supporting diagnostics only.

## Relationship to prior work

Xu and Chen [1] define the two-state Acc-Sinkhorn map and prove a homotopy objective guarantee under a stability condition. They do not supply the exact rectangular fixed-parameter minimax local spectral formula. A prior two-atom analysis of their fixed-parameter map (identifier `e038ddd6-5b39-4dea-ad43-68455bd41cbc`) derives the single-positive-mode critical-damping optimizer and the already-known quarter-eigenvalue comparison with unaccelerated Sinkhorn; this result does **not** imply the new below-quarter rectangular optimizer because it has no nongauge zero eigenvalue. Gao et al. [2] analyze classical Sinkhorn and different accelerated schemes, including PAGD and OSMS; their paper gives local spectral comparisons but not the present two-state map's forced-zero-mode minimax balance. Lehmann et al. [3] and Thibault et al. [4] analyze overrelaxed row/column rescalings, distinct from Xu and Chen's two-state recurrence. The present contribution is limited to the new rank-nullity-dependent tuning and its exact full-spectrum derivation, not a claim of discovering Sinkhorn linearization or the classical quarter comparison.

## Limitations

All conclusions are local, fixed-parameter, and exact-arithmetic. There is no global-basin estimate, no global convergence claim for the homotopy outer loop, and no general guarantee about finite iteration counts: at a repeated-root optimum a polynomial transient may occur. Strong positivity and the rectangular dimension condition are essential to this formulation. The novelty assessment depends on accessible sources and is not a uniqueness certificate against unindexed literature.

## References

1. Zeyi Xu and Long Chen, *Accelerating Sinkhorn for Entropy-Regularized Optimal Transport*, arXiv:2605.30267v1, May 28, 2026, https://arxiv.org/abs/2605.30267.
2. Wenzhi Gao, Zhaonan Qu, Yinyu Ye, Madeleine Udell, *Tight Nonasymptotic Local Convergence of Sinkhorn-Knopp*, arXiv:2608.11760v1, August 12, 2026, https://arxiv.org/abs/2608.11760.
3. Tobias Lehmann, Max-K. von Renesse, Alexander Sambale, André Uschmajew, *A note on overrelaxation in the Sinkhorn algorithm*, arXiv:2012.12562, December 23, 2020, https://arxiv.org/abs/2012.12562.
4. Alexis Thibault, Lénaïc Chizat, Charles Dossal, Nicolas Papadakis, *Overrelaxed Sinkhorn–Knopp Algorithm for Regularized Optimal Transport*, arXiv:1711.01851, November 6, 2017, https://arxiv.org/abs/1711.01851.
