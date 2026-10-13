# Exact annealed and quenched Gaussian-sketch BFGS rates in the plane

## Finding
For every real symmetric positive-definite \(2\times 2\) matrix \(H\), perform the rank-one inverse-BFGS matrix-inversion update with independent standard Gaussian sketches and any deterministic symmetric \(B_0\ne H^{-1}\). Write \(\lambda_1\ge\lambda_2>0\) for the eigenvalues of \(H\), set
\[
r=\frac{\sqrt{\lambda_1}-\sqrt{\lambda_2}}{\sqrt{\lambda_1}+\sqrt{\lambda_2}}\in[0,1),
\qquad E_n=H^{1/2}(B_n-H^{-1})H^{1/2},
\]
and measure squared inverse error by \(\lVert E_n\rVert_F^2\). Two generally different **exact asymptotic contraction factors** hold:
\[
\lim_{n\to\infty}\lVert E_n\rVert_F^{2/n}
=Q(r):=\left(\frac{1+r^2}{2}\right)^4\quad\text{almost surely},
\qquad
\lim_{n\to\infty}\left(\mathbb E\lVert E_n\rVert_F^2\right)^{1/n}=\Lambda(r).
\]
Here \(\Lambda(r)\) is the Perron eigenvalue of the explicit three-dimensional matrix
\[
T(r)=\begin{pmatrix}
3/8&3r/8&3r^2/8\\
r/2&(1+r^2)/4&(r+r^3)/4\\
r^2/8&(r+r^3)/16&(1+r^4)/16
\end{pmatrix}.
\]
Equivalently, it is the largest real root of
\[
512z^3-(352+128r^2+32r^4)z^2+(68-48r^2-20r^4)z-3(1-r^2)^2=0.
\]
Both \(Q\) and \(\Lambda\) increase strictly with \(r\) on \([0,1)\), and \(0<Q(r)<1\), \(0<\Lambda(r)<1\). In the isotropic case \(H=I_2\) and \(B_0=2I_2\), the stronger finite-time identity
\[
\mathbb E\lVert E_n\rVert_F^2=(3/8)^{n-1}\quad(n\ge1)
\]
holds, whereas the almost-sure squared-error factor is \(1/16\). This is a strict average-versus-typical rate separation within the original Gaussian-sketch inverse-BFGS update.

## Assumptions and scope
The Hessian \(H\) is fixed and positive definite in dimension two. The sketches \(s_k\), \(k\ge1\), are independent with law \(N(0,I_2)\), and independent of the deterministic initial matrix \(B_0=B_0^\top\ne H^{-1}\). There is no resampling or adaptation of the sketch law. The inverse-BFGS recurrence is
\[
G_k=\frac{s_ks_k^\top}{s_k^\top Hs_k},\qquad
B_k=G_k+(I-G_kH)B_{k-1}(I-HG_k)\quad(k\ge1).
\]
The normalizing inverse error is the \(H\)-weighted Frobenius error. Its behavior is not asserted to be the convergence rate of optimization iterates produced using these approximate inverses.

## Proof
**Step 1: exact projection identity.** Define \(u_k=H^{1/2}s_k/\lVert H^{1/2}s_k\rVert_2\), and let \(v_k\) be a unit vector orthogonal to \(u_k\). Because \(H^{1/2}G_kH^{1/2}=u_ku_k^\top\) and \(H^{-1}\) is a fixed point of the update, direct substitution gives
\[
E_k=(I-u_ku_k^\top)E_{k-1}(I-u_ku_k^\top)
=(v_k^\top E_{k-1}v_k)v_kv_k^\top.
\]
Writing \(u_k=(\cos\theta_k,\sin\theta_k)\) in the eigenbasis of \(H\) and rotating every \(u_k\) through the same right angle to obtain \(v_k\) yields, for every \(n\ge1\),
\[
\lVert E_n\rVert_F^2
=(v_1^\top E_0v_1)^2
\prod_{j=2}^n\cos^4(\theta_j-\theta_{j-1}). \tag{1}
\]
The first factor is positive almost surely for every nonzero symmetric \(E_0\): a nonzero quadratic form cannot vanish on a positive-measure set of angles. The product factors are positive almost surely, and \(\log|\cos(\theta_j-\theta_{j-1})|\) is integrable.

**Step 2: exact angular distribution.** Diagonalize \(H\) and put \(a=\sqrt{\lambda_1/\lambda_2}\). Polar change of variables for the bivariate normal \(H^{1/2}s_k\) gives the independent-angle law
\[
\mu_r(d\theta)=\frac{1-r^2}{2\pi(1-2r\cos2\theta+r^2)}\,d\theta,
\qquad r=\frac{a-1}{a+1}.
\]
It is the Poisson-kernel density at twice the angle, with exact Fourier moments
\[
\int e^{2im\theta}\,\mu_r(d\theta)=r^{|m|},\qquad m\in\mathbb Z.
\]
These identities follow either from the convergent geometric expansion of the Poisson kernel for \(r<1\) or by direct contour integration.

**Step 3: almost-sure factor.** The pair process \((\theta_{j-1},\theta_j)\) is stationary ergodic because it is a measurable function of an independent sequence. By the ergodic theorem, the normalized logarithm of (1) converges almost surely to \(4\mathbb E\log|\cos(\theta_2-\theta_1)|\). The standard logarithmic Fourier series, integrated against the absolutely continuous bounded product density (equivalently by Abel regularization), gives
\[
\mathbb E\log|\cos(\theta_2-\theta_1)|
=-\log2+\sum_{m\ge1}\frac{(-1)^{m-1}r^{2m}}m
=\log\frac{1+r^2}{2}.
\]
The initial factor in (1) contributes zero after division by \(n\). Exponentiating proves the \(Q(r)\) formula.

