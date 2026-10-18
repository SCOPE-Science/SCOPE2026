# Two-sink dark-state dimensions and the binary antipodal exception on Hamming quantum networks

## Finding
For the Hamming graph \(H(n,q)=K_q^{\square n}\), equip each edge with hopping amplitude one and any two **distinct** sites \(u,v\) with positive local loss rates. Write \(d\) for their Hamming distance, \(A\) for the unweighted adjacency matrix, and \(B\) for the span of the spectral projections of the two trap vectors onto every distinct eigenvalue of \(A\). Then the exact bright-space dimension is
\[
\dim B=\begin{cases}
2n+1,&q\ge3,\\
n+1,&q=2,\ d=n,\\
2n,&q=2,\ 1\le d<n.
\end{cases}
\]
The orthogonal complement \(D=B^\perp\) is exactly the nondecaying dark space, so \(\dim D=q^n-\dim B\). Consequently, a maximally mixed excitation has eventual survival probability \(1-\dim B/q^n\), independent of the strictly positive trap rates. In the binary antipodal case, adding the second trap does not change the dark subspace at all; for larger alphabets every distinct pair has the same two-trap bright rank, whatever its separation.

There is also an exact formula for any localized initial vertex \(x\). Put \(Q=q^n\), \(a=d(x,u)\), \(b=d(x,v)\), and \(d=d(u,v)\). Define the \(q\)-ary Krawtchouk evaluations
\[
K_k(j)=\sum_{h=0}^{k}(-1)^h(q-1)^{k-h}\binom jh\binom{n-j}{k-h},\qquad m_k=\binom nk(q-1)^k,
\]
with out-of-range binomial coefficients zero. For \(0\le k\le n\), let \(F_k=K_k(a)\), \(G_k=K_k(b)\), \(T_k=K_k(d)\). The bright probability in eigenspace \(k\) is
\[
P_k(x)=\begin{cases}
\dfrac{m_k(F_k^2+G_k^2)-2T_kF_kG_k}{Q(m_k^2-T_k^2)},& |T_k|<m_k,\\[4pt]
\dfrac{F_k^2}{Qm_k},& |T_k|=m_k.
\end{cases}
\]
Thus \(S_\infty(x)=1-\sum_{k=0}^{n}P_k(x)\). The second branch is well-defined because the projected trap vectors are then collinear, and the squared projected coordinates agree for both trap choices.

## Assumptions and scope
Let \(n\ge1\), \(q\ge2\) be integers and \(u\ne v\) be vertices of \(\{0,\dots,q-1\}^n\). The single-particle Hamiltonian is the real symmetric adjacency operator of the Cartesian product of \(n\) complete graphs. There is no magnetic flux, disorder, dephasing, onsite potential, hopping normalization, or stochastic transition at a trap. Instead, positive constants \(\gamma_u,\gamma_v\) generate the no-jump evolution
\[
\psi(t)=e^{-itH_{\mathrm{eff}}}\psi(0),\qquad H_{\mathrm{eff}}=A-\frac{i}{2}\bigl(\gamma_u|u\rangle\langle u|+\gamma_v|v\rangle\langle v|\bigr).
\]
Its squared norm is the probability that no irreversible capture has occurred by time \(t\). For an initial density operator the same statement holds after taking the trace of the unnormalized evolved state. This is the coherent continuous-time loss model, not a discrete-time coined walk or an incoherent routing model.

## Proof
**1. Spectrum and projectors.** Identify the vertex set with the additive group \((\mathbb Z/q\mathbb Z)^n\) solely for Fourier diagonalization; the graph itself depends only on equality or inequality of coordinate symbols. Its orthonormal characters are \(\chi_s(x)=q^{-n/2}\exp(2\pi i\langle s,x\rangle/q)\). A character with exactly \(k\) nonzero coordinates has adjacency eigenvalue \(\lambda_k=n(q-1)-qk\), of multiplicity \(m_k=\binom nk(q-1)^k\). The distinct eigenvalues are indexed by \(k=0,\dots,n\). If \(E_k\) denotes the corresponding orthogonal spectral projector, then character orthogonality and grouping according to the overlap of supports show
\[
\langle x|E_k|y\rangle=\frac{K_k(d(x,y))}{q^n}.
\]

