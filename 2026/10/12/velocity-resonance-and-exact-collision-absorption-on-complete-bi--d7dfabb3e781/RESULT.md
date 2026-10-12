# Velocity resonance and exact collision absorption on complete bipartite quantum networks

## Finding
Let \(p,q\ge3\) be integers, and let two distinguishable, noninteracting quantum walkers move with positive, possibly unequal hopping strengths \(a,b\) on the same complete bipartite graph \(K_{p,q}\). Irreversible loss occurs at every coincidence vertex, with any strictly positive, vertex-dependent loss coefficients. Write \(N=p+q\) and \(\mathcal B\) for the largest subspace observable from the coincidence vertices, equivalently the spectral subspace that is eventually absorbed.

Then the exact absorption-space dimension is
\[
\dim\mathcal B=\begin{cases}5N-4,&a\ne b,\\3N-2,&a=b.\end{cases}
\]
For a computational-basis state \(|i,j\rangle\), let \(C(i,j)\) be the eventual absorption probability. If \(i=j\), then \(C(i,j)=1\). If \(i\ne j\) and the two vertices belong to the same first color class of size \(p\), or the same second class of size \(q\), or opposite classes, respectively, then
\[
\begin{array}{c|ccc}
&\text{both in first class}&\text{both in second class}&\text{opposite classes}\\ \hline
 a\ne b&\dfrac{2p-1}{p(p-1)}&\dfrac{2q-1}{q(q-1)}&\dfrac{p+q-1}{pq}\\[2mm]
 a=b&\dfrac{2q-1}{2pq-p-q}&\dfrac{2p-1}{2pq-p-q}&\dfrac{p+q-1}{2pq}
\end{array}
\]
In particular, exact equality of the hopping strengths removes \(2N-2\) absorbing directions; every opposite-class localized preparation has exactly half its unequal-speed absorption probability at that equality. Arbitrarily small nonzero mismatch restores those directions in the infinite-time limit. The rates of positive loss do not change these limits.

## Assumptions and scope
The vertex set is a disjoint union \(X=A\sqcup B\) with \(|A|=p\ge3\), \(|B|=q\ge3\); the single-particle adjacency matrix \(J\) is \(1\) between opposite classes and \(0\) otherwise. The two-particle Hilbert space is \(\mathbb C^N\otimes\mathbb C^N\) with ordered basis \(|i,j\rangle\), and the Hermitian Hamiltonian is
\[
H=aJ\otimes I_N+bI_N\otimes J,\qquad a,b>0.
\]
The lossy evolution is \(\psi(t)=e^{-itK}\psi(0)\) with
\[
K=H-i\Gamma,\qquad\Gamma=\sum_{x\in X}\gamma_x|x,x\rangle\langle x,x|,\quad\gamma_x>0.
\]
Thus the norm-loss flux at site \(x\) equals \(2\gamma_x|\langle x,x|\psi(t)\rangle|^2\). There is no conditioning, no dephasing, no coherent interaction at coincidence, and no symmetrization between the distinguishable walkers. The result concerns \(t\to\infty\), not uniform finite-time capture. The threshold \(p,q\ge3\) is essential to the stated formulas because the zero-eigenspace detector Gram matrix has different rank for a two-vertex class.

## Proof
**1. Spectral observability is exactly eventual loss.** Let \(D:\mathbb C^N\to\mathbb C^{N^2}\) send \(e_x\) to \(|x,x\rangle\). For each distinct real eigenvalue \(E\) of \(H\), write \(\Pi_E\) for its orthogonal spectral projector and define
\[
\mathcal B=\bigoplus_{E\in\sigma(H)}\operatorname{ran}(\Pi_E D).
\]
This is the minimal \(H\)-invariant subspace containing all detector states, so its orthogonal complement is the maximal \(H\)-invariant subspace contained in \(\ker\Gamma\). The non-Hermitian evolution is contractive since \(\tfrac{d}{dt}\|\psi(t)\|^2=-2\langle\psi(t),\Gamma\psi(t)\rangle\le0\). A real-eigenvalue eigenvector of \(K\) satisfies \(\langle\psi,\Gamma\psi\rangle=0\), hence \(\Gamma\psi=0\) and \(H\psi=E\psi\); these are exactly the dark directions. A Jordan chain at a real eigenvalue would make the contraction semigroup polynomially unbounded, so none exists. All eigenvalues on \(\mathcal B\) therefore have strictly negative imaginary parts, and its component decays. It follows that
\[
C(i,j)=\langle i,j|P_{\mathcal B}|i,j\rangle
\]
for every normalized basis state, with \(P_{\mathcal B}\) the orthogonal projector onto \(\mathcal B\).

