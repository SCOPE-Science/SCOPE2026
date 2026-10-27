# Signed covariance and precision spectra of uniform acyclic orientations of \(K_{2,n}\)

## Finding

Let \(n\ge2\), and choose uniformly from all acyclic orientations of the complete bipartite graph \(K_{2,n}\). Denote the vertices of the part of size two by \(a,b\), and the other vertices by \(v_1,\ldots,v_n\). Set \(X_{ri}=\mathbf1\{r\to v_i\}\), with \(r\in\{a,b\}\), and arrange the \(2n\) indicators by columns as \((X_{a1},X_{b1},\ldots,X_{an},X_{bn})\). Write \(\Sigma\) for their covariance matrix and \(Q=\Sigma^{-1}\).

Define
\[
Z_n=2\cdot3^n-2^n,\qquad
c_n=\frac{3^{n-1}-2^{n-1}}{2Z_n},\qquad
d_n=\frac{3^{n-2}}{2Z_n},\qquad
s_n=\frac14+c_n.
\]
All three numbers \(Z_n,c_n,d_n\) are positive, and \(c_n+6d_n=1/4\). Every indicator has mean \(1/2\) and variance \(1/4\). The covariances between **distinct** indicators are completely classified:

* same column, different center: \(\operatorname{Cov}(X_{ai},X_{bi})=c_n>0\);
* different columns, same center: \(\operatorname{Cov}(X_{ri},X_{rj})=d_n>0\), for \(i\ne j\);
* different columns, different centers: \(\operatorname{Cov}(X_{ai},X_{bj})=-d_n<0\), for \(i\ne j\).

The positive eigenvalues of \(\Sigma\), with their multiplicities, are
\[
\begin{array}{c|c|c}
\text{eigenspace}&\text{eigenvalue}&\text{multiplicity}\\
\text{columnwise sums}&s_n&n\\
\text{zero-sum columnwise differences}&4d_n&n-1\\
\text{constant columnwise differences}&2(n+2)d_n&1
\end{array}.
\]
In particular, \(\Sigma\) is positive definite. With
\[
A_n=\frac{1}{2s_n},\qquad
B_n=\frac{n+1}{8d_n(n+2)},\qquad
F_n=\frac{1}{8d_n(n+2)},
\]
the **complete inverse covariance matrix** is
\[
Q_{ri,sj}=\begin{cases}
A_n+B_n,&(r,i)=(s,j),\\
A_n-B_n<0,&i=j,\ r\ne s,\\
-F_n<0,&i\ne j,\ r=s,\\
+F_n>0,&i\ne j,\ r\ne s.
\end{cases}
\]
Thus every distinct pair satisfies \(\operatorname{sign}\Sigma_{ef}=-\operatorname{sign}Q_{ef}\), and the sign of the **full-order linear partial correlation** \(-Q_{ef}/\sqrt{Q_{ee}Q_{ff}}\) agrees with its marginal correlation. These are linear residual correlations, not assertions of nonlinear conditional independence.

The classification also shows a mean-field separation. As \(n\to\infty\), the marginal correlation between indicators in different columns tends to \(+1/9\) for the same center and \(-1/9\) for opposite centers. Their full-order linear partial correlations tend to zero, with \(n\)-scaled limits \(+3/4\) and \(-3/4\), respectively. The same-column marginal and partial correlations tend to \(1/3\) and \(1/2\).

## Assumptions and scope

All vertices are labeled and the base graph is the unweighted, complete bipartite graph \(K_{2,n}\). Every admissible **acyclic orientation**, not every ordering of the vertices, receives equal probability. The uniform law is invariant under reversing every edge. All statements are exact for each integer \(n\ge2\). The binary indicators use the common reference direction from the part of size two to the other part; switching a reference direction switches the corresponding signs as expected. No weighted-orientation, arbitrary-bipartite-graph, or nonlinear conditional-independence statement is made.

## Proof

**1. Count admissible configurations.** Encode the two edge directions at leaf \(v_i\) by a binary column \((X_{ai},X_{bi})\). Because every simple undirected cycle of \(K_{2,n}\) has length four, a directed cycle exists exactly when two columns of types \((0,1)\) and \((1,0)\) both occur. Consequently, acyclic configurations are the union of the configurations avoiding \((0,1)\) and those avoiding \((1,0)\). Each avoidance family has \(3^n\) configurations, and their intersection contains precisely the \(2^n\) configurations with columns only \((0,0)\) or \((1,1)\). Inclusion-exclusion gives \(Z_n=2\cdot3^n-2^n\).

**2. Mark one or two indicators.** Global reversal of all arrows exchanges zero and one for every indicator, so each has probability \(1/2\) of being one. If both indicators in the same column are one, that column must be \((1,1)\), and the count is \(2\cdot3^{n-1}-2^{n-1}\). In two specified different columns, the count for both one-indicators referring to the same center is \(5\cdot3^{n-2}-2^{n-2}\): the two avoidance families contribute \(1\cdot3^{n-2}\) and \(4\cdot3^{n-2}\), respectively, with \(2^{n-2}\) counted twice. For different centers in different columns, the count is \(4\cdot3^{n-2}-2^{n-2}\), using contributions \(2\cdot3^{n-2}\) from each avoidance family. Dividing by \(Z_n\) and subtracting \(1/4\) gives precisely the three covariance formulas. Direct substitution proves \(c_n+6d_n=1/4\). For \(n\ge2\), \(3^{n-1}>2^{n-1}\), hence \(c_n,d_n>0\).

