# Cycle-type formula for spanning-tree completions of perfect matchings in crown graphs

## Finding
Let \(n\geq 3\), and let the crown graph \(\operatorname{Cr}_n\) have bipartition \(\{a_1,\ldots,a_n\}\) and \(\{b_1,\ldots,b_n\}\), with edges \(a_i b_j\) precisely when \(i\neq j\). Every perfect matching of \(\operatorname{Cr}_n\) is \(M_\sigma=\{a_i b_{\sigma(i)}:1\leq i\leq n\}\) for a derangement \(\sigma\) of \([n]\). Denote the lengths of the cycles of \(\sigma\) by \(\ell_1,\ldots,\ell_c\), including the lengths \(2\) with multiplicity, and let \(T_j\) be the Chebyshev polynomial of the first kind, defined by \(T_0(t)=1\), \(T_1(t)=t\), and \(T_{j+1}(t)=2tT_j(t)-T_{j-1}(t)\).

**Theorem.** The number \(N_n(\sigma)\) of spanning trees of \(\operatorname{Cr}_n\) containing every edge of \(M_\sigma\) is
\[
\boxed{N_n(\sigma)=\frac{2^{c-1}}{n^2}\prod_{j=1}^{c}\left(T_{\ell_j}(n-1)-(-1)^{\ell_j}\right).}
\]
In particular, the answer depends only on the cycle type of the derangement. For \(n=4\), a matching encoded by a \(4\)-cycle has \(36\) spanning-tree completions, whereas one encoded by two \(2\)-cycles has \(32\); thus different perfect matchings in the same crown graph have different numbers of completions. By contrast, all perfect matchings of \(K_{n,n}\) have the same completion count.

The unconditioned spanning-tree count and the probability of the event under a uniform random spanning tree are, respectively,
\[
\tau(\operatorname{Cr}_n)=(n-1)n^{n-2}(n-2)^{n-1},\qquad
\Pr(M_\sigma\subseteq T)=\frac{N_n(\sigma)}{(n-1)n^{n-2}(n-2)^{n-1}}.
\]

## Assumptions and scope
All graphs are finite, undirected, and unweighted. Parallel edges may arise during contraction and are counted distinctly when enumerating spanning trees. The forbidden perfect matching \(\{a_i b_i\}\) is fixed, and the given matching \(M_\sigma\) is any perfect matching among the remaining edges; hence \(\sigma\) is a derangement. The theorem covers **every** \(n\geq3\) and **every** such matching, not just one conjugacy class. The Chebyshev recurrence determines all quantities using integer arithmetic; the displayed rational expression is an integer by the spanning-tree interpretation.

## Proof
**Step 1: contraction.** Because \(M_\sigma\) is a forest, contracting all of its edges establishes a bijection between spanning trees of \(\operatorname{Cr}_n\) that contain \(M_\sigma\) and spanning trees of the loopless multigraph \(H_\sigma=\operatorname{Cr}_n/M_\sigma\). Label the contracted vertex \(i\) by the pair \(\{a_i,b_{\sigma(i)}\}\). Between distinct contracted vertices \(i\) and \(j\) there are precisely
\[
2-\mathbf 1_{\{\sigma(i)=j\}}-\mathbf 1_{\{\sigma(j)=i\}}
\]
parallel edges: one is possible from \(a_i\) to \(b_{\sigma(j)}\), and one from \(a_j\) to \(b_{\sigma(i)}\); either disappears exactly when it is one of the forbidden diagonal edges. In a \(2\)-cycle both are absent, which is why treating \(2\)-cycles as ordinary simple cycles would give an incorrect answer.

**Step 2: Laplacian decomposition.** Let \(P_\sigma\) be the permutation matrix with an entry \(1\) at \((i,\sigma(i))\). The adjacency matrix of the disjoint union of the directed permutation cycles viewed as undirected multigraphs is \(A_\sigma=P_\sigma+P_\sigma^{\mathsf T}\), with two parallel edges along a \(2\)-cycle. Each vertex has degree \(2\) in this multigraph. Consequently the Laplacian of \(H_\sigma\) is
\[
L_\sigma=2(n-1)I-2J+A_\sigma,
\]
where \(J\) is the all-ones matrix. On the subspace of vectors constant on each permutation cycle, \(A_\sigma\) acts as multiplication by \(2\). Thus \(L_\sigma\) has eigenvalue \(0\) once, along the global constant vector, and eigenvalue \(2n\) with multiplicity \(c-1\). On the \(\ell_j-1\) Fourier modes of nonzero frequency within a cycle of length \(\ell_j\), \(J\) vanishes and the Laplacian eigenvalues are
\[
2(n-1)+2\cos\left(\frac{2\pi h}{\ell_j}\right),\qquad 1\leq h<\ell_j.
\]
They are all strictly positive for \(n\geq3\), so \(H_\sigma\) is connected. The matrix-tree theorem gives
\[
N_n(\sigma)=\tau(H_\sigma)
=\frac{(2n)^{c-1}}{n}\prod_{j=1}^{c}\prod_{h=1}^{\ell_j-1}
\left(2(n-1)+2\cos\frac{2\pi h}{\ell_j}\right).
\]

