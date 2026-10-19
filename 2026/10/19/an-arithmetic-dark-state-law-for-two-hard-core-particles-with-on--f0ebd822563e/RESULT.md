# An arithmetic dark-state law for two hard-core particles with one pair-loss bond

## Finding

Let \(p\ge5\) be an odd prime. On the open path with \(p-1\) vertices, put two indistinguishable hard-core particles with real nonzero nearest-neighbor hopping. Loss occurs only when the configuration is \(|1,2\rangle\): a single jump transfers that pair into an absorbing vacuum. For every initially localized pair \(|i,j\rangle\), \(1\le i<j\le p-1\), its infinite-time **two-particle survival probability** is

\[
S_p(i,j)=\begin{cases}
0,&i+j\text{ even},\\[3pt]
\dfrac{2+\mathbf1_{\{i+j=p\}}}{p}
-\dfrac{1}{2p}\left(\mathbf1_{\{j-i=1\}}-\mathbf1_{\{j-i=3\}}+\mathbf1_{\{i+j\in\{3,2p-3\}\}}\right)^2,
&i+j\text{ odd}.
\end{cases}
\]

Here \(\mathbf1_E\) equals one exactly when condition \(E\) holds. The dimension of the exactly protected two-particle space is \((p-3)/2\). In particular, configurations with both particles on the same parity sublattice lose both particles with probability one, whereas many opposite-parity configurations retain a strictly positive probability. The result is valid for every nonzero hopping strength and every positive loss rate; it specifies eventual, not finite-time, survival.

## Assumptions and scope

The Hilbert space for two particles is \(\mathcal H_2=\operatorname{span}\{|i,j\rangle:1\le i<j\le p-1\}\), with the standard orthonormal localized-pair basis. The hard-core kinetic Hamiltonian \(H_2\) moves one particle by one edge whenever this does not cause double occupation; every allowed matrix element has the same real value \(h\ne0\). A unique jump \(L=\sqrt\kappa\,|\mathrm{vac}\rangle\langle1,2|\), \(\kappa>0\), annihilates the occupied boundary bond. The vacuum is absorbing and there are no other jumps or driving terms.

The no-jump effective Hamiltonian on \(\mathcal H_2\) is
\[
K=H_2-\frac{i\kappa}{2}|1,2\rangle\langle1,2|.
\]
Starting from \(|i,j\rangle\), the probability of remaining in the two-particle sector at time \(t\) is \(\|e^{-itK}|i,j\rangle\|^2\). Its nonincreasing limit is \(S_p(i,j)\). No assumption about the ratio \(\kappa/|h|\) is made. In particular, \(p-1\) is even, and the primality of \(p\) is used essentially to exclude accidental nonzero-energy degeneracies.

## Proof

**1. Free-fermion spectral representation.** In the ordered basis \(i<j\), the open-path hard-core two-particle Hamiltonian is the second exterior power of the one-particle path adjacency Hamiltonian. The one-body orthonormal eigenvectors and eigenvalues are
\[
\phi_k(x)=\sqrt{\frac{2}{p}}\sin\left(\frac{\pi kx}{p}\right),
\qquad \varepsilon_k=2h\cos\left(\frac{\pi k}{p}\right),
\qquad 1\le k\le p-1.
\]
Thus \(w_{k\ell}=\phi_k\wedge\phi_\ell\), \(k<\ell\), form an orthonormal basis of \(\mathcal H_2\), with energies \(E_{k\ell}=\varepsilon_k+\varepsilon_\ell\). Their boundary-bond amplitudes are
\[
w_{k\ell}(1,2)=\frac{4}{p}
\sin\frac{\pi k}{p}\sin\frac{\pi\ell}{p}
\left(\cos\frac{\pi\ell}{p}-\cos\frac{\pi k}{p}\right)\ne0.
\]
Indeed all sines are nonzero, and cosine is strictly decreasing on the relevant interval.

