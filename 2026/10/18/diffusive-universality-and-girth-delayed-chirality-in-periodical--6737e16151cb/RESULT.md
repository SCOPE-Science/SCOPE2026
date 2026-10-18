# Diffusive universality and girth-delayed chirality in periodically dephased magnetic cycles

## Finding
Let \(n\geq 3\), \(J>0\), \(\tau>0\), and \(\phi\in\mathbb R\). On the cyclic site Hilbert space \(\mathbb C^n\), let \(S|j\rangle=|j+1\pmod n\rangle\), and define
\[
H_{n,\phi}=J(e^{i\phi/n}S+e^{-i\phi/n}S^\dagger),\qquad
U_{n,\phi}=e^{-i\tau H_{n,\phi}},\qquad
Q_{n,\phi}(j,k)=|\langle j|U_{n,\phi}|k\rangle|^2.
\]
The stochastic evolution \(Q_{n,\phi}\) is the repeated process of coherent hopping for time \(\tau\), followed by **complete site-basis dephasing**. Let \(\delta_0\) be the point mass at site zero, \(u_n\) the uniform distribution, and \(d_{\mathrm{TV}}(p,q)=\frac12\sum_j|p(j)-q(j)|\).

**Quantitative flux erasure.** Put \(x=J\tau\), \(m_n=\lceil n/2\rceil\), \(B_x=2e^x-1\), and \(T_n=2e^x x^{m_n}/m_n!\). The flux-independent cyclic distribution
\[
r_n(d)=\sum_{\substack{k\in\mathbb Z\\k\equiv d\pmod n}}\mathrm J_k(2x)^2
\]
(using the ordinary Bessel function \(\mathrm J_k\)) obeys, for every \(n\ge3\), every real flux \(\phi\), and every integer \(t\ge0\),
\[
d_{\mathrm{TV}}(Q_{n,\phi}^{t}\delta_0,r_n^{*t})\le
\min\{1,\;t(B_x T_n+T_n^2)\}.
\]
Here the zero-fold convolution is \(\delta_0\). In particular, for fixed \(J\tau>0\), the right side vanishes faster than any inverse power of \(n\) when \(t=O(n^2)\), uniformly over arbitrary flux sequences \(\phi=\phi_n\).

**Exact mixing profile.** Define for \(s>0\)
\[
F_x(s)=\frac12\int_0^1\left|
\sum_{\ell\in\mathbb Z}e^{-4\pi^2 x^2s\ell^2}e^{2\pi i\ell y}-1
\right|\,dy.
\]
Then for any fixed \(s>0\) and every sequence of fluxes \(\phi_n\),
\[
\lim_{n\to\infty}d_{\mathrm{TV}}
\bigl(Q_{n,\phi_n}^{\lfloor s n^2\rfloor}\delta_0,u_n\bigr)=F_x(s).
\]
The function \(F_x\) decreases continuously and strictly from \(1\) at \(s\downarrow0\) to \(0\) at \(s\to\infty\). Consequently, for every fixed \(\varepsilon\in(0,1)\), the total-variation mixing time from any initial localized site satisfies \(t_{\mathrm{mix}}(\varepsilon)/n^2\to s_\varepsilon\), with \(F_x(s_\varepsilon)=\varepsilon\). There is **no total-variation cutoff** in this fixed-interval homogeneous-ring family. The profile, the diffusivity \(J^2\tau^2\) per dephasing step, and the leading mixing times are flux-independent.

**Odd-girth onset of chirality.** If \(n\) is even, \(Q_{n,\phi}=Q_{n,\phi}^{\mathsf T}\) for all \(\tau\) and \(\phi\). If \(n=2r+1\) is odd and the flux \(\phi\) is fixed, then, as \(\tau\downarrow0\),
\[
Q_{n,\phi}(1,0)-Q_{n,\phi}(0,1)
=\frac{4(-1)^r J^n\sin\phi}{(n-1)!}\tau^n
+O_{n,J,\phi}(\tau^{n+2}).
\]
Thus the first possible flux-induced forward/backward imbalance occurs at the odd-girth order \(n\), and its coefficient is nonzero whenever \(\sin\phi\ne0\). A uniform bound for any pair of sites is
\[
|Q_{n,\phi}(j,k)-Q_{n,\phi}(k,j)|
\le 2e^{4J\tau}(4J\tau)^n/n!\qquad(n\text{ odd}).
\]
The even-cycle transition-symmetry conclusion is established prior knowledge, stated here for completeness and not claimed as a new result.

## Assumptions and scope
The coherent Hamiltonian has equal nearest-neighbor hopping magnitudes and no onsite energies. The full gauge flux \(\phi\) is spread evenly over the \(n\) directed edges, a gauge-equivalent choice. The same positive \(J\) and \(\tau\) are fixed as \(n\to\infty\). Complete position dephasing takes place after each coherent interval; it is not local monitoring at one target, and it is not continuous Lindblad dephasing. The Markov chain acts on site occupation probabilities after the first measurement. The flux \(\phi_n\) may vary arbitrarily with size. Mixing is in total variation from a localized state, equivalently from any single site by translation invariance. The time \(t\) counts complete coherent/dephasing cycles, so physical elapsed time is \(t\tau\).

