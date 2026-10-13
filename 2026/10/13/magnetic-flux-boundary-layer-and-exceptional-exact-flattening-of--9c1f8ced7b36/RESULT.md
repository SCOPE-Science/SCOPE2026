# Magnetic-flux boundary layer and exceptional exact flattening of averaged quantum cycles

## Finding

For each integer \(n\geq3\), a weak-flux continuous-time quantum walk on a cycle has a nontrivial, explicit finite-window average when the observation time scales inversely with magnetic flux. The limiting distribution, rather than the unperturbed or generic-flux infinite-time average, resolves the singularity between them.

Write \(\mathbb Z_n\) for the cycle vertices and choose the hopping Hamiltonian
\[
H_\alpha|j\rangle=e^{-2\pi i\alpha/n}|j+1\rangle+e^{2\pi i\alpha/n}|j-1\rangle,
\quad j\in\mathbb Z_n.
\]
Starting from \(|0\rangle\), define the position probability averaged over a finite observation window by
\[
Q_{n,j}(T,\alpha)=\frac1T\int_0^T\big|\langle j|e^{-itH_\alpha}|0\rangle\big|^2\,dt,\qquad T>0.
\]
Let \(\alpha_r>0\) tend to zero while \(T_r\to\infty\), with \(\alpha_rT_r\to\tau\in[0,\infty)\). For every vertex \(j\),
\[
Q_{n,j}(T_r,\alpha_r)\longrightarrow q_{n,j}(\tau)
=\frac1n+\frac1{n^2}\!
\sum_{\substack{0\le k<n\\ 2k\not\equiv0\ (\mathrm{mod}\ n)}}
 e^{4\pi i kj/n}
 G\!\left(\frac{8\pi\tau}{n}\sin\frac{2\pi k}{n}\right),
\quad
G(z):=\int_0^1e^{izu}\,du.
\]
Equivalently, \(G(z)=e^{iz/2}\operatorname{sinc}(z/2)\), with \(\operatorname{sinc}(0)=1\). The displayed expression is real and defines a probability vector. Uniformly in the vertex, for any bounded nonnegative product \(\alpha T\) and sufficiently small \(\alpha>0\),
\[
\max_j\big|Q_{n,j}(T,\alpha)-q_{n,j}(\tau)\big|
\le C_{n,K}\left(T^{-1}+|\alpha T-\tau|\right)
\]
whenever \(\alpha T,\tau\in[0,K]\) and \(T\) is sufficiently large.

**The complete finite-parameter flattening classification:** for a finite \(\tau>0\), all \(n\) limiting probabilities equal \(1/n\) if and only if exactly one of the following holds:
\[
\begin{aligned}
 n&=3, & \tau&\in\tfrac{\sqrt3}{2}\mathbb N_{>0};\\
 n&=4, & \tau&\in\tfrac12\mathbb N_{>0};\\
 n&=6, & \tau&\in\tfrac{\sqrt3}{2}\mathbb N_{>0}.
\end{aligned}
\]
For every other \(n\ge3\), the limiting profile fails to be uniform at every finite \(\tau>0\). It is also nonuniform at \(\tau=0\) for all \(n\ge3\), while \(q_{n,j}(\tau)\to1/n\) as \(\tau\to\infty\).

## Assumptions and scope

All statements concern a single particle in the \(n\)-dimensional position basis of a ring. The hopping strength and Planck's constant are normalized to one. The phase \(\alpha\) is a dimensionless total flux in units of a flux quantum. The weak-flux sequence is taken with positive \(\alpha_r\to0\); \(n\) is fixed. The parameter \(\tau\) is the limit of the product of observation duration and total flux. This is a limit of **finite-window time averages**; no environment, physical dephasing, or instantaneous uniform mixing is assumed.

## Proof

**1. An exact finite-window formula.** The Fourier vectors
\[
|f_k\rangle=\frac1{\sqrt n}\sum_{j=0}^{n-1}e^{2\pi i kj/n}|j\rangle,\qquad 0\le k<n,
\]
form an orthonormal eigenbasis. Direct substitution in the defined action of \(H_\alpha\) gives
\[
 E_k(\alpha)=2\cos\!\left(\frac{2\pi(k+\alpha)}n\right).
\]
Consequently
\[
\langle j|e^{-itH_\alpha}|0\rangle
=\frac1n\sum_{k=0}^{n-1}e^{2\pi i kj/n}e^{-itE_k(\alpha)}.
\]
Squaring and integrating termwise (a finite sum) gives the exact identity
\[
Q_{n,j}(T,\alpha)
=\frac1{n^2}\sum_{k,l=0}^{n-1}e^{2\pi i(k-l)j/n}
G\big(-T[E_k(\alpha)-E_l(\alpha)]\big).\tag{1}
\]
Here \(G\) is defined by the integral in the finding, so its sign convention follows exactly from the propagation phase; \(G(-z)=\overline{G(z)}\).

