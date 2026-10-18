# Magnetic-flux lifting of dark states: exact singular absorption times on quantum cycles

## Finding
For every integer \(n\ge3\), detection strength \(\gamma>0\), and starting vertex \(d\in\{0,\ldots,n-1\}\), consider a particle with tight-binding Hamiltonian
\[
H_{n,\Phi}=\sum_{j\bmod n}\left(e^{i\Phi/n}|j\rangle\langle j+1|+e^{-i\Phi/n}|j+1\rangle\langle j|\right)
\]
and one irreversible detector at vertex \(0\), represented in the no-jump evolution by \(K_{\Phi}=H_{n,\Phi}-i\gamma|0\rangle\langle0|/2\). Its no-jump survival probability is \(p_d(t,\Phi)=\|e^{-itK_\Phi}|d\rangle\|^2\), and its unconditional mean absorption time is \(T_d(\Phi)=\int_0^\infty p_d(t,\Phi)\,dt\), possibly infinite.

**Theorem.** For \(0<|\Phi|<\pi\), all \(T_d(\Phi)\) are finite. As \(\Phi\to0\),
\[
\lim_{\Phi\to0}\Phi^2 T_d(\Phi)=C_{n,d}(\gamma):=
\begin{cases}
\displaystyle \frac{\gamma}{8}d(n-d),&n\ \text{odd},\\[2mm]
\displaystyle \frac{\gamma}{4}r(m-r),&n=2m\ \text{even},\quad r=d\bmod m.
\end{cases}
\]
In particular, this limit is strictly positive for every initial vertex other than \(d=0\), and, when \(n\) is even, \(d=n/2\). For those positive-coefficient vertices the mean time diverges asymptotically as \(C_{n,d}(\gamma)/\Phi^2\). At exactly zero flux their mean time is infinite, due to a nonzero dark-state overlap. For the two zero-coefficient starting vertices (the detector, and the antipode when it exists), both \(T_d(0)\) and the small-nonzero-flux means stay finite.

The result includes the **full slow-time survival profile**: for every fixed \(s>0\),
\[
\lim_{\Phi\to0}p_d(s/\Phi^2,\Phi)
=\frac2n\sum_{k=1}^{\lfloor(n-1)/2\rfloor}
\sin^2\!\left(\frac{2\pi k d}{n}\right)
\exp\!\left[-\frac{8s}{n\gamma}\sin^2\!\left(\frac{2\pi k}{n}\right)\right].
\]
A further exact singularity occurs even when starting at the detector: for every nonzero \(|\Phi|<\pi\), \(T_0(\Phi)=n/\gamma\), while \(T_0(0)=(\lfloor n/2\rfloor+1)/\gamma\). Thus the mean absorption time from the detector itself has a finite jump in the limit of vanishing flux, despite having no \(\Phi^{-2}\) divergence.

## Assumptions and scope
The cyclic Hilbert space has orthonormal vertex basis \(\{|j\rangle:j\in\mathbb Z/n\mathbb Z\}\). Hopping amplitudes along the two orientations have unit modulus, with total gauge-invariant flux \(\Phi\). The detector jump operator is \(\sqrt\gamma\,|\varnothing\rangle\langle0|\); its no-jump norm squared gives the probability of no detection, with physical jump rate \(\gamma\) at vertex \(0\). All limits in the theorem hold at fixed finite \(n\), fixed positive \(\gamma\), and fixed initial vertex \(d\). The interval \(|\Phi|<\pi\) excludes the separate half-flux degeneracy. No limit interchanging \(n\), \(\gamma\), and \(\Phi\) is claimed.

## Proof
**1. Dark and bright decomposition at zero flux.** Let \(u_k(j)=n^{-1/2}e^{2\pi ikj/n}\), \(\theta_k=2\pi k/n\), and \(E_k=2\cos\theta_k\). For \(1\le k\le p=\lfloor(n-1)/2\rfloor\), the pair \(u_k,u_{n-k}\) has equal energy. Form the normalized cosine/bright and sine/dark vectors \(B_k=(u_k+u_{n-k})/\sqrt2\) and \(D_k=(u_k-u_{n-k})/(i\sqrt2)\). Then \(\langle0|B_k\rangle=\sqrt{2/n}\) while \(\langle0|D_k\rangle=0\). The constant Fourier mode, and the alternating mode for even \(n\), are bright. The \(D_k\) are precisely the complete dark space for a single detector at zero flux. In particular, \(|\langle D_k|d\rangle|^2=(2/n)\sin^2(d\theta_k)\).

