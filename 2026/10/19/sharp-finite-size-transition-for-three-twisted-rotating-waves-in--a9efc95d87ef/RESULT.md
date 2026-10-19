# Sharp finite-size transition for three-twisted rotating waves in a directed Kuramoto ring

## Finding
For integers \(m\ge1\) and \(N>m\), consider the directed, equal-strength, forward-neighbor phase dynamics
\[
\dot\theta_j=\sum_{r=1}^{m}\sin(\theta_{j+r}-\theta_j),\qquad j\in\mathbb Z/N\mathbb Z.
\]
Write \(c=(1+\sqrt{13})/6\), \(\kappa=2\pi/\arccos(c)=9.03118727914176\ldots\), and
\[
A=\frac{\pi\sqrt{1-c^2}(26c-7)}{12(4-11c)(1-c)}=-2.10535453861589\ldots.
\]
There is an integer \(m_0\) such that, for every \(m\ge m_0\), a unique real number \(R_m\in(9m,91m/10)\) divides the integer network sizes in this interval: the three-twisted relative equilibrium is locally orbitally exponentially attracting whenever the integer \(N>R_m\), and nonlinearly unstable whenever the integer \(N<R_m\). At equality no conclusion about nonlinear stability is asserted. Moreover,
\[
\boxed{R_m=\kappa\left(m+\tfrac12\right)+\frac{A}{m+1/2}+O(m^{-3}).}
\]
In particular, the finite-size shift is a *half-neighbor correction*, and the next coefficient is explicitly negative. The conclusion is uniform across all nonneutral Fourier modes: for sufficiently large \(m\), in the stated interval it is the first mode alone that changes stability. The root \(R_m\) is defined below by a real interpolation of an exact finite sum, and does not represent a fractional-vertex network.

## Assumptions and scope
The oscillator count \(N\) and out-degree \(m\) are integers, \(m\ge m_0\), and \(9m\le N\le91m/10\). A three-twisted relative equilibrium has \(\theta_j(t)=\Omega t+6\pi j/N\) with \(\Omega=\sum_{r=1}^{m}\sin(6\pi r/N)>0\) in this range. Stability is orbital, modulo the common-phase direction, with standard Euclidean local quotient coordinates. The interpolation variable \(n\in[9m,91m/10]\) in the proof is real; only integer \(n=N\) has a network interpretation. The asymptotics hold as \(m\to\infty\), and no effective numerical value of \(m_0\) is asserted.

## Proof
**1. Exact spectral reduction.** Linearization in the corotating frame is circulant. Its complex eigenvalue on Fourier mode \(\ell\) has real part \(-\Gamma_\ell(N,m)\), where
\[
\Gamma_\ell(N,m)=\sum_{r=1}^{m}\cos(6\pi r/N)[1-\cos(2\pi\ell r/N)],\quad1\le\ell<N.
\]
The imaginary eigenvalue parts affect neither the sign of exponential contraction nor hyperbolic instability. The zero mode corresponds to common phase. Thus strict positivity of every \(\Gamma_\ell\) gives orbital exponential attraction, while a negative mode gives nonlinear instability, by the spectral linearization criterion. This finite Fourier criterion is prior work of Sun–Wang–Dong; it is used, not claimed as new. Because \(6\pi m/N\le2\pi/3\), every sine in \(\Omega\) is strictly positive.

**2. The continuum first-mode root is algebraic-trigonometric.** Put \(u=2\pi m/N\), with \(u\in[20\pi/91,2\pi/9]\). For each fixed \(\ell\), uniformly over this interval,
\[
\frac{\Gamma_\ell(N,m)}m\longrightarrow H_\ell(u):=\int_0^1\cos(3us)(1-\cos(\ell us))\,ds
\]
when \(m\to\infty\) and \(2\pi m/N\to u\). Equivalently, \(H_\ell(u)=J_\ell(u)/u\), where
\[
J_\ell(u)=\int_0^u\cos(3v)(1-\cos(\ell v))\,dv.
\]
For \(\ell=1\), using triple- and quadruple-angle identities and writing \(z=\cos u\),
\[
J_1(u)=\frac{\sin u}{3}(1-z)(3z^2-z-1).
\]
On this interval \(z\in(0,1)\), and \(3z^2-z-1\) is strictly increasing in \(z\). Its unique zero is \(c=(1+\sqrt{13})/6\). Therefore the unique first-mode continuum crossing occurs at \(u_*=\arccos(c)\), or at reciprocal interaction ratio \(\kappa=2\pi/u_*\). The first mode is positive when \(N/m>\kappa\) and negative when \(N/m<\kappa\), asymptotically away from the crossing.

