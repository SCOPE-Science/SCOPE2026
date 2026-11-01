# The integral Laplacian spectrum of two-token cocktail-party graphs

## Finding
For every integer \(m\ge 2\), let \(C_m=K_{2,2,\ldots,2}\) be the cocktail-party graph on \(2m\) vertices, partitioned into \(m\) nonadjacent pairs. Let \(T_m=F_2(C_m)\) be its two-token graph: its vertices are unordered pairs of distinct vertices of \(C_m\), adjacent when exactly one token is moved along an edge of \(C_m\) to a vacant vertex.

Write \(q=\binom m2\). The combinatorial Laplacian \(L(T_m)=D-A\), with one edge counted once and no normalization, has characteristic polynomial
\[
\boxed{\det(tI-L(T_m)) = t(t-2m)^{m-1}(t-(2m-2))^m(t-(4m-4))^{m(m-2)}(t-(4m-6))^q(t-(4m-2))^q.}
\]
Coincident eigenvalues in the boundary cases are combined by adding their multiplicities. In particular, the entire Laplacian spectrum is integral, \(T_m\) is connected, and its algebraic connectivity is \(2m-2\). For \(m=2\), that last eigenvalue has multiplicity three; for \(m\ge3\), it has multiplicity \(m\).

The graph has \(m(2m-1)\) vertices and \(4m(m-1)^2\) edges. Its spanning-tree number is exactly
\[
\boxed{\tau(T_m)=\frac{(2m)^{m-1}(2m-2)^m(4m-4)^{m(m-2)}(4m-6)^q(4m-2)^q}{m(2m-1)}.}
\]
For example, \(\tau(T_2)=32\), \(\tau(T_3)=16,986,931,200\), and \(\tau(T_4)=76,724,684,919,725,359,104,000,000\).

## Assumptions and scope
The parameter \(m\) is an arbitrary integer at least two. The graph \(C_m\) is the complete \(m\)-partite graph with exactly two vertices in each part, equivalently \(K_{2m}\) with a fixed perfect matching deleted. All graphs are simple and unweighted. Token configurations are **unordered** two-element subsets, no two tokens may occupy the same vertex, and the move is a single allowed token step. The Laplacian is the unnormalized, unsigned degree-minus-adjacency matrix; the spanning-tree count is for labelled graph vertices corresponding to these token configurations.

## Proof
Label each part \(P_i=\{i^+,i^-\}\) for \(i\in\{1,\ldots,m\}\). There are \(m\) configurations \(a_i=P_i\) and, for each unordered pair \(i<j\), four configurations \(b_{ij}^{\varepsilon\delta}=\{i^\varepsilon,j^\delta\}\), with \(\varepsilon,\delta\in\{+1,-1\}\). Thus \(N=m+4q=m(2m-1)\).

Let \(J=J(2m,2)=F_2(K_{2m})\), and let \(H=F_2(mK_2)\), where \(mK_2\) consists of the deleted edges. Every edge of \(J\) is an edge of exactly one of \(T_m\) and \(H\). Consequently
\[
L(T_m)=L(J)-L(H).
\]
In \(H\), the \(a_i\) are isolated, and each four-element block \(\{b_{ij}^{\varepsilon\delta}\}\) is a square \(C_4\), with transitions flipping one of the two signs. Hence \(L(H)\) has the following mutually perpendicular eigenspaces: the \(0\)-eigenspace \(E_0\) of dimension \(m+q\) (the isolated states and the constant function on each square); the \(2\)-eigenspace \(E_2\) of dimension \(2q\) (the two individual-sign characters on each square); and the \(4\)-eigenspace \(E_4\) of dimension \(q\) (the product-sign character on each square).

