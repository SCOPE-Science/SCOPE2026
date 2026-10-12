# Universal mean-square energy inflation under randomized symplectic Euler steps

## Finding

For the harmonic oscillator \(q'=p\), \(p'=-q\), every nonconstant independent random choice of individually stable symplectic Euler step sizes causes **exponential growth of the expected squared amplitude**. More precisely, let \(S_h\) be the kick-then-drift symplectic Euler map

\[
S_h=\begin{pmatrix}1-h^2&h\\-h&1\end{pmatrix},\qquad 0<h<2.
\]

If the \(H_j\) are identically distributed independent variables supported in the open interval \((0,2)\) and their common law is not a point mass, there exists a number \(\rho>1\) and constants \(c,C>0\), depending only on their common law, such that for every nonzero \(x_0\in\mathbb R^2\) and every integer \(k\ge0\),

\[
c\rho^k\|x_0\|_2^2\le\mathbb E\|S_{H_{k-1}}\cdots S_{H_0}x_0\|_2^2
\le C\rho^k\|x_0\|_2^2.
\]

The exact rate \(\rho\) is the spectral radius of the three-dimensional covariance map \(\mathcal T(P)=\mathbb E[S_HP S_H^{\mathsf T}]\). For a deterministic step \(H=h\in(0,2)\), the corresponding covariance spectral radius equals one and all orbits are bounded. Therefore nonzero step variability is a sharp *universal* criterion for mean-square energy inflation on the deterministic step-stability interval.

For equiprobable steps \(H\in\{1/2,1\}\), \(\rho=1.0179718538645\ldots\) is the unique real root of

\[
64z^3-66z^2+49z-49=0.
\]

Although \(\mathbb E\|X_k\|_2^2\) grows exponentially, the mean iterate \(\mathbb E X_k\) decays geometrically for this example.

For fixed \(h\in(0,2)\) and symmetric two-point jitter \(H=h\pm\delta\), each with probability \(1/2\),

\[
\rho(h,\delta)=1+\frac{2h^2}{4-h^2}\delta^2+O_h(\delta^4)
\quad(\delta\longrightarrow0).
\]

## Assumptions and scope

All arithmetic is exact. The physical oscillator has unit frequency, so the step parameter is dimensionless. The timestep law can be discrete or continuous and need not have a density; it must be a probability measure concentrated on \((0,2)\). Independent steps with the same law are drawn at each iteration. The conclusion is about fixed-step-count infinite-horizon **second moments** of numerical state vectors, not about almost-sure instability or simulation accuracy at fixed physical time. No additive forcing or damping is present.

The scheme first updates \(p_{k+1}=p_k-H_kq_k\), then \(q_{k+1}=q_k+H_kp_{k+1}\). Every \(S_h\) has determinant one, and for \(0<h<2\) its eigenvalues are distinct complex conjugates on the unit circle, because \(\operatorname{tr}S_h=2-h^2\in(-2,2)\). Every single fixed-step method therefore has bounded matrix powers.

## Proof

**1. Positive eigenmatrices for the covariance operator.** Let \(\mathcal S\) be the real vector space of symmetric \(2\times2\) matrices and \(\mathcal K\subset\mathcal S\) its positive-semidefinite cone. The linear map

\[
\mathcal T(P)=\mathbb E[S_HP S_H^{\mathsf T}]
\]

preserves \(\mathcal K\). The elementary finite-dimensional Perron–Frobenius theorem for a proper cone yields an eigenmatrix \(P\in\mathcal K\setminus\{0\}\) corresponding to the spectral radius \(\rho\ge0\). It cannot be rank one: if \(P=vv^{\mathsf T}\), then \(\mathbb E[(S_Hv)(S_Hv)^{\mathsf T}]=\rho vv^{\mathsf T}\) forces \(S_hv\) to lie in the real line spanned by \(v\) for almost every \(h\), whereas every \(S_h\) in the support interval has no real eigenline. Thus \(P\succ0\). The same argument for \(\mathcal T^*(Q)=\mathbb E[S_H^{\mathsf T}QS_H]\) gives \(Q\succ0\) with \(\mathcal T^*(Q)=\rho Q\). The matrices are well-defined for every law under consideration since the entries of \(S_h\) are uniformly bounded for \(0<h<2\).

**2. Strict determinant growth.** The function \(\det(P)^{1/2}\) is concave on positive-definite \(2\times2\) matrices, with equality in its Jensen inequality only for pairwise proportional matrices. Since \(\det S_h=1\),

\[
\rho\det(P)^{1/2}=\det(\mathcal T(P))^{1/2}
\ge\mathbb E\det(S_HP S_H^{\mathsf T})^{1/2}
=\det(P)^{1/2}.
\]

Hence \(\rho\ge1\). If \(\rho=1\), equality forces all \(S_hPS_h^{\mathsf T}\) to coincide almost surely; their common determinant equals \(\det P\), and their average equals \(P\), so \(S_hPS_h^{\mathsf T}=P\) almost surely. Write \(P=\begin{psmallmatrix}a&b\\b&c\end{psmallmatrix}\) with \(a>0\). Equating the lower-right entries gives \(b=ha/2\), while the off-diagonal entry then gives \(c=a\). Thus every such invariant positive-definite matrix is a scalar multiple of

\[
P_h=\begin{pmatrix}1&h/2\\h/2&1\end{pmatrix}.
\]

For two different positive steps these matrices are not proportional. Therefore a common invariant \(P\) forces the timestep law to be a point mass, contradicting the hypothesis. Hence \(\rho>1\).

**3. Uniform exponential lower and upper bounds.** Independence gives the covariance recursion \(\mathbb E[X_kX_k^{\mathsf T}]=\mathcal T^k(x_0x_0^{\mathsf T})\). The dual eigenmatrix therefore supplies the *exact* identity

