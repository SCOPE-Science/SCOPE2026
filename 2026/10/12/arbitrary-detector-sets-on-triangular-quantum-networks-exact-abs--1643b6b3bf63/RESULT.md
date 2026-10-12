# Arbitrary detector sets on triangular quantum networks: exact absorption and a two-detector gap

## Finding

Fix an integer \(N\geq3\). The triangular network \(J(N,2)\) has as vertices the \(M=\binom{N}{2}\) unordered pairs of \(\{1,\ldots,N\}\); pairs are adjacent when they share exactly one element. Choose an arbitrary nonempty detector set \(D\) of pair-vertices. Regard \(D\) as the edge set of a simple graph \(F\) on \(N\) labeled vertices, and let \(G\) be the complementary edge graph, so \(E(G)=E(K_N)\setminus D\).

For a graph \(X\) on this vertex set, let \(b(X)\) be its number of bipartite connected components, **including isolated vertices**. For a bipartite component, its two color classes have well-defined cardinalities up to interchange. Define \(u(F)=1\) when *every* bipartite component of \(F\) has equally large color classes, and \(u(F)=0\) otherwise. In particular, the universal quantifier is true when there is no bipartite component.

Let \(g\in\mathbb R\setminus\{0\}\), and let every \(e\in D\) have arbitrary positive population-loss rate \(\kappa_e>0\). The effective no-reaction Hamiltonian is
\[
H_{\mathrm{eff}}=gA(J(N,2))-\frac{i}{2}\sum_{e\in D}\kappa_e|e\rangle\langle e|.
\]
The **exact dimension of the absorbing spectral subspace** (the orthogonal complement of all no-loss Hamiltonian eigenstates) is
\[
\boxed{R(D)=1+N-b(F)-u(F)+|D|-b(G).}
\]
Equivalently, the subspace of perpetually dark states has dimension
\[
\boxed{\dim\mathcal D(D)=b(F)+u(F)-1+|E(G)|-N+b(G).}
\]
For *every* unit initial state \(\psi\), the infinite-time absorption probability equals \(\|P_{\mathcal D(D)^\perp}\psi\|^2\); both formulas and the probability are independent of the positive loss rates and the nonzero hopping magnitude.

**Complete absorption criterion.** Every initial state is eventually absorbed if and only if the following two simultaneous conditions hold: (i) either \(F\) has no bipartite connected components, or \(F\) has precisely one bipartite connected component and its two color classes have different sizes; (ii) every component of \(G\) is a tree (an isolated vertex counts as a tree) or a connected unicyclic graph whose unique cycle is odd.

**Sharp detector count.** The minimum \(|D|\) making absorption certain for every initial state is
\[
\boxed{m(N)=\begin{cases}
2,&N=3,\\
3,&N=4,\\
\binom{N}{2}-N,&N\geq5.
\end{cases}}
\]
For \(N\geq5\), this is precisely **two detectors fewer** than the known ordinary graph zero-forcing number \(Z(J(N,2))=\binom{N}{2}-N+2\). This is a comparison of different observability criteria, not a contradiction of zero-forcing theory.

## Assumptions and scope

The graph is finite and undirected. Edges of \(J(N,2)\) have the same real nonzero coherent hopping; there are no independent onsite potentials or coherent particle interactions. Every detector acts locally and irreversibly, with a strictly positive rate; no detector has a zero rate. Detector positions may be any nonempty subset, need not be connected, and rates need not agree. Evolution refers to the effective no-jump propagator \(e^{-itH_{\mathrm{eff}}}\), with loss probability \(1-\|e^{-itH_{\mathrm{eff}}}\psi\|^2\). All claims concern the infinite-time limit. An arbitrary initial density matrix is also covered by replacing the pure-state projection norm with \(\operatorname{tr}(P_{\mathcal D(D)^\perp}\rho)\).

## Proof