**3. The remaining infinitely many modes are uniformly positive.** For \(\ell\ge7\), the Fourier integral formula and \(u\in[20\pi/91,2\pi/9]\) imply
\[
H_\ell(u)\ge\frac{3\sqrt3}{4\pi}-\frac{\ell}{u(\ell^2-9)}
\ge\frac{3\sqrt3}{4\pi}-\frac{637}{800\pi}>0.
\]
Indeed \(\sin(3u)\ge\sqrt3/2\), and the terms with \(\ell\pm3\) are bounded in magnitude by their reciprocal frequencies. For modes \(2\le\ell\le6\), positivity follows from the following exact identities and elementary bounds. With \(z=\cos u\),
\[
J_2(u)=\frac{2\sin u}{15}(1-z^2)(12z^2-7)>0;
\]
\(z\ge\cos(2\pi/9)>\sqrt{7/12}\). The latter inequality follows because \(4z^3-3z=-1/2\) at \(z=\cos(2\pi/9)\), whereas \(4t^3-3t<-1/2\) for \(t=\sqrt{7/12}>3/4\), and the cubic is strictly increasing for \(t>1/2\). Also
\[
J_3(u)=\frac{\sin(3u)}3-\frac u2-\frac{\sin(6u)}{12}
\ge\frac{\sqrt3}{6}-\frac\pi9+\frac1{15}>0,
\]
where \(\sin(6u)\le-4/5\). Next,
\[
J_4(u)=\frac{\sin(3u)}3-\frac{\sin u}2-\frac{\sin(7u)}{14}
\ge\frac{\sqrt3}{6}-\frac13+\frac{\sqrt3}{28}>0,
\]
using \(\sin u<2/3\) and \(\sin(7u)\le-\sqrt3/2\). Furthermore,
\[
J_5(u)=\frac{\sin(3u)}3-\frac{\sin(2u)}4-\frac{\sin(8u)}{16}
\ge\frac{\sqrt3}{6}-\frac14>0,
\quad J_6(u)=\frac29\sin^3(3u)>0.
\]
All inequalities follow from the displayed short angle interval; for instance \(6u\in[120\pi/91,4\pi/3]\subset[13\pi/10,3\pi/2]\). Hence every fixed \(\ell\ge2\) has a strictly positive uniform continuum margin.

To make the result uniform over *finite-network* modes, write \(w_r=\cos(6\pi r/N)\). On the allowed interval, the weights decrease from at most \(1\) to at least \(-1/2\), so their total variation is at most \(3/2\). For \(1\le\ell\le N/2\), summation by parts and the geometric-series bound give
\[
\left|\sum_{r=1}^{m}w_r\cos(2\pi\ell r/N)\right|
\le\frac{|w_m|+\sum_{r<m}|w_{r+1}-w_r|}{\sin(\pi\ell/N)}
\le\frac2{\sin(\pi\ell/N)}\le\frac N\ell.
\]
For sufficiently large \(m\), uniformly in the ratio interval, \(m^{-1}\sum_{r=1}^mw_r>2/5\), by convergence to \(\sin(3u)/(3u)\ge3\sqrt3/(4\pi)>2/5\). When \(\ell\ge32\), the displayed weighted sum is at most \((91/10)/32<2/5\) times \(m\). Hence \(\Gamma_\ell>0\). Symmetry \(\Gamma_{N-\ell}=\Gamma_\ell\) handles \(\ell>N/2\). For \(2\le\ell\le31\), uniform Riemann-sum convergence and the established positive continuum margins give \(\Gamma_\ell>0\). This proves that, for sufficiently large \(m\), *only* \(\Gamma_1\) can change sign in the stated interval.

