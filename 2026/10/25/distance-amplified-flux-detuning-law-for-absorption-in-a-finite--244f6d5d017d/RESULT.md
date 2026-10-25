# Distance-amplified flux-detuning law for absorption in a finite diamond quantum chain

## Finding
For each positive integer \(L\) and strictly positive sink strength \(\gamma\), let \(T_L(\phi,\gamma)\) be the mean time to irreversible absorption of an excitation starting at the right backbone endpoint of an open magnetic diamond chain with \(L\) rhombi and a sink at the left endpoint. For flux \(0<\phi<2\pi\), \(\phi\ne\pi\), absorption is certain and the mean time is finite. Exactly at the half-flux caging point \(\phi=\pi\), no absorption occurs. At fixed \(L,\gamma\), the precise detuning singularity is
\[
\lim_{\phi\to\pi}|\phi-\pi|^{2L}T_L(\phi,\gamma)=\gamma4^{L-1}.
\]
Each added rhombus increases the detuning exponent by exactly two. This theorem quantifies the time required to overcome destructive-interference caging; it does not assert the same law when the chain length grows with detuning.

## Assumptions and scope
The backbone vertices are \(a_0,\ldots,a_L\). For each \(j=1,\ldots,L\), introduce an upper vertex \(u_j\) and lower vertex \(v_j\). The only edges join \(a_{j-1}\) and \(a_j\) through \(u_j\) or \(v_j\), with hopping magnitudes one. One convenient gauge specifies a backbone-to-side coupling matrix \(B\) (rows indexed by backbone vertices, columns by upper and lower vertices) by
\[
B_{j-1,u_j}=B_{j-1,v_j}=1,\qquad
B_{j,u_j}=e^{i\phi/2},\qquad B_{j,v_j}=e^{-i\phi/2}.
\]
All other entries vanish. The Hermitian Hamiltonian is \(H=\begin{pmatrix}0&B\\B^*&0\end{pmatrix}\). The sink is described by \(H_{\mathrm{eff}}=H-i\gamma |a_0\rangle\langle a_0|/2\), and the initial unit vector is \(\psi(0)=|a_L\rangle\). The survival probability is \(S(t)=\|e^{-itH_{\mathrm{eff}}}\psi(0)\|^2\); the first-passage density is \(f(t)=\gamma|\langle a_0|e^{-itH_{\mathrm{eff}}}\psi(0)\rangle|^2\). When absorption is certain, \(T_L=\int_0^\infty S(t)dt=\int_0^\infty tf(t)dt\). The theorem is for one excitation, a finite open chain, fixed hopping units, strictly positive loss, and flux approaching \(\pi\) from either side.

## Proof
**Reduction and absence of unobserved backbone modes.** Set \(g=2\cos(\phi/2)\). Direct multiplication gives
\[
K:=BB^*=\begin{pmatrix}
2&g& & &\\ g&4&g&&\\ &\ddots&\ddots&\ddots&\\ &&g&4&g\\ &&&g&2
\end{pmatrix}
\]
with dimension \(L+1\); for \(L=1\), both diagonal entries are \(2\). For \(0<\phi<2\pi\), the rows of \(B\) are independent: a linear combination of rows annihilating each pair of upper/lower columns forces the coefficient at row \(j\) to vanish because \(\sin(\phi/2)\ne0\), and then forces the remaining row to vanish. Thus \(K\) is positive definite. All zero modes of \(H\) have support on side vertices only, and are orthogonal to \(|a_L\rangle\).

Let \(q(t)\) be the backbone amplitude vector and \(p(t)\) the side amplitude vector. With \(w=-iBp\), the dynamics on the cyclic subspace of the initial vector is
\[
q'=w-\frac{\gamma}{2}E_0q,\qquad w'=-Kq,
\]
where \(E_0=|a_0\rangle\langle a_0|\). The physical norm on this space is \(\|q\|^2+w^*K^{-1}w\) and satisfies
\[
\frac{d}{dt}\big(\|q\|^2+w^*K^{-1}w\big)=-\gamma|q_0|^2.
\]
If \(g\ne0\), every eigenvector of the irreducible real Jacobi matrix \(K\) has a nonzero first coordinate (recursion from its first row). Any nondecaying eigenmode of the damped system would have \(q_0=0\), hence would satisfy an undamped eigenproblem for \(K\), a contradiction. The finite-dimensional surviving evolution therefore decays exponentially, proving certain eventual absorption and finite \(T_L\) for \(g\ne0\).

