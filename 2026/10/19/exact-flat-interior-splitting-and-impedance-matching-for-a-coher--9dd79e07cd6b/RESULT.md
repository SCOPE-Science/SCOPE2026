# Exact flat interior splitting and impedance matching for a coherent path with competing boundary sinks

## Finding

**Theorem (complete two-sink absorption effect).** For every integer \(N\ge 2\), every hopping strength \(J>0\), and every pair of sink rates \(a,b>0\), a coherent nearest-neighbor path with independent absorbing Lindblad jumps at its two endpoints has total absorption probability one. Its left-sink absorption probability, for a walker initially localized at site \(j\), is

\[
P_L(j)=\begin{cases}
\dfrac{a(ab+b^2+4J^2)}{(a+b)(ab+4J^2)},&j=1,\\[6pt]
\dfrac{a(b^2+4J^2)}{(a+b)(ab+4J^2)},&2\le j\le N-1,\\[6pt]
\dfrac{4aJ^2}{(a+b)(ab+4J^2)},&j=N.
\end{cases}
\]

The middle case is absent for \(N=2\). The right-sink probability is \(P_R(j)=1-P_L(j)\). **Every interior site has exactly the same splitting probability, independently of path length and starting position.** When the two sink rates coincide, this probability is exactly \(1/2\) for every interior site, every finite length, and every positive rate.

More strongly, the full left-absorption effect has an explicit tridiagonal form. Put

\[
D=(a+b)(ab+4J^2),\quad c=\frac{2abJ}{D},\quad
 d_1=\frac{a(ab+b^2+4J^2)}{D},\quad
 d=\frac{a(b^2+4J^2)}{D},\quad d_N=\frac{4aJ^2}{D}.
\]

The Hermitian effect \(E_L\) has diagonal \((d_1,d,\ldots,d,d_N)\), immediate upper-diagonal entries \(-ic\), immediate lower-diagonal entries \(+ic\), and all other entries zero. For \(N=2\) its diagonal is simply \((d_1,d_N)\). Consequently, an arbitrary initial density matrix \(\rho\) supported on the path satisfies \(P_L(\rho)=\operatorname{Tr}(E_L\rho)\), not just the site-localized formula above.

For a fixed rival sink rate \(b>0\), the left capture probability from **any** interior site (when \(N\ge3\)) is uniquely maximized at

\[
 a_{\mathrm{opt}}=2J,\qquad
 \max_{a>0}P_L(j)=\frac{b^2+4J^2}{(b+2J)^2}.
\]

The optimum is independent of \(b\), \(N\), and the interior starting site. The probability goes to zero both as \(a\to0^+\) and as \(a\to\infty\). The right-sink counterpart is obtained by reflecting the path and exchanging \(a,b\).

## Assumptions and scope

Take the one-excitation Hilbert space \(\mathcal H=\mathbb C^N\) with ordered basis \(\{|1\rangle,\ldots,|N\rangle\}\) and the resonant uniform hopping Hamiltonian

\[
H=J\sum_{j=1}^{N-1}(|j\rangle\langle j+1|+|j+1\rangle\langle j|).
\]

Add distinct orthogonal absorbing flag states \(|L\rangle,|R\rangle\) and two one-way Lindblad operators \(\sqrt a|L\rangle\langle1|\) and \(\sqrt b|R\rangle\langle N|\). There is no reinjection, bulk dephasing, or onsite detuning. All rates are strictly positive. The path-only, unnormalized surviving state evolves by the non-Hermitian amplitude generator

\[
 A=-iH-\frac12(a|1\rangle\langle1|+b|N\rangle\langle N|).
\]

For a normalized initial \(|j\rangle\), the left absorption probability is the integrated jump flux

\[
P_L(j)=a\int_0^\infty|\langle1|e^{At}|j\rangle|^2\,dt.
\]

## Proof

**1. Strict decay and normalized absorption.** For any eigenpair \(Av=\lambda v\), the real part of the inner product gives

\[
\operatorname{Re}(\lambda)\|v\|^2=-\tfrac12(a|v_1|^2+b|v_N|^2).
\]

If an eigenvalue had real part zero, then \(v_1=v_N=0\). The first-row eigenvector equation, using \(J>0\), forces \(v_2=0\); successive path equations force every remaining entry zero. Hence every eigenvalue has strictly negative real part. Consequently \(e^{At}\to0\) exponentially, the two jump integrals converge, and differentiation of \(\|e^{At}\psi\|^2\) shows \(P_L+P_R=1\) for every normalized initial state.

**2. Exact left-absorption effect.** Let \(P_1=|1\rangle\langle1|\). Define

\[
E_L=a\int_0^\infty e^{A^\dagger t}P_1e^{At}\,dt.
\]

It is the unique Hermitian solution of the continuous Lyapunov equation

\[
A^\dagger E_L+E_LA=-aP_1.
\]

Uniqueness follows from strict decay: the difference of two solutions is constant under \(e^{A^\dagger t}(\cdot)e^{At}\) and tends to zero.

Construct a Hermitian tridiagonal candidate with the entries displayed in the Finding. In \(A^\dagger E+EA=i[H,E]-\{aP_1+bP_N,E\}/2\), the only potentially nonzero entries are on the diagonal and first neighboring diagonals. On the diagonal the verification reduces to

\[
a d_1+2Jc=a,\qquad b d_N=2Jc.
\]

At the left and right neighboring positions when \(N\ge3\), the equations are

