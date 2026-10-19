# Universal subcritical Hopf onset in a directed two-hop Kuramoto ring

## Finding
For every integer \(N\ge5\) and winding number \(q\) satisfying \(\pi/4<2\pi q/N<\pi/2\), consider the forward weighted two-hop phase system
\[
\dot\vartheta_j=\sin(\vartheta_{j+1}-\vartheta_j)+\rho\sin(\vartheta_{j+2}-\vartheta_j),\quad j\in\mathbb Z/N\mathbb Z,\quad \rho>0.
\]
Put \(\theta=2\pi q/N\), \(a=\cos\theta>0\), \(b=\cos(2\theta)<0\), and
\[
\rho_H=\frac{a}{4(-b)\cos^2(\pi/N)},\qquad
\omega_H=a\tan(\pi/N).
\]
The traveling \(q\)-twisted wave \(\vartheta_j(t)=j\theta+(\sin\theta+\rho\sin2\theta)t\) undergoes a **strictly subcritical Hopf bifurcation modulo common phase shift** at \(\rho=\rho_H\): on the side \(\rho<\rho_H\) sufficiently close to \(\rho_H\), an unstable nonconstant periodic orbit bifurcates in the phase-shift quotient, while the twisted wave remains locally orbitally exponentially stable. On the side \(\rho>\rho_H\), the twisted wave is nonlinearly orbitally unstable. The quotient periodic orbit lifts to a modulated relative-periodic wave in the original phase system; no global attractor assertion is made.

The critical cubic Hopf coefficient is strictly positive for **every** such pair \((N,q)\). With \(u=\cos(2\pi/N)\), Fourier eigenvector entries \(e^{2\pi i j/N}\), and cubic normal-form convention \(\dot z=(\sigma+i\omega)z+G_{21}z|z|^2/2+\cdots\), it is exactly
\[
\boxed{\operatorname{Re}G_{21}=\frac{2a(1-u)(1+2u)(1+u-2a^2)}{(1-2a^2)^2}>0.}
\]
For the six-site one-twist ring, \(\rho_H=1/3\), \(\omega_H=1/(2\sqrt3)\), and the full coefficient is \(G_{21}=4-3\sqrt3\,i\).

## Assumptions and scope
All phases are elements of \(\mathbb R/(2\pi\mathbb Z)\); the vector field is smooth and real analytic. The equivalence relation quotients simultaneous rotation of every phase by the same angle; equivalently one may use the \((N-1)\)-dimensional phase-difference torus. The strict sector assumption implies \(a>0\), \(b<0\), \(0<a^2<1/2\), and \(0<u<1\). The number \(q\) is an integer with \(1\le q<N/2\); there need not be such a \(q\) for every \(N\). The twisted motion has nonzero angular velocity because both \(\sin\theta\) and \(\sin2\theta\) are positive.

For the optional quantitative branch law define \(\rho_0=a/(4(-b))\), \(\delta=\rho/\rho_0-1\), and \(\delta_H=\tan^2(\pi/N)\). In a Hopf coordinate normalized by \(x_j=z e^{2\pi i j/N}+\overline z e^{-2\pi i j/N}+O(|z|^2)\), the quotient periodic orbit has squared leading amplitude
\[
\boxed{|z|^2=\frac{(1+u)(1-2a^2)^2}{2(1+2u)(1+u-2a^2)}(\delta_H-\delta)+o(\delta_H-\delta),\qquad \delta\uparrow\delta_H.}
\]
This concerns only a sufficiently small one-sided parameter interval for each fixed \((N,q)\); its size is not uniform in \(N\).

