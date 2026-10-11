# Strict convexity and the full smooth locus of graph-edge numerical-radius norms

## Finding

For every finite simple undirected graph \(G=(V,E)\) with at least one edge, and over either \(\mathbb F=\mathbb R\) or \(\mathbb F=\mathbb C\), the edge-weight numerical-radius norm
\[
N_G(a)=\tfrac12\lambda_{\max}(A_G(a)),\qquad a\in\mathbb F^E,
\]
where \(A_G(a)\) is the symmetric matrix with entries \((A_G(a))_{uv}=|a_{\{u,v\}}|\) on edges and zero elsewhere, is **strictly convex if and only if the matching number of \(G\) is one**. Equivalently, deleting isolated vertices leaves a star or a triangle.

The entire nonzero real-Fréchet-smooth locus has a second precise graph characterization. At \(a\ne0\), let \(G_a\) retain exactly the edges with \(|a_e|>0\). For each nontrivial connected component \(C\) of \(G_a\), write \(\rho_C\) for the Perron eigenvalue of its positive weighted adjacency block. Then \(N_G\) is Fréchet differentiable at \(a\) (over the underlying real vector space) **if and only if** there is a unique component \(C_*\) with \(\rho_{C_*}=\max_C\rho_C\), and \(C_*\) is induced by its vertices in \(G\): every edge of \(G\) whose endpoints lie in \(V(C_*)\) has nonzero weight at \(a\).

If these conditions hold, let \(r\) be the unique nonnegative unit Perron eigenvector for \(A_G(a)\), supported on \(V(C_*)\). The derivative is
\[
DN_G(a)[h]=\sum_{\substack{e=\{u,v\}\in E\\a_e\ne0}}r_ur_v\,\operatorname{Re}\!\left(\frac{\overline{a_e}h_e}{|a_e|}\right).
\]
In particular, the periodic weighted-shift numerical-radius norm on \(\mathbb F^n\) is strictly convex among periods \(n\ge3\) exactly when \(n=3\). Its three-periodic norm is differentiable at precisely those nonzero weight triples having either one or three nonzero entries; at a triple with exactly two nonzero entries it has a genuine first-order cusp.

## Assumptions and scope

Throughout, \(G\) is finite, loopless, without multiple edges and with \(|E|\ge1\), and all edge coordinates vary freely in \(\mathbb F\). Isolated vertices are allowed. Strict convexity means that the midpoint of two distinct unit vectors has norm strictly less than one. Differentiability is real Fréchet differentiability, also when \(\mathbb F=\mathbb C\). The eigenvalue \(\lambda_{\max}\) is the largest **algebraic** eigenvalue of a real symmetric matrix (which equals its spectral radius for nonnegative symmetric matrices). The two ends of an edge \(e\) are denoted \(u,v\). The zero vector is excluded from the smooth-locus statement, since no nontrivial norm is Fréchet differentiable at zero.

The variational identity
\[
N_G(a)=\max_{\substack{r\in\mathbb R^V,\ r\ge0\\\sum_v r_v^2=1}}\;\sum_{e=\{u,v\}\in E}|a_e|r_ur_v
\]
follows by replacing a Rayleigh test vector by its coordinatewise modulus. It proves the triangle inequality, positive homogeneity and definiteness (one nonzero edge gives \(N_G(a)\ge |a_e|/2\)).

## Proof

**(1) Disjoint edges destroy strict convexity.** Suppose \(e,f\in E\) are vertex-disjoint. Put \(a_e=2\), with every other coordinate zero, and put \(b_e=2,b_f=s\) for any \(0<s<2\), with all remaining coordinates zero. The positive-support adjacency matrices consist of disjoint two-vertex blocks. Thus \(N_G(a)=N_G(b)=1\); moreover \(N_G((1-t)a+tb)=1\) for every \(0\le t\le1\), even though \(a\ne b\). Hence strict convexity requires matching number one.

**(2) Classification of matching-one graphs.** If every pair of edges of a finite simple graph meets, take two distinct edges \(uv,uw\). Every edge not incident to \(u\) must meet both edges and therefore must be \(vw\). If \(vw\) occurs, no fourth vertex can be incident to an edge: it would fail to meet at least one triangle edge. Thus, modulo isolates, the graph is a star or the triangle \(K_3\); the one-edge case is a star. Conversely, both types have matching number one.

