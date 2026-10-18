# Arithmetic dark-state resonances and sharp near-resonance lifetimes in antipodally linked hypercubes

## Finding

Let \(d\ge2\) be an integer, \(J>0\), \(\gamma>0\), and \(\lambda\in\mathbb R\). On the Hilbert space \(\mathbb C^{2^d}\) indexed by binary words, let \(X_j\) flip coordinate \(j\), let \(P=X_1\cdots X_d\) flip all coordinates, and define
\[
H_\lambda=J\left(\sum_{j=1}^d X_j+\lambda P\right),\qquad
K_\lambda=-iH_\lambda-\frac{\gamma}{2}|0^d\rangle\langle0^d|.
\]
Start at \(|1^d\rangle\). The probability of absorption at the continuously monitored vertex \(|0^d\rangle\) is
\[
p_d(\lambda)=1-\lim_{t\to\infty}\|e^{tK_\lambda}|1^d\rangle\|^2.
\]
Set \(q_k=2^{-d}\binom dk\) for \(0\le k\le d\). For every positive odd integer \(r\), put
\[
\mathcal I_+(r)=\{(k,k+r):1\le k\le d-r,\ k\ \mathrm{odd}\},\qquad
\mathcal I_-(r)=\{(k,k+r):0\le k\le d-r,\ k\ \mathrm{even}\}.
\]
Then \(p_d(\lambda)=1\) except when \(\lambda=r\) and \(\mathcal I_+(r)\ne\varnothing\), or \(\lambda=-r\) and \(\mathcal I_-(r)\ne\varnothing\). At those values,
\[
\boxed{p_d(\pm r)=1-4\sum_{(k,l)\in\mathcal I_\pm(r)}\frac{q_kq_l}{q_k+q_l}.}
\]
In particular, for every \(d\ge2\), \(p_d(1)=p_d(-1)=1/(d+1)\), while \(p_d(\lambda)=1\) for all sufficiently close \(\lambda\ne\pm1\).

For every nonresonant \(\lambda\), the unconditional mean absorption time is finite and equals
\[
T_d(\lambda)=\int_0^\infty\|e^{tK_\lambda}|1^d\rangle\|^2\,dt.
\]
For any resonant \(\lambda_0=\pm r\) with nonempty \(\mathcal I_\pm(r)\), the exact quadratic detuning law is
\[
\boxed{\lim_{\lambda\to\lambda_0,\ \lambda\ \mathrm{nonresonant}}(\lambda-\lambda_0)^2T_d(\lambda)
=\frac{\gamma}{4J^2}\sum_{(k,l)\in\mathcal I_\pm(r)}(q_k+q_l)^2>0.}
\]
The limit holds for fixed \(d,J,\gamma\), from either side. At the unit positive resonance, write \(C_d=\frac14\sum_{1\le k<d,\ k\ \mathrm{odd}}(q_k+q_{k+1})^2\). Then
\[
\boxed{\lim_{d\to\infty}\sqrt d\,C_d=\frac1{2\sqrt\pi}.}
\]
This last limit is taken **after** determining the fixed-dimensional detuning coefficient; no uniform joint limit in dimension and detuning is claimed.

## Assumptions and scope

The Hamiltonian is the *adjacency-type* coherent hopping operator stated above, with no onsite disorder, bulk dephasing, or other loss. The \(P\)-term models coherent antipodal perfect-matching links; \(\lambda=1\) yields an unweighted antipodally augmented cube. The detector is a single irreversible Markovian sink and the initial state is precisely its antipode. All rates and energy scales are as defined; no normalization of \(J\) or \(\gamma\) is implicit. At a resonance, the unconditional mean absorption time is infinite because some norm survives; the detuning limit concerns nearby nonresonant systems.

## Proof

