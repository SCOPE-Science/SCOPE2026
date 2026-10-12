# Collision-darkening and exchange-selective reaction on complete quantum networks

## Finding
For every integer \(n\ge4\), two distinguishable walkers on the complete graph \(K_n\) react irreversibly whenever they meet. Their coherent hopping strengths are independently chosen as positive numbers \(a,b\), and all coincidence reaction rates are strictly positive and may differ by site. The exact dimension of the absorbing subspace is
\[
\operatorname{rank}\Pi_{\mathrm{abs}}=
\begin{cases}3n-1,&a\ne b,\\2n,&a=b.\end{cases}
\]
Every localized pair on the same site reacts eventually with probability one. For two distinct starting sites \(x\ne y\),
\[
\eta(|x,y\rangle)=
\begin{cases}\dfrac{2n-1}{n(n-1)},&a\ne b,\\[2pt]\dfrac1{n-1},&a=b.\end{cases}
\]
Thus an arbitrarily small hopping mismatch increases the eventual reaction probability by exactly \(1/n\). For the normalized exchange-symmetric and exchange-antisymmetric preparations
\[
|\psi_\pm\rangle=(|x,y\rangle\pm|y,x\rangle)/\sqrt2,
\]
the complete formulas are
\[
\eta(\psi_+)=\frac2{n-1},\qquad
\eta(\psi_-)=\begin{cases}2/n,&a\ne b,\\0,&a=b.\end{cases}
\]
In particular, the hopping mismatch changes only the antisymmetric channel for these two preparations; its effect on the localized product input is half as large. All these exact probabilities are independent of the positive loss rates.

## Assumptions and scope
The site labels are \(\{0,\ldots,n-1\}\), with \(n\ge4\). Let \(A=J-I\) be the adjacency matrix of \(K_n\), and let
\[
H=aA\otimes I+bI\otimes A,\quad
\Gamma=\sum_{j=0}^{n-1}\kappa_j|j,j\rangle\langle j,j|,
\quad a,b,\kappa_j>0.
\]
For every normalized initial vector \(\psi\in\mathbb C^n\otimes\mathbb C^n\), the no-jump state is \(\psi_t=\exp[(-iH-\Gamma/2)t]\psi\), in units with \(\hbar=1\). The eventual reaction probability is
\[
\eta(\psi)=\int_0^\infty \langle\psi_t,\Gamma\psi_t\rangle\,dt
=1-\lim_{t\to\infty}\|\psi_t\|^2.
\]
The two walkers are distinguishable, even when prepared in exchange-symmetric or exchange-antisymmetric superpositions. Unequal hopping would not describe two identical fermions, and no such claim is made.

## Proof
**1. The loss-free spectral projection.** Define \(u=n^{-1/2}(1,\ldots,1)^T\), \(E=|u\rangle\langle u|\), and \(P=I-E\), whose range is \(W=u^\perp\). Since \(A=(n-1)E-P\), the four tensor spectral sectors of \(H\) are \(E\otimes E\), \(E\otimes P\), \(P\otimes E\), and \(P\otimes P\), with respective energies
\[
(a+b)(n-1),\quad a(n-1)-b,\quad -a+b(n-1),\quad -a-b.
\]
For strictly positive \(a,b\), the only collision of these four energies is the middle pair, exactly when \(a=b\).

For each energy, the detector-visible part of its eigenspace is the span of the orthogonal projections of the coincidence vectors \(|j,j\rangle\) into that eigenspace. Let \(\Pi_{\mathrm{abs}}\) be the sum of these mutually orthogonal visible projectors over distinct energies. To justify its probabilistic interpretation without any assumption on the numerical values of the loss strengths, differentiate the norm to obtain \(d\|\psi_t\|^2/dt=-\langle\psi_t,\Gamma\psi_t\rangle\). The orthogonal complement of the visible subspace is a sum of \(H\)-eigenspaces annihilated by \(\Gamma\); it reduces both \(H\) and \(\Gamma\) and evolves unitarily. Conversely, if the generator \(-iH-\Gamma/2\) on the visible subspace had an eigenvalue of zero real part, norm dissipation would force its eigenvector into \(\ker\Gamma\) and simultaneously into an eigenspace of \(H\), contradicting visibility. Finite-dimensionality then gives exponential decay of the visible component. Hence \(\eta(\psi)=\langle\psi,\Pi_{\mathrm{abs}}\psi\rangle\) for every normalized \(\psi\).

**2. Evaluating the diagonal-detector ranks.** The projected detector vectors in \(E\otimes E\) span one dimension. Their restrictions to each of \(E\otimes P\) and \(P\otimes E\) span its full \(n-1\) dimensions. For the final sector set
\[
q_j=(P|j\rangle)\otimes(P|j\rangle),\qquad Qe_j=q_j.
\]
Their Gram matrix is
\[
G=Q^*Q,\qquad G_{jk}=(\delta_{jk}-1/n)^2
=\frac{n-2}{n}I+\frac1{n^2}J.
\]
On the constant and zero-sum subspaces of \(\mathbb C^n\), respectively, its eigenvalues are \((n-1)/n\) and \((n-2)/n\). Both are strictly positive for \(n\ge4\), so \(Q\) has rank \(n\). The visible projector within \(P\otimes P\) is
\[
\Pi_Q=QG^{-1}Q^*,\qquad
G^{-1}=\frac n{n-2}I-\frac1{(n-2)(n-1)}J.
\]
For \(a\ne b\), the complete absorbing projector is explicitly
\[
\boxed{\Pi_{\mathrm{abs}}=E\otimes E+E\otimes P+P\otimes E+\Pi_Q.}
\]
At the resonance \(a=b\), the two middle spectral sectors share an eigenvalue. Their projected detector vectors instead span only the exchange-symmetric space
\[
M_+=\{(u\otimes w+w\otimes u)/\sqrt2:w\in W\},
\]
of dimension \(n-1\). Writing \(\Pi_+\) for its orthogonal projector, the complete resonant formula is
\[
\boxed{\Pi_{\mathrm{abs}}=E\otimes E+\Pi_++\Pi_Q\quad(a=b).}
\]
The displayed summands are pairwise orthogonal. Their ranks give \(3n-1\) and \(2n\), respectively; consequently the dark-space dimensions are \(n^2-3n+1\) and \(n^2-2n\).

