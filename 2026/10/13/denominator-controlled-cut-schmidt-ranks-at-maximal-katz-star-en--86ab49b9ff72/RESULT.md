# Denominator-controlled cut Schmidt ranks at maximal Katz-star entanglement distance

## Finding

Let a Katz-weighted star have \(m\ge 1\) leaves, coupling parameter \(0<\beta<m^{-1/2}\), and define \(D=1-m\beta^2\). Evolve its \(m+1\) qubits from \(|+\rangle^{\otimes(m+1)}\) under the Katz Ising Hamiltonian described below. At the first maximal one-site entanglement-distance time \(t_*=\pi D/2\), partition the system into the center plus \(a\) leaves and the other \(b=m-a\ge1\) leaves, where \(0\le a<m\).

The nonzero eigenvalues of the reduced state of the \(b\)-leaf side are exactly those of the \((b+1)\)-dimensional Hermitian matrix
\[
G_{jk}=2^{-b}\sqrt{\binom bj\binom bk}\,{\bf1}_{j\equiv k\ ({\rm mod}\ 2)}\,e^{i\pi\beta a(j-k)/2}\cos^a\!\left(\frac{\pi\beta(j-k)}2\right),\quad 0\le j,k\le b.
\]
All additional eigenvalues of the physical reduced density matrix vanish. In particular its exact purity is
\[
\operatorname{Tr}(\rho_B^2)=4^{-b}\sum_{r=-\lfloor b/2\rfloor}^{\lfloor b/2\rfloor}\binom{2b}{b+2r}\cos^{2a}(\pi\beta r).
\]
Its Schmidt rank across the cut is
\[
R(a,b,\beta)=\begin{cases}
\min\{b+1,2(a+1)\},&\beta\notin\mathbb Q,\\
\min\{b+1,2(a+1),2q\},&\beta=p/q\in\mathbb Q,\ \gcd(p,q)=1.
\end{cases}
\]
These formulas hold for every allowed \(m,a,\beta\) and do not require genericity assumptions. By purity of the global state the same spectrum and rank apply to the complementary side, with its requisite zero eigenvalues.

## Assumptions and scope

The star adjacency matrix \(A\) has one central vertex adjacent to each of \(m\) leaves. Its Katz matrix is \(K=(A+\beta A^2)/D\); thus the center--leaf edge weight is \(D^{-1}\), and each distinct leaf--leaf edge weight is \(\beta D^{-1}\). In dimensionless time \(t=J\tau\), use \(H=-(J/2)\sum_{u<v}K_{uv}Z_uZ_v\) and \(|\psi(t)\rangle=\exp[(it/2)\sum_{u<v}K_{uv}Z_uZ_v]|+\rangle^{\otimes(m+1)}\). These conventions match the motivating study's Katz-star model. The reduced spectrum is unaffected by diagonal unitaries acting separately on either side of the cut. The center is assigned to the first side without loss of generality.

## Proof

**1. Extracting the cross-cut phase.** At \(t=t_*\), every center--leaf Ising factor is \(\exp(i\pi Z_cZ_j/4)\), and every leaf--leaf factor is \(\exp(i\pi\beta Z_iZ_j/4)\). Write computational bits as \(c\in\{0,1\}\) and leaf bits as \(x_i\in\{0,1\}\) with \(Z_i=(-1)^{x_i}\). Expanding \((1-2x)(1-2y)\) shows that, after removing phases depending only on the first or second partition, the cross-cut multiplier is \((-1)^{cj}e^{i\pi\beta ij}\), where \(i\) is the Hamming weight of the \(a\) leaves on the center's side and \(j\) that of the other \(b\) leaves. The intra-partition diagonal unitaries depend only on the corresponding Hamming weights (and the center bit), so they preserve the Dicke subspaces used next.

**2. Exact matrix compression.** In normalized symmetric Dicke bases, the coefficient matrix of the bipartite pure state, after these local unitaries, is
\[
M_{(c,i),j}=2^{-(m+1)/2}\sqrt{\binom ai\binom bj}\,(-1)^{cj}e^{i\pi\beta ij},\quad c=0,1,\quad 0\le i\le a,\quad0\le j\le b.
\]
All orthogonal basis vectors have zero amplitude. The reduced density matrix on the \(b\)-leaf side is the Gram matrix \(G=M^*M\), up to a harmless complex conjugation convention. Summing over \(c\) gives zero unless \(j-k\) is even; summing over \(i\) by the binomial theorem then yields the displayed formula for \(G\). Its trace is \(2^{-b}\sum_j\binom bj=1\) and it is positive semidefinite by construction.

