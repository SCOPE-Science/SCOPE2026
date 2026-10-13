# Rational-speed collision resonances for two quantum walkers on the binary hypercube

## Finding
Let \(d\ge2\). Two distinguishable noninteracting continuous-time quantum walkers have positive edge-hopping rates \(a,b>0\) on the binary hypercube \(Q_d\). Every coincidence configuration \((x,x)\) is subject to irreversible absorption at an arbitrary strictly positive site-dependent rate. Write \(\mathcal B_d(a,b)\) for the spectral subspace eventually absorbed with probability one, and \(B_d(a,b)=\dim\mathcal B_d(a,b)\).

Define the generic value
\[
G_d=2^{d-2}(d^2+3d+4).
\]
Then the complete classification is
\[
B_d(a,b)=\begin{cases}
2^{d-1}(d+2),&a=b,\\
G_d,&a\ne b\text{ and }(a+b)/|a-b|\notin\mathbb Q,\\
G_d-\displaystyle\sum_{t=p}^{d-q}\binom dt(d-t-q+1)(t-p+1),&a\ne b,\quad (a+b)/|a-b|=p/q,
\end{cases}
\]
where the last ratio is in lowest positive terms, with integers \(p>q\ge1\); an empty sum is zero. In the rational unequal-speed case, the dimension is strictly below \(G_d\) if and only if \(d\ge p+q\). At this first possible dimension the deficit is exactly \(\binom{p+q}{p}\). In particular, for \(d=3\), the generic dimension is \(44\), whereas speed ratio \(a:b=3:1\) gives \(41\), and equal speeds give \(20\). The permanently dark subspace always has complementary dimension \(4^d-B_d(a,b)\).

## Assumptions and scope
The one-particle Hilbert space is \(\mathbb C^{2^d}\), with computational basis \(\{|x\rangle:x\in(\mathbb Z/2\mathbb Z)^d\}\) and hypercube adjacency \(A|x\rangle=\sum_{j=1}^d|x\oplus e_j\rangle\). The two-particle Hamiltonian is \(H=aA\otimes I+bI\otimes A\). For \(\gamma_x>0\), define the no-reaction generator
\[
K=H-i\sum_x\gamma_x|x,x\rangle\langle x,x|.
\]
The eventual reaction probability of a normalized initial vector \(\psi\) is \(1-\lim_{t\to\infty}\|e^{-itK}\psi\|^2\). The absorbing spectral subspace is the orthogonal complement of all \(H\)-eigenvectors killed by every coincidence detector. The claim does not assert a particular finite-time reaction rate or formula for every localized initial state's probability.

## Proof
Let \(\chi_k(x)=(-1)^{k\cdot x}\) denote the binary characters and \(|\widehat k\rangle=2^{-d/2}\sum_x\chi_k(x)|x\rangle\). Then \(A|\widehat k\rangle=(d-2|k|)|\widehat k\rangle\). The simultaneous translation symmetry decomposes the two-particle space orthogonally into \(2^d\) momentum sectors
\[
\mathcal H_m=\operatorname{span}\{|\widehat k\rangle\otimes|\widehat{k\oplus m}\rangle:k\in(\mathbb Z/2\mathbb Z)^d\}.
\]
The \(2^d\) coincidence kets span, in these sectors, one nonzero vector apiece, proportional to
\[
\xi_m=2^{-d/2}\sum_k|\widehat k\rangle\otimes|\widehat{k\oplus m}\rangle.
\]
For fixed \(m\), the detector-visible part of each distinct energy eigenspace of \(H|_{\mathcal H_m}\) is exactly one dimensional: the projection of \(\xi_m\) onto that eigenspace is nonzero because its coefficients in the orthonormal Fourier eigenbasis are all equal and nonzero. Distinct energy eigenspaces yield independent bright vectors. Consequently the total bright dimension is the sum, over \(m\), of the number of distinct energies in \(\mathcal H_m\).

Put \(t=|m|\). For each \(k\), let \(u\) be the number of ones of \(k\) in the \(d-t\) coordinates where \(m\) is zero, and \(v\) the number of ones in the \(t\) coordinates where \(m\) is one. All integer pairs in \(0\le u\le d-t\), \(0\le v\le t\) occur. The energy is
\[
E_m(u,v)=(a+b)d-2bt-2(a+b)u-2(a-b)v.
\]
For equal speeds, it depends only on \(u\), giving \(d-t+1\) distinct energies. Summing \(\binom dt(d-t+1)\) gives \(2^{d-1}(d+2)\).

