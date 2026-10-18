# The complete fastest-mixing optimizer face of complete split graphs

## Finding
For integers \(k,m\ge2\), let \(G=K_k\vee\overline{K_m}\), the join of a clique of size \(k\) and an independent set of size \(m\). Among all *symmetric*, entrywise nonnegative, row-stochastic transition matrices \(P\) whose off-diagonal support is contained in the edges of \(G\), minimize the second-largest eigenvalue modulus \(\mu(P)=\|P-J/(k+m)\|_2\), where \(J\) is the all-ones matrix. No vertex or edge symmetry is assumed of \(P\).

Set
\[
 a_* = \begin{cases}2/(m+2k),&m<2k,\\1/m,&m\ge2k,\end{cases}
\qquad
 \mu_* = \begin{cases}m/(m+2k),&m<2k,\\1-k/m,&m\ge2k.\end{cases}
\]
The optimal value \(\mu_*\) and existence of an invariant optimal kernel also follow from the known clique-lift-of-star reduction [3]; **the result here is the entire unrestricted optimizer set and its sharp edge-support regimes**, rather than a new fastest-mixing value.

**All optimizers, including asymmetric edge allocations, are as follows.** Every clique-to-independent-set entry equals \(a_*\). Every independent-set diagonal entry equals \(1-ka_*\), and independent-set off-diagonal entries vanish. If \(m\ge2k\), the *only* optimum has zero clique-to-clique off-diagonal entries and zero clique diagonal entries. If \(m<2k\), put \(c=(2k-m)/(m+2k)\). One can choose an arbitrary weighted graph \(B=(b_{ij})\) on the \(k\) clique vertices satisfying
\[
 b_{ij}=b_{ji}\ge0\quad(i\ne j),\qquad
 d_i:=\sum_{j\ne i}b_{ij}\le c,
\]
and
\[
 \operatorname{spec}\left(L_B\big|_{\mathbf1^\perp}\right)
 \subseteq\left[\frac{2(k-m)}{m+2k},\frac{2k}{m+2k}\right],
 \qquad L_B=\operatorname{diag}(d_i)-B.
\]
Here \(B\) has zero diagonal, and the restriction in the spectral statement is to the \((k-1)\)-dimensional zero-sum subspace. The remaining clique diagonal entries are \(c-d_i\). Conversely, **every** such choice produces a globally fastest-mixing kernel.

Consequently, among unrestricted optimal kernels, clique-internal transitions are **necessary** when \(m<k\), **optional** when \(k\le m<2k\), and **absent in every optimum** when \(m\ge2k\). In the necessary regime, the positive-weight clique-internal edges must form a connected graph. The unrestricted fastest-mixing kernel is unique **if and only if** \(m\ge2k\).

## Assumptions and scope
Throughout, \(k,m\) are arbitrary integers at least two, every vertex has a self-loop available as holding probability, and off-diagonal transitions are permitted only within the clique or between clique and independent-set vertices. Stochasticity means that every row sums to one. The stationary measure is uniform because \(P\) is symmetric. The claim concerns the SLEM optimum and *all* its minimizers; it does not optimize other mixing metrics or permit directed, nonreversible chains.

For a weighted core graph \(B\), \(L_B\) denotes its standard combinatorial Laplacian; \(\mathbf1^\perp\) means the vectors whose clique-coordinate sum is zero. For \(k=2\), this subspace is one-dimensional and all conditions apply unchanged.

## Proof
**1. Universal two-mode lower bound.** Write the vertices in core-first order. Let \(X\) denote the \(k\)-by-\(m\) matrix of cross-edge probabilities and \(T=\sum_{i,j}X_{ij}\). Row nonnegativity gives \(0\le T\le k\). The independent-set principal block of \(P\) is diagonal. On the leaf-zero-sum space
\[
 U=\{(0,u):u\in\mathbb R^m,\ \textstyle\sum_j u_j=0\},
\]
the trace of its compression is \((m-1)(1-T/m)\). Every Rayleigh quotient on this space is at most \(\mu(P)\), hence \(\mu(P)\ge1-T/m\). For the unit-mean-contrast vector \(z=(\mathbf1_k/k,-\mathbf1_m/m)\in\mathbf1^\perp\), direct evaluation of the cross-edge Dirichlet form yields
\[
 \frac{z^\top Pz}{z^\top z}=1-T\left(\frac1k+\frac1m\right),
\]
so \(\mu(P)\ge\left|1-T(1/k+1/m)\right|\). Minimizing the maximum of these bounds over \(0\le T\le k\) gives \(\mu_*\). If \(m<2k\), the unique minimizing total is \(T_*=2km/(m+2k)\); if \(m\ge2k\), it is \(T_*=k\). The latter conclusion also follows because \(1-T/m\) is strictly decreasing.