**(3) Stars and triangles are strictly convex.** On a star the adjacency matrix has form \(\begin{psmallmatrix}0&b^\top\\b&0\end{psmallmatrix}\) after a vertex permutation, so \(N_G(a)=\|a\|_2/2\), a strictly convex norm over both fields. For a triangle, suppose \(N_G(a)=N_G(b)=N_G((a+b)/2)=1\) and put \(c=(a+b)/2\). Take a nonnegative unit maximizing Rayleigh vector \(r\) for \(c\). Then
\[
1=\sum_e|c_e|r_ur_v\le\tfrac12\sum_e(|a_e|+|b_e|)r_ur_v\le\tfrac12(N_G(a)+N_G(b))=1.
\]
If the support of \(c\) has at least two edges, it connects all three vertices, so Perron--Frobenius gives \(r_1,r_2,r_3>0\). Equality makes \(r\) a top eigenvector of both \(A_G(a)\) and \(A_G(b)\), each with eigenvalue two. The linear map from the three nonnegative edge coefficients \((u_{12},u_{23},u_{13})\) to \(A_G(u)r\) is injective: its determinant has absolute value \(2r_1r_2r_3>0\). Therefore \(|a_e|=|b_e|\) for every edge. Equality in the triangle inequality for \(a_e+b_e\), with \(r_ur_v>0\), then gives \(a_e=b_e\) for each edge, including in the complex case. If \(c\) has exactly one supported edge, \(r\) is positive on its two endpoints and zero at the third vertex. The eigenvector equations for \(a\) and \(b\), together with nonnegative adjacency entries, force all edges meeting the third vertex to vanish for both. Equality at the one remaining edge forces those coefficients to agree. Hence in every case \(a=b\), proving strict convexity.

**(4) Simple top eigenvalue and a uniform first-order expansion.** At any nonzero \(a\), the eigenvalues of \(A_G(a)\) are the union of those of the nontrivial positive-support components and zeros from isolates. Each component has a simple Perron eigenvalue and a strictly positive Perron vector. Thus \(\lambda_{\max}(A_G(a))\) is simple precisely when one component attains the maximum \(\rho_C\) strictly above all others. Let \(r\) be the corresponding nonnegative unit eigenvector, zero off that component. By the Rayleigh principle and the positive spectral gap to the second algebraic eigenvalue, for every small real-symmetric perturbation \(H\),
\[
\tfrac12\lambda_{\max}(A_G(a)+H)=N_G(a)+\tfrac12r^\top Hr+O(\|H\|_{\mathrm{op}}^2).
\]
For completeness, decompose a maximizing unit vector into its \(r\) component and its orthogonal component. If the second algebraic eigenvalue is at most \(2N_G(a)-\gamma\), the Rayleigh loss from an orthogonal component of length \(s\) is at least \(\gamma s^2\), whereas the perturbative cross-term is bounded by \(2\|H\|_{\mathrm{op}}s\). Maximizing this quadratic bound gives a uniform \(O(\|H\|_{\mathrm{op}}^2/\gamma)\) remainder. For \(H=A_G(a+h)-A_G(a)\) this is \(O(\|h\|^2)\), since modulus is Lipschitz. Consequently,
\[
N_G(a+h)-N_G(a)=\sum_{e=\{u,v\}}r_ur_v\bigl(|a_e+h_e|-|a_e|\bigr)+O(\|h\|^2).
\]

**(5) The smooth locus.** If there is a unique leading component and its vertex set induces every internal edge of \(G\), then the coefficient \(r_ur_v\) vanishes at each edge with \(a_e=0\). For \(a_e\ne0\), real-differentiability of the complex modulus gives \(|a_e+h_e|-|a_e|=\operatorname{Re}(\overline{a_e}h_e/|a_e|)+O(|h_e|^2)\). Substitution gives the displayed real Fréchet derivative.