**Step 3: Chebyshev identity.** The eigenvalues of \(P_\ell+P_\ell^{\mathsf T}\) on one cyclic block are \(2\cos(2\pi h/\ell)\) for \(0\leq h<\ell\). Their characteristic-polynomial identity is
\[
\prod_{h=0}^{\ell-1}\left(x+2\cos\frac{2\pi h}{\ell}\right)
=2\bigl(T_\ell(x/2)-(-1)^\ell\bigr).
\]
The zero-frequency factor is \(x+2\). Taking \(x=2(n-1)\) and removing this factor yields
\[
\prod_{h=1}^{\ell-1}\left(2(n-1)+2\cos\frac{2\pi h}{\ell}\right)
=\frac{T_\ell(n-1)-(-1)^\ell}{n}.
\]
Substituting into the matrix-tree expression and collecting powers of \(n\) gives precisely the theorem.

**Step 4: unconditioned count.** The Laplacian of \(\operatorname{Cr}_n\), ordered by its two sides, is
\[
\begin{pmatrix}(n-1)I&I-J\\I-J&(n-1)I\end{pmatrix}.
\]
On constant symmetric and antisymmetric vectors it has eigenvalues \(0\) and \(2(n-1)\), and on the remaining symmetric and antisymmetric subspaces it has eigenvalues \(n\) and \(n-2\), each with multiplicity \(n-1\). Dividing the product of the nonzero eigenvalues by \(2n\) establishes the stated formula for \(\tau(\operatorname{Cr}_n)\), and division gives the uniform-spanning-tree probability. This completes the proof.

## Verification
Execute `python3 verify.py` with Python \(3\) and no third-party dependencies. It independently constructs the contracted multigraph from the original bipartite edges, constructs a second quotient by subtracting the directed permutation arcs from the doubled complete graph, and calculates exact integer Laplacian cofactors using fraction-free elimination. All \(2{,}174\) derangements on \(3\leq n\leq7\) were tested, in all cycle types. For \(3\leq n\leq5\), all \(55\) derangements were also checked by exhaustive spanning-tree subset enumeration in the original graph. The exact comparisons included \(N_4((1\,2)(3\,4))=32\), \(N_4((1\,2\,3\,4))=36\), \(N_5((1\,2)(3\,4\,5))=588\), and \(N_5((1\,2\,3\,4\,5))=605\). Finite verification is supplementary; the argument above covers unbounded \(n\).

## Relationship to prior work
The matrix-tree theorem and matching contraction are standard. Gilbert and Myrvold (1997) analyze spanning-tree counts for simple nearly complete graphs whose complements consist of paths and cycles; the contracted graph here is instead a multigraph with edge multiplicities zero, one, or two, so the quoted simple-graph family is not the same counting instance, although the spectral methods are related. Their available abstract was inspected, but not their full text; possible implicit coverage by their more general methods remains a documented risk. Ge and Dong (2019/2020, arXiv:1904.07766) give the unconditioned spanning-tree count and effective resistances for \(K_{m,n}\) minus a matching, and show the count for spanning trees of **the complete bipartite graph** that include a fixed matching. Dong and Ge (2021/2022, arXiv:2103.05294) generalize fixed-forest inclusion to **complete** bipartite graphs. These results concern closely related quantities but do not state the cycle-type-dependent count for simultaneously including a perfect matching in the matching-deleted biclique. For example, the complete-bipartite formula gives the same value for every perfect matching, whereas the two \(n=4\) values here are unequal. Das, Cevik, and Cangul (2013) give general Laplacian-based spanning-tree bounds rather than fixed-matching enumeration. Standard matrix-tree machinery underlies the proof, but recognizing the quotient \(2K_n\) with cycle edges removed and evaluating its spectrum are the specialized steps.

## Limitations
The theorem addresses perfect matchings \(M_\sigma\), not arbitrary partial matchings or forests; it does not assert an ordering of the cycle types by completion count for general \(n\). It does not claim discovery of the matrix-tree theorem, general contraction bijections, the unconditioned crown-tree count, or complete-bipartite fixed-forest formulae. No independent external audit is implied. A residual literature risk is that an unindexed specialization, an unseen result in the full Gilbert–Myrvold article, or a more general multivariate tree formula may already present an equivalent explicit derangement-cycle product.

## References
1. K. C. Das, A. S. Cevik, and I. N. Cangul, “The number of spanning trees of a graph,” *Journal of Inequalities and Applications* **2013**, article 395, published online 2013-08-20. https://doi.org/10.1186/1029-242X-2013-395
2. J. Ge and F. Dong, “Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs,” *Discrete Applied Mathematics* **283** (2020), 542–554; arXiv version 1, 2019-04-16. https://arxiv.org/abs/1904.07766
3. F. Dong and J. Ge, “Counting spanning trees in a complete bipartite graph which contain a given spanning forest,” *Journal of Graph Theory* **101** (2022), 79–94; arXiv version 1, 2021-03-09. https://arxiv.org/abs/2103.05294
4. D. Li, W. Chen, and W. Yan, “Enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest,” *Journal of Graph Theory* **104** (2023), 160–170. https://doi.org/10.1002/jgt.22954
5. B. Gilbert and W. Myrvold, “Maximizing spanning trees in almost complete graphs,” *Networks* **30** (1997), 23–30. https://doi.org/10.1002/(SICI)1097-0037(199708)30:1%3C23::AID-NET3%3E3.0.CO;2-N