**3. Diagonalize all directions.** In the column ordering, the diagonal \(2\times2\) blocks of \(\Sigma\) are \(\left(\begin{smallmatrix}1/4&c_n\\c_n&1/4\end{smallmatrix}\right)\) and every off-diagonal block is \(\left(\begin{smallmatrix}d_n&-d_n\\-d_n&d_n\end{smallmatrix}\right)\). Split each column into its normalized symmetric and antisymmetric vectors \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\). In the symmetric sector the matrix is \(s_n I_n\). In the antisymmetric sector it is \(4d_n I_n+2d_n J_n\), using \(1/4-c_n=6d_n\). The all-one vector and its orthogonal complement give the displayed eigenvalues and multiplicities. All eigenvalues are strictly positive.

**4. Invert and determine signs.** The symmetric-sector inverse is \(s_n^{-1}I_n\). The antisymmetric-sector inverse is
\[
(4d_n I_n+2d_nJ_n)^{-1}=\frac{1}{4d_n}I_n-\frac{1}{4d_n(n+2)}J_n.
\]
Transforming back to the original pairs produces the four entries in the displayed formula for \(Q\). It remains to verify \(A_n-B_n<0\). The diagonal of the antisymmetric-sector inverse is the weighted mean
\[
\frac{n-1}{n}\frac1{4d_n}+\frac1n\frac1{2(n+2)d_n}.
\]
The same weights applied to the two underlying positive eigenvalues yield \(6d_n=1/4-c_n\). Jensen's inequality for the strictly convex map \(x\mapsto1/x\) makes the displayed weighted reciprocal at least \(1/(1/4-c_n)\), strictly larger than \(1/(1/4+c_n)=1/s_n\). Therefore half their difference, \(Q_{ai,bi}=A_n-B_n\), is strictly negative. All other inverse signs follow immediately from \(F_n>0\).

**5. Take the infinite-size limits.** Dividing numerator and denominator by \(3^n\) shows \(c_n\to1/12\), \(d_n\to1/36\), and \(s_n\to1/3\). Consequently \(A_n\to3/2\), \(B_n\to9/2\), \(nF_n\to9/2\), and \(Q_{ee}=A_n+B_n\to6\). The marginal correlation is four times the covariance, while every full-order linear partial correlation equals \(-Q_{ef}/Q_{ee}\). Substitution gives all limiting constants claimed above.

## Verification

The accompanying `verify.py` uses only Python's standard library. It independently tests acyclicity by topological sorting of the *actual directed graph*, rather than relying on the forbidden-column criterion, for all \(4^n\) orientations with \(2\le n\le8\). For each size it checks the acyclic-state count, all exact rational means/covariances, the displayed inverse by exact matrix multiplication, and all signs. It also tests the relevant finite algebraic identities through \(n=100\). A complete execution passes **90,094 exact assertions**. These finite computations are consistency checks; the preceding all-parameter proof establishes the infinite family and asymptotic limits.

Run `python3 verify.py` from the directory containing this result and the checker. No other inputs or dependencies are needed.

## Relationship to prior work

The focal source, Khera and Lundberg (arXiv:2408.12716, first submitted August 22, 2024), studies the distribution of the **longest directed path** in uniform acyclic orientations of complete bipartite graphs, using lonesum matrices and poly-Bernoulli enumeration. It does not state the edge-indicator covariance, its eigenspaces, or its inverse sign law. Carballosa, Khera, and Reyes (arXiv:2303.09021, first submitted March 16, 2023) establish encoding and **counts** for complete multipartite acyclic orientations; those results supply structural context but do not include the present statistical dependence theorem. Cameron's January 6, 2014 Eindhoven slides explain the lonesum-matrix correspondence and explicitly raise questions about edge-orientation correlations; they neither prove the formulas above nor provide an inverse-covariance classification. These references are credited for the model, representation, and counting methods, not claimed as discoveries of this note.

A related published mathematical-result record, *Incidence precision law for all inversion indicators of a random permutation* (published-finding corpus identifier `2026/10/4/SCOPE-incidence-precision-law-for-all-inversion-indicators-of-a-random--f6af0a8c3805`), concerns orientations induced by **uniform total orders** on complete graphs: it has zero covariance for disjoint comparison indicators, unlike the nonzero \(\pm d_n\) correlations here. Neither that statement nor its parameters imply the present uniform-acylclic-orientation law. The database comparison is evidence of nonoverlap, not proof of global historical priority.

## Limitations

The result treats only unweighted, uniformly sampled acyclic orientations of \(K_{2,n}\), not all complete bipartite sizes, biased orientations, or arbitrary DAG ensembles. Positive and negative covariances do not assert a global association property, and precision signs are statements about *linear* partial correlations, not conditional independence. The exact direction-reference convention matters. An earlier specialized two-row lonesum-matrix moment calculation or an implicit derivation through a stronger multivariate enumerator remains a historical-priority risk. No independent mathematical audit has been performed.

## References

1. J. Khera and E. Lundberg, *The distribution of the length of the longest path in random acyclic orientations of a complete bipartite graph*, arXiv:2408.12716 (2024, first public posting August 22, 2024), https://arxiv.org/abs/2408.12716.
2. W. Carballosa, J. Khera, and F. Reyes, *Encoding and Enumerating Acyclic Orientations of Graphs*, arXiv:2303.09021 (first public posting March 16, 2023), https://arxiv.org/abs/2303.09021.
3. P. J. Cameron, *Acyclic orientations*, lecture slides, Eindhoven, January 6, 2014, https://cameroncounts.github.io/web/talks/14/pg_eindhoven.pdf.
4. published-finding corpus mathematical-result record, *Incidence precision law for all inversion indicators of a random permutation*, identifier `2026/10/4/SCOPE-incidence-precision-law-for-all-inversion-indicators-of-a-random--f6af0a8c3805`.
