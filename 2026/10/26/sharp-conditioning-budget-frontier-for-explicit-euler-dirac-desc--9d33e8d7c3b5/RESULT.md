# Sharp conditioning-budget frontier for explicit Euler Dirac descent

## Finding

Fix a finite real chain complex of dimensions zero, one and two with boundary maps \(B_1\) and \(B_2\), \(B_1B_2=0\), and let \(s=\max\{\|B_1\|_2,\|B_2\|_2\}>0\). Let \(\gamma_0,\gamma_1,\nu>0\). Consider the isotropic quadratic Dirac descent equation \(\dot z=-(\nu I+D_\gamma)z\), with
\[
D_\gamma=\begin{pmatrix}0&\gamma_0B_1&0\\\gamma_1B_1^\top&0&\gamma_0B_2\\0&\gamma_1B_2^\top&0\end{pmatrix},
\]
and its forward Euler matrix \(E_h=I-h(\nu I+D_\gamma)\), for \(h>0\).

For the natural one-parameter degree weights \(P_r=\operatorname{diag}(rI_{N_0},I_{N_1},r^{-1}I_{N_2})\), \(r>0\), set
\[
p=s\sqrt{\gamma_0\gamma_1},\quad
C_r=\frac{s}{2}\left(\gamma_0\sqrt r+\frac{\gamma_1}{\sqrt r}\right),\quad
D_r=\frac{s}{2}\left|\gamma_0\sqrt r-\frac{\gamma_1}{\sqrt r}\right|.
\]
Then \(C_r^2-D_r^2=p^2\) and the **exact** induced one-step norm is
\[
\boxed{\|E_h\|_{P_r}=\sqrt{(1-\nu h)^2+h^2D_r^2}+hC_r.}\tag{1}
\]
Here \(\|x\|_{P_r}=\sqrt{x^\top P_rx}\) and the matrix norm is induced by this vector norm. Consequently, strict contraction for some positive step in this specific metric occurs **if and only if** \(\nu>C_r\), and the complete interval of contracting steps is
\[
\boxed{0<h<\frac{2(\nu-C_r)}{\nu^2-p^2}.}\tag{2}
\]
For \(\nu>C_r\), put \(Q_r=\nu^2+D_r^2\), \(H=\sqrt{\nu^2-p^2}\). The unique positive step minimizing the one-step norm and its exact optimum are
\[
\boxed{h_*(r)=\frac{\nu-C_rD_r/H}{Q_r},\qquad
\min_{h>0}\|E_h\|_{P_r}=\frac{\nu C_r+D_rH}{Q_r}.}\tag{3}
\]

**Conditioning-budget theorem.** Suppose that the degree weight must satisfy \(\kappa_2(P_r)\le K\), with any fixed real \(K\ge1\). Here all three chain spaces are assumed nonzero, so \(\kappa_2(P_r)=\max\{r,r^{-1}\}^2\). Among all such weights and every fixed \(h>0\), the unique optimal weight is
\[
\boxed{r_K=\operatorname{clip}\!\left(\frac{\gamma_1}{\gamma_0},K^{-1/2},K^{1/2}\right).}\tag{4}
\]
Let \(U=\max\{\gamma_0,\gamma_1\}\) and \(V=\min\{\gamma_0,\gamma_1\}\). The smallest possible coupling symmetrization constant under this budget is
\[
\boxed{C_K=\begin{cases}
\displaystyle\frac{s}{2}(UK^{-1/4}+VK^{1/4}),&1\le K\le(U/V)^2,\\[3pt]
p,&K\ge(U/V)^2.
\end{cases}}\tag{5}
\]
(The two pieces coincide at their shared endpoint.) There exist an admissible weight and a strictly contracting positive Euler step **if and only if** \(\nu>C_K\). When this holds, the jointly optimal pair is \(r=r_K\), \(h=h_*(r_K)\); its optimal one-step factor is given by (3).

In the spectrally stable but Euclidean-noncontracting regime \(p<\nu\le s(U+V)/2\), write
\[
\boxed{K_{\mathrm{crit}}=
\left[\frac{U}{\nu/s+\sqrt{(\nu/s)^2-UV}}\right]^4.}\tag{6}
\]
Then strict contraction in an admissible metric is possible exactly for budgets \(K>K_{\mathrm{crit}}\), not at equality. If \(\nu>s(U+V)/2\), it is already possible for \(K=1\). If \(\nu\le p\), no degree-weight budget can produce strict contraction.

Independently, the Euler scheme is asymptotically Schur stable (every state tends to zero) **if and only if**
\[
\boxed{\nu>p,\qquad 0<h<\frac{2}{\nu+p}.}\tag{7}
\]
For every contracting pair with \(\kappa_2(P_r)\le K\), the corresponding unweighted transient estimate is
\[
\|E_h^n\|_2\le \sqrt K\,\|E_h\|_{P_r}^{\,n}\qquad(n=0,1,2,\ldots).
\]
Thus the metric budget also bounds the Euclidean prefactor in a certified finite-iteration estimate.

