# A chiral-to-synchronous instability switch in a lossy four-patch delayed population ring

## Finding

Consider the four-patch delayed logistic system, with indices read modulo four,
\[
\dot u_j(t)=d\bigl(u_{j-1}(t)-2u_j(t)\bigr)+u_j(t)\bigl(1-u_j(t-\tau)\bigr),\qquad j=1,2,3,4,
\]
where \(0<d<1\) and \(\tau\geq0\). Each patch exports to exactly one neighbor but loses an equal amount of dispersing population outside the system. The strictly positive homogeneous equilibrium is \(u_j=1-d=:p\).

Define
\[
T_{\mathrm{s}}(d)=\frac{\pi}{2(1-d)},\qquad
T_{\mathrm{c}}(d)=
\begin{cases}
\displaystyle\frac{\arccos\!\left(-\frac{d}{1-d}\right)}{d+\sqrt{(1-d)^2-d^2}},&0<d<1/2,\\
+\infty,&1/2\le d<1.
\end{cases}
\]
There is a **unique** \(d_*\in(0,1/2)\) satisfying \(T_{\mathrm{s}}(d_*)=T_{\mathrm{c}}(d_*)\). More exactly, let \(t_*\in(0,\pi/2)\) be the unique positive root of
\[
t+\frac{\pi}{2}=\frac{\pi}{2}(\sin t+\cos t),\qquad d_*=\frac{\sin t_*}{1+\sin t_*}.
\]
Numerically \(d_*\approx0.36767159106006936\), with a common first instability delay \(\tau_*\approx2.4841463780320483\). The exact first linear-instability threshold for every \(0<d<1\) is
\[
T(d)=\min\{T_{\mathrm{s}}(d),T_{\mathrm{c}}(d)\}.
\]
The equilibrium is linearly exponentially stable for \(0\le\tau<T(d)\) and linearly unstable for \(\tau>T(d)\). For \(0<d<d_*\), the first critical eigenspace is the rotating spatial Fourier mode \((1,i,-1,-i)\) and its conjugate; for \(d_*<d<1\), it is the synchronized Fourier mode \((1,1,1,1)\). At \(d=d_*\), the two distinct-frequency critical pairs occur simultaneously (a **linear double-Hopf point**); no nonlinear invariant torus or branch stability is asserted.

For context on minimal ring size: in the same unidirectional-loss model on a two- or three-patch directed cycle, the first small-positive-\(d\) instability is synchronized, whereas in the four-patch cycle it is rotating. Thus four patches is the smallest directed cycle with this **weak-dispersal** rotating-first effect.

## Assumptions and scope

There is one population species, four identical sites, intrinsic growth coefficient one, local delayed crowding coefficient one, one-way cyclic migration rate \(d\), and an additional mortality rate \(d\) during dispersal (diagonal dispersal coefficient \(-2d\) and a single off-diagonal coefficient \(d\) in each column). The delay occurs only in local density regulation, not in migration. The theorem concerns linear spectral stability of the positive equilibrium, not global attraction or nonlinear branch stability. Positive continuous initial histories generate nonnegative trajectories by quasi-positivity. All values and inequalities refer to the exact system above, with no hidden normalization.

## Proof

**1. Equilibrium and spectral reduction.** For a homogeneous state, the steady-state equation is \(0=-du+u(1-u)\); hence the positive equilibrium is \(p=1-d\) for \(0<d<1\). Write \(u_j=p+v_j\). The instantaneous derivative of the local reaction is \(1-p=d\), which cancels one of the two dispersal-loss terms. The exact linearization is therefore
\[
\dot v_j(t)=d\bigl(v_{j-1}(t)-v_j(t)\bigr)-p v_j(t-\tau).
\]
The cyclic shift has four eigenvalues \(1,i,-1,-i\). Corresponding scalar characteristic factors are
\[
F_0(\lambda)=\lambda+p e^{-\lambda\tau},\quad
F_\pm(\lambda)=\lambda+d\mp id+p e^{-\lambda\tau},\quad
F_2(\lambda)=\lambda+2d+p e^{-\lambda\tau}.
\]
At \(\tau=0\), all characteristic roots have negative real part, since the shift eigenvalues lie in the closed unit disk and \(p>0\).