**2. Prime-denominator nonresonance.** Set \(r=(p-1)/2\). The real numbers \(\cos(\pi k/p)\), \(1\le k\le r\), are linearly independent over \(\mathbb Q\). To see this, put \(\zeta=e^{2\pi i/p}\) and \(u=(p+1)/2\). Then
\[
2\cos\frac{\pi k}{p}=(-1)^k\bigl(\zeta^{uk}+\zeta^{-uk}\bigr).
\]
As \(k\) ranges from \(1\) to \(r\), the unordered pairs \(\{uk,-uk\}\pmod p\) run over all nonzero residue pairs. A rational linear relation would give a polynomial of degree at most \(p-1\) with zero constant coefficient and root \(\zeta\). The minimal polynomial \(1+X+\cdots+X^{p-1}\) forces that polynomial to vanish identically, hence every relation coefficient is zero.

Moreover, \(\varepsilon_{p-k}=-\varepsilon_k\). Consequently the only repeated two-particle energy is zero, whose eigenspace is
\[
\mathcal Z=\operatorname{span}\{u_k=w_{k,p-k}:1\le k\le r\},
\qquad \dim\mathcal Z=r.
\]
Every nonzero two-particle energy is simple: equality of two nonzero signed sums of independent basis energies forces the same occupied one-body modes. Since all \(w_{k\ell}(1,2)\) are nonzero, no nonzero-energy eigenvector avoids the loss configuration. The loss-invisible subspace is therefore
\[
\mathcal D=\{\psi\in\mathcal Z:\langle1,2|\psi\rangle=0\},
\qquad \dim\mathcal D=r-1=(p-3)/2.
\]

**3. Exact dark projector.** Let \(Q\) be the orthogonal projector onto \(\mathcal Z\) and \(b=|1,2\rangle\). Because \(Qb\ne0\), the orthogonal projector onto \(\mathcal D\) is
\[
P_{\mathcal D}=Q-\frac{Q|b\rangle\langle b|Q}{\langle b|Q|b\rangle}.
\]
The identity \(\phi_{p-k}(x)=(-1)^{x+1}\phi_k(x)\) implies
\[
u_k(i,j)=\begin{cases}
0,&i+j\text{ even},\\
\dfrac{4(-1)^i}{p}\sin\frac{\pi ki}{p}\sin\frac{\pi kj}{p},&i+j\text{ odd}.
\end{cases}
\]
For odd \(i+j\), elementary product-to-sum identities and the finite geometric sum
\[
\sum_{k=1}^{p-1}\cos\left(\frac{2\pi ak}{p}\right)
=\begin{cases}p-1,&p\mid a,\\-1,&p\nmid a\end{cases}
\]
give the two exact trigonometric evaluations
\[
\sum_{k=1}^{r}\sin^2\frac{\pi ki}{p}\sin^2\frac{\pi kj}{p}
=\frac p8+\frac p{16}\mathbf1_{\{i+j=p\}},
\]
and, with \(B_{ij}=\mathbf1_{\{j-i=1\}}-\mathbf1_{\{j-i=3\}}+\mathbf1_{\{i+j\in\{3,2p-3\}\}}\),
\[
\sum_{k=1}^{r}\sin\frac{\pi ki}{p}\sin\frac{\pi kj}{p}
\sin\frac{\pi k}{p}\sin\frac{2\pi k}{p}
=\frac p{16}B_{ij}.
\]
For clarity, the second formula follows by applying
\(2\sin A\sin B=\cos(A-B)-\cos(A+B)\) twice: its four residue tests are \(i-j\equiv\pm1,\pm3\pmod{2p}\) and \(i+j\equiv3,2p-3\), which reduce, in the stated range and opposite-parity case, to exactly the three indicators in \(B_{ij}\). The same identity yields the first sum upon squaring the two sines and using the fact that \(i\ne j\). In particular,
\[
Q_{ij,ij}=\frac{2+\mathbf1_{\{i+j=p\}}}{p},\quad
Q_{ij,12}=\frac{(-1)^{i+1}B_{ij}}p,\quad
Q_{12,12}=\frac2p
\]
for odd \(i+j\). All entries involving an even-sum configuration vanish. Taking the diagonal of \(P_{\mathcal D}\) yields exactly the displayed piecewise survival law.