**1. Three distinct spectral sectors.** Let \(B\) be the \(N\)-by-\(M\) unsigned incidence matrix of \(K_N\): its column for \(e=\{a,b\}\) contains a \(1\) at rows \(a,b\), zero elsewhere. Directly counting shared endpoints gives
\[
A(J(N,2))=B^{\mathsf T}B-2I_M,\qquad
BB^{\mathsf T}=(N-2)I_N+\mathbf 1_N\mathbf 1_N^{\mathsf T}.
\]
Since \(N\geq3\), the second matrix is positive definite; thus \(\operatorname{rank}B=N\). The mutually orthogonal eigenspaces of \(A\), with their eigenvalues and dimensions, are
\[
\begin{array}{c|c|c}
\operatorname{span}\{\mathbf1_M\}&2(N-2)&1\\
B^{\mathsf T}(\mathbf1_N^\perp)&N-4&N-1\\
\ker B&-2&M-N.
\end{array}
\]
The three displayed eigenvalues are pairwise distinct for every integer \(N\geq3\), even if the final space has dimension zero when \(N=3\).

**2. The loss-free subspace is exactly the dark eigenspace sum.** Let \(K=\sum_{e\in D}\kappa_e|e\rangle\langle e|\). Then
\[
\frac{d}{dt}\|e^{-itH_{\mathrm{eff}}}\psi\|^2
=-\langle e^{-itH_{\mathrm{eff}}}\psi,K e^{-itH_{\mathrm{eff}}}\psi\rangle\leq0.
\]
If a right eigenvector of \(H_{\mathrm{eff}}\) has purely real eigenvalue, taking the imaginary part of its eigenvalue equation yields \(\langle\phi,K\phi\rangle=0\); strict positivity of the detector rates forces \(\phi_e=0\) for every \(e\in D\). It is then an eigenvector of \(gA\). Conversely every \(gA\)-eigenvector vanishing on \(D\) remains a real-eigenvalue eigenvector of \(H_{\mathrm{eff}}\). The orthogonal span of all such vectors is invariant under the Hamiltonian and its adjoint; on its orthogonal complement all eigenvalues of the dissipative generator have strictly negative real parts. Finite-dimensional Jordan theory therefore proves exponential decay on that complement (with constants depending on the fixed parameters). Hence the asymptotic survival probability is projection onto the dark sum over the three distinct Hamiltonian eigenspaces.

**3. Unsigned incidence rank lemma.** For an arbitrary simple graph \(X\) on \(N\) vertices, the equations \(B_X^{\mathsf T}z=0\) say \(z_a+z_b=0\) across each edge. On a connected bipartite component, a nonzero solution alternates between the two color classes, giving one free scalar. On a component containing an odd cycle this scalar must vanish. An isolated vertex is a bipartite component and likewise contributes one free scalar. Consequently
\[
\dim\ker B_X^{\mathsf T}=b(X),\qquad \operatorname{rank}B_X=N-b(X).
\]
On a bipartite component the sum of the alternating solution is its scalar multiplied by the difference of the two color-class sizes. Thus the sum functional vanishes on all of \(\ker B_F^{\mathsf T}\) precisely when \(u(F)=1\). Intersecting with \(\mathbf1_N^\perp\), the restriction of \(B_F^{\mathsf T}\) to \(\mathbf1_N^\perp\) has rank
\[
(N-1)-\bigl(b(F)-(1-u(F))\bigr)=N-b(F)-u(F).
\]
This calculation also covers \(b(F)=0\), because its sum functional vanishes vacuously and then \(u(F)=1\).

