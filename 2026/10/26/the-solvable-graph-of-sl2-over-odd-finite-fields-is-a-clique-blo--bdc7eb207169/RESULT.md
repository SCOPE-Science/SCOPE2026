# The solvable graph of \(\mathfrak{sl}_2(\mathbb F_q)\) is a clique-blown-up middle graph: component classification, spectrum, and trees

## Finding
For every **odd prime power** \(q\ge3\), put \(n=q+1\), \(m=q-1\), and \(c=q(q-1)/2\). Let \(\Gamma_q\) be the simple graph on nonzero elements of \(L=\mathfrak{sl}_2(\mathbb F_q)\), where distinct \(x,y\) are adjacent exactly if their Lie-generated subalgebra is solvable. Let \(K_n^+\) be the graph obtained by attaching one pendant leaf to each vertex of the complete graph \(K_n\); write \(M_n=L(K_n^+)\) for its line graph. With \(G[H]\) denoting lexicographic graph product, there is an isomorphism
\[
\boxed{\Gamma_q\ \cong\ \big(M_n[K_m]\big)\ \sqcup\ cK_m.}
\]
The large component has \(N=m\binom{n+1}{2}\) vertices, and there are exactly \(c\) further components of size \(m\). The large component has the following **complete combinatorial Laplacian spectrum**, with all multiplicities and possible collisions treated as a multiset:
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
0&1\\
m(n+1)&1\\
\dfrac{m(2n+1+\sqrt{4n+1})}{2}&n-1\\
\dfrac{m(2n+1-\sqrt{4n+1})}{2}&n-1\\
2mn&\dfrac{n(n-3)}2\\
mn&n(m-1)\\
m(2n-1)&\binom n2(m-1)
\end{array}
\]
In addition, each of the \(c\) smaller components contributes a zero eigenvalue and the eigenvalue \(m\) with multiplicity \(m-1\). The number of spanning trees of the large component is
\[
\boxed{\tau_q=\frac{2}{n}(mn)^{2(n-1)}(2mn)^{n(n-3)/2}(mn)^{n(m-1)}\big(m(2n-1)\big)^{\binom n2(m-1)}.}
\]
The graph has independence number \(n+c\) and chromatic number \(mn\); its large component has diameter \(2\).

## Assumptions and scope
Here \(\mathbb F_q\) is any finite field of **odd** order; no primality assumption is made. Matrices in \(L\) have trace zero, and the Lie bracket is \([x,y]=xy-yx\). The solvabilizer is zero for this simple Lie algebra, so the graph indeed has all \(q^3-1\) nonzero matrices as vertices. The scalar multiple of a matrix means multiplication by an element of \(\mathbb F_q^\times\). The graph Laplacian is \(D-A\), with real spectral multiplicity understood algebraically. The notation \(cK_m\) means \(c\) disjoint copies, not a scalar multiple of the adjacency matrix. These statements do not cover characteristic two.

## Proof
**1. Classification of edges via Borels.** Any proper Lie subalgebra of \(L\) has dimension at most two. Every two-dimensional subalgebra \(\mathfrak b\) is nonabelian: the centralizer of any nonzero trace-zero matrix in \(L\) is its one-dimensional span, so there is no abelian two-plane. A two-dimensional nonabelian algebra has a basis \(h,z\) with \([h,z]=\lambda z\), \(\lambda\ne0\). The trace pairing gives \(\operatorname{tr}([h,z]z)=0=\lambda\operatorname{tr}(z^2)\). Since the characteristic is odd and \(\operatorname{tr}z=0\), the identity \(\operatorname{tr}(z^2)=0\) implies \(z^2=0\). The nilpotent \(z\) has a unique kernel line \(U\subseteq\mathbb F_q^2\), and \([h,z]\in\mathbb F_q z\) implies \(h(U)\subseteq U\). Thus \(\mathfrak b\) is the trace-zero algebra preserving \(U\). Conversely each of the \(q+1=n\) projective lines \(U\) defines such a two-dimensional solvable Borel algebra \(\mathfrak b_U\). For distinct nonzero \(x,y\), their span is a solvable Lie subalgebra exactly when they are scalar multiples or belong to a common Borel.

**2. Explicit incidence quotient.** For nonzero \(x\), let \(P(x)\) be the set of one-dimensional invariant subspaces of the defining two-dimensional module. This is precisely the set of Borels containing \(x\). According to the characteristic polynomial of \(x\), \(|P(x)|\) is respectively \(1\) (nonzero nilpotent), \(2\) (two distinct rational eigenlines), or \(0\) (irreducible quadratic). A nonzero nilpotent projective matrix line occurs once for every \(U\), giving \(n\) singleton labels \(\{U\}\). For each unordered pair \(\{U,V\}\) of distinct projective lines, the intersection \(\mathfrak b_U\cap\mathfrak b_V\) is a unique nonzero projective matrix line; these \(\binom n2\) lines carry two-element labels. The remaining projective matrix lines, in number \(q^2+q+1-n-\binom n2=q(q-1)/2=c\), carry empty labels. Every projective line contains exactly \(m=q-1\) nonzero matrices, which form a clique. Two distinct nonempty labels are adjacent precisely when they intersect; empty labels have no neighbors outside their own scalar line. The incidence graph on all one- and two-element labels is exactly the middle graph \(M_n=L(K_n^+)\), proving the displayed isomorphism and component count. In particular the components and all their edges are determined, not just the degrees.

