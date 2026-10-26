# Sharp linear-spline projection norms on regular metric trees and local high-girth stability

## Finding

Equip every edge of a graph with unit arclength. Let \(P\) be the \(L^2\)-orthogonal projection onto continuous, edgewise-affine functions represented by their vertex values. For the infinite \(d\)-regular metric tree \(\mathcal T_d\), every integer \(d\geq3\), put
\[
q_d=\frac{1}{d+\sqrt{d^2-d+1}}.
\]
Then the projection has a bounded extension to \(L^1\) and \(L^\infty\), and its exact attained endpoint norm is
\[
\boxed{\|P_d\|_{L^1\to L^1}=\|P_d\|_{L^\infty\to L^\infty}=\Lambda_d=\frac{3(1+q_d^2)}{(1+q_d)^2}.}
\]
The sequence \(\Lambda_d\) increases strictly with degree and satisfies \(\Lambda_d=3-3/d+O(d^{-2})\); for comparison the degree-two bi-infinite line has norm \(2\).

For every finite connected unit-edge metric graph \(G\) with no isolated vertices, the analogous projector satisfies \(\|P_G\|_{L^1\to L^1}=\|P_G\|_{L^\infty\to L^\infty}\leq3\). This bound is globally optimal even when restricted to **finite trees**. More quantitatively, if \(G\) is finite, \(d\)-regular, and has girth greater than \(2K+3\), then, for each integer \(K\geq0\),
\[
\boxed{\big|\|P_G\|_{\infty\to\infty}-\Lambda_d\big|\leq 3\,2^{-K}.}
\]
Similarly, at the center of a finite radius-\(R\) ball in the \(d\)-regular tree, its local absolute-kernel row sum differs from \(\Lambda_d\) by at most \(3\,2^{-K}\) whenever \(R\geq K+2\). Thus branching, not nonuniform edge lengths or cycles, yields a family whose exact constants rise from the line value \(2\) toward \(3\).

## Assumptions and scope

All edges have length one and carry unweighted one-dimensional arclength. Functions in the spline space are continuous at every vertex and affine on each edge. In a finite graph, \(P_G\) denotes the ordinary \(L^2\)-orthogonal projection on that finite-dimensional space. In the infinite tree, the closed spline subspace is the range of the bounded hat interpolation map from \(\ell^2(V)\) to \(L^2(\mathcal T_d)\); \(P_d\) is its Hilbert orthogonal projection. Endpoint statements concern the bounded integral-kernel extensions to \(L^1\) and \(L^\infty\), not an \(L^\infty\) Hilbert projection. The tree formula also holds algebraically for \(d=2\), but novelty is claimed only for the branching family \(d\geq3\).

## Proof

**1. Gram matrix and universal bound.** Write \(\phi_v\) for the continuous nodal hat functions and \(T c=\sum_v c_v\phi_v\). Each incident unit edge contributes \(1/3\) to \(\langle\phi_v,\phi_v\rangle\) and \(1/6\) to \(\langle\phi_v,\phi_w\rangle\) for neighboring vertices. Consequently
\[
M:=T^*T=\tfrac16(2D+A),\qquad b:=T^*f,\qquad (Pf)(v)=(M^{-1}b)_v,
\]
where \(D\) is the vertex-degree diagonal and \(A\) the adjacency matrix. Since \(M\) is positive definite, the nodal system is well defined; on the regular infinite tree \(M\geq(d/6)I\) by \(\|A\|\leq d\). Put \(R=D^{-1}A\). As \(\|R\|_{\ell^\infty\to\ell^\infty}=1\),
\[
M^{-1}b=3\sum_{k=0}^\infty(-R/2)^kD^{-1}b,
\quad |(D^{-1}b)_v|\leq\tfrac12\|f\|_\infty.
\]
This yields \(\|P_G\|_{\infty\to\infty}\leq3\) for every finite graph. The tail after terms indexed \(0,\ldots,K\) is at most \((3/2)2^{-K}\|f\|_\infty\). Edgewise affineness makes each output's absolute maximum occur at a vertex. On finite graphs the integral kernel is symmetric, so duality also yields the \(L^1\) bound.

**2. Exact inverse on the regular tree.** Set \(B=2dI+A\). For vertices \(u,v\) at combinatorial distance \(r\), define
\[
(B^{-1})_{uv}=C_d(-q_d)^r,\qquad C_d=\frac1{d(2-q_d)}.
\]
Indeed \(q_d\) is the small positive root of \((d-1)q^2-2dq+1=0\); that identity verifies every off-diagonal row of \(B B^{-1}=I\), while \(C_d(2d-dq_d)=1\) verifies the diagonal. Since \((d-1)q_d<1\), each inverse row is absolutely summable, and the kernel gives the bounded inverse. Multiplication by six gives \(M^{-1}=6B^{-1}\).