**4. Equivalence to long-time absorption.** For any eigenpair \(Kv=zv\) with \(v\ne0\), taking imaginary parts of \(\langle v,Kv\rangle\) gives
\[
\operatorname{Im}z=-\frac\kappa2\frac{|\langle b,v\rangle|^2}{\|v\|^2}\le0.
\]
Equality forces \(\langle b,v\rangle=0\) and then \(H_2v=zv\), so \(v\in\mathcal D\). Conversely \(K\) vanishes on \(\mathcal D\), which is reducing for \(K\). Every eigenvalue of the complementary finite-dimensional block has strictly negative imaginary part, hence the complementary no-jump propagator decays to zero, including possible Jordan blocks. Therefore
\[
\lim_{t\to\infty}\|e^{-itK}|i,j\rangle\|^2
=\langle i,j|P_{\mathcal D}|i,j\rangle=S_p(i,j).
\]
This proves the claim for all admissible hopping strengths and loss rates.

## Verification

Run `python verify.py` with the versions or compatible newer versions in `requirements.txt`. The checker constructs the hard-core configuration adjacency independently from allowed particle moves; diagonalizes the full finite-dimensional Hamiltonian; forms the full spectral sink-invisible projector, including every numerically detected energy degeneracy; checks idempotence, sink orthogonality, invariance, rank, and all sitewise values against the closed formula for \(p\in\{5,7,11,13,17,19\}\). A separate non-Hermitian propagation check compares finite-time two-particle survival with the dark projector at large times for two small systems and two loss strengths.

These finite checks are not the proof for arbitrary primes. The proof is the cyclotomic nonresonance argument, the two exact finite trigonometric sums, and the spectral decay argument above.

## Relationship to prior work

Krovi and Brun's quantum-walk dark-subspace criterion and Krapivsky, Luck, and Mallick's trap-survival treatment motivate reducing absorption to a protected spectral projector, but their considered walks are single-particle rather than the two-particle configuration graph with one pair-loss jump. Large, Underwood, and Feder discuss the hard-core/free-fermion description of particles on paths, without localized two-particle loss. Everest, Hush, and Lesanovsky treat hard-core bosons with nonlocal two-body loss on many bonds, emphasizing a spatially distributed strong-loss/Zeno regime; that is distinct from the one-bond loss and all-positive-rate eventual survival solved here. Marché and collaborators consider translationally invariant **on-site** two-body losses for soft-core particles and different long-time decay questions. The contribution assessed here is the prime-length, all-start, closed sitewise probability and dark-space dimension for a single adjacent-pair absorber—not a new claim about those existing general methods.

## Limitations

The theorem is specific to two particles, an open uniform path with \(p-1\) vertices for odd prime \(p\), and a unique absorbing pair configuration at the first bond. Primality is a sufficient arithmetic nonresonance condition; this result does not classify composite path lengths, multiple lossy bonds, other initial coherent superpositions, inhomogeneous hopping, or finite-time decay rates. The total number of surviving particles after a loss jump is zero by model definition; a different particle-loss channel might leave one particle. Literature priority remains subject to independent assessment.

## References

1. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094 (first posted 2006-06-10), https://arxiv.org/abs/quant-ph/0606094.
2. P. L. Krapivsky, J. M. Luck, and K. Mallick, *Survival of classical and quantum particles in the presence of traps*, arXiv:1311.6298 (2013), https://arxiv.org/abs/1311.6298.
3. B. Everest, M. R. Hush, and I. Lesanovsky, *Many-body out-of-equilibrium dynamics of hard-core lattice bosons with non-local loss*, arXiv:1406.6097 (2014), https://arxiv.org/abs/1406.6097.
4. N. Large, M. Underwood, and D. L. Feder, *Perfect quantum state transfer of hard-core bosons on weighted path graphs*, arXiv:1412.1022 (2014), https://arxiv.org/abs/1412.1022.
5. Marché et al., *Universality and two-body losses: lessons from the effective non-Hermitian dynamics of two particles*, arXiv:2405.04789 (2024), https://arxiv.org/abs/2405.04789.
