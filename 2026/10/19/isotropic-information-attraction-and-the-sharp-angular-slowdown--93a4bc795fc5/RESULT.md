# Isotropic information attraction and the sharp angular slowdown of equal-strength SIFt-RLS

## Finding

For the subspace-of-information-forgetting recursive least-squares (SIFt-RLS) information update with a common nonzero singular value \(\rho\), every persistently exciting sequence of regressor row *subspaces* drives the information matrix to the **same isotropic limit**, even when subspace dimensions and orientations vary with time. Specifically,
\[
R_k\longrightarrow\frac{\rho^2}{1-\lambda}I_d,
\qquad P_k=R_k^{-1}\longrightarrow\frac{1-\lambda}{\rho^2}I_d.
\]
The result holds for every positive-definite initial information matrix and every fixed \(0<\lambda<1\). It is an information-matrix assertion, not an assertion about measured responses or parameter-estimation convergence.

For two alternating unit row directions in dimension two, making angle \(0<\theta<\pi/2\), the **sharp local linearized convergence factor per two updates** is
\[
r_+(\theta)=\frac{T+\sqrt{T^2-4\lambda^2}}2,
\qquad T=2\lambda+(1-\lambda)^2\cos^4\theta.
\]
This is the actual asymptotic factor for suitably small positive-definite perturbations of the isotropic state, not only an upper bound for a derivative. As the angle closes,
\[
1-r_+(\theta)\sim\frac{2(1-\lambda)}{1+\lambda}\,\theta^2.
\]
By contrast, the stationary information matrix produced by **ordinary exponential forgetting** for the same alternating unit regressors has condition number asymptotic to
\[
\kappa\bigl(R_{\mathrm{EF},\infty}\bigr)
\sim \frac{(1+\lambda)^2}{\lambda\theta^2}.
\]
Thus equal-strength SIFt-RLS asymptotically removes this directional conditioning anisotropy, but near-parallel excitation can make its approach to isotropy arbitrarily slow.

## Assumptions and scope

Fix integers \(d\ge2\) and \(1\le q_k\le d\). For each \(k\ge0\), let \(V_k\in\mathbb R^{d\times q_k}\) have orthonormal columns. The filtered regressor is \(\bar\Phi_k=\rho V_k^{\mathsf T}\), with one constant \(\rho>0\); equivalently all its positive singular values equal \(\rho\). Choose any SIFt filtering threshold retaining these positive singular values, for example \(0<\varepsilon<\rho^2\). Let \(R_0\) be any real symmetric positive-definite \(d\times d\) matrix, and let \(0<\lambda<1\).

The information recursion under examination is exactly
\[
R_{k+1}=R_k-(1-\lambda)R_kV_k(V_k^{\mathsf T}R_kV_k)^{-1}V_k^{\mathsf T}R_k
+\rho^2V_kV_k^{\mathsf T}.
\tag{1}
\]
This is the SIFt-RLS information update of Lai and Bernstein (2024), equations (27) and (29), specialized to equal retained singular values; the scalar-output specialization originates in older work of Cao and Schwartz (1999/2000). The convergence hypothesis is the **uniform subspace frame condition**: there exist an integer \(L\ge1\) and \(\beta>0\) such that, for every integer \(k\ge0\),
\[
\sum_{j=k}^{k+L-1}V_jV_j^{\mathsf T}\succeq\beta I_d.
\tag{2}
\]
A periodic finite family of row subspaces jointly spanning \(\mathbb R^d\) automatically satisfies (2). The local rate statement additionally takes \(d=2\), \(q_k=1\), alternate \(V_{2m}=u\) and \(V_{2m+1}=v\) with \(u,v\) unit and \(|u^{\mathsf T}v|=\cos\theta\in(0,1)\), and observes complete two-update epochs.

## Proof

