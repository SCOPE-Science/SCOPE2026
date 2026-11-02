# Exact Frobenius projection onto prescribed circular numerical ranges of \(2\times2\) matrices

## Finding

For every \(A\in\mathbb C^{2\times2}\), prescribed center \(c\in\mathbb C\), and radius \(r>0\), define the numerical range
\[
W(X)=\{z^*Xz:z\in\mathbb C^2,\ z^*z=1\}
\]
and the closed, nonconvex target family \(\mathcal D(c,r)=\{X:W(X)=\{z\in\mathbb C:|z-c|\le r\}\}\). Put
\[
a=\frac{\operatorname{tr}A}{2},\qquad T=A-aI_2,\qquad s=\sigma_{\max}(T),\qquad t=\sigma_{\min}(T).
\]
Then the exact squared Frobenius distance is
\[
\boxed{\min_{X\in\mathcal D(c,r)}\|A-X\|_F^2
=2|a-c|^2+\|T\|_F^2+4r^2-4rs
=2|a-c|^2+t^2+(s-2r)^2.}
\]
If \(s>0\), choose a unit top right singular vector \(v\) of \(T\) for which \(v^*Tv=0\), and put \(u=Tv/s\). Such a choice always exists, and \(u\perp v\). A nearest matrix is explicitly
\[
\boxed{X_*=cI_2+2r\,uv^*.}
\]
If \(s=0\), choose any orthonormal pair \(u,v\) instead. For \(r>0\), the minimizing matrix is unique **if and only if** \(T\) is nonnormal (equivalently \(s>t\)). If \(T\) is normal, there is a continuum of distinct minimizers. If \(A\) and \(c\) are real, at least one minimizer is real even though complex competitors are permitted.

Allowing the disk radius to vary over \(r\ge0\) gives the unique optimal radius \(r=s/2\) and squared distance \(2|a-c|^2+t^2\) to the family of all circular numerical ranges centered at \(c\), including the degenerate radius-zero disk. Allowing the center to vary additionally gives squared distance \(t^2\); its optimal center is \(a\).

## Assumptions and scope

All matrices are exactly \(2\times2\), the norm is the complex Frobenius norm, and \(\sigma_{\max}\), \(\sigma_{\min}\) are the two ordinary singular values. The numerical range includes its boundary. The main fixed-disk theorem assumes strictly positive radius \(r\); radius zero is considered only in the free-radius corollary. The real-minimizer statement requires both \(A\in\mathbb R^{2\times2}\) and \(c\in\mathbb R\).

## Proof

**1. Exactly which matrices have the requested disk.** Write any \(X\) as \(bI_2+N\) with \(\operatorname{tr}N=0\). For every angle \(\theta\), its numerical-range support function is
\[
h_X(\theta)=\operatorname{Re}(e^{-i\theta}b)+\frac12\sqrt{\|N\|_F^2+\operatorname{Re}(e^{-2i\theta}\operatorname{tr}N^2)}.
\]
Indeed, the last term is the largest eigenvalue of the traceless Hermitian matrix \((e^{-i\theta}N+e^{i\theta}N^*)/2\). If the support function equals \(\operatorname{Re}(e^{-i\theta}c)+r\) for all \(\theta\), subtracting the supports at \(\theta\) and \(\theta+\pi\) first forces \(b=c\). Constancy of the even term then forces \(\operatorname{tr}N^2=0\) and \(\|N\|_F=2r\). For a traceless \(2\times2\) matrix, Cayley--Hamilton says \(N^2=\tfrac12\operatorname{tr}(N^2)I_2\); hence \(N^2=0\). Conversely, these two conditions make the support function exactly that of the prescribed disk, so they are also sufficient. Every nonzero such square-zero matrix has the form \(N=2r\,uv^*\) with \(\|u\|=\|v\|=1\) and \(v^*u=0\): this is its rank-one singular-value decomposition, and the orthogonality is equivalent to \(N^2=0\).

**2. The singular-pair orthogonality identity.** For every traceless complex \(2\times2\) matrix \(T\), direct multiplication (or Cayley--Hamilton) gives
\[
T^*T+TT^*=\|T\|_F^2I_2=(s^2+t^2)I_2.
\]
If \(s>t\), take any top right singular vector \(v\) with \(T^*Tv=s^2v\). The identity gives \(TT^*v=t^2v\), whereas \(u=Tv/s\) is a left singular vector for \(s\). Distinct eigenspaces of the Hermitian matrix \(TT^*\) are perpendicular, so \(u\perp v\). This top singular ray is unique.

If \(s=t>0\), then \(T^*T=s^2I_2\), so \(T\) is normal, and \(T\) has a unitary eigenbasis with eigenvalues \(\lambda,-\lambda\) of modulus \(s\). A unit vector \(v\) having equal-modulus components in that eigenbasis satisfies \(v^*Tv=0\), while \(\|Tv\|=s\). Hence \(u=Tv/s\) is again a unit vector perpendicular to \(v\). If \(s=0\), \(T=0\) and any orthonormal pair suffices. In particular, for traceless matrices, \(s=t\) is equivalent to normality.

**3. Attainment and the global lower bound.** The scalar and trace-free matrix subspaces are Frobenius-orthogonal, so, for every candidate \(cI_2+2r\,uv^*\) with \(u\perp v\),
\[
\begin{aligned}
\|A-cI_2-2r\,uv^*\|_F^2
&=2|a-c|^2+\|T\|_F^2+4r^2
 -4r\operatorname{Re}(u^*Tv)\\
&\ge 2|a-c|^2+\|T\|_F^2+4r^2-4rs.
\end{aligned}
\]
The last step uses \(|u^*Tv|\le\|Tv\|\le s\). The singular-pair construction of step 2 satisfies \(u^*Tv=s\), so equality is attained and the displayed distance is exact. Since \(\|T\|_F^2=s^2+t^2\), completing the square gives the alternative \(t^2+(s-2r)^2\) expression.