**3. Sharp kernel integral.** Fix a vertex \(o\). On an edge directed outward from a vertex at distance \(r\) from \(o\), with coordinate \(s\in[0,1]\), the kernel of \(f\mapsto (P_df)(o)\) is
\[
K_o(r,s)=6C_d(-q_d)^r\big(1-(1+q_d)s\big).
\]
There are exactly \(d(d-1)^r\) such edges. Their one-edge absolute integral is
\[
I(q)=\int_0^1|1-(1+q)s|\,ds=\frac{1+q^2}{2(1+q)}.
\]
Hence every vertex functional has norm
\[
\frac{6I(q_d)}{(2-q_d)(1-(d-1)q_d)}
=\frac{3(1+q_d^2)}{(1+q_d)^2},
\]
using \((2-q_d)(1-(d-1)q_d)=1+q_d\). Taking \(f\) to be the sign of this kernel on each edge attains the functional norm in \(L^\infty\); this sign input need not lie in \(L^2\), but finite truncations approach the sharp value using \(L^2\cap L^\infty\) inputs. The absolute kernel is symmetric, so the same sharp value holds in \(L^1\).

**4. Degree and finite-locality laws.** The positive root \(q_d\) decreases strictly with \(d\); the displayed norm decreases strictly with \(q\in(0,1)\). As \(q_d=1/(2d)+O(d^{-2})\), \(3-\Lambda_d=6q_d/(1+q_d)^2=3/d+O(d^{-2})\). For an arbitrary graph the order-\(K\) truncated Neumann operator is determined, at a root vertex, by the incident-edge data and vertex degrees within graph radius \(K+1\). Such a neighborhood is identical to the rooted regular tree if the graph has degree \(d\) and girth exceeding \(2K+3\), and also at the center of the finite radius-\(R\) regular-tree ball for \(R\geq K+2\). The two omitted Neumann tails have norms at most \((3/2)2^{-K}\) each, establishing the claimed error bound. Taking first \(R\to\infty\) then \(d\to\infty\) produces finite trees with projector norms tending to \(3\), proving optimality of the universal bound.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It performs exact rational inversions and integrations for finite metric graphs, checks the tree Green recurrence and geometric shell sums to 70-digit decimal precision for degrees \(2\) through \(39\), verifies strict degree monotonicity, and independently checks truncated-kernel locality on cycles. A replay passed **1,648 checks**. Finite checks do not substitute for the proof of the infinite-tree or all-graph statements.

## Relationship to prior work

Oswald's 2006 preprint, *A counterexample concerning the \(L_2\)-projector onto linear spline spaces*, establishes context for endpoint stability and recalls the earlier universal constant \(3\) on one-dimensional interval partitions. Its construction concerns planar simplicial triangulations and does not identify the degree-dependent infinite metric-tree constants, their sharp extremizers, or high-girth convergence. Post's 2007 account develops spectral analysis of metric graphs and the connection to discrete graph operators, but does not determine these spline projector norms. The line case is also present in earlier spline-projection literature and is not presented as new. The present contribution concerns regular-tree **branching** and its quantitative finite approximations, not merely repeating an interval-mesh estimate.

## Limitations

Graph edges are required to have equal unit length; arbitrary weighted networks, higher-degree edge polynomials, and nonsymmetric nonorthogonal projectors are not included. The finite-girth estimate gives a quantitative sufficient condition rather than a sharp error. No claim is made that the uniform upper bound \(3\) itself is historically new; it serves to identify the optimal global envelope reached asymptotically by branching metric trees. Bibliographic priority for the exact branching formula is assessed from inspected accessible sources, not independently certified; an inaccessible older specialist publication might contain an equivalent statement.

## References

1. P. Oswald, *A counterexample concerning the \(L_2\)-projector onto linear spline spaces*, arXiv:math/0611573v1, publicly posted 2006-11-19, https://arxiv.org/abs/math/0611573.
2. O. Post, *Spectral analysis of metric graphs and related spaces*, arXiv:0712.1507v1, publicly posted 2007-12-10, https://arxiv.org/abs/0712.1507.
3. M. Karkulik, D. Pfeiler, D. Praetorius, *\(L^2\)-orthogonal projections onto finite elements on locally refined meshes are \(H^1\)-stable*, arXiv:1307.0917v1 (2013), https://arxiv.org/abs/1307.0917.
4. M. Crouzeix and V. Thomée, *The stability in \(L^p\) and \(W_p^1\) of the \(L^2\)-projection onto finite element function spaces*, Mathematics of Computation 48 (1987), https://doi.org/10.1090/S0025-5718-1987-0878688-2 (full text not inspected).
