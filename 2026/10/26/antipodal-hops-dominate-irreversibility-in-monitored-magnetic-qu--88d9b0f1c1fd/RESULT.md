# Antipodal hops dominate irreversibility in monitored magnetic quantum rings

## Finding

**Theorem (sharp stationary irreversibility of an odd magnetic cycle).** Fix an odd integer \(N=2m+1\ge5\). Number the vertices of a cycle by \(0,\ldots,N-1\) modulo \(N\). Give edge \(j\to j+1\) a nonzero positive hopping magnitude \(a_j\) and a real phase \(\theta_j\), with total flux \(\Phi=\sum_j\theta_j\). Let the Hermitian one-particle Hamiltonian \(H\) have entries \(H_{j+1,j}=a_je^{i\theta_j}\), \(H_{j,j+1}=a_je^{-i\theta_j}\), and all diagonal entries zero. After each free evolution interval \(\tau>0\), completely dephase the vertex basis, giving the classical transition matrix

\[
P_{uv}(\tau)=|\langle u|e^{-i\tau H}|v\rangle|^2.
\]

Its invariant distribution is uniform. Define the stationary path-reversal relative entropy per step by

\[
\sigma(\tau)=\frac1N\sum_{0\le u<v<N}
 (P_{uv}-P_{vu})\log\frac{P_{uv}}{P_{vu}}.
\]

For every fixed choice of positive \(a_j\), all terms are defined for sufficiently small positive \(\tau\), and

\[
\boxed{\sigma(\tau)=
\frac{16\sin^2\!\Phi}{N[(m+1)!]^2}
\left[\sum_{j=0}^{N-1}\left(\prod_{r=0}^{m}a_{j+m+r}\right)^2\right]
\tau^{N+1}+O(\tau^{N+3}).}
\]

All indices inside products are modulo \(N\). Each product in the bracket follows the **longer arc**, consisting of \(m+1\) edges, complementary to the \(m\)-edge shortest arc from \(j\) to \(j+m\). The coefficient is strictly positive exactly when \(\sin\Phi\ne0\). **Only transitions between maximally separated vertex pairs contribute at leading order**; contributions from every shorter-distance pair are \(O(\tau^{N+3})\).

For uniform hopping \(a_j=J>0\), this specializes to the parameter-free cycle law

\[
\boxed{\sigma(\tau)=\frac{16\sin^2\!\Phi}{[(m+1)!]^2}
(J\tau)^{N+1}+O((J\tau)^{N+3}).}
\]

For comparison, if \(N\) is even with the same zero-onsite-energy Hamiltonian, or if the flux satisfies \(\sin\Phi=0\) for any cycle length, then \(P(\tau)\) is symmetric and \(\sigma(\tau)=0\) **at every** \(\tau\) for which the entropy expression is defined (with the standard zero-current convention). The preceding exact-zero cases are known symmetry mechanisms, not claimed as new discoveries.

## Assumptions and scope

This theorem concerns finite **single-particle** magnetic tight-binding cycles without self-energies or additional chords, with fixed strictly positive hopping magnitudes, arbitrary Peierls phases, and complete unselective vertex dephasing after every coherent interval. The limit is \(\tau\downarrow0\) **with \(N\), all magnitudes, and the flux fixed**. Throughout, logarithms are natural; \(\sigma\) is the classical entropy production of the induced stationary discrete-time Markov chain, not von Neumann entropy production of a partially dephased quantum state.

For each small \(\tau>0\), every entry of \(P(\tau)\) is strictly positive by its first nonzero shortest-path Taylor term, hence the chain has a unique invariant distribution. Unitarity makes \(P\) doubly stochastic, so that distribution is \(\pi_j=1/N\). The definition is therefore the relative entropy between stationary adjacent-step path probabilities \(\pi_vP_{uv}\) and their reversals \(\pi_uP_{vu}\). The time-normalized value \(\sigma(\tau)/\tau\) has leading power \(\tau^N\).

## Proof

**1. Shortest paths and analytic expansions.** Write \(U(\tau)=e^{-i\tau H}\). For vertices \(j\) and \(j+d\) with \(1\le d\le m\), the shortest path is the clockwise arc of length \(d\); its positive magnitude product is

\[
A_{j,d}=\prod_{r=0}^{d-1}a_{j+r}.
\]

