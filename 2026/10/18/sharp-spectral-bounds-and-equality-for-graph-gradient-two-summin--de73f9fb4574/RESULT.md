# Sharp spectral bounds and equality for graph-gradient two-summing norms

## Finding
Let \(G=(V,E)\) be a finite connected simple graph with \(n=|V|\ge2\) vertices and \(m=|E|\ge1\) edges. Orient each edge arbitrarily and write \(b_e=\mathbf e_u-\mathbf e_v\) for its incidence vector. Put
\[
L=\sum_{e\in E}b_eb_e^\top,\qquad Q=(L^\dagger)^{1/2},\qquad S=\operatorname{tr}(L^{1/2}),\qquad \rho_e=b_e^\top Qb_e.
\]
Here \(L^\dagger\) is the Moore--Penrose inverse, so \(Q\) is the inverse square root of \(L\) on the zero-sum hyperplane and vanishes on constants. The values \(\rho_e>0\) are independent of edge orientation; we call them edge half-resistances.

Define the edge-gradient operator \(D_G:\ell_2^V(\mathbb R)\to\ell_\infty^E(\mathbb R)\) by \((D_Gu)_e=\langle b_e,u\rangle\). Its absolutely two-summing norm obeys
\[
\boxed{\ \biggl(\sum_{e\in E}\rho_e^2\biggr)^{1/2}\ \le\ \pi_2(D_G)\ \le\ \sqrt{S\max_{e\in E}\rho_e}\ }.\tag{1}
\]
Since \(\sum_e\rho_e=S\), this yields the exact spectral equality criterion
\[
\boxed{\ \pi_2(D_G)=\frac{\operatorname{tr}(L^{1/2})}{\sqrt m}\quad\Longleftrightarrow\quad \rho_e\text{ is independent of }e\in E.\ }\tag{2}
\]
Whenever equality holds, the \(m\) test vectors \(x_e=Qb_e\) attain the summing norm. The same theorem evaluates the free two-convex Banach-lattice norm of \(F_G=\bigvee_{e\in E}|\delta_{b_e}|\), because \(\|F_G\|=\pi_2(D_G)\) by the published free-lattice norm representation.

Equality in (2) holds for every connected edge-transitive graph and every connected nontrivial strongly regular graph. In particular, with \(n\ge3\),
\[
\pi_2(D_{C_n})=\frac{2}{\sqrt n}\cot\!\frac{\pi}{2n};\qquad \pi_2(D_{K_n})=\sqrt{2(n-1)}\quad(n\ge2).
\]
For a Boolean hypercube \(Q_d\), \(d\ge1\), it equals
\[
\pi_2(D_{Q_d})=\frac{\sum_{k=1}^{d}\binom dk\sqrt{2k}}{\sqrt{d\,2^{d-1}}}.
\]
For any connected nontrivial strongly regular graph on \(v\) vertices, of degree \(k\), adjacency eigenvalues \(k>r>s\) with multiplicities \(1,f,g\), the value is
\[
\pi_2(D_G)=\frac{f\sqrt{k-r}+g\sqrt{k-s}}{\sqrt{vk/2}}.
\]
For each of the three Chang graphs (which are not edge-transitive), this yields \((7\sqrt8+20\sqrt{14})/\sqrt{168}\). These are specializations of (2), not separate independent assertions.

## Assumptions and scope
All vector spaces, functionals and lattice norms are **real**. The graph is finite, undirected, unweighted, connected, simple, loopless and has at least one edge. The Euclidean domain uses the ordinary coordinate \(\ell_2\) norm, and the target has the ordinary maximum norm without degree or edge normalization. The two-summing norm is defined for \(T:H\to Y\) with finite-dimensional real Hilbert domain by
\[
\pi_2(T)=\sup\left\{\biggl(\sum_{j=1}^t\|Tu_j\|_Y^2\biggr)^{1/2}:\ t\ge1,\ \sup_{\|h\|_H\le1}\sum_{j=1}^t|\langle h,u_j\rangle|^2\le1\right\}.
\]
No choice of orientation affects this norm. The spectral square roots and pseudoinverse above are defined by the unique nonzero eigenvalues of the positive-semidefinite combinatorial Laplacian.

