# Exact fixed-cardinality cut-entanglement law for cycle graph states

## Finding

Let \(C_n\) be the simple cycle on \(n\ge3\) vertices, with its standard qubit graph state \(|C_n\rangle\). For every vertex set \(S\subseteq V(C_n)\), write \(h_n(S)\) for the bipartite entanglement entropy in **bits** across \(S\mid V(C_n)\setminus S\). Define the bivariate enumerator
\[
\mathcal E_n(z,t)=\sum_{S\subseteq V(C_n)}z^{|S|}t^{h_n(S)}.
\]
All exponents are nonnegative integers. Put
\[
T(z,t)=\begin{pmatrix}
1&0&0&t\\
1&0&1&0\\
0&zt&z&0\\
z&0&z&0
\end{pmatrix}.
\]
**For every integer \(n\ge3\), the exact identity is**
\[
\boxed{\mathcal E_n(z,t)=\operatorname{tr}(T(z,t)^n)
+\mathbf 1_{2\mid n}\,2z^{n/2}t^{n/2-1}(1-2t).}
\]
Thus, simultaneously for every \(0\le k\le n\) and every integer \(h\ge0\), the exact number of cuts having a specified subsystem size and entropy is
\[
N_{n,k,h}=[z^kt^h]\mathcal E_n(z,t),\qquad
\Pr\{h_n(S)=h\mid |S|=k\}=\frac{N_{n,k,h}}{\binom nk},
\]
where the subset is uniform among size-\(k\) sets. In particular, the exact Shannon entropy of this cut-rank distribution (the entanglement-heterogeneity statistic studied in the motivating literature) is
\[
H_{n,k}=-\sum_{h:N_{n,k,h}>0}\frac{N_{n,k,h}}{\binom nk}
\log_2\left(\frac{N_{n,k,h}}{\binom nk}\right).
\]
The matrix has characteristic polynomial
\[
\det(\lambda I-T)=\lambda\left(\lambda^3-(1+z)\lambda^2+z(1-2t)\lambda+zt(1+z)\right),
\]
so the polynomial is computable for arbitrary \(n\) using a fixed-dimensional polynomial recurrence, without enumerating subsets.

For a uniformly random unrestricted subset, the complete univariate law and its first-moment and asymptotic consequences are
\[
\mathcal E_n(1,t)=\left(\frac{1+\sqrt{1+8t}}2\right)^n+
\left(\frac{1-\sqrt{1+8t}}2\right)^n+1
+\mathbf 1_{2\mid n}\,2t^{n/2-1}(1-2t),
\]
\[
\mathbb E h_n(S)=
\begin{cases}
\frac n3(1-2^{1-n}),& n\text{ odd},\\
\frac n3-\frac{n+6}{3\cdot2^n},& n\text{ even},
\end{cases}
\]
\[
\operatorname{Var}(h_n(S))=\frac{2n}{27}+O(n^2 2^{-n}),
\qquad
\frac{h_n(S)-n/3}{\sqrt{2n/27}}\xrightarrow[n\to\infty]{\mathrm{law}}N(0,1).
\]
Here the limiting Gaussian statements concern **unrestricted uniformly random subsets**, not uniformly random balanced subsets.

## Assumptions and scope

The cycle is unweighted, has no loops or multiple edges, and is indexed cyclically. The graph state is \(|C_n\rangle=\prod_{i=1}^n \mathrm{CZ}_{i,i+1}|+\rangle^{\otimes n}\), with \(n+1\equiv1\). The bipartite entropy is the ordinary von Neumann entropy of the pure graph state's reduced density matrix with base-two logarithm; all its Rényi entropies of nonnegative order agree for every bipartition because its nonzero reduced spectrum is uniform. Empty and full sets are allowed and contribute entropy zero. The matrix entries and ranks used below are over \(\mathbb F_2\). No random Hamiltonian dynamics or noisy preparation is assumed.

## Proof