## Proof
**1. Spectrum and the isolated critical pair.** Let \(\phi=2\pi/N\) and write the perturbation in the co-rotating frame as \(x_j\). Its linear operator at the twisted wave is
\[
(Lx)_j=a(x_{j+1}-x_j)+\rho b(x_{j+2}-x_j).
\]
The Fourier vector \(v^{(k)}_j=e^{i k j\phi}\) has eigenvalue
\[
\lambda_k=a(e^{ik\phi}-1)+\rho b(e^{2ik\phi}-1).
\]
With \(s_k=\sin(\pi k/N)\) and the preceding \(\delta\), direct trigonometric algebra gives
\[
\operatorname{Re}\lambda_k=2a s_k^2[\delta-(1+\delta)s_k^2].
\]
The smallest nonzero \(s_k^2\) is \(\sin^2(\pi/N)\), attained precisely for \(k=1,N-1\). Consequently the unique first crossing is \(\delta_H=\tan^2(\pi/N)\), and all other nonzero quotient modes are strictly damped there. At the crossing, \(\rho_H b=-a/[2(1+u)]\), hence \(\lambda_1=i\omega_H\), \(\lambda_{N-1}=-i\omega_H\), with \(\omega_H=a\tan(\pi/N)>0\). The crossing is transverse, since
\[
\frac{d}{d\rho}\operatorname{Re}\lambda_1=8(-b)\sin^2(\pi/N)\cos^2(\pi/N)>0.
\]
The mode \(k=0\) is exactly the eliminated common-phase direction.

**2. The cubic coefficient.** Use the Fourier vectors of unit component magnitude, normalize the adjoint left vector by division by \(N\), and let \(D_r(k)=e^{irk\phi}-1\). The symmetric Taylor bilinear and trilinear maps, evaluated on Fourier inputs, have scalar coefficients
\[
B_{k,\ell}=-\sum_{r=1}^{2}w_r\sin(r\theta)D_r(k)D_r(\ell),\qquad
C_{k,\ell,m}=-\sum_{r=1}^{2}w_r\cos(r\theta)D_r(k)D_r(\ell)D_r(m),
\]
where \(w_1=1\) and \(w_2=\rho_H\). At the Hopf point the standard cubic normal-form expression simplifies to
\[
G_{21}=C_{1,1,-1}+\frac{B_{-1,2}B_{1,1}}{2i\omega_H-\lambda_2}.
\]
The otherwise possible zero-mode correction is absent: \(B_{1,-1}\) lies in the constant-vector direction, which is removed by quotienting, and \(B(v,\mathbf1)=0\) for every \(v\) because all couplings depend only on phase differences.

For an explicit algebraic check set \(z=e^{i\phi}\), \(c=a^2\), \(u=(z+z^{-1})/2\). The critical identities are
\[
\frac{\rho_H\sin2\theta}{\sin\theta}=\frac{c}{(1+u)(1-2c)},\qquad
\frac{\rho_H\cos2\theta}{a}=-\frac1{2(1+u)}.
\]
Inserting these into the displayed bilinear/trilinear coefficients and canceling the rational functions yields
\[
\frac{G_{21}}a=-\frac{(z-1)\big[-4c^2z^2+2c^2z+2c^2+cz^3+2cz^2-2cz-3c+z+1\big]}{cz(2c-1)^2}.
\]
Taking the half-sum under \(z\mapsto z^{-1}\), using \(z+z^{-1}=2u\), gives
\[
\operatorname{Re}G_{21}=\frac{2a(1-u)(1+2u)(1+u-2c)}{(1-2c)^2}.
\]
Every factor is strictly positive: \(a>0\), \(0<u<1\), and \(c<1/2\). Thus the first Lyapunov coefficient has the strictly positive sign independently of dimension and winding within the stated sector.