**4. All minimizers, uniqueness and reality.** For \(r>0\) and \(s>0\), equality in the bound forces \(\|Tv\|=s\) and \(u=Tv/s\), with \(v^*Tv=0\). When \(s>t\), the top singular ray is unique, and a common phase change in \(u,v\) does not change \(uv^*\); consequently \(X_*\) is unique. When \(s=t>0\), the equal-modulus superpositions of the two opposite eigenspaces vary in relative phase, producing infinitely many distinct \(uv^*\). When \(s=0\), all orthogonal pairs give the same minimal cost and distinct matrices. For real \(T\) with \(s>t\), a real top singular vector supplies real \(u,v\). For real \(T\) with \(s=t>0\), choose a real unit vector \(v\) satisfying \(v^T(T+T^T)v=0\), which exists because the real symmetric part has zero trace and therefore has either eigenvalues of opposite signs or is zero; then \(u=Tv/s\) is real and perpendicular to \(v\). This proves the real-minimizer claim.

**5. Free-radius and free-center assertions.** The exact squared distance is \(2|a-c|^2+t^2+(s-2r)^2\). Minimizing over nonnegative radii gives \(r=s/2\), including \(r=0\) for a scalar input; then minimizing over centers gives \(c=a\). These statements include all degenerate cases.

## Verification

The included standard-library Python program `verify.py` recomputes the trace-free identity with exact rational arithmetic on \(693\) small integer matrices (two exact identities per instance), and independently samples complex matrices, computes the proposed minimizer, checks nilpotency, norm, singular-vector orthogonality and the distance formula, and compares with \(75\) competing disk matrices in each of \(400\) trials. It also checks the normal-input continuum and scalar-input cases. Observed run result: **1,386 exact-rational checks and 32,810 deterministic numerical/competing-orbit checks passed**. These checks are only finite supplementary evidence; the preceding proof establishes all universal assertions.

Reproduce with Python 3.9 or later: `python3 verify.py`. No third-party modules or external files are required.

## Relationship to prior work

The new primary motivating literature is Wang--Li--Lim, *Generalized matrix nearness problems II* (arXiv:2605.30181, first public May 28, 2026), which studies exact and iterative solutions of constrained matrix-nearness problems but not this exact circular-numerical-range target. The earlier Li--Lim 2023 paper treats constraints involving low rank, norm, symmetry and prescribed eigenvalues separately. Gnazzo--Guglielmi--Poloni--Sicilia (arXiv:2603.05419, first public March 5, 2026) addresses structured distance to singularity with a general linear perturbation space, but not a prescribed nonzero circular numerical-range radius; the free-radius singularity consequence is not presented as independently new. The classical elliptical range theorem and O'Loughlin's 2025 unitary-orbit description supply the two-dimensional numerical-range characterization, while the Eckart--Young--Mirsky principle supplies rank-one approximation; these facts are acknowledged, not claimed as new. The added statement is the exact prescribed-*disk* nearness formula, its complete minimizer uniqueness classification, and the reality guarantee under complex competitors. No checked source furnished that combined optimization statement. Noferini--Zhukov (arXiv:2609.14828, first public September 13, 2026) addresses real-versus-complex minimizers for different target sets, supplying another relevant contrast.

## Limitations

The theorem does not extend as stated to larger matrices: their circular numerical ranges need not be rank-one square-zero perturbations of scalars. The formula is for exact Frobenius distance, not spectral-norm distance, numerical condition estimates, or backward error of finite-precision SVD. The classification does not claim that the same real-nearest property holds for arbitrary nonconvex matrix target sets. Scholarly priority for this special fixed-disk problem has not been independently established; any earlier explicitly equivalent constrained-approximation theorem would supersede a novelty claim.

## References

1. R. T. Wang, C.-K. Li and L.-H. Lim, *Generalized matrix nearness problems II*, arXiv:2605.30181, v1, May 28, 2026, https://arxiv.org/abs/2605.30181.
2. Z. Li and L.-H. Lim, *Generalized Matrix Nearness Problems*, SIAM Journal on Matrix Analysis and Applications 44 (2023), 1709–1730, DOI:10.1137/22M1526034, https://doi.org/10.1137/22M1526034.
3. V. Noferini and M. Zhukov, *Matrix nearness problems: Do real inputs admit real solutions?*, arXiv:2609.14828, v1 submitted September 13, 2026, https://arxiv.org/abs/2609.14828.
4. G. Lakos, *A short proof of the elliptical range theorem*, Archiv der Mathematik (2024), DOI:10.1007/s00013-023-01957-9, https://doi.org/10.1007/s00013-023-01957-9.
5. M. Gnazzo, N. Guglielmi, F. Poloni and S. Sicilia, *Structured distance to singularity as a nonlinear system of equations*, arXiv:2603.05419, March 5, 2026, https://arxiv.org/abs/2603.05419.
6. M. Gnazzo, V. Noferini, L. Nyman and F. Poloni, *Riemann-Oracle: A general-purpose Riemannian optimizer to solve nearness problems in matrix theory*, Foundations of Computational Mathematics, first online October 16, 2025, https://doi.org/10.1007/s10208-025-09731-9.
7. R. O'Loughlin, *Describing the Numerical Range and C-Numerical Range of Matrices via Their Unitary Orbits and the Joukowsky Transform*, arXiv:2504.05481, first public April 7, 2025, https://arxiv.org/abs/2504.05481.
