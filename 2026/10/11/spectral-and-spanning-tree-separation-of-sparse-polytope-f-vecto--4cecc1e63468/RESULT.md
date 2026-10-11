# Spectral and spanning-tree separation of sparse polytope f-vector twins

## Finding

Let \(d\ge3\) be an integer. Let \(A_d\) be obtained by truncating a nonsimple vertex of a \((2,d-2)\)-triplex, and \(B_d\) by truncating a simple vertex of a \((3,d-3)\)-triplex. A \((k,d-k)\)-triplex means a \((d-k)\)-fold pyramid over a simplicial \(k\)-prism. Truncation is a sufficiently shallow cut separating just the chosen vertex from the other vertices. Write \(G(P)\) for the undirected one-skeleton of a polytope, \(L(G)\) for its combinatorial graph Laplacian, and \(\tau(P)\) for the number of spanning trees of \(G(P)\).

**Theorem.** For every integer \(d\ge3\),
\[
\tau(A_d)=(d-1)^2(d+1)^{d-1}(d+3)^{d-2}.
\]
For every integer \(d\ge4\),
\[
\tau(B_d)=d(d+1)(d^2+2d-1)(d^3+3d^2-d-5)(d^2+4d+2)^{d-4},
\]
and the remaining case is \(\tau(B_3)=336\), compared with \(\tau(A_3)=384\). In all dimensions \(d\ge3\),
\[
\tau(A_d)>\tau(B_d),\qquad
\frac{\tau(B_d)}{\tau(A_d)}=1-\frac2d+O(d^{-2})\quad(d\to\infty).
\]
The Laplacian spectrum of \(G(A_d)\) is integral, while \(L(G(B_d))\) has eigenvalues \(d+1-\sqrt2\) and \(d+1+\sqrt2\). Thus these two graph invariants distinguish the families although they have identical face vectors.

## Assumptions and scope

All graphs are finite, simple, undirected, and unweighted; spanning trees are unrooted. Pyramid means a join with a vertex and prism means Cartesian product with a segment. The graph of a shallow truncation of a **simple** vertex is formed by deleting that vertex, introducing a clique indexed by its incident edges, and joining each new clique vertex to the surviving endpoint of its corresponding old edge. The geometric families are defined up to combinatorial equivalence, so \(\tau\) is independent of their particular coordinates.

The original classification [1] implies that the two families have \(2d+2\) vertices and \((d+3)(d-1)\) edges, and are the only edge-count minimizers in dimensions \(d=3,6\) and \(d\ge8\). There are additional co-minimizers in dimensions \(4\) and \(7\); in dimension \(5\), a different polytope has fewer edges. The assertion here compares the specified pair in **every** dimension \(d\ge3\); it does not rank other exceptional examples. The equality of all face counts \(f_k(A_d)=f_k(B_d)\), including the vertex and facet counts, is established by the later face-bound theorem [2], and is cited rather than claimed as new.

## Proof

**The product family.** Put \(r=d-3\), allowing \(r=0\). The square is a simplicial \(2\)-prism, so the graph of a \((d-3)\)-fold pyramid over it is \(K_r\vee C_4\), where \(\vee\) denotes graph join and \(K_0\vee C_4=C_4\). Source [1] identifies \(A_d\) as the prism over this pyramid, hence
\[
G(A_d)=(K_r\vee C_4)\mathbin{\square}K_2.
\]
The Laplacian eigenvalues of the first factor are \(0\) (once), \(d-1\) (twice) and \(d+1\) (multiplicity \(d-2\)). The Cartesian-product eigenvalues add to \(0\) or \(2\). Therefore the nonzero eigenvalues of \(G(A_d)\), with multiplicities, are
\[
2\ (1),\quad d-1\ (2),\quad d+1\ (d),\quad d+3\ (d-2).
\]
The matrix-tree theorem, with \(2d+2\) vertices, immediately yields the displayed formula for \(\tau(A_d)\); its spectrum is integral.

**The truncated-prism family.** In the base triangular prism of \(B_d\), label the triangles \(a_0,a_1,a_2\) and \(b_0,b_1,b_2\), connect corresponding \(a_i,b_i\), and append \(r\) mutually adjacent pyramid apices \(u_1,\ldots,u_r\), each joined to every prism vertex. Truncate the simple vertex \(a_0\). Its neighbors are \(a_1,a_2,b_0,u_1,\ldots,u_r\). Replace \(a_0\) by a \(d\)-clique with vertices \(t_{a_1},t_{a_2},t_{b_0},t_{u_1},\ldots,t_{u_r}\), and connect each new vertex just to its named old neighbor outside the new clique. This describes every edge of \(G(B_d)\).

For \(r\ge1\), the commuting permutations of the pairs indexed by \(1,2\) and the \(r\) apex/new-apex pairs decompose the Laplacian representation into three invariant parts. The \((r-1)\)-fold standard part has the two-dimensional block
\[
T_d=\begin{pmatrix}d+3&-1\\-1&d+1\end{pmatrix},
\qquad \det T_d=d^2+4d+2.
\]
The antisymmetric part exchanging the indices \(1,2\) has block
\[
S_d=\begin{pmatrix}d+1&-1&-1\\-1&d+1&0\\-1&0&d+1\end{pmatrix},
\quad \det S_d=(d+1)(d^2+2d-1).
\]
Its eigenvalues are \(d+1\) and \(d+1\pm\sqrt2\). The latter pair also exists when \(r=0\), since these three antisymmetric vectors are present in the original triangular-prism truncation.

