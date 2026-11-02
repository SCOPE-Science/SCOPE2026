# Universal finite-step mixing and stroboscopic memory in dynamically percolated quantum graphs

## Finding
Let \(G=(V,E)\) be any finite, connected, simple, undirected graph with \(n=|V|\ge2\). Each edge \(e\) is independently present in each time step with fixed probability \(p_e\in(0,1)\); different time steps are independent. For a retained-edge subset \(A\subseteq E\), define its ordinary combinatorial Laplacian \(L_A\) on \(\mathbb C^n\), including isolated vertices. The unitary evolution for a step of duration \(\tau>0\), in units where the hopping parameter is one, is \(U_A=e^{-i\tau L_A}\). The averaged step channel on density operators is
\[
\Phi_\tau(\rho)=\sum_{A\subseteq E}w_AU_A\rho U_A^\dagger,
\qquad
w_A=\prod_{e\in A}p_e\prod_{e\notin A}(1-p_e).
\]
Write \(s=n^{-1/2}(1,\dots,1)^\mathsf T\), \(P=|s\rangle\langle s|\), and \(Q=I-P\).

**Universal nonresonant limit.** If \(\tau\notin\pi\mathbb Z\), then for every density operator \(\rho\),
\[
\boxed{\lim_{m\to\infty}\Phi_\tau^m(\rho)
=\operatorname{tr}(P\rho)P+
\frac{1-\operatorname{tr}(P\rho)}{n-1}Q.}
\]
The convergence is exponential at each fixed admissible graph, collection of probabilities, and step duration. In particular, a localized initial state \(|v\rangle\langle v|\) converges to \(I/n\) for **every** connected graph, independent of its geometry and edge probabilities. For a general initial state, the uniform-mode population remains conserved and its asymptotic state need not equal \(I/n\).

**Sharp stroboscopic obstruction.** The exclusion of \(\tau\in\pi\mathbb Z\) cannot be removed from a theorem valid for all connected graphs. On the three-vertex path \(P_3\), with any two edge probabilities in \((0,1)\), let \(r\) be their product. For \(\tau=k\pi\) with positive integer \(k\):

- If \(k\) is even, \(\Phi_\tau\) is exactly the identity channel.
- If \(k\) is odd, then for every \(m\ge0\),
\[
\Phi_\tau^m(\rho)=P\rho P+Q\rho Q+(1-2r)^m(P\rho Q+Q\rho P).
\]
Hence its limit is \(P\rho P+Q\rho Q\), rather than the nonresonant universal limit. A particle initially localized at any vertex has limiting probability \(5/9\) at the starting vertex and \(2/9\) at each of the other two vertices. At even multiples of \(\pi\), it remains localized. Thus the exact return-probability limits on \(P_3\) are \(1/3\), \(5/9\), and \(1\), for noninteger, odd-integer, and even-integer multiples of \(\pi\), respectively.

## Assumptions and scope
The graph is finite, connected, undirected and simple; its Laplacian is the **combinatorial** Laplacian, not the adjacency matrix or a normalized Laplacian. All retained edges have unit coupling. Retention probabilities need not be identical but are strictly between zero and one, so every edge subset, including the empty set, has positive probability. The subset is resampled independently at every step. The limit concerns the ensemble-averaged density operator at integer step counts, with \(\tau>0\) held fixed before \(m\to\infty\). There is no position measurement between steps, no internal coin, no disorder in the on-site energies, and no claim concerning a single realization's pure-state limit.

## Proof
For each edge \(e=\{a,b\}\), define \(b_e=|a\rangle-|b\rangle\) and \(L_e=b_eb_e^\dagger\). Since \(\|b_e\|^2=2\), its eigenvalues are \(0\) and \(2\), giving the exact one-edge formula
\[
U_e=I+\frac{e^{-2i\tau}-1}{2}L_e.
\]
Let \(S_e=I-L_e\). Acting on vertex vectors, \(S_e\) swaps \(|a\rangle\) and \(|b\rangle\) while fixing every other basis vector. When \(\tau\notin\pi\mathbb Z\), \(e^{-2i\tau}-1\ne0\), and therefore an operator commutes with \(U_e\) precisely when it commutes with \(S_e\).

Consider the averaged conjugation map \(\Phi_\tau\) as a linear operator on all complex \(n\)-by-\(n\) matrices with the Hilbert--Schmidt norm. For any matrix \(X\), the Hilbert--Schmidt norms of \(U_AXU_A^\dagger\) all equal \(\|X\|_2\). The finite weighted variance identity yields
\[
\|X\|_2^2-\|\Phi_\tau(X)\|_2^2
=\frac12\sum_{A,B\subseteq E}w_Aw_B
\big\|U_AXU_A^\dagger-U_BXU_B^\dagger\big\|_2^2.
\]
Suppose \(\Phi_\tau(X)=zX\) with \(|z|=1\) and \(X\ne0\). The variance vanishes; since every \(w_A>0\), all conjugates coincide. Taking \(A=\varnothing\), whose unitary is \(I\), shows that \(z=1\) and that \(X\) commutes with every \(U_A\). Conversely, an operator commuting with every \(U_A\) is fixed. Thus the entire peripheral eigenspace consists of fixed operators; there are no other eigenvalues of modulus one.

For nonresonant \(\tau\), the singleton subsets imply that fixed operators commute with every edge transposition \(S_e\). Since the graph is connected, its edge transpositions generate the full symmetric group on the vertices. A matrix invariant under conjugation by every vertex permutation has one common diagonal entry and one common off-diagonal entry, so it has the form \(aI+b\mathbf1\mathbf1^\mathsf T\), equivalently \(\operatorname{span}\{P,Q\}\). Conversely, \(L_As=0\) for every edge set \(A\), so every \(U_A\) preserves the decomposition \(P\oplus Q\) and commutes with both projectors. Therefore the fixed algebra is exactly \(\operatorname{span}\{P,Q\}\).

