# Sharp parity-dependent Zeno suppression of magnetic-ring directionality

## Finding

Consider an integer \(n\geq3\), a cycle \(C_n=\mathbb Z/n\mathbb Z\), hopping strength \(J>0\), flux \(\Phi\in\mathbb R\), and observation time \(T>0\). Define the Hermitian nearest-neighbor Hamiltonian, with indices modulo \(n\), by

\[
H_{j+1,j}=J e^{i\Phi/n},\qquad H_{j,j+1}=J e^{-i\Phi/n},\qquad H_{jj}=0.
\]

Prepare the walker at site \(0\). Divide \(T\) into \(m\geq1\) equal intervals, and perform a **complete, nonselective, projective site measurement** after each unitary interval (including the last). Its resulting final position distribution is the zeroth column of

\[
M_m=P_{T/m}^{\,m},\qquad
P_\delta(j,k)=\left|\langle j|e^{-i\delta H}|k\rangle\right|^2.
\]

Define the oriented nearest-neighbor contrast and escape probability by

\[
\mathcal A_m=M_m(1,0)-M_m(n-1,0),\qquad
\mathcal E_m=1-M_m(0,0).
\]

**Theorem (sharp cycle-parity Zeno hierarchy).** For every even \(n\), and for every \(m,T,J,\Phi\), one has **exactly** \(\mathcal A_m=0\). For every odd \(n\geq3\), at fixed \(n,J,T,\Phi\) as \(m\to\infty\),

\[
\boxed{\displaystyle
\mathcal A_m=
\frac{4(-1)^{(n-1)/2}J^nT^n\sin\Phi}{(n-1)!\,m^{n-1}}
+O(m^{-n}).}
\]

In both parity classes,

\[
\boxed{\displaystyle \mathcal E_m=\frac{2J^2T^2}{m}+O(m^{-2}).}
\]

Consequently, for odd \(n\),

\[
\boxed{\displaystyle
\lim_{m\to\infty}m^{n-2}\frac{\mathcal A_m}{\mathcal E_m}
=\frac{2(-1)^{(n-1)/2}J^{n-2}T^{n-2}\sin\Phi}{(n-1)!}.}
\]

If \(n\) is odd and \(\sin\Phi\ne0\), the directional contrast is nonzero for every sufficiently large \(m\), with sign \((-1)^{(n-1)/2}\operatorname{sgn}(\sin\Phi)\). In contrast, when \(\sin\Phi=0\), it vanishes for **every** \(m\) and \(T\). Thus an oriented, resolved readout distinguishes the two globally reversed flux orientations exactly when the ring is odd and the flux is not gauge-real, whereas the return-only readout cannot distinguish them.

For example, the raw chirality scales as \(m^{-2}\), \(m^{-4}\), and \(m^{-6}\) on three-, five-, and seven-site rings, respectively, although total escape remains of order \(m^{-1}\) in each case. The coefficient, including its factorial dependence on circumference, is exact.

## Assumptions and scope

The Hilbert space is \(\mathbb C^n\). The Hamiltonian has only the stated Hermitian nearest-neighbor links, with no on-site potentials, long-range hopping, decoherence, postselection, or feedback. The Peierls flux \(\Phi\) is understood modulo \(2\pi\); the orientation convention is the displayed sign on \(H_{j+1,j}\). Projective site measurements are rank-one measurements in the distinguished lattice basis, and their outcomes are forgotten before the next interval. The limit fixes \(n,J,T,\Phi\) and sends the integer \(m\) to infinity; there is no uniform claim in growing \(n\) or simultaneously scaled parameters.

The contrast \(\mathcal A_m\) is a difference of two site probabilities, not a persistent stationary current, an entropy-production rate, or a Leggett–Garg functional. The result is a finite-system statement and makes no assumption about a thermodynamic phase transition.

## Proof

**1. The measured evolution is classical between measurements.** After a complete site measurement, the state is diagonal. Evolving for \(\delta\) and forgetting the next site outcome sends its diagonal probabilities through the unistochastic matrix \(P_\delta\). Repeating \(m\) times gives \(M_m=P_\delta^m\) without approximation. Translation invariance makes \(P_\delta\) circulant and doubly stochastic.

