# Sharp two-periodic step-ratio stability threshold for scalar primal-dual hybrid gradient

## Finding
For the primal-first, unit-extrapolation primal-dual hybrid gradient (PDHG) iteration on the bilinear saddle \(\min_{x\in\mathbb R}\max_{y\in\mathbb R}xy\), let the positive steps alternate periodically between \((\tau,\sigma)=(t,r/t)\) and \((qt,r/(qt))\), where \(t>0\), \(q\ge1\), and \(0<r<1\). Every *individual* iteration matrix is Schur stable, with spectral radius \(\sqrt{1-r}\). Nevertheless the full periodic iteration need not converge.

Put \(U=q+q^{-1}\), \(U_*=4\sqrt5-6\), and
\[
q_*=\frac{U_*+\sqrt{U_*^2-4}}2=2.55249898195048\ldots.
\]
The two-step iteration converges to the unique saddle for every initial pair exactly when
\[
\boxed{F_U(r):=5r^2-(U+6)r+4>0.}
\]
It is marginal, with one two-step eigenvalue \(-1\), exactly when \(F_U(r)=0\); if \(F_U(r)<0\), some (indeed generically all) nonzero initial pairs grow exponentially in norm. In particular, for \(1\le q<q_*\) every product \(0<r<1\) is stable, while at \(q=q_*\) there is exactly one marginal product \(r=2/\sqrt5\). For \(q>q_*\), write
\[
r_\pm(U)=\frac{U+6\pm\sqrt{(U+6)^2-80}}{10}.
\]
When \(U_*<U<3\), both roots belong to \((0,1)\), and the unstable products are precisely \(r_-<r<r_+\). When \(U=3\), the unstable products are \(4/5<r<1\). When \(U>3\), they are \(r_-<r<1\). Endpoints inside \((0,1)\) are marginal; all other products are Schur stable. Interchanging alternating phases replaces \(q\) by \(q^{-1}\) and leaves the classification unchanged.

A rational witness has \(r=4/5\), \(q=3\), \(t=4/5\). Its two individual matrices have spectral radius \(1/\sqrt5\), yet the two-step characteristic polynomial evaluated at \(-1\) is \(-4/15<0\), so its two-step matrix has a real eigenvalue less than \(-1\).

## Assumptions and scope
The saddle function is precisely \(L(x,y)=xy\) on the unconstrained real line; its unique saddle is \((0,0)\). The primal-first PDHG update has extrapolation coefficient \(1\), exact arithmetic, and no adaptive feedback: the predetermined periodic steps satisfy \(\tau_k\sigma_k=r<1\) for every iteration. The update is
\[
x_{k+1}=x_k-\tau_k y_k,\qquad
y_{k+1}=y_k+\sigma_k(2x_{k+1}-x_k).
\]
The positive scale \(t\) is arbitrary; it does not affect spectral stability. The classification is for asymptotic convergence of the full alternating trajectory from every initial state. At a marginal parameter the method is not convergent for generic initial data, although a one-dimensional stable subspace remains. The classification is **not** a claim about a method with ratio-dependent extrapolation \(\theta_k=\tau_k/\tau_{k-1}\), about the original tuning-free feedback schedule, or about general nonlinear and higher-dimensional systems.

## Proof
For one step with \(r=\tau\sigma\), the state \(z_k=(x_k,y_k)^\mathsf T\) evolves as \(z_{k+1}=M(\tau,\sigma)z_k\), with
\[
M(\tau,\sigma)=\begin{pmatrix}1&-\tau\\\sigma&1-2r\end{pmatrix}.
\]
Its trace and determinant are \(2-2r\) and \(1-r\). Its characteristic discriminant is \(-4r(1-r)<0\), so its conjugate eigenvalues have modulus \(\sqrt{1-r}<1\) for \(0<r<1\). This holds for each periodic phase separately.

Let \(M_1=M(t,r/t)\), \(M_2=M(qt,r/(qt))\), and \(P=M_2M_1\). Exact multiplication yields
\[
\operatorname{tr}P=2-4r+4r^2-r(q+q^{-1}),\qquad \det P=(1-r)^2.
\]
A real quadratic \(\lambda^2-T\lambda+D\) has both roots strictly inside the unit disk precisely when \(1-D>0\), \(1-T+D>0\), and \(1+T+D>0\) (the degree-two Jury criterion). Here the first two expressions are
\[
1-\det P=r(2-r)>0,\quad
1-\operatorname{tr}P+\det P=r(U+2-3r)>0
\]
because \(U\ge2\), \(0<r<1\); the third is exactly \(F_U(r)\). This proves the stability criterion. Since \(\det P=(1-r)^2<1\), equality \(F_U(r)=0\) gives an eigenvalue \(-1\) and the other eigenvalue \(-(1-r)^2\), not equal to \(-1\). If \(F_U(r)<0\), the characteristic polynomial takes a negative value at \(-1\), but tends to positive infinity as \(\lambda\to-\infty\); thus it has one real eigenvalue below \(-1\). The other eigenvalue has modulus strictly less than \(1\). Unless the initial state lies in its one-dimensional stable eigenspace, the periodic orbit diverges geometrically. Conversely if the roots are Schur stable then \(P^m z_0\to0\), and the interleaved states \(M_1P^m z_0\to0\).