**2. Equality forces uniformity across every cross edge.** When \(m<2k\), both bounds are attained: the compression of \(\mu_*I-P\) onto \(U\) has trace zero, while \(\mu_*I-P\) is positive semidefinite on \(\mathbf1^\perp\). Therefore \(Pu=\mu_*u\) for every \(u\in U\). The clique coordinates of this equation give \(Xu=0\) for all zero-sum \(u\), forcing each row of \(X\) to be constant. Equality in the contrast bound similarly forces \(Pz=-\mu_*z\); its clique coordinates then give the same constant \((1+\mu_*)/(k+m)=2/(m+2k)\) in every row. For \(m\ge2k\), equality \(T=k\) forces each clique row to spend its entire mass on leaves. The leaf-zero-sum trace bound again saturates and forces \(Pu=\mu_*u\) on \(U\). Thus cross-edge entries are constant along each clique row; stochasticity then makes them all \(1/m\). This also forces all core-internal and core-holding probabilities to vanish.

**3. Exact converse and the unrestricted optimizer face.** For \(m<2k\), uniform cross probability \(a_*=2/(m+2k)\) leaves a residual core row mass \(c=1-ma_*\). Any admissible core weights \(b_{ij}\) and diagonals \(c-d_i\) produce an orthogonal invariant decomposition into the constant subspace, the leaf-zero-sum space, the core-versus-leaf contrast, and the core-zero-sum space. The eigenvalues on the first three spaces are \(1\), \(\mu_*\), and \(-\mu_*\), respectively; on core-zero-sum vectors the operator is \(cI-L_B\). Thus \(\mu(P)=\mu_*\) if and only if all eigenvalues of \(cI-L_B\) lie in \([-\mu_*,\mu_*]\), giving exactly the stated spectral interval. A feasible witness exists for all \(m<2k\): take \(b_{ij}=c/k\) for each distinct clique pair; then \(cI-L_B\) vanishes on core-zero-sum vectors, and each core diagonal entry is \(c/k\). For \(m\ge2k\), the forced unique kernel has eigenvalues \(1\), \(1-k/m\) on leaf-zero-sum vectors, \(-k/m\) on the contrast, and zero on core-zero-sum vectors, so its SLEM is indeed \(1-k/m\).

**4. Sharp support regimes and uniqueness.** When \(m<k\), the lower endpoint \(2(k-m)/(m+2k)\) of the allowed core Laplacian spectrum is strictly positive, so the core graph must be connected. When \(k\le m<2k\), the zero core graph \(B=0\) obeys the spectral interval, while the positive complete-graph choice \(b_{ij}=c/k\) also obeys it. When \(m\ge2k\), only one optimum exists and its core has no positive off-diagonal entries. In the intermediate and lower regimes the strictly feasible uniform-core construction can be perturbed (or contrasted with the zero graph in the intermediate regime), showing nonuniqueness for all \(m<2k\).

## Verification
The accompanying \(verification.py\) checks exact rational spectra for \(2\le k\le9\) and \(2\le m\le12\), exact sample optimizer-face conditions, independent symmetry-invariant linear programs, and randomly generated non-invariant feasible transitions. The recorded successful invocation was \(\texttt{python verification.py}\), yielding \(\texttt{VERIFY\_OK 3343 checks}\). These finite computations only corroborate the analytic infinite-family proof; they do not establish it by enumeration.

For an explicit nonsymmetric optimizer choose \(k=3\), \(m=4\), every cross-edge probability \(1/5\), and exactly one positive clique edge of weight \(1/10\). The clique residual row mass is \(1/5\); its core Laplacian eigenvalues on zero-sum vectors are \(0\) and \(1/5\), both in the admissible interval \([-1/5,3/5]\). The resulting chain is optimal but not vertex-symmetric.

## Relationship to prior work
Boyd, Diaconis and Xiao [1] formulated fastest symmetric Markov-chain mixing as a semidefinite program. Boyd, Diaconis, Parrilo and Xiao [2] developed symmetry reduction and a complete multipartite graph SDP (Section 5.4.2), which includes the present graph as a case but does not characterize its unrestricted full optimizer face. Jafarizadeh [3] proves that clique lifting preserves optimal SLEM and constructs an optimal lifted chain; applying the star formulas of Section VI-E gives the present **optimal value** and a canonical symmetric optimum. Those known conclusions are **not** asserted to be original here. What is established beyond this constructive reduction is an if-and-only-if spectral characterization of **all**, potentially non-invariant, optimal core assignments; forced uniformity of **every** cross-edge transition; the two thresholds for core-edge necessity and uniqueness; and an explicit non-invariant family of additional optimizers.

## Limitations
The proof does not give a classification for arbitrary nonuniform target stationary distributions, nonreversible stochastic matrices, independent sets of size one, or other mixing objectives. The originality comparison is based on inspected relevant primary text and indexed searches, not an exhaustive theorem-proving search of all literature. In particular [3] strongly covers the optimal rate and a canonical solution, and the remaining claim is restricted to the entire optimizer set and its support transitions. A differently phrased published full-face classification cannot be ruled out solely from search results. Independent verification has not been performed.

## References
[1] S. Boyd, P. Diaconis and L. Xiao, “Fastest Mixing Markov Chain on a Graph,” *SIAM Review* 46 (2004), 667–689. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf

[2] S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” arXiv:0709.0955v1 (first posted 2007-09-06), *SIAM Journal on Optimization* 20 (2009), 792–819. https://arxiv.org/abs/0709.0955

[3] S. Jafarizadeh, “Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs,” arXiv:2501.02421. https://arxiv.org/abs/2501.02421