The remaining seven-dimensional space consists of vectors constant on the classes \(A=\{a_1,a_2\}\), \(B=\{b_1,b_2\}\), \(C=\{b_0\}\), \(U=\{u_j\}\), \(T_A=\{t_{a_1},t_{a_2}\}\), \(T_C=\{t_{b_0}\}\), and \(T_U=\{t_{u_j}\}\). In that order, the quotient Laplacian is
\[
Q_r=\begin{pmatrix}
r+2&-1&0&-r&-1&0&0\\
-1&r+2&-1&-r&0&0&0\\
0&-2&r+3&-r&0&-1&0\\
-2&-2&-1&6&0&0&-1\\
-1&0&0&0&r+2&-1&-r\\
0&0&-1&0&-2&r+3&-r\\
0&0&0&-1&-2&-1&4
\end{pmatrix}.
\]
The class sizes \((2,2,1,r,2,1,r)\) give a positive left null vector of \(Q_r\); the all-ones vector is a right null vector, and the total size is \(N=2d+2\). Connectedness makes the zero eigenvalue simple. For a quotient matrix with these normalized null vectors, the product of its six nonzero eigenvalues equals \(N\) times the cofactor at the singleton class \(C\). Direct exact expansion gives
\[
\det (Q_r)_{\widehat C,\widehat C}=(r+3)(r^3+12r^2+44r+46).
\]
This identity also has a short exact certificate: every entry of the six-by-six cofactor is affine in \(r\), hence the determinant is a polynomial of degree at most six; checking it at the seven integers \(r=0,1,\ldots,6\) proves the identity for all \(r\). The supplied standalone verifier evaluates these seven determinants using fraction-free integer elimination, independently of a symbolic-algebra package.

Multiplying the nonzero Laplacian eigenvalues and dividing by \(N\) as in the matrix-tree theorem yields
\[
\begin{aligned}
\tau(B_d)&=(r+3)(r^3+12r^2+44r+46)\,
\det(S_d)\,[\det(T_d)]^{r-1}\\
&=d(d+1)(d^2+2d-1)(d^3+3d^2-d-5)(d^2+4d+2)^{d-4}.
\end{aligned}
\]
For \(d=3\), the absent apex classes are omitted. A direct seven-by-seven Laplacian cofactor of the eight-vertex truncated triangular prism gives \(336\); the complete graph construction and exact cofactor are reproduced by the verifier.

**Strict ordering and asymptotic proximity.** For \(d\ge4\), set \(C_d=(d+1)(d+3)\). Division of the two formulas gives
\[
\frac{\tau(B_d)}{\tau(A_d)}=
\frac{d(d^2+2d-1)(d^3+3d^2-d-5)}{(d-1)^2C_d^2}
\left(1-\frac1{C_d}\right)^{d-4}.
\]
The denominator of the first factor exceeds its numerator by
\[
\begin{aligned}
&(d-1)^2C_d^2-d(d^2+2d-1)(d^3+3d^2-d-5)\\
&\quad=h^5+18h^4+124h^3+406h^2+628h+372>0,
\qquad h=d-3\ge1.
\end{aligned}
\]
The other factor belongs to \((0,1]\), proving strict inequality for \(d\ge4\); the numerical cofactor values \(336<384\) give \(d=3\). Expansion of the rational first factor gives \(1-1/d+O(d^{-2})\), while the power factor is \(1-1/d+O(d^{-2})\), proving the stated asymptotic ratio.

## Verification

The standalone file `verify.py` uses only the Python standard library and implements two independent constructions of the full graph edge sets, fraction-free Laplacian cofactors, the seven-point polynomial identity, block determinant identities, and the strict comparison polynomial. Run `python3 verify.py` from the directory containing the extracted file. It reports `VERIFY_OK` on success. Complete matrix-tree comparisons were checked for all integers \(3\le d\le10\); the symbolic determinant identity and group-invariant decomposition, not the bounded enumeration, establish the general theorem. The reported graph vertex and edge counts were also independently checked in those dimensions.

## Relationship to prior work

Pineda-Villavicencio, Ugon, and Yost [1] introduce and classify the two families by face incidence and edge minimization, explicitly giving the prism/pyramid description of \(A_d\) and the simple-vertex truncation description of \(B_d\). The later lower-bound paper [2] proves the equality of their entire face vectors. Neither cited result states a spanning-tree formula, a strict all-dimensional tree-complexity ordering, or the irrational-versus-integral Laplacian distinction. The matrix-tree theorem and standard graph-product spectral rules are used openly; the seven-cell quotient computation and exact comparison are supplied here rather than attributed to these general tools.

## Limitations

The classification of all edge-count minimizers has exceptional dimensions; this theorem concerns just the designated \(A_d,B_d\), not the other exceptional minimizers. A full closed-form factorization of the remaining quintic quotient spectrum is not asserted. General identities and finite tests do not establish that no equivalent graph-theoretic formula exists elsewhere; the literature comparison is supported by inspected primary sources and named searches, not by a proof of absence. No independent audit or external certification has been carried out.

## References

1. G. Pineda-Villavicencio, J. Ugon, D. Yost, *Minimum number of edges of polytopes with \(2d+2\) vertices*, arXiv:2005.06746v1 (first public 2020-05-14); *Electronic Journal of Combinatorics* 29 (2022), P3.18. Relevant material: definitions of \(A_d,B_d\), Remarks 6–8, Theorem 13.
2. G. Pineda-Villavicencio, A. Tritama, J. Wang, D. Yost, *A lower bound theorem for \(d\)-polytopes with \(2d+2\) vertices*, arXiv:2409.14294 (initially public 2024-09-22; later revised). Relevant material: equation (2) and Theorem 3(i), asserting equal face counts for the two families.
3. Kirchhoff's matrix-tree theorem and the Laplacian spectral rules for graph joins and Cartesian products, used in their standard unweighted forms.
