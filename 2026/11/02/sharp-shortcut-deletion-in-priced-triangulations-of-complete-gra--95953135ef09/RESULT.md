# Sharp shortcut deletion in priced triangulations of complete graphs

## Finding
For the triangulation \(T(K_n)\) of a complete graph, \(n\ge 3\), let original edges cost \(P>0\) per unit conductance and the two new spokes in every added triangle cost \(Q>0\) per unit. All edge conductances may be set independently to nonnegative values, subject to total cost at most \(B>0\). The unique allocation minimizing the sum of all pairwise effective resistances has a common original-edge conductance \(x_*\) and a common spoke conductance \(y_*>0\).

Define
\[
 r_c(n)=\frac{8(n+1)}{n^2+n+2},\qquad m=\binom n2,\qquad
 A_n=\frac{(n-1)^2(n+2)}{4(n+1)},\qquad
 C_n=\frac{(n-1)(n+2)}{2n}.
\]
The optimal ratio \(t_*=x_*/y_*\) is
\[
 t_*=\begin{cases}
 \displaystyle\frac12\left[\sqrt{\frac{2(n+1)}{n(n-1)}\left(\frac{4Q}{P}-1\right)}-1\right],& P/Q<r_c(n),\\[7pt]
 0,&P/Q\ge r_c(n).
 \end{cases}
\]
The individual optimal conductances and minimum Kirchhoff index are
\[
 y_*=\frac{B}{m(Pt_*+2Q)},\qquad x_*=t_*y_*,\qquad
 \mathcal K_*=\frac{(n+m)m}{B}(Pt_*+2Q)
 \left(A_n+\frac{C_n}{2t_*+1}\right).
\]
In particular, with equal prices \(P=Q\), all original clique edges receive exactly zero conductance if and only if \(n\ge8\). The price threshold obeys \(r_c(n)\sim 8/n\) as \(n\to\infty\). Thus the unique optimal support switches from the triangulation to its full subdivision backbone, while every added spoke stays positive.

## Assumptions and scope
Start with \(n\) labeled original vertices and one additional vertex \(v_{ij}\) for each unordered pair \(\{i,j\}\). Retain each original edge \(\{i,j\}\) and connect \(v_{ij}\) to \(i\) and \(j\); no other edges are allowed. This is the conventional triangulation graph \(T(K_n)\), not a planar triangulation. The graph has \(N=n+m\) vertices, \(m\) original edges and \(2m\) spokes. Nonnegative conductances are admitted, but disconnected allocations have infinite objective. Price \(P\) applies separately to each original edge and price \(Q\) separately to each spoke, with \(B>0\) a single total budget. The resistance objective is \(\mathcal K=\sum_{u<v}R_{uv}=N\operatorname{tr}(L^+)\), with the ordinary (unnormalized) weighted Laplacian \(L\) and its Moore--Penrose pseudoinverse \(L^+\). There are no prescribed equalities among individual edge conductances.

## Proof
**1. Unrestricted uniqueness and symmetry.** On connected allocations, restrict \(L\) to the orthogonal complement of its constant vector. The objective \(\operatorname{tr}(L^+)\) is the trace of the inverse of this positive-definite restriction. The inverse-trace function is strictly convex, and the map from all conductances to the Laplacian is injective because each distinct graph edge has a unique off-diagonal entry. Consequently, the objective is strictly convex along distinct connected allocations. It decreases strictly if a positive amount is added to any edge, so the budget is saturated. A connected feasible point exists (positive spokes), and the bounded budget simplex together with the blow-up at disconnection ensures existence. Hence the minimizer is unique. Permutations of the original \(n\) vertices preserve costs and the objective; uniqueness forces an equal value \(x\ge0\) on every original edge and \(y\ge0\) on every spoke. Necessarily \(y>0\), since \(y=0\) isolates all new vertices.

**2. Entire nonzero spectrum.** Let \(U\) be the unsigned \(n\)-by-\(m\) incidence matrix of \(K_n\), and \(J\) the all-ones \(n\)-by-\(n\) matrix. Its Gram matrix satisfies \(UU^{\mathsf T}=(n-2)I+J\). In the original/new-vertex ordering,
\[
 L=\begin{pmatrix}
 x(nI-J)+(n-1)yI&-yU\\
 -yU^{\mathsf T}&2yI_m
 \end{pmatrix}.
\]
The two constant-coordinate directions contribute one zero eigenvalue and one eigenvalue \((n+1)y\). For each of the \(n-1\) mutually orthogonal zero-sum original directions, there is a coupled two-dimensional block
\[
 \begin{pmatrix}nx+(n-1)y&-y\sqrt{n-2}\\-y\sqrt{n-2}&2y\end{pmatrix},
\]
whose trace and determinant are \(nx+(n+1)y\) and \(ny(2x+y)\). The remaining \(m-n\) eigenvalues (zero such multiplicity when \(n=3\)) equal \(2y\). These account for all \(N\) eigenvalues and remain positive apart from the single constant mode even when \(x=0\).

