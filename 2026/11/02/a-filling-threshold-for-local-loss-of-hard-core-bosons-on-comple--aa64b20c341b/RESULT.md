# A filling threshold for local loss of hard-core bosons on complete quantum networks

## Finding

Consider the complete graph on \(N\ge4\) physical sites, with a fixed particle count \(1\le k\le N-1\), real uniform nonzero hopping amplitude \(J\), and one site, numbered \(0\), subject to particle loss of rate \(\kappa>0\). For either hard-core bosons or spinless fermions, let the initial state be maximally mixed on the \(k\)-particle sector, which has dimension \(M=\binom Nk\). Define capture as *at least one loss event at site \(0\) at any finite time*. Then its eventual probability is precisely

\[
\boxed{P_{\mathrm{HC}}(N,k)=\min\!\left\{\frac{2k}{N},1\right\},\qquad
P_{\mathrm F}(N,k)=1-\frac{(N-k)(N-k-1)}{N(N-1)}.}
\]

More precisely, the dimensions of the subspaces that never suffer a first jump are

\[
\boxed{d_{\mathrm{HC}}=\max\!\left\{\binom{N-1}{k}-\binom{N-1}{k-1},0\right\},\quad
d_{\mathrm F}=\binom{N-2}{k},}
\]

with \(\binom ab=0\) when \(b>a\) or \(b<0\). The no-jump survival for any initial density operator converges to its weight in the appropriate dark subspace. Thus **all** maximally mixed hard-core-boson sectors capture with probability one exactly at fillings \(k\ge\lceil N/2\rceil\), while the corresponding fermion sectors retain a dark component until \(k\ge N-1\). The capture difference is positive for every \(2\le k\le N-2\), equals \(k(k-1)/[N(N-1)]\) when \(2k\le N\), and equals \((N-k)(N-k-1)/[N(N-1)]\) when \(2k\ge N\). For even \(N\) and \(k=N/2\), the fermionic uncaptured fraction is exactly \((N-2)/[4(N-1)]\), tending to \(1/4\), despite full hard-core-boson capture. These probabilities are independent of the positive loss rate and the magnitude of nonzero uniform hopping.

## Assumptions and scope

The Hilbert space has an orthonormal occupation basis \(\lvert S\rangle\) indexed by all \(k\)-subsets \(S\subseteq\{0,\ldots,N-1\}\). Creation and annihilation operators obey, respectively, the hard-core bosonic or canonical fermionic relations. The hopping Hamiltonian in the fixed-\(k\) sector is

\[
H=J\sum_{i\ne j} a_i^\dagger a_j,
\]

with the usual interpretation of ordered annihilation and creation products; there are no site energies, disorder, other interactions, or other baths. A local quantum jump is \(L=\sqrt\kappa\,a_0\); prior to its first occurrence, the non-Hermitian generator is \(H_{\mathrm{eff}}=H-i\kappa n_0/2\), where \(n_0=a_0^\dagger a_0\). The squared no-jump norm is the survival probability. A loss transfers the state into the \((k-1)\)-sector, but only the occurrence of the *first* jump is counted. The result is not a claim about subsequent losses or mean waiting times.

## Proof

**1. Dark-space reduction.** Let \(\mathcal D\) be the largest \(H\)-invariant subspace in \(\ker n_0\). The identity

\[
\frac{d}{dt}\|e^{-iH_{\mathrm{eff}}t}v\|^2=-\kappa\langle e^{-iH_{\mathrm{eff}}t}v,n_0e^{-iH_{\mathrm{eff}}t}v\rangle
\]

makes the evolution contractive. For an eigenvector of \(H_{\mathrm{eff}}\), a nondecaying eigenvalue requires zero occupation at the lossy site; such a vector is then an eigenvector of the Hermitian \(H\). Conversely, vectors in \(\mathcal D\) suffer no loss. The dark subspace and its orthogonal complement are invariant under both \(H\) and \(n_0\). On that complement all eigenvalues of \(-iH_{\mathrm{eff}}\) have strictly negative real parts, and finite dimensionality implies exponential decay. Hence survival tends to \(\operatorname{tr}(\Pi_{\mathcal D}\rho_0)\). For \(\rho_0=I/M\), capture equals \(1-\dim(\mathcal D)/M\).

**2. Hard-core bosons and the Boolean down-map.** Put \(n=N-1\) and let \(V_r\) denote the complex vector space spanned by \(r\)-subsets of the other \(n\) sites. A state free of site \(0\) lives in \(V_k\). The part of \(H\) that transfers this space into configurations containing site \(0\) is \(J D_k\), where

\[
(D_kv)(T)=\sum_{j\notin T}v(T\cup\{j\}),\qquad |T|=k-1.
\]

The restriction of \(H/J\) to \(V_k\) is adjacency of the Johnson graph on the \(k\)-subsets of the \(n\) remaining sites. Writing \(U_{k-1}=D_k^\dagger\), its adjacency satisfies \(A=U_{k-1}D_k-kI\). Therefore \(\ker D_k\) is automatically an eigenspace of \(A\) with eigenvalue \(-k\), and it is exactly the full dark subspace: any dark vector must first have zero site-\(0\) occupancy and zero outgoing amplitude \(D_kv\).

The standard Boolean-lattice commutator can be verified entrywise:

\[
D_{r+1}U_r-U_{r-1}D_r=(n-2r)I\quad\text{on }V_r.
\]

For \(r<n/2\) it yields \(\|U_rv\|^2=\|D_rv\|^2+(n-2r)\|v\|^2\), so \(U_r\) is injective. It follows that \(D_k\) is surjective whenever \(k\le(n+1)/2\). The complement operation on subsets identifies \(D_k\) with an up-map on \(V_{n-k}\), proving injectivity whenever \(k>n/2\). At the possible shared middle level both statements agree. Consequently