**4. Sum of observable ranks.** The top eigenvector \(\mathbf1_M\) is nonzero at every detector, so its detector restriction has rank \(1\). The middle sector's restriction is the map in Step 3 and has rank \(N-b(F)-u(F)\). For the bottom sector, restriction to coordinates \(D\) on \(\ker B\) has kernel consisting of the zero extensions of \(\ker B_G\); using the rank lemma,
\[
\dim\ker B_G=|E(G)|-N+b(G).
\]
Since \(\dim\ker B=M-N\), the detector restriction on this sector has rank
\[
(M-N)-\bigl(|E(G)|-N+b(G)\bigr)=|D|-b(G).
\]
The observable spectral subspace is the orthogonal direct sum of these three observable components. Adding their ranks gives \(R(D)\) as claimed; subtracting from \(M\) gives the dark dimension. All terms are exact integer quantities independent of hopping or positive detector strengths.

**5. Characterization of full absorption.** The middle dark dimension \(b(F)+u(F)-1\) is zero exactly when \(b(F)=0\), or \(b(F)=1\) with an unbalanced bipartite component. The bottom dark dimension \(|E(G)|-N+b(G)\) is a sum of nonnegative nullities of the unsigned incidence matrix of each component. A bipartite connected component has zero nullity exactly when it is a tree (edges equal vertices minus one). A nonbipartite connected component has zero nullity exactly when it is unicyclic, and its unique cycle is then odd. These conditions are independent and jointly equivalent to \(\dim\mathcal D(D)=0\).

**6. Sharp minimum.** For \(N\geq5\), the bottom eigenvalue \(-2\) has multiplicity \(M-N\). At most one independent condition on this eigenspace can be imposed by each detector, so \(|D|\geq M-N\). The bound is attained as follows. If \(N\geq5\) is odd, take \(G\) to be a spanning odd \(N\)-cycle; if \(N\geq6\) is even, take \(G\) to be an odd cycle on \(N-1\) vertices with the remaining vertex attached by one pendant edge. In both cases \(|E(G)|=N\) and \(G\) is connected odd-unicyclic. Its complement \(F\) is connected and nonbipartite: for \(N=5\), the complement of a five-cycle is itself a five-cycle; for odd \(N\geq7\), the complement of the cycle is connected and contains a triangle; for even \(N\geq6\), the pendant vertex connects in \(F\) to all but one cycle vertex, while the omitted cycle vertex has another edge in \(F\), and a triangle uses the pendant vertex and two nonconsecutive cycle vertices. Therefore \(b(F)=b(G)=0\), \(u(F)=1\), and \(R(D)=M\) with exactly \(M-N\) detectors.

For \(N=3\), one detector cannot resolve the \(2\)-dimensional middle eigenspace, but the two edges \(\{1,2\},\{1,3\}\) suffice. For \(N=4\), any two-edge \(F\) has at least two bipartite components (either a length-two path plus an isolated vertex, or two disjoint edges), preventing full observation of the middle eigenspace. The three-edge star \(D=\{\{1,2\},\{1,3\},\{1,4\}\}\) suffices: \(F\) is a connected bipartite graph with unequal color-class sizes, while \(G\) consists of one triangle and one isolated vertex. This proves all three cases of \(m(N)\). Finally, the published zero-forcing number \(M-(N-2)\) exceeds \(M-N\) by exactly two for \(N\geq5\).

## Verification

The accompanying \(\texttt{verify.py}\) constructs \(J(N,2)\) independently by pair intersection, diagonalizes its adjacency matrix, and compares the directly calculated detector-restriction ranks with the bipartite-component formula. It tests every nonempty detector subset for \(N=3,4,5\), samples additional subsets for \(N=6,7,8\), checks constructive witnesses through \(N=12\), exhaustively enumerates minimum detector counts for \(N=3,4,5,6\), and compares predicted dark multiplicities with the real-axis spectrum of explicit non-Hermitian lossy matrices at unequal random positive rates.

With NumPy installed, execute \(\texttt{python3 verify.py}\). Replayed output:

```text
VERIFY_OK spectral_ranks=1760 threshold_checks=14 loss_spectrum=80
```

These checks are finite corroborations; every quantified statement for arbitrary \(N\), arbitrary \(D\), all positive rates, and every initial state follows from the algebraic proof above rather than enumeration.

## Relationship to prior work