**1. A globally decreasing information divergence.** Normalize the information matrix by \(M_k=(1-\lambda)R_k/\rho^2\), so the desired fixed point becomes \(I_d\). Write \(t=1-\lambda\), and set
\[
G_V(M)=M-MV(V^{\mathsf T}MV)^{-1}V^{\mathsf T}M+VV^{\mathsf T}.
\]
Then (1) is \(M_{k+1}=\lambda M_k+tG_{V_k}(M_k)\). In an orthogonal basis \([V,W]\) completing any such \(V\), write
\[
M=\begin{pmatrix}A&B\\B^{\mathsf T}&C\end{pmatrix},\quad
A=V^{\mathsf T}MV\succ0.
\]
Direct Schur-complement elimination yields
\[
G_V(M)=\begin{pmatrix}I_q&0\\0&C-B^{\mathsf T}A^{-1}B\end{pmatrix}
\tag{3}
\]
in this basis. Both blocks are positive-definite, so the nonlinear iteration remains in the positive-definite cone for all time.

Define the nonnegative Stein divergence
\[
\mathcal D(M)=\operatorname{tr}M-\log\det M-d.
\]
The determinant factorization in (3) gives the **exact identity**
\[
\mathcal D(M)-\mathcal D(G_V(M))
=\operatorname{tr}A-\log\det A-q
+\operatorname{tr}(B^{\mathsf T}A^{-1}B).
\tag{4}
\]
The two terms on the right are nonnegative. Equality holds exactly when \(A=I_q\) and \(B=0\), equivalently \(MV=V\). Since \(\mathcal D\) is convex on positive-definite matrices, (4) yields
\[
\mathcal D(M_k)-\mathcal D(M_{k+1})
\ge t\bigl(\operatorname{tr}A_k-\log\det A_k-q_k
+\operatorname{tr}(B_k^{\mathsf T}A_k^{-1}B_k)\bigr)\ge0.
\tag{5}
\]
The level sets of \(\mathcal D\) are spectrally compact: each eigenvalue remains bounded above and away from zero because \(z-\log z-1\to\infty\) at both endpoints. The nonnegative decrements in (5) are summable. Therefore their bracket tends to zero. Uniform spectral compactness and \(1\le q_k\le d\) imply \(A_k-I_{q_k}\to0\) and \(B_k\to0\), and consequently
\[
\|(M_k-I_d)V_k\|_F\to0,
\quad\|G_{V_k}(M_k)-M_k\|_F\to0,
\quad\|M_{k+1}-M_k\|_F\to0.
\tag{6}
\]

**2. Joint excitation identifies the unique limit.** For the uniform window length \(L\), (6) also implies
\[
\max_{0\le j<L}\|(M_k-I_d)V_{k+j}\|_F\to0,
\]
because the \(L\) successive matrices differ from \(M_k\) by a vanishing amount. With \(E_k=M_k-I_d\) symmetric, condition (2) gives
\[
\beta\|E_k\|_F^2
\le\operatorname{tr}\left(E_k^2\sum_{j=k}^{k+L-1}V_jV_j^{\mathsf T}\right)
=\sum_{j=k}^{k+L-1}\|E_kV_j\|_F^2\to0.
\]
Hence \(M_k\to I_d\). Undo normalization and invert the limiting positive-definite matrices to obtain both limits in the Finding. This argument does not assume that the subspaces repeat periodically or that a fixed subspace dimension is maintained.

**3. Exact two-direction local spectrum.** In dimension two, the derivative of one normalized step at \(I_2\) in symmetric direction \(E\) is
\[
L_u(E)=\lambda E+(1-\lambda)\langle E,W_u\rangle_F W_u,
\qquad W_u=I_2-uu^{\mathsf T}.
\tag{7}
\]
Here \(W_u\) is a rank-one orthogonal projector and \(\|W_u\|_F=1\). The two-step derivative is \(L_vL_u\) on the three-dimensional space of symmetric \(2\times2\) matrices. Its eigenvalues are \(\lambda^2\) and the roots of
\[
z^2-\bigl(2\lambda+(1-\lambda)^2\cos^4\theta\bigr)z+\lambda^2=0.
\tag{8}
\]
Indeed, \(\langle W_u,W_v\rangle_F=(u^{\mathsf T}v)^2=\cos^2\theta\). The product of the two nontrivial eigenvalues equals \(\lambda^2\), and their sum equals the coefficient in (8). When \(0<\theta<\pi/2\), they are distinct and satisfy \(0<\lambda^2<r_-<r_+<1\). The analytic two-step map is a strict local contraction in a suitable equivalent norm. Starting along its dominant eigendirection with small nonzero amplitude, the quadratic nonlinear remainder is summable after division by \(r_+^m\), because a contraction bound \(q\in(r_+,\sqrt{r_+})\) can be selected. Dominant-eigenvector projection then approaches a nonzero coefficient after this division; the other eigencomponents are smaller. Hence an actual nearby positive-definite trajectory satisfies
\[
\lim_{m\to\infty}\|M_{2m}-I_2\|_F^{1/m}=r_+(\theta).
\]
Expanding \(\cos^4\theta=1-2\theta^2+O(\theta^4)\) in (8) gives the stated coefficient of the angular slowdown.

