# Flux-independent diffusive mixing on periodically dephased magnetic cycles

## Finding

Let \(n\ge3\), \(J,\tau>0\), \(\phi\in\mathbb R\), and let \(S|j\rangle=|j+1\pmod n\rangle\) on \(\mathbb C^n\). Set
\[
H_{n,\phi}=J(e^{i\phi/n}S+e^{-i\phi/n}S^\dagger),\qquad
Q_{n,\phi}(j,k)=|\langle j|e^{-i\tau H_{n,\phi}}|k\rangle|^2.
\]
Thus \(Q_{n,\phi}\) evolves a site distribution by coherent hopping for time \(\tau\) followed by complete, nonselective position dephasing. Write \(\delta_0\) for unit mass at zero, \(u_n\) for the uniform site distribution, and \(d_{\mathrm{TV}}(p,q)=\tfrac12\sum_j|p(j)-q(j)|\).

**Theorem.** Put \(x=J\tau\), \(m_n=\lceil n/2\rceil\), \(B_x=2e^x-1\), \(T_n=2e^x x^{m_n}/m_n!\), and let
\[
r_n(d)=\sum_{k\equiv d\pmod n}\mathrm J_k(2x)^2
\]
be the periodized Bessel-square probability law. For every \(n,J,\tau,\phi\) as above and integer \(t\ge0\),
\[
d_{\mathrm{TV}}\bigl(Q_{n,\phi}^{t}\delta_0,r_n^{*t}\bigr)
\le \min\{1,\ t(B_xT_n+T_n^2)\},\qquad r_n^{*0}=\delta_0.
\]
For fixed \(x>0\) this bound tends to zero faster than every inverse power of \(n\) when \(t=O(n^2)\), uniformly in \(\phi\).

For fixed \(x>0\) and \(s>0\), uniformly over \(\phi\in\mathbb R\),
\[
d_{\mathrm{TV}}\bigl(Q_{n,\phi}^{\lfloor sn^2\rfloor}\delta_0,u_n\bigr)
\ \longrightarrow\ F_x(s):=\frac12\int_0^1\left|K_x(s,y)-1\right|\,dy,
\qquad
K_x(s,y)=\sum_{h\in\mathbb Z}e^{-4\pi^2x^2sh^2}e^{2\pi i h y}.
\]
The profile is continuous and strictly decreasing from \(1\) to \(0\). For every \(\varepsilon\in(0,1)\), the \(\varepsilon\)-mixing time divided by \(n^2\) tends to the unique \(s_\varepsilon>0\) such that \(F_x(s_\varepsilon)=\varepsilon\), uniformly over the flux. There is no total-variation cutoff along any sequence of fluxes. The limiting diffusivity in the scaled time is \(x^2\).

## Assumptions and scope

Edges have equal nearest-neighbor hopping magnitudes and there are no onsite terms. The flux \(\phi\) is placed uniformly on the edges; it can vary arbitrarily with \(n\). The asymptotic mixing claims fix \(J,\tau>0\) as \(n\to\infty\). The time \(t\) counts complete coherent/dephasing cycles, of physical duration \(\tau\) each. Mixing is from a localized start; translation invariance makes all such starts equivalent. The uniform distribution is stationary by unitarity. A mixing time is the first step at which the distance is at most the specified threshold, with value infinity if this never occurs; the result only implies finiteness for sufficiently large \(n\) at each fixed threshold. The theorem does not cover a single monitored target, continuous environmental dephasing, inhomogeneous hopping, or coherent intervals that grow with \(n\).

## Proof

**1. Uniform comparison of the kernels.** The Fourier series of \(e^{-i2x\cos\theta}\) gives the exact winding expansion
\[
\langle d|e^{-i\tau H_{n,\phi}}|0\rangle
=\sum_{k\equiv d\pmod n}(-i)^k e^{ik\phi/n}\mathrm J_k(2x).
\]
By Parseval, \(\sum_k\mathrm J_k(2x)^2=1\), so \(r_n\) is a probability law. The Bessel integral representation gives \(|\mathrm J_k(2x)|\le x^{|k|}/|k|!\) for real \(x>0\). Consequently the total coefficient sum in absolute value is at most \(B_x\), and the sum for \(|k|\ge m_n\) is at most \(T_n\); the latter follows from \((m_n+j)!\ge m_n!j!\).

For each residue \(d\) choose a representative of minimum absolute value, resolving any tie arbitrarily. Let \(a_d\) be its term and \(b_d\) the sum of the remaining terms in the amplitude. Every remaining index has absolute value at least \(m_n\). Thus \(\sum_d|a_d|\le B_x\) and \(\sum_d|b_d|\le T_n\). At site \(d\), the difference between \(|a_d+b_d|^2\) and the sum of the individual squared magnitudes is bounded in absolute value by \(2|a_d||b_d|+|b_d|^2\) plus the sum of squared magnitudes of the omitted terms. The sums over sites of the two tail-square contributions are each at most \(T_n^2\). Dividing the resulting bound by two yields the one-step estimate. Both kernels are circulant, hence act by convolution. Telescoping their powers, and using contraction in total variation under either convolution, gives the announced estimate for \(t\) steps, including \(t=0\). Factorial decay at fixed \(x\) proves the asserted uniformity on the diffusive scale.