**2. Exact obstruction on even cycles.** When \(n\) is even, let \(\Gamma\) multiply the even sublattice by \(+1\) and the odd sublattice by \(-1\). Every nonzero hopping crosses the sublattices, so \(\Gamma H\Gamma=-H\). Writing \(U(t)=e^{-itH}\),

\[
\Gamma U(t)\Gamma=U(-t)=U(t)^\dagger.
\]

Therefore \(|U(t)_{jk}|=|U(t)_{kj}|\) for all sites and real \(t\). Hence \(P_\delta\) is symmetric. Its circulant symmetry forces \(P_\delta(1,0)=P_\delta(n-1,0)\); the same holds for every power \(M_m\). This proves exact zero contrast even at nonzero magnetic flux.

**3. The first odd-cycle direction-sensitive interference.** Now take odd \(n\). In the walk expansion of \(U(\delta)_{1,0}\), the two shortest paths with different winding numbers are the direct positive edge of length one and the negative winding of length \(n-1\). Their respective contributions are

\[
(-iJ\delta)e^{i\Phi/n},\qquad
\frac{(-iJ\delta)^{n-1}}{(n-1)!}e^{-i(n-1)\Phi/n}.
\]

Paths in the same winding sector have lengths of one parity and share a fixed magnetic phase. Their squared-amplitude interference has only even powers of \(\delta\) and is reciprocal under inversion. Interference of different winding sectors requires a total path length at least \(n\); at precisely \(n\), the displayed pair is the unique possibility. Taking the real part of their cross term, and reversing orientation for the other neighbor, gives

\[
P_\delta(1,0)-P_\delta(n-1,0)
=\frac{4(-1)^{(n-1)/2}J^n\sin\Phi}{(n-1)!}\delta^n
+O(\delta^{n+1}).
\]

The same walk-length argument applies to any ordered site pair: the antisymmetric part of the entire circulant transition matrix satisfies \(\|P_\delta-P_\delta^\mathsf T\|=O(\delta^n)\). These bounds use finite-dimensional analytic expansions and hold for fixed model parameters.

**4. Propagation through repeated measurements.** Unitarity gives \(\|P_\delta-I\|=O(\delta^2)\). Since powers of a stochastic matrix are bounded in the induced probability norm, \(\|P_\delta^j-I\|=O(j\delta^2)\) for \(0\leq j\leq m\). The telescoping identity

\[
P_\delta^m-(P_\delta^\mathsf T)^m
=\sum_{j=0}^{m-1}P_\delta^{m-1-j}
(P_\delta-P_\delta^\mathsf T)(P_\delta^\mathsf T)^j
\]

therefore yields

\[
P_\delta^m-(P_\delta^m)^\mathsf T
=m(P_\delta-P_\delta^\mathsf T)
+O(m^2\delta^{n+2}).
\]

Translation invariance identifies the \((1,0)\) entry of the left side with \(M_m(1,0)-M_m(n-1,0)\). Substituting \(\delta=T/m\) proves the sharp asymptotic and its \(O(m^{-n})\) remainder.

**5. Universal leading escape and conditional directionality.** The short-time transition probability to either neighboring site equals \(J^2\delta^2+O(\delta^3)\); the diagonal is \(1-2J^2\delta^2+O(\delta^3)\). Thus

\[
P_{T/m}^{\,m}=I+\frac{J^2T^2}{m}L_{\rm jump}+O(m^{-2}),
\]

where \(L_{\rm jump}\) has nearest-neighbor off-diagonal entries \(+1\) and diagonal entries \(-2\). This yields the claimed escape law and the ratio after dividing the two asymptotic expressions.

**6. Exactly gauge-real fluxes.** If \(\sin\Phi=0\), the total cycle holonomy is \(+1\) or \(-1\), and a diagonal unitary gauge makes every hopping real. The resulting Hamiltonian is real symmetric, so \(U(t)\) and \(P_t\) are symmetric. The contrast then vanishes identically. Under \(\Phi\mapsto-\Phi\), complex conjugation exchanges clockwise and counterclockwise transport but leaves return probability unchanged; in an odd ring with \(\sin\Phi\ne0\), the nonzero asymptotic coefficient completes the stated discrimination criterion.

## Verification