**A sharp slow-mode calculation.** The modal equation for a solution \(q(t)=e^{st}q\) is
\[
\big(s^2 I+K+(\gamma/2)sE_0\big)q=0.
\]
At \(g=0\) the right-end oscillator has the two simple eigenvalues \(s_\pm=\pm i\sqrt2\). The left end is a damped oscillator with spectral parameter satisfying \(s^2+(\gamma/2)s+2=0\); the \(L-1\) interior oscillators have frequencies \(\pm2\). The right-end pair is separated from both other groups for every fixed \(\gamma>0\). Analytic perturbation therefore gives one nearby eigenvalue and a normalized mode for each sign when \(g\) is small. Normalize its displacement by \(q_L=1\). The interior recurrence, whose leading interior diagonal is \(-2\) at \(s=\pm i\sqrt2\), yields, for each fixed \(1\le j\le L-1\),
\[
q_j=(g/2)^{L-j}(1+O(g))
\]
(up to an irrelevant sign fixed by the gauge). The left boundary equation then yields
\[
q_0=-\frac{2g^L}{\gamma s_\pm 2^{L-1}}(1+O(g)),
\qquad |q_0|^2=\frac{2g^{2L}}{\gamma^2 4^{L-1}}(1+O(g)).
\]
For \(L=1\), the interior recurrence is empty and the same boundary formula follows directly. For the modal velocity \(w=(sI+\gamma E_0/2)q\), the physical squared norm tends to \(2\). Apply the exact dissipation identity to this eigenmode:
\[
2\operatorname{Re}(s)\left(\|q\|^2+w^*K^{-1}w\right)=-\gamma|q_0|^2.
\]
Consequently each of the two right-end modes has the same leading norm-decay rate
\[
-2\operatorname{Re}(s)=\frac{g^{2L}}{\gamma4^{L-1}}(1+O(g)).
\]

**Dominance of the slow modes.** At \(g=0\), the initial displacement at \(a_L\), with zero modal velocity, lies entirely in the two right-end modes, with equal squared norm weights \(1/2\). For small nonzero \(g\), its total squared overlap with the complementary modes is \(O(g^2)\). The stable left-end modes retain a strictly negative real-part bound. The \(L-1\) interior modes split at first order according to the ordinary finite path Jacobi matrix, whose eigenvectors all have nonzero component at the first interior vertex. Their induced boundary dissipation rates are of order \(g^2\); their combined contribution to the integrated survival is therefore \(O(1)\). Spectrally distinct cross terms have bounded time integrals, while the two slow right-end modes are separated by a nonzero imaginary frequency and hence also have bounded cross terms. Thus only their diagonal contributions determine the leading divergence, giving
\[
T_L(\phi,\gamma)=\frac{\gamma4^{L-1}}{g^{2L}}(1+o(1)).
\]
Since \(g=2\cos(\phi/2)=-(\phi-\pi)+O((\phi-\pi)^3)\), the claimed limit follows.

**Exactly at caging.** At \(\phi=\pi\), \(g=0\), so \(K=BB^*\) is diagonal and \(H^2\) does not transfer backbone amplitude between distinct sites. Because \(H\) is bipartite, the entire time evolution of \(|a_L\rangle\) has zero amplitude at \(a_0\). The local sink never acts, \(S(t)=1\), and \(T_L=\infty\).

## Verification
Run `python check.py` with NumPy and SciPy. It constructs the magnetic graph directly, checks \(BB^*=K\), evolves the full non-Hermitian Hamiltonian at finite times, evaluates absorption means using a reduced Hamiltonian Lyapunov equation, independently recomputes those means in damped-oscillator coordinates, and checks approach to the asserted leading coefficient for several lengths and positive sink strengths. The recorded run passed 204 computational checks. These are finite numerical corroborations only; the all-length exponent and prefactor follow from the spectral perturbation argument above.

## Relationship to prior work
Lopes and Dias (arXiv:1110.2224, first submitted 2011-10-10) derived the diamond-chain tight-binding model, magnetic bands, and compact localized states. In particular, complete Aharonov–Bohm caging at half flux is prior art. Gligorić, Leykam, and Maluckov (arXiv:1909.07055) studied disorder-induced transport and loss of caging in diamond photonic arrays, but not a terminal absorbing-time asymptotic. Zhang and Jin (arXiv:2005.01044) study different non-Hermitian caging mechanisms involving gain/loss and exceptional points. Riberi (arXiv:2605.08056) gives exact first-passage dynamics for a boundary sink on a semi-infinite one-dimensional chain, not magnetic diamond plaquettes. The finding isolates the sharp exponent and prefactor for escape from *finite* flux cages to a remote endpoint sink. It does not claim discovery of Aharonov–Bohm caging, boundary absorption, or generic perturbative tunneling.

## Limitations
The length and absorption rate are fixed before flux approaches \(\pi\). No uniform remainder in growing length or vanishing sink strength is proved, and the result does not concern finite-temperature incoherent hopping, disorder, multiple particles, or different sink placements. It does not provide the full first-passage density. Historical originality has not undergone independent exhaustive verification.

## References
1. A. A. Lopes and R. G. Dias, *Interacting spinless fermions in a diamond chain*, arXiv:1110.2224 (first public submission 2011-10-10), https://arxiv.org/html/1110.2224v2.
2. G. Gligorić, D. Leykam and A. Maluckov, *Influence of different disorder types on Aharonov-Bohm caging in the diamond chain*, arXiv:1909.07055 (2019), https://arxiv.org/html/1909.07055v1.
3. S. M. Zhang and L. Jin, *Non-Hermitian Aharonov-Bohm Cage*, arXiv:2005.01044 (2020), https://arxiv.org/abs/2005.01044.
4. F. Riberi, *An Exactly Solvable Absorbing Quantum Walk*, arXiv:2605.08056 (2026), https://arxiv.org/abs/2605.08056.
