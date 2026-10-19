# Exact absorption-time kernel for a two-wall coined quantum walk

## Finding
For the discrete-time two-state quantum walk with absorbing sites at \(-N\) and \(N\), \(N\ge2\), and coin
\[
C_\theta=\begin{pmatrix}\cos\theta&\sin\theta\\\sin\theta&-\cos\theta\end{pmatrix},\qquad 0<\theta<\pi/2,
\]
write \(u=\tan\theta\). From any interior site \(x\in\{-N+1,\dots,N-1\}\) with normalized coin amplitudes \((\alpha,\beta)\in\mathbb C^2\), first absorption time \(T\) is almost surely finite and
\[
\boxed{\mathbb ET=N+u^2[N(N-1)-x^2]+x(1-u^2)(|\alpha|^2-|\beta|^2)+4ux\operatorname{Re}(\overline\alpha\beta).}
\]
In particular the full complex initial coin state is irrelevant at the midpoint:
\[
\boxed{\mathbb E_{0,\alpha,\beta}T=N+N(N-1)\tan^2\theta.}
\]
For the Hadamard coin this is exactly \(N^2\), although the unmonitored walk spreads ballistically. The result also gives the **entire exact survival-time quadratic-form kernel**, including correlations between starting positions, rather than only this expectation.

## Assumptions and scope
At each step apply the coin at all sites, shift its \(L\) component one site left and \(R\) component one site right, then perform a projective measurement at the two absorbing vertices and stop on detection. All surviving amplitudes remain on \(\{-N+1,\ldots,N-1\}\), and \(T\) counts the detecting step, beginning at step one. The initial position is strictly between the sinks. The coin angle is strictly between zero and \(\pi/2\). No intermediate position monitoring or decoherence occurs.

## Proof
**1. Survival operator and stability.** Let \(\mathcal H\) have orthonormal basis \(|x,L\rangle,|x,R\rangle\) for interior sites, and let \(K\) be the coin-and-shift operator projected back to \(\mathcal H\) (all outgoing amplitudes at \(\pm N\) are removed). Its only nonzero entries are \(K_{x-1,L;x,L}=\cos\theta\), \(K_{x-1,L;x,R}=\sin\theta\), \(K_{x+1,R;x,L}=\sin\theta\), and \(K_{x+1,R;x,R}=-\cos\theta\), when the destination remains interior. Suppose \(Kv=\lambda v\) and \(|\lambda|=1\). Equality of the norms of \(Kv\) and \(v\) forces zero amplitude in both outward channels. At the leftmost site the \(R\) component of \(Kv\) has no predecessor, hence the eigenvector's \(R\) component vanishes. The outward \(L\) amplitude then forces its \(L\) component to vanish because \(\cos\theta>0\). Inductively, at each successive site the \(R\) component receives zero input from the preceding site and the \(L\) output toward that preceding site vanishes, forcing both components to zero. This contradicts a nonzero eigenvector. As \(K\) is a finite-dimensional contraction it has spectral radius strictly below one.

**2. Explicit full kernel.** Define the positive operator \(Q=\sum_{t\ge0}(K^\dagger)^tK^t\), which solves uniquely \(Q-K^\dagger QK=I\). All entries are real. If \(x-y\) is odd then \(Q_{x,a;y,b}=0\) for either coin basis vector. For \(x=y\), the \(2\times2\) block (order \(L,R\)) is
\[
Q_{x,x}=\begin{pmatrix}
N+x+u^2[N(N-1)-x(x+1)]&2xu\\
2xu&N-x+u^2[N(N-1)-x(x-1)]
\end{pmatrix}.
\]
For \(x<y\) with \(y-x\) even, put \(\varepsilon=(-1)^{(y-x)/2}\). Then
\[
Q_{x,y}=\varepsilon\begin{pmatrix}
u^2(N+x)(N-y-1)&0\\
u(x+y)&u^2(N+x-1)(N-y)
\end{pmatrix}.
\]
For \(x>y\), set \(Q_{x,y}=Q_{y,x}^{\mathsf T}\).

