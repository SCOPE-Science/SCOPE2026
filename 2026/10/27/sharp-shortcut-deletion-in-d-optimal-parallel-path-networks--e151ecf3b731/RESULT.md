# Sharp shortcut deletion in D-optimal parallel-path networks

## Finding
Let two distinct terminal vertices be joined by one direct edge and by \(m\ge 1\) pairwise internally vertex-disjoint simple paths of integer lengths \(\ell_1,\ldots,\ell_m\ge 2\). Each edge independently receives a nonnegative conductance, with total conductance exactly \(B>0\). Maximize the weighted spanning-tree enumerator \(\tau\), equivalently the determinant of any reduced weighted Laplacian.

Set
\[
\rho=1+\sum_{i=1}^{m}(\ell_i-1),\qquad S=\sum_{i=1}^{m}\frac{1}{\ell_i+1}.
\]
There is **exactly one global maximizing edge allocation**. Every edge on a given long path has the same strictly positive optimal conductance \(w_i^\star\). Denote the direct-edge conductance by \(a^\star\). It vanishes **if and only if** \(S\ge 1\).

If \(S\le 1\), including the threshold, the exact solution is
\[
a^\star=\frac{B(1-S)}{\rho},\qquad
w_i^\star=\frac{B\ell_i}{\rho(\ell_i+1)}\quad(1\le i\le m).
\]
If \(S>1\), set \(a^\star=0\), and let \(\xi>1\) be the unique real root of
\[
\sum_{i=1}^{m}\frac{\ell_i-1}{\xi\ell_i^2-1}=1.
\]
Then
\[
w_i^\star=\frac{B(\ell_i-1)\xi\ell_i}{\rho(\xi\ell_i^2-1)}\quad(1\le i\le m).
\]
In either regime, the exact optimum is
\[
\tau^\star=\left(\prod_{i=1}^m \ell_i(w_i^\star)^{\ell_i-1}\right)
\left(a^\star+\sum_{i=1}^m\frac{w_i^\star}{\ell_i}\right).
\]
The second factor is \(B/\rho\) when \(S\le1\), and \(B\xi/\rho\) when \(S>1\).

## Assumptions and scope
The network is finite, undirected, and simple: the only shared vertices of the \(m\) long paths are their two terminals, the direct edge is distinct from all long-path edges, and \(\ell_i\ge2\). The budget charges one unit per unit conductance on **each individual edge**, not per physical path or unit of length. Conductances may be zero, but disconnected designs have \(\tau=0\). Let \(L(w)\) be the weighted combinatorial Laplacian and \(L^{(v)}(w)\) its principal minor obtained by deleting one row and the corresponding column. The objective is
\[
\tau(w)=\sum_{T\text{ a spanning tree}}\prod_{e\in T}w_e=\det L^{(v)}(w).
\]
The conclusion concerns optimal allocation for this determinant criterion, not the minimum-spanning-tree edge-weight sum or the Kirchhoff index.

## Proof
**1. The path polynomial.** For each long path \(P_i\), let \(U_i\) be the product of all its edge conductances, and let \(V_i\) be the sum of products obtained by omitting exactly one of its edges. Any spanning tree either includes the direct edge and omits one edge from *every* long path, or omits the direct edge and keeps exactly one entire long path while omitting one edge from every other path. Consequently, with direct-edge weight \(a\),
\[
\tau=a\prod_{i=1}^m V_i+
\sum_{i=1}^m U_i\prod_{j\ne i}V_j.
\]
This is a polynomial identity valid even when some conductances vanish. It is invariant under arbitrary permutations of the edge conductances **within** each long path, although those permutations need not be graph automorphisms.

**2. Unique maximizer and equalization.** A uniform positive allocation has \(\tau>0\), so a global maximizer on the compact budget simplex has \(\tau>0\). For such weights, \(L^{(v)}(w)\) is positive definite. The map from individual edge conductances to \(L^{(v)}(w)\) is injective for a simple graph: nonroot-edge weights can be read from the off-diagonal entries, then root-edge weights from the diagonal entries. Since \(\log\det\) is strictly concave on positive-definite matrices, \(\log\tau(w)\) is strictly concave on its convex positive-determinant domain. Thus the global optimizer is unique. Permuting weights within a long path preserves both budget and \(\tau\); uniqueness forces all its weights to agree. Those common weights are strictly positive, since setting them all to zero disconnects the path's internal vertices. Let their common values be \(w_i>0\). Now \(U_i=w_i^{\ell_i}\) and \(V_i=\ell_i w_i^{\ell_i-1}\), giving
\[
\tau=\left(\prod_i\ell_i w_i^{\ell_i-1}\right)
\left(a+\sum_i\frac{w_i}{\ell_i}\right).
\]