\[
\mathbb E[X_k^{\mathsf T}QX_k]=\rho^k x_0^{\mathsf T}Qx_0.
\]

With \(0<\lambda_{\min}(Q)\le\lambda_{\max}(Q)\), this proves the claimed bounds using \(c=\lambda_{\min}(Q)/\lambda_{\max}(Q)\) and \(C=1/c\). The deterministic case is bounded because \(P_h\succ0\) (its determinant is \(1-h^2/4>0\)) and \(S_hP_hS_h^{\mathsf T}=P_h\).

**4. Exact rational two-step-law witness.** On \(P=\begin{psmallmatrix}a&b\\b&c\end{psmallmatrix}\), the covariance map for fixed \(h\) has matrix

\[
M_h=\begin{pmatrix}
(1-h^2)^2&2h(1-h^2)&h^2\\
-h(1-h^2)&1-2h^2&h\\
h^2&-2h&1
\end{pmatrix}
\]

in coordinates \((a,b,c)\). Averaging \(h=1/2\) and \(h=1\) yields

\[
M=\begin{pmatrix}
9/32&3/8&5/8\\-3/16&-1/4&3/4\\5/8&-3/2&1
\end{pmatrix},\qquad
\det(zI-M)=\frac{64z^3-66z^2+49z-49}{64}.
\]

The derivative \(192z^2-132z+49\) of the integer polynomial is positive on the real line (negative discriminant), and the polynomial changes sign between \(1\) and \(51/50\). Thus its unique real root exceeds one. The positive-cone argument above identifies this root as \(\rho\). Meanwhile, the mean-state transition is

\[
\bar S=\mathbb E S_H=\begin{pmatrix}3/8&3/4\\-3/4&1\end{pmatrix}
\]

with conjugate eigenvalues of modulus \(\sqrt{15}/4<1\), proving decay of the mean state.

**5. Small-jitter expansion.** At deterministic \(h\in(0,2)\), the eigenvalue one of \(\mathcal T_h\) is simple: the other two covariance eigenvalues equal \(e^{\pm2i\theta}\), where the eigenvalues of \(S_h\) are \(e^{\pm i\theta}\) with \(0<\theta<\pi\). Its positive right and left eigenmatrices are \(P_h\) and \(Q_h=P_h^{-1}\). The symmetric two-point covariance map is polynomial and even in \(\delta\). Direct multiplication gives

\[
\frac{\operatorname{tr}\left(Q_h(\mathcal T_{h,\delta}(P_h)-P_h)\right)}{\operatorname{tr}(Q_hP_h)}
=\frac{2\delta^2(h^2+\delta^2)}{4-h^2}.
\]

Analytic perturbation of the simple eigenvalue one gives the displayed leading coefficient \(2h^2/(4-h^2)\) and a remainder of order \(O_h(\delta^4)\). The eigenvalue branch is the positive covariance spectral radius for sufficiently small \(|\delta|\).

## Verification

The accompanying `verify.py` runs with the Python 3 standard library. It checks the fixed-step symplectic determinant and invariant quadratic forms, the exact \(3\times3\) covariance matrix and characteristic coefficients for the rational witness, the mean-state spectrum, 762 explicitly enumerated finite histories contributing to 21 expected-error checks (three starting vectors, horizons one through seven), and exact small-jitter Rayleigh-quotient identities at multiple rational parameters. Run `python verify.py`. These finite tests check arithmetic identities and small cases; they do not substitute for the infinite-horizon determinant-concavity and cone arguments.

## Relationship to prior work

Abdulle and Garegnani introduced random-time-step probabilistic integrators, gave weak/mean-square convergence estimates, and investigated symplectic energy behavior on long but finite time horizons. In particular, their Theorem 6 includes a finite-time restriction and a proximity assumption; its Remark 12 discusses drift under varying symplectic steps. Those results are consistent with, but do not state, the universal infinite-step strict covariance spectral-radius criterion, the two-point exact witness, or the small-jitter spectral coefficient proved above.

Earlier numerical celestial-mechanics work by Kaib, Quinn and Brasser addresses energy errors of adaptive timestep symplectic schemes, rather than this independent fixed-law oscillator calculation. Sturman and Thiffeault examine random products of two shear matrices, but their random product law differs from the coupled opposite-shear factors in each symplectic Euler update. Classical cone Perron–Frobenius theory and determinant concavity are used as established tools; their priority is not claimed.

## Limitations

Only the kick-then-drift first-order symplectic Euler discretization of the *undamped linear oscillator* is covered. The infinite-horizon limit fixes the distribution and counts iteration steps, not elapsed physical time. Mean-square divergence does not itself imply divergence almost surely or loss of finite-time weak/strong accuracy. In particular, midpoint integration has a common Euclidean invariant and is not subject to this assertion. The numerical estimate of the rational-witness rate is illustrative; the exact polynomial uniquely defines it. Equivalence to a special case of a broader unpublished or unindexed random-matrix theorem has not been excluded. No independent external verification was performed.

## References

1. A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340 (first posted 2018-01-04), Sections 2, 7, 9.6 and Theorem 6, https://arxiv.org/abs/1801.01340 .
2. N. Kaib, T. Quinn and R. Brasser, *Decreasing Computing Time with Symplectic Correctors in Adaptive Timestepping Routines*, arXiv:1011.3830, https://arxiv.org/abs/1011.3830 .
3. R. Sturman and J.-L. Thiffeault, *Lyapunov Exponents for the Random Product of Two Shears*, Journal of Nonlinear Science (2019), https://doi.org/10.1007/s00332-018-9497-3 .
