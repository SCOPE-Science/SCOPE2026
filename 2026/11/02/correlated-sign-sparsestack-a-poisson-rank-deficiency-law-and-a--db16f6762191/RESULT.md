# Correlated-sign SparseStack: a Poisson rank-deficiency law and a sharp half-density transition

## Finding
For a two-block, one-hash-per-block SparseStack matrix with independent hashes but correlated Rademacher signs, the *entire* asymptotic column-nullity distribution is Poisson in the subcritical column-density regime. If there are \(r\) rows per block, \(m=\lfloor cr\rfloor\) columns, and within-column sign correlation \(\rho\in[-1,1]\), then for every fixed \(0<c<1\),
\[
 m-\operatorname{rank}(S_r)\ \xrightarrow{d}\ \operatorname{Poisson}(\lambda(c,\rho)),\qquad
 \lambda(c,\rho)=-\tfrac14\log(1-c^2)-\tfrac14\log(1-\rho^2c^2).
\]
Thus the probability of injectivity of this sketch on the specified coordinate subspace has the exact limit
\[
 \lim_{r\to\infty}\Pr\{\operatorname{rank}(S_r)=m\}=[(1-c^2)(1-\rho^2c^2)]^{1/4}.
\]
For each fixed \(c\ge1\), column nullity tends to infinity in probability. The special cases \(\rho=0\) and \(|\rho|=1\) have limiting full-column-rank probabilities \((1-c^2)^{1/4}\) and \((1-c^2)^{1/2}\), respectively. This is a statement about rank, not an assertion of a norm-preserving subspace embedding.

## Assumptions and scope
Fix \(c>0\) and \(\rho\in[-1,1]\), and let \(r\) tend through the positive integers. Construct \(S_r\in\mathbb R^{2r\times m}\), with \(m=\lfloor cr\rfloor\), as follows. For each column \(j\), independently choose row locations \(U_j,V_j\) uniformly from \(\{1,\ldots,r\}\); choose an independent fair sign \(\xi_j\) and an independent sign \(\sigma_j\) with \(\Pr(\sigma_j=1)=(1+\rho)/2\). The only two nonzero entries of column \(j\) are \(\xi_j/\sqrt 2\) in row \(U_j\) of block one and \(\xi_j\sigma_j/\sqrt2\) in row \(V_j\) of block two. Choices for different columns are independent. Consequently the two block signs have correlation \(\rho\); at \(\rho=0\) they are independent, and at \(|\rho|=1\) they are reused up to a deterministic flip. Parallel edges (colliding location pairs) are retained as separate columns.

This model is precisely the restriction of a two-block hashed sketch to any fixed coordinate subspace of dimension \(m\), up to irrelevant extra all-zero columns outside that subspace. The domain is real arithmetic and column rank, with no norm distortion guarantee.

## Proof
**1. Exact finite-graph nullity formula.** Multiplying each column by \(\sqrt2\xi_j\) preserves rank. Interpret column \(j\) as the signed incidence vector \(e_{U_j}+\sigma_je_{r+V_j}\) of an edge of a labeled bipartite multigraph with \(r\) vertices in each part. For any connected component \(C\) with \(v_C\) vertices and \(e_C\) edges, the equations in the *left* nullspace are \(y_u+\sigma_e y_v=0\) for every edge \(e=uv\). Values propagate from any root; the solution space has dimension one if all cycle-sign products are \(+1\), and zero otherwise. Call the former components **balanced**; trees and isolated vertices are automatically balanced. By rank-nullity applied to the component incidence matrix, the column-nullity contribution is \(e_C-v_C+1\) for a balanced component and \(e_C-v_C\) otherwise. Hence the exact identity
\[
 D_r:=m-\operatorname{rank}(S_r)=\sum_C\bigl(e_C-v_C+\mathbf1_{\{C\text{ balanced}\}}\bigr).
\]
Every summand is nonnegative (an unbalanced component necessarily contains a cycle). On a tree, the summand is zero; on a unicyclic component it is one precisely when its unique cycle is balanced.

**2. Sparse bipartite multigraph cycles.** Fix \(0<c<1\). For every fixed \(L\), the numbers \(C_{2\ell,r}\) of edge-labeled simple cycles of length \(2\ell\), with \(\ell=1,\ldots,L\) and a parallel-edge pair counted as a length-two cycle, converge jointly to independent Poisson variables with means \(c^{2\ell}/(2\ell)\). Indeed, for each \(\ell\) the *exact* expected cycle count is
\[
 \mathbb EC_{2\ell,r}=\frac{(r)_\ell^2(m)_{2\ell}}{2\ell\,r^{4\ell}},
\]
where \((x)_k=x(x-1)\cdots(x-k+1)\). The joint factorial moments of finitely many vertex-disjoint cycles converge to products of these means; overlapping distinct cycles have an underlying graph with more edges than vertices and contribute \(O(1/r)\). This proves the independent Poisson limits by the factorial-moment method, including edge-labeled parallel pairs.

