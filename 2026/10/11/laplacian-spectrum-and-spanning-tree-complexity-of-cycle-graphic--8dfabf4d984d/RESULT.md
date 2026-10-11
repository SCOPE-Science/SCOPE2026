# Laplacian spectrum and spanning-tree complexity of cycle graphical zonotopes

## Finding
Let \(n\ge3\), let \(C_n\) be the cycle on \(n\) labeled vertices, and define its graphical zonotope
\[
Z_n=\sum_{\{i,j\}\in E(C_n)}[e_i,e_j]\subset\mathbb R^n.
\]
Write \(G_n\) for the undirected one-skeleton of \(Z_n\), and \(L_n=\operatorname{diag}(\deg)-A\) for its **combinatorial**, not normalized, Laplacian. Then \(G_n\) is the induced hypercube graph obtained from \(Q_n\) by removing the all-zero and all-one vertices; in particular it has \(2^n-2\) vertices.

Set \(d_r=\binom nr-\binom n{r-1}\) for \(0\le r\le\lfloor n/2\rfloor\), with \(\binom n{-1}=0\). For \(r=0,1\), define polynomials by the integer recurrences
\[
F_{r,0}(t)=1,\qquad F_{r,1}(t)=t-(n-1),
\]
\[
F_{r,j}(t)=\bigl(t-n+\mathbf1_{j=n-1}\bigr)F_{r,j-1}(t)
 -(j-r)(n-j+1-r)F_{r,j-2}(t),
\qquad 2\le j\le n-1,
\]
and let \(P_r(t)=F_{r,n-1}(t)\). Then the **complete** Laplacian characteristic polynomial is
\[
\boxed{\det(tI-L_n)=P_0(t)P_1(t)^{n-1}
\prod_{r=2}^{\lfloor n/2\rfloor}
\prod_{k=r}^{n-r}(t-2k)^{d_r}.}
\]
Empty products equal \(1\). All multiplicities and factors are included; coincident eigenvalues from different factors add their multiplicities.

Define the positive integer
\[
D_n=\frac{(n-1)!(n-2)\bigl((n-2)2^{n-1}+2\bigr)}{(n-1)^2}.
\]
The exact number of undirected spanning trees of \(G_n\) is
\[
\boxed{\tau(G_n)=\frac{(n-1)!}{n}D_n^{\,n-1}
\prod_{r=2}^{\lfloor n/2\rfloor}
\left(2^{n-2r+1}\frac{(n-r)!}{(r-1)!}\right)^{d_r}.}
\]
The first values for \(n=3,4,5\) are \(6\), \(331776\), and \(97955205120000000\).

## Assumptions and scope
The assertions hold for **every integer** \(n\ge3\); graph vertices and edges are unweighted, every spanning tree is counted once, and \(\det(tI-L_n)\) uses the usual nonnegative Laplacian convention. The polytopes lie in a codimension-one affine hyperplane, of intrinsic dimension \(n-1\). The result concerns the spanning trees of the **one-skeleton** of the zonotope; this is different from the classical identity relating the *Euclidean volume* of a graphical zonotope to the spanning trees of its *defining cycle*.

## Proof
**1. Identification of the polytope graph.** The normal fan of \(Z_n\) is the graphical arrangement \(x_i=x_j\) over edges of \(C_n\). Its full-dimensional chambers are in bijection with acyclic orientations of \(C_n\), and adjacent chambers differ by one edge orientation. Among the \(2^n\) edge orientations, precisely the two directed cyclic orientations are excluded. Thus the one-skeleton is \(Q_n\) with these two antipodal orientation strings deleted. Since \(n\ge3\), it is connected. A surviving vertex of Hamming weight \(j\) has degree \(n-1\) if \(j=1\) or \(j=n-1\), and otherwise degree \(n\); the two endpoint ranks are absent.

