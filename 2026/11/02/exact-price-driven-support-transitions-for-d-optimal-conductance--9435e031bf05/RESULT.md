# Exact price-driven support transitions for D-optimal conductances on cactus networks

## Finding

**Theorem (sharp cactus cost-allocation and support rule).** Let \(G=(V,E)\) be a finite connected simple cactus: every edge lies in at most one simple cycle. Put \(n=|V|\ge2\). Assign a positive price \(p_e>0\) to every edge, and fix \(B>0\). For independent conductances \(w_e\ge0\) subject to \(\sum_{e\in E}p_e w_e=B\), maximize the weighted spanning-tree enumerator
\[
\mathcal T_G(w)=\sum_{T\text{ spanning tree}}\prod_{e\in T}w_e
=\det L_{\widehat v,\widehat v}(w),
\]
where \(L_{\widehat v,\widehat v}\) is any grounded principal minor of the weighted Laplacian. A unique global maximizer exists, and the support and expenditure of every edge can be described exactly.

For each bridge \(e\), \(p_e w_e^*=B/(n-1)\). For each simple cycle \(C\) of length \(\ell\ge3\), its total optimized expenditure equals \(\sum_{e\in C}p_e w_e^*=(\ell-1)B/(n-1)\). These expenditures are independent of other prices, neighboring blocks and attachment positions.

A cycle has a zero-conductance edge if and only if there exists an edge \(k\in C\) satisfying the **sharp dominance inequality**
\[
p_k\ge\sum_{e\in C\setminus\{k\}}p_e.
\]
Such an edge is necessarily unique. In that case, \(w_k^*=0\) and, for every \(e\in C\setminus\{k\}\), \(w_e^*=B/((n-1)p_e)\). If no edge price dominates the sum of the remaining cycle prices, all optimized weights on that cycle are positive and uniquely solve
\[
\sum_{e\in C}p_e w_e=\frac{(\ell-1)B}{n-1},\qquad
\frac{1}{p_e}\left(\frac{1}{w_e}-\frac{w_e^{-2}}{\sum_{f\in C}w_f^{-1}}\right)=\frac{n-1}{B}\quad(e\in C).
\]
Consequently the optimal support is a spanning tree if and only if **every** cycle has a dominant-priced edge; otherwise every nondominant cycle remains intact in the support.

For a cycle of length \(\ell\ge3\) with \(\ell-1\) prices equal to one and one exceptional price \(\tau\), write \(D=(\ell-1)B/(n-1)\). If \(0<\tau<\ell-1\), the ordinary weights and exceptional weight are respectively
\[
a=\frac{(\ell-2)D}{(\ell-1)^2-\tau},\qquad
b=\frac{D(\ell-1-\tau)}{\tau((\ell-1)^2-\tau)}.
\]
At \(\tau\ge\ell-1\), \(a=D/(\ell-1)\) and \(b=0\), so the exceptional weight vanishes linearly on approach to the threshold from below.

## Assumptions and scope

Graphs are finite, undirected, loopless and **simple**. Distinct cycles share at most one vertex and never an edge. All edge prices are strictly positive, the budget is strictly positive, and zero conductances are allowed. This is **continuous conductance allocation**, not a combinatorial problem selecting a fixed count of edges or maximizing a Kirchhoff *resistance* sum. The optimization includes every individual edge as an independent variable and imposes no within-block symmetry. The logarithm of the objective is considered only on the feasible designs with positive spanning-tree enumerator. The one-vertex graph is excluded.

## Proof

**1. Factorization.** In any cactus, every spanning tree contains all bridges and deletes exactly one edge from each cycle. The cycles have edge-disjoint supports, hence for all nonnegative weights
\[
\mathcal T_G(w)=\prod_{e\text{ bridge}}w_e
\prod_{C\text{ cycle}}\left(\sum_{k\in C}\prod_{e\in C\setminus\{k\}}w_e\right).
\]
Every bridge factor has homogeneity degree one, and each length-\(\ell\) cycle factor has degree \(\ell-1\). The sum of these degrees is \(n-1\), because a connected cactus has exactly one independent edge for each bridge and \(\ell-1\) for each cycle.

**2. Uniqueness.** An equal-small-positive-weight feasible vector has positive tree enumerator, so a maximizer is connected in its positive support. On this domain its grounded Laplacian is positive definite. The map from conductances on a simple graph to this grounded matrix is injective: off-diagonal entries recover edges between ungrounded vertices, and remaining diagonal entries recover incident edges to the grounded vertex. Strict concavity of \(\log\det\) on positive-definite matrices therefore gives strict concavity in the edge weights. Compactness of the budget simplex and continuity establish existence, and strict concavity establishes a single global optimum.

**3. Block budget law.** For an individual block factor of degree \(d_H\), maximizing its value with a fixed expenditure \(B_H\) yields \(B_H^{d_H}\) times a price-dependent positive constant. Thus the remaining problem maximizes \(\sum_H d_H\log B_H\) subject to \(\sum_H B_H=B\). Strict concavity or Lagrange multipliers give \(B_H=d_H B/(n-1)\). This applies equally to bridges and cycles. An optimized bridge necessarily has \(w_e=B/((n-1)p_e)\).