**2. Imaginary-axis crossings.** For the general factor
\[
F(\lambda)=\lambda+a-ib+p e^{-\lambda\tau},\qquad a\geq0,
\]
a root \(\lambda=i\omega\) requires \(a=-p\cos(\omega\tau)\) and \(\omega=b+p\sin(\omega\tau)\). For \(a>p\) no imaginary root exists. The synchronized mode first crosses at \(\omega=p\), \(\tau=T_{\mathrm{s}}=\pi/(2p)\). For the real alternating mode \((a,b)=(2d,0)\), if a finite crossing is possible then its first delay is \(\arccos(-2d/p)/\sqrt{p^2-4d^2}>\pi/(2p)\); at equality \(a=p\) there is no finite imaginary-axis root because the only possible frequency is zero and \(F(0)>0\).

For the rotating mode \((a,b)=(d,d)\), if \(d<p\), set \(\nu=\sqrt{p^2-d^2}>0\) and \(\theta=\arccos(-d/p)\in(\pi/2,\pi)\). The positive-frequency first root is \(\omega=d+\nu\) at \(\tau=\theta/(d+\nu)=T_{\mathrm{c}}\). The other possible frequency \(d-\nu\), if nonzero, requires a strictly larger positive delay: when it is positive its least angle is \(2\pi-\theta\), and when negative the least absolute angle is \(\theta\) but its absolute frequency is smaller. The conjugate Fourier mode gives the complex conjugate characteristic root. If \(d>p\), neither rotating factor has imaginary roots. At \(d=p\), its isolated imaginary root occurs at \(\tau=\pi/d\), strictly later than \(T_{\mathrm{s}}\), so it does not alter the first-instability formula. These exhaust all four modes.

