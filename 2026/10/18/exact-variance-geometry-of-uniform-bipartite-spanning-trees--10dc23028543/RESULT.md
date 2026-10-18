# Exact variance geometry of uniform bipartite spanning trees

## Finding

Let \(a,b\ge 2\) be arbitrary integers. Choose uniformly among spanning trees of the complete bipartite graph \(K_{a,b}\). For each left vertex \(i\in\{1,\ldots,a\}\) and right vertex \(j\in\{1,\ldots,b\}\), let \(X_{ij}\) be the indicator that edge \((i,j)\) belongs to the tree. Regard \(X\) as a vector in the Euclidean space \(\mathbb R^{a\times b}\).

Its covariance operator has the following complete orthogonal decomposition. Multiplicities are dimensions of the indicated subspaces; when eigenvalues coincide, their multiplicities add.

| Eigenspace | Eigenvalue | Multiplicity |
|---|---|---|
| Constant matrices | \(0\) | \(1\) |
| Row contrasts, \(W_{ij}=r_i\) with \(\sum_i r_i=0\) | \(\frac{b-1}{ab}\) | \(a-1\) |
| Column contrasts, \(W_{ij}=c_j\) with \(\sum_j c_j=0\) | \(\frac{a-1}{ab}\) | \(b-1\) |
| Double-centered interactions, \(\sum_i W_{ij}=\sum_j W_{ij}=0\) | \(\frac{a+b-3}{ab}\) | \((a-1)(b-1)\) |

In particular, the covariance has rank \(ab-1\), and every centered matrix of deterministic edge weights has strictly positive random-tree cost variance.

Here is an exact formula for that variance. For any real \(a\)-by-\(b\) matrix \(W\), define its grand mean \(\mu=(ab)^{-1}\sum_{ij}W_{ij}\), its centered row means \(r_i=b^{-1}\sum_j W_{ij}-\mu\), its centered column means \(c_j=a^{-1}\sum_i W_{ij}-\mu\), and its residual \(H_{ij}=W_{ij}-\mu-r_i-c_j\). If \(Z_W=\sum_{ij}W_{ij}X_{ij}\), then

\[
\mathbb E Z_W=(a+b-1)\mu,
\qquad
\operatorname{Var}(Z_W)
=\frac{b-1}{a}\sum_i r_i^2
+\frac{a-1}{b}\sum_j c_j^2
+\frac{a+b-3}{ab}\sum_{ij}H_{ij}^2.
\]

The exact minimum mean-square error of the best **affine predictor using all individual vertex degrees linearly** is

\[
\frac{a+b-3}{ab}\sum_{ij}H_{ij}^2.
\]

For any nonzero centered weight matrix \(W\) (so \(\mu=0\)), the sharp extremal bounds are

\[
\frac{\min(a,b)-1}{ab}\lVert W\rVert_F^2
\le \operatorname{Var}(Z_W)
\le \frac{a+b-3}{ab}\lVert W\rVert_F^2.
\]

Both equality cases exist, including on the boundary \(a=2\) or \(b=2\), by taking weights in the appropriate covariance eigenspaces. The condition number of the nonzero covariance spectrum is exactly \((a+b-3)/(\min(a,b)-1)\): it approaches \(2\) when \(a=b\to\infty\), but diverges linearly when one part is fixed and the other increases.

## Assumptions and scope

The law is uniform on *unweighted* spanning trees of \(K_{a,b}\). All edges are distinguished and all deterministic cost weights may be arbitrary real numbers, including negative numbers. Both sides must have at least two vertices. The covariance and prediction statements are finite-size identities for **all** admissible \(a,b\), not asymptotic approximations. Projection onto vertex-degree statistics is explicitly an *affine/linear* least-squares projection; nothing is claimed about optimal nonlinear prediction from the degrees.

## Proof

Orient every graph edge from left to right. Let \(B\) be the vertex-by-edge oriented incidence matrix, \(L=BB^{\mathsf T}\) its Laplacian, and \(L^+\) the Moore–Penrose pseudoinverse. The classical transfer-current theorem states that the uniform spanning-tree edge set is determinantal with edge kernel \(K=B^{\mathsf T}L^+B\). In particular, for different edges \(e,f\),

\[
\mathbb E[X_eX_f]=K_{ee}K_{ff}-K_{ef}^2,
\qquad
\operatorname{Cov}(X_e,X_f)=-K_{ef}^2.
\]

The identity for coinciding edges is \(\operatorname{Var}(X_e)=K_{ee}(1-K_{ee})\). We use only the transfer-current theorem, not any unproved model-specific correlation formula.

The vertex Laplacian of \(K_{a,b}\) acts as multiplication by \(b\) on left-side zero-sum vectors, by \(a\) on right-side zero-sum vectors, and by \(a+b\) on the one-dimensional contrast of the two parts. Decompose each oriented edge incidence vector accordingly. Direct evaluation of \(B^{\mathsf T}L^+B\) gives, for all left vertices \(i,k\) and right vertices \(j,\ell\),

\[
K_{(i,j),(k,\ell)}
=\frac{\mathbf 1_{\{i=k\}}}{b}
 +\frac{\mathbf 1_{\{j=\ell\}}}{a}
 -\frac1{ab}.
\]