**3. Localized probabilities.** For \(x\ne y\), the vector \(v=Q^*|x,y\rangle\) has components \(v_j=(\delta_{jx}-1/n)(\delta_{jy}-1/n)\), so
\[
\sum_jv_j=-1/n,\qquad
\sum_j|v_j|^2=(2n-3)/n^3.
\]
The explicit inverse yields
\[
\langle x,y|\Pi_Q|x,y\rangle=v^*G^{-1}v
=\frac{2n-1}{n^2(n-1)}.
\]
In the nonresonant case the other three contributions are \(1/n^2\), \((n-1)/n^2\), and \((n-1)/n^2\), giving \((2n-1)/[n(n-1)]\). At resonance \(\Pi_+\) instead contributes \((n-2)/n^2\), giving \(1/(n-1)\). If \(x=y\), the initial state lies in \(\operatorname{ran}\Pi_{\mathrm{abs}}\) because it is itself a detector vector; its eventual absorption is one.

**4. Exchange preparations.** Since \(Q^*|x,y\rangle=Q^*|y,x\rangle\), the off-diagonal element of \(\Pi_Q\) between these two vectors equals its diagonal element computed above. For \(a\ne b\), the two middle visible sectors each contribute \(-1/n^2\) to the off-diagonal element, while \(E\otimes E\) contributes \(1/n^2\). Thus
\[
\langle x,y|\Pi_{\mathrm{abs}}|y,x\rangle=\frac1{n(n-1)}\quad(a\ne b).
\]
At resonance the visible subspace is exchange symmetric, hence this off-diagonal matrix element equals the diagonal value \(1/(n-1)\). Adding or subtracting these real off-diagonal elements to the localized probabilities gives \(\eta(\psi_+)=2/(n-1)\) in both cases, and \(\eta(\psi_-)=2/n\) or zero according as \(a\ne b\) or \(a=b\). This proves the stated classification.

## Verification
The included `verify.py` independently constructs the full two-particle Hamiltonian and spectral detector projectors via numerical eigendecomposition and singular-value ranks. Run `python verify.py` after installing the two packages in `requirements.txt`. It exhaustively checks ordered localized pairs and the symmetric and antisymmetric preparations at \(n=4,\ldots,9\) for two resonant and two nonresonant hopping choices; it also checks randomly unequal positive loss rates through the non-Hermitian spectrum and a long-time matrix exponential at \(n=4\). A successful execution prints `VERIFY_OK spectral_ranks=24 sitewise=1084 exchange=928 lossy_spectrum=12 long_time=4`. These are finite corroborations; the all-size and all-positive-rate claims follow from the preceding algebraic proof.

## Relationship to prior work
Štefaňák, Kiss, Jex and Mohring introduced a two-walker meeting problem for a discrete-time coined walk on the infinite line and studied detection at a fixed time. Carson, Loke and Wang studied two-particle coined walks on complete graphs, including \(K_8\), with a coherent collision-dependent phase interaction and entanglement dynamics. Neither model includes persistent positive coincidence loss on all complete-graph sites. Razzoli, Paris and Bordone established a general spectral-subspace approach to continuous-time trapping and evaluated single-trap, single-walker examples; this proof applies that underlying principle to a different, genuinely multi-detector two-walker geometry. The novelty asserted here concerns the *evaluated* complete-graph diagonal-observation projector, the two speed regimes, and the exchange-selective reaction probabilities, not the general spectral projection principle.

## Limitations
The hopping graph is complete and homogeneous for each walker, the particles are distinguishable, and all coincidence loss rates are strictly positive. The formulae do not apply to zero loss at some meeting sites, incoherent dephasing, interactions before meeting, arbitrary graph perturbations, or two identical fermions with different hopping speeds. They describe infinite-time reaction, not a uniform finite-time relaxation bound. A broader published spectral classification not identified by the searches could imply this specialization; independent publication-priority evaluation has not been performed.

## References
1. M. Štefaňák, T. Kiss, I. Jex, and B. Mohring, *The meeting problem in the quantum random walk*, arXiv:0705.1985v1 (public 2007-05-14), https://arxiv.org/abs/0705.1985.
2. G. R. Carson, T. Loke, and J. B. Wang, *Entanglement dynamics of two-particle quantum walks*, arXiv:1511.04828v1 (public 2015-11-16), https://arxiv.org/abs/1511.04828.
3. L. Razzoli, M. G. A. Paris, and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794v1 (public 2020-11-27), https://arxiv.org/abs/2011.13794; *Entropy* **23** (2021), 85.
