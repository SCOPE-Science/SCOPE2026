# Exact fluctuation-symmetry obstruction for stationary Gaussian inertial gyrators

## Finding
Let \(X_t,V_t\in\mathbb R^2\) be a centered stationary, nondegenerate jointly Gaussian process with \(X_t=X_0+\int_0^t V_s\,ds\), and define instantaneous signed specific angular momentum \(L=X_{1,t}V_{2,t}-X_{2,t}V_{1,t}\). Set \(C=\mathbb E[XX^\top]\), \(D=\mathbb E[XV^\top]\), \(E=\mathbb E[VV^\top]\), and \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\). Stationarity makes \(D=hJ\) for one real \(h\). Let \(R=E-D^\top C^{-1}D\succ0\), and denote by \(\lambda_1,\lambda_2>0\) the eigenvalues of \(C^{1/2}JRJ^\top C^{1/2}\).

The **exact one-time law**, with its maximal moment-generating-function interval around zero, is
\[
\mathbb E[e^{sL}]=\left[(1-2hs-\lambda_1s^2)(1-2hs-\lambda_2s^2)\right]^{-1/2}.
\]
In particular \(\mathbb E L=2h\) and \(\operatorname{Var}(L)=4h^2+\lambda_1+\lambda_2\). If \(h\ne0\), the signal-to-noise ratio obeys the **sharp strict bound**
\[
0<\frac{|\mathbb EL|}{\sqrt{\operatorname{Var}(L)}}<1.
\]

Most importantly, write \(p_L\) for the strictly positive density of \(L\). There exists a real constant \(a\) satisfying an **exact instantaneous exponential fluctuation relation**
\[
p_L(\ell)=e^{a\ell}p_L(-\ell)\qquad(\ell\in\mathbb R)
\]
**if and only if** either \(h=0\) (symmetric distribution with \(a=0\)), or \(\lambda_1=\lambda_2=\lambda\) (when \(a=2h/\lambda\)). In the second case the complete density is the asymmetric Laplace law
\[
p_L(\ell)=\frac{\exp\!\left(\frac h\lambda\ell-\frac{\sqrt{h^2+\lambda}}\lambda|\ell|\right)}{2\sqrt{h^2+\lambda}}.
\]
Thus a nonzero rotation current does not generally imply an exact exponential asymmetry law: unequal eigenvalues of the **conditional velocity-noise covariance in position-whitened coordinates** are a complete obstruction.

## Assumptions and scope
The process need not be Markovian, but its one-time joint distribution must be centered nondegenerate Gaussian and its position must possess the stated continuous velocity derivative in integral form. Stationarity here refers to equal-time position covariances; it guarantees \(D+D^\top=0\). The theorem concerns **instantaneous** mechanical angular momentum, not finite-difference overdamped estimators, winding angle, integrated angular momentum, entropy production, or a nonlinear ellipsoid with unsuppressed orientation fluctuations. The matrices are evaluated at one stationary time. The positive Schur complement \(R\) follows from nondegeneracy of the joint covariance.

## Proof
**1. Stationary skew covariance.** Differentiate \(\mathbb E[X_tX_t^\top]\) using the pathwise integral relation and finite Gaussian moments. Its derivative is \(D+D^\top\), hence zero. Every real skew \(2\times2\) matrix is \(hJ\).

**2. Gaussian regression.** Write \(V=D^\top C^{-1}X+\epsilon\), where \(\epsilon\) is independent of \(X\), centered Gaussian with covariance \(R\). Since \(JD^\top=hI\),
\[
L=hX^\top C^{-1}X+X^\top J\epsilon.
\]
Choose a factorization \(C=BB^\top\) and whiten \(X=BZ\) with \(Z\sim N(0,I_2)\). The vector \(B^\top J\epsilon\) is independent of \(Z\) and has covariance \(B^\top JRJ^\top B\). Orthogonally diagonalizing that matrix, and rotating \(Z\) by the same orthogonal matrix, gives independent standard normal \(Z_1,Z_2,Y_1,Y_2\) with
\[
L\overset d=\sum_{j=1}^{2}(hZ_j^2+\sqrt{\lambda_j}Z_jY_j).
\]
(The eigenvalues agree with those in the statement because the two covariance factors differ by an orthogonal transformation.) For one index, conditioning on \(Z_j\) and integrating a standard Gaussian yields \(\mathbb E\exp[s(hZ_j^2+\sqrt{\lambda_j}Z_jY_j)]=(1-2hs-\lambda_js^2)^{-1/2}\) wherever the denominator is positive. Independence proves the moment-generating function. Its first two derivatives at zero prove the moment identities and strict bound. A convolution of two nondegenerate product-normal densities has an everywhere positive continuous density.

**3. Sufficiency of symmetry conditions.** If \(h=0\), the representation is invariant under \((Y_1,Y_2)\mapsto(-Y_1,-Y_2)\), giving \(p_L(\ell)=p_L(-\ell)\). If both eigenvalues equal \(\lambda\), the moment-generating function becomes \((1-2hs-\lambda s^2)^{-1}\). Direct Laplace integration of the density displayed above gives this same function on an open interval around zero, so moment-generating-function uniqueness yields the density and the fluctuation relation with \(a=2h/\lambda\).