**2. The profile for the reference kernel.** The characteristic function of the Bessel-square law on \(\mathbb Z\) is
\[
\chi_x(\xi)=\sum_k\mathrm J_k(2x)^2e^{ik\xi}=\mathrm J_0(4x\sin(\xi/2)).
\]
Indeed the sum is the periodic correlation of \(e^{-i2x\cos\theta}\) with its translate by \(\xi\), and the cosine-difference identity reduces the integral to the displayed \(\mathrm J_0\). In particular \(\chi_x(\xi)=1-x^2\xi^2+O_x(\xi^4)\) near zero. The integral averaging phases for \(\mathrm J_0(z)\) has absolute value strictly less than one for real \(z\ne0\) because the phases are not constant. The expansion and compactness on the rest of the circle give a constant \(c_x>0\) such that \(1-|\chi_x(\xi)|\ge c_x\operatorname{dist}(\xi,2\pi\mathbb Z)^2\).

At \(t_n=\lfloor sn^2\rfloor\), the cyclic multiplier \(\chi_x(2\pi h/n)^{t_n}\) tends to \(e^{-4\pi^2x^2s h^2}\) for each fixed integer \(h\), by the expansion. For representatives \(-n/2<h\le n/2\) and sufficiently large \(n\), the bound on \(|\chi_x|\) and \(t_n\ge sn^2/2\) dominate those multipliers by \(e^{-c_{x,s}h^2}\) with \(c_{x,s}>0\). The dominance is summable even if some finite-size multipliers are negative. Extending the finite sequence by zero, dominated convergence in the Fourier sum gives
\[
\sup_{0\le j<n}|n r_n^{*t_n}(j)-K_x(s,j/n)|\longrightarrow0.
\]
The sign convention in inversion does not affect the expression since the coefficients are even. A Riemann sum yields the reference total-variation profile; Step 1 transfers it to \(Q_{n,\phi}\), uniformly in \(\phi\).

**3. Mixing and no cutoff.** The circle heat kernel \(K_x(s,\cdot)\) is continuous and strictly positive for \(s>0\), as is evident from its periodized Gaussian form. It integrates to one and is nonconstant because the first harmonic is nonzero. For a nonzero continuous mean-zero function, the strict positivity of any positive-time heat kernel makes convolution a strict \(L^1\) contraction: the positive and negative parts both contribute at every point. The heat semigroup identity therefore makes \(F_x\) strictly decreasing. Its continuity on positive times follows from the Fourier series on compact time intervals. As \(s\downarrow0\), the heat law concentrates on any fixed arc around zero; arcs of arbitrarily small uniform mass give \(F_x(s)\to1\). As \(s\to\infty\), all nonconstant Fourier modes tend uniformly to zero, giving \(F_x(s)\to0\). The Markov distance to stationarity is nonincreasing in step count. Evaluating the uniform profile at fixed times just below and just above \(s_\varepsilon\) therefore brackets the rescaled mixing times uniformly. For \(0<\varepsilon<1/2\), the ratio of the \(\varepsilon\)- and \((1-\varepsilon)\)-mixing times tends to \(s_\varepsilon/s_{1-\varepsilon}>1\); this rules out cutoff. \(\square\)

## Verification

The analytical proof covers all parameters in the theorem. The original `verify.py` (Python with NumPy and SciPy) contains bounded floating-point cross-checks of the matrix exponential, Bessel comparison and representative diffusion-scale distances, along with ancillary symmetry tests outside the theorem above. See `VERIFICATION.md` for the status and scope of these recorded checks.

## Relationship to prior work

Longhi [1, §2] already obtains the stochastic channel of transition probabilities under complete periodic dephasing and studies a three-site ring with unequal hopping. The channel itself is not new. The present theorem gives a uniform comparison at growing cycle sizes and the exact macroscopic total-variation profile for homogeneous magnetic hopping. The classical local-limit method applies to the reference kernel; the uniform winding-tail estimate is what transfers it to the magnetic quantum channel.

The fixed-total-time Zeno comparison in [2] uses the same fully dephased magnetic cycle but treats directionality as the coherent interval shrinks at fixed size. The microscopic odd-cycle coefficient is not part of the present theorem. Single-target stroboscopic first detection [3], continuous decoherence [4] and instantaneous or time-averaged coherent mixing [5] are different evolutions or observables and are not subsumed by the theorem.

## References

1. S. Longhi, *Dynamical Phase Transitions in Open Quantum Walks*, arXiv:2508.11947v1, https://arxiv.org/abs/2508.11947.
2. *Sharp parity-dependent Zeno suppression of magnetic-ring directionality*, SCOPE-20261026-6b103059d648, https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-sharp-parity-dependent-zeno-suppression-of-magnetic-ring-directi--6b103059d648/RESULT.md.
3. S. Finocchiaro et al., *Optimal quantum transport on a ring via locally monitored chiral quantum walks*, arXiv:2507.10669, https://arxiv.org/abs/2507.10669.
4. L. Fedichkin, D. Solenov and C. Tamon, *Mixing and Decoherence in Continuous-Time Quantum Walks on Cycles*, arXiv:quant-ph/0509163, https://arxiv.org/abs/quant-ph/0509163.
5. L. Levine et al., *Uniform Mixing in Chiral Quantum Walks*, arXiv:2605.04414, https://arxiv.org/abs/2605.04414.