## Assumptions and scope

All spaces are finite-dimensional real Euclidean spaces; \(N_0,N_1,N_2\ge1\). The boundary matrices may describe an oriented simplicial or cell complex (only \(B_1B_2=0\) is needed). The scalar state case suffices; tensoring each boundary matrix with an identity of any fixed component dimension leaves every formula unchanged. The objective is exactly isotropic quadratic with Hessian \(\nu I\). The coupling strengths are strictly positive, as is the Euler step. The optimization in (4) and (5) is over **only** the prescribed reciprocal degree-weight family \(P_r\), not all positive-definite matrices or all diagonal scalings. There is no claim about nonlinear, heterogeneous, asynchronous, or finite-precision methods.

## Proof

**Hodge-mode reduction.** The chain identity gives \(\operatorname{im}B_1^\top\perp\operatorname{im}B_2\) in the one-chain space. Choose orthonormal singular-vector pairs for every positive singular value of \(B_1\) and separately for \(B_2\); their one-chain singular vectors are mutually orthogonal. Complete them with orthonormal kernel vectors. The block similarity \(P_r^{1/2}E_hP_r^{-1/2}\) becomes an orthogonal direct sum of blocks
\[
T_{h,\sigma}=\begin{pmatrix}
1-\nu h&-h\sigma\gamma_0\sqrt r\\
-h\sigma\gamma_1/\sqrt r&1-\nu h
\end{pmatrix},\qquad 0<\sigma\le s,
\]
and one-dimensional blocks \(1-\nu h\) (the latter may be absent). A singular mode with \(\sigma=s\) exists by definition of \(s\).

**Exact singular-value calculation.** For a real matrix \(T=\bigl(\begin{smallmatrix}a&-b\\-c&a\end{smallmatrix}\bigr)\) with \(b,c\ge0\), let \(c_+=(b+c)/2\), \(c_-=|b-c|/2\). Its largest singular value is
\[
\|T\|_2=c_++\sqrt{a^2+c_-^2}.
\]
Indeed, \(\operatorname{tr}(T^\top T)=2(a^2+c_+^2+c_-^2)\) and \((c_++\sqrt{a^2+c_-^2})^2\) is its larger eigenvalue (the other is \((c_+-\sqrt{a^2+c_-^2})^2\)). This expression is nondecreasing in \(\sigma\), and is at least \(|a|\). Therefore the \(\sigma=s\) block attains the norm of the full matrix, proving (1).

