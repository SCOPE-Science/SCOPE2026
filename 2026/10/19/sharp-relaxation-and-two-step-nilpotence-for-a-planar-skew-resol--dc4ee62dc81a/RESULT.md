# Sharp relaxation and two-step nilpotence for a planar skew-resolvent saddle iteration

## Finding

A simple bilinear saddle model has a sharp and complete relaxation phase diagram. More strikingly, a *unique* positive forward step and relaxation make the fixed iteration matrix nonzero but square-zero exactly when the scalar primal curvature is less than twice the coupling strength. The resulting solver reaches the saddle after two iterations from **every** starting pair in exact arithmetic. Outside that curvature-coupling region, finite universal termination by any fixed positive pair is impossible.

Let the positive constants be \(q,c>0\). Consider the convex-concave saddle function
\[
\Phi(x,y)=\frac q2x^2-cxy,\qquad (x,y)\in\mathbb R^2.
\]
Its unique saddle is \((0,0)\). Let \(z=(x,y)^{\mathsf T}\), and split the KKT operator as
\[
F=\begin{pmatrix}q&0\\0&0\end{pmatrix},\qquad
S=\begin{pmatrix}0&-c\\c&0\end{pmatrix},\qquad 0=(F+S)z.
\]
For forward step \(\tau>0\) and relaxation \(\rho>0\), define the **constant relaxed forward--backward map** (with skew part implicit and smooth part explicit)
\[
K_{\tau,\rho}=(1-\rho)I+\rho(I+\tau S)^{-1}(I-\tau F),\qquad z_{k+1}=K_{\tau,\rho}z_k.
\]
This is not an assertion about the distinct anchored Halpern iteration or a particular ADMM block sweep.

Put \(h=\tau q\), \(s=\tau c\), and
\[
t=\frac{2s^2+h}{1+s^2},\qquad d=\frac{s^2}{1+s^2},\qquad
\Delta=t^2-4d=\frac{h^2+4s^2(h-1)}{(1+s^2)^2}.
\]
Then \(t,d>0\). The following formulas characterize convergence from **every** real initial point and minimize the asymptotic spectral radius over **all positive relaxations at fixed \(\tau\)**:

* If \(\Delta>0\), the eigenvalues of \(I-K_{\tau,\rho}\), divided by \(\rho\), are \(\mu_\pm=(t\pm\sqrt\Delta)/2>0\). The iteration converges geometrically for every start exactly when \(0<\rho<4/(t+\sqrt\Delta)\). Its unique spectrally fastest relaxation is \(\rho_{\mathrm{opt}}=2/t\), with minimal radius \(\sqrt\Delta/t\).
* If \(\Delta<0\), the eigenvalues are a conjugate pair. Convergence for every start holds exactly when \(0<\rho<t/d\). The unique spectrally fastest relaxation is \(\rho_{\mathrm{opt}}=t/(2d)\), with minimal radius \(\sqrt{1-t^2/(4d)}\).
* If \(\Delta=0\), both formulas agree: convergence holds exactly when \(0<\rho<4/t\), and the unique spectrally optimal choice is \(\rho=2/t\), where the radius is zero and \(K_{\tau,\rho}^2=0\ne K_{\tau,\rho}\). It is the sole universal finite-termination relaxation at that fixed step.

The equality case in each strict convergence bound is *not* globally attracting: at least one eigenvalue has modulus one.

In particular, the only positive globally two-step-terminating tuning is
\[
\boxed{\tau_*=\frac{4c^2-q^2}{4c^2q},\qquad
\rho_*=\frac{4c^2+q^2}{4c^2-q^2}}\qquad (0<q<2c).
\]
It satisfies \(\rho_*>2\) exactly for \(2c/\sqrt3<q<2c\). For the rational example \(q=3/2\), \(c=1\), \(\tau_*=7/24\), \(\rho_*=25/7\), one obtains
\[
K_{\tau_*,\rho_*}=\begin{pmatrix}-18/25&24/25\\-27/50&18/25\end{pmatrix},\qquad
K_{\tau_*,\rho_*}^2=0.
\]

## Assumptions and scope

All scalar parameters \(q,c,\tau,\rho\) are strictly positive; all spaces, operators and iterates are real and two-dimensional; coefficients and iteration are exact. The algorithm applies fixed parameters to every iterate, without anchoring, adaptive changes or noise. Convergence means \(K_{\tau,\rho}^kz_0\to0\) for **every** initial vector, not a claim of one-step monotonicity in the Euclidean norm. The rate measures spectral radius, so nonnormal finite transients are permitted.

The saddle is unique because the first-order KKT operator \(F+S\) is invertible (determinant \(c^2>0\)); its saddle inequalities also hold because \(\Phi(0,y)=0\le\Phi(x,0)\). The no-finite-termination statement concerns the existence of a fixed \(\tau,\rho>0\) and a finite \(N\) with \(K_{\tau,\rho}^N=0\) on *all* starts, not the possibility of special starts reaching zero.

## Proof

**1. Matrix and characteristic polynomial.** Since
\[
(I+\tau S)^{-1}=\frac1{1+s^2}\begin{pmatrix}1&s\\-s&1\end{pmatrix},
\]
the displacement \(D=\rho^{-1}(I-K_{\tau,\rho})\) is
\[
D=\frac1{1+s^2}\begin{pmatrix}s^2+h&-s\\s(1-h)&s^2\end{pmatrix}.
\]
Direct multiplication gives \(\operatorname{tr}D=t\), \(\det D=d\), and the displayed \(\Delta\). Its two eigenvalues are \(\mu_\pm=(t\pm\sqrt\Delta)/2\). When the roots are real they are both positive, because their sum and product are positive. The eigenvalues of \(K\) are \(1-\rho\mu_\pm\). All formulas therefore hold without assuming diagonalizability.