Write \(\mathcal B\) for the span of the bright vectors and \(K_{\mathcal B}\) for the restriction of \(K_0\). Every eigenvalue of \(K_{\mathcal B}\) has strictly negative imaginary part: if an eigenvector had real eigenvalue, the nonpositive imaginary part of its expectation would force zero amplitude at the detector; it would then be a bright eigenvector of \(H_0\), impossible because each bright Fourier-energy line has nonzero detector amplitude. Thus each dark eigenvalue \(E_k\) of \(K_0\) is isolated and algebraically simple, and the entire bright part decays.

**2. Imaginary second-order splitting.** In the fixed Fourier basis, \(H_{n,\Phi}u_k=2\cos(\theta_k+\Phi/n)u_k\). On \(\operatorname{span}\{B_k,D_k\}\), the first flux derivative has off-diagonal matrix element of magnitude \(v_k=2|\sin\theta_k|/n\) and no diagonal term. Its second derivative contributes only a real scalar at the order relevant to the imaginary part of the eigenvalue. Analytic perturbation theory for the simple dark eigenvalue therefore gives
\[
\operatorname{Im}\lambda_k(\Phi)
=\Phi^2v_k^2\operatorname{Im}\langle B_k,(E_k-K_{\mathcal B})^{-1}B_k\rangle+O(\Phi^3).
\]
The resolvent matrix element is exact for arbitrary \(\gamma>0\). In the bright-energy basis, write \(a_j=\langle0|B_j\rangle>0\); the energy \(E_k\) is nondegenerate there, with \(a_k^2=2/n\). Solving \((E_k-K_{\mathcal B})z=B_k\), its \(k\)-th coordinate equation fixes \(\sum_j a_jz_j=2/(i\gamma a_k)\). The other coordinate equations make \(z_j\) real for \(j\ne k\). Hence \(\operatorname{Im}z_k=-2/(\gamma a_k^2)=-n/\gamma\). It follows that
\[
\boxed{\operatorname{Im}\lambda_k(\Phi)=-\frac{4\sin^2\theta_k}{n\gamma}\Phi^2+O(\Phi^3).}
\]
All eigenvalues away from these dark branches remain uniformly in the open lower half-plane near \(\Phi=0\).

**3. Survival scaling and the integrated mean.** For \(0<|\Phi|<\pi\), the Hermitian magnetic cycle has distinct Fourier energies. Every Fourier eigenvector is nonzero at vertex \(0\), so the dissipative \(K_\Phi\) has no real eigenvalue; its survival is integrable. The spectral projections of the slow branches converge to \(|D_k\rangle\langle D_k|\). Their decay-rate limits are \(-2\operatorname{Im}\lambda_k(\Phi)/\Phi^2=8\sin^2\theta_k/(n\gamma)\), and their limiting projectors are orthogonal. This proves the stated \(s/\Phi^2\) survival law for each fixed \(s>0\).

The integrated mean may be evaluated using the finite-dimensional spectral expansion. Diagonal slow-mode terms contribute \(|\langle D_k|d\rangle|^2/[-2\operatorname{Im}\lambda_k(\Phi)]\). Distinct slow modes have different limiting real energies, so their integrated cross terms remain bounded. Contributions involving uniformly decaying bright modes are also bounded. Consequently
\[
\lim_{\Phi\to0}\Phi^2T_d(\Phi)=\frac\gamma4\sum_{k=1}^{p}\frac{\sin^2(d\theta_k)}{\sin^2\theta_k}.
\]
The standard cyclic Parseval identity
\[
\sum_{j=1}^{N-1}\frac{\sin^2(\pi rj/N)}{\sin^2(\pi j/N)}=r(N-r),\qquad 0\le r<N,
\]
follows by writing the quotient as the squared modulus of a finite geometric sum and using discrete Fourier orthogonality. For odd \(n\), multiplication of Fourier labels by two permutes the nonzero residues, and symmetry halves the sum, giving \(d(n-d)/2\). For \(n=2m\), the paired dark labels run through \(1,\ldots,m-1\), and the sum equals \(r(m-r)\), \(r=d\bmod m\). These are the claimed closed forms. If all initial dark overlaps vanish, the slow spectral weights are \(O(\Phi^2)\), so their contributions to the mean stay bounded; the bright contributions remain bounded as well.

