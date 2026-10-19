# Sharp cross-layer transfer ceiling in a six-vertex chiral quantum router

## Finding
Consider an oriented triangle with one pendant vertex attached to each triangle vertex, with unit hopping magnitudes, zero on-site energies, and loop-flux magnitude \(\pi/2\). Label the triangle sites \(c_j\) and the pendant sites \(p_j\), with \(j\in\mathbb Z/3\mathbb Z\), in the gauge specified below. For every ordered pair \(j,k\), the exact probability of transfer from a *single internal site* to a *single external site* has the sharp all-time supremum

\[
\sup_{t\geq0}\left|\langle p_k|e^{-itH}|c_j\rangle\right|^2
=\frac{(1+4/\sqrt7)^2}{9}
=\frac{23+8\sqrt7}{63}
=0.701047785532011\ldots.
\]

This supremum is **never attained at any finite time**, but it can be approached arbitrarily closely at arbitrarily large positive times. The ceiling is the same for all nine ordered internal-to-external site pairs. In particular, no waiting time can achieve even approximately unit-fidelity transfer between any such pair in this fixed model, despite the known near-unit external-to-external routing in the same network.

More precisely, the complete cross-layer transition kernel is

\[
\boxed{\langle p_k|e^{-itH}|c_j\rangle=-\frac{i}{3}\left[\sin t+\frac{4}{\sqrt7}\sin\left(\frac{\sqrt7\,t}{2}\right)\cos\left(\frac{\sqrt3\,t}{2}-\frac{2\pi(k-j)}3\right)\right].}
\]

Here time is expressed in units of the inverse common hopping magnitude.

## Assumptions and scope
The Hilbert space has orthonormal ordered basis \((c_0,c_1,c_2,p_0,p_1,p_2)\). Fix

\[
C=\begin{pmatrix}0&-i&i\\ i&0&-i\\-i&i&0\end{pmatrix},\qquad
H=\begin{pmatrix}C&I_3\\I_3&0_3\end{pmatrix}.
\]

All triangle bonds have modulus one, and each \(c_j\) is connected only to \(p_j\) outside the triangle, also with modulus one. The diagonal entries vanish. The phase accumulated around the triangle has modulus \(\pi/2\) modulo \(2\pi\); reversing the cycle orientation exchanges the two flux signs and relabels directed site pairs, leaving the ceiling unchanged. Arbitrary diagonal-gauge rephasing changes amplitudes by endpoint phases but preserves all transfer probabilities.

The assertion is for all \(j,k\in\{0,1,2\}\), all \(t\geq0\), and exactly this fixed coupling/flux/energy model. It is not an optimization over flux, detuning, or hopping weights.

## Proof
**Fourier decomposition.** Write \(\omega=e^{2\pi i/3}\) and let \(v_s=3^{-1/2}(1,\omega^s,\omega^{2s})^T\) for \(s=0,1,2\). Direct multiplication gives \(Cv_0=0\), \(Cv_1=\sqrt3\,v_1\), and \(Cv_2=-\sqrt3\,v_2\). For each of these three Fourier modes, the full six-site Hamiltonian reduces exactly to the two-dimensional matrix

\[
B_\lambda=\begin{pmatrix}\lambda&1\\1&0\end{pmatrix},\qquad\lambda\in\{0,\sqrt3,-\sqrt3\}.
\]

Its internal-to-external transition amplitude is obtained by subtracting the scalar part and squaring the traceless part:

\[
\bigl[e^{-itB_\lambda}\bigr]_{2,1}
=-i\,e^{-i\lambda t/2}\frac{2}{\sqrt{\lambda^2+4}}
\sin\left(\frac{\sqrt{\lambda^2+4}\,t}{2}\right).
\]

For the zero Fourier mode this equals \(-i\sin t\). For the other two modes the oscillation frequency is \(\sqrt7/2\), with conjugate factors \(e^{\mp i\sqrt3\,t/2}\). Reassembling the three spectral projections, whose \((k,j)\) entries are \(1/3\), \(\omega^{k-j}/3\), and \(\omega^{-(k-j)}/3\), gives the exact boxed kernel in the Finding section.

**Upper bound.** Its imaginary bracket is real. The estimates \(|\sin t|\leq1\), \(|\sin(\sqrt7\,t/2)|\leq1\), and \(|\cos(\sqrt3\,t/2-2\pi(k-j)/3)|\leq1\) therefore yield

\[
\left|\langle p_k|e^{-itH}|c_j\rangle\right|
\leq\frac13\left(1+\frac4{\sqrt7}\right)
\]

for every real time and every site pair.

