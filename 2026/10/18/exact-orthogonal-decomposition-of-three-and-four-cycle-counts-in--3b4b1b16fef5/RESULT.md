# Exact orthogonal decomposition of three- and four-cycle counts in random tournaments

## Finding
Let \(T_n\), \(n\ge4\), be the uniformly random labeled tournament obtained by orienting independently each edge of the complete graph with probability \(1/2\) in each direction. Let \(X_n\) count its directed three-cycles, once per three-element vertex set, and let \(Y_n\) count its directed four-cycles, once per cyclic rotation of a directed circuit (not counting its rotations separately). Then
\[
Y_n-\mathbb E Y_n=\frac{n-3}{2}(X_n-\mathbb E X_n)+R_n,
\]
where \(R_n\) is a sum of **pairwise uncorrelated, identically distributed, locally degenerate** four-vertex terms. Each term is uncorrelated with every directed-three-cycle indicator, not merely with their total.

The exact moments are
\[
\begin{aligned}
\mathbb E X_n&=\tfrac14\binom n3,&\operatorname{Var}(X_n)&=\tfrac3{16}\binom n3,\\
\mathbb E Y_n&=\tfrac38\binom n4,&\operatorname{Var}(Y_n)&=\tfrac3{64}(4n-11)\binom n4,\\
\operatorname{Cov}(X_n,Y_n)&=\tfrac38\binom n4,&\operatorname{Var}(R_n)&=\tfrac3{64}\binom n4.
\end{aligned}
\]
In particular, the exact Pearson correlation is
\[
\operatorname{Corr}(X_n,Y_n)=\sqrt{\frac{4(n-3)}{4n-11}},\qquad
1-\operatorname{Corr}(X_n,Y_n)^2=\frac{1}{4n-11}.
\]
Thus the centered three- and four-cycle counts become asymptotically perfectly correlated, with an *exact* finite-size discrepancy, although their correlation is strictly less than one at every finite \(n\ge4\). The coefficient \((n-3)/2\) is the unique minimum-mean-squared-error linear regression slope of \(Y_n\) on \(X_n\).

## Assumptions and scope
All edge orientations are independent and equiprobable. A directed \(k\)-cycle means a simple directed cycle on \(k\) distinct vertices; directed cyclic rotations are identified, while reversing a cycle is not an identification. On any four-element set there can be at most one directed four-cycle. Both counts are integer valued. The assertions require \(n\ge4\); for \(n=3\) the four-cycle count is identically zero and Pearson correlation is undefined.

For a four-element subset \(S\subseteq[n]\), let \(A_S\) count directed three-cycles among its four triples and let \(B_S\in\{0,1\}\) mark its directed four-cycle. Define
\[
Z_S=B_S-\tfrac12 A_S+\tfrac18,
\qquad R_n=\sum_{S\in\binom{[n]}4}Z_S.
\]
The local degeneracy is the precise conditional statement \(\mathbb E[Z_S\mid T_n[U]]=0\) for every \(U\subset S\) with \(|U|\le3\), where \(T_n[U]\) denotes the oriented induced subgraph. This property, together with independence of disjoint edge sets, yields pairwise orthogonality for distinct \(Z_S\).

## Proof
**1. Exact four-vertex table.** Fix three vertices. Their tournament is either a directed triangle, with probability \(1/4\), or transitive, with probability \(3/4\). Conditioned on a cyclic triple, the fourth vertex creates a directed four-cycle precisely when it beats some but not all of those three vertices: six of the eight possible attachments. The conditional probability is \(3/4\). In all four-vertex tournaments exactly one of the configurations \((A_S,B_S)=(0,0),(1,0),(2,1)\) occurs. Their labeled frequencies among the \(2^6=64\) orientations are respectively \(24,16,24\). In particular, \(\mathbb P(B_S=1)=3/8\), and conditioned on a given transitive triple, \(\mathbb P(B_S=1)=1/4\) by total probability. These assertions can also be checked directly by the four-vertex classification: transitive, cyclic triple with a source or sink, and strongly connected.