As a quadratic in \(r\),
\[
F_U(r)=5\left(r-\frac{U+6}{10}\right)^2+4-\frac{(U+6)^2}{20}.
\]
It has no real zeros if \(U<U_*:=4\sqrt5-6\); at equality it has the unique double zero \(r=(U_*+6)/10=2/\sqrt5\). Since \(q+q^{-1}\) is strictly increasing for \(q>1\), this determines the unique universal ratio threshold \(q_*\). If \(U>U_*\), its two real roots are \(r_\pm\) as stated. Both are positive, since the root sum and product are positive. The larger root crosses the admissible boundary \(r=1\) exactly when \(F_U(1)=3-U=0\). For \(U_*<U<3\), the vertex lies inside \((0,1)\) and \(F_U(1)>0\), so both roots lie in \((0,1)\). At \(U=3\) they are \(4/5\) and \(1\). For \(U>3\), one root remains in \((0,1)\), whereas the other exceeds \(1\). The positive leading coefficient determines each unstable interval. Finally, the product matrices \(M_1M_2\) and \(M_2M_1\) have identical characteristic polynomials; hence swapping phases or replacing \(q\) by its reciprocal does not affect the classification.

For the witness \(r=4/5\), \(q=3\), \(t=4/5\),
\[
M_1=\begin{pmatrix}1&-4/5\\1&-3/5\end{pmatrix},\quad
M_2=\begin{pmatrix}1&-12/5\\1/3&-3/5\end{pmatrix},\quad
P=\begin{pmatrix}-7/5&16/25\\-4/15&7/75\end{pmatrix}.
\]
Here \(\operatorname{tr}P=-98/75\), \(\det P=1/25\), and \(1+\operatorname{tr}P+\det P=-4/15\), completing the exact instability certificate.

## Verification
Execute `python verify.py` with Python 3 and SymPy installed. It performs 1,941 exact symbolic and rational comparisons, including derivations of the trace/determinant and Jury expressions, algebraic root relations, direct coordinate updates over a rational test grid, and the explicit period-two instability witness. This verification is supplementary: no finite grid establishes the infinite-parameter classification, which follows from the preceding algebraic proof.

## Relationship to prior work
Wang, Lan and Ye (2024) study nonstationary PDHG, allowing variable primal/dual steps whose product remains fixed; their generic algorithm specializes to the primal-first, unit-extrapolation form used here, though their convergence guarantee additionally uses a ratio-dependent extrapolation and summably varying steps. The present periodic schedule is **not** claimed to satisfy those sufficient conditions or to be an execution of their automatic stepsize-selection rule. Goldstein and collaborators (2013/2015) already explicitly observe that variable steps may fail even when every step-product meets the usual bound and require control of successive changes for their convergence theorem. The qualitative possibility of failure is therefore **prior art**, not the proposed new conclusion.

The narrower exact classification here supplies a universal sharp jump-ratio threshold, a closed stability/instability phase diagram over both step product and ratio, and a rational full-rank witness in which every phase is individually Schur stable. Existing constant-parameter scalar PDHG spectral classifications concern one fixed iteration matrix, not its noncommuting periodic products. Earlier nonstationary Douglas–Rachford convergence theorems with summable parameter changes address a different regime. These connections motivate the claim without establishing its exact threshold by implication.

## Limitations
The result is restricted to a single unconstrained real bilinear saddle mode, unit extrapolation, alternating reciprocal step pairs, and exact arithmetic. This is not a universal counterexample to the tuning-free adaptive scheme: its step-change assumptions are deliberately absent. Local phasewise stability is not a convergence theorem for arbitrary switching, and the classification addresses just two-periodic switching. The search did not exclude equivalent exact thresholds in unindexed older works on switched linear iterations or periodic numerical methods. No independent priority determination or external audit has been performed.

## References
1. Y. Wang, H. Lan, Y. Ye, *A Tuning-Free Primal-Dual Splitting Algorithm for Large-Scale Semidefinite Programming*, arXiv:2402.00311v1, first public 2024-02-01, https://arxiv.org/html/2402.00311v1 (especially Algorithm 1 and Theorem 2.1).
2. T. Goldstein, M. Li, X. Yuan, E. Esser, R. Baraniuk, *Adaptive Primal-Dual Hybrid Gradient Methods for Saddle-Point Problems*, arXiv:1305.0546v2, first public 2013-05-02, https://arxiv.org/html/1305.0546v2 (especially Sections II and VI).
3. D. A. Lorenz and Q. H. Tran-Dinh, *Non-stationary Douglas-Rachford and alternating direction method of multipliers: adaptive stepsizes and convergence*, arXiv:1801.03765, 2018, https://arxiv.org/abs/1801.03765.
4. Published scalar constant-step PDHG comparison: *Exact fixed-product rate phase diagram for scalar PDHG*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-fixed-product-rate-phase-diagram-for-scalar-pdhg--788191221208.