**Spectral compression and collision classification.** The Walsh characters of weight \(k\) diagonalize all coordinate flips and \(P\). The permutation-symmetric weight-\(k\) unit vector has energy
\[
E_k=J\big(d-2k+\lambda(-1)^k\big)
\]
and overlaps \(v_k=\sqrt{q_k}\) with the detected vertex and \(\psi_k=(-1)^k\sqrt{q_k}\) with the antipode. All other Walsh combinations are irrelevant to these two vectors and invariant under the loss. Hence the actual dynamics of the initial state lie in the \((d+1)\)-dimensional space where \(K=-i\operatorname{diag}(E_k)-\gamma vv^* /2\).

For \(k<l\), equality \(E_k=E_l\) is impossible for equal parity. For opposite parity, equality holds precisely when \(\lambda=l-k\) and \(k\) is odd, or when \(\lambda=-(l-k)\) and \(k\) is even. Here \(l-k\) is necessarily odd. At any fixed exceptional \(\lambda\), the collisions are *disjoint pairs* in exactly one of the sets \(\mathcal I_\pm(r)\); there are no triple collisions.

**Exact eventual detection.** For a finite-dimensional sink \(-\gamma vv^*/2\), the nondecaying subspace is the orthogonal sum, over distinct eigenspaces of its Hermitian Hamiltonian, of the vectors orthogonal to each eigenspace's projection of \(v\). Thus, writing \(\Pi_E\) for the spectral projections, the bright fraction is
\[
p_d(\lambda)=\sum_E\frac{|\langle v,\Pi_E\psi\rangle|^2}{\|\Pi_Ev\|^2},
\]
where zero denominators are omitted. If all energies are distinct, the sum is \(\sum_k q_k=1\). A colliding opposite-parity pair replaces the generic contribution \(q_k+q_l\) by \((q_k-q_l)^2/(q_k+q_l)\), a decrease of \(4q_kq_l/(q_k+q_l)\). This gives the complete exceptional-value formula.

For \(r=1\), the identity \(\binom dk\binom d{k+1}/(\binom dk+\binom d{k+1})=\binom dk(d-k)/(d+1)\), together with \(\sum_{k\ \mathrm{odd}}\binom dk(d-k)=\sum_{k\ \mathrm{even}}\binom dk(d-k)=d2^{d-2}\) over \(0\le k<d\), gives \(p_d(\pm1)=1/(d+1)\).

**Exact coefficient of the mean-time pole.** Away from collisions, \(v_k>0\) and all \(E_k\) are distinct, so no eigenvector of \(K\) can have zero decay. Hence \(K\) is Hurwitz, and \(W=\int_0^\infty e^{tK^*}e^{tK}\,dt\) is the unique Hermitian solution of \(K^*W+WK=-I\). Let \(w_i=(Wv)_i\) and \(\Delta_{ij}=E_i-E_j\). The diagonal Lyapunov identities give \(\operatorname{Re}w_i=1/(\gamma v_i)\); taking imaginary parts of the row sums in the off-diagonal identities gives the *exact* formulas
\[
\operatorname{Im}w_i=y_i=-\frac1{2v_i}\sum_{j\ne i}\frac{q_i+q_j}{\Delta_{ij}},\qquad
\operatorname{Re}W_{ij}=\frac{\gamma}{2\Delta_{ij}}(v_jy_i-v_iy_j)\quad(i\ne j).
\]
Writing \(\sigma_i=(-1)^i\), and comparing \(\psi^*W\psi\) with \(v^*Wv=\sum_i v_i\operatorname{Re}w_i=(d+1)/\gamma\), yields
\[
T_d(\lambda)=\frac{d+1}{\gamma}+\gamma\sum_{i<j}(\sigma_i\sigma_j-1)
\frac{v_iv_j(v_jy_i-v_iy_j)}{\Delta_{ij}}.
\]
At an isolated resonance pair \((i,j)\), \(\sigma_i\sigma_j=-1\). As its gap \(\Delta=\Delta_{ij}\to0\), the divergent parts satisfy
\[
y_i=-\frac{q_i+q_j}{2v_i\Delta}+O(1),\qquad
 y_j=\frac{q_i+q_j}{2v_j\Delta}+O(1).
\]
Its contribution to \(T_d\) is therefore \(\gamma(q_i+q_j)^2/\Delta^2+O(|\Delta|^{-1})\). Distinct collision pairs are disjoint, and all other terms are at worst first-order poles. Because \(|\Delta|=2J|\lambda-\lambda_0|\), adding the pair contributions proves the positive quadratic coefficient.