Conversely, if two positive-support components share the largest Perron eigenvalue, multiply the edge weights of one such component by \(1+t\). For small \(t>0\), the maximum eigenvalue increases linearly, while for small \(t<0\) the other tied component still fixes the maximum; opposite one-sided directional derivatives preclude differentiability. If the leading component is unique but an original graph edge \(e=\{u,v\}\) internal to it has \(a_e=0\), then \(r_ur_v>0\) and perturbing only that edge by a real \(t\) gives \(N_G(a+t1_e)=N_G(a)+r_ur_v|t|+O(t^2)\). The two one-sided slopes disagree. These cases exhaust all failures of the stated criterion.

**(6) Periodic shifts.** Ridge's variational formula, reproduced as equation (5) and Example 1.6 of Sharif's 2023 paper, identifies the numerical radius of an \(n\)-periodic unilateral weighted shift for \(n\ge3\) with \(N_{C_n}\). The triangle \(C_3\) has matching number one, while each cycle \(C_n\) for \(n\ge4\) has two vertex-disjoint edges. The three-edge induced-support criterion gives the claimed one-or-three-support description of its smooth points.

## Verification

A standalone Python 3 (standard-library only) checker accompanies this proof as `verify_graph_norm.py`; running `python3 verify_graph_norm.py` checks the exact matching/star-or-triangle dichotomy for all \(1094\) nonempty labeled simple graphs with two through five vertices. It also checks the explicit two-disjoint-edge flat-face witnesses by symmetric Jacobi eigensolver, and exercises the triangular first-order cusp and a four-cycle cusp. The observed output was:

`VERIFY_OK graphs=1094 matching_one=109 disjoint_matching=985 triangle_cusp=0.2500004 triangle_axis_slope=2.5e-06 cycle4_cusp=0.1381970 analytic_proof_needed=True`

Finite numerical checks do not establish the all-graph theorem, the exact derivative, or strict convexity in arbitrary dimension; these are proved in the preceding sections. The finite eigensolver uses floating-point arithmetic and is not an exact spectral certificate.

## Relationship to prior work

Sharif, arXiv:2303.00876, Example 1.6 and equation (5), treats periodic weighted-shift numerical radii as norms on the periodic coefficient space and reproduces Ridge's Rayleigh quotient formula. Those results supply the motivating objects and the identification with cycles, but the inspected full paper discusses shift numerical radii, norm equivalence, operator norms and Banach limits, not strict convexity or the full differentiability locus in the edge-weight coordinates. Nussbaum (1986) studies strict log-convexity under diagonal scaling and convexity under diagonal perturbations of nonnegative matrices, not the asserted strict convexity classification for freely variable undirected edge weights. Perron-eigenvalue perturbation and edge sensitivity are established background tools; the induced-support and matching criteria concern different global and boundary-level questions.

## Limitations

This statement is restricted to finite simple undirected graphs and freely varying independent edge coefficients; it makes no assertion for loops, hypergraphs, directed graphs, infinite graph norms or coupled/degree-constrained edge weights. The complex derivative is only real-linear, not complex-holomorphic. The periodic-shift corollary is for \(n\ge3\) (at period two the standard periodic norm is an \(\ell_1\) norm, not the two-vertex simple-graph formula). The original Ridge paper and relevant broad matrix-convexity literature were not fully accessible during comparison; an equivalent earlier formulation under a different parameterization remains possible.

## References

1. A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876v1 (first public version 2023-03-02), full text https://arxiv.org/html/2303.00876v2, especially §1 and Example 1.6.
2. W. C. Ridge, *Numerical range of a weighted shift with periodic weights*, Proc. Amer. Math. Soc. 55 (1976), 107–110, DOI 10.2307/2041852; formula reproduced in [1].
3. R. D. Nussbaum, *Convexity and log convexity for the spectral radius*, Linear Algebra Appl. 73 (1986), 59–122, DOI 10.1016/0024-3795(86)90233-8; abstract at https://www.researchwithrutgers.org/en/publications/convexity-and-log-convexity-for-the-spectral-radius/.
4. K.-Z. Wang and P. Y. Wu, *Numerical ranges of weighted shifts*, J. Math. Anal. Appl. 381 (2011), 897–909, DOI 10.1016/j.jmaa.2011.04.010; related Perron-Frobenius results described in [1].