**2. Exact bright rank.** For the two sinks, \(B=\sum_{k=0}^n\mathrm{span}\{E_k|u\rangle,E_k|v\rangle\}\), with the sum orthogonal. The Gram matrix of the two generators in layer \(k\) is
\[
\frac1{q^n}\begin{pmatrix}m_k&K_k(d)\\K_k(d)&m_k\end{pmatrix}.
\]
Its rank is one if and only if the two projected vertex vectors are collinear, and two otherwise. Layer \(k=0\) always has rank one. A relative displacement character distinguishes the vectors: their Fourier coefficients differ by the phase \(\chi_s(v-u)\).

For \(q\ge3\) and every \(k\ge1\), choose a weight-\(k\) Fourier support containing any coordinate where \(u\) and \(v\) differ. Fix all other Fourier indices and vary the nonzero index in that differing coordinate between \(1\) and \(2\). These two phases are distinct, because the nonzero displacement is not divisible by \(q\). Therefore the two projected vectors are independent for all nonconstant layers, giving \(1+2n\).

For \(q=2\), at weight \(k\) the relative phases are the signs of \((-1)^{|S\cap\Delta|}\), where \(S\) is a \(k\)-subset of the coordinates and \(\Delta\) is the set where the two traps differ. If \(d=n\), the sign is always \((-1)^k\) and every layer has rank one, giving \(n+1\). If \(1\le d<n\), for each \(1\le k\le n-1\) choose a coordinate in \(\Delta\) and one outside it, then exchange them between two weight-\(k\) supports while leaving the other \(k-1\) choices fixed. This changes the sign, so every interior layer has rank two. Layers \(0\) and \(n\) both have rank one, giving \(2+2(n-1)=2n\). These cases exhaust the permissible parameters, including \(n=1\).

**3. Why the dimension is the asymptotic survivor dimension.** Define \(D=B^\perp\). Because the eigenprojectors partition the identity, \(D\) is exactly the direct sum, across eigenspaces, of vectors orthogonal to the two sink kets. It is invariant under \(A\), and the loss operator \(\Gamma=\gamma_u|u\rangle\langle u|+\gamma_v|v\rangle\langle v|\) vanishes identically on it. Its orthogonal complement \(B\) is invariant under both \(A\) and \(\Gamma\). If an eigenvector of \(H_{\mathrm{eff}}\) restricted to \(B\) had a real eigenvalue, taking the imaginary part of its expectation would force its components at both traps to vanish, after which it would be a real-energy eigenvector of \(A\) in \(B\cap D=\{0\}\), a contradiction. Every eigenvalue on \(B\) therefore has strictly negative imaginary part. Finite-dimensional Jordan theory implies that the no-jump propagator decays to zero on \(B\), while it is unitary on \(D\). Hence the final no-capture probability for any pure initial vector \(\psi\) is \(\|P_D\psi\|^2\). Taking a maximally mixed initial state gives \(\dim D/q^n\). Trap rates influence the transient decay, but not the dark projector.

**4. Localized sources.** In eigenlayer \(k\), the squared projection of \(|x\rangle\) onto \(\mathrm{span}\{E_k|u\rangle,E_k|v\rangle\}\) is obtained by contracting the evaluation vector \(q^{-n}(F_k,G_k)\) against the pseudoinverse of the two-by-two Gram matrix above. In the full-rank case, inversion gives the first displayed formula for \(P_k(x)\); in the rank-one case, one normalized projected trap vector gives the second. Orthogonality of eigenlayers sums these contributions and proves the localized survival formula.