**3. Purity.** For even \(j-k=2r\), the absolute square is \(4^{-b}\binom bj\binom bk\cos^{2a}(\pi\beta r)\). Apply Vandermonde's identity \(\sum_{k}\binom bk\binom b{k+2r}=\binom{2b}{b+2r}\), with out-of-range binomial coefficients interpreted as zero. Summing over \(j,k\) gives the purity formula.

**4. Exact rank.** Remove the nonzero positive row and column binomial factors from \(M\). Its entries become \(z_{c,i}^{\,j}\), with nodes \(z_{c,i}=(-1)^c e^{i\pi\beta i}\), for \(c=0,1\) and \(0\le i\le a\). The Vandermonde theorem gives \(\operatorname{rank}M=\min\{b+1,s\}\), where \(s\) is the number of distinct nodes. For irrational \(\beta\), equality \((-1)^c e^{i\pi\beta i}=(-1)^{c'}e^{i\pi\beta i'}\) forces \(i=i'\), then \(c=c'\), hence \(s=2(a+1)\). For \(\beta=p/q\) in lowest terms, equality reduces to a collision among residues \(p i+cq\pmod{2q}\). If \(p\) is odd, \(p\) generates the cyclic residue classes modulo \(2q\) and the two translates give exactly \(2\min\{a+1,q\}\) distinct nodes. If \(p\) is even, \(q\) must be odd; the \(c=0\) and \(c=1\) nodes occupy opposite parity classes, each containing \(\min\{a+1,q\}\) distinct nodes. Thus in both cases \(s=2\min\{a+1,q\}\), proving the claimed rank.

## Verification

Run `python3 verify_rank.py` after installing the standalone dependency in `requirements.txt`. Direct evolution of all computational-basis amplitudes was compared with the reduced Gram eigenvalues, purity, and rank for 510 small instances through eight leaves, without relying on the compressed-state construction in the direct evolution. Exact integer residue counts were checked for 8,550 rational parameter triples. These finite computations corroborate the formulas but do not establish the infinite statement; the Vandermonde and residue arguments above do.

For \(m=13\), \(a=5\), \(b=8\), the rational value \(\beta=1/4\) gives rank \(8\), whereas the admissible irrational value \(\beta=\sqrt2/6\) gives rank \(9\). For \(m=80\), \(a=30\), \(b=50\), \(\beta=1/10\) gives rank \(20\), while every admissible irrational value gives rank \(51\). The latter is an analytic rank statement, not a numerical small-eigenvalue assertion.

## Relationship to prior work

De Simone, Capra and Franzosi (2026), arXiv:2609.20390v1, introduce Katz-weighted graph-state dynamics and prove that the full one-body entanglement distance of their star is maximal at \(t_*=\pi D/2\). The present result conditions on that same model and time but addresses its full bipartite reduced spectra, purities, and arithmetic Schmidt ranks; maximal single-site distance alone does not imply these formulas. Wang, Roy, Maskey and Ramachandran (2026), arXiv:2610.03595v1, develop rational-time one-axis-twisting cat decompositions, which provide related finite-component upper-bound mechanisms but do not explicitly yield this cut-dependent Katz-star rank classification or the exact Gram-spectrum formula. Finite-field quadratic-phase rank results (arXiv:2605.05167) and weighted graph-state resource constructions (arXiv:2512.01327) address structurally related but mathematically different domains.

## Limitations

Only the Katz-weighted star family, its first single-site-distance maximum, and the stated bipartitions are covered. The formulas do not assert comparable arithmetic rank jumps at arbitrary times or for other graphs. In practice, floating-point eigenvalue thresholds cannot reliably reveal tiny nonzero eigenvalues of large Gram matrices; the exact rank is established algebraically. A conceptually equivalent specialization of general one-axis-twisting or weighted graph-state results could exist in literature not indexed or fully accessible during comparison; independent novelty validation is not claimed.

## References

- L. De Simone, L. Capra and R. Franzosi, *Entanglement Dynamics in Katz-Weighted Graph States*, arXiv:2609.20390v1 (first public version September 17, 2026), https://arxiv.org/html/2609.20390v1.
- Wang, Roy, Maskey and Ramachandran, *The exact LCU sampling overhead of collective diagonal unitaries: resonances and a continued-fraction dichotomy*, arXiv:2610.03595v1 (2026), https://arxiv.org/html/2610.03595v1.
- *Entanglement-Rank Duality in Quadratic Phase Quantum States*, arXiv:2605.05167v2 (2026), https://arxiv.org/html/2605.05167v2.
- *Measurement-based quantum computation on weighted graph states with arbitrarily small weight*, arXiv:2512.01327v1 (2025), https://arxiv.org/html/2512.01327v1.