**2. Single-particle spectral decomposition.** Put
\[
u_A=p^{-1/2}\sum_{i\in A}|i\rangle,\quad u_B=q^{-1/2}\sum_{j\in B}|j\rangle,\quad |\pm\rangle=(u_A\pm u_B)/\sqrt2.
\]
Then \(J|\pm\rangle=\pm\sqrt{pq}|\pm\rangle\). Its zero eigenspace is \(U=U_A\oplus U_B\), where \(U_A\) and \(U_B\) are the zero-sum subspaces of dimensions \(p-1\) and \(q-1\). Let \(P_U\) project onto \(U\), and set \(w_i=P_U|i\rangle\). Within a class of size \(r\in\{p,q\}\),
\[
\langle w_i,w_j\rangle=\delta_{ij}-1/r,\qquad \langle w_i,w_j\rangle=0\text{ for opposite classes}.
\]
The two-particle Hamiltonian eigenvalues are \(\sqrt{pq}(a\lambda+b\mu)\) with \(\lambda,\mu\in\{+1,0,-1\}\). Each coincidence detector has a nonzero component in each of the four one-dimensional \(|\pm\rangle\otimes|\pm\rangle\) sectors. It also spans each available \(|\pm\rangle\otimes U\) and \(U\otimes|\pm\rangle\) sector: its projections are nonzero multiples of \(|\pm\rangle\otimes w_i\) and \(w_i\otimes|\pm\rangle\), and the \(w_i\) span \(U\).

**3. Zero-energy detector Gram matrices.** Let \(G_r\) be the \(r\times r\) matrix with entries \((\delta_{ij}-1/r)^2\). Its eigenvalue on the constant vector is \((r-1)/r\), and its eigenvalue on the \((r-1)\)-dimensional zero-sum space is \((r-2)/r\). Both are strictly positive for \(r\ge3\).

For \(a\ne b\), the zero-energy sector contains \(U\otimes U\), and detector projections into it have Gram matrix \(G_p\oplus G_q\), of rank \(N\). The four one-dimensional sign sectors contribute rank four and the four sign–zero sectors contribute \(4(N-2)\). The resulting dimension is \(N+4+4(N-2)=5N-4\).

The only additional degeneracies for positive unequal speeds can occur at ratios \(a/b=2\) or \(1/2\). At those ratios, the coinciding sign–sign and sign–zero sectors transform in inequivalent representations (trivial versus zero-sum) of the color-preserving permutation group \(S_p\times S_q\). Group averaging splits the detector image orthogonally into these representations, so their observable ranks still add. Thus the dimension calculation does not silently assume generic irrational hopping ratios.

For \(a=b\), the two sign–zero sectors of each energy \(\pm a\sqrt{pq}\) coalesce. Their detector images occupy only the symmetric subspace \((|\pm\rangle\otimes U+U\otimes|\pm\rangle)/\sqrt2\) and contribute \(N-2\) directions at each sign. The zero-energy sector additionally contains the unit vector
\[
v=(u_A\otimes u_A-u_B\otimes u_B)/\sqrt2,
\]
coming from the symmetric combination of \(|+\rangle\otimes|-\rangle\) and \(|-\rangle\otimes|+\rangle\). Its detector Gram matrix is \(G_p\oplus G_q+zz^{\mathsf T}\), where \(z_i=1/(\sqrt2p)\) on \(A\), and \(z_j=-1/(\sqrt2q)\) on \(B\). The old positive definite Gram matrix remains positive definite, so the merged zero-energy detector image has rank exactly \(N\). The two unmixed sign–sign sectors contribute rank two, giving \(N+2(N-2)+2=3N-2\).

**4. Localized probabilities.** For a given eigenspace with detector Gram matrix \(M=D^*\Pi_E D\), the squared norm of the absorbing projection of a state \(|x\rangle\) in that eigenspace is \(b^*M^+b\), where \(b=D^*\Pi_E|x\rangle\) and \(M^+\) is its Moore–Penrose inverse. The orthogonal eigenspace contributions sum.

If \(a\ne b\), for distinct \(i,j\in A\) the four sign–sign sectors together contribute \(1/p^2\), the four sign–zero sectors together contribute \(2(p-1)/p^2\), and \(U\otimes U\) contributes
\[
\frac2{p^2}+\frac1{p^2(p-1)}.
\]
Their sum is \((2p-1)/(p(p-1))\). For \(i,j\in B\), replace \(p\) by \(q\). For opposite classes, the zero-energy projection is orthogonal to every detector projection; the other sectors contribute \(1/(pq)+(p+q-2)/(pq)=(p+q-1)/(pq)\).