**4. Ordinary forgetting comparison.** For the conventional information update \(R_{k+1}^{\mathrm{EF}}=\lambda R_k^{\mathrm{EF}}+\rho^2V_kV_k^{\mathsf T}\), the stationary even state for alternating \(u,v\) equals
\[
R_{\mathrm{EF},\infty}^{\mathrm{even}}=
\frac{\rho^2}{1-\lambda^2}(\lambda uu^{\mathsf T}+vv^{\mathsf T}),
\]
when each even index precedes the update with \(u\). The odd-state matrix swaps the weights \(\lambda\) and \(1\). The two eigenvalues have sum proportional to \(1+\lambda\) and product proportional to \(\lambda\sin^2\theta\). Thus their ratio is asymptotic to \((1+\lambda)^2/(\lambda\theta^2)\). The same condition number arises at the opposite parity.

## Verification

A standalone Python/NumPy checker in `verify.py` confirms the block Schur identity, the exact divergence drop and positive definiteness for hundreds of randomly generated SPD matrices and varying subspace ranks. It also tests convergence for several persistently exciting cyclic schedules; reconstructs the full three-dimensional derivative in a Frobenius-orthonormal symmetric basis; compares its spectrum with (8); compares its Jacobian against finite differences; and checks both small-angle asymptotic constants. Running `python verify.py` with NumPy prints the recorded assertion count. These finite tests corroborate the calculations; the infinite-time conclusions follow from the proof above, not from numerical iteration.

## Relationship to prior work

Lai and Bernstein (2024), arXiv:2404.10844v1, introduce vector-measurement SIFt-RLS, derive the information update used in (1), and establish covariance bounds and parameter-estimation stability results; those established results are not claimed as new. Cao and Schwartz (1999/2000) established the scalar-regressor directional decomposition underlying the rank-one specialization. Their published work and the inspected 2024 source do not state the equal-strength **global isotropic information limit under a uniform subspace frame condition**, an exact Stein-divergence certificate for that limit, or the two-direction **sharp local information-state contraction** and anisotropy comparison as a combined statement. Older identification stability and logarithmic-determinant/projection arguments may contain equivalent formulations; this remains a genuine priority uncertainty.

## Limitations

The equal-strength assumption is essential to the displayed universal isotropic fixed point: unequal retained singular values generally do not share the same fixed point. Global convergence requires the windowed spanning condition (2); without it, unexcited components need not approach the claimed limit. The exact spectral rate describes the local information recursion only and does not directly bound tracking error, measurement noise, finite precision, or the parameter estimate. Numerical checks are finite and are not substitutes for the global and asymptotic proofs. Independent validation has not been performed.

## References

1. B. Lai and D. S. Bernstein, *SIFt-RLS: Subspace of Information Forgetting Recursive Least Squares*, arXiv:2404.10844v1, first posted April 16, 2024; especially Sections 3–5 and equations (27), (29). https://arxiv.org/html/2404.10844v1
2. L. Cao and H. M. Schwartz, *A Directional Forgetting Algorithm Based on the Decomposition of the Information Matrix*, Proceedings of the 7th Mediterranean Conference on Control and Automation (1999); *Automatica* 36 (2000), 1725–1731, DOI:10.1016/S0005-1098(00)00093-5.
3. S. Bittanti, P. Bolzern, and M. C. Campi, *Convergence and exponential convergence of identification algorithms with directional forgetting factor*, *Automatica* 26 (1990), 929–932, DOI:10.1016/0005-1098(90)90012-7; related directional-forgetting convergence literature rather than an assertion of coverage of the present information-matrix result.