**1. Cut rank equals entanglement.** For any simple graph, the computational-basis amplitude of its graph state is, up to a fixed normalization, a quadratic binary phase. Across \(S\mid S^c\), phases internal to one side are local diagonal unitaries and do not affect Schmidt coefficients. The cross phase is \((-1)^{a^\top\Gamma_{S,S^c}b}\). Gaussian elimination over \(\mathbb F_2\), accompanied by local invertible binary changes of basis, puts the cross adjacency matrix into a rank-\(r\) identity block. Its associated bipartite state is locally unitary equivalent to \(r\) Bell pairs and unentangled factors. Therefore
\[
h_n(S)=\operatorname{rank}_{\mathbb F_2}\Gamma_{S,S^c},
\]
and the reduced nonzero eigenvalues are exactly \(2^{-h_n(S)}\).

**2. Crossing-edge runs.** Label the membership of vertex \(i\) by \(b_i=\mathbf1_{i\in S}\) and write \(w_i=b_i\oplus b_{i+1}\), with cyclic subscripts. An edge crosses the cut precisely when \(w_i=1\). If some \(w_i=0\), the crossing-edge graph is a disjoint union of paths formed by maximal consecutive runs of \(L\ge1\) crossing edges. Each such path is alternately colored by membership of \(S\) and \(S^c\). The corresponding bipartite adjacency matrix has full rank on its smaller side, namely \(\lceil L/2\rceil\): along a path, successively deleting a leaf with its adjacent vertex exhibits an upper-triangular full-size minor with diagonal entries one. Direct sums over components imply
\[
h_n(S)=\sum_{\text{maximal runs}}\left\lceil \frac L2\right\rceil
\qquad\text{if some }w_i=0.
\]