## Verification
The accompanying standalone `check_hamming.py` builds the complete unweighted adjacency matrices, independently diagonalizes their eigenspaces, compares the exact two-trap Fourier rank with the predicted classification for \(174\) distinct test configurations, compares \(6366\) localized survival evaluations against explicit spectral projection calculations, and checks \(12\) direct no-jump time evolutions. The tests cover binary dimensions through six, ternary dimensions through three, and four-symbol dimensions through two. Run `python check_hamming.py` in an environment with NumPy and SciPy. All infinite-parameter assertions, including strict rate independence of the limiting projection, follow from the preceding proof rather than these finite tests.

For example, for \(q=2\) and \(n=4\), antipodal traps yield \(\dim D=11\), whereas any nonantipodal two traps yield \(\dim D=8\). Uniformly sampling an initial nontrap site gives respective limiting survival probabilities \(11/14\) and \(8/14\). For \(q=3\), \(n=4\), every distinct trap pair leaves \(81-9=72\) dark dimensions.

## Relationship to prior work
Moore and Russell (2001) diagonalize coherent quantum walks on a binary hypercube; their eigenvalue structure is adopted here, with a distinct two-trap survival question and an extension to all \(q\)-ary Hamming graphs. Perfect antipodal binary transfer and the associated one-trap redundancy are well known; **antipodal redundancy alone is not claimed as a new phenomenon**. Angeles-Canul and coauthors (2009) study transfer in related weighted graph systems, without the present all-placement sink classification.

Schuld, Sinayskiy, and Petruccione (2014) construct a stochastic quantum walk toward two attractor vertices of a binary hypercube, but remove edges from the coherent Hamiltonian and use directed incoherent Lindblad transport to the sinks; their sink model therefore differs mathematically from the unchanged-adjacency local-loss evolution here. Makmal, Tiersch, Ganahl, and Briegel (2015) analyze dark states on *modified, embedded* hypercubes using **discrete-time coined** walks and hitting-time projections; they do not give the two-local-loss spectral rank or the \(q\)-ary distinction. Le, Donati, Severini, and Caruso (2017) provide broad graph-theoretic dark-state methods and analyze other networks, but not the all-size two-sink Hamming classification or localized Krawtchouk formula. The novelty asserted here is the combined two-sink, all-distance, all-alphabet coherent-loss law, with exact source-resolved eventual survival.

## Limitations
The result assumes exact homogeneous Hamming connectivity, no coherent perturbations, exactly two distinct traps with strictly positive rates, and irreversible no-jump monitoring. Weak dephasing, noise, trap removal, or engineered hopping destroys assumptions needed for the Fourier argument. The statements concern eventual capture/survival, not finite-time optimal search or monotonicity in trap strength. The proof establishes no corresponding many-trap formula. Although the searched literature did not establish a prior theorem implying this exact combination, an unindexed equivalent spectral-controllability formula could exist; independent bibliographic audit has not been performed.

## References
1. C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137 (first public 29 April 2001), https://arxiv.org/abs/quant-ph/0104137.
2. M. Schuld, I. Sinayskiy, and F. Petruccione, *Quantum walks on graphs representing the firing patterns of a quantum neural network*, Physical Review A **89**, 032333 (2014), arXiv:1404.0159, https://arxiv.org/abs/1404.0159.
3. A. Makmal, M. Tiersch, C. Ganahl, and H. J. Briegel, *Quantum walks on embedded hypercubes: Nonsymmetric and nonlocal cases*, Physical Review A **93**, 022322 (2016), arXiv:1510.08388, https://arxiv.org/abs/1510.08388.
4. T. P. Le, L. Donati, S. Severini, and F. Caruso, *How to suppress dark states in quantum networks and bio-engineered structures*, Journal of Physics A **51**, 365306 (2018), arXiv:1707.07482, https://arxiv.org/abs/1707.07482.
5. R. J. Angeles-Canul and collaborators, *On quantum perfect state transfer in weighted join graphs* (2009), arXiv:0909.0431, https://arxiv.org/abs/0909.0431.