**3. Algebraic certificate.** Let \(v_L=-1\), \(v_R=1\) and \(M=\begin{pmatrix}1&u\\u&-1\end{pmatrix}\); thus \(C_\theta=M/\sqrt{1+u^2}\). With entries outside the interior treated as zero, the Lyapunov identity is exactly
\[
(1+u^2)Q_{x,a;y,b}-\sum_{d,e\in\{L,R\}}M_{da}M_{eb}Q_{x+v_d,d;y+v_e,e}=(1+u^2)\delta_{xy}\delta_{ab}.
\]
Substitute the displayed kernel: for opposite position parity both sides vanish; for equal parity the exhaustive positional classes are \(x=y\), \(y=x+2\), and \(y=x+2k\) with \(k\ge2\), together with their transposes. The four coin indices in each class reduce the left-hand side to \(0\) after subtracting the indicated Kronecker term; these are polynomial identities in \(N,x,u\) (and in the last class the parity sign). At either absorbing boundary, the formally extended row \(Q_{-N,L;\cdot}\), respectively \(Q_{N,R;\cdot}\), vanishes for all permitted destination indices; the discarded terms therefore contribute zero. The accompanying symbolic checker independently expands all these generic polynomial identities and checks exact finite matrices including both boundaries. It is a reproducibility aid, not a substitute for the stated exhaustive algebraic identity.

**4. Expectation.** Survival at step \(t\) has probability \(\|K^t\psi_0\|^2\). Since the spectral radius of \(K\) is below one, \(\mathbb ET=\sum_{t\ge0}\|K^t\psi_0\|^2=\langle\psi_0,Q\psi_0\rangle\). Inserting the diagonal block at the starting site gives the formula. At \(x=0\) the diagonal entries coincide and the off-diagonal entries vanish, proving exact independence of the initial coin amplitudes.

## Verification
Run `python check_kernel.py` with SymPy installed (see `requirements.txt`). The symbolic routine verifies all four coin-component identities in each of the three generic positional cases for an arbitrary formal \(N\), \(x\), and \(u\), with arbitrary separation and parity sign in the distant case; its separate finite-rational checks include both boundaries for \(2\le N\le10\), at three exact positive values of \(u\). A separate finite-step direct simulation for \(2\le N\le16\) and several mixing angles agreed with the midpoint law up to its controlled numerical truncation error. Finite checks alone are not used to infer an all-size result: the casewise algebra above is uniform in the system size.

## Relationship to prior work
The finite-line model and coin follow Ammara et al. (2025 preprint, updated 2026), which studies the **left/right eventual absorption probabilities** and their large-size behavior, not the finite-size lifetime kernel stated here. Konno et al. (2003) provide general path-integral and generating-function recurrences determining the absorption distributions, but not this evaluated closed-form survival-time operator. Bach et al. (2004) study exit probabilities and long-time tails, not this exact first moment for a fixed finite strip. Yamasaki et al. (2003) analyze absorption times in other geometries. Mondal et al. (2026) study average absorption time with a **single absorber on an unbounded line**, which does not determine this two-wall kernel. The present identity is an explicit evaluation of an observable implicitly determined by general finite-system evolution, not a claim to have introduced the underlying walk or absorbing measurement.

## Limitations
The formula assumes symmetric sinks, homogeneous real coin, a pure state localized at one interior site, projective removal at the two endpoints after every step, and strictly positive mixing with nonzero left-moving diagonal coefficient. At \(\theta=\pi/2\), trapped two-site oscillations may violate sure absorption. No result is asserted for disorder, other monitoring schemes or arbitrary multivertex initial superpositions without using the full kernel. Novelty searches cannot rule out an equivalent unpublished identity or a hidden closed-form summation of earlier generating functions; independent review remains necessary.

## References
1. Ammara Ammara, V. Potoček, M. Štefaňák, F. V. Pepe, *Quantum Walk on a Line with Absorbing Boundaries*, arXiv:2508.13318 (first posted 2025-08-18), https://arxiv.org/abs/2508.13318.
2. N. Konno, T. Namiki, T. Soshi, A. W. Sudbury, *Absorption problems for quantum walks in one dimension*, J. Phys. A 36 (2003) 241–253, arXiv:quant-ph/0208122, https://arxiv.org/abs/quant-ph/0208122.
3. E. Bach, S. Coppersmith, M. P. Goldschen, R. Joynt, J. Watrous, *One-dimensional quantum walks with absorbing boundaries*, J. Comput. Syst. Sci. 69 (2004) 562–592, arXiv:quant-ph/0207008, https://arxiv.org/abs/quant-ph/0207008.
4. T. Yamasaki, H. Kobayashi, H. Imai, *Analysis of absorbing times of quantum walks*, Phys. Rev. A 68 (2003) 012302, arXiv:quant-ph/0205045.
5. S. Mondal, A. Mandal, U. Sen, *Infinite reduction in absorbing time in quantum walks over classical ones*, arXiv:2602.14880 (2026), https://arxiv.org/abs/2602.14880.