## Proof
**1. Operator constraint.** For vectors \(u_1,\ldots,u_t\in\mathbb R^n\), the weak two-summability condition is equivalent to \(\sum_j u_ju_j^\top\preceq I_n\). Indeed its left side is the maximum Rayleigh quotient of that positive matrix. Connectivity makes \(H=\mathbf1^\perp\) the positive spectral subspace of \(L\), whence \(QLQ=P_H\), the orthogonal projection onto \(H\).

**2. Constructive lower bound.** Choose \(u_e=Qb_e\) for each edge. This is admissible because
\[\sum_{e\in E}u_eu_e^\top=Q\Bigl(\sum_eb_eb_e^\top\Bigr)Q=QLQ=P_H\preceq I_n.\]
The \(e\)-th output coordinate on the \(e\)-th test vector is \(\langle b_e,u_e\rangle=\rho_e\). Thus
\[\pi_2(D_G)^2\ge\sum_e\|D_Gu_e\|_\infty^2\ge\sum_e\rho_e^2.\]
Cyclicity of trace gives \(\sum_e\rho_e=\operatorname{tr}(QL)=\operatorname{tr}(L^{1/2})=S\). Therefore Cauchy--Schwarz yields \(\sum_e\rho_e^2\ge S^2/m\), with equality if and only if all the positive \(\rho_e\) are equal.

**3. Sharp upper bound.** On \(H\), \(Q\) is the inverse of \(L^{1/2}\), and each \(b_e\) belongs to \(H\). The ordinary Euclidean Cauchy--Schwarz inequality in the spectral coordinates of \(L\) gives, for all \(u\in\mathbb R^n\),
\[|\langle b_e,u\rangle|^2\le(b_e^\top Qb_e)(u^\top L^{1/2}u)=\rho_e\,u^\top L^{1/2}u.\]
Setting \(R=\max_e\rho_e\) and using the matrix constraint of Step 1, every admissible family satisfies
\[
\sum_j\|D_Gu_j\|_\infty^2\le R\sum_j u_j^\top L^{1/2}u_j=R\operatorname{tr}\!\left(L^{1/2}\sum_ju_ju_j^\top\right)\le R\operatorname{tr}(L^{1/2})=RS.
\]
This proves (1). If \(\rho_e=S/m\) for every edge, its bounds coincide, proving sufficiency in (2) and attainment by the explicit \(m\)-tuple. Conversely, if the spectral identity in (2) holds, the lower chain in Step 2 forces equality in finite Cauchy--Schwarz, so all \(\rho_e\) agree. This proves necessity without assuming any automorphism group.

**4. Edge-transitive and strongly regular classes.** Every graph automorphism commutes with \(L\) and hence with \(Q\), so it preserves the scalars \(b_e^\top Qb_e\). Edge transitivity therefore ensures uniform \(\rho_e\).

For a connected nontrivial strongly regular graph with adjacency matrix \(A\), the algebraic identity \(A^2=(k-\mu)I+(\lambda-\mu)A+\mu J\) and \(AJ=kJ\) imply the adjacency algebra \(\operatorname{span}\{I,A,J\}\) is closed under multiplication. Its three spectral idempotents lie in that algebra, so the spectral function \(Q=((kI-A)^\dagger)^{1/2}\) has the form \(aI+bA+cJ\). Since all diagonal entries of \(A\) are zero and \(A_{uv}=1\) for adjacent vertices, \(\rho_{\{u,v\}}=Q_{uu}+Q_{vv}-2Q_{uv}=2(a-b)\) is independent of the edge, even when the graph is not edge-transitive.