The included `verify.py` is an independently executable high-precision numerical checker requiring Python and `mpmath`. It verifies the Hamiltonian sign convention by comparing Fourier diagonalization with a separate matrix exponential, checks the exact parity obstruction for three even cycle sizes, checks the gauge-real cases, and tests odd-cycle coefficients and Zeno convergence for \(n\in\{3,5,7,9\}\). The checker uses 65-decimal-place arithmetic, and it passed 150 deterministic assertion groups. These are finite consistency tests; the proof of the statements for all fixed admissible parameters and every odd circumference is in the preceding steps, not in the numerical outputs.

To reproduce: run `python verify.py` with `mpmath` installed. The expected final line begins `PASS: 150 deterministic assertion groups`.

## Relationship to prior work

Luppi, *Flux control of measurement back-action and Leggett-Garg correlations in chiral quantum walks* (arXiv:2608.12519v1, first public August 12, 2026), analyzes sequential **single-vertex dichotomic return** measurements. Its published abstract describes winding-number and return-only flux-parity effects; that protocol is invariant under simultaneous flux reversal. The current theorem instead concerns **complete position resolution at every step**, an oriented pair of final site probabilities, and the exact suppression exponent under an arbitrary growing number of measurements. The source's arXiv full text was not retrievable during the comparison, so it remains a priority risk; a searchable abstract and secondary detailed account were inspected rather than silently treated as the entire paper.

Luppi, Benedetti and Smirne, *Temporal nonclassicality in continuous-time quantum walks* (arXiv:2512.18873v1, December 21, 2025), derives the nonselective intermediate-position-measurement rule and a Kolmogorov-distance witness on **real symmetric** cycle and complete-graph Laplacians. The current magnetic-flux odd-cycle sign discriminator, all-circumference power law, and repeated-measurement coefficient are not implied by its real-Hamiltonian formulas alone.

Wampler, Khor, Refael and Klich, *Stirring by Staring: Measurement Induced Chirality* (arXiv:2108.05906v1), studies **patterned measurements** of fermions on a Lieb lattice that create chiral motion and develops a different Zeno stochastic limit. Yu and Cai, *Controlled transport in chiral quantum walks on graphs* (arXiv:2308.12516v1), studies chirality-dependent transport in graph junctions, without the present full-site Zeno protocol. Standard unistochastic reductions and bipartite reciprocity are used here as established methods, not claimed as discoveries.

The result is not claimed to rule out implicit derivability from a more general theorem on Zeno expansions or magnetic quantum walks; the asserted contribution is the explicit **sharp, parameter-exact ring-parity and circumference law for the resolved repeated-measurement directional observable**.

## Limitations

Only a single particle, unitary evolution between instantaneous rank-one measurements, uniform nearest-neighbor Peierls hopping, and fixed positive \(J,T\) are considered. The theorem does not treat partially resolved instruments, noisy detection, disorder, loss, higher-dimensional lattices, unbounded Hamiltonians, or the limit in which the ring circumference grows with the number of measurements. The flux orientation is detectable through its sign when \(\sin\Phi\ne0\); its exact angle cannot in general be reconstructed from this single leading coefficient because that coefficient depends only on \(\sin\Phi\). The analyzed source on chiral local return measurements was not accessible in full; the remaining possibility of a broader earlier formula is recorded in the accompanying scientific review.

## References

1. P. Luppi, *Flux control of measurement back-action and Leggett-Garg correlations in chiral quantum walks*, arXiv:2608.12519v1 (August 12, 2026), https://arxiv.org/abs/2608.12519 .
2. P. Luppi, C. Benedetti, A. Smirne, *Temporal nonclassicality in continuous-time quantum walks*, arXiv:2512.18873v1 (December 21, 2025), https://arxiv.org/abs/2512.18873 .
3. M. Wampler, B. J. J. Khor, G. Refael, I. Klich, *Stirring by Staring: Measurement Induced Chirality*, arXiv:2108.05906v1 (August 12, 2021), https://arxiv.org/abs/2108.05906 .
4. Y.-C. Yu, X. Cai, *Controlled transport in chiral quantum walks on graphs*, arXiv:2308.12516v1 (August 24, 2023), https://arxiv.org/abs/2308.12516 .