**4. Sharp support rule for a cycle.** A length-\(\ell\) cycle can have at most one zero edge if its tree enumerator is positive. Fix an edge \(k\) to be zero, and a positive cycle budget \(D\). On this face the cycle polynomial is \(\prod_{e\ne k}w_e\). Maximizing its logarithm under \(\sum_{e\ne k}p_e w_e=D\) yields the unique face optimizer \(p_e w_e=D/(\ell-1)\) for every surviving edge and face multiplier \(\mu=(\ell-1)/D\). At this face, differentiating \(\log\mathcal T_C\) into the previously absent coordinate gives \(\partial_{w_k}\log\mathcal T_C=\sum_{e\ne k}1/w_e=((\ell-1)/D)\sum_{e\ne k}p_e\). The boundary Karush–Kuhn–Tucker condition is exactly \(\partial_{w_k}\log\mathcal T_C\le\mu p_k\), equivalently \(\sum_{e\ne k}p_e\le p_k\). By concavity this condition is sufficient for a global cycle optimum, and by strict concavity that optimum is unique. Conversely if no edge meets it, none of the possible boundary faces can contain an optimum; the optimum therefore has all positive entries.

For a positive cycle, the identity \(\mathcal T_C=(\prod_e w_e)(\sum_e w_e^{-1})\) gives \(\partial_{w_e}\log\mathcal T_C=w_e^{-1}-w_e^{-2}/\sum_f w_f^{-1}\). Under the optimum's cycle budget \(D=(\ell-1)B/(n-1)\), homogeneity forces the Lagrange multiplier \((\ell-1)/D=(n-1)/B\). This proves the displayed interior system and its unique solution, while also proving that a cycle cannot have two zero edges. Two distinct positive prices cannot simultaneously exceed the sum of the other positive prices, so the dominant index is unique.

**5. One-exception closed form.** For \(\ell-1=k\ge2\) ordinary edges, permutation invariance plus uniqueness forces a common ordinary weight \(a\). Denote exceptional weight \(b\). The cycle objective is \(a^{k-1}(a+kb)\) and budget is \(ka+\tau b=D\). For \(\tau<k\), differentiating the resulting one-variable polynomial on the positive interval yields \(a=(k-1)D/(k^2-\tau)\) and \(b=D(k-\tau)/(\tau(k^2-\tau))\); both are positive. For \(\tau\ge k\), step 4 gives \(b=0\) and \(a=D/k\). These formulae agree at equality, and the exceptional weight approaches zero linearly as \(\tau\uparrow k\). This completes the proof.

## Verification

The accompanying `verify.py` independently computes grounded Laplacian determinants using exact rational Gaussian elimination and checks the cycle-block factorization on 28 heterogeneous 12-vertex instances. It checks the single-price sharp threshold and formulas in 36 exact-rational cycle instances, and compares 50 heterogeneous cactus solutions (including equality and near-threshold price profiles) with 900 asymmetric feasible perturbations. All reported tests pass. These checks supplement, rather than establish, the arbitrary-size theorem.

An exact worked case consists of a triangle (prices \((1,1,3)\)), a bridge (price \(4\)), and a quadrilateral (prices \((1,1,1,2)\)), joined at one vertex on each cycle. With total budget \(6\) and \(n=7\), the optimal triangle weights are \((1,1,0)\), the bridge weight is \(1/4\), and the quadrilateral weights are \((6/7,6/7,6/7,3/14)\). The resulting exact weighted spanning-tree enumerator equals \(27/98\), verified directly from the grounded determinant.

Reproduce with `python verify.py` using Python 3, NumPy and SciPy; no external data files are required.

## Relationship to prior work

The weighted Matrix–Tree identity and concavity of log determinant are classical. Boyd (2006) explains spectral graph optimization through convex design. Sagnol and Harman (arXiv:1307.4953, first posted July 18, 2013) develop general second-order-cone and exact D-optimal-design formulations; their block-design discussion connects information determinants with spanning trees. Khosoussi et al. (arXiv:1604.01116, first posted April 5, 2016) address weighted spanning-tree maximization for **combinatorial edge-selection constraints**, developing log-submodularity and convex relaxations. Their full text treats fixed-weight candidate edges and bounded selection variables, not this arbitrary positive heterogeneous per-conductance price simplex. No equivalent cactus-specific support/budget theorem was located among the examined sources. The novelty assessment is relative to this bounded literature inspection, not a declaration of exhaustive priority.

## Limitations

The factorized budget law depends on the cactus restriction and does not apply verbatim to overlapping cycles. Only linear positive conductance prices and total budget are covered; upper/lower conductance constraints, other objectives, and integer edge-selection models are not classified. Interior cycle weights are uniquely specified by equations but not given as closed radicals for arbitrary price lists. The implementation uses floating-point optimization for numerical interior solutions; rigorous uniqueness and support follow from the analytical argument, not solver outputs. A different historical source may contain these special-case formulas; a full exhaustive bibliographic search and independent validation have not been performed.

## References

1. Kirchhoff's Matrix–Tree Theorem (classical result on Laplacian cofactors).
2. S. Boyd, “Convex Optimization of Graph Laplacian Eigenvalues,” International Congress of Mathematicians, 2006, https://web.stanford.edu/~boyd/papers/laplacian_opt.html .
3. G. Sagnol and R. Harman, “Computing exact D-optimal designs by mixed integer second-order cone programming,” arXiv:1307.4953, first version July 18, 2013, https://arxiv.org/abs/1307.4953 .
4. K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, “Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs,” arXiv:1604.01116, first version April 5, 2016, https://arxiv.org/abs/1604.01116 .
