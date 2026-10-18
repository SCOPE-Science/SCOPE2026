# Sharp finite-volume Airy relaxation law for the sluggish random walk

## Finding

The position-dependent hopping model of Zodage–Allen–Evans–Majumdar [1], confined to the symmetric interval of integer sites \(\{-L,\ldots,L\}\) by rejecting jumps that would cross its endpoints, has a spectral gap \(\lambda_L\) obeying the **two-term asymptotic law**
\[
\boxed{\lambda_L=\frac{\mu}{L^3}-\frac{c}{L^4}+O(L^{-5})\quad(L\longrightarrow\infty).}
\]
Here \(\mu=3.47661900799224\ldots\) is the first Dirichlet–Neumann eigenvalue of
\[
-u''(x)=\mu x u(x),\qquad u(0)=0,\quad u'(1)=0,
\]
and the correction is the explicit positive constant
\[
\boxed{c=\mu\frac{\tfrac12u(1)^2+2\int_0^1u(x)^2\,dx}{\int_0^1xu(x)^2\,dx}
=14.9183562399750\ldots.}
\]
The ratio defining \(c\) is independent of eigenfunction normalization. The first nonconstant eigenfunction is **odd for every finite \(L\)**, and the stationary position \(K_L/L\) converges weakly to the density \(|x|\) on \([-1,1]\). Thus the box relaxation time scales as \(L^3/\mu\), with a determined nonvanishing finite-size correction of order \(L^2\). The asymptotics hold for positive integer \(L\) tending to infinity, not for arbitrary modifications of boundary rules.

## Assumptions and scope

At each integer time step, from \(k\in\{-L,\ldots,L\}\), propose a move to each of \(k+1\) and \(k-1\) with probability \(1/(|k|+2)\). A proposed move outside the interval is rejected, leaving the particle at its present site. The remaining probability is also a holding event. The Markov transition matrix is \(P_L\), and \(\lambda_L\) is the smallest positive eigenvalue of \(I-P_L\). An equivalent continuous-time Poissonization has generator \(P_L-I\) and exponential relaxation rate \(\lambda_L\). Only the displayed rule, the symmetric finite interval, and its stationary spectral gap are asserted here. The matching microscopic rate is one proposed update per unit time.

## Proof

**1. Detailed balance and parity.** Write \(w_k=|k|+2\). For each neighboring pair, \(w_kP_L(k,k+1)=w_{k+1}P_L(k+1,k)=1\). Hence the unique stationary measure is
\[
\pi_L(k)=\frac{|k|+2}{L^2+5L+2}.
\]
Reversibility gives the Dirichlet form
\[
\langle f,(I-P_L)f\rangle_{\pi_L}
=\frac1{L^2+5L+2}\sum_{k=-L}^{L-1}(f(k+1)-f(k))^2.
\]
Conjugating \(I-P_L\) by the square root of its positive stationary weights gives a real symmetric tridiagonal matrix with strictly negative off-diagonal entries. Such a Jacobi matrix has simple eigenvalues and a first excited eigenvector with exactly one nodal sign transition, by the discrete Sturm oscillation theorem. Since reflection commutes with this matrix, that simple eigenvector is either even or odd. An even vector cannot have exactly one nodal sign transition on a reflection-symmetric chain; therefore the eigenvector is odd. It vanishes at the origin, and its restriction to \(1,\ldots,L\) is positive up to an overall sign.

The Rayleigh characterization of the gap is consequently the **half-chain Dirichlet–Neumann quotient**
\[
\lambda_L=\min_{f_0=0,\ f\ne0}
\frac{\sum_{j=0}^{L-1}(f_{j+1}-f_j)^2}
{\sum_{j=1}^{L}(j+2)f_j^2}.
\]
There is no imposed derivative condition at the outer endpoint of this discrete minimization: rejected steps provide its natural reflecting boundary condition.