In particular, \(p=\mathbb P(X_{ij}=1)=(a+b-1)/(ab)\). Writing \(C=\operatorname{Cov}(X)\), its diagonal entry is \(d=p(1-p)\). Distinct edges in the same row have covariance \(-((a-1)/(ab))^2\); distinct edges in the same column have covariance \(-((b-1)/(ab))^2\); and edges in different rows and columns have covariance \(-1/(ab)^2\).

Let \(J_a\) and \(J_b\) be all-ones matrices and \(I_a,I_b\) identities. Four mutually orthogonal projectors on the edge-array space are

\[
P_0=\frac{J_a}{a}\otimes\frac{J_b}{b},\quad
P_R=\left(I_a-\frac{J_a}{a}\right)\otimes\frac{J_b}{b},\quad
P_C=\frac{J_a}{a}\otimes\left(I_b-\frac{J_b}{b}\right),\quad
P_H=\left(I_a-\frac{J_a}{a}\right)\otimes\left(I_b-\frac{J_b}{b}\right).
\]

Substituting the four possible entries \(d\), same-row, same-column, and disjoint-row-and-column into these projectors, and simplifying, yields the **exact matrix identity**

\[
C=\frac{b-1}{ab}P_R
+\frac{a-1}{ab}P_C
+\frac{a+b-3}{ab}P_H.
\]

This establishes all eigenvalues and multiplicities, including the zero constant direction. Because \(a,b\ge2\), all three displayed coefficients are positive. The row-column-interaction decomposition \(W=\mu\mathbf1+R+C+H\) is the orthogonal decomposition determined by these projectors. Taking the quadratic form \(\langle W,CW\rangle\) and noting \(\lVert R\rVert_F^2=b\sum_i r_i^2\), \(\lVert C\rVert_F^2=a\sum_j c_j^2\) proves the cost-variance identity.

The linear span of the centered left and right vertex-degree counts is exactly the row-plus-column contrast space in the random edge indicators. Since the interaction eigenspace is orthogonal to that space, the orthogonal projection onto all affine degree predictors retains precisely the constant, row, and column components. The residual is the interaction part, with squared norm in \(L^2\) equal to \(((a+b-3)/(ab))\sum_{ij}H_{ij}^2\). This establishes the predictor statement without asserting conditional independence.

Finally, on the mean-zero weight space the eigenvalues lie between the smallest of the row/column eigenvalues and the interaction eigenvalue: \(a+b-3\ge a-1,b-1\). The spectral theorem gives the stated sharp bounds; choosing nonzero weights in the corresponding eigenspaces attains each boundary. At \(a=2\), interaction and row eigenspaces share the maximum; at \(b=2\), interaction and column eigenspaces share the maximum. At \(a=b=2\), all nonconstant eigenspaces have the same eigenvalue. The condition number follows immediately, and its two limiting regimes follow by elementary division.

## Verification

The accompanying dependency-free Python program `verify_covariance.py` constructs every spanning tree of \(K_{a,b}\) for \((a,b)=(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\), yielding \(4657\) enumerated trees in total. It reconstructs the covariance from the uniform distribution with exact rational arithmetic, checks \(597\) covariance entries against the stated matrix identity, and performs \(2388\) projector/eigenrelation entry checks. It also independently compares cost variance from the list of tree weights with the matrix quadratic form. All checks passed on the shipped source code.

The program tests finitely many small graphs only. The proof for arbitrary \(a,b\) is the preceding transfer-current computation plus an exact projector identity.

## Relationship to prior work

Burton and Pemantle established the general transfer-current/determinantal representation for edge-membership events in a uniform spanning tree. It is the critical known input here, **not** a new result of this note. The contribution assessed here is the completely evaluated covariance spectrum of the specific random-edge vector on \(K_{a,b}\), together with the arbitrary-cost variance decomposition, sharp extremizers, and exact linear-degree prediction residual.

The spanning-tree enumerations and degree-generating polynomials for complete multipartite graphs studied by Eğecioğlu and Remmel, and the vertex-product weighted enumerators revisited by Klee and Stamps, supply related enumeration results, but are distinct from the evaluated edge-incidence covariance spectrum. Rapoport develops general joint degree fields via fermionic representations, again with a different observable. General determinantal formulas make the calculation possible; the claimed finite-size spectral factorization and its sharp all-weight consequences are the additional explicit evaluation.

## Limitations

The result is restricted to a complete **bipartite** base graph with equal tree weights. It does not address nonuniform spanning-tree laws, general multipartite graphs with three or more parts, nonlinear conditioning on degrees, or non-Gaussian/asymptotic laws for weighted tree costs. Exact reproducibility and the general transfer-current theorem do not by themselves establish historical originality; prior implicit derivations in the wider spanning-tree literature remain a risk.

## References

1. R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, Annals of Probability 21 (1993), 1329–1371; openly available preprint https://arxiv.org/abs/math/0404048 (initial arXiv posting 2004-04-02).
2. Ö. Eğecioğlu and J. B. Remmel, *A Bijection for Spanning Trees of Complete Multipartite Graphs*, full text https://sites.cs.ucsb.edu/~omer/DOWNLOADABLE/multipartite94.pdf.
3. S. Klee and M. T. Stamps, *Linear Algebraic Techniques for Weighted Spanning Tree Enumeration*, https://arxiv.org/abs/1903.03575 (initial posting 2019-02-27).
4. A. Rapoport, *Correlations in Uniform Spanning Trees: a Fermionic Approach*, Journal of Statistical Physics 192 (2025), article 145, https://pmc.ncbi.nlm.nih.gov/articles/PMC12535553/.
