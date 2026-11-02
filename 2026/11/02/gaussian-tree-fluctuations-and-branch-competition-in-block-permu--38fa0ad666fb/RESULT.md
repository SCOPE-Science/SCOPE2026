# Gaussian-tree fluctuations and branch competition in block-permuton search trees

## Finding

Fix an integer \(k\ge2\), a permutation \(\rho\in S_k\), and positive masses \(p_i\) with \(\sum_{i=1}^k p_i=1\). A block-permutation permuton, defined precisely below, generates a random binary search tree \(T_n\). Let \(H_n\) be its height counted in edges. Let \(T(\rho)\) be the external BST on \(k\) keys, let \(h\) be its height, and let \(\mathcal D\) be all vertices of external depth \(h\). Put independent \(N(0,1)\) labels \(Z_e\) on its directed edges, and write \(G_v=\sum_{e\in P(v)}Z_e\) along the root-to-vertex path. Let \(c_*\) be the uniform-BST constant, the larger solution of \(c\log(2e/c)=1\), approximately \(4.31107\).

Then, as \(n\to\infty\),
\[
\frac{H_n-(c_*+h)\log n}{\sqrt{\log n}}
\Longrightarrow M_\rho:=\max_{v\in\mathcal D}G_v.
\]
The Gaussian field has \(\operatorname{Cov}(G_u,G_v)=\operatorname{depth}(\operatorname{LCA}(u,v))\). In particular it is not a collection of independent Gaussian values except in special shapes.

This convergence also holds in first moment:
\[
\mathbb EH_n=(c_*+h)\log n+\mu_\rho\sqrt{\log n}+o(\sqrt{\log n}),
\qquad \mu_\rho=\mathbb EM_\rho.
\]
Exactly one deepest external vertex gives \(\mu_\rho=0\); at least two deepest vertices give \(\mu_\rho>0\). This precisely characterizes when a positive square-root-logarithmic mean-height correction arises from competition between deepest branches.

For \(k=3\), the balanced external trees, \(\rho=213\) or \(231\), have \(h=1\) and \(M_\rho=\max(Z_1,Z_2)\) for independent standard normals, so their limit CDF is \(\Phi(t)^2\) and \(\mu_\rho=1/\sqrt\pi\). The other four external permutations have a unique vertex at depth \(2\), giving \(M_\rho\sim N(0,2)\) and \(\mu_\rho=0\). For a uniformly random independent external \(\rho\in S_3\), with the centering using its observed external height, the limit CDF is
\[
\frac13\Phi(t)^2+\frac23\Phi(t/\sqrt2).
\]

## Assumptions and scope

Partition the \(x\)-axis into consecutively ordered intervals \(I_1,\ldots,I_k\) of lengths \(p_1,\ldots,p_k\). Partition the \(y\)-axis into consecutively ordered intervals \(J_1,\ldots,J_k\), with \(J_{\rho(i)}\) having length \(p_i\). Define a probability measure \(\mu\) with density \(1/p_i\) on each rectangle \(I_i\times J_{\rho(i)}\) and density zero elsewhere. Each coordinate marginal is uniform on \([0,1]\). Draw \(n\) independent \((X,Y)\) pairs with this law, order the points by increasing \(X\), and insert their \(Y\)-coordinates consecutively into an ordinary unbalanced binary search tree. Coordinates are almost surely distinct. Height is the largest root-to-node graph distance (a singleton has height zero).

The number of points in each rectangle, \(N_i\), is multinomial with \(N_i/n\to p_i\) in probability, and conditional on these counts the induced permutation within every block is uniform and independent across blocks. The external BST shape is the BST of \(\rho\) on the event all blocks are occupied; that event has probability tending to one exponentially quickly. All logarithms are natural.

## Proof

