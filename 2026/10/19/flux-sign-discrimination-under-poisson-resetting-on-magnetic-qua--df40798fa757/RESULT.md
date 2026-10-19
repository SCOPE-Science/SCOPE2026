# Flux-sign discrimination under Poisson resetting on magnetic quantum cycles

## Finding

Let \(N\ge3\) and let a one-particle continuous-time quantum walk on a magnetic \(N\)-cycle have uniform hopping \(J>0\), total oriented magnetic flux \(\phi\), and Poissonian resets to vertex zero at rate \(r>0\). Write \(p_j(r,\phi)\) for its stationary occupation probability at vertex \(j\).

**Exact even-cycle obstruction.** For every even \(N\), every \(r,J,\phi\), and every vertex \(j\),
\[
p_j(r,\phi)=p_j(r,-\phi).
\]
Thus stationary site occupations cannot distinguish the two signs of magnetic flux on an even cycle, at any reset rate.

**Sharp odd-cycle discrimination.** For odd \(N=2m+1\), every \(j\in\{1,\ldots,N-1\}\), and fixed \(N\), as \(J/r\to0^+\), uniformly in real \(\phi\),
\[
p_j(r,\phi)-p_j(r,-\phi)
=4(-1)^{m+j+1}\binom Nj\sin\phi\,\left(\frac Jr\right)^N
+O_N\!\left(\left(\frac Jr\right)^{N+2}\right).
\]
The reset-site probability satisfies \(p_0(r,\phi)=p_0(r,-\phi)\) exactly for every \(N\) and every rate. Consequently, for every odd \(N\), the total-variation distance between stationary position distributions has the sharp asymptotic
\[
\frac12\sum_{j=0}^{N-1}|p_j(r,\phi)-p_j(r,-\phi)|
=2(2^N-2)|\sin\phi|\left(\frac Jr\right)^N
+O_N\!\left(\left(\frac Jr\right)^{N+2}\right).
\]
When \(\sin\phi\ne0\), the leading coefficient is strictly positive. At \(\phi\in\pi\mathbb Z\) the two flux signs are gauge-equivalent, so their stationary position distributions agree exactly for all \(N,r\).

## Assumptions and scope

Use vertex indices modulo \(N\), with orthonormal basis \(|k\rangle\) and the Hermitian nearest-neighbor Hamiltonian
\[
H_\phi|k\rangle=J e^{i\phi/N}|k+1\rangle+J e^{-i\phi/N}|k-1\rangle.
\]
(The two neighbors are distinct since \(N\ge3\).) Between reset events the particle evolves unitarily; every independent rate-\(r\) reset places it in \(P_0=|0\rangle\langle0|\), without additional dephasing. The stationary density is
\[
\rho_{r,\phi}=r\int_0^\infty e^{-rt}e^{-itH_\phi}P_0e^{itH_\phi}\,dt,
\qquad p_j(r,\phi)=\langle j|\rho_{r,\phi}|j\rangle.
\]
This density is the unique solution of \(0=-i[H_\phi,\rho]+r(P_0-\rho)\). All asymptotics hold for fixed \(N\) as \(J/r\to0\); no claim of uniformity in \(N\) is made.

## Proof

**1. Stationarity.** The reset semigroup solves \(\dot\rho=-i[H_\phi,\rho]+r(P_0-\rho)\). Its stable resolvent yields the integral above. Exponential contraction of the homogeneous evolution by \(e^{-rt}\) makes the stationary state unique, trace one, and positive.

**2. Even-cycle symmetry.** For even \(N\), define the diagonal involution \(\Gamma|j\rangle=(-1)^j|j\rangle\). Bipartiteness gives \(\Gamma H_\phi\Gamma=-H_\phi\); complex conjugation gives \(\overline{H_\phi}=H_{-\phi}\). Consequently,
\[
e^{-itH_{-\phi}}=\Gamma\,\overline{e^{-itH_\phi}}\,\Gamma.
\]
The \(j,0\) matrix elements therefore have equal moduli at every time, and exponential averaging preserves the equality.

**3. A fixed-basepoint reflection.** Reflection \(R|j\rangle=|-j\rangle\) satisfies \(RH_\phi R^*=H_{-\phi}\) and fixes \(|0\rangle\). The return amplitude to zero and hence its probability are even in \(\phi\), proving \(p_0(r,\phi)=p_0(r,-\phi)\) for all \(N\).