**4. Exact jump in the detector-start mean.** For \(\Phi\ne0\), define \(A_\Phi=-iH_{n,\Phi}-\gamma|0\rangle\langle0|/2\) and \(X=\int_0^\infty e^{A_\Phi^\dagger t}e^{A_\Phi t}\,dt\). It solves \(A_\Phi^\dagger X+XA_\Phi=-I\). Taking traces cancels the commutator and yields \(-\gamma X_{00}=-n\); hence \(T_0(\Phi)=n/\gamma\). At exactly zero flux, the initial vector \(|0\rangle\) lies entirely in the bright subspace of dimension \(\lfloor n/2\rfloor+1\); applying the same trace identity to that decaying restriction gives \(T_0(0)=(\lfloor n/2\rfloor+1)/\gamma\). This establishes the finite discontinuity and completes the proof.

## Verification
The accompanying standalone `verify_flux.py` constructs the complex cycle generator directly, solves the continuous Lyapunov equation for the integrated survival Gramian, and independently computes the proposed Fourier coefficients. It checks 63 finite-dimensional Gramian equations, 63 detector-start identities, 126 paired-flux asymptotic comparisons, 126 dark-projection checks, 48 decay-branch comparisons, and 28 rescaled-survival comparisons for \(3\le n\le9\), several detection rates, and multiple nonzero fluxes. This is numerical corroboration of the proved all-size formulas, not an exhaustive or independent proof. The script requires Python with NumPy and SciPy and runs with `python verify_flux.py`.

## Relationship to prior work
Mülken and colleagues studied coherent exciton trapping and non-Hermitian survival spectra, including trapping on cycles [1]. Varbanov, Krovi and Brun developed continuous-quantum-walk hitting-time machinery and analyzed symmetry-induced infinite hitting times [2]. Agliari, Mülken and Blumen analyzed multiple-trap arrangements and exact dark modes in unthreaded cycles [3]. These precedents establish the absorption framework and the importance of dark states. The point here is **not** the existence of a dark subspace, the general Lyapunov method, or the general detector-start trace identity; it is the explicit all-cycle weak-flux lifetime law, parity-dependent coefficient, and multimode slow-time profile at fixed positive loss. Work on magnetic-flux-dependent, stroboscopically measured quantum triangles [4] concerns a different monitoring protocol and geometry. A more general historical first-passage representation might imply the present coefficient after a nontrivial specialization; this is an acknowledged residual originality risk.

## Limitations
The result assumes one coherent single-particle nearest-neighbor cycle, one perfectly local irreversible Markovian detector, uniform hopping magnitudes, fixed finite size, and fixed positive detection strength. It does not cover stroboscopic projection measurements, multiple simultaneous sinks, generic disordered rings, joint large-size/weak-flux limits, or flux neighborhoods of \(\Phi=\pi\). The exact single-detector start-time formula is an ancillary identity, not an independent originality claim. The source comparison is not an exhaustive proof of novelty, and no external scientific validation has been performed.

## References
[1] O. Mülken et al., *Survival Probabilities in Coherent Exciton Transfer with Trapping*, Phys. Rev. Lett. 99, 090601 (2007), arXiv:0705.3700 (first public version 2007-05-25).

[2] M. Varbanov, H. Krovi, T. A. Brun, *Hitting time for the continuous quantum walk*, Phys. Rev. A 78, 022324 (2008), arXiv:0803.3446.

[3] E. Agliari, O. Mülken, A. Blumen, *Continuous-Time Quantum Walks and Trapping* (2009), arXiv:0903.3288.

[4] Q. Wang et al., *First Hitting Times on a Quantum Computer: Tracking vs. Local Monitoring, Topological Effects, and Dark States*, Entropy 26, 869 (2024), arXiv:2402.15843.