**3. Bifurcation direction and amplitude.** On the phase-difference torus the Hopf pair is simple, all other eigenvalues have strictly negative real part, and the crossing speed and cubic coefficient are nonzero. The finite-dimensional Hopf theorem therefore supplies one small quotient periodic-orbit branch on the stable side of the equilibrium, \(\rho<\rho_H\). Its radial normal form is
\[
\dot r=\sigma(\delta)r+\frac12\operatorname{Re}G_{21}\,r^3+O(r^5+|\delta-\delta_H|r^3),
\]
where \(\sigma(\delta)=2a\sin^2(\pi/N)\cos^2(\pi/N)(\delta-\delta_H)\). The positive cubic coefficient makes the bifurcating cycle radially unstable and the equilibrium exponentially stable below threshold. Above threshold, the equilibrium possesses a positive-real-part pair and is orbitally unstable. Solving the leading radial equation and substituting the exact coefficient gives the stated squared-amplitude law. The same normal form proves no claim about dynamics far from the threshold.

## Verification
The standalone \(verify.py\) script checks the exact rational-function identity for the cubic coefficient with symbolic arithmetic, the exact value \(G_{21}=4-3\sqrt3 i\) on the six-node ring, Fourier eigenvalues and positive cubic coefficient for 612 admissible \((N,q)\) samples with \(5\le N\le100\), and three independent finite-time nonlinear drift diagnostics. Run with \(python verify.py\), with SymPy, NumPy and SciPy installed. These computations support, but do not replace, the analytic proof for arbitrary \(N,q\).

## Relationship to prior work
Sun, Wang and Dong [1] introduce and analyze asymmetric Kuramoto dancing equilibria; their explicit forward-neighbor Fourier classifications assume **equal** neighbor weights and do not compute the first Lyapunov coefficient at a weighted two-hop Hopf crossing. Sinha and collaborators [2] give a more general circulant **linear** stability formula that already implies the location of the crossing once the present weights are substituted. That prior formula does **not** determine the cubic Hopf sign or establish the subcritical relative-periodic branch: this nonlinear assertion, not the standalone Fourier spectrum, is the main finding. Bick, Böhle and Kuehn [3] study twisted states in nonlocal pairwise and higher-order coupling in a continuum/symmetric framework, not the present finite directed weighted-ring Hopf coefficient. Bick, Böhle and Omel'chenko [4] study Hopf bifurcations with nonpairwise higher-order interactions, rather than the purely sinusoidal pairwise directed model here.

## Limitations
The existence/instability assertions are local near \(\rho_H\); neither a global basin boundary nor a global attractor is established. The original phase system's lifted waves are relative-periodic rather than necessarily closed periodic trajectories in the unreduced torus. The formula does not address sector endpoints \(\theta=\pi/4,\pi/2\), other winding sectors, or negative coupling weights. An apparently relevant 2026 comparison [5] could not be inspected beyond bibliographic/abstract material; equivalent earlier nonlinear results remain a priority risk requiring independent literature review.

## References
[1] W. Sun, Y.-Q. Wang and J.-G. Dong, *Existence and Stability of Dancing Equilibria in Asymmetric Kuramoto Networks*, arXiv:2608.29630v1 (first posted 2026-08-30), https://arxiv.org/abs/2608.29630.

[2] Y. Sinha et al., *Geometric perspective of linear stability in finite networks of nonlinear oscillators*, arXiv:2504.06377v1 (2025), https://arxiv.org/abs/2504.06377.

[3] C. Bick, T. Böhle and C. Kuehn, *Phase Oscillator Networks with Nonlocal Higher-Order Interactions: Twisted States, Stability, and Bifurcations*, SIAM J. Appl. Dyn. Syst. (2023), https://doi.org/10.1137/22M1500940; arXiv:2206.01951.

[4] C. Bick, T. Böhle and O. E. Omel'chenko, *Hopf bifurcations of twisted states in phase oscillator rings with nonpairwise higher-order interactions*, J. Phys.: Complexity (2024), arXiv:2310.15698.

[5] *Twisted States in Coupled Phase Oscillator Systems with Different Coupling Weight Schemes*, Chinese J. Phys. (2026), PII S0577907326003461; https://www.sciencedirect.com/science/article/abs/pii/S0577907326003461 (full text not inspected).
