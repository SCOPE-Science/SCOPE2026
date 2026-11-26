# Proliferation of linearly stable equilibria in the fractional sine–cubic map

## Finding

For the real commensurate Caputo-delta system with fractional right-hand side
\[
G_c(x,y)=\big(\sin(\pi y)-x,\,[c(1-x^2)-1]y\big),\qquad c>0,
\]
the stationary set consists of the origin for \(c<1\), the lattice \(\{(0,m):m\in\mathbb Z\}\) for \(c=1\), and the origin and four full sine branches for \(c>1\). For each fixed order \(0<\nu\le1\), the number of nonzero equilibria whose linearized dynamics is asymptotically stable satisfies
\[
N_\nu(c)=\frac{d_\nu}{\pi\sqrt{c-1}}+O_\nu(1)\qquad(c\downarrow1).
\]
The threshold \(d_\nu>1/4\) is the unique solution of
\[
\sqrt{d_\nu}=\left[2\cos\left(\frac{\arccos(-1/(2\sqrt{d_\nu}))-\pi}{2-\nu}\right)\right]^\nu,
\qquad d_1=1.
\]

## Assumptions and scope

The system is Eq. (10) of [1], with a common order, the shifted argument in the Caputo-delta equation, and real states on all of \(\mathbb R^2\). A stationary state is a constant sequence. Linear asymptotic stability here means that all solutions of the constant-coefficient variational equation tend to zero. At \(\nu=1\) the map is \((x,y)\mapsto(\sin(\pi y),c(1-x^2)y)\). No conclusion about nonlinear attraction is inferred from the linear count.

## Proof

**All branches.** The equilibrium equations are \(x=\sin(\pi y)\) and \([c(1-x^2)-1]y=0\). If \(y=0\), then \(x=0\); otherwise \(x^2=1-1/c\). This proves the cases \(c<1\) and \(c=1\). For \(c>1\), let \(h=\sqrt{c-1}\), \(r=h/\sqrt c\), and \(\theta=\arcsin(r)/\pi=\arctan(h)/\pi\). The four distinct families, indexed by \(k\in\mathbb Z\), are
\[
(r,2k+\theta),\quad(r,2k+1-\theta),\quad(-r,2k-\theta),\quad(-r,2k+1+\theta).
\]
The nonzero branches for \(c>1\) have Jacobian
\[
M=\begin{pmatrix}-1&\pi\cos(\pi y)\\-2cxy&0\end{pmatrix},\qquad
D=\det M=2\pi cxy\cos(\pi y),\qquad |D|=2\pi h|y|.
\]
Their characteristic polynomial is \(\lambda^2+\lambda+D\).

**Linear stability including the boundary.** The discrete fractional summation formula of [1, §2] for the shifted equation gives the recurrence
\[
u_n=u_0+\sum_{j=0}^{n-1}\frac{(\nu)_{n-1-j}}{(n-1-j)!}M u_j,\qquad n\ge1,
\]
where \((\nu)_m\) is the rising factorial, with \((\nu)_0=1\). Summing formally using \(\sum_{m\ge0}(\nu)_m z^m/m!=(1-z)^{-\nu}\) gives
\[
\sum_{n\ge0}u_n z^n=(1-z)^{\nu-1}\big[(1-z)^\nu I-zM\big]^{-1}u_0.
\]
Use the branch real and positive for real \(z<1\). For each nonzero eigenvalue \(\lambda\) the scalar denominator is \(f_\lambda(z)=(1-z)^\nu-\lambda z\). If no such denominator vanishes on \(|z|\le1\) and zero is not an eigenvalue, the inverse matrix is bounded on the closed disk. As \(\rho\uparrow1\), the boundary values at \(z=\rho e^{it}\) are dominated by a constant times \(|t|^{\nu-1}\) for \(0<|t|\le\pi\), since \(|1-\rho e^{it}|\) is bounded below by a positive multiple of \(|t|\) for \(\rho\ge1/2\). Thus the solution coefficients are Fourier coefficients of an integrable function, by radial passage in the coefficient integral, and tend to zero. This proof includes repeated eigenvalues and Jordan blocks.

