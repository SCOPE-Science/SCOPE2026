# Universal curvature-contrast correction for rapid stochastic return in confining diffusions

## Finding
Consider a one-dimensional search alternating between two overdamped diffusions. In the search phase it follows \(dX_t=b_1(X_t)\,dt+\sqrt{2}\,dB_t\), starting at zero. It stops successfully on reaching the target \(1\), or at an independent exponential clock of rate \(r\) switches *without moving its position* to the return diffusion \(dX_t=b_2(X_t)\,dt+\sqrt{2}\,dB_t\). During return, reaching \(1\) succeeds and reaching \(0\) restarts a fresh search phase. The return phase has no resetting clock.

Suppose \(b_1,b_2\) are odd \(C^5\) functions, globally Lipschitz with bounded derivatives through order five, and both are strictly mean-reverting outside a compact interval: for each \(j\), \(xb_j(x)\le-c_jx^2\) whenever \(|x|\ge R_j\), with \(c_j,R_j>0\). Let \(M_r\) denote the overall mean target time, and let \(m_2(0)\) denote the mean target time for the uninterrupted return diffusion started at zero. Put
\[
S_2=\int_0^1\exp\!\left(-\int_0^z b_2(y)\,dy\right)dz.
\]
Then the **sharp high-reset correction** is
\[
\boxed{M_r=m_2(0)+4\bigl(b_2'(0)-b_1'(0)\bigr)S_2\,r^{-3/2}+O(r^{-5/2}).}
\]
If the two local slopes differ, the sign of \(M_r-m_2(0)\) is eventually the sign of \(b_2'(0)-b_1'(0)\). If the two drifts agree everywhere, \(M_r=m_2(0)\) *exactly for every* \(r>0\). The leading coefficient depends on the return dynamics through its scale integral \(S_2\), but on the search dynamics only through its derivative at the resetting point.

This is a theorem about the correction to a known return-dominated limit, **not a novelty claim for that limiting value itself**.

## Assumptions and scope
All stochastic processes are real-valued strong solutions of their SDEs, with independent standard Brownian driving noise restarted at each renewal and independent exponential search clocks. No instantaneous jump of position occurs when the clock initiates return. The clock operates only during search; in return, the first hit of zero or one ends the phase. The target remains active in both phases. The leading asymptotic is pointwise for each fixed pair of drifts satisfying the stated smoothness and confinement assumptions; no uniformity over drift families is claimed. The diffusion coefficient is normalized to one, so the Brownian noise amplitude is \(\sqrt2\). The mean is finite for every \(r>0\).

For a transparent nonlinear subfamily, take \(b_j(x)=-k_jx-c_j\tanh x\), with \(k_j>0\), \(c_j\ge0\). Then
\[
S_2=\int_0^1 e^{k_2z^2/2}(\cosh z)^{c_2}\,dz
\]
and the coefficient becomes \(4[(k_1+c_1)-(k_2+c_2)]S_2\). Harmonic potentials are the special cases \(c_1=c_2=0\).

## Proof
Write \(T=\inf\{t\ge0:X_t=1\}\) for the search diffusion started at zero and \(R\sim\operatorname{Exp}(r)\), independent of it. For the return generator \(L_2=\partial_x^2+b_2(x)\partial_x\), let \(u(x)=\mathbb E_x^{(2)}T_1\), where \(T_1\) is the first hitting time of one *without switching*. The standard scale/speed solution of \(L_2u=-1\), \(u(1)=0\), gives
\[
J_2(x)=\exp\!\left(\int_0^xb_2(y)\,dy\right),\quad
u'(x)=-\frac{\int_{-\infty}^xJ_2(y)\,dy}{J_2(x)},\quad
u(0)=\int_0^1\frac{\int_{-\infty}^zJ_2(y)\,dy}{J_2(z)}\,dz.
\]
The confinement conditions guarantee finiteness and justify the stopped expectations. As \(b_2(0)=0\), the equation gives \(u''(0)=-1\).

