# Laplacian factorization and spanning-tree complexity of second partial permutohedra

## Finding

Let \(m\ge3\), and let \(G_m\) be the undirected one-skeleton of the partial permutohedron \(\mathcal P(m,2)\). Write \(L_m\) for the **combinatorial** graph Laplacian (diagonal entries are degrees; adjacent off-diagonal entries are \(-1\)). Its full characteristic polynomial is

\[
\begin{aligned}
\det(tI-L_m)={}&t\left[t^2-(2m+1)t+(m^2+1)\right]\\
&\cdot\left[t^3-(2m+3)t^2+(m^2+4m+3)t-(m^2+2m+2)\right]^{m-1}\\
&\cdot(t-m)^{m(m-3)/2}(t-m-2)^{(m-1)(m-2)/2}.
\end{aligned}
\]

In particular, the exact number of **undirected, unweighted, labeled-vertex** spanning trees of \(G_m\) is

\[
\boxed{\tau(G_m)=m^{m(m-3)/2}(m+2)^{(m-1)(m-2)/2}(m^2+2m+2)^{m-1}.}
\]

Moreover the algebraic connectivity \(\lambda_2(G_m)\) is the unique root in \((1,2)\) of the displayed cubic factor. It satisfies \(1<\lambda_2(G_m)<1+1/m\), so it tends to \(1\) even though \(G_m\) is \(m\)-regular. These are simultaneous consequences of the full factorization, not separate hypotheses.

## Assumptions and scope

The partial permutohedron is defined as the convex hull of vectors in \(\{0,1,2\}^m\) whose nonzero entries are distinct. Its explicit halfspace description, already known from the literature, is

\[
\mathcal P(m,2)=\{x\in\mathbb R^m:0\le x_i\le2\ (1\le i\le m),\ \sum_{i=1}^{m}x_i\le3\}.
\]

We assume the integer \(m\ge3\); no asymptotic or generic-position hypothesis is needed. Its \(m^2+1\) vertices have exactly three types: \(o=0\), \(a_i=2e_i\), and \(b_{ij}=2e_i+e_j\) for distinct indices \(i,j\in\{1,\ldots,m\}\). In the two smallest excluded cases, the resulting graphs are respectively a single edge for \(m=1\) and a five-cycle for \(m=2\); their spanning-tree numbers are respectively \(1\) and \(5\). The factors with exponent \(m(m-3)/2\) therefore are not asserted at \(m<3\).

## Proof

**1. Recover the exact graph without relying on a picture.** At each displayed vertex, exactly \(m\) independent inequalities from the halfspace description are active. The polytope is simple. Two vertices are adjacent exactly when they share \(m-1\) facets. Checking the active coordinates and the sum facet yields *all* edges, with no duplicates:

\[
o\sim a_i,\qquad a_i\sim b_{ij},\qquad b_{ij}\sim b_{ik}\quad(j\ne k,\ j,k\ne i),\qquad b_{ij}\sim b_{ji}\quad(i\ne j).
\]

No other vertex pairs share \(m-1\) facets. Every graph vertex has degree \(m\), confirming that \(|V(G_m)|=m^2+1\). In particular the graph is connected (every \(b_{ij}\) links via \(a_i\) to \(o\)).

**2. Write the Laplacian on coordinates.** For a real vector on graph vertices, write its entries as \(w\) at \(o\), \(a_i\) at \(a_i\), and \(B_{ij}\) at \(b_{ij}\), with \(B_{ii}=0\) by convention. Set \(r_i=\sum_{j\ne i}B_{ij}\). The edge list gives the exact linear formulas

\[
\begin{aligned}
(L_m B)_{ij}&=(m+1)B_{ij}-B_{ji}-r_i-a_i,\\
(L_m a)_i&=ma_i-w-r_i,\\
L_mw&=mw-\sum_i a_i.
\end{aligned}
\]

**3. Zero-row/column part.** Let \(U\) consist of arrays with every row sum and every column sum zero, extended by zero at hub and origin coordinates. This is \(L_m\)-invariant. On \(U\), the operator is \((m+1)I-\mathsf T\), where \(\mathsf T\) interchanges \(B_{ij}\) and \(B_{ji}\). The symmetric arrays in \(U\) have dimension \(\binom m2-m=m(m-3)/2\) (the symmetric row-sum constraints are independent because the complete graph with \(m\ge3\) contains an odd cycle). They have eigenvalue \(m\). The skew-symmetric arrays have dimension \(\binom m2-(m-1)=(m-1)(m-2)/2\) (the row-sum map is an oriented incidence matrix of rank \(m-1\)). They have eigenvalue \(m+2\). Symmetric and skew-symmetric parts are orthogonal and exhaust \(U\).

**4. The remaining invariant subspace.** The orthogonal complement to the zero-row/column space among the \(B\)-coordinates consists exactly of matrices \(B_{ij}=x_i+y_j\) for \(i\ne j\). It splits into a scalar constant \(b\) and two zero-sum families \(\sum_i x_i=\sum_i y_i=0\). Include the \(m\) hub coordinates and origin \(w\). For constant entries \(B_{ij}=b\) and \(a_i=a\), the Laplacian acts on \((b,a,w)\) by

