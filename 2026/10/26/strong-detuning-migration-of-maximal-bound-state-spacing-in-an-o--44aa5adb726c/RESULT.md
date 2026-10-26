# Strong-detuning migration of maximal bound-state spacing in an optical oscillator

## Finding
For the single-excitation light–matter Hamiltonian
\[
H_{g,\Omega}=\begin{pmatrix}|D|&g|x|\\g|x|&\Omega\end{pmatrix}
\]
on \(L^2(\mathbb R)\oplus L^2(\mathbb R)\), fix \(g>0\) and increase the positive atomic detuning \(\Omega\to\infty\). Let \(\omega_1<\omega_2<\cdots\) be its bound-state energies above \(\Omega\), and put \(\Delta_n=\omega_{n+1}-\omega_n\). Every fixed \(\Omega\) admits at least one maximizing index \(n_\Omega\in\operatorname{argmax}_{n\ge1}\Delta_n\).

Define
\[
C=\frac{3\pi}{4},\qquad z_*=\frac{3+\sqrt3}{4},\qquad t_*=z_*^{3/2}\sqrt{z_*-1}.
\]
Then **every choice** of maximizing index satisfies
\[
\lim_{\Omega\to\infty}\frac{g n_\Omega}{\Omega^2}
=\frac{t_*}{C}=0.233621921565\ldots,
\]
and the maximal spacing obeys
\[
\lim_{\Omega\to\infty}\frac{\Omega}{g}\max_{n\ge1}\Delta_n
=\frac{2C\sqrt{z_*-1}}{\sqrt{z_*}(4z_*-3)}
=1.070105058314\ldots.
\]
The two limiting constants apply to the entire infinite bound spectrum, not to a finite search window.

## Assumptions and scope
The photon dispersion is \(|D|\); the real-space coupling is \(g|x|\); the matter frequency \(\Omega>0\) is spatially constant. The analysis concerns the self-adjoint realization and simple discrete eigenvalues established in Johar–Kraisler. The coupling \(g>0\) is fixed (equivalently, it suffices that \(g/\Omega^2\to0\)); there is no assumption of a fixed eigenvalue index. The relevant mode index may diverge jointly with detuning; no interchange of nonuniform limits is assumed.

## Proof
Johar–Kraisler's spectral reduction gives positive ordered roots \(r_1<r_2<\cdots\), alternating between absolute values of zeros of \(\mathrm{Ai}'\) and \(\mathrm{Ai}\), and the exact equation
\[
\omega_n^3(\omega_n-\Omega)=g^2r_n^3,
\qquad \omega_n>\Omega.
\]
The standard large-index Airy-zero expansions (DLMF §9.9(iv)) imply, separately for both parities,
\[
r_n^{3/2}=C(n-\tfrac12)+O(n^{-1}),\qquad
r_{n+1}^{3/2}-r_n^{3/2}\longrightarrow C.
\]
The first expansion follows from the phases \(\tfrac{3\pi}{2}(k-\tfrac34)\) of the derivative zeros and \(\tfrac{3\pi}{2}(k-\tfrac14)\) of the function zeros, which interlace. Define the small parameter \(\delta=g/\Omega^2\), \(t_n=\delta r_n^{3/2}\), and the unique smooth function \(W:[0,\infty)\to[1,\infty)\) characterized by
\[
W(t)^3[W(t)-1]=t^2,\qquad W(0)=1.
\]
Then exactly \(\omega_n=\Omega W(t_n)\). A mean-value point \(\xi_n\in(t_n,t_{n+1})\) gives the exact identity
\[
\frac{\Omega}{g}\Delta_n
=\frac{t_{n+1}-t_n}{\delta}W'(\xi_n)
=[r_{n+1}^{3/2}-r_n^{3/2}]W'(\xi_n).
\]
From the defining equation,
\[
W'(t)=\frac{2\sqrt{W(t)-1}}{\sqrt{W(t)}[4W(t)-3]}.
\]
It is positive for \(t>0\), tends to zero at both \(t\downarrow0\) and \(t\to\infty\), and has exactly one maximum. Indeed, differentiation of its logarithm in the variable \(z=W(t)>1\) yields the critical equation
\[
8z^2-12z+3=0.
\]
Only its larger root \(z_*=(3+\sqrt3)/4\) is in \((1,\infty)\), and the corresponding \(t\) is \(t_*\).