**3. A parity transfer.** Scan the directed cycle. Attach a binary state \((b,r)\), with \(b\) the current vertex-membership bit and \(r\) the parity of the length of the crossing-edge run immediately preceding the current edge: \(r=0\) at the start of a run and after a noncrossing edge. Advancing from \(b\) to \(b'\) contributes \(z^b\). If \(b'=b\), the run ends, the parity resets to zero, and the entropy increment is zero. If \(b'\ne b\), the run parity flips, and the entropy increases by one precisely when the previous run parity is zero. With state order \((0,0),(0,1),(1,0),(1,1)\), these rules give the displayed transfer matrix \(T(z,t)\).

If at least one edge is not crossing, that edge fixes a unique reset state, and therefore each labeled subset has exactly one compatible closed state walk. Its contribution to \(\operatorname{tr}T^n\) is exactly \(z^{|S|}t^{h_n(S)}\).

**4. Alternating-cycle correction.** For odd \(n\), no membership sequence has every edge crossing; hence the transfer trace is already the answer. For even \(n=2m\), there are exactly two fully alternating membership sequences, each of size \(m\). Their crossing-edge graph is the entire cycle, not a collection of paths. The bipartite \(m\times m\) adjacency matrix is \(I+P\), where \(P\) is cyclic permutation on \(m\) sites, including the \(m=2\) case. Over \(\mathbb F_2\), its kernel is the one-dimensional constant subspace, so its rank is \(m-1\). The actual two sequences contribute \(2z^m t^{m-1}\). The transfer trace instead has two compatible parity phases for each sequence, each contributing \(z^m t^m\), hence a spurious total \(4z^m t^m\). Subtracting this and inserting the true contribution gives exactly the theorem, including \(n=4\) and all larger even sizes.

**5. Moments and Gaussian limit.** At \(z=1\), \(T\) has eigenvalues \(0,1,\lambda_+(t),\lambda_-(t)\), where \(\lambda_\pm(t)=(1\pm\sqrt{1+8t})/2\). This yields the stated univariate polynomial. At \(t=1\), it sums to \(2^n\), and differentiating at one gives both exact cases of the mean. For the moment-generating function, substitute \(t=e^s\). In a fixed complex neighborhood of \(s=0\), \(\lambda_+(e^s)\) is the unique strictly dominant eigenvalue; the other eigenvalues and the even-cycle correction are exponentially smaller uniformly on a sufficiently small neighborhood. Direct differentiation gives
\[
\log\left(\frac{\lambda_+(e^s)}2\right)
=\frac s3+\frac{s^2}{27}+O(s^3).
\]
The moment expansion yields variance \(2n/27+O(n^2 2^{-n})\). Replacing \(s\) by \(is/\sqrt{2n/27}\) and subtracting the mean proves convergence of characteristic functions to \(e^{-s^2/2}\), establishing the displayed central limit theorem.

## Verification

The standalone Python 3 program `verify_cycle_entanglement.py` requires only the standard library. It computes each coefficient of the bivariate transfer formula by dynamic polynomial propagation. Independently, it enumerates **all** vertex subsets of every cycle of sizes \(3\le n\le15\), constructs each cut adjacency matrix, and performs exact binary Gaussian elimination. Every pair \((k,h)\) agrees; total counts, complement symmetry, and exact means also agree. These finite tests corroborate the analytic proof for arbitrary \(n\); enumeration through fifteen vertices is not a substitute for the infinite proof.

For the balanced cut of \(C_{12}\), the distribution at entropies \(2,3,4,5,6\) has exact counts \((12,96,306,386,124)\) out of \(\binom{12}{6}=924\), yielding \(H_{12,6}=1.8637129063345772\) bits. This agrees with the approximate histogram-based value reported in the motivating finite computation.

## Relationship to prior work

The 2025 study of fixed-cardinality cut-rank heterogeneity by Sakib defines the Shannon entropy of the cut-rank distribution and evaluates cycles empirically for \(n\le12\), including the balanced \(C_{12}\) histogram. The present finding supplies the exact **joint polynomial in subsystem cardinality and cut entropy for every cycle size**, allowing every such probability and Shannon statistic to be recovered, together with the unrestricted mean, variance, and limit law. These all-size statements are not provided by the finite tables and plots in the inspected source.

Nguyen and Oum study the average cut-rank of general graphs and its structural consequences; a mean does not determine the conditional distribution at fixed subset size. The standard graph-state cut-rank/Schmidt-rank identity is used, not claimed as new. Rao and collaborators study entanglement associated with graph-state circuit blocks and particular contiguous cuts; that is a different sampling problem from every size-\(k\) subset of a cycle.

The closest relevant publicly accessible cycle rank-enumerator concerns ranks of **arbitrarily weighted antisymmetric full-cycle adjacency matrices** over finite fields, for graphical-group character degrees. Those matrices, rank statistics, and weight choices do not encode the binary-cut adjacency rank conditional on the number of chosen vertices. Both arguments exploit path-run decomposition, but the rank-enumerator's specialization does not provide the present bivariate probability law. No equivalently strong cut-entropy enumerator was identified in the targeted literature comparison; absence from searches is not proof of novelty.

## Limitations

The theorem is exact for simple unweighted cycle graph states, not weighted graph states, general regular graphs, arbitrary graph-state local-Clifford orbits expressed without a cycle representative, or noisy states. The Gaussian limit concerns **unconditioned** random cuts, not conditioned balanced cuts. Neither the numerical finite-size figures in motivating literature nor the present exact entanglement distribution imply an operational quantum speedup or establish a link to simulation complexity. An equivalent transfer recurrence could exist under different graph-polynomial terminology not found in the source searches; this is a remaining priority risk.

## References

1. S. M. N. Sakib, “Entanglement Rank Entropy: A Graph-Theoretic Invariant of Bipartite Entanglement Heterogeneity,” public manuscript posted 28 November 2025, DOI:10.6084/m9.figshare.30740282; public full text https://www.researchgate.net/publication/398089419_S_M_Nazmuz_Sakib_Entanglement_Rank_Entropy_A_Graph-Theoretic_Invariant_of_Bipartite_Entanglement_Heterogeneity.
2. H.-T. Nguyen and S.-il Oum, “The average cut-rank of graphs,” arXiv:1906.02895v1 (2019), https://arxiv.org/abs/1906.02895.
3. M. Hein, J. Eisert, and H. J. Briegel, “Multi-party entanglement in graph states,” arXiv:quant-ph/0307130, https://arxiv.org/abs/quant-ph/0307130.
4. C. Rao and collaborators, “Graph-State Circuit Blocks control Entanglement and Scrambling Velocities,” arXiv:2605.11076v1 (11 May 2026), https://arxiv.org/abs/2605.11076.
5. “Cycle graphical groups have an explicit character-degree enumerator,” published published-finding corpus record, 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-cycle-graphical-groups-have-an-explicit-character-degree-enumera--a874723da77e.