## Proof
**1. Exact amplitudes and a factorial tail.** Fourier diagonalization of the cyclic shift, or the Jacobi–Anger expansion, gives the exact winding-number representation
\[
\langle d|U_{n,\phi}|0\rangle
=\sum_{k\equiv d\ (\mathrm{mod}\ n)}(-i)^k e^{ik\phi/n}\mathrm J_k(2J\tau).
\]
For real \(z\) and every integer \(k\), the standard integral representation for Bessel functions yields \(|\mathrm J_k(2x)|\le x^{|k|}/|k|!\). Hence
\[
\sum_{k\in\mathbb Z}|\mathrm J_k(2x)|\le B_x,
\qquad
\sum_{|k|\ge m}|\mathrm J_k(2x)|\le 2e^x x^m/m!.
\]
In each residue class modulo \(n\), choose at most one representative \(k_d\) with \(|k_d|<n/2\); for a boundary tie use any one. Split its amplitude into a central term \(a_d\) and the sum \(b_d\) of the other winding terms. The omitted winding terms all satisfy \(|k|\ge\lceil n/2\rceil\), so \(\sum_d |a_d|\le B_x\) and \(\sum_d|b_d|\le T_n\). The reference probability is the sum of individual winding squares, rather than their coherent square. Summing
\[
\bigl||a_d+b_d|^2-
 (|a_d|^2+\sum_{k\equiv d,\ k\ne k_d}|\mathrm J_k(2x)|^2)\bigr|
\le 2|a_d||b_d|+|b_d|^2+
\sum_{k\equiv d,\ k\ne k_d}|\mathrm J_k(2x)|^2
\]
and dividing by two gives \(d_{\mathrm{TV}}(Q\delta_0,r_n)\le B_xT_n+T_n^2\). Both kernels are circulant; convolution and Markov contraction yield the claimed \(t\)-step telescoping bound. The factorial decay beats every power for \(t=O(n^2)\). No small-flux approximation enters.

**2. Characteristic function and local-limit theorem.** The Bessel identity
\[
\sum_{k\in\mathbb Z}\mathrm J_k(2x)^2e^{ik\xi}
=\mathrm J_0(4x\sin(\xi/2))
\]
implies that the cyclic Fourier multiplier of \(r_n\) at frequency \(h\) is \(\chi_x(2\pi h/n)\), with \(\chi_x(\xi)=\mathrm J_0(4x\sin(\xi/2))\). For fixed \(x>0\),
\[
\chi_x(\xi)=1-x^2\xi^2+O_x(\xi^4),
\qquad |\chi_x(\xi)|<1\quad(\xi\notin2\pi\mathbb Z).
\]
Indeed \(|\mathrm J_0(z)|<1\) for every real \(z\ne0\). Compactness and the quadratic expansion give \(1-|\chi_x(\xi)|\ge c_x\operatorname{dist}(\xi,2\pi\mathbb Z)^2\) for some \(c_x>0\). With \(t_n=\lfloor sn^2\rfloor\), the Fourier coefficient at each fixed integer frequency converges to \(e^{-4\pi^2x^2s h^2}\), and the inequality gives a summable \(e^{-c_{x,s}h^2}\) domination for frequencies represented in \((-n/2,n/2]\). Fourier inversion therefore yields uniform convergence of the scaled site probabilities \(n r_n^{*t_n}(j)\) to the circle heat kernel at \(j/n\). Riemann sums imply the stated total-variation limit; the flux error from part 1 tends to zero uniformly.

The heat kernel is positive, smooth, and not spatially constant for finite \(s>0\). Its convolution with any positive-time heat kernel strictly contracts the \(L^1\) norm of a nonzero continuous mean-zero function, by strict positivity and sign change. Hence \(F_x(s)\) strictly decreases. Weak convergence to a point mass as \(s\downarrow0\) gives the TV limit \(1\), while exponential decay of nonzero Fourier modes gives limit \(0\). The standard mixing-time consequences and absence of cutoff follow from this non-step-shaped limiting profile. Translation invariance makes the localized-start mixing time independent of the chosen initial vertex.

**3. Chirality and odd girth.** On an even cycle the alternating-sign unitary \(\Gamma\) obeys \(\Gamma H\Gamma=-H\), so \(\Gamma U(\tau)\Gamma=U(-\tau)=U(\tau)^\dagger\). Consequently \(|U_{jk}|=|U_{kj}|\) for every \(j,k\), proving exact transition symmetry. This well-known bipartite chiral-walk fact is included only to frame the odd-cycle contrast.

