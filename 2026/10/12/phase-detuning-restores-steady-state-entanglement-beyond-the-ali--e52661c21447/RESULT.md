# Phase detuning restores steady-state entanglement beyond the aligned-squeezing ceiling

## Finding

Consider two resonant linearly coupled bosonic oscillators in the phase-locked (co-rotating) squeezed-thermal-reservoir model below. Both local baths have the same damping rate, thermal occupancy and squeezing magnitude, but their squeezing phases may differ. The following formulas describe the unique Gaussian stationary state and its partial-transpose spectrum **for every relative phase**, rather than only the aligned-phase specialization.

Put
\[
 y=2\bar n+1,\quad S=\sinh(2r),\quad
 \mu=\frac{\gamma^2}{\gamma^2+4J^2},\quad
 \chi=\frac{2\gamma J}{\gamma^2+4J^2},\quad
 z=S|\cos(\phi_1-\phi_2)|.
\]
The smallest partially transposed symplectic eigenvalue and logarithmic negativity are exactly
\[
 2\widetilde\nu_-=yR(z),\qquad
 R(z)=\sqrt{1+(1-\mu^2)z^2}-\chi z,\qquad
 E_N=\max\{0,-\log_2[yR(z)]\}.
\]
In particular, let
\[
 z_*=\sqrt{\frac{\mu}{1-\mu^2}},\qquad
 r_*=\frac12\operatorname{arsinh}(z_*).
\]
Optimization over **all** relative phases at each fixed squeezing magnitude has the sharp law
\[
 \min_{\phi_1-\phi_2}R(S|\cos(\phi_1-\phi_2)|)
 =\begin{cases}
 \sqrt{1+(1-\mu^2)S^2}-\chi S,&S\le z_*,\\
 (1+\mu)^{-1/2},&S\ge z_*.
 \end{cases}
\]
When \(S>z_*\), the maximizing phases satisfy precisely
\[|\cos(\phi_1-\phi_2)|=z_*/S.\]
For \(0<S<z_*\), the maximizing phases are exactly aligned modulo \(\pi\); for \(S=0\), every phase is equivalent. Thus **arbitrarily large squeezing retains the same strictly positive optimum** if and only if \(1\le y<\sqrt{1+\mu}\), in which case
\[
 E_{N,\mathrm{opt}}=\log_2\left(\frac{\sqrt{1+\mu}}{y}\right)>0
 \qquad (r\ge r_*).
\]
For \(y\ge\sqrt{1+\mu}\) no choice of squeezing magnitude or relative phase gives positive logarithmic negativity.

There is a sharp finite high-squeezing phase window. If \(1\le y<\sqrt{1+\mu}\) and \(b=1/y\), define
\[
 z_\pm=\frac{b\chi\pm\sqrt{(1-\mu)[b^2(1+\mu)-1]}}{1-\mu}.
\]
Then \(E_N>0\) if and only if \(z_-<S|\cos(\phi_1-\phi_2)|<z_+\). For \(S>z_+\), each entangled interval adjacent to a zero of the cosine has angular width
\[
 \arccos(z_-/S)-\arccos(z_+/S)
 =\frac{z_+-z_-}{S}+O(S^{-3})
 =\Theta(e^{-2r}).
\]
Phase detuning therefore removes the fixed-alignment high-squeezing entanglement ceiling, but the required relative-phase precision shrinks exponentially.

## Assumptions and scope

The two bosonic modes have canonical commutators and a resonant rotating-frame Hamiltonian
\[H=J(a_1^\dagger a_2+a_2^\dagger a_1),\qquad J>0.\]
Each mode couples to its *own independent*, stationary, phase-locked, Markovian squeezed thermal reservoir, with the same rate \(\gamma>0\), thermal mean \(\bar n\ge0\), and squeezing \(r\ge0\), and with possibly distinct phases \(\phi_1,\phi_2\). The local Lindblad generator is
\[
 \gamma(N+1)\mathcal D[a_j]+\gamma N\mathcal D[a_j^\dagger]
 -\gamma M_j\mathcal S[a_j]-\gamma M_j^*\mathcal S[a_j^\dagger],
\]
where \(\mathcal D[L]\rho=L\rho L^\dagger-\{L^\dagger L,\rho\}/2\), \(\mathcal S[L]\rho=L\rho L-\{L^2,\rho\}/2\), and
\[
 N=\bar n\cosh(2r)+\sinh^2r,\qquad
 M_j=-\frac{2\bar n+1}{2}\sinh(2r)e^{2i\phi_j}.
\]
The covariance convention is \([x_j,p_k]=i\delta_{jk}\), vacuum covariance \(I/2\); the logarithmic negativity uses partial transposition on mode 2. All asserted extrema concern optimization **only over the relative squeezing phases**, keeping \(J,\gamma,\bar n,r\) fixed. The thermal threshold is a condition on the bath occupancy, not on an experimentally calibrated absolute temperature.