**2. Exact Schur boundaries.** With two positive real roots, both \(|1-\rho\mu_\pm|<1\) precisely when \(0<\rho<2/\mu_+=4/(t+\sqrt\Delta)\). With conjugate roots, the common squared modulus is
\[
|1-\rho\mu_\pm|^2=1-\rho t+\rho^2d;
\]
it is below one precisely when \(0<\rho<t/d\). These criteria also apply at \(\Delta=0\) by continuity, giving \(0<\rho<4/t\). Spectral radius below one is equivalent to convergence for every start even for a defective two-by-two matrix; spectral radius at least one cannot give convergence for all starts.

**3. Unique optimal relaxation for a fixed step.** In the real-root regime the maximum of \(|1-\rho\mu_-|\) and \(|1-\rho\mu_+|\) is minimized uniquely when these two errors have opposite signs and equal modulus, i.e. \(\rho=2/(\mu_-+\mu_+)=2/t\). The resulting radius is \(\sqrt\Delta/t\). In the complex-root regime the squared modulus is a strictly convex quadratic in \(\rho\), uniquely minimized at \(t/(2d)\) with radius \(\sqrt{1-t^2/(4d)}\). At the double-root boundary the two minimizers coincide and the spectral radius vanishes.

**4. The curvature-coupling threshold and unique nilpotence.** The discriminant identity has numerator
\[
\tau^2\big(q^2+4c^2(\tau q-1)\big).
\]
Because \(\tau>0\), \(\Delta=0\) has exactly one positive root precisely when \(q<2c\), namely \(\tau_*=(4c^2-q^2)/(4c^2q)\). At that step \(\rho=2/t\) is the unique choice making both eigenvalues of \(K\) vanish, and simplifying \(2/t\) gives the stated \(\rho_*\). Cayley--Hamilton now gives \(K^2=0\). Its off-diagonal entry is \(\rho s/(1+s^2)>0\), so \(K\ne0\) and its nilpotency index equals two. Conversely, if \(K^N=0\) for any finite positive \(N\), its two eigenvalues both vanish; thus \(\rho\mu_+=\rho\mu_-=1\), forcing \(\Delta=0\) and the same unique parameters. When \(q\ge2c\), the discriminant is strictly positive at every positive step, ruling out finite universal termination. Finally \(\rho_*>2\) reduces algebraically to \(3q^2>4c^2\), i.e. \(q>2c/\sqrt3\).

## Verification

Run the included standard-library Python program `verify.py` using `python verify.py`. It independently assembles the iteration matrix, compares trace, determinant and roots over 5,000 reproducible positive parameter samples, checks every piecewise stability boundary and optimum, and verifies nilpotence with exact rational arithmetic over a family of curvature-coupling ratios. The recorded reproduction result is 50,139 counted verification checks and no failures. These finite tests verify implementation identities and examples, **not** the universal inequalities; those are proved above.

The rational case with \(q=3/2,c=1\) is a particularly transparent exact certificate: multiplying the displayed rational matrix by itself gives the zero matrix entrywise.

## Relationship to prior work

Zhang, Liu and Zhang (2026), arXiv:2609.38808v1, §2, Eq. (2.15), introduces a preconditioned forward--backward fixed-point form for majorized ADMM and proves generic nonexpansiveness and a sufficient outer relaxation interval in §§3--4. In contrast, the present **standalone two-dimensional skew-resolvent model** determines the exact spectral stability boundary, the unique fixed-step rate-optimal relaxation, and sharp two-step nilpotence feasibility; it does not claim these formulas for majorized ADMM itself. The source's relaxation guarantee is sufficient for its metric nonexpansiveness and Halpern analysis, not a necessary bound for the present matrix. The explicit parameter values beyond two are not a contradiction to that theorem.

Briceño-Arias and Combettes (2010), arXiv:1011.5517v1, formulate primal--dual monotone-plus-skew inclusions and analyze a **forward--backward--forward** algorithm that treats the skew operator explicitly in two evaluations, rather than the skew-resolvent map analyzed here. Its general framework motivates the splitting but does not state this exact scalar phase diagram.

Closely related prior numerical work studies other matrices and objectives: two-dimensional PDHG with fixed-product step tuning, warm-start termination of over-relaxed ADMM, and the two-step-memory forward-reflected-backward method. Their rate or termination statements do not algebraically imply this result, because the underlying iteration matrices differ. Exhaustive literature uniqueness is not claimed.

## Limitations

This is an exact-arithmetic result for a fixed, 2-by-2 linear map with one nonzero smooth curvature and bilinear coupling. It does not cover the anchored Halpern iteration, a general preconditioner, actual majorized ADMM implementations, finite precision, large-scale or multi-mode coupling, noise or nonlinear smooth terms. Near \(q=2c\) from below, the nilpotent relaxation is large and may lead to transient amplification or parameter sensitivity; finite termination is therefore not a numerical-conditioning guarantee. Prior results in unindexed operator-splitting literature might give equivalent specialized consequences.

## References

1. N. Zhang, B. Liu, L. Zhang, *Halpern-Accelerated Majorized ADMM with Optimal Non-Ergodic Convergence under Degenerate Preconditioning*, arXiv:2609.38808v1 (first public 2026-09-30), https://arxiv.org/abs/2609.38808 . See §§2--4, especially Eqs. (2.15), (3.16), (4.3).
2. L. M. Briceño-Arias, P. L. Combettes, *A Monotone+Skew Splitting Model for Composite Monotone Inclusions in Duality*, arXiv:1011.5517v1 (2010), https://arxiv.org/abs/1011.5517 . See §§1--3 and the forward--backward--forward scheme.