The channel is a Hilbert--Schmidt contraction, so an eigenvalue on the unit circle cannot have a nontrivial Jordan block (otherwise its powers would grow). All remaining eigenvalues lie strictly inside the unit disk. Moreover, the adjoint channel fixes \(P\) and \(Q\), so their expectation values are conserved. Consequently the power limit is the Hilbert--Schmidt orthogonal projection onto \(\operatorname{span}\{P,Q\}\), namely the claimed formula. Finite dimensionality implies exponential convergence, without asserting a size-uniform rate. For \(\rho=|v\rangle\langle v|\), \(\operatorname{tr}(P\rho)=1/n\), which makes the limit \(I/n\).

For the resonance example, take \(G=P_3\) with edges \(\{1,2\},\{2,3\}\). The single-edge Laplacians have spectrum \(\{0,0,2\}\) and the full path Laplacian
\[
L=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix}
\]
has spectrum \(\{0,1,3\}\), with the zero eigenvector \(s=(1,1,1)^\mathsf T/\sqrt3\). At every \(\tau=k\pi\), both single-edge unitaries are \(I\). If \(k\) is even, the full-graph unitary is also \(I\). If \(k\) is odd, it equals \(R=P-Q=2P-I\), as its eigenvalue is \(+1\) on the uniform mode and \(-1\) on its orthogonal complement. The both-edges event has probability \(r\), whereas all three other events act as \(I\); hence \(\Phi_\tau=(1-r)\mathrm{id}+r\operatorname{Ad}_R\). The diagonal blocks \(PXP+QXQ\) have eigenvalue one, and the off-diagonal blocks \(PXQ+QXP\) have eigenvalue \(1-2r\). Since \(0<r<1\), the latter has modulus less than one. This proves the finite-step identity and limiting formula. For localized \(|v\rangle\), the limiting density is \((|v\rangle\langle v|+R|v\rangle\langle v|R)/2\); the diagonal entries are exactly \(5/9\) and \(2/9\) at the other vertices. All boundary cases are covered.

## Verification
The included standalone `verify.py` constructs the four (or, on larger tested graphs, all) subset Laplacians independently and diagonalizes their unitary propagators. It builds each one-step superoperator as a Kronecker sum of unitary conjugation channels, checks that the eigenvalue one has multiplicity two for nonresonant examples, numerically verifies exponential convergence to the displayed limit on connected paths, a cycle, and a star, and checks the exact finite-step odd-multiple formula, even-multiple identity channel, and \(5/9,2/9,2/9\) vertex probabilities on \(P_3\). Run `python verify.py` with NumPy installed. The checks are numerical diagnostics; the arbitrary-graph theorem and singular cases are proved in the preceding section.

## Relationship to prior work
Darázs and Kiss introduced the independently resampled graph-Laplacian continuous-time quantum walk and proved the rapidly switching (zero step-size) time-rescaling limit. Their original 2012 preprint's Sections 5--7 examine finite step sizes numerically, including relaxation toward flat vertex probabilities; they do not give the all-connected-graph fixed-step channel limit or isolate integer-\(\pi\) stroboscopic resonances.

Kollár, Kiss, Novotný, and Jex established the general attractor-space method and explicit long-time behavior for **coined discrete-time** walks with broken links. Their state space, single-step operator and reflection rule differ from the coinless, subset-Laplacian matrix exponentials used here. The Hilbert--Schmidt peripheral-mode argument is consistent with their established random-unitary framework; it is not presented as a new general channel principle.

Shi, Dong, Petersen, and Johansson investigated permutation-based quantum consensus for networks of qubits under swap-generated master equations. Such continuous-time Lindblad symmetrization is conceptually related to the permutation commutant used here, but its generator is not the finite-step channel obtained by independently retaining edges and exponentiating the resulting Laplacian. In particular it supplies no \(\tau=k\pi\) three-site resonance classification. The new content is the evaluated arbitrary-connected-graph finite-step theorem and its sharp sampling obstruction, not the basic algebra of permutations.

## Limitations
No result is claimed at arbitrary resonant step times on graphs other than the explicit \(P_3\) calculation. Strictly positive probabilities for both the presence and absence of every edge are required for the nonresonant universal statement; deterministic edges can preserve extra modes. Nonuniform hopping strengths change the resonance set. The long-time limit and the fast-switching limit need not commute. The theorem concerns ensemble averages, not typical trajectory convergence, time-to-mixing bounds uniform in graph size, or interacting many-particle states. Historical originality remains subject to broader literature examination and independent review.

## References
1. Z. Darázs and T. Kiss, *Time evolution of continuous-time quantum walks on dynamical percolation graphs*, arXiv:1211.3550 (first publicly submitted 2012-11-15), https://arxiv.org/abs/1211.3550 .
2. B. Kollár, T. Kiss, J. Novotný, and I. Jex, *Asymptotic dynamics of coined quantum walks on percolation graphs*, arXiv:1204.6149 (first publicly submitted 2012-04-27), https://arxiv.org/abs/1204.6149 .
3. G. Shi, D. Dong, I. R. Petersen, and K. H. Johansson, *Reaching a Quantum Consensus: Master Equations that Generate Symmetrization and Synchronization*, arXiv:1403.6387 (first publicly submitted 2014-03-25), https://arxiv.org/abs/1403.6387 .