## Proof

**Stationary second moments.** Set \(K=\cosh(2r)\). The normal moment matrix is \(\langle a_j^\dagger a_k\rangle=N\delta_{jk}\): it solves the stationary number-moment Lyapunov equation, uniquely because the homogeneous drift has real part \(-\gamma/2\). The symmetric anomalous matrix \(B_{jk}=\langle a_ja_k\rangle\) solves
\[
 0=-\gamma B-iJ(\sigma_xB+B\sigma_x)
   +\gamma\operatorname{diag}(M_1,M_2).
\]
Write \(q=(M_1+M_2)/2\), \(d=(M_1-M_2)/2\). Direct substitution gives its unique solution
\[
 B=\begin{pmatrix}\mu q+d&-i\chi q\\-i\chi q&\mu q-d\end{pmatrix}.
\]
A common local phase rotation does not alter any symplectic eigenvalue. After removing the average squeezing phase and a common sign, take \(q=h c\), \(d=ihs\) with \(h=yS/2\), \(c=\cos(\phi_1-\phi_2)\), \(s=\sin(\phi_1-\phi_2)\); put \(a=yK/2\). The covariance matrix in quadrature order \((x_1,p_1,x_2,p_2)\) becomes
\[
 V=\begin{pmatrix}
 a+h\mu c&hs&0&-h\chi c\\
 hs&a-h\mu c&-h\chi c&0\\
 0&-h\chi c&a+h\mu c&-hs\\
 -h\chi c&0&-hs&a-h\mu c
 \end{pmatrix}.
\]
**Partial-transpose eigenvalue.** Let \(A_1,A_2,C\) be the two local and one intermode covariance blocks. With
\[u=a^2-h^2(\mu^2c^2+s^2),\qquad w=h\chi|c|,\]
direct determinant calculation yields
\[
 \det A_1=\det A_2=u,\qquad \det C=-w^2,\qquad
 \det V=(u-w^2)^2.
\]
Since \(\mu^2+\chi^2=\mu\) and \(K^2-S^2=1\), one has \(u\ge w^2\), so the Gaussian partial-transpose invariant \(\widetilde\Delta=\det A_1+\det A_2-2\det C=2(u+w^2)\) gives
\[
 \widetilde\nu_-^2=
 \frac{\widetilde\Delta-\sqrt{\widetilde\Delta^2-4\det V}}2
 =(\sqrt u-w)^2.
\]
Taking the nonnegative square root, using \(c^2+s^2=1\), and substituting \(a,h\) proves the asserted \(R(z)\). This is an exact infinite-dimensional Gaussian-state result, not an inference from finite Fock truncation.

**Sharp phase optimum.** Put \(A=1-\mu^2>0\). The derivative of \(R(z)=\sqrt{1+Az^2}-\chi z\) is \(Az/\sqrt{1+Az^2}-\chi\), and
\[R''(z)=\frac A{(1+Az^2)^{3/2}}>0.\]
As \(\chi^2=\mu(1-\mu)\), its unique minimizer on \([0,\infty)\) is \(z_*=\sqrt{\mu/(1-\mu^2)}\) and its minimum is \(1/\sqrt{1+\mu}\). Since every \(z\in[0,S]\) is reachable by a relative phase, constraining this minimizer to \([0,S]\) proves both branches, the equality conditions, the thermal cutoff, and the positive high-squeezing plateau.

**Strict entanglement window.** Write \(b=1/y\). Since \(b+\chi z>0\), \(R(z)<b\) is equivalent (without extraneous squaring solutions) to
\[
 (1-\mu)z^2-2b\chi z+(1-b^2)<0.
\]
For \(1\le y<\sqrt{1+\mu}\), its discriminant is positive and its two roots are \(z_-\) and \(z_+\) above; \(z_-\ge0\) and \(z_+>z_-\). For \(y\ge\sqrt{1+\mu}\) the global minimum already forbids strict NPT. For \(S>z_+\), \(z_-<S|\cos\delta|<z_+\) corresponds to intervals near \(\delta=\pi/2\pmod\pi\) with the stated arccosine width. The Taylor series of arccosine at zero yields \((z_+-z_-)/S+O(S^{-3})\), and \(S\sim e^{2r}/2\).

