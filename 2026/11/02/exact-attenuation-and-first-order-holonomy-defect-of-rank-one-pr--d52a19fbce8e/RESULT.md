# Exact attenuation and first-order holonomy defect of rank-one projected transport

## Finding

Consider the Frobenius-metric manifold of rank-one real \(2\times2\) matrices, the closed curve \(Y(t)=u(t)u(t)^\top\) with \(u(t)=(\cos t,\sin t)^\top\), and \(0\le t\le\pi\). Parallel transport of a tangent matrix \(Q\) means \(P_t\dot Q=0\), where \(P_t\) is the orthogonal tangent projector. Approximate it at the \(N+1\) equally spaced points \(t_j=j\pi/N\) by consecutive tangent projection \(Q_{j+1}=P_{t_{j+1}}Q_j\), with integer \(N\ge3\).

The loop map fixes the unit skew-symmetric matrix \(A=(E_{12}-E_{21})/\sqrt2\). On the symmetric two-dimensional tangent subspace, in the orthonormal frame specified below, the **exact finite-grid monodromy** is \(B_N^N\), where
\[
B_N=\begin{pmatrix}(1+\cos\delta)/2&\sin\delta/\sqrt2\\-\sin\delta/\sqrt2&\cos\delta\end{pmatrix},\qquad \delta=2\pi/N.
\]
Its eigenvalues are \(\rho_N^N e^{\pm iN\theta_N}\), with
\[
\rho_N=\cos(\pi/N),\qquad \cos\theta_N=\frac{1+3\cos(2\pi/N)}{4\cos(\pi/N)},\qquad 0<\theta_N<\pi.
\]
Thus every finite grid strictly attenuates the two symmetric modes, with spectral radius **exactly** \(\cos^N(\pi/N)\), while the skew mode is preserved. This spectral statement must not be confused with Euclidean operator-norm attenuation: the step matrix is generally nonnormal.

More precisely, set \(c=\cos\delta\), \(b=\sin\delta/\sqrt2\), \(v=(1-c)/4\), \(\omega=\sqrt{b^2-v^2}>0\), and \(\alpha=N\theta_N\). Then
\[
B_N^N=\rho_N^N\left[\cos\alpha\,I+\frac{\sin\alpha}{\omega}\begin{pmatrix}v&b\\-b&-v\end{pmatrix}\right].
\]
Its two singular values are exactly
\[
\sigma_\pm=\rho_N^N\left(\sqrt{1+\tau_N^2}\pm|\tau_N|\right),\qquad \tau_N=\frac{v\sin(N\theta_N)}{\omega}.
\]
Both singular values are strictly below one for every \(N\ge3\).

The exact continuous symmetric-plane holonomy is \(R(\sqrt2\pi)\), where \(R(\beta)=\left(\begin{smallmatrix}\cos\beta&\sin\beta\\-\sin\beta&\cos\beta\end{smallmatrix}\right)\). The loop's worst-case global error has the **sharp first-order constant**
\[
\boxed{\lim_{N\to\infty}N\|B_N^N-R(\sqrt2\pi)\|_2=\frac{\pi^2}{2}+\frac{\pi}{2\sqrt2}|\sin(\sqrt2\pi)|.}
\]
The full three-dimensional tangent-loop error has the same norm because the skew mode is transported exactly.

## Assumptions and scope

All matrices are real \(2\times2\), with \(\langle X,Z\rangle_F=\operatorname{tr}(X^\top Z)\). The underlying fixed-rank manifold is \(\mathcal M_1=\{Y\in\mathbb R^{2\times2}:\operatorname{rank}Y=1\}\). The state path has constant nonzero singular value, so there is no singular-rank event. The curve closes at \(t=\pi\). Only the **homogeneous covariant equation** and **exact state projectors** are considered: no claim is made for inexact state bases or a nonzero forcing term.