**2. Resolving the small-flux spectral pairs.** At zero flux, \(E_k(0)=E_l(0)\) precisely when \(k\equiv l\) or \(k\equiv-l\pmod n\), because equality of two cosine values forces equality or opposition of their arguments modulo a complete turn. For every other pair, the zero-flux energy difference is nonzero and, for this fixed finite \(n\), stays bounded away from zero for sufficiently small \(\alpha\). Since \(|G(z)|\le\min\{1,2/|z|\}\), every such pair contributes \(O_n(T^{-1})\) in (1).

The diagonal \(k=l\) contributes exactly \(1/n\). For a distinct opposite pair \(l\equiv-k\pmod n\), the difference is
\[
E_k(\alpha)-E_{-k}(\alpha)
=-4\sin\!\left(\frac{2\pi k}n\right)
\sin\!\left(\frac{2\pi\alpha}n\right),
\]
so that its argument in (1) tends to \(\frac{8\pi\tau}{n}\sin(2\pi k/n)\). These are exactly the terms in the claimed profile. The exclusion \(2k\equiv0\pmod n\) avoids counting the self-opposite modes as extra pairs. Continuity of \(G\) completes convergence.

For the quantitative estimate, differentiate its integral: \(|G'(z)|\le\int_0^1u\,du=1/2\) for real \(z\). The opposite-pair arguments differ from their limits by at most \(C_n(|\alpha T-\tau|+T\alpha^3)\) for small \(\alpha\). Boundedness of \(\alpha T\) implies \(T\alpha^3=O_K(T^{-2})\). There are only finitely many spectral pairs, proving the stated \(O_{n,K}(T^{-1}+|\alpha T-\tau|)\) bound.

**3. Algebraic classification of exact limiting uniformity.** Set
\[
z_k=\frac{8\pi\tau}{n}\sin\frac{2\pi k}{n},\qquad
\omega=e^{2\pi i/n}.
\]
The deviation \(q_{n,j}(\tau)-1/n\) is a finite discrete Fourier expansion with frequency \(2k\pmod n\) and coefficient \(G(z_k)/n^2\). A finite Fourier series on \(\mathbb Z_n\) vanishes at every vertex if and only if each frequency coefficient vanishes.

If \(n\) is **odd**, multiplication by \(2\) is invertible modulo \(n\), so the nonzero-frequency coefficients are separate: uniformity demands \(G(z_k)=0\) for each \(1\le k<n\). For finite real nonzero \(z\), the zero set of \(G(z)=(e^{iz}-1)/(iz)\) is exactly \(2\pi(\mathbb Z\setminus\{0\})\). All \(z_k\) under consideration are nonzero when \(\tau>0\). For \(n\ge5\), applying this to \(k=1,2\) requires
\[
\frac{\sin(4\pi/n)}{\sin(2\pi/n)}=2\cos(2\pi/n)\in\mathbb Q.\tag{2}
\]
Yet \(2\cos(2\pi/n)=\omega+\omega^{-1}\) is an algebraic integer: roots of unity are algebraic integers, and the latter are closed under addition. A rational algebraic integer must be an integer. For odd \(n\ge5\), \(2\cos(2\pi/n)\) is strictly between \(0\) and \(2\) and is not \(1\): the latter would force \(n=6\). Thus (2) is impossible. For \(n=3\), the two nonzero modes have sine magnitudes \(\sqrt3/2\), and setting their arguments to nonzero multiples of \(2\pi\) gives exactly \(\tau\in(\sqrt3/2)\mathbb N_{>0}\).

If \(n\) is **even**, the two values \(k\) and \(k+n/2\), for \(1\le k<n/2\), represent the same nonzero Fourier frequency \(2k\). Their arguments satisfy \(z_{k+n/2}=-z_k\), so the corresponding coefficient becomes
\[
G(z_k)+G(-z_k)=\frac{2\sin z_k}{z_k}.
\]
Hence uniformity demands \(z_k\in\pi(\mathbb Z\setminus\{0\})\) for every \(1\le k<n/2\). For \(n\ge8\), taking the ratio at \(k=2\) and \(k=1\) again forces the rationality in (2). But now \(2\cos(2\pi/n)\) is strictly between \(1\) and \(2\), impossible for a rational algebraic integer. At \(n=4\), the only independent argument is \(z_1=2\pi\tau\), giving \(\tau\in\tfrac12\mathbb N_{>0}\). At \(n=6\), the independent arguments have the same sine magnitude \(\sqrt3/2\), giving \(\tau\in\tfrac{\sqrt3}2\mathbb N_{>0}\). Necessity and sufficiency follow from the Fourier coefficient criterion.

**4. Two distinct orders of limits.** When \(\tau=0\), all retained coefficients equal one and, at the starting vertex, all their Fourier phases equal one. Since there is at least one retained mode for \(n\ge3\), \(q_{n,0}(0)>1/n\). For \(\tau\to\infty\), each sine factor in a retained term is nonzero, so \(G(z_k)\to0\) term by term; hence \(q_{n,j}(\tau)\to1/n\). Finally, if \(\alpha\in(0,1)\setminus\{1/2\}\) is held fixed, the eigenvalues are distinct: a distinct equality would require \(k+l+2\alpha\in n\mathbb Z\), impossible as \(2\alpha\) is not an integer. Only the diagonal remains under \(T\to\infty\), and the average is exactly \(1/n\). This proves the noncommutation of weak-flux and long-time limits.

## Verification

The standalone `verify.py` implements the exact spectral double sum (1), independently approximates the time integral by Simpson quadrature of the directly constructed state amplitudes, tests the uniform resonances in dimensions three, four and six, tests the boundary-layer convergence at increasing observation times, and checks normalization and real-valuedness on a finite sample. Execute it with `python3 verify.py` using only the Python standard library. It returns `VERIFY_OK chiral_cycle_flux_window=passed` if all assertions hold. All infinite-scope claims follow from the preceding algebraic argument, not from finite sampling or numerical tolerance checks.

## Relationship to prior work

Adamczak et al. (2007), arXiv:0708.2096v1, analyzed the **zero-flux, real-adjacency** continuous-time walk on cycles and its nonuniform infinite-time average. Their work supplies the natural singular limit and the Fourier spectral framework, but its stated mixing theorems do not examine weak magnetic flux with a time window inversely proportional to flux.

Levine et al. (2026), arXiv:2605.04414v1, proved that a chiral circulant with simple spectrum has uniform **infinite-time** average and exhibited oriented odd cycles. The fixed-flux generic uniformity observed here is consistent with that theorem; it does not determine the joint small-flux/large-time profile or its exceptional exact flattening dimensions. Zanoli et al. (2026), DOI:10.3389/frqst.2026.1894991, studied flux-threaded ring Hamiltonians and parameter estimation using a different observable and initial-state protocol. The present theorem specifically concerns the distribution of a position measurement averaged over a finite observation window from a localized initial state.

## Limitations

The cycle size \(n\) is fixed; the estimates are not asserted uniformly as \(n\to\infty\). The special resonance times are exact **only for the boundary-layer limiting probability vector**; no assertion is made that finite \(T\) and nonzero \(\alpha\) give exact uniformity. The theorem does not cover arbitrary graphs, nonuniform hoppings, baths, or measurements interleaved with evolution. A comparable result may have been derived elsewhere under another formulation of near-degenerate spectral dephasing; priority has not been independently certified.

## References

1. W. Adamczak, K. Andrew, L. Bergen, D. Ethier, P. Hernberg, J. Lin, and C. Tamon, *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096v1 (first publicly posted 2007-08-15), https://arxiv.org/html/0708.2096v1.
2. L. Levine, J. J. Mesapam, B. Mustico, C. Tamon, G. Tucker, and H. Zhan, *Uniform Mixing in Chiral Quantum Walks*, arXiv:2605.04414v1 (2026), https://arxiv.org/html/2605.04414v1.
3. L. Zanoli, G. Ragazzi, P. Bordone, and M. G. A. Paris, *Quantum walks on a ring as a versatile single-parameter sensor*, *Frontiers in Quantum Science and Technology* **5** (2026), DOI:10.3389/frqst.2026.1894991.
4. P. Luppi, *Flux control of measurement back-action and Leggett-Garg correlations in chiral quantum walks*, arXiv:2608.12519v1 (2026); examined from accessible abstract only for a possible related flux model.