**Concrete high-squeezing recovery.** Set \(2J/\gamma=1\), \(\bar n=0\), and \(S=2\). Then \(\mu=\chi=1/2\); at aligned phase \(R(2)=1\), hence zero logarithmic negativity. At \(|\cos\delta|=1/\sqrt6\), however, \(z=z_*=\sqrt{2/3}\) and \(E_N=\log_2\sqrt{3/2}>0\). Thus the departure from the fixed-phase ceiling is a genuine, explicitly attainable physical distinction.

## Verification

The standalone `check_symbolic.py` checks the exact covariance determinant factors, critical stationarity identity, optimal value, and threshold discriminant using symbolic algebra. The standalone `verify.py` computes the stationary covariance **directly** from the real four-dimensional Lyapunov equation and obtains \(\widetilde\nu_-\) from the eigenvalues of \(i\Omega V^{\Gamma}\). It compares those numerical results against the theorem's expression in 1,500 reproducible random parameter configurations, with additional fixed-coupling phase sweeps. It does not substitute a truncated Hilbert-space calculation for the analytic Gaussian proof. Execute `python check_symbolic.py` and `python verify.py` after installing the dependencies in `requirements.txt`; successful outputs start with `SYMBOLIC_OK` and `VERIFY_OK`. Symbolic determinant identities and the scalar convexity/root arguments above supply the infinite-parameter proof; finite numerical tests are checks rather than proof of those universal statements.

## Relationship to prior work

Ayoub, Castillo-Gonzalez and Bittner (2026, arXiv:2605.03978v1) formulate exactly the independently squeezed, phase-locked two-mode Lindblad model, derive the Gaussian covariance technique, and report the **aligned-phase** expression \(\widetilde\nu_-=(y/2)[\sqrt{K^2-\mu^2S^2}-\chi S]\), together with qualitative phase landscapes and fixed-phase finite-squeezing entanglement domes. Their equations (2), (5)–(6), and (12)–(17) are antecedents, not new claims here. Setting \(|\cos\delta|=1\) in the formula proved above reproduces their expression exactly. The present theorem instead gives the arbitrary-relative-phase closed form, its complete phase optimization, the disappearance of the aligned-phase high-squeezing bound under active phase control, the exact thermal feasibility boundary, and the exponentially narrowing angular survival windows. Those results are not statements or direct inequalities supplied by the cited aligned-phase formula alone.

Bittner (2025, arXiv:2511.19662v1) analyzes a related two-mode squeezed-bath system from the perspectives of entropy flow and exceptional-point structure. It supplies overlapping bath definitions, but not the optimized partial-transpose eigenvalue or phase-window classification. The present use of standard Gaussian partial-transpose invariants is credited as a pre-existing method, not asserted to be new.

## Limitations

The classification is exact for the stated symmetric, resonant, independent, Markovian, phase-locked Gaussian model. It does **not** address unequal losses, unequal squeezing magnitudes, detuning, shared reservoirs, laboratory-fixed squeezing phases with Floquet evolution, non-Gaussian states, or noise in the phase-control actuator. High-squeezing recovery requires phase precision of order \(e^{-2r}\); the positive optimal plateau does not imply robustness to phase errors. The source papers and comparable unindexed literature might already imply a related optimization by another formulation; no absolute priority is claimed.

## References

1. A. Ayoub, A. Castillo-Gonzalez and E. R. Bittner, *Phase-Reference Control of Steady-State Entanglement in Open Quantum Systems*, arXiv:2605.03978v1 (first public version 2026-05-05), https://arxiv.org/abs/2605.03978.
2. E. R. Bittner, *Entropy Flow and Exceptional-Point Structure in Two-Mode Squeezed-Bath Dynamics*, arXiv:2511.19662v1 (2025-11-24), https://arxiv.org/abs/2511.19662.
3. G. Adesso and F. Illuminati, *Entanglement in continuous-variable systems: recent advances and current perspectives*, J. Phys. A 40 (2007), 7821–7880, for standard two-mode Gaussian partial-transpose invariants.
