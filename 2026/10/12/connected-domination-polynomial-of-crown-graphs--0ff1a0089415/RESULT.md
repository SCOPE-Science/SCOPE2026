# Connected domination polynomial of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_i\) is the deleted perfect matching. A set \(D\subseteq V(\operatorname{Cr}_n)\) is connected dominating if and only if \(|D\cap A|\ge2\), \(|D\cap B|\ge2\), and it is not the exceptional four-set \(\{a_i,a_j,b_i,b_j\}\) for two distinct indices \(i,j\). Consequently, with \(A_n(x)=(1+x)^n-1-nx\), the connected domination polynomial is
\[
D_c(\operatorname{Cr}_n,x)=A_n(x)^2-\binom{n}{2}x^4.
\]
Equivalently,
\[
d_c(\operatorname{Cr}_n,k)=\sum_{i=\max\{2,k-n\}}^{\min\{n,k-2\}}\binom ni\binom n{k-i}-\mathbf 1_{k=4}\binom n2.
\]
In particular, \(\gamma_c(\operatorname{Cr}_n)=4\), the number of minimum connected dominating sets is \(\binom n2(\binom n2-1)\), and the total number of connected dominating sets is \((2^n-n-1)^2-\binom n2\).

## Assumptions and scope
Graphs are finite, simple, and undirected. For \(n\ge3\), the crown graph \(\operatorname{Cr}_n\) has bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and \(a_i\) is adjacent to \(b_j\) exactly when \(i\ne j\). A connected dominating set is a dominating set whose induced subgraph is connected. The connected domination polynomial is
\[
D_c(G,x)=\sum_D x^{|D|},
\]
where the sum ranges over connected dominating sets.

The scalar value \(\gamma_c(\operatorname{Cr}_n)=4\) is already tabulated in standard graph references; the contribution here is the all-set characterization, every coefficient, the closed polynomial, and the exact number of minimum and total connected dominating sets.

## Proof
Write \(P=\{i:a_i\in D\}\) and \(Q=\{j:b_j\in D\}\), and put \(p=|P|\), \(q=|Q|\).

First, a connected dominating set must have \(p,q\ge2\). Suppose for example that \(q=1\), say \(Q=\{j\}\). To dominate \(a_j\), which is the unique vertex of \(A\) not adjacent to \(b_j\), one must have \(a_j\in D\). But then \(a_j\) has no neighbour in \(D\), because \(b_j\) is the only selected vertex of \(B\); hence \(\operatorname{Cr}_n[D]\) is disconnected. The case \(p=1\) is symmetric, and a connected set cannot have \(p=0\) or \(q=0\).

Conversely assume \(p,q\ge2\). Domination is automatic. If \(a_i\notin D\), at most one selected vertex of \(B\) fails to be adjacent to it, namely \(b_i\); since \(q\ge2\), another selected vertex of \(B\) dominates \(a_i\). The same argument dominates every omitted vertex of \(B\).

It remains to decide connectivity. If \(q\ge3\), any two selected vertices \(a_i,a_j\) have a common selected neighbour \(b_k\) with \(k\notin\{i,j\}\), so all selected vertices of \(A\) lie in one component; every selected vertex of \(B\) has at least one selected neighbour because \(p\ge2\), and therefore the whole induced subgraph is connected. The symmetric argument handles \(p\ge3\). Thus disconnection is possible only when \(p=q=2\). For two-element index sets \(P,Q\), the induced graph is \(K_{2,2}\) with the equal-index edges deleted. It is disconnected exactly when \(P=Q\), when it consists of two independent edges; if \(|P\cap Q|\le1\), it is respectively \(K_{2,2}\) or a three-edge path and is connected. This proves the all-set criterion.

Now every choice of at least two vertices from each shore contributes independently the product
\[
A_n(x)^2=\left((1+x)^n-1-nx\right)^2.
\]
Exactly \(\binom n2\) of its degree-four terms are the disconnected sets with \(P=Q\), so subtracting \(\binom n2x^4\) gives the polynomial. Extracting coefficients gives the displayed coefficient formula. Evaluating at \(x=1\) gives the total count. The degree-four coefficient is
\[
\binom n2^2-\binom n2=\binom n2\left(\binom n2-1\right)>0
\]
for \(n\ge3\), proving the minimum-size and minimum-count statements.

## Verification
The accompanying verifier constructs \(\operatorname{Cr}_n\) directly for \(3\le n\le8\), enumerates every vertex subset, checks domination and induced connectivity from the definitions, and compares every cardinality count with the theorem. It separately checks the structural criterion, the degree-four count, and the total-count formula. This finite census is a stress test only; the all-parameter result follows from the proof above.

## Relationship to prior work
Shao and Zhao's 2026 paper on connected domination polynomials gives the definition, proves a lexicographic-product substitution formula, and studies root density. Its full text treats cycles and joins of cycles as explicit seed families; document-wide searches locate no crown-graph theorem. Its first arXiv version was public on 6 September 2026 and lists primary MSC 05C69.

Mojdeh and Emadi's 2018 paper gives the exact complete-bipartite formula
\[
D_c(K_{m,n},x)=((1+x)^m-1)((1+x)^n-1).
\]
Deleting a perfect matching changes the connected-set structure substantially: in a crown graph no connected dominating set can use only one selected vertex on a shore, and one additional family of balanced four-sets must be removed. Thus the complete-bipartite formula does not imply the stated crown polynomial.

Standard graph tables already record \(\gamma_c(\operatorname{Cr}_n)=4\). The theorem therefore makes no novelty claim for that scalar consequence. Targeted statement-level searches for the crown graph, the matching-deleted complete bipartite graph, and the exact polynomial form found no source giving the all-set classification or the displayed polynomial.

## Limitations
The theorem concerns crown graphs only. It does not classify connected domination polynomials for arbitrary matching deletions \(K_{m,n}-M_t\), for unequal shores, or for other dense bipartite perturbations. The literature comparison located the known scalar connected domination number and the complete-bipartite polynomial, but an older poorly indexed source could still contain the same crown enumerator. The 2018 article was available in indexed full-text extraction around its complete-bipartite theorem, while complete PDF retrieval was not available during this check; that access limitation remains a residual originality risk.

## References
1. P. Shao and C. Zhao, *On the Roots of Connected Domination Polynomials*, arXiv:2609.06569; first version public 6 September 2026.
2. D. A. Mojdeh and A. S. Emadi, *Connected Domination Polynomial of Graphs*, Fasciculi Mathematici 60 (2018), DOI:10.1515/fascmath-2018-0007.
3. E. W. Weisstein, *Connected Domination Number*, MathWorld; the crown-graph entry records connected domination number \(4\).