For unequal speeds, two pairs of grid indices yield the same energy exactly when
\[
(a+b)(u-u')+(a-b)(v-v')=0.
\]
If \((a+b)/|a-b|\) is irrational, every pair is distinct, so the number of energies for a sector of weight \(t\) is \((d-t+1)(t+1)\). The binomial sums \(\sum_t\binom dt=2^d\), \(\sum_t t\binom dt=d2^{d-1}\), and \(\sum_t t^2\binom dt=d(d+1)2^{d-2}\) give \(G_d\).

Otherwise let \((a+b)/|a-b|=p/q\) in lowest terms. Since \(a,b>0\), \(p>q\ge1\). Equality of energies on the rectangular grid connects points differing by the primitive shift \((q,-p)\) when \(a>b\), or \((q,p)\) when \(a<b\). Every collision class is a finite chain under this shift. Its earliest representative is unique. Counting all grid points except those with a predecessor gives exactly
\[
(d-t+1)(t+1)-\max(0,d-t-q+1)\max(0,t-p+1)
\]
distinct energies. Summing over the \(\binom dt\) momenta of weight \(t\) proves the formula. A deficit exists exactly when some integer \(t\) satisfies \(p\le t\le d-q\), or \(d\ge p+q\); at equality only \(t=p\) contributes \(\binom{p+q}{p}\).

Finally, the no-reaction flow is a contraction because \(\frac{d}{dt}\|e^{-itK}\psi\|^2=-2\sum_x\gamma_x|\langle x,x|e^{-itK}\psi\rangle|^2\le0\). A nondecaying eigenvector must lie in the detector kernel and be an \(H\)-eigenvector. Conversely these vectors evolve unitarily with no absorption. Their orthogonal complement is invariant and, in finite dimension, decays: a hypothetical nondecaying eigenmode there would contradict its definition; the contraction property excludes nontrivial Jordan blocks on the real spectral axis. Thus the detector-visible spectral rank computed above is precisely the eventually absorbing dimension, independently of all positive \(\gamma_x\). \(\square\)

## Verification
The standalone `verify.py` reconstructs the Hamiltonian and coincidence-detector matrix independently in position basis, diagonalizes the real symmetric two-particle Hamiltonian, and sums the detector-restriction ranks within *all* distinct energy eigenspaces. It compares those ranks with the analytic formula for dimensions \(1\) through \(3\) and multiple integer speed ratios. It also independently checks the rectangular-grid energy counts and exact first-resonance deficits through dimension \(9\). Run `python verify.py` after installing the dependencies in `requirements.txt`. Finite checks are corroboration, not the infinite-family proof above.

## Relationship to prior work
Štefaňák, Kiss, Jex and Mohring introduced a two-particle meeting problem for discrete-time walks on a line (arXiv:0705.1985); their setting does not identify the absorbing collision subspace for independently hopping continuous-time walkers on hypercubes. Carson, Loke and Wang (arXiv:1511.04828) studied entanglement dynamics of interacting two-particle walks on graphs, not this all-coincidence absorption rank. Thiel, Mualem, Meidan, Barkai and Kessler (arXiv:1906.08112) established general spectral principles for bright and dark subspaces of repeatedly monitored walks, principally for a single detection state. Such principles motivate the detector-visible spectral approach, but they do not supply the weighted binary-cube momentum decomposition or the sharp coprime \((p,q)\) resonance hierarchy here. The distinction between a generic general spectral criterion and this explicit all-dimensional arithmetic evaluation is essential. Independent publication-priority verification has not been performed.

## Limitations
The classification assumes two **distinguishable**, noninteracting walkers on an exactly homogeneous binary hypercube, positive real hopping strengths, and strictly positive reaction rates on **every** coincidence vertex. It counts the absorbing subspace rather than furnishing sitewise probabilities, capture times, or robustness to disorder, interactions, partial detector coverage or finite-time perturbations. The countably many rational speed ratios only cause a rank deficit when \(p+q\le d\); no claim is made about discontinuities in finite-time observables. General spectral detection theorems remain important prior knowledge, and an unlocated stronger two-particle hypercube classification would affect originality.

## References
1. M. Štefaňák, T. Kiss, I. Jex and B. Mohring, *The meeting problem in the quantum random walk*, arXiv:0705.1985 (first submitted 14 May 2007).
2. G. R. Carson, T. Loke and J. B. Wang, *Entanglement dynamics of two-particle quantum walks*, arXiv:1511.04828 (first submitted 16 November 2015).
3. F. Thiel, I. Mualem, D. Meidan, E. Barkai and D. A. Kessler, *Dark states of quantum search cause imperfect detection*, arXiv:1906.08112 (2019/2020).
