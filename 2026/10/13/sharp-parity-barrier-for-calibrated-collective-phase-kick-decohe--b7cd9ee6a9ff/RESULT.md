# Sharp parity barrier for calibrated collective phase-kick decoherence

## Finding

For \(n\ge2\) qubits exposed to collective phase kicks at a known fixed Poisson event rate, knowing the one-qubit decoherence rate leaves a sharply constrained range of possible GHZ decoherence. The exact **least** possible GHZ rate is zero for every even \(n\) and every admissible local rate; odd \(n\) has a sharp nonzero-rate boundary. Write \(g=\Gamma_1/\Gamma\), where \(\Gamma>0\) is the event rate and \(\Gamma_1\in[0,2\Gamma]\) is the local real decoherence rate. Define \(T_n\) by \(T_n(\cos\theta)=\cos(n\theta)\). Then

\[
\min_{\mu:\,\int(1-\cos\theta)\,d\mu=g}\frac{\Gamma_n}{\Gamma}
=\begin{cases}
0, & n\text{ even},\quad 0\le g\le2,\\
0, & n\text{ odd},\quad 0\le g\le1+\cos(\pi/n),\\
1-T_n(1-g), & n\text{ odd},\quad 1+\cos(\pi/n)<g\le2.
\end{cases}
\]

For odd \(n\ge3\), put \(g_c=1+\cos(\pi/n)\). Immediately above the boundary,
\[
\frac{\Gamma_n^{\min}}{\Gamma}=\frac{n^2}{2\sin^2(\pi/n)}(g-g_c)^2+O_n((g-g_c)^3).
\]
This is an all-size parity classification, not simply a demonstration of one exceptional phase-kick law.

## Assumptions and scope

Let \(J_z=\tfrac12\sum_{j=1}^n Z_j\), and let \(\mu\) be any Borel probability measure on the phase circle, including measures with atoms. Fix an event rate \(\Gamma>0\). The Markovian, completely positive collective-kick generator is
\[
\mathcal L_\mu(\rho)=\Gamma\Big(\int e^{-i\theta J_z}\rho e^{i\theta J_z}\,\mu(d\theta)-\rho\Big).
\]
The one-qubit and the extremal GHZ coherence decay rates of their magnitudes are respectively
\[
\Gamma_1=\Gamma\int(1-\cos\theta)\,d\mu,\qquad
\Gamma_n=\Gamma\int(1-\cos(n\theta))\,d\mu.
\]
The imaginary characteristic-function component may contribute a known coherent frequency shift for a nonsymmetric law, but does not affect these decay rates. The optimizing laws constructed below are symmetric, so have no such shift. Neither independent dephasing nor a fixed kick variance/support/absolutely continuous density is assumed. The *event rate* \(\Gamma\) is fixed: this is not an optimization over changing \(\Gamma\).

The frequency to be estimated multiplies \(J_z\). The initial GHZ state is \(2^{-1/2}(|0\rangle^{\otimes n}+|1\rangle^{\otimes n})\). The quantum Fisher-information formula below refers only to that state and fixed interrogation time, with known noise dynamics.

## Proof

**1. Reduction to a one-moment extremum.** Let \(X=\cos\theta\in[-1,1]\). Since \(\cos(n\theta)=T_n(X)\), the calibration fixes \(\mathbb E X=1-g\), and the target is \(\Gamma_n/\Gamma=1-\mathbb E T_n(X)\). Any probability law of \(X\) can be lifted to a phase law symmetric under \(\theta\mapsto-\theta\). Thus one must compute the **greatest** \(\mathbb E T_n(X)\) for fixed mean \(x=1-g\), and an optimizer can always be symmetric.

**2. Even case.** If \(n\) is even, both \(T_n(1)\) and \(T_n(-1)\) equal \(1\). The measure \(\mu=(1-g/2)\delta_0+(g/2)\delta_\pi\) has local rate \(g\) and \(n\)-qubit rate zero. Nonnegativity of \(1-\cos(n\theta)\) proves optimality.