**4. Oppositely wound minimal paths.** Apply the diagonal gauge \(G|j\rangle=e^{ij\phi/N}|j\rangle\). The equivalent Hamiltonian \(G^*H_\phi G\) has real hopping \(J\) along edges \(0\leftrightarrow1,\ldots,N-2\leftrightarrow N-1\), while its closing edge carries the total flux. At \(j\ne0\), the two simple directed paths from zero to \(j\) have lengths \(j\) and \(N-j\), and relative phase \(e^{i\phi}\). Expand
\[
\langle j|e^{-itH_\phi}|0\rangle
=\sum_{\ell\ge0}\frac{(-it)^\ell}{\ell!}\langle j|H_\phi^\ell|0\rangle.
\]
Any pair of paths with distinct net winding has total length at least \(N\). Equality is attained only by this pair of simple paths. Any such pair of larger total length has total length at least \(N+2\), since backtracking contributes two edges; pairs with winding difference of absolute value at least two have total length at least \(2N\), which is no smaller than \(N+2\) for \(N\ge3\). Therefore the leading flux-odd part of the time-dependent probability is the interference of just those two paths. With \(N=2m+1\), its difference under sign reversal is
\[
|\langle j|e^{-itH_\phi}|0\rangle|^2
-|\langle j|e^{-itH_{-\phi}}|0\rangle|^2
=\frac{4(-1)^{m+j+1}J^N}{j!(N-j)!}\sin\phi\,t^N
+O_N((Jt)^{N+2}).
\]
The sign follows directly from \(\operatorname{Re}((-1)^j i^N e^{i\phi})=(-1)^{m+j+1}\sin\phi\).

**5. Controlled exponential averaging.** The expansion of \(\rho_{r,\phi}=\left(1+i\operatorname{ad}_{H_\phi}/r\right)^{-1}P_0\) is absolutely convergent in operator norm when \(r>4J\), since \(\|\operatorname{ad}_{H_\phi}\|\le4J\). Its coefficients are the exponential averages of the time-polynomial coefficients because \(r\int_0^\infty e^{-rt}t^k\,dt=k!/r^k\). This gives the stated uniform \(O_N\) error after degree \(N\) and the exact binomial factor \(N!/[j!(N-j)!]\). Summing the leading absolute coefficients for all \(j\ne0\) and using \(\sum_{j=1}^{N-1}\binom Nj=2^N-2\) proves the total-variation formula. For fixed \(N\) and \(\sin\phi\ne0\), each leading coefficient is nonzero, justifying the absolute-value expansion. Uniformity in \(\phi\), including the zeros of \(\sin\phi\), follows from the uniform coefficient bounds and \(\big||a+b|-|a|\big|\le|b|\).

## Verification

The accompanying `verify_flux_reset.py` uses exact SymPy walks to check the full finite-time flux-sign difference through orders \(N+1\) for all \(3\le N\le9\); it also builds the Hermitian Hamiltonian independently and evaluates the reset resolvent numerically. It reports 364 exact moment assertions, 21 numerical stationary-state comparisons, and high-rate tests for \(N=3,5,7\). These finite checks corroborate, but do not replace, the proof for arbitrary \(N\).

## Relationship to prior work

Wald and Böttcher derived the Poisson-reset quantum-walk stationary-density representation on networks [1], from which the present resolvent starting point follows. Frigerio, Benedetti, Olivares, and Paris analyzed flux-induced chirality and parity effects for unreset quantum walks on cycles [2]. The contribution here is the all-site stationary **opposite-flux** comparison for the two protocols combined, including exact even-cycle indistinguishability and the sharp odd-cycle binomial total-variation coefficient. A related subsequent study [3] analyzes magnetic-flux signatures in measured return statistics; its full treatment of this topic was not accessible in the material inspected, so possible priority overlap beyond its abstract remains unresolved. No general claim that flux information is absent from even-cycle quantum states is made: only stationary position probabilities from a fixed reset site are covered.

## Limitations

The result assumes uniform nearest-neighbor Hermitian hopping, exactly one resetting vertex, independent Poisson resets, and no other dissipative channel. It does not determine full-state distinguishability, transient mixing, optimal reset rate, uniform large-cycle limits, or finite-rate nonvanishing for arbitrary odd cycles. The leading high-reset result is not a proof of behavior at all rates. The related work [3] remains an originality-comparison risk at the full-text level. Independent audit and experimental validation have not been performed.

## References

[1] S. Wald and L. Böttcher, *From classical to quantum walks with stochastic resetting on networks*, arXiv:2008.00510 (first public version 2020-08-02), https://arxiv.org/abs/2008.00510.

[2] M. Frigerio, C. Benedetti, S. Olivares, and M. G. A. Paris, *Quantum-classical distance as a tool to design optimal chiral quantum walks*, arXiv:2106.11685 (first public version 2021-06-22), https://arxiv.org/abs/2106.11685.

[3] P. Luppi, *Flux control of measurement back-action and Leggett–Garg correlations in chiral quantum walks*, arXiv:2608.12519 (2026; abstract consulted), https://arxiv.org/abs/2608.12519.
