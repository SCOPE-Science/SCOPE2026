# Exact Laplacian spectral radius of 2-token complete bipartite graphs

## Finding

For every pair of integers \(m,n\ge 2\), let \(F_2(K_{m,n})\) denote the 2-token graph of the complete bipartite graph \(K_{m,n}\). Its Laplacian spectral radius is
\[
\rho_L(F_2(K_{m,n}))=2(m+n-1).
\]
Consequently, the known lower bound \(\rho_L(F_2(K_{m,n}))\ge 2(m+n-1)\) is attained by every nonstar complete bipartite graph, including every unbalanced one.

## Assumptions and scope

All graphs are finite, simple, and undirected. For a graph \(G\), the 2-token graph \(F_2(G)\) has the 2-subsets of \(V(G)\) as vertices; two such 2-subsets are adjacent when their symmetric difference is an edge of \(G\). The Laplacian spectral radius \(\rho_L(H)\) is the largest eigenvalue of the Laplacian matrix \(L(H)=D(H)-A(H)\).

The theorem assumes \(m,n\ge 2\). The star cases \(K_{1,n}\) are deliberately excluded and are not asserted to satisfy the formula.

## Proof

Write the two shores of \(K_{m,n}\) as \(A\) and \(B\), with \(|A|=m\) and \(|B|=n\). Partition the vertices of \(H=F_2(K_{m,n})\) into
\[
X_A=\binom{A}{2},\qquad Y=\{\{a,b\}:a\in A,\ b\in B\},\qquad X_B=\binom{B}{2}.
\]
Every token move changes the number of tokens lying in \(A\) by one. Hence \(H\) is bipartite, with bipartition \((X_A\cup X_B,Y)\). Because \(m,n\ge2\), these three cells are nonempty, and \(H\) is connected.

Let \(Q=D(H)+A(H)\) be the signless Laplacian. Bipartiteness gives a diagonal signature matrix \(S\) with \(SQS=L(H)\), so \(Q\) and \(L(H)\) are similar and have the same spectral radius.

The partition \((X_A,Y,X_B)\) is equitable for \(Q\). A vertex of \(X_A\) has degree \(2n\) and all its neighbors lie in \(Y\); a vertex of \(Y\) has \(m-1\) neighbors in \(X_A\), degree \(m+n-2\), and \(n-1\) neighbors in \(X_B\); a vertex of \(X_B\) has degree \(2m\) and all its neighbors lie in \(Y\). Therefore the quotient of \(Q\) is
\[
B=
\begin{pmatrix}
2n&2n&0\\
m-1&m+n-2&n-1\\
0&2m&2m
\end{pmatrix}.
\]
Now set
\[
z=
\begin{pmatrix}
n(n-1)\\
(m-1)(n-1)\\
m(m-1)
\end{pmatrix}.
\]
Every entry of \(z\) is positive, and direct multiplication gives
\[
Bz=2(m+n-1)z.
\]
Lifting \(z\) to the vector that is constant with these values on \(X_A,Y,X_B\) gives a strictly positive eigenvector of the nonnegative matrix \(Q\) with eigenvalue \(2(m+n-1)\). Since \(H\) is connected, \(Q\) is irreducible. Perron--Frobenius therefore identifies this eigenvalue with \(\rho(Q)\). Similarity of \(Q\) and \(L(H)\) yields
\[
\rho_L(F_2(K_{m,n}))=2(m+n-1).
\]

## Verification

The accompanying checker verifies the quotient identities exactly for every ordered pair \(2\le m,n\le100\). It also constructs the full 2-token graph for all \(2\le m\le n\le6\), checks its bipartition and connectivity, and verifies exactly that the lifted positive vector is a signless-Laplacian eigenvector with eigenvalue \(2(m+n-1)\). These finite checks stress-test the implementation and boundary cases; the theorem itself is proved for all \(m,n\ge2\) by the argument above.

## Relationship to prior work

Song, Dalfó, Fiol, and Zhang prove for a complete bipartite graph of total order \(N\) that
\[
\rho_L(F_2(K_{m,n}))\ge 2(N-1).
\]
Their Corollary 4.14 gives this lower bound, and Remark 4.15 proves equality for the balanced family. The theorem above shows that the same lower bound is exact for every nonstar complete bipartite graph, including all unbalanced pairs \(m\ne n\).

Reyes, Dalfó, and Fiol develop spectral tools for token graphs and obtain exact Laplacian quotient results for bipartite distance-regular bases. This covers balanced complete bipartite graphs through regularity but does not cover unbalanced \(K_{m,n}\). Earlier work of Deepalakshmi, Marimuthu, Somasundaram, and Arumugam establishes basic 2-token graph structure and terminology but does not give this Laplacian formula.

## Limitations

The result concerns only the 2-token graph and only the Laplacian spectral radius. It does not determine the full Laplacian spectrum, and it does not address \(k\)-token graphs for \(k\ge3\). The star cases \(m=1\) or \(n=1\) are outside the statement. A residual literature risk is that an older result under the aliases “double vertex graph” or “symmetric square” may contain an equivalent unbalanced formula despite not appearing in the inspected sources and targeted searches.

## References

1. Xiaodi Song, Cristina Dalfó, Miquel Àngel Fiol, and Shenggui Zhang, *The Algebraic Connectivity and Laplacian Spectral Radius of Token Graphs*, arXiv:2610.00500v1, first public 2026-09-30.
2. M. A. Reyes, C. Dalfó, and M. A. Fiol, *On the spectra and spectral radii of token graphs*, Boletín de la Sociedad Matemática Mexicana 30 (2024), Article 11, DOI 10.1007/s40590-023-00583-3.
3. J. Deepalakshmi, G. Marimuthu, A. Somasundaram, and S. Arumugam, *On the 2-token graph of a graph*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 265–268, DOI 10.1016/j.akcej.2019.05.002.