**Step 4: exact second-moment transfer operator.** On \(L^2(\mu_r)\), introduce the compact self-adjoint positive integral operator
\[
(K_rf)(\theta)=\int\cos^4(\theta-\phi)f(\phi)\,\mu_r(d\phi).
\]
If \(g(\theta)=(v(\theta)^\top E_0v(\theta))^2\), independence and (1) imply
\[
\mathbb E\lVert E_n\rVert_F^2
=\langle g,K_r^{n-1}{\boldsymbol1}\rangle_{L^2(\mu_r)}.
\]
The continuous kernel is nonnegative and positive for almost every pair of angles, so its largest eigenvalue is strictly positive, simple and has a strictly positive eigenfunction. Since both \(g\) and \({\boldsymbol1}\) pair positively with that eigenfunction, the \(n\)-th-root limit equals this eigenvalue. Reflection symmetry forces the leading eigenfunction to be even. The elementary identity
\[
\cos^4 t=\frac{3+4\cos2t+\cos4t}{8}
\]
shows that the even part of the range of \(K_r\) lies in the span of \(1,\cos2\theta,\cos4\theta\). Applying the Fourier moments from Step 2 to this basis gives precisely the displayed matrix \(T(r)\); its characteristic polynomial is the stated cubic. This proves the exact annealed rate for all nonzero initial symmetric errors.

**Step 5: range and anisotropy dependence.** For \(r<1\), the angular density is everywhere positive and \((K_r{\boldsymbol1})(\theta)<1\) for every \(\theta\). Continuity on the circle gives \(\sup_\theta(K_r{\boldsymbol1})(\theta)<1\); hence \(\Lambda(r)<1\). All entries of \(T(r)\) are nonnegative and nondecreasing on \([0,1)\); for \(r>0\) the matrix is positive and increases strictly in some entries. Perron monotonicity proves strict increase of \(\Lambda(r)\), including from \(r=0\). At \(r=0\), \(T(0)=\operatorname{diag}(3/8,1/4,1/16)\); as \(r\uparrow1\), \(T(r)\) approaches a rank-one matrix with largest eigenvalue one. The displayed formula for \(Q(r)\) similarly increases strictly. For \(H=I_2\), \(B_0=2I_2\), the first factor of (1) is identically one, and uniform independent angles make each subsequent conditional expected factor exactly \(3/8\), proving the stated finite-time identity.

## Verification
The companion `verify.py` is standalone Python 3 code using only the standard library. Running `python verify.py` checks 500 independent direct-matrix BFGS/projection identities, 100 distinct exact-rational characteristic-polynomial identities and corresponding Perron orderings, four angular-Fourier quadrature instances at 16,384 nodes, and three seeded 250,000-step simulations of the almost-sure logarithmic factor. The rational checks are exact; quadrature and simulation are numerical corroboration, not substitutes for the analytic proof. The supplied package path is the file to execute, without dependence on unpublished data.

## Relationship to prior work
Gower and Richtárik, *Randomized Quasi-Newton Updates Are Linearly Convergent Matrix Inversion Algorithms* (arXiv:1602.01768), established the stochastic inverse-BFGS recurrence and a general mean-square **upper bound** based on the smallest eigenvalue of the expected sketch projector. In the present model their factor is \((1+r)/2\), whereas the exact asymptotic mean-square factor obtained here is \(\Lambda(r)\). In particular, at \(r=0\) the published guarantee is \(1/2\) and the actual asymptotic factor is \(3/8\); thus the present claim is not that existing bound restated. Kovalev, Gower, Richtárik and Rogozin, *Fast Linear Convergence of Randomized BFGS* (arXiv:2002.11337), analyze optimization iterates and a coupled Lyapunov function and test Gaussian sketches but do not give the stated exact fixed-Hessian inverse-error rates. Gower, Hanzely, Richtárik and Stich (arXiv:1802.04079) analyze an **accelerated** matrix-inversion iteration rather than these exact nonaccelerated two-dimensional factors. General finite-rank transfer-operator and Poisson-kernel facts are classical mathematical tools; novelty is claimed only for their explicit combination into the Gaussian inverse-BFGS rates and exact isotropic separation, not for those tools.

## Limitations
The result is restricted to a **fixed** real positive-definite \(2\times2\) Hessian and independent isotropic Gaussian rank-one sketches. It does not analyze moving Hessians, adaptive or block sketches, higher-dimensional updates, computational cost, or convergence of optimization iterates. No priority claim is made about unpublished or unindexed equivalent formulas. The almost-sure factor describes a single infinite sample path and need not coincide with mean-square error reduction; finite simulated runs cannot prove either infinite limit.

## References
1. R. M. Gower and P. Richtárik, *Randomized Quasi-Newton Updates Are Linearly Convergent Matrix Inversion Algorithms*, arXiv:1602.01768, first submitted 4 February 2016. https://arxiv.org/abs/1602.01768
2. D. Kovalev, R. M. Gower, P. Richtárik and A. Rogozin, *Fast Linear Convergence of Randomized BFGS*, arXiv:2002.11337, first submitted 26 February 2020. https://arxiv.org/abs/2002.11337
3. R. M. Gower, F. Hanzely, P. Richtárik and S. Stich, *Accelerated Stochastic Matrix Inversion: General Theory and Speeding up BFGS Rules for Faster Second-Order Optimization*, arXiv:1802.04079, first submitted 12 February 2018. https://arxiv.org/abs/1802.04079