For this fixed \(c<1\), with probability tending to one no connected component contains two cycles. For completeness, one may bound the expected count of minimal connected double-cycle subgraphs (two cycles sharing vertices/edges or joined by a path) by enumerating their subdivisions: a double-cycle kernel has a bounded number of branching vertices, and for a subgraph with \(e\) labeled edges and \(v=e-1\) vertices its placement-and-edge-occurrence bound is \(O(r^v)(m)_e/r^{2e}=O_c(r^{-1}c^e)\), up to a polynomial factor in \(e\). Summing the finitely many kernel families over \(e\ge2\) yields \(O_c(1/r)\). Similarly the cycle-count tail obeys
\[
 \limsup_{r\to\infty}\sum_{\ell>L}\mathbb EC_{2\ell,r}\le\sum_{\ell>L}\frac{c^{2\ell}}{2\ell}\longrightarrow0.
\]
This follows directly from \((r)_\ell\le r^\ell\) and \((m)_{2\ell}\le m^{2\ell}\), noting that terms with \(2\ell>m\) vanish and \(m/r\le c\). These bounds justify transferring the finite cycle-count limits to the total unicyclic counts.

**3. Sign thinning and limiting law.** On a cycle of length \(2\ell\) the product of the independent relative signs \(\sigma_j\) is positive with probability
\[
 q_{2\ell}=\tfrac12(1+\rho^{2\ell}).
\]
Disjoint cycles use disjoint edge signs. As double-cycle components vanish asymptotically, independent thinning of the Poisson cycle counts yields independent balanced-cycle counts with respective means \(c^{2\ell}(1+\rho^{2\ell})/(4\ell)\). Step 1 shows that their sum is exactly \(D_r\) with probability tending to one. The convergent sum of means is
\[
 \lambda(c,\rho)=\sum_{\ell\ge1}\frac{c^{2\ell}(1+\rho^{2\ell})}{4\ell}=-\frac14\log(1-c^2)-\frac14\log(1-\rho^2c^2).
\]
Poisson summation proves the full nullity distribution and the full-rank probability, including the endpoint sign correlations.

**4. The threshold.** For every fixed \(c\ge1\), every \(0<c_0<1\), and all sufficiently large \(r\), the first \(\lfloor c_0r\rfloor\) columns of \(S_r\) are distributed as the subcritical model and are a submatrix. Column nullity cannot decrease on appending columns, so for every nonnegative integer \(K\),
\[
 \limsup_{r\to\infty}\Pr(D_r\le K)\le\Pr\{\operatorname{Poisson}(\lambda(c_0,\rho))\le K\}.
\]
Sending \(c_0\uparrow1\) sends \(\lambda(c_0,\rho)\) to infinity, hence the right-hand side to zero. Thus \(D_r\to\infty\) in probability for every \(c\ge1\). This includes the critical case \(c=1\); no supercritical giant-component assumptions are needed.

## Verification
The accompanying standard numerical verifier exhaustively compares graph-derived nullity to explicit real-matrix rank in 5,018 small instances, independently enumerates the exact two-column singularity probability \(1/(2r^2)\) for \(1\le r\le5\), and simulates 40,000 further sketches across two densities, four within-column sign correlations, and two sketch sizes, comparing empirical full-rank probabilities and nullity means with the formulas. It checks only finite examples; the distributional and threshold assertions follow from the proof above. Run `python verify_sparse_stack.py` with NumPy installed (the numerical seed is fixed).

## Relationship to prior work
Jeendgar, Flint, and Anzt introduce and evaluate the low-precision, multi-block SparseStack construction (arXiv:2606.20195, first publicly posted June 18, 2026). The independently signed case \(\rho=0\) matches its two-block random-sign setup. The correlated-sign variant is defined here, not attributed to that article. Heidary (arXiv:2609.02978) proves general oblivious-subspace embedding bounds for SparseStack, whereas this result concerns exact rank deficiency for the specific two-block coordinate-subspace case; neither claim implies the other without an additional singularity analysis. Sparse JL/OSNAP work supplies related stacked-hash models and embedding estimates. The signed-graph incidence rank rule and sparse-graph Poisson cycle limits are classical ingredients; novelty is **not** claimed for either ingredient individually. The specific correlation-resolved Poisson law, full-rank limit, and critical transition are the claim investigated here.

## Limitations
The law is for fixed density and fixed sign correlation as the block size grows, not for a varying near-critical window. Rank injectivity is necessary but not sufficient for norm preservation or small conditioning. The formulas do not cover higher block counts, nonuniform hashes, finite-precision rounding, or an arbitrary dense subspace. The original source's fully accessible PDF was unavailable during this comparison, and older signed sparse-matrix literature could contain an equivalent specialization. The result has undergone self-review only, not independent validation.

## References
- A. Jeendgar, C. Flint, H. Anzt, *Randomized Sketching is Robust to Low-Precision Rounding on GPUs*, arXiv:2606.20195 (first posted 2026-06-18).
- D. Heidary, *SparseStack Is an Optimal Oblivious Subspace Embedding*, arXiv:2609.02978 (2026).
- M. Cohen, T. S. Jayram, J. Nelson, *Simple Analyses of the Sparse Johnson–Lindenstrauss Transform*, SOSA (2018).
- J. Nelson, H. L. Nguyen, *OSNAP: Faster Numerical Linear Algebra Algorithms via Sparser Subspace Embeddings*, arXiv:1211.1002.
- A. Coja-Oghlan and collaborators, *The Full Rank Condition for Sparse Random Matrices*, APPROX/RANDOM (2023), covering a different minimum-degree regime.
