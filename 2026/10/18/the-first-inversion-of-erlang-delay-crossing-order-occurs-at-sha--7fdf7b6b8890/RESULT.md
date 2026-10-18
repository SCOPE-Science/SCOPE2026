# The first inversion of Erlang-delay crossing order occurs at shape 28

## Finding
For an integer Erlang shape \(m\ge1\), positive feedback constants \(a>b>0\), and mean delay \(\tau>0\), consider the characteristic equation
\[
\Delta_m(s,\tau)=s^2+a-b(1+\tau s/m)^{-m}=0.
\]
This is the type-two, positive-coupling center characteristic family in the distributed-delay theta-neuron model of Bîrdac–Fikl–Kaslik–Mureşan, specialized to a mean-preserving Erlang kernel. Define \(K_m=\lfloor(m-1)/2\rfloor\). The complete positive-imaginary crossing list is indexed by \(1\le k\le K_m\):
\[
\theta_k=\frac{k\pi}{m},\qquad
\omega_k=\sqrt{a-(-1)^k b\cos^m\theta_k},\qquad
\tau_k=\frac{m\tan\theta_k}{\omega_k}.
\]
Each crossing pair is simple and transverse, with direction \(\operatorname{sgn}\Re (ds/d\tau)=(-1)^{k+1}\) (odd \(k\) adds a right-half-plane pair, even \(k\) removes one). For **every** ratio \(0<b/a<1\) and every \(1\le m\le27\), the crossing times are strictly increasing in their phase index. **Shape 28 is the first possible inversion:** put
\[
\rho_* = \frac{\tan^2(3\pi/28)-\tan^2(2\pi/28)}{\tan^2(2\pi/28)\cos^{28}(3\pi/28)+\tan^2(3\pi/28)\cos^{28}(2\pi/28)}.
\]
Then \(0.9981109835968<\rho_*<0.9981109836566\); for \(m=28\), \(\tau_3<\tau_2\) precisely when \(b/a>\rho_*\), with simultaneous **distinct imaginary-frequency pairs** at equality. All other adjacent indices retain their natural order for \(m=28\). At \(a=4\) and \(b=999/250\) (so \(b/a=999/1000\)), the full chronological crossing order is \(1,3,2,4,5,\ldots,13\). In particular the counts of right-half-plane roots on the first five successive open delay intervals are \(0,2,4,2,0\). The result concerns linearized spectra; it does not infer nonlinear Hopf criticality at the double-frequency point.

## Assumptions and scope
Take \(m\in\mathbb N\), \(m\ge1\); \(a,b\in\mathbb R\) with \(a>b>0\); and \(\tau>0\). The delay distribution is Gamma/Erlang of integer shape \(m\) and rate \(m/\tau\), whose Laplace transform is \((1+\tau s/m)^{-m}\). The spectral problem is equivalent (at each positive delay) to the \((m+2)\)-dimensional linear-chain characteristic polynomial
\[
P_m(s,\tau)=(s^2+a)(1+\tau s/m)^m-b.
\]
In the cited neuron model one writes \(a=a_2\), \(b=b_2\) at a type-two center; choosing its real equilibrium \(u=0\), positive coupling \(\kappa=999/500\), and input \(\eta=1-3\kappa/2=-1997/1000\) gives \(a=4\), \(b=999/250\), \(a-b=1/250>0\). The pair \(s=\pm i\sqrt{a-b}\) is neutral at zero delay but its real parts are negative for sufficiently small positive delay. There are no positive-imaginary crossings for \(m=1,2\). Zero eigenvalues never occur because \(P_m(0,\tau)=a-b>0\).

## Proof
**Complete crossing formula.** At \(s=i\omega\), \(\omega>0\), put \(\theta=\arctan(\tau\omega/m)\in(0,\pi/2)\). Since the imaginary part of \((1+i\tau\omega/m)^{-m}\) must vanish, \(m\theta=k\pi\) for a unique integer \(1\le k<m/2\). The transform then equals \((-1)^k\cos^m(k\pi/m)\). The real part of \(\Delta_m=0\) gives the stated \(\omega_k\) and \(\tau_k\), which are positive because \(a>b>0\). Conversely each such pair solves the characteristic equation. No finite-delay crossing has \(m\theta=m\pi/2\), so the list is exhaustive.

**Simplicity and direction.** Set \(Q_k=(1+i\tan\theta_k)^{-m-1}=(-1)^k\cos^{m+1}\theta_k\,(\cos\theta_k-i\sin\theta_k)\). Implicit differentiation yields
\[
\frac{ds}{d\tau}=-\frac{b s Q_k}{2s+b\tau Q_k},\qquad
\Re\frac{ds}{d\tau} =\frac{-2b\omega_k^2(-1)^k\cos^{m+2}\theta_k}{|2i\omega_k+b\tau_k Q_k|^2}.
\]
The denominator is nonzero since its complex argument has real part \(b\tau_k(-1)^k\cos^{m+2}\theta_k\ne0\). Thus each pair is simple and crosses in the claimed direction. At \(\tau\downarrow0\), the two finite roots satisfy \(s_\pm=\pm i\sqrt{a-b}-b\tau/2+O(\tau^2)\); the other \(m\) roots in the linear-chain representation have real part tending to \(-\infty\). Therefore the unstable-root count starts at zero and changes by two according to the signed crossings (four at a double crossing if both directions add, but here the two signs are opposite).