**3. Odd-case concave envelope.** Fix an odd \(n\ge3\), and set \(x_0=-\cos(\pi/n)\). This is the **leftmost** point in \([-1,1]\) where \(T_n\) attains its maximum \(1\). Define
\[
C_n(x)=\begin{cases}T_n(x),&-1\le x\le x_0,\\1,&x_0\le x\le1.\end{cases}
\]
Since \(|T_n(x)|\le1\), this function majorizes \(T_n\). It is also concave. To verify the nontrivial branch without citing a numerical plot, write \(x=-\cos u\) with \(0<u<\pi/n\). Because \(n\) is odd,
\[
T_n(x)=-\cos(nu),\quad T_n'(x)=\frac{n\sin(nu)}{\sin u},\quad
T_n''(x)=\frac{n[n\cos(nu)\sin u-\sin(nu)\cos u]}{\sin^3u}.
\]
For \(0<u<\pi/(2n)\), strict convexity of \(\tan\) gives \(\tan(nu)>n\tan u\), making the numerator negative. For \(\pi/(2n)\le u<\pi/n\), \(\cos(nu)\le0\), while \(\sin(nu)>0\) and \(\cos u>0\), so it is again negative. At \(x_0\), \(T_n'(x_0)=0\), which matches the derivative of the constant branch; the extension at \(x=-1\) is continuous. Therefore \(C_n\) is concave on the closed interval.

Jensen's inequality now yields the global bound
\[
\mathbb E T_n(X)\le\mathbb E C_n(X)\le C_n(\mathbb E X)=C_n(1-g).
\]
This is an inequality over *all* Borel phase laws, not just finitely supported choices.

**4. Sharpness, all boundaries and the threshold.** If \(x=1-g\ge x_0\), set \(\theta_0=\pi-\pi/n\) and \(p=g/[1+\cos(\pi/n)]\in[0,1]\). The symmetric law
\[
\mu=(1-p)\delta_0+\frac p2(\delta_{\theta_0}+\delta_{-\theta_0})
\]
has \(\mathbb EX=1-g\) and \(\cos(n\theta)=1\) at every support point, because \(n\theta_0=(n-1)\pi\) is an even multiple of \(\pi\). Consequently its GHZ decay rate is zero and it attains \(C_n(x)=1\). If \(x<x_0\), take \(\theta=\arccos x\) and \(\mu=(\delta_\theta+\delta_{-\theta})/2\). Then \(X=x\) almost surely, so \(\mathbb E T_n(X)=T_n(x)=C_n(x)\), attaining the bound. These constructions include \(g=0\), \(g=g_c\), and \(g=2\); for odd \(n\) the last gives rate \(2\).

At \(x_0=-\cos(\pi/n)\), the derivative of \(T_n\) vanishes and the second derivative equals \(-n^2/\sin^2(\pi/n)\). Taylor expansion at \(x_0\), using \(x=1-g=x_0-(g-g_c)\), gives the stated quadratic onset. The remainder holds with \(n\) fixed.

**5. GHZ quantum Fisher information.** Since the two GHZ basis vectors differ in their \(J_z\) eigenvalues by \(n\), their off-diagonal density-matrix entry after interrogation time \(t\) has magnitude \(\tfrac12e^{-\Gamma_nt}\) and signal phase \(n\omega t\). The two-level symmetric-logarithmic-derivative formula therefore gives
\[
F_Q(\omega;n,t,\mu)=n^2t^2e^{-2\Gamma_nt}.
\]
Maximizing over admissible \(\mu\) is equivalent to minimizing \(\Gamma_n\), and thus yields \(F_Q^{\max}=n^2t^2e^{-2\Gamma t r_n(g)}\). There is no claim about globally optimal probes or protocols.

## Verification

An accompanying self-contained standard-Python script `verify.py` checks explicit extremal distributions against exact Chebyshev evaluations for a range of sizes/calibrations, verifies the global concave-majorant inequality on deterministic grids and many randomized finite-support laws, and cross-checks the GHZ QFI expression on its two-dimensional density-matrix model. Run `python verify.py` in the extracted directory; successful completion prints `VERIFY_OK`. Computations are consistency tests, **not** a substitute for the concavity/Jensen proof or a certificate covering continuous inputs.

## Relationship to prior work

Liu, Heng, Wang and Ma, *Higher-order noise statistics restore Heisenberg scaling under collective dephasing* (arXiv:2607.02962v1), derive the finite-rate phase-kick generator, the characteristic-function decay law \(\Gamma_q=\Gamma[1-\operatorname{Re}\phi(q)]\), and GHZ Fisher information. They establish broad scaling phenomena and flag deterministic or lattice kick distributions as outside the hypotheses of their saturation theorem, including a lattice counterexample in supplemental discussion. These are acknowledged premises: neither the general decay identity nor the *existence* of special lattice behavior is claimed as new. The result here instead solves the inverse **minimum**-decay problem at every specified single-qubit rate \(g\) and event rate \(\Gamma\), for each finite \(n\), including the sharp odd/even classification and the odd-size quadratic activation coefficient.

The classical facts \(\cos(n\theta)=T_n(\cos\theta)\), the concave-envelope principle for fixed-mean moment problems, and Jensen's inequality are standard and not new. The contribution is the explicit concave envelope relevant to this noise-calibration problem and the resulting all-size physically interpreted sharp bound. Decoherence-free subspace constructions for symmetry-protected states and general truncated trigonometric moment theory do not automatically specify the above sharp calibrated GHZ envelope. The paper's later expanded version, *Entanglement Drives Common Noise into the Strong-Coupling Regime* (same arXiv identifier), was located but could not be inspected in complete form, so possible implicit or explicit coverage there remains a meaningful originality risk.

## Limitations

Atomic kick laws are allowed; this is essential for exact protection at nonzero local decoherence. The result does not establish such protection for an absolutely continuous law, its perturbative robustness, an experimentally realizable calibration protocol, optimal sensing under added independent noise, or optimality among all initial states/measurements. It assumes a fixed known Poisson event rate and unconstrained phase-kick distribution; fixing only a single-atom \(T_2\), but not the event rate, gives a different optimization. The statement is idealized and the lack of full-text access to the expanded closest paper leaves an originality risk.

## References

1. J. Liu, X. Heng, Z. Wang and D. Ma, *Higher-order noise statistics restore Heisenberg scaling under collective dephasing*, arXiv:2607.02962v1 (first public 2026-07-07). Full original manuscript: https://www.researchgate.net/publication/408521453_Higher-order_noise_statistics_restore_Heisenberg_scaling_under_collective_dephasing
2. Y. Zhou, X. Lei, X. Heng, Z. Wang and D. Ma, *Entanglement Drives Common Noise into the Strong-Coupling Regime*, later version of arXiv:2607.02962 (abstract/index checked; complete expanded text not inspected).
3. P. Zanardi and M. Rasetti, *Noiseless Quantum Codes*, Phys. Rev. Lett. 79, 3306 (1997). Structural context for decoherence-free quantum codes; no claim of exact inverse phase-kick optimization attributed.
4. MSC2020: 81S22, *Open systems, reduced dynamics, master equations, decoherence*.
