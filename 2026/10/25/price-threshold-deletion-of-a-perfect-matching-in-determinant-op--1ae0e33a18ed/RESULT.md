# Price-threshold deletion of a perfect matching in determinant-optimal bipartite networks

## Finding
Fix an integer \(n\ge3\), a budget \(B>0\), and a relative edge price \(\tau>0\). Consider the simple complete bipartite graph \(K_{n,n}\), with labeled sides \(u_1,\ldots,u_n\) and \(v_1,\ldots,v_n\), and distinguished perfect matching \(M=\{u_iv_i:1\le i\le n\}\). Every edge receives its *own* nonnegative conductance. Each matching conductance costs \(\tau\) per unit and every other conductance costs one per unit; total expenditure must equal \(B\). Maximize the weighted spanning-tree enumerator, equivalently the determinant of any reduced weighted Laplacian.

The **unique globally optimal allocation**, including among all asymmetric allocations, puts a common conductance \(a_*\) on each of the \(n\) matching edges and a common conductance \(b_*>0\) on each of the \(n(n-1)\) other edges. Define
\[
\tau_c(n)=\frac{n(2n-3)}{(n-2)(2n-1)}
=1+\frac{2(n-1)}{(n-2)(2n-1)}.
\]
The entire distinguished matching is optimally removed exactly when \(\tau\ge\tau_c(n)\). More precisely, if \(\tau<\tau_c(n)\), set
\[
z_* = \frac{n-2\tau(n-1)+\sqrt{n(n+2\tau^2-2\tau)}}{2\tau}>0;
\]
otherwise set \(z_*=0\). Then
\[
 b_* = \frac{B}{n(\tau z_*+n-1)},\qquad a_*=z_*b_*.
\]
The exact maximum tree weight is
\[
\mathcal T_*=n^{n-2}\left(\frac Bn\right)^{2n-1}
\frac{(z_*+n-1)(2z_*+n-2)^{n-1}}
{(\tau z_*+n-1)^{2n-1}}.
\]
The critical premium satisfies \(\tau_c(n)-1\sim1/n\); consequently, for every fixed \(\varepsilon>0\), all sufficiently large such networks remove their entire distinguished matching when its unit price is \(1+\varepsilon\). At equal unit prices \(\tau=1\), the unique optimum is uniform on all \(n^2\) edges, with conductance \(B/n^2\) each.

## Assumptions and scope
The network has \(2n\) distinct vertices; edge conductances are continuous nonnegative real variables, with no per-edge caps or prescribed positive lower bounds. The price of a matching edge is the same for all \(n\) matching edges, and the price of every remaining edge is one. \(\mathcal T(w)\) is the sum over every spanning tree of the product of its edge conductances; a zero-weight edge cannot contribute. The objective is the *weighted tree enumerator*, not the weight of a minimum spanning tree, Kirchhoff-index minimization, or largest Laplacian eigenvalue optimization. The graph with all matching edges removed, also called a crown graph, is connected for \(n\ge3\). The case \(n=2\) is excluded from the deletion criterion because removing the two matching edges disconnects the graph.

## Proof
**1. Existence, uniqueness, and unforced symmetry.** The budget simplex is compact and contains strictly positive allocations, so the continuous tree polynomial has a positive maximum. Every maximizer has connected positive-conductance support, since disconnected support gives tree polynomial zero. Fix one vertex as a Laplacian anchor. Its reduced Laplacian \(Q(w)\) is positive definite whenever the positive support is connected, and \(\log\det Q(w)\) is strictly concave in \(w\): the map from the edge weights to the reduced Laplacian is injective for any simple graph (non-anchor off-diagonal entries recover all corresponding weights, and the diagonals subsequently recover anchor-edge weights), while \(\log\det\) is strictly concave on positive definite symmetric matrices. Hence there is exactly one maximizing edge-weight vector. Simultaneous permutation of matching index labels, and interchange of the two sides, preserve both budget and tree enumerator. Uniqueness forces invariance. This automorphism group is transitive separately on matching and nonmatching edges, giving common weights \(a\) and \(b\) on the two classes. If \(b=0\), the graph is disconnected, so necessarily \(b>0\).

**2. Exact tree enumerator.** For such invariant weights, write \(d=a+(n-1)b\). The full \(2n\)-vertex Laplacian has block form
\[
L=\begin{pmatrix}dI&-[ (a-b)I+bJ]\\-[(a-b)I+bJ]&dI\end{pmatrix},
\]
where \(J\) is the \(n\)-by-\(n\) all-ones matrix. Splitting each side into constants and their orthogonal complements gives eigenvalues \(0\) (once), \(2d\) (once), \(nb\) (multiplicity \(n-1\)), and \(2a+(n-2)b\) (multiplicity \(n-1\)). The weighted matrix-tree theorem therefore gives, also at \(a=0\) by continuity,
\[
\mathcal T(a,b)=\frac{2d}{2n}(nb)^{n-1}[2a+(n-2)b]^{n-1}
=n^{n-2}b^{n-1}[a+(n-1)b][2a+(n-2)b]^{n-1}.
\]