**4. Necessity.** If \(p_L(\ell)=e^{a\ell}p_L(-\ell)\), its moment-generating function satisfies \(M(s)=M(-a-s)\) on a neighborhood of \(s=-a/2\). Positivity of the density and exponential moments near zero ensure both arguments belong to the common open moment domain. Squaring and inverting gives the polynomial identity \(F(s)=F(-a-s)\), where
\[
F(s)=(1-2hs-\lambda_1s^2)(1-2hs-\lambda_2s^2).
\]
Every quartic polynomial symmetric around \(c=-a/2\) has \(F'(c)=F'''(c)=0\). Direct differentiation shows \(F'''(c)=0\) only at
\[
c=-\frac{h(\lambda_1+\lambda_2)}{2\lambda_1\lambda_2},
\]
and at this point
\[
F'(c)=\frac{h(\lambda_1-\lambda_2)^2[\lambda_1\lambda_2+h^2(\lambda_1+\lambda_2)]}{\lambda_1^2\lambda_2^2}.
\]
All eigenvalues are strictly positive. Thus \(F'(c)=0\) forces \(h=0\) or \(\lambda_1=\lambda_2\). This completes the characterization.

**5. Sharpness and nontriviality in physical Langevin systems.** For every \(\varepsilon>0\), consider the stable linear underdamped Langevin system (independent two-dimensional Wiener noise)
\[
dX_t=V_t\,dt,\qquad dV_t=[-(1+\varepsilon)X_t+JX_t-V_t]dt+\sqrt{2\varepsilon}\,dW_t.
\]
It has stationary blocks \(C=I_2\), \(D=-J\), \(E=(1+\varepsilon)I_2\), verified by its Lyapunov equation. Hence \(h=-1\), \(R=\varepsilon I_2\) and \(\lambda_1=\lambda_2=\varepsilon\). Its signal-to-noise ratio is \(2/\sqrt{4+2\varepsilon}\nearrow1\) as \(\varepsilon\downarrow0\), proving sharpness (the limiting covariance is degenerate and is **not** included in the theorem).

For a standard two-temperature *conservative* harmonic gyrator, \(dX=Vdt\), \(dV=-(KX+V)dt+\operatorname{diag}(\sqrt2,\sqrt6)dW\), with \(K=\begin{psmallmatrix}2&1/2\\1/2&3/2\end{psmallmatrix}\), its exact stationary blocks are
\[
C=\begin{pmatrix}2/3&-14/33\\-14/33&68/33\end{pmatrix},\quad D=(8/33)J,\quad E=\begin{pmatrix}37/33&-2/33\\-2/33&95/33\end{pmatrix}.
\]
The eigenvalue discriminant of \(CJRJ^\top\) is \(24700/11979>0\), so \(h\ne0\) but \(\lambda_1\ne\lambda_2\); this explicit thermally driven gyrator **cannot** obey any exact linear-slope instantaneous asymmetry relation.

## Verification
The accompanying standalone `verify_gyrator.py` checks the polynomial derivative factorization symbolically, solves stationary Lyapunov equations for a finite grid of harmonic two-bath examples, compares the Gaussian-quadratic determinant and factorized moment-generating functions, checks both first moments and variances, and verifies the sharpness-family covariance. It passes 255 deterministic checks with fixed inputs and no stochastic sampling. The proof is analytic and not inferred from this finite grid. To reproduce: `python verify_gyrator.py` with Python, NumPy, SciPy and SymPy installed. The rational example and the algebraic obstruction are supplied explicitly above.

## Relationship to prior work
Dutta and Saha (2026) investigate inertial Brownian-ellipsoid gyration, numerically graphing the instantaneous specific-angular-momentum distribution and signal-to-noise ratio and analytically treating the steady covariance in a small-anisotropy linearization. Their reported observation that the plotted signal-to-noise ratio is below one is **prior work**, not claimed here as a newly discovered empirical effect. The present theorem instead provides an all-covariance closed moment-generating function and a necessary-and-sufficient criterion for an exact instantaneous exponential fluctuation relation, distinguishing conditional rotational noise isotropy from genuine anisotropy.

Viot et al. (2023) derive angular-momentum PDFs and characteristic functions for a different **overdamped finite-increment** observable; those formulas do not by themselves establish the present continuous-velocity planar Gaussian classification. Cerasoli et al. (2018) analyze asymmetry of **position distributions** in biased Brownian gyrators, not this instantaneous kinetic angular-momentum law. Classical Gaussian conditioning, quadratic-form determinants and the asymmetric Laplace distribution are established tools rather than novel claims. Exact fluctuation relations for integrated currents and entropy production are distinct observables.

## Limitations
This is a one-time Gaussian theorem, not a general fluctuation theorem for arbitrary nonequilibrium processes. In the full nonlinear ellipsoid model, orientation fluctuations can destroy Gaussianity, so the theorem applies to its Gaussian linearized regimes only when stationary Gaussianity and the stated velocity relation are independently valid. It does not assert anything about temporal correlations, time-integrated angular momentum, or non-Gaussian bath forcing. Gaussian quadratic-form or generalized-hyperbolic literature could contain implicit equivalent formulas; priority beyond the inspected gyrator literature requires further independent review. No independent audit has been performed.

## References
1. S. Dutta and A. Saha, *Brownian gyration of an inertial ellipsoid*, arXiv:2606.17554v1, first public 2026-06-16. https://arxiv.org/abs/2606.17554
2. A. Viot, A. Argun, G. Volpe, A. Imparato, L. Rondoni, and G. Oshanin, *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248 (2023), especially Section 3 and Supplementary Section 7.2. https://arxiv.org/abs/2307.05248
3. S. Cerasoli, V. Dotsenko, G. Oshanin, and L. Rondoni, *Asymmetry relations and effective temperatures for biased Brownian gyrators*, arXiv:1810.02580 (2018). https://arxiv.org/abs/1810.02580