**5. Spectral specializations.** For \(C_n\) the Laplacian eigenvalues are \(4\sin^2(\pi j/n)\), \(0\le j<n\); summing their nonnegative square roots uses \(\sum_{j=1}^{n-1}\sin(\pi j/n)=\cot(\pi/(2n))\). For \(K_n\), the positive Laplacian eigenvalue is \(n\) with multiplicity \(n-1\). For \(Q_d\), eigenvalues \(2j\) have multiplicity \(\binom dj\). For connected strongly regular graphs, the nonzero Laplacian eigenvalues are \(k-r\) and \(k-s\) of multiplicities \(f,g\). In each case divide the sum of the square roots by the square root of the number of edges. The Chang parameters \((v,k,\lambda,\mu)=(28,12,6,4)\) give adjacency eigenvalues \(4\) and \(-2\) with multiplicities \(7\) and \(20\); the displayed formula follows.

**6. Free-lattice interpretation.** The pointwise lattice element \(F_G\) acts on \(u\in(\ell_2^V)^*\cong\ell_2^V\) as \(\max_e|\langle b_e,u\rangle|=\|D_Gu\|_\infty\). The defining norm of the free two-convex Banach lattice is the supremum of sums of squares of these values over all weakly two-summable dual-vector families of norm at most one (Jardón-Sánchez et al., Eq. (1.1), Theorem 6.1). Hence it equals \(\pi_2(D_G)\), without an additional normalization constant.

## Verification
A standalone NumPy verifier in `verify.py` forms the actual oriented incidence matrix, diagonalizes \(L\), computes the pseudoinverse square root and verifies the norming-frame identity \(\sum_e(Qb_e)(Qb_e)^\top=P_H\), the trace identity, both bounds, and equality for cycles, complete and complete-bipartite graphs, hypercubes, and a Seidel-switched Chang graph. It also checks strict inequality against the spectral baseline on a nonuniform-edge path. Run `python3 verify.py` with NumPy installed. The finite floating-point tests are reproducibility checks, **not** an infinite proof or an independent audit; Steps 1--6 establish the theorem for all allowed graphs.

## Relationship to prior work
The free two-convex lattice norm representation and its connection with summing maps are due to Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky [1]. Lee, Sharma, Junge and Romberg [2] analyze two-summing norms of adjoint matrix operators through factorization and semidefinite bounds. These provide frameworks, not the particular graph-gradient spectral inequality or its necessary-and-sufficient equality criterion. A prior exact evaluation for complete-bipartite gradients is subsumed by the present theorem and is **not** counted as new here; the new content is the all-connected-graph two-sided bound, its exact uniform-half-resistance boundary, and the non-edge-transitive strongly regular class. The Chang switching construction and non-edge-transitivity are documented in [3, 4]. A fully equivalent classical operator-ideal formulation outside the inspected material remains a residual literature risk.

## Limitations
The upper and lower bounds need not coincide for nonuniform half-resistances; no exact general formula for \(\pi_2(D_G)\) beyond the equality class is asserted. The condition involves a spectral fractional power and is not claimed to be an efficient purely combinatorial characterization. No infinite graph, weighted-edge, complex-scalar, or exponent-other-than-two extension is proved. Numerical spectral diagonalization is approximate and cannot prove exact equality for unbounded families. Independent audit has not been performed.

## References
[1] H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete, V. G. Troitsky, *Free Banach lattices under convexity conditions*, arXiv:2101.03510 (first posted 2021-01-10); RACSAM 116, Article 15 (2022), doi:10.1007/s13398-021-01155-8. In particular the introductory norm formula and Section 6.

[2] K. Lee, R. S. Sharma, M. Junge, J. Romberg, *Approximately low-rank recovery from noisy and local measurements by convex program*, Information and Inference 12 (2023), 1612--1654, doi:10.1093/imaiai/iaad013. Compare Sections 3.1--3.2 (two-summing adjoint factorizations and bounds).

[3] E. W. Weisstein, *Chang Graphs*, MathWorld, https://mathworld.wolfram.com/ChangGraphs.html (parameters and switching construction).

[4] M. Lavrov, *Strongly regular graph which is not edge transitive*, Mathematics Stack Exchange (2020), https://math.stackexchange.com/questions/3576253/strongly-regular-graph-which-is-not-edge-transitive (explicit switching-set witness for distinct edge orbits).