The Taylor expansion of \(U\) gives, for either orientation,

\[
P_{j+d,j}(\tau)=\frac{A_{j,d}^2}{(d!)^2}\tau^{2d}(1+O(\tau)),
\qquad
P_{j,j+d}(\tau)=\frac{A_{j,d}^2}{(d!)^2}\tau^{2d}(1+O(\tau)).
\]

The nearest alternative simple path has length \(N-d\). The analyticity of the amplitudes makes these expansions genuine convergent local expansions, rather than approximations based on enumerating finitely many walks.

**2. First antisymmetric term.** Hermiticity implies \(P_{uv}(-\tau)=P_{vu}(\tau)\). Consequently \(P_{uv}(\tau)-P_{vu}(\tau)\) is odd analytic in \(\tau\). For a coefficient of odd degree \(k\), its path-pair expansion consists of two directed walks between the same endpoints with total length \(k\); concatenating one with the reverse of the other produces a closed odd walk of length \(k\). A cycle graph of odd order \(N\) has no odd closed walk of length below \(N\). The first possible antisymmetry is therefore degree \(N\).

At degree \(N\), every contributing closed odd walk must traverse the cycle exactly once, and its two constituent paths are precisely the complementary simple arcs of lengths \(d\) and \(N-d\). Their product of hopping magnitudes is \(A=\prod_{r=0}^{N-1}a_r\); their oriented phase difference is the full flux \(\Phi\). Expanding the two interference terms, with \(N=2m+1\), yields the exact coefficient

\[
\boxed{P_{j+d,j}(\tau)-P_{j,j+d}(\tau)=
\frac{4(-1)^{m+d+1}A\sin\Phi}{d!(N-d)!}\tau^N
+O(\tau^{N+2}).}
\]

The error exponent is \(N+2\), not \(N+1\), by the oddness already established. This formula is valid for each distance \(1\le d\le m\), including all non-nearest-neighbor pairs. At maximal separation \(d=m\), the signed coefficient is \(-4A\sin\Phi/[m!(m+1)!]\).

**3. Pairwise entropy and antipodal dominance.** Fix a pair at distance \(d\). Write \(b=A_{j,d}^2/(d!)^2>0\) and \(c=4(-1)^{m+d+1}A\sin\Phi/[d!(N-d)!]\). The expansions in steps 1 and 2 give

\[
(P_{j+d,j}-P_{j,j+d})
\log\frac{P_{j+d,j}}{P_{j,j+d}}
=\frac{c^2}{b}\tau^{2N-2d}+O(\tau^{2N-2d+1}).
\]

Since \(d\le m\), the smallest exponent is \(2N-2m=N+1\), attained **only when \(d=m\)**. Every other distance has exponent at least \(N+3\). Each unordered pair at distance \(m\) is represented exactly once by \(\{j,j+m\}\) as \(j\) runs through all \(N\) vertices. For such a pair,

\[
\frac{c^2}{b}=
\frac{16\sin^2\!\Phi}{[(m+1)!]^2}
\left(\prod_{r=0}^{m}a_{j+m+r}\right)^2,
\]

because the squared full-cycle product divided by the squared shortest-arc product is the squared complementary long-arc product. Summing these contributions and dividing by \(N\) proves the displayed leading coefficient.

Finally \(\sigma(-\tau)=\sigma(\tau)\), since \(P(-\tau)=P(\tau)^T\). After factoring their strictly positive leading powers, all off-diagonal probabilities have analytic nonzero factors near zero; therefore every logarithmic ratio extends analytically and \(\sigma\) has an even Taylor expansion. This rules out the candidate order \(N+2\) correction and upgrades the error to \(O(\tau^{N+3})\).

**4. Exact reversible cases.** On an even cycle, let \(\Gamma\) be \(+1\) on even vertices and \(-1\) on odd vertices. Then \(\Gamma H\Gamma=-H\), hence \(U(-\tau)=\Gamma U(\tau)\Gamma\). Transition probabilities are unchanged by this conjugation, whereas Hermiticity gives \(P(-\tau)=P(\tau)^T\); thus \(P\) is symmetric for all \(\tau\). If \(\Phi\) is an integer multiple of \(\pi\), a diagonal gauge transformation makes every edge of \(H\) real; the transformed Hamiltonian and its exponential are symmetric, so \(P\) is again symmetric at all times. This completes the proof.