**3. Exact objective.** Summing reciprocals of the nonzero eigenvalues yields
\[
 \operatorname{tr}(L^+)=\frac1y\left[
 \frac1{n+1}+\frac{m-n}{2}+\frac{n-1}{n}\,
 \frac{nt+n+1}{2t+1}\right]
 =\frac1y\left(A_n+\frac{C_n}{2t+1}\right),\qquad t=\frac xy\ge0.
\]
The saturated budget is \(mPx+2mQy=B\), so \(y=B/[m(Pt+2Q)]\). Minimizing the Kirchhoff index is therefore equivalent to minimizing
\[
 F(t)=(Pt+2Q)\left(A_n+\frac{C_n}{2t+1}\right),\quad t\ge0.
\]
Its derivative is exactly
\[
 F'(t)=PA_n+\frac{C_n(P-4Q)}{(2t+1)^2}.
\]
For \(P\ge4Q\), this is positive everywhere. Otherwise it increases strictly toward \(PA_n>0\). Accordingly its minimizer is at zero precisely when \(PA_n+C_n(P-4Q)\ge0\), or equivalently
\[
 \frac PQ\ge\frac{4C_n}{A_n+C_n}=\frac{8(n+1)}{n^2+n+2}.
\]
When the inequality reverses, \(F'\) has the unique positive root displayed in the finding, using \(C_n/A_n=2(n+1)/[n(n-1)]\). Equality at the threshold still gives a unique boundary minimizer. Substitution yields the unique edge weights and the stated minimum objective.

**4. Support cutoff and scaling.** At equal prices, \(r_c(n)>1\) exactly when \(n^2-7n-6<0\), which for integer \(n\ge3\) means \(n\le7\). For \(n\ge8\), all original edges are deleted, but all spokes remain positive and the remaining graph is the connected subdivision \(S(K_n)\). Finally, \(n r_c(n)\to8\) directly from the rational threshold formula.

## Verification
Run \(\texttt{python3 verify.py}\) using the included Python standard-library-only checker. It reconstructs the full Laplacian for \(n=3,4,5,6\) at three exact rational conductance pairs, calculates \(\operatorname{tr}(L^+)\) by exact inversion of \(L+J_N/N\), and compares with the spectral formula. It also performs exact rational checks of the threshold identity, coefficient ratio and boundary derivative for \(3\le n\le100\), including the equal-price cutoff. The supplied run passed 308 checks. These finite computations corroborate but do not replace the all-size proof above.

## Relationship to prior work
Ghosh, Boyd and Saberi established general strict convexity, uniqueness, and semidefinite formulations for total-effective-resistance minimization; these general facts are not new here. Yang and Klein studied resistance-distance invariants under graph subdivision and triangulation, including a formula for the *fixed unit-conductance* Kirchhoff index of \(T(G)\) (Theorem 4.3 of their 2014 preprint). The present claim concerns a different assertion: a fully unrestricted **priced conductance optimization** on \(T(K_n)\), with exact optimal weights, a sharp direct-edge support transition and an equal-price cutoff at \(n=8\). The inspected cited sections do not state or imply that closed classification without additional spectral optimization. Related earlier graph-family optimizations do not cover the incidence-expanded complete-graph topology. A literature search is not a mathematical proof of priority, and specialized coverage could remain unindexed.

## Limitations
This theorem applies to one triangulation of \(K_n\), to uniform prices within each of its two edge orbits, and to the ordinary all-pairs resistance objective. It does not assert the same threshold for heterogeneous per-edge prices, multiple triangulation iterations, alternative objectives, or restricted/quantized conductances. The finite checker does not prove the infinite family; the analytic spectral and convexity argument does. Independent mathematical validation has not been performed.

## References
1. Yujun Yang and Douglas J. Klein, *Resistance distance-based graph invariants of subdivisions and triangulations of graphs*, arXiv:1403.1851v1, publicly posted 2014-03-07, https://arxiv.org/abs/1403.1851 (especially Section 4 and Theorem 4.3).
2. Arpita Ghosh, Stephen Boyd and Amin Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS 2006, https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf (especially Sections II, IV, and V--VI); extended journal version, *SIAM Review* 50 (2008), https://doi.org/10.1137/050645452.