Let \(X\) be the \((2m)\)-by-\(N\) unsigned vertex-configuration incidence matrix, with column \(\{u,v\}\) equal to \(e_u+e_v\). Direct entry-counting gives
\[
L(J)=(4m-2)I-X^{\mathsf T}X,\qquad XX^{\mathsf T}=(2m-2)I+\mathbf1\mathbf1^{\mathsf T}.
\]
The latter matrix has eigenvalues \(4m-2\) on the all-ones line and \(2m-2\) on its orthogonal complement. Therefore \(L(J)\) is \(0\) on the one-dimensional constant configuration vector, \(2m\) on the remaining \((2m-1)\)-dimensional part of \(\operatorname{im}(X^{\mathsf T})\), and \(4m-2\) on \(\ker X\).

We now calculate the *joint* decomposition, rather than trying to subtract unordered lists of eigenvalues. On each square form the four orthonormal vectors
\[
c_{ij}=\tfrac12\sum_{\varepsilon,\delta}b_{ij}^{\varepsilon\delta},\quad
s_{ij}^{i}=\tfrac12\sum_{\varepsilon,\delta}\varepsilon b_{ij}^{\varepsilon\delta},\quad
s_{ij}^{j}=\tfrac12\sum_{\varepsilon,\delta}\delta b_{ij}^{\varepsilon\delta},\quad
p_{ij}=\tfrac12\sum_{\varepsilon,\delta}\varepsilon\delta b_{ij}^{\varepsilon\delta}.
\]
Here configuration names denote their coordinate unit vectors. Set \(u_i=e_{i^+}+e_{i^-}\) and \(v_i=e_{i^+}-e_{i^-}\) in vertex-coordinate space. One directly checks
\[
Xa_i=u_i,\qquad Xc_{ij}=u_i+u_j,\qquad Xs_{ij}^{i}=v_i,\qquad Xs_{ij}^{j}=v_j,\qquad Xp_{ij}=0.
\]
The vectors \(u_1,\ldots,u_m\) and \(v_1,\ldots,v_m\) are each independent; the first span the pair-constant vertex space and the second the pair-antisymmetric vertex space. The last display also shows that \(X^{\mathsf T}X\) preserves each of \(E_0,E_2,E_4\): applying \(X^{\mathsf T}\) to a \(u_i\) gives a linear combination of \(a_i,c_{ij}\), and applying it to a \(v_i\) gives a linear combination of the relevant \(s\)-vectors. Thus the three spaces are also invariant for \(L(J)\).

On \(E_0\), the map \(X\) has rank \(m\), its kernel has dimension \(q\), and its image is the pair-constant vertex space. The constant vector gives one \(L(J)\)-eigenvalue \(0\); the other \(m-1\) independent vectors in \(\operatorname{im}(X^{\mathsf T})\cap E_0\) have eigenvalue \(2m\); the \(q\) kernel vectors have eigenvalue \(4m-2\). Subtracting the \(H\)-eigenvalue \(0\) changes none of these.

On \(E_2\), \(X\) has rank \(m\) and kernel dimension \(2q-m=m(m-2)\). Its nonzero image lies in the pair-antisymmetric vertex space, perpendicular to the all-ones vector; hence \(L(J)\) is \(2m\) on an \(m\)-dimensional subspace and \(4m-2\) on its orthogonal complement within \(E_2\). Subtracting the \(H\)-eigenvalue \(2\) produces \(2m-2\) with multiplicity \(m\), and \(4m-4\) with multiplicity \(m(m-2)\).

On \(E_4\) we have \(X=0\), so \(L(J)=4m-2\) and \(L(T_m)=4m-6\), with multiplicity \(q\). Adding the dimensions gives \(1+(m-1)+q+m+m(m-2)+q=N\), so these exhaust the entire spectrum, including \(m=2\) (where the \(E_2\)-kernel dimension is zero). The multiplicity of zero is one, proving connectivity.

The \(m\) same-part states have degree \(4m-4\), while each of the \(4q\) cross-part states has degree \(4m-6\). Half their total degree is \(\tfrac12(m(4m-4)+4q(4m-6))=4m(m-1)^2\), the asserted edge count. The matrix-tree theorem gives the spanning-tree formula by dividing the product of the \(N-1\) nonzero Laplacian eigenvalues by \(N\). The least positive eigenvalue is \(2m-2\), with the noted coincidence at \(m=2\).