**3. Exact unique switch.** For \(0<d<1/2\), substitute \(q=d/p=\sin t\) with \(0<t<\pi/2\). Multiplying the comparison \(T_{\mathrm{c}}-T_{\mathrm{s}}\) by the positive quantity \(p(\sin t+\cos t)\) gives
\[
h(t):=t+\frac\pi2-\frac\pi2(\sin t+\cos t).
\]
Now \(h(0)=0\), \(h'(0)=1-\pi/2<0\), \(h''(t)=(\pi/2)(\sin t+\cos t)>0\), and \(h(\pi/2)=\pi/2>0\). Strict convexity proves that there is exactly one positive root \(t_*\), with \(h<0\) before it and \(h>0\) afterward. Since \(d=q/(1+q)\), the asserted sharp dispersal switch follows. At its crossing the synchronous frequency is \(p\), whereas the rotating frequency is \(p(\sin t_*+\cos t_*)>p\); the two pairs are distinct.

**4. Stability on either side.** At an imaginary root of \(F\), implicit differentiation gives
\[
\operatorname{Re}\frac{d\lambda}{d\tau}=
\frac{\omega(\omega-b)}{|1-p\tau e^{-i\omega\tau}|^2}.
\]
For the synchronized and alternating modes this is positive at each positive-frequency crossing. For the rotating first branch \(\omega=d+\nu\), it is positive. In the rotating-first region \(d<d_*\), one has \(d/p=\sin t_*<1/\sqrt 2\): indeed \(h(\pi/4)>0\), as follows from \(h(\pi/4)=3\pi/4-\pi/\sqrt2>0\). Hence \(d<\nu\), and the second rotating branch, when it crosses, also has positive crossing direction by the same formula. Thus no eigenvalue crosses back into the stable half-plane in the rotating-first regime. In the synchronized-first regime the synchronized factor already has a positive-real-part root after \(T_{\mathrm{s}}\), and each of its successive crossings is destabilizing. Standard continuity of roots for retarded characteristic equations, together with the initial stability at \(\tau=0\), proves stability below the stated threshold and instability above it. At \(d_*\), both first crossings are transverse in the delay direction; the codimension-two label is purely spectral.

**5. Two and three sites.** The two-cycle only has synchronized and real alternating spatial modes, so its first crossing is synchronized. For a three-cycle the nonconstant modes have cyclic phase \(2\pi/3\) and coefficients \((a,b)=(3d/2,\sqrt3d/2)\); expansion of their first crossing relative to the synchronized threshold, for \(d\downarrow0\), gives
\[
T_{\mathrm{nonconst}}-T_{\mathrm{s}}=
\left(\frac32-\frac{\pi\sqrt3}{4}\right)d+O(d^2)>0.
\]
For the four-cycle the analogous difference is \((1-\pi/2)d+O(d^2)<0\). Hence the minimality statement holds precisely for sufficiently small positive dispersal and not as an assertion about every dispersal rate in arbitrary larger rings.

## Verification

The accompanying standalone `verify.py` evaluates every Fourier characteristic factor, the exact linearization matrices, the critical-delay formulas, crossing-direction identities, and numerical brackets for the unique switch. It uses only Python's standard library. Its numerical results are reproducibility and algebraic diagnostics; the preceding analytic proof establishes the continuum of \(d\) values and all-delay assertions. The calculated threshold values are rounded, not presented as exact algebraic numbers.

## Relationship to prior work

Huang and Chen (2023) introduced delayed patch population equations with migration loss, established global equilibrium results at zero delay, and studied Hopf thresholds for small dispersal or near extinction. Their explicit network-topology asymptotics assume distinct local intrinsic growth rates; the exact intermediate-dispersal chiral/synchronous comparison on a homogeneous directed cycle is not stated in the inspected source. Liu, Shen, and Chen (2024) analyze a **one-way open-ended advective chain** with downstream loss, not a directed **closed cycle** with uniform per-patch loss, and find a different stabilizing comparison for their chain. Petit et al. (2015) place delay in diffusion on an undirected network; Petit et al. (2016) analyze two-component networks with delayed diffusion; neither directly covers the present one-species, instantaneous directed migration with delayed local crowding. The present result is an exact solvable specialization of general delay-network spectral methods, not a claim to invent modal decomposition, retarded root-continuity, or Hopf crossing theory.

## Limitations

The result is a linear spectral bifurcation classification; it does not prove existence, stability, amplitude, or global attraction of nonlinear traveling waves, synchronized oscillations, or quasiperiodic tori. The double-Hopf point denotes two distinct imaginary spectral pairs, not an independently calculated nonlinear normal form. Heterogeneous site growth, multidirectional migration, and delay in the dispersal flux are excluded. The literature comparison is best-knowledge and cannot certify worldwide priority against inaccessible or unindexed equivalent source results.

## References

1. D. Huang and S. Chen, *Dynamics of a delayed population patch model with the dispersion matrix incorporating population loss*, arXiv:2302.01814 (first submitted 2023-02-03), https://arxiv.org/abs/2302.01814 ; European Journal of Applied Mathematics 34 (2023), DOI:10.1017/S0956792523000049.
2. W. Liu, Z. Shen, and S. Chen, *Hopf bifurcations for a delayed discrete single population patch model in advective environments*, first online 2024, DOI:10.1017/S0956792524000342, https://doi.org/10.1017/S0956792524000342.
3. J. Petit, T. Carletti, M. Asllani, and D. Fanelli, *Delay induced Turing-like waves for one species reaction-diffusion model on a network*, arXiv:1507.00976, https://arxiv.org/abs/1507.00976.
4. J. Petit, M. Asllani, D. Fanelli, B. Lauwens, and T. Carletti, *Pattern formation in a two-component reaction-diffusion system with delayed processes on a network*, arXiv:1603.07122, https://arxiv.org/abs/1603.07122.
5. A. Otto, J. Wang, and G. Radons, *Delay-induced wave instabilities in single-species reaction-diffusion systems*, Physical Review E 96 (2017), DOI:10.1103/PhysRevE.96.052202.