**2. Boolean harmonic decomposition.** Regard the space of real functions on subsets of \([n]\) as a direct sum of rank spaces \(V_j\). Define the raising operator \(U:V_j\to V_{j+1}\) by summing over one-element deletions of an output subset, and the lowering operator \(D=U^*\). Direct double counting gives \(DU-UD=(n-2j)I\) on \(V_j\). In particular, \(U\) is injective for \(j<n/2\), since
\[
\|Uf\|^2=\|Df\|^2+(n-2j)\|f\|^2.
\]
For each \(0\le r\le\lfloor n/2\rfloor\), set \(H_r=\ker(D:V_r\to V_{r-1})\). Then \(\dim H_r=d_r\). Orthogonality and the preceding commutator yield the complete decomposition into mutually orthogonal strings \(U^{j-r}h\), one for each orthonormal \(h\in H_r\), over \(r\le j\le n-r\). After normalizing each string vector, the adjacency operator \(U+D\) has offdiagonal entries
\[
\sqrt{(j+1-r)(n-j-r)}\qquad(r\le j<n-r).
\]
These formulas follow inductively from the commutator, and the dimensions sum to \(2^n\), so no eigenvectors are omitted.

Delete the rank-zero and rank-\(n\) basis vectors belonging only to the \(r=0\) string. The resulting Laplacian leaves all the indicated strings invariant: it has diagonal \(n-1\) at ranks \(1,n-1\), diagonal \(n\) elsewhere, and negatives of the preceding adjacency entries off diagonal. Consequently the \(r=0\) and \(r=1\) strings each contribute an \((n-1)\)-by-\((n-1)\) symmetric tridiagonal block \(M_r\), with \(r=1\) occurring \(n-1\) times. Their determinants are precisely the integer continuants \(P_r(t)=\det(tI-M_r)\) given in the statement. In the \(r\ge2\) strings, there are no endpoint defects; the block has diagonal \(n\) and is unitarily equivalent to \(2rI+L(Q_{n-2r})\) restricted to the rank-symmetric functions. Its eigenvalues are exactly \(2r,2r+2,\dots,2(n-r)\), all simple within each string. This proves the factorization.

**3. Product of nonzero eigenvalues in the radial block.** The first block \(M_0\) is a symmetric path Laplacian under the rank masses \(c_j=\binom nj\), \(1\le j\le n-1\). Neighboring rank conductances are \(w_j=c_j(n-j)=c_{j+1}(j+1)\). Its kernel is spanned by \((\sqrt{c_j})_{j=1}^{n-1}\) and has squared norm \(2^n-2\). The cofactor obtained by omitting its rank-\(1\) row and column is
\[
\prod_{j=1}^{n-2}w_j\Big/\prod_{j=2}^{n-1}c_j=(n-1)!.
\]
For a connected symmetric Laplacian-like matrix with one-dimensional kernel, that cofactor equals the product of nonzero eigenvalues times the squared corresponding normalized kernel coordinate. Here the coordinate is \(n/(2^n-2)\). Therefore
\[
\prod_{\lambda\in\operatorname{spec}(M_0),\lambda\ne0}\lambda
=\frac{(n-1)!(2^n-2)}{n}.
\]

**4. Exact determinant of the first harmonic block.** Let \(B\) be the size-\(n-1\) tridiagonal matrix obtained from \(M_1\) by setting both endpoint diagonal entries to \(n\). It has diagonal \(n\) and offdiagonal entries \(-\sqrt{j(n-j-1)}\) between ranks \(j\) and \(j+1\). Write \(E=e_1e_1^{\mathsf T}+e_{n-1}e_{n-1}^{\mathsf T}\); then \(M_1=B-E\). For \(0\le k\le n-1\), the leading \(k\)-by-\(k\) determinant of \(B\) is
\[
B_k=k!\sum_{\ell=0}^k\binom{n-1}{\ell}.
\]
This follows by induction from \(B_0=1\), \(B_1=n\), and \(B_k=nB_{k-1}-(k-1)(n-k)B_{k-2}\), using Pascal's identity. Thus \(\det B=2^{n-1}(n-1)!\). Standard cofactor identities, together with the reversal symmetry of \(B\), give the two diagonal entries and the corner entry of its inverse:
\[
(B^{-1})_{1,1}=(B^{-1})_{n-1,n-1}
=\frac{2^{n-1}-1}{(n-1)2^{n-1}},
\quad
(B^{-1})_{1,n-1}=\frac1{(n-1)2^{n-1}}.
\]
(The corner numerator is the product \(\prod_{j=1}^{n-2}\sqrt{j(n-j-1)}=(n-2)!\).) The rank-two matrix determinant lemma applied to \(B-E\) yields
\[
\det M_1=\det B\left[(1-(B^{-1})_{1,1})^2-(B^{-1})_{1,n-1}^2\right]
=\frac{(n-1)!(n-2)((n-2)2^{n-1}+2)}{(n-1)^2}=D_n.
\]
In particular, this expression is a positive integer because it is the determinant of the positive definite first harmonic block.

