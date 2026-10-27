# Exact tree-cut modulus of total-variation denoising and degree-three amplification

## Finding
Let \(T=(V,E)\) be a finite, simple, unweighted tree with \(|V|\ge2\). For \(x\in\mathbb R^V\), put
\[
J_T(x)=\sum_{\{u,v\}\in E}|x_u-x_v|,
\qquad
R_\lambda(y)=\operatorname*{argmin}_{x\in\mathbb R^V}
\left\{\tfrac12\|y-x\|_2^2+\lambda J_T(x)\right\},\quad\lambda>0.
\]
Define the sharp two-input variation modulus by
\[
K_T(\lambda)=\sup_{J_T(y-z)>0}\frac{J_T(R_\lambda(y)-R_\lambda(z))}{J_T(y-z)}.
\]
For every connected vertex set \(A\subseteq V\) with \(|A|\ge2\) and edge \(e\in E(T[A])\), write \(A_0,A_1\) for the two components of \(T[A]\setminus\{e\}\), and let
\[
t_i=\#\{\{u,v\}\in E:u\in A_i,\ v\in V\setminus A\}\quad(i=0,1).
\]
Then the exact, attained, and parameter-independent result is
\[
\boxed{K_T(\lambda)=\max\left\{1,\max_{A,e}
\frac{|A_1|t_0+|A_0|t_1}{|A_0|+|A_1|}\right\}.}
\]
In particular, every finite path has modulus \(1\). A star with \(n\ge1\) leaves has modulus \(\max\{1,(n-1)/2\}\). If \(C_m\) is the comb with \(m\ge3\) spine vertices, one leaf attached to each, and thus maximum degree three, then
\[
K_{C_m}(\lambda)\ge\frac{2\lfloor m^2/4\rfloor}{m},
\]
so this modulus is unbounded among maximum-degree-three trees.

## Assumptions and scope
All vertex masses and all edge-variation weights are one; the target and input signals are real. The number of vertices is finite and at least two, and \(\lambda\) is any positive real. The squared-data fidelity is Euclidean, while stability is measured in the **homogeneous graph-total-variation seminorm**, not in Euclidean or graph-Sobolev norm. The quotient excludes differences with zero graph variation. The minimizer exists and is unique by strict convexity; it commutes with addition of constant vectors.

## Proof
**1. Local affine pieces and their realization.** Orient the tree edges arbitrarily and let \(B\) be the edge–vertex incidence matrix, so \(J_T(x)=\|Bx\|_1\). The optimality condition for \(u=R_\lambda(y)\) is
\[
y-u=\lambda B^{\mathsf T}q,\quad q_e\in[-1,1],\quad
q_e=\operatorname{sign}((Bu)_e)\ \text{if }(Bu)_e\ne0.
\]
On a nondegenerate cell, the edges where \((Bu)_e=0\) form a forest \(F\) of fused edges; all other edge signs are fixed. If \(P_F\) orthogonally averages coordinates over the connected components of \((V,F)\), then minimizing on the corresponding equality subspace gives
\[
R_\lambda(y)=P_F\bigl(y-\lambda B_{E\setminus F}^{\mathsf T}s\bigr),
\]
where \(s\) is the fixed sign vector on unfused edges. Therefore its local linear part is \(P_F\). The polyhedral optimality conditions yield finitely many such affine pieces, and continuity gives the global Lipschitz upper bound by the maximum of their operator seminorms.

Conversely every choice of fused-edge forest \(F\subseteq E\) occurs on an open input cell. Choose \(u\) constant on every component of \((V,F)\), with unequal endpoint values on every edge outside \(F\). Put \(q_e=0\) on \(F\), and equal to the strict edge-difference sign elsewhere; then \(y=u+\lambda B^{\mathsf T}q\) has minimizer \(u\). All fused-edge dual constraints are strictly interior and all unfused differences remain nonzero. Small changes of \(y\) thus preserve the pattern and produce the affine derivative \(P_F\). (The dual corrections on \(F\) exist uniquely componentwise because each fused component is a tree.) In particular, every local operator norm is achieved by an actual pair of close inputs.