**Sharp Euler contraction and optimal step.** Let \(f(h)=\sqrt{(1-\nu h)^2+D_r^2h^2}+C_rh\). Then \(f(0)=1\), and its right derivative at zero is \(C_r-\nu\). The square-root term is a strictly convex function of \(h\) whenever \(D_r>0\); when \(D_r=0\), the function \(|1-\nu h|+C_rh\) has a unique minimum at \(h=1/\nu\) if \(\nu>C_r\). If \(\nu\le C_r\), the derivative from zero is nonnegative, and convexity excludes any strict decrease below one. If \(\nu>C_r\), squaring \(f(h)<1\) is legitimate for \(0<h<1/C_r\) and yields
\[
h\bigl[(\nu^2+D_r^2-C_r^2)h-2(\nu-C_r)\bigr]<0.
\]
The resulting endpoint \(2(\nu-C_r)/(\nu^2-p^2)\) indeed satisfies \(h<1/C_r\), since \(2C_r(\nu-C_r)<\nu^2-p^2\), equivalent to \((\nu-C_r)^2+D_r^2>0\). This proves (2). Differentiating \(f\), solving \(f'(h)=0\) using \(Q_r-C_r^2=\nu^2-p^2=H^2\), and taking the branch \(h>0\), gives (3). If \(D_r>0\) strict convexity ensures uniqueness; the \(D_r=0\) case was handled directly.

**Budget optimization.** With \(p\) fixed, \(D_r^2=C_r^2-p^2\). For each \(h>0\), the right side of (1) strictly increases with \(C_r\). Minimizing \(C_r\) is therefore simultaneously optimal for every step and for the jointly optimized step. The function \(\gamma_0\sqrt r+\gamma_1/\sqrt r\) uniquely decreases up to \(r=\gamma_1/\gamma_0\) and uniquely increases afterward. Since \(\kappa_2(P_r)\le K\) is equivalent to \(K^{-1/2}\le r\le K^{1/2}\), this proves the clip formula (4), the piecewise expression (5), and the strict feasibility criterion. For \(p<\nu\le s(U+V)/2\), the strictly decreasing first branch of (5) crosses \(\nu\) at the unique \(K_{\mathrm{crit}}\) given by (6), by solving the quadratic in \(K^{1/4}\) and choosing the root before complete symmetrization. Strict inequality at the crossing gives the stated open budget frontier.

**Spectral comparison.** The same Hodge-mode argument without metric scaling shows that every nonzero singular mode of \(D_\gamma\) has the two real eigenvalues \(\pm\sigma\sqrt{\gamma_0\gamma_1}\); zero modes give eigenvalue zero. It follows that \(E_h\) has a real spectrum bounded by \(1-h(\nu\pm p)\), with both endpoints attained on the largest singular mode. Its spectral radius is less than one exactly under (7). Since these mode matrices are diagonalizable for positive couplings, this is also equivalent to convergence from every initial state. Finally, \(\|E_h^n\|_2\le\|P_r^{-1/2}\|_2\|P_r^{1/2}\|_2\|E_h\|_{P_r}^{\,n}=\sqrt{\kappa_2(P_r)}\|E_h\|_{P_r}^{\,n}\), as claimed.

## Verification

A concrete filled oriented triangle has
\[
B_1=\begin{pmatrix}-1&0&1\\1&-1&0\\0&1&-1\end{pmatrix},\quad
B_2=\begin{pmatrix}1\\1\\1\end{pmatrix},\qquad s=\sqrt3.
\]
With \(\gamma_0=4\), \(\gamma_1=1/4\), and \(\nu=2\), spectral stability holds for \(0<h<2/(2+\sqrt3)\), but \(C_1=17\sqrt3/8>2\), so **no** positive step is Euclidean-norm contracting. The smallest conditioning budget admitting a contractive degree metric is the *strict* threshold \(K>256/9\). At \(K=81\), the optimum is attained by \(r_K=1/9\), for which
\[
C_K=25\sqrt3/24,\quad D_K=7\sqrt3/24,\quad
h_*=209/817,\quad \|E_{h_*}\|_{P_{1/9}}=456\sqrt3/817<1.
\]
Thus a weight considerably better conditioned than the fully symmetrizing weight (whose condition number is \(256\)) already supplies a strict one-step guarantee.

The accompanying standalone checker (`verify.py`) constructs the actual seven-dimensional Euler matrix, independently evaluates its largest singular value for multiple budgets and steps, checks these exact constants, and tests the formulas on additional chain-complex examples. These finite checks support reproducibility; the assertions for all dimensions, budgets, and steps follow from the preceding proof rather than finite tests.

## Relationship to prior work

Rodríguez-Camargo, Urquijo-Rodríguez, and Mojica-Nava (2026), arXiv:2610.22628v1, introduce this directionally coupled Dirac gradient flow and prove the *continuous-time* geometric-mean stability criterion using its fully symmetrizing weight \(P_{\gamma_1/\gamma_0}\). They also explicitly contrast that weight with the more restrictive **continuous-time Euclidean** arithmetic-mean criterion. Those premises and the Hodge decomposition are credited to that work. Their stability section does not establish (1)–(6): the finite-step induced Euler norm, all positive contracting steps, optimal finite Euler step, or sharp budget-limited diagonal-metric frontier. Their numerical experiments use fourth-order Runge–Kutta time integration rather than the Euler guarantee studied here.

Carletti, Giambagli, Muolo, and Bianconi (2024), arXiv:2410.15338, analyze topological Dirac synchronization and singular-mode stability in continuous time. The present result addresses an isotropic quadratic, first-order discretization and a precise conditioning constraint absent from that dynamical treatment. General classical matrix-scaling and numerical ODE theory contain ingredients such as weighted norms and convex scaling; the present formulas should not be interpreted as inventing those ingredients. Instead, the assessed mathematical result is their exact, joint specialization to this Dirac Euler iteration, including the critical metric budget and optimally bounded transient prefactor.

## Limitations

Only the finite-dimensional isotropic quadratic and exact forward Euler schemes are analyzed. The metric-optimality statement is restricted to \(P_r=\operatorname{diag}(rI,I,r^{-1}I)\); arbitrary SPD metrics might attain different frontiers. The model allows trivial zero-coupling boundary maps but requires at least one nonzero incidence singular value. Schur stability is weaker than one-step norm contraction, and the theorem does not conflate them. The finite triangle example is an operator-stability witness, not a claim that every nonzero synchronization manifold exists on that simplicial complex. No independent audit, finite-precision roundoff guarantee, nonlinear guarantee, or asynchronous convergence assertion is supplied. Earlier general matrix-scaling literature might contain reformulations implying special portions of these calculations; that bibliographic uncertainty remains.

## References

1. C. D. Rodríguez-Camargo, A. F. Urquijo-Rodríguez, and E. Mojica-Nava, *Distributed Optimization over Simplicial Complexes via Topological Dirac Synchronization*, arXiv:2610.22628v1 (first posted October 15, 2026), https://arxiv.org/html/2610.22628v1 . Sections 2, 4.1–4.3, and 5.
2. T. Carletti, L. Giambagli, R. Muolo, and G. Bianconi, *Global Topological Dirac Synchronization*, arXiv:2410.15338 (2024), https://arxiv.org/abs/2410.15338 . Sections 4, 6–7.
3. R. D. Braatz and M. Morari, *Minimizing the Euclidean Condition Number*, SIAM Journal on Control and Optimization 32 (1994), 1763–1768, https://doi.org/10.1137/S0363012992238680 . Background on matrix scaling (not asserted to contain the Euler frontier).