**4. Midpoint sum, unique finite-size crossing, and its two corrections.** For each fixed integer \(m\), extend the real first-mode factor to real \(n>m\):
\[
G_m(n)=\sum_{r=1}^m\cos(6\pi r/n)(1-\cos(2\pi r/n)).
\]
Let \(M=m+1/2\), \(t=M/n\), and \(F_m(t)=G_m(M/t)/(M/t)\). The exact geometric-sum identity is
\[
G_m(n)=\frac{\sin(6\pi t)}{2\sin(3\pi/n)}
-\frac{\sin(4\pi t)}{4\sin(2\pi/n)}
-\frac{\sin(8\pi t)}{4\sin(4\pi/n)}.
\]
The familiar expansion \(1/\sin v=v^{-1}+v/6+O(v^3)\), uniformly together with one derivative on compact subintervals, yields
\[
F_m(t)=J(t)+\frac{t^2}{M^2}E(t)+O(M^{-4}),
\]
where
\[
J(t)=\int_0^t\cos(6\pi s)(1-\cos(2\pi s))\,ds,
\quad E(t)=\pi\left[\frac{\sin(6\pi t)}4-\frac{\sin(4\pi t)}{12}-\frac{\sin(8\pi t)}6\right].
\]
Here \(t\) runs over the compact interval corresponding to \(9m\le n\le91m/10\), which shrinks to \([10/91,1/9]\). Throughout this interval \(J'(t)=\cos(6\pi t)(1-\cos(2\pi t))<0\); its magnitude is uniformly bounded away from zero. The \(C^1\)-uniform remainder therefore gives, for all sufficiently large \(m\), a *unique* zero \(t_m\) and hence a unique real zero \(R_m=M/t_m\), with positive \(G_m(n)\) precisely for \(n>R_m\). Set \(t_*=1/\kappa\). Taylor inversion gives
\[
t_m=t_*-\frac{t_*^2E(t_*)}{J'(t_*)M^2}+O(M^{-4}),\qquad
R_m=\kappa M+\frac{E(t_*)}{J'(t_*)M}+O(M^{-3}).
\]
At the root \(3c^2-c-1=0\), elementary trigonometric reduction yields
\[
E(t_*)=\frac{\pi\sqrt{1-c^2}(26c-7)}{108},\quad
J'(t_*)=\frac{(4-11c)(1-c)}9,
\]
which proves the stated exact coefficient \(A\). Combined with Step 3 and the already established spectral criterion, this proves all assertions.

## Verification
The standalone Python file `verify.py` checks the first-mode polynomial identity using exact rational arithmetic, numerically locates interpolated roots for several finite degrees, confirms the half-neighbor and next-order asymptotic formula within stated finite tolerances, and directly checks all physical Fourier modes at integer network sizes straddling the threshold. Run with `python3 verify.py`. These finite checks support arithmetic reproducibility but **do not prove** the all-degree or all-mode theorem, whose proof is Steps 1–4.

## Relationship to prior work
Sun, Wang and Dong (2026, arXiv:2608.29630v1) prove existence and general finite Fourier-mode orbital stability/instability criteria for directed dancing equilibria, sharp results for the first two twists, and only broader sufficient regions for higher twists. Those criteria and the general physical interpretation are prior; the present result determines the three-twist large-degree *all-mode* transition, an exact algebraic-trigonometric threshold, and two finite-size corrections. Bick, Böhle and Kuehn (2022/2023, arXiv:2206.01951v1) analyze symmetric ring twisted-state stability in the continuum and finite-size bifurcation simulations; the corresponding real linearized spectra coincide after appropriate normalization, so the continuum threshold is not claimed as newly discovered in principle. Their work does not state the centered finite-degree transition or its \(M^{-1}\) coefficient. Sinha and coauthors (2025, arXiv:2504.06377v1) give a general finite circulant spectral criterion and a specific third-twist discrepancy between finite and continuum predictions, but no all-large-degree threshold or expansion of the form above. The genuinely assessed advance is the sharp finite-degree asymptotic stability classification and its corrections, **not** the known DFT spectrum or the existence of twisted states.

## Limitations
The theorem is asymptotic in \(m\), requires \(9m\le N\le91m/10\), and does not give an effective minimum \(m_0\). It makes no nonlinear assertion if an integer \(N\) equals the real critical interpolation \(R_m\), or for other ratios or twists. The correction does not measure basin size, nonlinear rates at threshold, or disorder robustness. The similarity between real spectra of directed and symmetric rings means priority of equivalent asymptotic corrections needs independent checking; searches and source comparisons cannot prove absolute novelty.

## References
1. W. Sun, Y.-Q. Wang, and J.-G. Dong, *Existence and Stability of Dancing Equilibria in Asymmetric Kuramoto Networks*, arXiv:2608.29630v1, publicly posted 2026-08-30, especially Sections 3, 5 and Appendix B. https://arxiv.org/abs/2608.29630
2. C. Bick, T. Böhle, and C. Kuehn, *Phase Oscillator Networks with Nonlocal Higher-Order Interactions: Twisted States, Stability and Bifurcations*, arXiv:2206.01951v1 (2022); SIAM J. Appl. Dyn. Syst. 22 (2023), 1590–1638. https://arxiv.org/abs/2206.01951
3. Y. Sinha, P. B. Jain, A. Mihara, et al., *Geometric perspective of linear stability in finite networks of nonlinear oscillators*, arXiv:2504.06377v1 (2025); Phys. Rev. E 112 (2025), 054204. https://arxiv.org/abs/2504.06377