**2. Vanishing of lower-order projections.** If \(U\) is a specified triple inside \(S\), put \(I_U=\mathbf1_{\{T_n[U]\text{ is cyclic}\}}\). Every other triple inside \(S\) has conditional cyclic probability \(1/4\) given the orientation on \(U\): its two free edges are fair and independent, whatever the fixed shared edge. Therefore
\[
\mathbb E[A_S\mid T_n[U]]=I_U+\tfrac34.
\]
The four-vertex classification gives
\[
\mathbb E[B_S\mid T_n[U]]=\tfrac14+\tfrac12 I_U.
\]
Subtracting half the first identity from the second and adding \(1/8\) proves \(\mathbb E[Z_S\mid T_n[U]]=0\). Conditional expectation onto smaller vertex subsets also vanishes. The local table gives \(Z_S=1/8\) when \(A_S=0\) or \(2\), and \(Z_S=-3/8\) when \(A_S=1\). Hence \(\mathbb E Z_S=0\) and
\[
\operatorname{Var}(Z_S)=\tfrac34(\tfrac18)^2+\tfrac14(\tfrac38)^2=\tfrac3{64}.
\]

**3. Orthogonality.** Two different four-subsets intersect in at most three vertices. Conditional on the orientations of all edges with both endpoints in the intersection, the edges specific to each subset are independent. Each conditional mean of the respective \(Z\) terms is zero by Step 2. Therefore \(\mathbb E[Z_SZ_{S'}]=0\) whenever \(S\ne S'\). Similarly \(\mathbb E[Z_S(I_U-1/4)]=0\) for *every* triple \(U\): if \(U\subset S\), condition on its three edges; otherwise condition on the edges in \(U\cap S\) and use conditional independence. Consequently
\[
\operatorname{Var}(R_n)=\tfrac3{64}\binom n4,
\qquad \operatorname{Cov}(R_n,X_n)=0.
\]

**4. Exact count decomposition.** Each triple is contained in exactly \(n-3\) four-subsets, so \(\sum_{|S|=4}A_S=(n-3)X_n\), whereas \(\sum_{|S|=4}B_S=Y_n\). Consequently
\[
R_n=Y_n-\tfrac{n-3}{2}X_n+\tfrac18\binom n4.
\]
Since an individual triple is cyclic with probability \(1/4\), \(\mathbb E X_n=\binom n3/4\); similarly \(\mathbb E Y_n=3\binom n4/8\). These means satisfy the centered decomposition claimed above.

**5. Moments and correlation.** Indicators of two *distinct* cyclic triples are uncorrelated: if their vertex sets intersect in two vertices, condition on the orientation of their one common edge, after which the two cyclic events are independent and each has conditional probability \(1/4\). If they intersect in at most one vertex, they depend on disjoint sets of edges. Thus \(\operatorname{Var}(X_n)=\binom n3(1/4)(3/4)=3\binom n3/16\). By Step 3 the decomposition in Step 4 is orthogonal in \(L^2\), giving
\[
\operatorname{Cov}(X_n,Y_n)=\frac{n-3}{2}\operatorname{Var}(X_n)=\frac38\binom n4,
\]
\[
\operatorname{Var}(Y_n)=\frac{(n-3)^2}{4}\operatorname{Var}(X_n)+\operatorname{Var}(R_n)
=\frac3{64}(4n-11)\binom n4.
\]
Division of these strictly positive variances establishes the correlation formula and the optimal linear slope. No asymptotic theorem is required: letting \(n\to\infty\) in the exact expression proves the correlation limit.

## Verification
Run the supplied standard-library-only script as `python3 verify.py`. It enumerates all \(64\) four-vertex tournaments, checks the conditional degeneracy for all four three-vertex subsets and their eight orientations, and exhaustively compares exact means, variances, covariances, residual orthogonality, and correlations for \(n=4,5,6\) (respectively \(64,1024,32768\) complete labeled tournaments). It checks finite algebraic identities for \(4\le n\le100\). These tests corroborate the exact finite calculations but do not substitute for the all-\(n\) proof above.

## Relationship to prior work
Classical work already establishes the **separate** means, variances, and Gaussian limits for the triangle and four-cycle counts: Moran (1947), as presented in Iyer's *Random Tournaments* (2016, Section 2.4.1), gives exactly the marginal variance formulas displayed above. Ribas's 2017 thesis also uses these exact single-count moments in the shifted Turán-sieve treatment (Chapter 5.2). The marginal first- and second-moment formulas and their asymptotic normality are **not** claimed as original here. The contribution assessed here is the *joint* exact covariance/correlation and, more structurally, the locally conditionally mean-zero decomposition into pairwise uncorrelated four-vertex residuals orthogonal to every triangle indicator.

Linial and Morgenstern (arXiv:1405.1576, publicly available May 7, 2014) analyze deterministic extremal constraints between cyclic-three- and four-cycle densities; their Observation 1.2 explicitly counts the four-vertex classes and is acknowledged as earlier coverage of a key elementary combinatorial input. Chan, Grzesik, Král' and Noel (arXiv:1902.00572, publicly available February 1, 2019) sharpen deterministic/extremal density constraints. Ma and Tang (arXiv:2011.14142, first public version November 28, 2020) extend extremal cycle-density comparisons. Those inspected full texts do not state the present finite-size joint covariance or orthogonal residual construction; their deterministic relations do not alone imply the stochastic cross-moment.

Andersson's 1998 paper, *On the asymptotic distributions of subgraph counts in a random tournament*, develops general fluctuation theory and is a particularly relevant historical comparison. Its abstract was accessible but the full paper could not be checked, so an implicit or explicit earlier equivalent cannot be excluded. Generalized U-statistic and orthogonal-projection techniques also provide an established conceptual framework; that framework is not claimed as new.

## Limitations
This is a theorem for **uniform independent orientations** only; it does not assert the same regression or correlation for biased or exchangeable non-independent tournaments. Pairwise uncorrelated four-vertex terms need not be mutually independent. The theorem is an exact identity for the first two joint moments and a local orthogonal decomposition; it is not a claim about the complete joint distribution, a central limit theorem, or historical priority. The full text of Andersson (1998) and of Moran (1947) could not be inspected, leaving specific historical-priority risks. The separate marginal variance and normal-limit formulas are established prior work.

## References
1. T. F. N. Chan, A. Grzesik, D. Král', and J. A. Noel, *Cycles of length three and four in tournaments*, arXiv:1902.00572 (first public version February 1, 2019), https://arxiv.org/abs/1902.00572.
2. J. Ma and T. Tang, *Minimizing cycles in tournaments and normalized \(q\)-norms*, arXiv:2011.14142 (first public version November 28, 2020), https://arxiv.org/abs/2011.14142.
3. N. Linial and A. Morgenstern, *On the number of 4-cycles in a tournament*, arXiv:1405.1576 (first posted May 7, 2014), https://arxiv.org/abs/1405.1576 (full text inspected).
4. T. Iyer, *Random Tournaments* (2016), Section 2.4.1, https://tqft.net/web/research/students/TejasIyer/thesis.pdf (relevant pages inspected; summarizes Moran's classical exact marginal moments).
5. S. Ribas, *Extremal product-one free sequences and the shifted Turán sieve method on tournaments* (2017), Chapter 5.2, https://www.mat.ufmg.br/posgrad/wp-content/uploads/TesesDissertacoes/Tese090.pdf (relevant chapter inspected).
6. P. A. P. Moran, *On the method of paired comparisons*, Biometrika **34** (1947), 363–365, DOI: 10.1093/biomet/34.3-4.363 (cited through Iyer; full text not inspected).
7. P. Andersson, *On the asymptotic distributions of subgraph counts in a random tournament*, Random Structures & Algorithms **13** (1998), 249–260, DOI: 10.1002/(SICI)1098-2418(199810/12)13:3/4<249::AID-RSA4>3.0.CO;2-V (abstract inspected, full text unavailable).