\[
J(d-d_1)+\tfrac a2c=0,\qquad
J(d_N-d)+\tfrac b2c=0.
\]

All interior neighboring equations vanish because their diagonal entries coincide and the loss vanishes there. Second-neighbor terms cancel because all the first off-diagonal entries have the same value. For \(N=2\) the single neighboring equation is instead

\[
J(d_N-d_1)+\tfrac{a+b}{2}c=0.
\]

Substituting the four rational expressions proves every equation, for all integers \(N\ge2\). Thus the candidate is exactly \(E_L\). Evaluating \(\langle j|E_L|j\rangle\) yields the three-case formula. The general-density-matrix assertion follows directly from the effect definition.

**3. Sharp rate optimization.** For an interior site, write \(P_L(j)=K f(a)\), where \(K=b^2+4J^2\) and

\[
f(a)=\frac{a}{(a+b)(ab+4J^2)}.
\]

Differentiation gives

\[
f'(a)=\frac{b(4J^2-a^2)}{(a+b)^2(ab+4J^2)^2}.
\]

Since \(b,J>0\), the derivative is strictly positive for \(a<2J\) and strictly negative for \(a>2J\), and both endpoint limits are zero. This establishes the unique global maximum and its stated value. Setting \(a=b\) in the bulk formula gives \(1/2\) identically.

## Verification

The independent numerical verifier `artifacts/verify.py` reconstructs the coherent Hamiltonian and the two-sink amplitude generator, solves the full Lyapunov equation numerically rather than using the closed-form candidate, and compares every matrix entry with the theorem. It also checks the matrix identity, completeness \(E_L+E_R=I\), positivity of both effects, the special two-site boundary, and the interior optimizer. The separate exact-rational residual checks substitute diverse rational parameters into the finite-difference identities. The executed package verifier returned `VERIFY_OK 309 matrix/effect checks + 24 exact rational identities`. Run with `python artifacts/verify.py` after installing the dependencies in `artifacts/requirements.txt`.

The finite tests do **not** establish a theorem for arbitrary path length; the entrywise symbolic identities and the strict-decay argument establish that result.

## Relationship to prior work

Singh, Kessler and Barkai [1] analyze two-target splitting of a coherent finite path using *periodic projective measurement*. They obtain a bulk \(1/2\) regime in the large-system, small-sampling-period domain together with a sampling-time transition. Their survival operator is a product of a unitary and a projection; it is not the continuous two-rate Lindblad semigroup considered here. Neither their bulk asymptotic nor its exceptional sampling-time behavior implies the present exact finite-size, unequal-rate tridiagonal effect or the impedance-matching optimizer.

Ammara, Potoček, Štefaňák and Pepe [2] analyze a *coined discrete-time* walk with two absorbing boundaries, deriving large-size absorption results with a coin-dependent law; their position–coin dynamics is different. Riberi [3] solves a *single* Lindblad sink on a semi-infinite chain and clarifies the weak/strong absorption mechanisms, but has no competing endpoint or finite-chain splitting effect. Zhang and coauthors [4] discuss the relation of trapping times to sink dynamics; the one-sink exact mean-time results are distinct and not claimed here. Loebens [5] develops a continuous-time open-quantum-walk decay parameter and a finite system with two absorbing boundaries, but its two-boundary example has zero coherent hopping Hamiltonian and diagonal stochastic intersite jumps, and concerns decay rates rather than coherent integrated competing-sink probabilities.

The identity \(P_L(j)=1/2\) when \(a=b\) is a *finite-size exact property of this specific continuously monitored path*, not an assertion about discrete monitoring, arbitrary networks, or generic quantum gambler's ruin.

## Limitations

The result assumes spatially uniform real nearest-neighbor coherent hopping, zero onsite potential, no dephasing, independent irreversible sinks exclusively at the two endpoints, and strictly positive sink rates. Initial-position independence is for a position-localized interior state (or diagonal mixtures thereof); an initial coherent superposition can exhibit phase-sensitive splitting through the nonzero off-diagonals of \(E_L\). The optimizer concerns ultimate branching probability, not mean detection time, transient current, or transfer fidelity. No generalization to nonuniform chains, cycles, coherent recombination of sink flags, or other monitoring protocols is asserted. The closed formula is self-contained; publication priority versus earlier unindexed or implicit equivalents is not independently established.

## References

1. P. Singh, D. A. Kessler and E. Barkai, *Transition in Splitting Probabilities of Quantum Walks*, arXiv:2601.16111 (first posted 2026-01-22), https://arxiv.org/html/2601.16111v2.
2. A. Ammara, V. Potoček, M. Štefaňák and F. V. Pepe, *Quantum Walk on a Line with Absorbing Boundaries*, arXiv:2508.13318 (first posted 2025-08-18), https://arxiv.org/html/2508.13318v3.
3. F. Riberi, *Boundary-localized non-Hermitian modes in an absorbing quantum walk*, arXiv:2605.08056 (first posted 2026-05-08), https://arxiv.org/abs/2605.08056.
4. Y. Zhang et al., *Optimal Dephasing for Ballistic Energy Transfer in Disordered Linear Chains*, arXiv:1706.09524, https://arxiv.org/abs/1706.09524.
5. N. Loebens, *Decay Parameter for Continuous-Time Open Quantum Walks*, *Brazilian Journal of Physics* **56** (2026), article 200, https://doi.org/10.1007/s13538-026-02125-4.