**3. Laplacian of the middle graph.** Order the vertices of \(M_n\) first by its \(n\) singleton labels and then by its \(e=\binom n2\) pair labels. Let \(B\) be the ordinary \(n\)-by-\(e\) unsigned vertex-edge incidence matrix of \(K_n\). Direct degree counting gives the integer block matrix
\[
\mathcal L(M_n)=\begin{pmatrix}(n-1)I_n&-B\\-B^{\mathsf T}&2nI_e-B^{\mathsf T}B\end{pmatrix},\qquad BB^{\mathsf T}=(n-2)I_n+J_n.
\]
The constant-vector singular sector of \(B\) has squared singular value \(2(n-1)\) and gives eigenvalues \(0,n+1\). The \((n-1)\)-dimensional orthogonal sector has squared singular value \(n-2\) and yields the quadratic \(t^2-(2n+1)t+n^2\), whose roots are \((2n+1\pm\sqrt{4n+1})/2\). Finally \(\ker B\) has dimension \(e-n=n(n-3)/2\) (as \(n\ge4\)) and gives eigenvalue \(2n\). This proves the complete middle-graph Laplacian factorization.

**4. Clique blowup.** For any graph \(H\), the Laplacian on \(H[K_m]\) preserves the subspace of vectors constant on each \(m\)-clique and there acts as \(m\mathcal L(H)\). On each fiberwise sum-zero subspace, it acts by the scalar \(m(d_H(v)+1)\), of multiplicity \(m-1\) for each vertex \(v\). In \(M_n\), singleton labels have degree \(n-1\), while pair labels have degree \(2n-2\). Combining these with Step 3 gives all seven spectral rows. Each isolated smaller component \(K_m\) has Laplacian spectrum \(\{0,m^{[m-1]}\}\).

**5. Spanning trees, independence, and coloring.** By the matrix-tree theorem, \(N\tau_q\) is the product of all nonzero large-component Laplacian eigenvalues. The two conjugate quadratic roots multiply to \(n^2\), so their scaled pair contributes \((mn)^{2(n-1)}\). Dividing the remaining product by \(N=mn(n+1)/2\) yields the stated closed formula. An independent vertex set in \(M_n\) corresponds to a matching in \(K_n^+\); its maximum size is \(n\), attained by its \(n\) pendant edges. The clique blowup keeps independence number \(n\), while each isolated small clique adds one. Since \(n=q+1\) is even, the edges of \(K_n\) have a proper \((n-1)\)-edge-coloring, and all pendant edges can use color \(n\). Thus \(\chi(M_n)=n\), and the clique blowup has chromatic number \(mn\), also forced by its \(mn\)-clique at any original vertex. The other components need only \(m\) colors. Finally every pair of vertices of \(M_n\) is at distance at most two, and clique blowup preserves this diameter.

## Verification
Run `python3 verify.py`. The checker uses only the Python standard library. For \(q=3,5\), it enumerates every nonzero traceless matrix, independently computes Lie brackets and spans over the prime field, reconstructs every edge, and checks that adjacency agrees for **every pair** with the invariant-eigenline incidence criterion. It verifies component counts and degrees, then computes the exact integer characteristic polynomial of the middle-graph Laplacian with the Faddeev–LeVerrier algorithm and checks the claimed factorization coefficient by coefficient. The actual run returned `EXACT_CHECK_OK` for both fields followed by `VERIFY_OK`. The proof above covers all odd prime powers; enumeration alone would not do so.

## Relationship to prior work
Towers, Gutierrez, and Fernandez introduced the solvable graph of finite-dimensional Lie algebras and gave, in their preprint of **2025-11-11**, the degree sequence for \(\mathfrak{sl}_2(\mathbb F_q)\), the nonconnectedness observation, and the small \(q=3\) example. Their analysis of one, two, or zero rational eigenlines is foundational here. The contribution claimed here is not those degree counts: it is the **all-field explicit graph isomorphism**, its **entire Laplacian spectrum and exact spanning-tree number**, and the resulting global invariants. The middle-graph matrix algebra and matrix-tree theorem are standard graph-theoretic inputs, not new general spectral methods. Matching the earlier degree counts is a verification condition, not a novelty argument.

## Limitations
Only odd characteristic is treated. The result does not assert new general theorems about arbitrary simple Lie algebras, nor does it independently establish novelty beyond inspected publications and mathematical records. In particular, it is possible that the middle-graph identification, or an equivalent general incidence construction whose consequences subsume it, appears in an uninspected source. No independent audit has been performed.

## References
1. D. Towers, I. Gutierrez, L. Fernandez, *The solvable Graph of a finite-dimensional Lie Algebra*, first posted 2025-11-11, arXiv:2511.08290; published in Ricerche di Matematica, 2026, DOI: 10.1007/s11587-026-01093-w. Full text: https://arxiv.org/abs/2511.08290.
2. G. Kirchhoff, the classical matrix-tree theorem (1847); invoked only in its standard Laplacian-eigenvalue form.