**2. Finite-element scaling.** Put \(h=L^{-1}\), \(x_j=jh\), and interpolate the \(f_j\) piecewise linearly to \(f_h\in V_h\), where \(V_h\subset H^1(0,1)\) consists of such functions vanishing at zero. Define
\[
a(f)=\int_0^1|f'|^2dx,\qquad
b_h(f)=h\sum_{j=1}^{L}(x_j+2h)f(x_j)^2.
\]
The previous quotient reads exactly \(L^3\lambda_L=\min_{f\in V_h\setminus\{0\}}a(f)/b_h(f)\). The composite trapezoidal rule on the mesh and the elementary trace/Poincaré bounds for functions satisfying \(f(0)=0\) give, **uniformly for every piecewise-linear \(f\)**,
\[
b_h(f)=b_0(f)+h b_1(f)+O(h^2 a(f)),
\]
with
\[
b_0(f)=\int_0^1xf(x)^2dx,\qquad
b_1(f)=\frac12f(1)^2+2\int_0^1f(x)^2dx.
\]
For clarity, the \(f(1)^2/2\) term comes from using right endpoints in the discrete stationary-mass sum; the second term comes from the microscopic \(+2\) in the waiting weights. The \(O(h^2)\) remainder follows cell by cell. For the piecewise-cubic function \(g(x)=xf(x)^2\), the interior second derivative on a cell with slope \(s=f'\) is \(g''=4fs+2xs^2\). Trapezoidal quadrature, summation, Cauchy–Schwarz and \(\|f\|_{L^2}\le C\|f'\|_{L^2}\) bound its global error by \(Ch^2a(f)\); its right-endpoint correction is \(hf(1)^2/2\). Likewise the error of the right-endpoint Riemann sum for \(f^2\) is at most \(Ch\|f\|_{L^2}\|f'\|_{L^2}\); multiplication by the microscopic factor \(2h\) makes it \(O(h^2a(f))\). These estimates are uniform in the entire discrete trial space.

**3. Continuum eigenproblem and first correction.** Let
\[
\nu(h)=\min_{\substack{f\in H^1(0,1),\ f(0)=0,\ f\ne0}}
\frac{a(f)}{b_0(f)+h b_1(f)}.
\]
At \(h=0\) this is the regular weighted Sturm–Liouville problem \(-u''=\mu xu\), \(u(0)=0\), \(u'(1)=0\), with a simple first eigenvalue \(\mu>0\). For sufficiently small \(h\ge0\), the minimizer solves
\[
-u_h''=\nu(h)(x+2h)u_h,\quad
\nu(h)\frac h2u_h(1)=u_h'(1),\quad u_h(0)=0.
\]
This smooth one-parameter problem has uniformly bounded eigenfunctions through two derivatives and a simple analytic eigenvalue. Differentiating its Rayleigh quotient at the simple minimum gives
\[
\nu(h)=\mu-\mu\frac{b_1(u)}{b_0(u)}h+O(h^2).
\]
The finite-element eigenvalue differs from \(\nu(h)\) by \(O(h^2)\). Indeed, if \(I_hu_h\) is nodal interpolation of the smooth continuum minimizer, its derivative and function errors are \(O(h)\) and \(O(h^2)\), respectively, in \(L^2\). The cross term in the energy expansion is \(a(u_h,I_hu_h-u_h)=\nu(h)[b_0+h b_1](u_h,I_hu_h-u_h)=O(h^2)\) by the eigenfunction weak equation, since the interpolation error vanishes at both boundary points. Hence the interpolant changes its continuum Rayleigh quotient by \(O(h^2)\), and the displayed mass-quadrature estimate gives the discrete upper bound. Conversely, the uniform denominator error \(Ch^2a(f)\) implies \(a(f)/b_h(f)\ge \nu(h)/(1+Ch^2\nu(h))\) for every discrete trial function, giving the matching lower bound. Thus
\[
L^3\lambda_L=\mu-\mu\frac{b_1(u)}{b_0(u)}L^{-1}+O(L^{-2}),
\]
which is exactly the claimed two-term law.

**4. Explicit Airy constant and stationary shape.** Let \(b=\mu^{1/3}\). The unique first-mode profile up to scale is
\[
u(x)=\operatorname{Ai}(-bx)-\frac1{\sqrt3}\operatorname{Bi}(-bx).
\]
The identity \(\operatorname{Ai}(0)/\operatorname{Bi}(0)=1/\sqrt3\) enforces \(u(0)=0\). The Neumann condition is
\[
\operatorname{Ai}'(-b)-\frac1{\sqrt3}\operatorname{Bi}'(-b)=0.
\]
Choose its smallest positive root \(b=1.51490605029665\ldots\); Sturm theory identifies it as the ground Dirichlet–Neumann mode. The positive integral formula above yields \(c\). Multiplying the Airy equation by \(xu'\) and integrating also yields the useful normalization-free identity \(u(1)^2=3\int_0^1xu^2dx\), independently confirming the boundary contribution. Finally, the exact reversible weights form a Riemann sum: for bounded continuous \(\varphi\),
\[
\sum_{k=-L}^L\pi_L(k)\varphi(k/L)\ \longrightarrow\
\int_{-1}^1|x|\varphi(x)dx.
\]
The proof is analytic for all chain lengths and does not extrapolate a finite numerical enumeration.

## Verification

Run `python verify.py` with Python 3, NumPy and SciPy. This program reconstructs the finite transition weights and both full and odd-sector Jacobi spectral problems; it verifies 2,953 exact-rational and numerical checks, including detailed balance for lengths \(1\) through \(30\), odd-first-mode parity, endpoint and Rayleigh identities, and a bounded second-order asymptotic residual at twelve larger sizes. It prints \(\mu\approx3.476619007992242\) and \(c\approx14.918356239975047\). Numerical evidence corroborates but does not replace Steps 1–4.

## Relationship to prior work

Zodage, Allen, Evans and Majumdar [1] define the infinite-line sluggish walk and prove its \(t^{1/3}\) spreading, survival and maximum scaling. Their exact generating-function analysis is not a reflecting-box relaxation-spectrum result. Grebenkov and Tupikina [2] supply a general heterogeneous-walk spectral propagator method and illustrate reflecting finite graphs, but the inspected analysis does not provide the Airy gap or its microscopic first correction for the waiting weights here. Del Vecchio and Majumdar [3] compute generalized arcsine statistics of the unconfined sluggish process; those trajectory observables do not yield the claimed reflecting-box eigenvalue asymptotics. The present claim concerns only the new finite-size gap constant and first correction, not the already-known \(t^{1/3}\) exponent or general finite-matrix spectral representations.

## Limitations

The boundary convention matters: a proposed outward step is rejected, not mirrored inward. The \(+2\) waiting weight determines part of the order-\(L^{-4}\) coefficient; changing it changes that coefficient. The result treats the finite symmetric interval and its first relaxation rate, not the full scaling distribution of the unbounded walk, general power-law trap exponents, or nonlinear disordered traps. The eigenvalue formula is a self-reviewed mathematical result; independent auditing and comprehensive priority certification have not been performed.

## References

1. A. Zodage, R. J. Allen, M. R. Evans, S. N. Majumdar, *A sluggish random walk with subdiffusive spread*, Journal of Statistical Mechanics (2023) 033211, arXiv:2301.13077, first posted January 30, 2023; DOI: 10.1088/1742-5468/acc4b1.
2. D. S. Grebenkov, L. Tupikina, *Heterogeneous continuous time random walks*, Physical Review E 97 (2018) 012148, arXiv:1712.01020; DOI: 10.1103/PhysRevE.97.012148.
3. G. Del Vecchio, S. N. Majumdar, *Generalized arcsine laws for a sluggish random walker with subdiffusive growth*, arXiv:2410.22097, first posted October 29, 2024.