For any positive \(\delta\), the individual gaps tend to zero as \(n\to\infty\): the root increments remain bounded and \(W'(t_n)\to0\). Hence a maximum exists. Choose integers \(m_\delta\sim t_*/(C\delta)\). Their mean-value points tend to \(t_*\) and their root increments tend to \(C\), giving the lower bound \(\liminf\max_n(\Omega/g)\Delta_n\ge C W'(t_*)\).

For the reverse bound, consider maximizing indices \(n_\delta\). They cannot remain bounded as \(\delta\downarrow0\), because then \(t_{n_\delta}\to0\) and their rescaled gaps tend to zero, contradicting that lower bound. Consequently \(n_\delta\to\infty\), their root increments tend to \(C\), and the exact mean-value identity gives \(\limsup\max_n(\Omega/g)\Delta_n\le C W'(t_*)\). Equality of the bounds forces \(W'(\xi_{n_\delta})\to W'(t_*)\). Uniqueness of the maximum and vanishing at both endpoints imply \(\xi_{n_\delta}\to t_*\). Since \(t_{n_\delta+1}-t_{n_\delta}=\delta[C+o(1)]\to0\), also \(t_{n_\delta}\to t_*\). Finally \(t_n/(\delta n)\to C\), whence \(\delta n_\delta\to t_*/C\). This proves both limits for every maximizing-index selection.

## Verification
The accompanying `verify_spacing.py` solves the exact positive-root equation numerically using SciPy Airy zeros and a bracketing solver, then maximizes adjacent spacings over a finite diagnostic range. For \(g=1\), detunings \(\Omega=20,30,40\) produce maximizing indices \(93,211,373\); the rescaled gaps are approximately \(1.070872814,1.070443378,1.070297302\), approaching the proved coefficient \(1.070105058314\). Finite computations serve only as diagnostic checks; the proof above establishes the global infinite-index limits.

## Relationship to prior work
Johar and Kraisler, *Spectral Theory of an Exactly Solvable Quantum-Optical Oscillator*, arXiv:2610.18421, establish the Hamiltonian, full bound eigenvalue equation and fixed-\(\Omega\) high-index asymptotics. These ingredients are prior results, not claimed here. The present limit instead optimizes **all** adjacent gaps as detuning diverges and obtains the previously unresolved simultaneous scaling \(n\asymp\Omega^2/g\), which cannot be inferred by substituting a moving detuning into a fixed-parameter error term. DLMF §9.9 provides the classical Airy-zero asymptotics; the new step is the uniform global maximum argument via the exact mean-value identity and unique scaling-profile maximizer.

## Limitations
The result concerns a mathematically idealized, unbounded spatial coupling and exact eigenvalues; it provides no finite-detuning error estimate, numerical-noise robustness, or uniqueness of the maximizing index at any given finite detuning. It does not cover modified photon dispersion, finite spatial confinement, or interacting multi-excitation models. Priority is best-knowledge only; a broader uninspected theorem could imply these constants. No independent audit has been performed.

## References
1. S. Johar and J. Kraisler, *Spectral Theory of an Exactly Solvable Quantum-Optical Oscillator*, arXiv:2610.18421 (first posted 13 October 2026), https://arxiv.org/html/2610.18421v2 .
2. NIST Digital Library of Mathematical Functions, §9.9(iv), *Airy Function Zeros: Asymptotic Expansions*, https://dlmf.nist.gov/9.9 .