**1. Exact grafting decomposition.** For any positive block sizes and any independent within-block permutations, first build the external BST of \(\rho\). A child block is grafted to the extreme key of its parent block on the side prescribed by their order: via the parent's leftmost search path for a left child, and rightmost path for a right child. Write \(A_i\) and \(B_i\) for the numbers of edges in the leftmost and rightmost paths of the BST internal to block \(i\), and \(K_i\) for its height. For each external vertex \(v\), define
\[
D_v=\sum_{(u,w)\in P(v)}(1+E_{u,w}),\quad
E_{u,w}=\begin{cases}A_u,&w<u,\\B_u,&w>u.\end{cases}
\]
Here the external labels are values \(1,\ldots,k\); every path is taken in \(T(\rho)\). The maximum depth in block \(v\) is exactly \(D_v+K_v\), hence
\[
H_n=\max_{v\in T(\rho)}(D_v+K_v).
\]
This is a deterministic identity, including unequal positive block sizes. A direct argument follows by inserting the blocks in their \(X\)-order and observing that comparisons with every key of a previously inserted block all have the same sign until that block's extreme key is reached. The same decomposition is stated for block BSTs in Peca-Medlin--Zhong, Section 2, Lemma 1 and Corollary 2; it is acknowledged, not claimed as new.

**2. Joint extreme-path limit.** Let \(A_m,B_m\) denote the two extreme path lengths in a BST from a uniform permutation on \(m\) elements. The rightmost path visits successive left-to-right maxima; the leftmost visits successive left-to-right minima. In a uniform permutation the relative rank \(R_j\) of entry \(j\) among the first \(j\) entries is independently uniform on \(\{1,\ldots,j\}\). Therefore
\[
A_m=\sum_{j=2}^{m}\mathbf1\{R_j=1\},\qquad
B_m=\sum_{j=2}^{m}\mathbf1\{R_j=j\}.
\]
The excluded first entry is the root, not an edge. For \(j\ge2\), these events are disjoint with probability \(1/j\) each, and the pairs across distinct \(j\)'s are independent. In particular,
\[
\begin{aligned}
\mathbb EA_m&=\mathbb EB_m=H_m^{(1)}-1=\log m+O(1),\\
\operatorname{Var}(A_m)&=\operatorname{Var}(B_m)=H_m^{(1)}-H_m^{(2)}=\log m+O(1),\\
\operatorname{Cov}(A_m,B_m)&=1-H_m^{(2)}=O(1),
\end{aligned}
\]
where \(H_m^{(r)}=\sum_{j=1}^{m}j^{-r}\). Multivariate Lindeberg--Feller (bounded independent summands) gives
\[
\left(\frac{A_m-\log m}{\sqrt{\log m}},\frac{B_m-\log m}{\sqrt{\log m}}\right)
\Longrightarrow (Z_-,Z_+)
\]
with independent standard normals. Different internal blocks are independent conditional on their counts. Because each \(N_i/n\to p_i>0\), the random block sizes do not alter this joint limit if \(\log N_i\) and \(\sqrt{\log N_i}\) are replaced by \(\log n\) and \(\sqrt{\log n}\). One may condition on the multinomial vector and use its concentration; the requisite limits are uniform along every sequence of block sizes proportional to \(n\).

**3. Internal heights have negligible fluctuations at this scale.** Reed's height theorem for a uniform BST of \(m\) nodes gives \(\mathbb EK_m=c_*\log m-\beta\log\log m+O(1)\), with a fixed \(\beta>0\), and \(\operatorname{Var}(K_m)=O(1)\). Consequently, for each block,
\[
\frac{K_i-c_*\log n}{\sqrt{\log n}}\longrightarrow0
\]
in probability; in fact the convergence is in \(L^2\). To deal with random block sizes, first restrict to the exponentially likely event on which each \(N_i\) lies in a fixed positive proportion interval around \(p_i n\); outside it the deterministic bound \(0\le K_i\le n\) suffices.