\[
\operatorname{rank}D_k=\min\!\left\{\binom nk,\binom n{k-1}\right\},
\qquad \dim\ker D_k=\max\!\left\{\binom nk-\binom n{k-1},0\right\}.
\]

Since \(\binom Nk=\binom nk+\binom n{k-1}\) and \(\binom{N-1}{k-1}/\binom Nk=k/N\), the bosonic capture law follows, including its sharp threshold.

**3. Spinless fermions and exterior powers.** The one-particle hopping matrix is \(J(\mathbf1\mathbf1^T-I)\). Put \(u=N^{-1/2}\sum_i\lvert i\rangle\). On the fermionic \(k\)-particle exterior power,

\[
H=J(N\widehat n_u-kI),
\]

where \(\widehat n_u\) counts occupancy of the single uniform orbital. The two eigenspaces are \(\bigwedge^k u^\perp\) and \(u\wedge\bigwedge^{k-1}u^\perp\), with distinct energies \(-Jk\) and \(J(N-k)\). Let \(W=\lvert0\rangle^\perp\) be the \((N-1)\)-dimensional one-particle space avoiding the absorber. The zero-occupancy sector is \(\bigwedge^k W\). In the low-energy block its intersection is precisely \(\bigwedge^k(W\cap u^\perp)\), of dimension \(\binom{N-2}{k}\).

There is no nonzero vector in the intersection of the high-energy block and \(\bigwedge^k W\): if \(u\wedge\eta\) has zero site-\(0\) occupancy, contraction with \(\langle0\rvert\) gives \(N^{-1/2}\eta-u\wedge\iota_0\eta=0\); projecting onto \(\bigwedge^{k-1}u^\perp\) forces \(\eta=0\). Since the two energies are distinct, any invariant no-loss subspace splits across these two blocks. Thus \(d_{\mathrm F}=\binom{N-2}{k}\). Taking the binomial ratio yields the fermionic capture formula.

**4. Comparison.** Subtracting the two capture probabilities yields \(k(k-1)/[N(N-1)]\) below half filling and \((N-k)(N-k-1)/[N(N-1)]\) above half filling; the expressions coincide at the boundary. Both are strictly positive exactly when \(2\le k\le N-2\). The half-filled even-\(N\) asymptotic and all claimed limits follow directly.

## Verification

The reproducible Python program `verification/check_capture.py` builds the complete \(k\)-particle Hamiltonians directly in their occupation bases, including the fermionic exchange signs. For all \(4\le N\le9\) and \(1\le k<N\), it independently computes the spectral-sector intersections with the loss projector for both statistics: 66 spectral-rank cases agree with the claimed dark dimensions and capture probabilities. It also constructs the non-Hermitian generator and computes the trace of its finite-time no-jump evolution at \(t=600\) for 48 combinations of system size, filling, statistics and loss rate. The largest discrepancy from the predicted asymptotic survival was below \(1.1\times10^{-13}\). The proof above, rather than finite numerical tests, establishes the formulas for all allowed integers.

## Relationship to prior work

The quantum-walk formalism for multiple identical particles and the distinction between hard-core bosons and fermions are established in Qin et al. [1] and Large, Underwood and Feder [2]. Wong [3] treats coherent spatial search on Johnson graphs, whereas the present problem has an entire coordinate face subject to irreversible loss and compares physical particle statistics. Le et al. [4] develop dark-subspace transport methods for single excitations; their general criterion motivates Step 1 but does not state or evaluate the many-particle coordinate-face dark ranks. Malo et al. [5] examine statistics-dependent loss in one-dimensional lattices, not the exact all-filling complete-network law. The known Johnson scheme and Boolean up/down operators underlie Step 2. The resulting combined capture classification, especially the half-filling disparity between statistics, is the contribution considered here; historical originality is not independently certified.

## Limitations

The classification is for the probability of at least one loss, from an exactly maximally mixed fixed-particle sector, on a complete graph with real uniform hopping, hard-core occupancy, one local loss operator and no other processes. No claim is made about first-jump time distributions, repeated losses, disorder, extended networks, other initial mixtures beyond their dark-projector formula, or robustness to extra interactions. Symmetry breaking can eliminate the dark states. The finite computations are consistency checks, not proof for untested system sizes. Historical-priority risk persists for specialized many-body local-loss and Johnson-scheme literature.

## References

[1] X. Qin, Y. Ke, X. Guan, Z. Li, N. Andrei and C. Lee, *Quantum Walks of Two Interacting Particles in One Dimension*, arXiv:1402.3349 (first public 2014-02-14). https://arxiv.org/abs/1402.3349

[2] S. J. Large, M. S. Underwood and D. L. Feder, *Perfect quantum state transfer of hard-core bosons on weighted path graphs*, arXiv:1412.1022 (first public 2014-12-02). https://arxiv.org/abs/1412.1022

[3] T. G. Wong, *Quantum Walk Search on Johnson Graphs*, arXiv:1601.04212 (first public 2016-01-16). https://arxiv.org/abs/1601.04212

[4] T. P. Le, L. Donati, S. Severini and F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482 (2017). https://arxiv.org/abs/1707.07482

[5] J. Yago Malo, E. P. L. van Nieuwenburg, M. H. Fischer and A. J. Daley, *Particle statistics and lossy dynamics of ultracold atoms in optical lattices*, arXiv:1709.03464 (2017). https://arxiv.org/abs/1709.03464

[6] P.-A. Bernard, N. Crampé and L. Vinet, *Entanglement of Free Fermions on Johnson Graphs*, arXiv:2104.11581 (2021), regarding a different fermionic model on the Johnson graph as its physical site graph. https://arxiv.org/html/2104.11581v1