Let \(h(x)\) be the probability that the return diffusion started at \(x<1\) hits one before zero. It is zero for \(x\le0\), and for \(0<x<1\) is
\[
h(x)=\frac{1}{S_2}\int_0^x J_2(y)^{-1}\,dy.
\]
For \(v(x)=\mathbb E_x^{(2)}[T_{\{0,1\}}]\), the strong Markov property implies \(u(x)=v(x)+(1-h(x))u(0)\) for every \(x<1\); on the negative half-line the return first reaches zero. The probability that one full search-return cycle succeeds is
\[
p_r=\mathbb P(T<R)+\mathbb E[\mathbf1_{\{R<T\}}h(X_R)]>0.
\]
The renewal equation for the mean is
\[
M_r=\frac{\mathbb E(T\wedge R)+\mathbb E[\mathbf1_{\{R<T\}}v(X_R)]}{p_r}.
\]
Apply Dynkin's identity to the return-only mean \(u\), but along the search trajectory stopped at \(T\wedge R\). As \(L_1u=-1+(b_1-b_2)u'\) and \(u(1)=0\), cancellation with the renewal identity gives the **exact all-rate relation**
\[
M_r-u(0)=\frac{\mathbb E\!\left[\int_0^{T\wedge R}(b_1-b_2)(X_t)u'(X_t)\,dt\right]}{p_r}.
\]
In particular it vanishes identically if \(b_1=b_2\).

For the asymptotics, oddness and global Lipschitz continuity imply symmetry of the unrestricted search law and small-time bounds \(\mathbb E[X_t^2]=2t+O(t^2)\), \(\mathbb E|X_t|^4=O(t^2)\), and \(\mathbb E(X_t)^+=\sqrt{t/\pi}+O(t^{3/2})\). A Gronwall/reflection estimate gives \(\mathbb P(T\le t)\le C e^{-c/t}\) for sufficiently small \(t\). Consequently, replacing the stopped short-time expectations by unrestricted ones produces errors exponentially small in \(\sqrt r\).

Near zero, \(h(x)=x/S_2+O(x^3)\) for positive \(x\), hence averaging the reset-time endpoint distribution yields
\[
p_r=\frac{1}{2S_2\sqrt r}+O(r^{-3/2}).
\]
With \(\delta=b_1'(0)-b_2'(0)\), odd Taylor expansions and \(u''(0)=-1\) give
\[
(b_1-b_2)(x)u'(x)=\delta u'(0)x-\delta x^2+C_3x^3+O(x^4).
\]
The odd moments vanish for the unrestricted symmetric search law. Thus, since \(\int_0^\infty e^{-rt}(2t+O(t^2))\,dt=2r^{-2}+O(r^{-3})\),
\[
\mathbb E\!\left[\int_0^{T\wedge R}(b_1-b_2)(X_t)u'(X_t)\,dt\right]=-2\delta r^{-2}+O(r^{-3}).
\]
Divide this by the positive expression for \(p_r\), obtaining \(-4\delta S_2r^{-3/2}+O(r^{-5/2})\), as claimed. Localization to a fixed neighborhood of zero and the dissipativity assumptions control the Taylor remainder; the exponentially rare early hit and large displacement tails are smaller than every power of \(r^{-1}\).

## Verification
The accompanying `verify.py` is an independent finite-difference and quadrature consistency test for the exact renewal-resolvent identity. It solves two killed elliptic resolvent equations on a mesh, one for the cycle success probability and one for the drift-discrepancy integral. It checks nonlinear hyperbolic-tangent drifts with both correction signs and the equal-drift identity, over multiple rates. Run `python verify.py` using Python 3 with NumPy and SciPy installed. Its finite numerical checks support the formulas but do not prove the infinite-parameter theorem; the proof is analytic above.

## Relationship to prior work
Dubey and Pal, arXiv:2610.18814 (first submitted 13 October 2026), establish a renewal expression for mean first passage with *two harmonic* search/return traps and target detection during return. Frydel, arXiv:2511.14646 (first submitted 18 November 2025), already identifies the finite high-reset return-only mean in a free-search/harmonic-return protocol, and derives its explicit integral. Biswas, Dubey, Kundu and Pal, arXiv:2406.08975, develop target-active stochastic return with a linear return potential. Those facts are credited, not claimed as discoveries. The present statement is the sharp \(r^{-3/2}\) approach coefficient for **arbitrary smooth odd strongly confining pairs of search/return drifts**, a structural extension not directly supplied by the harmonic formula or the previously identified limiting plateau. Exact general renewal identities alone do not state this asymptotic rate or its local-versus-global dependence.

## Limitations
The theorem does not claim a universal correction when drifts are asymmetric, non-smooth, or the search and return diffusivities differ. The coefficient can vanish for unequal drifts having equal slopes at zero; in that case no nonzero next-order law is asserted. The result concerns the mean target time, not the full first-passage distribution or optimization over all reset rates. The high-rate plateau is known in a special harmonic setting, and no novelty is claimed for it. A priority risk remains because the full text of the 2026 motivating paper could not be retrieved for every section; a general uncatalogued diffusion-asymptotic theorem could also contain this expansion. No independent scientific audit has been performed.

## References
- A. Dubey and A. Pal, *Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols*, arXiv:2610.18814 (submitted 2026-10-13), https://arxiv.org/abs/2610.18814 .
- D. Frydel, *Search by Return: Stochastic Resetting in Fluctuating Harmonic Potentials*, arXiv:2511.14646 (submitted 2025-11-18), https://arxiv.org/abs/2511.14646 .
- A. Biswas, A. Dubey, A. Kundu and A. Pal, *Drift-diffusive resetting search process with stochastic returns: Speedup beyond optimal instantaneous return*, arXiv:2406.08975 (submitted 2024-06-13), https://arxiv.org/abs/2406.08975 .
- S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, Physical Review E 108, 024114 (2023), https://doi.org/10.1103/PhysRevE.108.024114 .