**3. Complete one-dimensional optimization.** The exact budget equation is \(n\tau a+n(n-1)b=B\). Put \(z=a/b\ge0\). Then \(b=B/[n(\tau z+n-1)]\), and apart from a positive \(z\)-independent factor, the objective is
\[
F(z)=\frac{(z+n-1)(2z+n-2)^{n-1}}
{(\tau z+n-1)^{2n-1}}.
\]
Its logarithmic derivative is
\[
\frac{F'(z)}{F(z)}=\frac1{z+n-1}+\frac{2(n-1)}{2z+n-2}
-\frac{(2n-1)\tau}{\tau z+n-1}
=\frac{-(n-1)Q(z)}{(z+n-1)(2z+n-2)(\tau z+n-1)},
\]
where
\[
Q(z)=2\tau z^2+[4\tau(n-1)-2n]z
+\tau(n-2)(2n-1)-n(2n-3).
\]
All denominators are positive. If \(\tau<\tau_c(n)\), the quadratic has \(Q(0)<0\) and positive leading coefficient, so its two real roots have opposite signs. The unique positive root is exactly the claimed \(z_*\) (the discriminant after dividing by two is \(n(n+2\tau^2-2\tau)>0\)); the derivative of \(F\) changes from positive to negative there. If \(\tau\ge\tau_c(n)\), then \(Q(0)\ge0\) and \(Q'(z)=4\tau z+4\tau(n-1)-2n>0\) on \([0,\infty)\), because \(\tau_c(n)>1\) and \(n\ge3\). Thus \(F\) strictly decreases away from \(z=0\). In all cases the maximizer is unique and the formulas follow. The limit \(F(z)\to0\) as \(z\to\infty\) excludes an omitted endpoint.

**4. Electrical interpretation of the sharp transition.** On the optimal support at and above the transition, the graph is the crown graph with equal nonmatching conductance \(b\). Let \(R_{\mathrm{missing}}\) denote effective resistance between the endpoints of an absent matching edge, and \(R_{\mathrm{present}}\) effective resistance across an existing edge. The same four-eigenspace decomposition gives
\[
R_{\mathrm{missing}}=\frac{2n-3}{(n-1)(n-2)b}.
\]
For \(R_{\mathrm{present}}\), symmetry and the identity \(\sum_{e}b R_e=2n-1\) for the \(n(n-1)\) nonmatching edges yield
\[
R_{\mathrm{present}}=\frac{2n-1}{n(n-1)b}.
\]
Consequently \(R_{\mathrm{missing}}/R_{\mathrm{present}}=\tau_c(n)\). Indeed, \(\partial_{w_e}\log\mathcal T=R_e\) for a connected weighted graph, including one-sided differentiation on an absent candidate edge. At a boundary optimum, the incremental benefit per unit budget of reviving a matching edge cannot exceed that of an active nonmatching edge: \(R_{\mathrm{missing}}/\tau\le R_{\mathrm{present}}\). This is exactly \(\tau\ge\tau_c(n)\). It independently identifies the same threshold and explains its meaning as the crossing of cost-normalized electrical leverage scores. These resistance identities do not assert that the resistance formulas themselves are new.

## Verification
A standalone standard-library Python program `verification.py` and its saved output `verification_output.txt` accompany this statement. The program recomputes the reduced-Laplacian determinants with exact rational arithmetic for 24 cases, checks the two crown-graph resistances and their exact ratio for six graph sizes, compares candidate optima against 4,410 independently generated feasible asymmetric allocations across 42 parameter cases, and checks 196 equal-price/threshold identities. All reported checks pass. Exact numerical checks are corroboration only: the universal claims follow from the proof above. The program uses the mathematical weights and independently constructs each matrix rather than substituting the closed polynomial to compute its left side.

## Relationship to prior work
The weighted matrix-tree theorem and general convex log-determinant design principles are classical. Khosoussi et al. (2016) investigate graph-design objectives based on weighted tree count, mostly through edge selection and convex relaxations; their inspected primary source does not contain the continuous two-price \(K_{n,n}\) allocation classification. Ge and Dong (2019), extending earlier work on nearly complete bipartite graphs, provide exact spanning-tree enumeration involving specified matchings and exact resistances in matching-deleted bipartite graphs. Their matching-containment formula *can generate the underlying two-weight spanning-tree polynomial*, so that polynomial and the electrical resistance at the deleted-matching endpoint are not asserted to be original. The contribution assessed here is the sharp, globally unique **unrestricted conductance-budget optimizer**, its complete price phase transition, and its cost-normalized leverage interpretation. Ghosh, Boyd and Saberi (2008) optimize the *sum* of all effective resistances over conductances, a distinct spectral objective not implying the present determinant optimum. A general log-determinant framework or a counting identity alone does not explicitly determine the edge-price support transition; nevertheless, the proximity of the 2019 matching results is a genuine originality limitation.

## Limitations
The theorem does not treat unequal prices within the matching, additional per-edge bounds, unequal bipartition sizes, or optimization of Kirchhoff index or spectral gap. A full prior-art guarantee is not claimed: specialized formulations or straightforward derivations from published spanning-tree matching identities could reduce the independent novelty. The cited 2019 paper already covers the unoptimized tree counts for the crown endpoint. The classification is exact in real arithmetic; floating-point experiments cannot establish it independently.

## References
1. K. Khosoussi, G. S. Sukhatme, S. Huang and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-\(t\)-Optimal Graphs*, arXiv:1604.01116, first publicly posted April 5, 2016. https://arxiv.org/abs/1604.01116
2. J. Ge and F. Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs*, arXiv:1904.07766, first publicly posted April 16, 2019; see Theorems 1.3, 1.5 and 5.7. https://arxiv.org/abs/1904.07766
3. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, doi:10.1137/050645452. https://web.stanford.edu/~boyd/papers/eff_res.html
4. The weighted matrix-tree theorem and Foster's edge-resistance identity, used here in their standard forms.