## Verification

The accompanying `verify.py` has been executed from the present package. Its exact-arithmetic portion constructs the full Gaussian-integer matrix powers of the Hamiltonian (flux \(\pi/2\) on one edge), extracts Taylor coefficients of \(|U_{uv}|^2\) by rational arithmetic, and checks the absence of lower odd terms, the degree-\(N\) coefficient for every displacement and origin, and the claimed weighted entropy coefficient for \(N=3,5,7,9\). This gives 328 exact checks. The optional high-precision part independently evaluates matrix exponentials and stationary entropy production for four odd cycle sizes and three small step times, checking convergence to the coefficient. It also checks exact even-cycle reciprocity numerically for three even sizes, giving 19 numerical diagnostics.

These finite tests verify formulas and implementations at the specified cases. They do not prove the theorem for unbounded \(N\); that conclusion follows from the path-pair parity and unique-cycle arguments above.

## Relationship to prior work

Huang et al. (arXiv:2606.15935, first posted 2026-06-14) experimentally study dephasing-induced Markov dynamics \(P_{uv}=|U_{uv}|^2\), uniform stationary populations, and flux-controlled spectral transitions on a three-node network. Longhi (arXiv:2508.11947) develops the preceding dynamical spectral picture. Lu et al. (arXiv:1405.6209) and Zimborás et al. (arXiv:1208.4049) establish foundational gauge and bipartite symmetry principles for chiral quantum walks, including the fact that bipartite graphs need not have directional probability bias. These ingredients are acknowledged, not claimed here.

Luppi (arXiv:2608.12519) investigates flux-dependent Leggett–Garg correlations and return probabilities under a single-site Lüders measurement, which does not erase coherence inside the complementary subspace. Its odd-ring return asymptotics therefore do not evaluate the fully vertex-dephased Markov chain or its stationary forward/backward path relative entropy.

The present mathematical result is the **exact stationary path-reversal entropy-production asymptotic** for every odd cycle with arbitrary positive edge magnitudes, together with the unexpected fact that its leading contribution comes from the rare *most distant* transitions rather than the highest-probability nearest-neighbor steps. Its exponent and inhomogeneous coefficient do not follow from a nearest-neighbor directional asymmetry statement alone. Vallejo et al. (arXiv:2004.04850) consider entropy generation in the reduced coin of a coined quantum walk on the line, a different entropy observable and model.

## Limitations

The result is a fixed-size, short-coherent-step asymptotic. It is not uniform when \(N\) grows with \(\tau^{-1}\), does not quantify finite-dephasing \(0<q<1\), and makes no claims for graphs with chords, nonzero onsite energies, or multiple particles. The classical path-space entropy production is not automatically the total physical heat dissipation of any particular photonic hardware. The proof of the exact leading coefficient does not establish global originality; related general chiral-walk and stochastic-thermodynamic results could have implications beyond those checked.

## References

1. X. Huang, L. Xiao, B. Huo, X. Wang, S. Longhi, and P. Xue, *Experimental Observation of Dynamical Phase Transitions in a Dephased Photonic Quantum Walk*, arXiv:2606.15935 (first public 2026-06-14), https://arxiv.org/abs/2606.15935.
2. S. Longhi, *Dynamical Phase Transitions in Open Quantum Walks*, arXiv:2508.11947 (2025), https://arxiv.org/abs/2508.11947.
3. D. Lu et al., *Chiral Quantum Walks*, arXiv:1405.6209 (first public 2014-05-23), https://arxiv.org/abs/1405.6209.
4. Z. Zimborás et al., *Quantum Transport Enhancement by Time-Reversal Symmetry Breaking*, arXiv:1208.4049 (2012), https://arxiv.org/abs/1208.4049.
5. A. Vallejo, A. Romanelli, R. Donangelo, and R. Portugal, *Entropy production in the quantum walk*, arXiv:2004.04850 (2020), https://arxiv.org/abs/2004.04850.
6. P. Luppi, *Flux control of measurement back-action and Leggett-Garg correlations in chiral quantum walks*, arXiv:2608.12519 (first public 2026-08-12), https://arxiv.org/abs/2608.12519.