**5. Spanning trees.** The spectrum of each remaining rank-\(r\) block has product
\[
\prod_{k=r}^{n-r}2k=2^{n-2r+1}\frac{(n-r)!}{(r-1)!}.
\]
There are \(2^n-2\) vertices and exactly one Laplacian zero eigenvalue. Kirchhoff's matrix-tree theorem divides the product of all nonzero Laplacian eigenvalues by \(2^n-2\). Combining steps 3 and 4, the factor \(2^n-2\) cancels, leaving the displayed spanning-tree product. This completes the proof for all \(n\ge3\).

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. The standalone script constructs the induced hypercube graph independently from bitstrings, checks the characteristic-polynomial factorization by modular direct determinants at \(53\) parameter/evaluation pairs for \(3\le n\le7\), and compares the exact integer spanning-tree product with independent Laplacian cofactors at \(n=3,4,5,6\). All checks passed. The symbolic derivation above, rather than finite data, establishes the all-dimensional claims.

## Relationship to prior work
Padrol, Pilaud, and Poullot give the normal-fan, acyclic-orientation, and deformation-cone description for graphical zonotopes (arXiv:2111.12422). Grujić, arXiv:1604.06931v2, Proposition 5.2, already gives the complete face polynomial of the **same cycle graphical zonotope**, including its \(2^n-2\) vertices; that face-count formula does not determine the Laplacian spectrum or the number of spanning trees of the one-skeleton. Their result also recalls the classical identity between a graphical zonotope's *volume* and the defining graph's spanning-tree number, which is not the invariant calculated here. Bernardi (arXiv:1207.0896) computes spanning-tree counts for the **unpunctured** hypercube and certain augmented hypercubes, not this induced graph after deleting its two antipodes. Cardinal, Hoang, Merino, Mička, and Mütze (arXiv:2212.03915) study generation and flips of acyclic orientations; their results concern Hamilton traversals rather than this all-dimensional evaluated Laplacian spectrum. The derivation uses classical Boolean-lattice operators and Kirchhoff's theorem, and does not claim these general tools are new.

## Limitations
The result determines the full characteristic polynomial by two explicit continuants and a product, not by a closed radical expression for every eigenvalue. All-dimensional proof completeness is mathematical, not external formal certification. The inspected literature has not furnished an equivalent preexisting evaluated formula, but literature under the aliases “antipodally punctured hypercube” and “cycle-orientation flip graph” may remain unindexed or unavailable. No independent external audit has been performed.

## References
1. A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422v1 (first public 2021-11-24); full text arXiv:2111.12422v2, Sections 1.3 and 2. https://arxiv.org/abs/2111.12422
2. O. Bernardi, *On the spanning trees of the hypercube and other products of graphs*, arXiv:1207.0896v3 (2012). https://arxiv.org/abs/1207.0896
3. J. Cardinal, H. P. Hoang, A. Merino, O. Mička, T. Mütze, *Combinatorial generation via permutation languages. V. Acyclic orientations*, arXiv:2212.03915v1 (2022). https://arxiv.org/abs/2212.03915
4. V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931 (2016). https://arxiv.org/abs/1604.06931