## Verification
The two packaged checkers build the token graph from its *actual* allowed moves, with no precomputed adjacency table. The Python program independently enumerates all two-subsets, computes the symmetric Laplacian eigenvalues numerically for \(2\le m\le9\), and compares rounded values and multiplicities with the exact formula; it also calculates exact reduced-Laplacian determinants for \(m=2,3,4\). The C++17 program verifies the predicted multiplicities using exact finite-field nullities of \(L-\lambda I\) and verifies the matrix-tree formula with a separate modular determinant for \(2\le m\le8\), over two prime fields. These finite computations corroborate the general proof but are not used as a substitute for it. Sample exact tree counts above are obtained with integer determinants and independently from the product formula.

## Relationship to prior work
The two-token graph, or *symmetric square*, is a classical object; Audenaert, Godsil, Royle and Rudolph (arXiv:math/0507251, first public 2005-07-12) prove, in particular, that symmetric squares of strongly regular graphs with the same parameters have equal **adjacency** spectra and describe their equitable partitions. The cocktail-party graph is strongly regular, so its symmetric-square adjacency spectral radius also falls within that earlier framework. We do not claim these general structural results or the construction of token graphs as new.

Dalfó and collaborators (arXiv:2012.00808, 2020-12-01), Theorem 6.2, prove that complementary token-graph Laplacians commute and sum to the Johnson Laplacian. The identity \(L(T_m)=L(J)-L(H)\) is therefore previously known in general. What is determined here is the **specific common-eigenspace pairing** for the matching complement, with all six explicit multiplicities and the resulting full spanning-tree product: the general complement theorem alone does not state those multiplicities. Reyes, Dalfó, Fiol and Messegué (arXiv:2309.07089, 2023-09-13) establish the algebraic-connectivity equality for two-token complete multipartite graphs; Dalfó and Fiol (DOI:10.1007/s10801-024-01323-0) also cover the spectral-gap equality for cocktail-party graphs. Thus the scalar spectral gap is established prior work and is included only as a consequence, not as an independent novelty claim. Daoud (DOI:10.3844/ajassp.2012.202.207) calculates spanning-tree complexity for the **original cocktail-party graph**; that is a different graph from its two-token configuration graph, so no value of \(\tau(T_m)\) follows just by identifying the original vertex set. The explicit full Laplacian factorization, joint eigenspace decomposition, and exact configuration-graph tree complexity are the intended contribution.

## Limitations
The theorem concerns exactly two indistinguishable noncolliding tokens on the complete multipartite graph with all parts of size two. It does not give spectra for unequal multipartite parts or larger token numbers, and its spanning-tree count is for the configuration graph, not the original cocktail-party graph. Finite tests are finite corroboration; the proof uses the displayed invariant eigenspace decomposition. Closely related general spectral methods exist and an unindexed special-case calculation may predate this explicit formula. No claim of independent external validation is made.

## References
1. K. Audenaert, C. Godsil, G. Royle, T. Rudolph, *Symmetric Squares of Graphs*, arXiv:math/0507251, first posted 2005-07-12; Journal of Combinatorial Theory, Series B 97 (2007), 74–90.
2. C. Dalfó, F. Duque, R. Fabila-Monroy, M. A. Fiol, C. Huemer, A. L. Trujillo-Negrete, F. J. Zaragoza Martínez, *On the Laplacian spectra of token graphs*, arXiv:2012.00808, first posted 2020-12-01; Theorem 6.2.
3. M. A. Reyes, C. Dalfó, M. A. Fiol, A. Messegué, *On the spectra of token graphs of cycles and other graphs*, arXiv:2309.07089, first posted 2023-09-13; Section 3 and Corollary 3.6.
4. C. Dalfó and M. A. Fiol, *On the algebraic connectivity of some token graphs*, Journal of Algebraic Combinatorics 60 (2024), 45–56, DOI:10.1007/s10801-024-01323-0.
5. S. N. Daoud, *Complexity of Cocktail Party Graph and Crown Graph*, American Journal of Applied Sciences 9 (2012), 202–207, DOI:10.3844/ajassp.2012.202.207.