For \(u_\perp(t)=(-\sin t,\cos t)^\top\), the normal line is spanned by \(n(t)=u_\perp(t)u_\perp(t)^\top\), which is Frobenius-unit; hence \(P_t Z=Z-\langle n(t),Z\rangle_Fn(t)\). Define the orthonormal ambient matrices
\[
E_1=\frac1{\sqrt2}\begin{pmatrix}-1&0\\0&1\end{pmatrix},\quad E_2=-\frac1{\sqrt2}\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad E_3=\frac I{\sqrt2},\quad A=\frac1{\sqrt2}\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Put \(r(t)=\cos(2t)E_1+\sin(2t)E_2\), \(f_1(t)=(r(t)-E_3)/\sqrt2\), and \(f_2(t)=-\sin(2t)E_1+\cos(2t)E_2\). The orthonormal tangent frame is \((f_1(t),f_2(t),A)\), which is periodic at \(t=\pi\).

## Proof

**1. Normal and tangent splitting.** The Frobenius normal at a rank-one point \(Y=uv^\top\), for nonzero \(u,v\in\mathbb R^2\), is \(u^\perp(v^\perp)^\top\). In the symmetric trajectory \(Y=uu^\top\), it is exactly \(n=u_\perp u_\perp^\top=(E_3+r)/\sqrt2\). Direct inner products show \(f_1,f_2,A\) form an orthonormal basis of its orthogonal complement. All normals are symmetric, so projection fixes the skew vector \(A\) at every step.

**2. Continuous holonomy.** Differentiating the moving symmetric frame gives \(f_1'=\sqrt2f_2\) and \(f_2'=-\sqrt2(f_1+n)\). Thus, if \(Q(t)=a(t)f_1(t)+b(t)f_2(t)+c(t)A\), the equation \(P_t\dot Q=0\) is equivalent to \(a'=\sqrt2 b\), \(b'=-\sqrt2 a\), and \(c'=0\). Hence its symmetric-plane coefficient map from \(0\) to \(\pi\) is \(R(\sqrt2\pi)\) and the skew component is fixed.

**3. Discrete coefficient map.** Orthogonal projection from the old tangent plane onto the next tangent plane sends coefficient \(j\) to the inner product \(\langle f_i(t_{j+1}),f_j(t_j)\rangle_F\). Since the frame rotates by the same angle \(\delta=2\pi/N\) at each step, these inner products are the displayed constant matrix \(B_N\). The endpoint frame agrees with the initial frame, so the loop map is \(B_N^N\) on the symmetric plane and identity on \(A\).

**4. Spectrum, powers and singular values.** With \(c=\cos\delta\), direct calculation gives \(\operatorname{tr}B_N=(1+3c)/2\) and \(\det B_N=(1+c)/2=\rho_N^2\). The characteristic discriminant is \((c-1)(9c+7)/4<0\), because \(-1/2\le c<1\) for \(N\ge3\). Thus the eigenvalues are a nonreal conjugate pair of modulus \(\rho_N\), with the stated \(\theta_N\). Writing \(B_N=\rho_N\cos\theta_N I+H\), where \(H=\left(\begin{smallmatrix}v&b\\-b&-v\end{smallmatrix}\right)\) and \(H^2=-\omega^2I\), yields the power formula.

For \(M=B_N^N/\rho_N^N\), \(\det M=1\) and \(\operatorname{tr}(M^\top M)=2+4\tau_N^2\). Its singular values must therefore equal \(\sqrt{1+\tau_N^2}\pm|\tau_N|\). Strict norm contraction for the symmetric plane follows directly from the projection chain: equality at the final step would require one initial symmetric vector to be orthogonal to every normal \(n(t_j)\), \(j=1,\ldots,N\). These normals span the full three-dimensional symmetric ambient space (already three equally spaced normals do for \(N\ge3\)); hence no such nonzero vector exists. In particular the larger displayed singular value is strictly below one.

**5. Sharp asymptotics.** Taylor expansions as \(N\to\infty\) give
\[
\rho_N^N=1-\frac{\pi^2}{2N}+O(N^{-2}),\quad N\theta_N=\sqrt2\pi+O(N^{-2}),\quad \frac v\omega=\frac{\pi}{2\sqrt2N}+O(N^{-3}),\quad \frac b\omega=1+O(N^{-2}).
\]
Consequently, with \(D=\operatorname{diag}(1,-1)\) and \(\Omega=\sqrt2\pi\),
\[
B_N^N-R(\Omega)=\frac1N\left[-\frac{\pi^2}2R(\Omega)+\frac{\pi\sin\Omega}{2\sqrt2}D\right]+O(N^{-2})
\]
in operator norm. The matrix \(R(\Omega)^\top D\) is a symmetric involution with eigenvalues \(\pm1\). Multiplying the leading coefficient by \(R(\Omega)^\top\), its spectral norm is therefore \(\pi^2/2+(\pi/(2\sqrt2))|\sin\Omega|\). This proves the asserted limit and sharpness.

## Verification

The standalone `verify.py` uses only the Python standard library. It independently forms the moving orthonormal Frobenius frames, compares projected step coefficients to \(B_N\), checks characteristic identities and the closed power/singular-value formulas, verifies exact rational special cases at \(N=3,4\), and checks convergence of the finite-grid error toward the proven asymptotic constant. Run `python3 verify.py` in the directory containing the file. Its floating-point checks supplement, but do not replace, the analytic proof above.

## Relationship to prior work

Carrel and Vanzan, *Dynamical low-rank approximations for the optimal control of matrix ODEs* (first publicly posted 2026-10-21; arXiv:2610.29554v1), Section 5.2.1, explicitly develops the projected-Euler covariant transport step and proves first-order global accuracy under general assumptions. The present calculation is a self-contained, homogeneous, exact-state, closed-loop benchmark for that step; it gives **finite-grid eigenvalues and singular values plus a sharp asymptotic error constant**, which are not stated in the inspected section or its adjacent analysis. Classical parallel transport and projected vector transport, including Boumal's manifold-optimization text, supply the geometric setting and are not claimed as novel. The projection-based scheme and first-order order estimate are prior knowledge.

## Limitations

This is one fixed-size, smooth, constant-singular-value closed curve and only the homogeneous covariant equation. It does not quantify gradient errors in a general control problem, prove behavior with nonzero forcing, or analyze inexact numerical state projectors. The exact special-loop algebra may be implied by older work on products of rotating orthogonal projections not identified in the literature search; broader priority remains uncertain. Numerical checks are finite and do not certify the infinite-\(N\) asymptotic independently of the analytic proof.

## References

1. B. Carrel and T. Vanzan, *Dynamical low-rank approximations for the optimal control of matrix ODEs*, arXiv:2610.29554v1 (2026-10-21), Section 5.2.1, https://arxiv.org/abs/2610.29554 .
2. N. Boumal, *An Introduction to Optimization on Smooth Manifolds*, Cambridge University Press (2023), discussion of projection to moving tangent spaces as a vector transport, https://www.nicolasboumal.net/book/IntroOptimManifolds_Boumal_2022.pdf .
3. M. Louis et al., *A Fanning Scheme for the Parallel Transport along Geodesics on Riemannian Manifolds*, SIAM Journal on Numerical Analysis **56** (2018), 2563–2584, https://doi.org/10.1137/17M1130617 (a different geometric numerical transport method).
4. D. Nguyen and S. Sommer, *Parallel transport on matrix manifolds and Exponential Action*, arXiv:2408.06054 (2024), https://arxiv.org/abs/2408.06054 (exact continuous transports on other matrix manifolds).