**Sharpness.** The three real numbers \(1,\sqrt3/2,\sqrt7/2\) are linearly independent over \(\mathbb Q\). Indeed, the independent sign-changing automorphisms of the biquadratic field \(\mathbb Q(\sqrt3,\sqrt7)\) show that \(a+b\sqrt3+c\sqrt7=0\), with rational coefficients, forces \(a=b=c=0\). Consequently the continuous positive-time Kronecker flow

\[
t\longmapsto\left(t,\frac{\sqrt3\,t}{2},\frac{\sqrt7\,t}{2}\right)\pmod{2\pi}
\]

is dense in the three-torus, including along arbitrarily large times. For each fixed \(j,k\), it therefore approaches the target phases \(\bigl(\pi/2,2\pi(k-j)/3,\pi/2\bigr)\), making both sine factors and the cosine factor simultaneously tend to \(+1\). The preceding upper bound is thus the exact supremum; squaring and simplifying gives \((23+8\sqrt7)/63\).

**Nonattainment.** Equality in the upper bound forces both \(|\sin t|=1\) and \(|\sin(\sqrt7\,t/2)|=1\). Thus \(t\) would be an odd multiple of \(\pi/2\), and \(\sqrt7\,t/2\) another odd multiple of \(\pi/2\). These two requirements would make \(\sqrt7\) rational, a contradiction. The supremum is consequently not a finite-time maximum. This proves every assertion.

## Verification
The included standalone program `verify.py` constructs the full Hermitian \(6\times6\) matrix independently, diagonalizes it numerically, compares all nine matrix-exponential transition amplitudes against the exact kernel at seven times, and checks additional boundedness instances. It verifies the six predicted eigenvalues and tests 4,563 site-time amplitudes in total. A separate finite scan along times with \(\sin t=1\) produces probabilities above \(0.7010\) for each cyclic site displacement; these are numerical lower approximations, **not** an infinite-time proof. Running `python verify.py` with NumPy reproduces the checks. The Kronecker argument and spectral derivation, not the finite tests, establish the general theorem.

## Relationship to prior work
Bottarelli, Frigerio, and Paris (arXiv:2302.08472; first public 16 February 2023), Section III, Eqs. (4)–(14), introduced and analyzed this exact six-site router with its single loop flux and showed nearly unit external-to-external transfer. Their eigenvector expressions and mixed-channel derivative relations supply a natural point of departure, but their displayed transfer probabilities and optimizations concern different initial/target configurations; they do not state the sharp internal-to-single-external all-time maximum or its nonattainment.

Acuaviva and collaborators (arXiv:2301.01473; first public 4 January 2023), Section 5.1, treat the same oriented-triangle-with-star graph as a rooted product. Their spectral projectors (Lemma 5.2) and transfer classification (Theorem 5.4) establish multiple pretty-good transfers **among the three non-pendant sites**; they do not establish the present cross-layer numerical supremum. The Fourier-sector eigenvalues here are consistent with their published decomposition. The novelty claimed is only the sharp cross-layer performance ceiling and finite-time nonattainment, not discovery of the graph, its spectrum, or its near-perfect same-layer transport.

Cavazzoni and collaborators' later work on perfect chiral quantum routing (arXiv:2406.11834; first public 17 June 2024) considers a different router topology and is not an implication of the present exact six-site cross-layer statement.

## Limitations
The sharp bound is at fixed loop-flux magnitude \(\pi/2\), equal unit-modulus hoppings, and zero on-site detuning. It need not survive optimization over those physical parameters, different graph topologies, target superpositions, or the addition of measurement, decoherence, or controls. It concerns site-to-site probability, not quantum-channel fidelity for an arbitrary encoded qubit. Dense recurrence can require long times; this result supplies no efficient waiting-time estimate. The prior-work comparison is based on the cited material and targeted searches; it does not constitute independent proof of global novelty or a comprehensive postpublication literature audit.

## References
1. A. Bottarelli, M. Frigerio, and M. G. A. Paris, *Quantum routing of information using chiral quantum walks*, arXiv:2302.08472 (first posted 2023-02-16), https://arxiv.org/html/2302.08472v2, Sec. III and Appendix A.
2. A. Acuaviva, A. Chan, S. Eldridge, C. Godsil, M. How-Chun-Lun, C. Tamon, E. Wright, and X. Zhang, *State Transfer in Complex Quantum Walks*, arXiv:2301.01473 (first posted 2023-01-04), https://arxiv.org/html/2301.01473v1, Sec. 5.1, Lemma 5.2 and Theorem 5.4.
3. E. Cavazzoni et al., *Perfect chiral quantum routing*, arXiv:2406.11834 (first posted 2024-06-17), https://arxiv.org/abs/2406.11834.