A zero of \(f_\lambda\) in the open disk prevents decay on an eigendirection, since a sequence tending to zero has a power series analytic in that disk, while the scalar numerator does not vanish there. If the zero is at \(z_0\) on the unit circle, then \(z_0\ne1\) and it is simple: at a zero, \(f_\lambda'(z_0)=-(1-z_0)^{\nu-1}[1-(1-\nu)z_0]/z_0\ne0\). The boundary pole gives \(\lim_{\rho\uparrow1}(1-\rho)\sum_n u_n(\rho z_0)^n\ne0\) for nonzero scalar initial data. This limit would be zero if \(u_n\to0\), by bounding the finite initial part and the small tail separately. A complex eigendirection gives the same obstruction for real dynamics, since decay for every real datum implies decay for its complexification. A zero eigenvalue has a constant solution on its eigenspace.

For \(z=e^{it}\), \(0<t<2\pi\), the boundary curve \(\lambda=(1-z)^\nu/z\) has radius \([2\sin(t/2)]^\nu\) and argument \((\nu/2-1)t-\nu\pi/2\) modulo \(2\pi\). At absolute argument \(\phi>\nu\pi/2\) its one radial crossing is at
\[
R_\nu(\phi)=\left[2\cos\left(\frac{\phi-\pi}{2-\nu}\right)\right]^\nu.
\]
For small nonzero \(\lambda\) on such a ray, a root in the closed unit disk would have to be near \(z=1\), by \(|1-z|^\nu=|\lambda z|\le|\lambda|\). But there \(\arg \lambda=\nu\arg(1-z)-\arg z\) has absolute value at most \(\nu\pi/2+o(1)\), a contradiction. For sufficiently large \(|\lambda|\), Rouché's theorem on \(|z|=1/2\) gives a root of \(f_\lambda\) inside that circle. The number of interior roots is locally constant between boundary crossings: at each fixed nonzero \(\lambda\), the denominator tends to \(-\lambda\) uniformly near \(z=1\) and zeros cannot enter there, so the argument principle applies on interior contours approaching the circle. This proves decay precisely below the radial crossing on the rays in question. A positive real \(\lambda\) gives an interior real root by the opposite signs of \(f_\lambda(0)\) and \(f_\lambda(1)\).

**The determinant criterion and the count.** When \(D<0\) there is a positive real eigenvalue. When \(0<D\le1/4\), both eigenvalues are real in \((-1,0)\), inside the radius \(2^\nu\) on the negative axis. For \(D>1/4\), the pair has modulus \(\sqrt D\) and absolute argument \(\phi(D)=\arccos[-1/(2\sqrt D)]>\pi/2\). As \(D\) grows, \(\sqrt D\) increases from \(1/2\) to infinity, whereas \(R_\nu(\phi(D))\) decreases from \(2^\nu\) to a finite nonnegative limit (zero at \(\nu=1\)). There is exactly one crossing. For \(\nu=1\), the right side is \(1/\sqrt D\), hence \(d_1=1\). This gives stability exactly for \(0<D<d_\nu\); equality is excluded by the boundary argument. At \(c=1\) every lattice point has a zero eigenvalue, so none meets this linear decay condition.

For \(c>1\), checking the cosine signs on the four branches shows that positive \(y\) and \(D>0\) occur exactly at \(y=n+\theta\) for integers \(n\ge0\), once each. The reflection \((x,y)\mapsto(-x,-y)\) gives the corresponding negative half and preserves \(D\). The stable pairs thus have \(n+\theta<d_\nu/(2\pi h)\), giving
\[
N_\nu(c)=2\max\left\{0,\left\lceil\frac{d_\nu}{2\pi h}-\theta\right\rceil\right\}.
\]
The ceiling implements the strict boundary, including when its argument is an integer. The asserted asymptotic follows since \(0<\theta<1/2\).

## Verification

The count follows analytically from the exhaustive branch parametrization, the necessary and sufficient pole test on the relevant rays, and the strict integer count. Finite sample counts are not used to verify the limit.

## Relationship to prior work and limitations

The integer-order map is due to [2] and the fractional model is from [1]. In its fixed-point discussion, [1, §3.2] lists only the origin and the principal-arcsine pair, and gives the strict linear stability criterion in §2. General spectral stability criteria are prior work [3,4]; the argument above shows explicitly why the boundary is excluded for this variational equation. The contribution is the full-real-state branch and linear-stability census and its fixed-order asymptotic, not a new general stability theorem. The same census and determinant threshold also appear in the later catalogue entry [5], which additionally treats accumulation of the transition parameters. The accessible comparisons do not certify exhaustive priority, especially for order one. Nonlinear stability, basin size, and incommensurate orders are not addressed.

## References

1. X. Liu, D. Tang and L. Hong, *A Fractional-Order Sinusoidal Discrete Map*, Entropy 24 (2022), 320. https://doi.org/10.3390/e24030320
2. C. Bi, Q. Zhang, Y. Xiang and J.-M. Wang, *Bifurcation and attractor of two-dimensional sinusoidal discrete map*, Acta Phys. Sin. 62 (2013), 240503. https://doi.org/10.7498/aps.62.240503
3. J. Čermák, I. Győri and L. Nechvátal, *On explicit stability conditions for a linear fractional difference system*, Fract. Calc. Appl. Anal. 18 (2015), 651–672. https://doi.org/10.1515/fca-2015-0040
4. M. Busłowicz and A. Ruszewski, *Necessary and sufficient conditions for stability of fractional discrete-time linear state-space systems*, Bull. Pol. Acad. Sci. Tech. Sci. 61 (2013), 779–786. https://doi.org/10.2478/bpasts-2013-0084
5. *Fractional-memory stability staircase and inverse-square accumulation*, Resultary, 2026-11-22, record `83f0e50e0fe3`. [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-fractional-memory-stability-staircase-and-inverse-square-accumul--83f0e50e0fe3/RESULT.md)