**4. Gaussian edge field and maximum.** For every fixed external edge \((u,w)\), the corresponding normalized graft-path length converges to a standard normal after subtracting \(\log n\). The vector over all edges converges jointly to independent standard normals. Distinct parents use independent internal blocks; the only within-parent pair is its left/right extrema, whose asymptotic independence was proved in step 2. For a vertex \(v\) of external depth \(d_v\), the deterministic decomposition and step 3 now give jointly over finitely many vertices
\[
D_v+K_v=(c_*+d_v)\log n+\sqrt{\log n}\,G_{v,n}+o_{\mathbb P}(\sqrt{\log n}),
\]
where \((G_{v,n})\) converges to the Gaussian sums \((G_v)\). Every vertex with \(d_v<h\) has a negative gap of at least \(\log n\) relative to the leading height, dominating square-root-logarithmic fluctuations. The maximum therefore reduces to \(\mathcal D\), and the continuous mapping theorem yields the displayed distributional limit.

**5. Expected height and positive correction.** The record-path centered squares have expectation \(O(\log n)\), and the centered internal-height squares have expectation \(O((\log\log n)^2+1)\). Since there are only finitely many blocks and edges, the centered normalized maximum has bounded second moment, including the exponentially small event that a block is empty. Thus the family is uniformly integrable and convergence holds in first moment, proving the claimed mean expansion. If \(\mathcal D\) is a singleton, its Gaussian path sum has mean zero. If \(\mathcal D\) has two distinct vertices \(u,v\), the Gaussian difference \(G_u-G_v\) has positive variance (their paths diverge), and
\[
\mathbb E\max(G_u,G_v)=\frac12\mathbb E|G_u-G_v|>0.
\]
The maximum over all deepest vertices has at least this mean. For three blocks in the balanced shape, \(G_u,G_v\) are independent \(N(0,1)\), hence the mean of their maximum is \(1/\sqrt\pi\); in skew shapes the unique deepest vertex has a path of two independent Gaussian edges and law \(N(0,2)\). This completes all assertions.

## Verification

The accompanying standalone `verify_block_bst.py` checks the grafting height identity against a completely separate node-by-node BST insertion routine in every one of 84,294 equal-size three-block instances up to block size four, and a further 720 unequal-size cases, including four-block external shapes. It also enumerates all uniform permutations of sizes two through eight to verify 14 exact extreme-record mean/covariance formulas. There are 85,028 assertions. Run with `python3 verify_block_bst.py`; no nonstandard packages are required. Finite checks corroborate only finite identities. The Gaussian limit and expectation correction follow analytically from the independent-relative-rank CLT, the published uniform-BST height estimates, and the exact grafting identity.

## Relationship to prior work

Corsini, Dubach and Féray introduced the permuton-sampled BST framework and gave first-order height results under regularity assumptions in arXiv:2403.03151, first posted March 5, 2024. Block-permutation permutons fall outside the positivity hypotheses of its universal-height result. Peca-Medlin and Zhong (arXiv:2507.04505, first posted July 6, 2025) supply the exact block-tree grafting identity and the first-order limit \((c_*+h)\log n\) for fixed-size outer blocks. Those ingredients are prior work. Reed (2003) established the required quantitative uniform-BST height estimates. The contribution here is the fixed-external-shape Gaussian edge-field limit for randomly sized permuton blocks, the sharp classification of a positive square-root-logarithmic expectation correction, and the explicit non-Gaussian balanced-versus-Gaussian skew three-block crossover. No claim is made to the first-order height constants, the grafting identity, or the classical record/rank CLT.

## Limitations

The number of rectangles \(k\), the external order \(\rho\), and all positive block masses are fixed as \(n\) grows. Results do not cover vanishing block masses, growing numbers of blocks, general permutons without a finite block structure, or rates of weak convergence. The result depends on Reed's published uniform-BST second-order height estimates. A prior unpublished or differently formulated derivation of the same Gaussian-tree fluctuation theorem cannot be ruled out; independent validation has not been performed.

## References

- B. Corsini, V. Dubach and V. Féray, *Binary search trees of permuton samples*, arXiv:2403.03151, first posted 2024-03-05. https://arxiv.org/abs/2403.03151
- J. Peca-Medlin and C. Zhong, *Heights of butterfly trees*, arXiv:2507.04505, first posted 2025-07-06, especially Section 2. https://arxiv.org/abs/2507.04505
- B. Reed, *The height of a random binary search tree*, J. ACM 50 (2003), 306--332, DOI:10.1145/765568.765571. https://doi.org/10.1145/765568.765571