General work on hitting times and dark states (Varbanov, Krovi, Brun, 2008) and on irreversible random multi-trap transport (Agliari, 2011) establishes the physical context. Their models and statements do not give the exact arbitrary-detector triangular-network component formula. Wong (2016) studies **unitary marked-vertex spatial search** on Johnson graphs, whereas the result here concerns **irreversible losses at any subset of vertices**. Novo and collaborators (2015) and Razzoli, Paris, and Bordone (2020/2021) develop subspace projection methods for trapping, mainly with a single trap; the latter explicitly identifies multiple trapping sites as further work. Those general methods are used, not presented as new.

Vorob'ev, Mogilnykh, and Valyuzhenich (2017) characterize **minimum support of individual Johnson-graph eigenfunctions**. An arbitrary detector set destroys *all* dark eigenfunctions only when the restriction maps are simultaneously injective on each eigenspace; the minimum support of a single eigenfunction does not supply this all-subset criterion. Abiad, Simoens, and Zeijlemaker (arXiv 2023; journal 2024) calculate \(Z(J(N,2))=M-N+2\), a graph-wide zero-forcing parameter. Their result is not an exact minimum observability number for the **particular** adjacency Hamiltonian, nor does it provide the complete bipartite-component classification. The present two-detector gap is therefore a distinction between established zero forcing and the evaluated quantum-absorption condition, not a claim to have discovered the published zero-forcing result.

The unsigned-incidence rank lemma and the spectral decomposition of triangular graphs are classical ingredients. The contribution assessed here is their combined **all-detector-set trapping classification**, explicit full-absorption criterion, and sharp detector threshold including the comparison with zero forcing. Literature searches do not constitute a proof of publication priority.

## Limitations

The theorem depends on ideal, homogeneous hopping on \(J(N,2)\) and strictly positive localized irreversible detector rates. It does not give sitewise closed-form capture probabilities for arbitrary \(D\), finite-time decay bounds uniform in parameters, optimal expected hitting times, or results under disorder, dephasing, directed edges, different two-particle interactions, or arbitrary Johnson graphs \(J(N,k)\) with \(k>2\). Its novelty is subject to independent literature-priority assessment, especially in control-theoretic treatments of line-graph observability.

## References

1. M. Varbanov, H. Krovi, T. A. Brun, “Hitting time for the continuous quantum walk,” arXiv:0803.3446 (first public preprint 2008-03-24), https://arxiv.org/abs/0803.3446.
2. E. Agliari, “Trapping of Continuous-Time Quantum walks on Erdos-Renyi graphs,” arXiv:1102.3994 (first public preprint 2011-02-19), https://arxiv.org/abs/1102.3994.
3. S. Novo et al., “Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs,” Scientific Reports 5, 13304 (2015), https://www.nature.com/articles/srep13304.
4. T. G. Wong, “Quantum Walk Search on Johnson Graphs,” arXiv:1601.04212 (first public preprint 2016-01-16), https://arxiv.org/abs/1601.04212.
5. K. Vorob'ev, I. Mogilnykh, A. Valyuzhenich, “Minimum supports of eigenfunctions of Johnson graphs,” arXiv:1706.03987 (2017-06-13), https://arxiv.org/abs/1706.03987.
6. L. Razzoli, M. G. A. Paris, P. Bordone, “Transport efficiency of continuous-time quantum walks on graphs,” arXiv:2011.13794 (2020), https://arxiv.org/abs/2011.13794.
7. A. Abiad, R. Simoens, S. Zeijlemaker, “On the diameter and zero forcing number of some graph classes in the Johnson, Grassmann and Hamming association scheme,” arXiv:2302.07757 (2023; Discrete Applied Mathematics 348, 221–230, 2024), https://arxiv.org/abs/2302.07757.
8. L. Dai, “Minimum leader selection for controllability of undirected graphs with leader–follower framework,” IET Control Theory & Applications (2023), https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/cth2.12385.