\[
T_m=\begin{pmatrix}1&-1&0\\-(m-1)&m&-1\\0&-m&m\end{pmatrix},
\qquad \det(tI-T_m)=t[t^2-(2m+1)t+(m^2+1)].
\]

For each zero-sum standard coordinate family \(B_{ij}=x_i+y_j\), \(a_i=z_i\), the operator acts simultaneously on the three zero-sum vectors by

\[
(x',y',z')=\big(2x-z,\ -x+(m+1)y,\ -(m-1)x+y+mz\big).
\]

This is the same \(3\)-by-\(3\) matrix on \(m-1\) independent coordinate directions:

\[
M_m=\begin{pmatrix}2&0&-1\\-1&m+1&0\\-(m-1)&1&m\end{pmatrix},
\]

\[
\det(tI-M_m)=t^3-(2m+3)t^2+(m^2+4m+3)t-(m^2+2m+2).
\]

The subspaces above exhaust the graph coordinate space: their dimensions add to

\[
\frac{m(m-3)}2+\frac{(m-1)(m-2)}2+3+3(m-1)=m^2+1.
\]

Multiplying their characteristic polynomials therefore proves the factorization for every integer \(m\ge3\).

**5. Count spanning trees, and locate the first nonzero eigenvalue.** The matrix-tree theorem says that the product of the \(m^2\) nonzero Laplacian eigenvalues, divided by \(m^2+1\), equals the spanning-tree count. The nonzero product of the scalar block is \(m^2+1\), and the product of the three eigenvalues of each standard block is \(m^2+2m+2\). Multiplying these with the two integer eigenvalue contributions gives exactly the boxed product.

To identify the spectral gap, denote the cubic factor by \(C_m(t)\). Direct substitution gives \(C_m(1)=-1\), \(C_m(2)=m(m-2)>0\), and \(C_m(1+1/m)=[m^2(m-2)(m+1)+1]/m^3>0\). Its derivative is positive on \((0,2)\) for \(m\ge3\), since the derivative decreases there and \(C_m'(2)=(m-1)(m-3)\ge0\). Thus it has exactly one root in \((1,1+1/m)\). The smaller root of the quadratic factor is at least \(2\), because the quadratic decreases on \((0,2)\) and its value at \(2\) is \((m-1)(m-3)\ge0\). All remaining roots are at least \(m\ge3\), or are larger roots of the cubic. Therefore this cubic root is precisely \(\lambda_2(G_m)\).

## Verification

Run the included standalone file `verify.py` using `python3 verify.py`. It uses only integer arithmetic and the Python standard library. For \(m=3,4,5,6\), a fraction-free integer determinant of a grounded Laplacian agrees with the closed spanning-tree count. For \(m=3,4\), determinants of \(tI-L_m\) agree with the claimed polynomial at \(m^2+2\) distinct integer arguments, respectively \(11\) and \(18\), giving exact complete polynomial equality for those two finite graph sizes. The program also asserts each vertex degree is \(m\). The all-dimensional conclusion follows from Steps 1–5, not these finite computations.

## Relationship to prior work

Heuer and Striker introduced partial permutohedra and described their faces and vertices. Behrend and collaborators' *Partial permutohedra* gives the halfspace model and graph-adjacency information; its Theorem 5.11 evaluates the Ehrhart polynomial and normalized volume in the second-parameter-two family. Those results supply the natural geometric object and a known edge description, but they do not provide the Laplacian characteristic polynomial or an evaluated count of spanning trees. Behrend's subsequent 2024 Ehrhart article focuses on a different range of the second parameter, not Laplacian data. Generic Kirchhoff and spectral formulas supply methods but not the specific factorization established here. Generic clique insertion of all vertices in a graph is distinct from the present operation, which leaves one simplex vertex untruncated.

## Limitations

The theorem concerns the **unweighted graph** of the exact second-parameter-two partial permutohedron, not weighted Euclidean polytope edges or higher second-parameter values. Its primary spectral calculation is not a claim about normalized Laplacians or arbitrary truncation patterns. No assertion of uniqueness across unpublished mathematical work or independent verification is made. An equivalent graph-spectral result under a different name for the partially truncated simplex remains a residual literature-coverage risk.

## References

1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901 (first posted 2020), especially the partial-permutohedron face description. https://arxiv.org/abs/2012.09901
2. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris, and E. Insko, *Partial permutohedra*, arXiv:2207.14253 (first posted 2022-07-28), especially Proposition 5.7, Remark 5.9, and Theorem 5.11. https://arxiv.org/abs/2207.14253
3. R. E. Behrend, *Ehrhart polynomials of partial permutohedra*, arXiv:2403.06975 (first posted 2024-03-11). https://arxiv.org/abs/2403.06975
4. C.-L. Kan and Y.-Y. Tan, *Some Chemistry Indices of Clique-Inserted Graph of a Strongly Regular Graph*, Complexity (2021), DOI:10.1155/2021/7671212 (different graph operation). https://doi.org/10.1155/2021/7671212