For an odd cycle \(n=2r+1\), the series for a transition probability has terms of total degree \(a+b\) in \(\tau\), formed from a forward length-\(a\) path and a reversed length-\(b\) path. Any flux-sensitive antisymmetry between \(j\to k\) and \(k\to j\) requires an odd closed walk in their concatenation. Every odd closed walk has length at least \(n\), so all coefficients of total degree below \(n\) cancel. The coefficient of degree \(n\) for adjacent sites comes from interference between the single forward hop and the unique reverse path of length \(n-1\), and its conjugate pair. Evaluating their phases and powers of \(-i\) yields \(4(-1)^rJ^n\sin\phi/(n-1)!\). Transition-probability antisymmetry is an odd function of real \(\tau\): for Hermitian \(H\), \(|U_{jk}(-\tau)|^2=|U_{kj}(\tau)|^2\), so the next possible term has order \(n+2\).

For the uniform inequality, each coefficient of degree \(q\) in an entry of \(|e^{-i\tau H}|^2\) is bounded by \((4J)^q/q!\), since \(\|H\|\le2J\). The difference of reversed entries has no contributions below order \(n\), hence its absolute value is bounded by \(2\sum_{q\ge n}(4J\tau)^q/q!\le 2e^{4J\tau}(4J\tau)^n/n!\).

## Verification
The standalone file `verify.py` uses NumPy/SciPy to form the full Hamiltonian and matrix exponential directly for eleven cycle sizes, multiple fluxes and dephasing intervals. It checks stochasticity, circulant structure, Bessel periodization, a conservative flux-erasure bound, parity/girth onset, and representative diffusive-time mixing profiles against the circle heat kernel. Running `python verify.py` produced `VERIFY_OK 702 finite identities and mixing comparisons`. These finite computations do not constitute an infinite-size proof, which is given above.

## Relationship to prior work
Longhi, *Dynamical Phase Transitions in Open Quantum Walks* (arXiv:2508.11947, first publicly posted 16 August 2025), derives the periodically dephased Markov matrix and demonstrates spectral dynamical transitions in a three-site gauge-flux model with unequal hopping strengths. The complete homogeneous ring's uniform-in-flux diffusive scaling, exact total-variation heat profile, quantitative factorial error, and odd-girth first chirality coefficient are not stated there.

Zimborás and collaborators (2013) establish gauge-phase invariance and exact transition symmetry on bipartite networks, as well as directional effects on odd cycles; the even-cycle symmetry is **prior work**, not the novelty claimed here. Finocchiaro and collaborators (arXiv:2507.10669) study the same type of magnetic ring under **single-target stroboscopic monitoring**, whose non-unitary first-detection map and nearly cubic first-detection times differ from our full-site dephasing kernel and diffusive total-variation mixing. Levine and collaborators (arXiv:2605.04414) study instantaneous/averaged **unmeasured** chiral quantum-walk uniformity, not repeated complete dephasing. Fedichkin, Solenov, and Tamon (arXiv:quant-ph/0509163) study continuously decohering walks on cycles, a different generator.

Classical circle heat-kernel mixing, Bessel identities, and Fourier local-limit methods are standard ingredients. The claim is the precise flux-uniform bridge from a periodically **fully dephased magnetic quantum ring** to this diffusion law together with a quantitative odd-girth suppression of its microscopic chirality. Mathematical publication priority remains subject to independent scrutiny.

## Limitations
The theorem requires homogeneous nearest-neighbor hopping, fixed positive dephasing interval and full site-basis measurement, with no defects or localized sinks. Flux erasure is asymptotic as system size grows at fixed coherent interval; it does not assert exact flux independence at finite odd size, and does not cover intervals growing with size, finite-strength dephasing, multi-particle walks, or target-only detection. The small-time chirality coefficient is an asymptotic at each fixed odd \(n\), with an implicit remainder constant depending on \(n,J,\phi\). The result does not claim experimentally verified or independently certified novelty. Under the full dephasing model the homogeneous circulant kernel is normal, so its spectral behavior need not exhibit the exceptional points found in anisotropic small networks.

## References
1. S. Longhi, *Dynamical Phase Transitions in Open Quantum Walks*, arXiv:2508.11947v1 (16 August 2025), https://arxiv.org/abs/2508.11947 .
2. Z. Zimborás, M. Faccin, Z. Kádár, J. D. Whitfield, B. P. Lanyon, J. Biamonte, *Quantum Transport Enhancement by Time-Reversal Symmetry Breaking*, Scientific Reports **3**, 2361 (2013), https://doi.org/10.1038/srep02361 .
3. S. Finocchiaro, G. O. Luilli, G. Benenti, M. G. A. Paris, L. Razzoli, *Optimal quantum transport on a ring via locally monitored chiral quantum walks*, arXiv:2507.10669 (2025), https://arxiv.org/abs/2507.10669 .
4. L. Levine, J. J. Mesapam, B. Mustico, C. Tamon, G. Tucker, H. Zhan, *Uniform Mixing in Chiral Quantum Walks*, arXiv:2605.04414 (2026), https://arxiv.org/abs/2605.04414 .
5. L. Fedichkin, D. Solenov, C. Tamon, *Mixing and Decoherence in Continuous-Time Quantum Walks on Cycles*, arXiv:quant-ph/0509163, https://arxiv.org/abs/quant-ph/0509163 .
