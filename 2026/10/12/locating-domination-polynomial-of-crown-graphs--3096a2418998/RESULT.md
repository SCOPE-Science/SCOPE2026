# Locating-domination polynomial of crown graphs
## Finding
For every integer \(n\ge5\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_i\) is the deleted matching edge. For \(S\subseteq V(\operatorname{Cr}_n)\), define the omission-index sets
\[I=\{i:a_i\notin S\},\qquad J=\{i:b_i\notin S\}.\]
Then \(S\) is locating-dominating exactly when \(|I\cap J|\le1\) and the two singleton-side domination obstructions are absent: if \(I\ne\varnothing\), the selected vertices in \(B\) are nonempty and, if they equal \(\{b_t\}\), then \(t\notin I\); symmetrically, if \(J\ne\varnothing\), the selected vertices in \(A\) are nonempty and, if they equal \(\{a_t\}\), then \(t\notin J\).

Therefore the bivariate enumerator of all locating-dominating sets is
\[\Lambda_n(x,y)=\sum_S x^{|S\cap A|}y^{|S\cap B|}=(xy+x+y)^n+n(xy+x+y)^{n-1}-n\bigl(x^{n-1}+y^{n-1}+x^{n-1}y+xy^{n-1}\bigr)-n(n-1)\bigl(x^{n-2}y+xy^{n-2}\bigr).\]
Setting \(x=y=z\) gives
\[L_n(z)=(z^2+2z)^n+n(z^2+2z)^{n-1}-2nz^n-2n^2z^{n-1}.\]
In particular,
\[\gamma_L(\operatorname{Cr}_n)=n-1,\qquad N_{\min}=n\bigl(2^{n-1}-2n\bigr),\]
and the total number of locating-dominating sets is
\[(n+3)3^{n-1}-2n(n+1).\]

## Assumptions and scope
The graph is simple and labeled as above, with \(n\ge5\). A locating-dominating set is a dominating set \(S\) such that for distinct vertices \(u,v\notin S\), the open-neighborhood traces \(N(u)\cap S\) and \(N(v)\cap S\) are distinct. The theorem counts labeled vertex sets; it does not quotient by graph automorphisms.

The restriction \(n\ge5\) keeps the minimum-layer statement uniform. The displayed bivariate formula also holds for \(n=4\), but the minimum size there is \(4\), not \(n-1\).

## Proof
For an omitted vertex \(a_i\),
\[N(a_i)\cap S=(B\setminus\{b_j:j\in J\})\setminus\{b_i\}\]
when \(b_i\in S\), while it is simply the selected \(B\)-set when \(b_i\notin S\). Thus two omitted vertices \(a_i,a_k\) have the same trace exactly when both matched partners \(b_i,b_k\) are also omitted. The same statement holds with \(A\) and \(B\) interchanged. Once domination guarantees nonempty traces, an omitted \(A\)-vertex and an omitted \(B\)-vertex cannot collide because their traces lie in disjoint bipartition classes. Hence the locating condition is exactly \(|I\cap J|\le1\).

For domination, if \(I\ne\varnothing\) and at least two vertices of \(B\) are selected, every omitted \(a_i\) has a selected neighbor. If no vertex of \(B\) is selected, domination fails. If the selected \(B\)-set is \(\{b_t\}\), then the unique omitted \(A\)-vertex that this singleton cannot dominate is \(a_t\), so domination is equivalent to \(t\notin I\). The symmetric rule gives the stated classification.

To enumerate, first ignore the domination boundary exceptions. At each matching index there are three states with no double omission: both vertices selected, only \(a_i\) selected, or only \(b_i\) selected, of weights \(xy,x,y\). This contributes \((xy+x+y)^n\). If exactly one index is doubly omitted, choose that index in \(n\) ways and use the same three states on the other indices, giving \(n(xy+x+y)^{n-1}\).

The forbidden domination configurations are disjoint for \(n\ge4\). If no \(B\)-vertex is selected and \(I\ne\varnothing\), the locating condition forces \(I\) to be a singleton, contributing \(nx^{n-1}\). If only \(b_t\) is selected and \(t\in I\), then \(|I\cap J|\le1\) permits either \(I=\{t\}\) or \(I=\{t,i\}\) with \(i\ne t\); these contribute \(nx^{n-1}y+n(n-1)x^{n-2}y\). Subtracting these terms and their symmetric counterparts proves the bivariate formula.

For the minimum size, \(|I\cap J|\le1\) implies
\[|I|+|J|=|I\cup J|+|I\cap J|\le n+1,\]
so \(|S|=2n-|I|-|J|\ge n-1\). Equality forces \(I\cup J=[n]\) and \(|I\cap J|=1\). Domination rules out \(|I|\le2\) and \(|J|\le2\); for \(n\ge5\), all choices with \(3\le |I|\le n-2\) are feasible. With \(|I|=p\), the number is \(n\binom{n-1}{p-1}\), so summing \(p=3,\ldots,n-2\) gives \(n(2^{n-1}-2n)\).

## Verification
The standalone checker reconstructs \(\operatorname{Cr}_n\), independently tests the locating-dominating definition against the omission classification for every subset when \(5\le n\le7\), compares every bivariate coefficient with the closed formula, and checks the minimum and total-count corollaries. It is finite evidence supporting, but not replacing, the symbolic proof.

## Relationship to prior work
Foucaud, Henning, Löwenstein and Sasse study locating-dominating sets in twin-free graphs and prove general upper bounds; their full text notes that bipartite graphs satisfy the half-order conjectural bound through a vertex-cover argument. The crown graph is a canonical twin-free bipartite family of order \(2n\), and the result here sharpens that qualitative bound to \(n-1\) for \(n\ge5\), together with a complete all-set classification and bivariate enumerator. The inspected full text contains no crown-graph or complete-bipartite specialization and does not enumerate locating-dominating sets.

A later paper on locating-dominating sets of regular graphs treats regular graphs whose degree is order minus \(2\) or order minus \(3\). A crown graph \(\operatorname{Cr}_n\) in the claimed range has order \(2n\) and degree \(n-1\), so those theorems do not cover this family. Searches also included the aliases complete bipartite graph minus a perfect matching, Kronecker or canonical double cover of \(K_n\), tensor product \(K_n\times K_2\), and bipartite Kneser graph \(H(n,1)\); no source located in those searches supplied the stated classification or polynomial.

## Limitations
The theorem is only for crown graphs and labeled-set enumeration. It does not classify locating-dominating sets modulo automorphisms. The exact all-order proof is symbolic; exhaustive computation was performed only through \(n=7\). Literature search cannot rule out an unindexed or differently phrased source, especially under the graph's several equivalent names.

## References
1. F. Foucaud, M. A. Henning, C. Löwenstein, T. Sasse, “Locating-dominating sets in twin-free graphs,” arXiv:1412.2376; Discrete Applied Mathematics 200 (2016), 52–58, DOI: 10.1016/j.dam.2015.06.038.
2. F. Foucaud, M. A. Henning, “Locating-Total Dominating Sets in Twin-Free Graphs: a Conjecture,” Electronic Journal of Combinatorics 23(3) (2016), P3.9, DOI: 10.37236/5147. The paper records Mathematics Subject Classification \(05C69\).
3. A. Gafur, “On Locating-Dominating Set of Regular Graphs,” Journal of Mathematics (2021), Article 8147514, DOI: 10.1155/2021/8147514.