**Dimension asymptotic.** The elementary binomial identity \(q_k+q_{k+1}=2^{-d}\binom{d+1}{k+1}\) reduces \(4C_d\) to the even-index binomial-square sum, omitting endpoints. By Vandermonde's identity and the alternating binomial-square identity, it equals \(2^{-1}4^{-d}\binom{2d+2}{d+1}\) up to the negligible endpoint corrections and, for odd \(d\), a parity term of order \(4^{-d}2^d\). The central binomial asymptotic \(\binom{2m}{m}\sim 4^m/\sqrt{\pi m}\) gives \(\sqrt d\,C_d\to1/(2\sqrt\pi)\).

## Verification

The included `verify.py` and `requirements.txt` reproduce finite checks with `python verify.py`. Checks include exact rational pair weights for dimensions \(2\) through \(18\); direct full \(2^d\)-site non-Hermitian propagation against the Fourier-compressed evolution; matrix Lyapunov identities; detuning coefficients at the lowest resonances; and large-dimensional central-binomial comparisons. The numerical tests are not a substitute for the preceding all-dimensional proof and do not certify a joint detuning-dimension limit.

## Relationship to prior work

Mulherkar (arXiv:2609.04503, first public 2026-09-03) studies one-shot and concurrent hitting on cubelike graphs for a **discrete-time Grover-coined** quantum walk. The present setting is a continuously evolving, uncoined coherent walk with one Lindblad sink and a tunable coherent antipodal shortcut; the original motivating preprint's abstract, not its full manuscript, was accessible for comparison. Thiel, Mualem, Kessler, and Barkai (arXiv:1909.02114) establish the general bright/dark spectral-projector viewpoint for **periodic projective** measurements and discuss hypercube examples. That general viewpoint is used here, not claimed as novel. Liu, Yin, Ziegler, and Barkai (Physical Review Research 2, 033113, 2020) already analyze inverse-square mean detection-time divergences near *stroboscopic sampling* degeneracies. We do **not** claim inverse-square divergence in itself is new; the result here is its exact continuous-Lindblad coefficient and arithmetic classification for the tunable antipodal hypercube family.

## Limitations

The result is an exact theorem for this specific model, not a uniqueness or publication-priority certificate. Its exceptional values are exact-coherent degeneracies: onsite disorder, other sink locations, additional decoherence, or different detection protocols need not preserve them. The mean-time asymptotic is for fixed dimension before the dimension limit. The full recent motivating preprint was not available for detailed comparison, leaving residual priority uncertainty, although its stated model and main theorem differ materially. No independent scientific audit is claimed.

## References

1. J. Mulherkar, *One-Shot and Concurrent Hitting Times for Grover-Coined Quantum Walks on Cubelike Graphs*, arXiv:2609.04503, first posted 2026-09-03, https://arxiv.org/abs/2609.04503 .
2. F. Thiel, I. Mualem, D. A. Kessler, E. Barkai, *Quantum total detection probability from repeated measurements II. Exploiting symmetry*, arXiv:1909.02114, https://ar5iv.labs.arxiv.org/html/1909.02114 .
3. Q. Liu, R. Yin, K. Ziegler, E. Barkai, *Quantum walks: The mean first detected transition time*, Physical Review Research 2, 033113 (2020), DOI:10.1103/PhysRevResearch.2.033113, https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.2.033113 .
4. T. Yamasaki, H. Kobayashi, H. Imai, *Analysis of absorbing times of quantum walks*, Physical Review A 68, 012302 (2003), DOI:10.1103/PhysRevA.68.012302 (discrete-time symmetric hypercube absorption).