**3. Normalization.** Define \(x_0=a/B\), \(x_i=\ell_i w_i/B\), \(d_i=\ell_i-1\), and \(c_i=\ell_i^{-2}\). Then \(x_0\ge0\), \(x_i>0\), and \(x_0+\sum_i x_i=1\). With \(V=x_0+\sum_i c_i x_i\), maximizing \(\tau\) is equivalent to maximizing
\[
F=\sum_i d_i\log x_i+\log V.
\]
The objective is homogeneous of degree \(\rho=1+\sum_i d_i\) before taking logarithms; therefore the common Karush–Kuhn–Tucker multiplier of the budget constraint at any optimum is exactly \(\rho\). For positive coordinates, the equations are
\[
\frac{d_i}{x_i}+\frac{c_i}{V}=\rho,\qquad
\frac1V=\rho\ \text{if }x_0>0.
\]
When \(x_0=0\), the remaining complementary inequality is \(1/V\le\rho\).

**4. Active direct edge.** If \(x_0>0\), then \(V=1/\rho\). Hence
\[
x_i=\frac{d_i}{\rho(1-c_i)}=\frac{\ell_i^2}{\rho(\ell_i+1)},
\qquad
x_0=\frac{1-S}{\rho},
\]
using \(\ell_i^2/(\ell_i+1)=\ell_i-1+1/(\ell_i+1)\). These values satisfy every KKT equation, and are feasible precisely when \(S<1\). At \(S=1\) they give a feasible boundary solution with \(x_0=0\).

**5. Deleted direct edge.** Suppose \(x_0=0\). Put \(\xi=\rho V\). The long-path stationarity equations give
\[
x_i=\frac{d_i\xi}{\rho(\xi-c_i)}.
\]
Positivity requires \(\xi>\max_i c_i\). The identity \(V=\sum_i c_i x_i\) becomes
\[
1=\sum_i\frac{d_i c_i}{\xi-c_i}
=\sum_i\frac{\ell_i-1}{\xi\ell_i^2-1}.
\]
The right side strictly decreases from \(+\infty\) to zero on \((\max_i c_i,\infty)\), so its root is unique. At \(\xi=1\), it equals \(S\). Therefore the root satisfies \(\xi\ge1\) exactly when \(S\ge1\). This is exactly the missing KKT inequality \(1/V\le\rho\) for the deleted edge. Reverting \(x_i\) to \(w_i\) yields the stated formula. Strict concavity proves global optimality and uniqueness in every regime. \(\square\)

## Verification
The standalone `verify.py` constructs the full graph Laplacian from individual edges, evaluates a reduced determinant, and compares it with the path product formula. It checks three nonuniform exact-rational configurations and equality under rearrangements within a path. Nine heterogeneous length tuples are tested against a full-dimensional, edge-by-edge constrained SLSQP optimization; the formula's budget, determinant, and numerical optimality agree. Representative checks include \((2,3)\) with a positive shortcut, \((2,2,2)\) at the transition, and \((2,2,2,2)\) beyond it. `verify_output.txt` gives the recorded run output. Numerical tests support but do not establish the arbitrary-parameter theorem; that conclusion follows from the proof above.

## Relationship to prior work
Weighted tree-connectivity and determinant-maximization under network constraints are established concepts. Cheng (1981) identifies the connection with D-optimal design and proves graph-topology extremal theorems for specified numbers of edges, not the present fixed-support continuous-conductance allocation. Boyd (2006) formulates general convex graph-Laplacian eigenvalue optimization, but does not present the reciprocal-path-length shortcut criterion. Khosoussi and coauthors (first public preprint 2016) study weighted tree-connectivity, edge selection, and its convex relaxations; the inspected original includes the weighted matrix-tree theorem and general MAXDET formulations, not an exact optimum or zero-shortcut classification for arbitrary internally disjoint path lengths. General-purpose convex optimization methods imply that an optimum can be computed, but not the explicit harmonic threshold without additional graph-specific analysis.

## Limitations
The theorem assumes identical unit conductance cost per individual edge, a single direct terminal edge, and otherwise internally disjoint paths of length at least two. It does not cover unequal construction costs, prescribed lower/upper conductance bounds, additional cross-connections, or robustness measured by the minimum spanning-tree weight. Full analytical correctness is established under these assumptions; external independent review and a definitive exclusion of all specialized prior literature have not been performed.

## References
- C.-S. Cheng, *Maximizing the Total Number of Spanning Trees in a Graph: Two Related Problems in Graph Theory and Optimum Design Theory*, Journal of Combinatorial Theory, Series B **31** (1981), 240–248.
- S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, Proceedings of the International Congress of Mathematicians, Vol. III (2006), 1311–1319. https://www-leland.stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf
- K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116, first publicly submitted 2016-04-05. https://arxiv.org/abs/1604.01116