**The order comparison.** Write \(r=b/a\), \(t_k=\tan(k\pi/m)\), and \(c_k=\cos(k\pi/m)\). The crossing times are \(m a^{-1/2} t_k(1-(-1)^k r c_k^m)^{-1/2}\). Every odd-to-even adjacent pair satisfies \(\tau_k<\tau_{k+1}\), because \(t_{k+1}>t_k\) and the odd denominator is greater than one whereas the even denominator is less than one. For an even-to-odd pair, squaring the positive expressions yields the exact equivalence
\[
\tau_k<\tau_{k+1}\quad\Longleftrightarrow\quad r<\rho_{m,k},\qquad
\rho_{m,k}=\frac{t_{k+1}^2-t_k^2}{t_k^2c_{k+1}^m+t_{k+1}^2c_k^m}.
\]
The only possible adjacent-order inversion therefore occurs at an even index \(k\). The assertion that shape 28 is minimal is an **exact finite inequality certificate**, not a sample of floating-point evaluations: the accompanying `interval_certificate.py` uses Machin's formula for \(\pi\), alternating rational Taylor bounds for the sine/cosine, and outward rational enclosures. It verifies \(\rho_{m,k}>1\) for **all 66** admissible even indices \(k\) and shapes \(3\le m\le27\) (minimum certified lower bound \(>1.0336337865\)), verifies \(\rho_{28,2}\in(0.9981109835968,0.9981109836566)\), and verifies \(\rho_{28,k}>1\) for every other even \(k\) at shape 28. Each bound follows from interval-monotonic arithmetic on positive quantities. A further exact interval test establishes the full order \(1,3,2,4,5,\ldots,13\) at \(m=28,r=999/1000\). By the crossing signs, the first open intervals have unstable-root counts \(0,2,4,2,0\). At \(r=\rho_*\) the distinct pairs indexed two and three cross simultaneously because their frequencies straddle \(\sqrt a\), even though their critical delays coincide.

## Verification
Run `python3 interval_certificate.py` using the standard library; it terminates with four PASS messages and exit status zero, including exhaustive, rational, outward interval checks for the 66 earlier even-index comparisons and the entire 28-stage example ordering. Run `python3 spectral_check.py` with NumPy to construct the \(30\times30\) linear-chain matrix and independently check unstable-root counts at delays \(1\), \(3\), \(4.474\), \(4.476\), \(4.479\), and \(6\). The rational interval certificate establishes the finite minimal-order inequalities; the spectral diagnostics alone do not prove the general theorem or a nonlinear bifurcation.

## Relationship to prior work
Bîrdac, Fikl, Kaslik and Mureşan (2026), Section 5, develop the type-two center scalar characteristic equation, a general phase criterion and the cases of weak Gamma (shape 1), strong Gamma (shape 2), and Dirac delays. Their Dirac case already has alternating crossing directions and certain stability switches. The new claim is **not** the general phase reduction, nor the observation of alternation: it is the sharp, finite **Erlang-shape 28** threshold for a reversal of **chronological** crossing order at fixed physical coefficients, plus the simultaneous distinct-pair boundary and the certified unstable-index chronology. The general phase criterion alone does not establish these global comparison inequalities. Zhang and Stépán (2019) treat multiple crossings for pure discrete-delay force control, not the exact Erlang-order threshold for this characteristic family. Broader distributed-delay spectral literature may contain equivalent consequences of general results.

## Limitations
The result establishes the complete imaginary-root list and signed spectral crossings of a linear-chain realization under \(a>b>0\); it does not establish the existence, criticality or stability of nonlinear periodic solutions. The integer 28 is minimal within this precisely stated **mean-preserving integer-shape Erlang family**, not for arbitrary distributed delay densities or arbitrary neuron equilibria. The proof's extensive exact finite certificate covers a bounded range because the minimal threshold claim only requires \(m\le28\); it is not a claim about all later shapes. The literature comparison remains non-exhaustive and is not a guarantee of priority.

## References
1. L. Bîrdac, A. Fikl, E. Kaslik and R. Mureşan, *Macroscopic Multistability and Bifurcations in Theta-Neuron Networks with Distributed Delays*, arXiv:2607.17645v1, publicly posted 2026-07-20, https://arxiv.org/abs/2607.17645 .
2. L. Zhang and G. Stépán, *Bifurcations in basic models of delayed force control*, Nonlinear Dynamics (2019), https://doi.org/10.1007/s11071-019-05058-7 .