**2. Cut-step basis for tree variation.** Fix a root. For each edge \(e\), let \(h^e\) be the indicator of the component of \(T\setminus\{e\}\) not containing the root. The edge increments of the family \(\{h^e\}\) form a signed coordinate basis. Every signal has the decomposition
\[
x=c\mathbf1+\sum_{e\in E}d_eh^e,\qquad
J_T(x)=\sum_{e\in E}|d_e|,\quad J_T(h^e)=1.
\]
Each \(P_F\) fixes constants, so the triangle inequality and evaluation on the basis show
\[
\|P_F\|_{J_T\to J_T}=\max_{e\in E}J_T(P_Fh^e).
\]
If \(e\notin F\), each fused component lies wholly on one side of its cut, and therefore \(P_Fh^e=h^e\), giving value \(1\). If \(e\in F\), let \(A\) be the fused component containing \(e\). Removing \(e\) splits \(A\) into \(A_0,A_1\). With \(h^e\) equal to \(1\) on the side containing \(A_1\), its block average on \(A\) is \(|A_1|/|A|\); outside \(A\), the values stay zero or one. Only edges leaving \(A\) contribute, and their exact variation is
\[
J_T(P_Fh^e)=t_0\frac{|A_1|}{|A|}+t_1\frac{|A_0|}{|A|}.
\]
Every connected \(A\) can be made one fused block with all outside vertices left singleton. Maximizing these displayed quantities, together with the identity chamber, proves the formula and attainment.

**3. Structural consequences.** On a path, each side of any connected block has at most one edge leaving the block: \(t_0,t_1\le1\). Thus the inner fraction is at most \(1\). On a star with \(n\) leaves, every nontrivial fused block consists of the hub and \(k\) leaves. For a fused hub–leaf edge the cut formula is \((n-k)/(k+1)\), maximized at \(k=1\). This gives the star formula.

For the comb with spine vertices \(1,\ldots,m\) and one tooth per spine vertex, take the entire spine as \(A\) and cut its edge between positions \(k\) and \(k+1\). The component sizes and exterior-edge counts are both \(k,m-k\), so the cut value is \(2k(m-k)/m\). Choosing \(k\) closest to \(m/2\) proves the stated unbounded lower bound while the maximum graph degree remains three.

**4. One-input versus two-input variation.** The inequality \(J_T(R_\lambda(y))\le J_T(y)\) holds on every finite graph: if \(u=R_\lambda(y)\), the subgradient inequality with \((y-u)/\lambda\in\partial J_T(u)\) gives
\[
J_T(y)\ge J_T(u)+\lambda^{-1}\|y-u\|_2^2.
\]
Hence the two-input amplification on combs does not contradict ordinary variation reduction.

## Verification
Run `python3 CHECKER.py` from the extracted package. It uses only Python's standard library and exact rational arithmetic. It independently enumerates every fused-edge partition and every edge-cut step for all \(1,441\) labeled trees with two through six vertices, and compares the resulting exact norm with the connected-subtree formula. Additional exact regressions cover stars, paths, and combs; explicit pairwise KKT certificates attain factors \(3/2\) on the four-leaf star and \(2\) on the four-spine comb. The proof above, rather than those bounded finite checks, establishes the all-tree theorem.

## Relationship to prior work
Tibshirani and coauthors introduced fused penalties that favor adjacent equality and considered unordered-neighbor generalizations. Tibshirani and Taylor studied general graph fused lasso and proved that its solution is locally an affine projection in the **Euclidean data geometry** (their Section 10.1, Lemma 3). That affine-piece fact is a useful starting point, but it supplies neither the exact graph-variation operator norm nor its reduction to connected-subtree boundary counts. Kirisits, Scherzer, and Setterqvist established a universal convex minimality property for graph ROF denoising relative to a **single input's** admissible dual-translation set; the property does not compare the graph variation of outputs for two different inputs. The present theorem measures precisely that different two-input stability notion and identifies its branching-dependent amplification.

## Limitations
This result assumes simple finite trees, uniform edge variation and Euclidean vertex fidelity. The cut-step basis argument uses the absence of cycles; no claim is made for cyclic graphs, unequal masses or edge weights, general nonlinear data fidelities, or infinite trees. The exact comb **lower bound** is not asserted to equal its full sharp modulus. Unindexed prior work on graph-TV resolvents could contain an equivalent invariant; this is not an independence or publication certification.

## References
1. R. Tibshirani, M. Saunders, S. Rosset, J. Zhu, K. Knight, “Sparsity and smoothness via the fused lasso,” *JRSS B* 67 (2005), 91–108, DOI `10.1111/j.1467-9868.2005.00490.x`, first publicly dated 2004-12-13. Full author-hosted text: https://web.stanford.edu/group/SOL/papers/fused-lasso-JRSSB.pdf.
2. R. J. Tibshirani and J. Taylor, “The solution path of the generalized lasso,” *Annals of Statistics* 39 (2011), 1335–1371, arXiv:1005.1971 (first posted 2010-05-11). Full text: https://arxiv.org/abs/1005.1971.
3. C. Kirisits, O. Scherzer, E. Setterqvist, “Invariant \(\varphi\)-minimal sets and total variation denoising on graphs,” *SIAM Journal on Imaging Sciences* 12 (2019), 1643–1668, arXiv:1807.10514 (posted 2018-07-27). Full text: https://www.gs.jku.at/pubs/NFNreport74.pdf.
