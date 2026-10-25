# Sharp inverse-square-root buckling susceptibility in a triangular active crystal

## Finding

Let \(A=U''(\ell)>0\), \(B=U'(\ell)/\ell\), and approach the stable-side pressure threshold through \(B=A(-1/3+\delta)\), \(\delta\downarrow0\). For the stationary two-dimensional triangular harmonic crystal with independent isotropic white and exponentially correlated site forcings of respective covariance strengths \(\Gamma^2\) and \(\nu^2\), and positive active decorrelation rate \(\mu\), let \(V_\delta\) denote the infinite-volume variance of the displacement difference across one nearest-neighbor bond. The sharp limit is

\[
\boxed{\lim_{\delta\downarrow0}\sqrt\delta\,V_\delta=\frac{2}{A}\sqrt{\frac23}\left(\frac{\Gamma^2}{2}+\frac{\nu^2}{\mu}\right).}
\]

A stronger mode-resolved statement explains this divergence. Write the Fourier-torus phases as \((k_1,k_2)\in(\mathbb R/2\pi\mathbb Z)^2\), with the measured bond in the first lattice direction. Let \(\mathsf D_\delta(k)\) be the two-by-two dynamical matrix defined below, and put

\[
F_\delta(k)=2(1-\cos k_1)\operatorname{tr}\!\left[\frac{\Gamma^2}{2}\mathsf D_\delta(k)^{-1}+\nu^2\mathsf D_\delta(k)^{-1}(\mathsf D_\delta(k)+\mu I)^{-1}\right].
\]

For **every** continuous function \(f\) on the Fourier torus,

\[
\boxed{\lim_{\delta\downarrow0}\sqrt\delta\int_{\mathbb T^2}\!f(k)F_\delta(k)\frac{dk_1dk_2}{(2\pi)^2}
=\frac{T_*}{A}\sqrt{\frac23}\left[\int_0^{2\pi}\!f(s,0)\frac{ds}{2\pi}+\int_0^{2\pi}\!f(s,s)\frac{ds}{2\pi}\right],}
\]

where \(T_*=\Gamma^2/2+\nu^2/\mu\). Therefore exactly two of the three symmetry-related lines of pressure-softened Fourier modes contribute at leading order to a given bond's variance. The third line, \(k_1=0\), is annihilated by the bond-difference factor. The two surviving line contributions are equal, each accounting for one half of the leading divergence.

## Assumptions and scope

For integers \(N\ge3\), let lattice sites be \(n\in(\mathbb Z/N\mathbb Z)^2\), with equilibrium positions \(\ell(n_1(1,0)+n_2(1/2,\sqrt3/2))\). Each site has two real displacement coordinates \(u_n(t)\), and interacts through the harmonic second-order expansion of a central pair potential \(U\) with its six nearest neighbors. Assume \(U\) is twice differentiable at \(\ell>0\), \(A=U''(\ell)>0\), and \(0<\delta<1/3\) with \(B=U'(\ell)/\ell=A(-1/3+\delta)\).

The overdamped dynamics is \(\dot u_n=-\sum_m \mathsf D_{nm}u_m+\xi_n+w_n\), where the independent mean-zero forcings obey

\[
\mathbb E[\xi_n(t)\xi_m(s)^\mathsf T]=\Gamma^2I\,\mathbf1_{n=m}\,\delta_{\rm Dirac}(t-s),\qquad
\mathbb E[w_n(t)w_m(s)^\mathsf T]=\nu^2 I\,\mathbf1_{n=m}e^{-\mu|t-s|}.
\]

Assume \(\Gamma,\nu\ge0\), \(\Gamma^2+\nu^2>0\), and \(\mu>0\). The temporal forcing may be Gaussian, but Gaussianity is not required for this second-moment theorem. Work at stationary time after removing the global translation mode, then take \(N\to\infty\) **before** \(\delta\downarrow0\). Set

\[
V_\delta=\lim_{N\to\infty}\lim_{t\to\infty}\mathbb E\left|u_n(t)-u_{n+(1,0)}(t)\right|^2.
\]

Use vectors \(e_1=(1,0)\), \(e_2=(1/2,\sqrt3/2)\), \(e_3=(-1/2,\sqrt3/2)\), and indices \(m_1=(1,0)\), \(m_2=(0,1)\), \(m_3=(-1,1)\). The Fourier matrix is explicitly

\[
\mathsf D_\delta(k)=2\sum_{j=1}^3\big(1-\cos(k\cdot m_j)\big)\left[BI+(A-B)e_je_j^\mathsf T\right].
\]

All eigenvalues at nonzero Fourier modes are positive for \(\delta>0\). At \(\delta=0\), nontranslation zero modes occur on three full reciprocal lines, so this statement does not assert a stationary law *at* the threshold.

## Proof

**1. Exact inverse matrix.** Set \(a=1-\cos k_1\), \(b=1-\cos k_2\), and \(c=1-\cos(k_2-k_1)\). The elementary trigonometric identity

\[
a^2+b^2+c^2-2(ab+bc+ca)=-2abc
\]

reduces the determinant and trace to

\[
\frac{\det\mathsf D_\delta}{A^2}=\frac83abc+4\delta(a^2+b^2+c^2)+3\delta^2(ab+bc+ca),\qquad
\frac{\operatorname{tr}\mathsf D_\delta}{A}=2(2/3+\delta)(a+b+c).
\]

All terms in the determinant are nonnegative, and for \(\delta>0\) it vanishes only at \(a=b=c=0\), the excluded translation mode. For each nonzero mode,

\[
\operatorname{tr}\mathsf D_\delta^{-1}=\frac1A\frac{2(2/3+\delta)(a+b+c)}{\frac83abc+4\delta(a^2+b^2+c^2)+3\delta^2(ab+bc+ca)}.
\]

**2. Stationary mode covariance.** The temporal exponential convolution gives, for every scalar damping eigenvalue \(\lambda>0\),

\[
C(\lambda)=\frac{\Gamma^2}{2\lambda}+\frac{\nu^2}{\lambda(\lambda+\mu)}
=\frac{T_*}{\lambda}-\frac{\nu^2/\mu}{\lambda+\mu}.
\]

Consequently \(V_\delta=(2\pi)^{-2}\int F_\delta(k)\,dk\). The second term in the last expression for \(C\) contributes a uniformly bounded amount to this integral because \(0\le2a\le4\) and the resolvent \((\mathsf D_\delta+\mu I)^{-1}\) has eigenvalues at most \(1/\mu\). Therefore it disappears after multiplication by \(\sqrt\delta\). The same holds with any bounded test function \(f\).

**3. Two contributing soft lines.** Away from the origin on \(k_2=0\), fix \(k_1=s\not\equiv0\), and write \(k_2=t\) near zero. With \(q=1-\cos s>0\), the exact determinant and trace yield the local singular kernel

\[
2a\operatorname{tr}\mathsf D_\delta^{-1}\sim\frac{4}{A(t^2+6\delta)}
\]

in the scaling \(t=\sqrt\delta\,z\) as \(\delta\downarrow0\), uniformly for \(s\) in compact sets away from zero and for bounded \(z\). Indeed \(b\sim t^2/2\), \(a,c\to q\), \(\det(\mathsf D_\delta/A)\sim(4/3)q^2(t^2+6\delta)\), and \(\operatorname{tr}(\mathsf D_\delta/A)\to(8/3)q\). Since \(\int_{\mathbb R}dt/(t^2+6\delta)=\pi/\sqrt{6\delta}\), this line contributes the normalized arclength measure multiplied by \(T_*\sqrt{2/3}/A\). The line \(k_2=k_1\) gives the identical contribution by sixfold symmetry.

For \(k_1=0\) away from the origin, the factor \(2a=O(k_1^2)\) cancels the soft-line singularity, so this line contributes zero to the rescaled limit. Away from all three lines the integrand is uniformly bounded.

**4. Uniform treatment of the line intersection.** In a small radius-\(\eta\) disk around the torus origin, write \(k=r(\cos\theta,\sin\theta)\). The determinant formula and \(a,b,c\) quadratic in their respective linear phases imply, with constants uniform for small \(r\),

\[
0\le 2a\operatorname{tr}\mathsf D_\delta^{-1}\le\frac{C}{\delta+r^2g(\theta)},\quad
g(\theta)=\cos^2\theta\,\sin^2\theta\,(\sin\theta-\cos\theta)^2.
\]

The finitely many angular zeros of \(g\) are quadratic. Splitting \(r\le\sqrt\delta\) from \(r>\sqrt\delta\) and integrating in polar coordinates gives

\[
\sqrt\delta\int_{r<\eta}2a\operatorname{tr}\mathsf D_\delta^{-1}\,d^2k\le C(\eta+\sqrt\delta).
\]

Thus the line crossing carries no extra limiting mass. On the complement of this small disk, ordinary dominated convergence after the substitution \(t=\sqrt\delta\,z\) and the integrable bound \(C/(1+z^2)\) complete the weak convergence for every continuous \(f\). Taking \(f\equiv1\) gives the stated scalar limit. This proves both the coefficient and the equal-line decomposition.

## Verification

A standalone standard-library script `verify.py` checks the cosine identity, the exact determinant and inverse-trace formulas at 600 deterministic pseudorandom Fourier points (1,800 algebraic/numeric assertions), together with 8 midpoint-quadrature checks at two small positive pressure gaps. The script's 1,808 tests pass. For \(A=T_*=1\) with purely white forcing, numerical quadrature gives \(\sqrt\delta V_\delta\approx1.547708309\) at \(\delta=10^{-3}\), and \(\approx1.604868226\) at \(\delta=10^{-4}\), approaching the analytical coefficient \(2\sqrt{2/3}\approx1.632993162\). These finite diagnostics do not prove the singular-limit theorem; its proof is given above.

## Relationship to prior work

Roberts and Pruessner (2025 preprint; 2026 journal paper) derive the full Fourier covariance and the bond-variance Brillouin-zone integral (their Eq. 87–88), identify the threshold \(B/A=-1/3\), and establish that complete families of Fourier modes soften at the threshold (Appendix A.1.2). None of those source statements is claimed here as new. The present assertion is the *pressure-to-threshold asymptotic measure*—the exact coefficient and its equal weight on the two mode families surviving the measured bond filter—which requires a singular analysis of the known integrand. Shi, Cheng and Chaté (2023) analyze effective elastic temperatures and large deformations in active crystals, while Maire and Plati (2024) analyze fluctuation-induced order in a different dual-bath harmonic solid; neither comparison supplies this specific prestressed triangular-lattice critical measure in its inspected material.

## Limitations

The order of limits matters: thermodynamic volume first, stable-side pressure gap second. No uniform joint finite-size/pressure limit, nonlinear post-buckling behavior, physically exact melting criterion, or results for spatially correlated active forcing are asserted. The harmonic approximation loses self-consistency before arbitrarily large predicted displacements can be physically realized. The coefficient describes its *formal stationary linear response* within the stable region. Exact prior integral representations make the present asymptotic mathematically derivable; a broader unstated spectral-singularity theorem might also imply it, so independent originality validation remains necessary.

## References

1. C. Roberts and G. Pruessner, *Exact results and instabilities in the harmonic approximation of active crystals*, arXiv:2512.01539 (first public 2025-12-01), and *Journal of Chemical Physics* 164 (2026), 134108, DOI:10.1063/5.0314725. https://arxiv.org/abs/2512.01539
2. X.-q. Shi, F. Cheng and H. Chaté, *Extreme Spontaneous Deformations of Active Crystals*, arXiv:2309.04212 (2023). https://arxiv.org/abs/2309.04212
3. R. Maire and A. Plati, *Enhancing (quasi-)long-range order in a two-dimensional driven crystal*, arXiv:2405.05621 (2024). https://arxiv.org/pdf/2405.05621