If \(a=b\), for distinct \(i,j\in A\) the \(\pm2a\sqrt{pq}\) sectors contribute \(1/(2p^2)\), the \(\pm a\sqrt{pq}\) sectors contribute \((p-2)/p^2\), and the merged zero sector contributes
\[
\frac2{p^2}+\frac{p+q}{2p^2(2pq-p-q)}.
\]
The last expression follows by diagonalizing the rank-one-updated Gram matrix into the two class-standard spaces and the two-dimensional constant space; on the latter the matrix is
\[
\begin{pmatrix}1-\frac1{2p}&-\frac1{2\sqrt{pq}}\\ -\frac1{2\sqrt{pq}}&1-\frac1{2q}\end{pmatrix}.
\]
The sum simplifies to \((2q-1)/(2pq-p-q)\); exchanging the classes gives the other same-class formula. For opposite classes, the merged zero-sector detector image is orthogonal to the initial state, while the \(\pm2a\sqrt{pq}\) and \(\pm a\sqrt{pq}\) contributions are \(1/(2pq)\) and \((p+q-2)/(2pq)\), respectively. The cross-class formula follows. A coincidence basis state lies in \(\operatorname{ran}D\subseteq\mathcal B\), so its probability is one. This completes the proof.

## Verification
The standalone file `verify_bipartite.py` constructs the full two-particle Hermitian Hamiltonian, groups its exact-in-principle spectral clusters numerically, and computes the observable projector from singular-value decompositions of each detector overlap matrix. It checks dimensions, projector idempotence, commutation with the Hamiltonian, and every localized probability for \((p,q)=(3,3),(3,4),(3,5),(4,4),(4,5),(5,3),(5,5)\), using equal rates, two rational speed ratios including the exceptional \(2{:}1\), and an irrational ratio. It also checks the number of undamped eigenvalues of the full non-Hermitian operator at unequal positive detector rates in six small cases. Run `python verify_bipartite.py` with the versions in `requirements.txt`; a successful check prints `VERIFY_OK`.

The recorded verification produced `VERIFY_OK spectral_cases=35 localized_probabilities=2290 loss_spectra=6 max_error=6.44e-15`. The numerical tests are corroboration only; the preceding all-size proof supplies the infinite-family result.

## Relationship to prior work
Štefaňák, Kiss, Jex, and Mohring (arXiv:0705.1985v1, especially §§2–4) introduced a two-particle *meeting* problem for coined **discrete-time** walks on an infinite line; they did not study continuous-time irreversible coincidence loss on complete bipartite graphs. Carson, Loke, and Wang (arXiv:1511.04828v1, §§II–IV) studied entanglement dynamics in interacting coined discrete-time two-particle walks, also without the present absorbing model. Razzoli, Paris, and Bordone (arXiv:2011.13794v2, §4.1 and Appendix B.1) treated a **single-particle**, single-trap complete-bipartite transport problem with a Laplacian Hamiltonian. Their observability framework is an important methodological antecedent, but their single-trap formulas do not imply this two-particle, all-coincidence-detector classification.

The exact all-\(p,q\) resonance law, dimension jump, and four localized probability classes are the assessed claim. Search failure cannot establish absolute novelty, and stronger unlocated results in spectral observability or two-particle trapping remain possible.

## Limitations
The theorem assumes \(p,q\ge3\), positive real hopping strengths, homogeneous hopping along graph edges for each walker, distinguishable noninteracting particles, all coincidence vertices absorbing at positive rates, and no additional decoherence. Two-vertex color classes have exceptional Gram ranks and are excluded. The asserted discontinuity concerns only the infinite-time limit: at fixed finite time the lossy propagator depends continuously on \(a,b\). No uniform capture-time bound as \(a\to b\) is supplied. This is not an assertion about arbitrary initial superpositions beyond the projector characterization, or about arbitrary graph perturbations. Independent publication-priority assessment has not been performed.

## References
1. M. Štefaňák, T. Kiss, I. Jex, and B. Mohring, *The meeting problem in the quantum random walk*, arXiv:0705.1985v1, publicly submitted 14 May 2007, https://arxiv.org/html/0705.1985v1 .
2. G. R. Carson, T. Loke, and J. B. Wang, *Entanglement dynamics of two-particle quantum walks*, arXiv:1511.04828v1, publicly submitted 16 November 2015, https://arxiv.org/html/1511.04828v1 .
3. L. Razzoli, M. G. A. Paris, and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794v2 (originally public 27 November 2020), especially §4.1 and Appendix B.1, https://arxiv.org/html/2011.13794v2 .
