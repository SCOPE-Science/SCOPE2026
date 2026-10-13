# All super dominating sets of crown graphs
## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\), with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i\) and \(b_i\) are the deleted matched pair. For \(D\subseteq V(\operatorname{Cr}_n)\), set
\[
I=\{i:a_i\notin D\},\qquad J=\{j:b_j\notin D\}.
\]
Then:

- if \(n=3\), \(D\) is super dominating exactly when \(|I|+|J|\le 2\);
- if \(n\ge4\), \(D\) is super dominating exactly when \(|I|\le2\), \(|J|\le2\), and \(I\cap J=\varnothing\) whenever \(|I|=2\) or \(|J|=2\).

Hence the bivariate enumerator
\[
F_n(u,v)=\sum_D u^{|D\cap A|}v^{|D\cap B|}
\]
over all super dominating sets is, for \(n=3\),
\[
F_3(u,v)=u^3v^3+3(u^2v^3+u^3v^2)+9u^2v^2+3(uv^3+u^3v),
\]
and for \(n\ge4\),
\[
\begin{aligned}
F_n(u,v)={}&u^nv^n+n(u^{n-1}v^n+u^nv^{n-1})+n^2u^{n-1}v^{n-1}\\
&+\binom n2(u^{n-2}v^n+u^nv^{n-2})\\
&+\binom n2(n-2)(u^{n-2}v^{n-1}+u^{n-1}v^{n-2})\\
&+\binom n2\binom{n-2}2u^{n-2}v^{n-2}.
\end{aligned}
\]
Setting \(u=v=x\) gives
\[
D_{sp}(\operatorname{Cr}_3;x)=x^6+6x^5+15x^4,
\]
and, for \(n\ge4\),
\[
D_{sp}(\operatorname{Cr}_n;x)=x^{2n}+2n x^{2n-1}+n(2n-1)x^{2n-2}+n(n-1)(n-2)x^{2n-3}+\frac{n(n-1)(n-2)(n-3)}4x^{2n-4}.
\]
Therefore \(\gamma_{sp}(\operatorname{Cr}_3)=4\) with \(15\) minimum sets. For every \(n\ge4\),
\[
\gamma_{sp}(\operatorname{Cr}_n)=2n-4,
\qquad
N_{sp}(\operatorname{Cr}_n)=\binom n2\binom{n-2}2.
\]
The total number of super dominating sets for \(n\ge4\) is
\[
\frac{n^4-2n^3+7n^2+6n+4}4.
\]

## Assumptions and scope
A super dominating set \(D\) is a set such that for each \(t\notin D\) there is \(d\in D\) with \(N(d)\cap(V\setminus D)=\{t\}\). The theorem concerns simple crown graphs \(K_{n,n}-M_n\) for all integers \(n\ge3\). The six-cycle case \(n=3\) is separated because a one-vertex omitted set on one side can exhaust all possible witnesses when two vertices are omitted on the other side.

## Proof
Let \(T=V\setminus D\). For an omitted vertex \(a_i\), a possible witness must be some selected \(b_j\) with \(j\ne i\). Its omitted neighbors are exactly
\[
N(b_j)\cap T=\{a_k:k\in I,\ k\ne j\}.
\]
For this set to equal \(\{a_i\}\), necessarily \(I\subseteq\{i,j\}\). Hence every super dominating set has \(|I|\le2\). By symmetry, \(|J|\le2\).

If \(I=\{i,k\}\), then \(a_i\) can only be witnessed by \(b_k\), while \(a_k\) can only be witnessed by \(b_i\). Thus both \(b_i\) and \(b_k\) must belong to \(D\), so \(I\cap J=\varnothing\). The same argument with the two sides interchanged shows that \(I\cap J=\varnothing\) whenever \(|J|=2\).

Conversely, assume \(n\ge4\), \(|I|,|J|\le2\), and the stated disjointness condition. If \(I=\{i,k\}\), the selected vertices \(b_k\) and \(b_i\) witness \(a_i\) and \(a_k\), respectively. If \(I=\{i\}\), choose an index \(j\notin J\cup\{i\}\); such a \(j\) exists because \(n\ge4\) and \(|J|\le2\). Then \(b_j\in D\) witnesses \(a_i\). The empty case is vacuous. The symmetric argument handles all omitted vertices in \(B\). This proves sufficiency for \(n\ge4\).

For \(n=3\), the same necessary analysis leaves only a boundary issue: if one side has one omission and the other has two, the unique index outside the two omitted indices on the opposite side is the singleton's own index, hence is nonadjacent and cannot witness it. Thus those profiles fail, while every profile with at most two total omissions passes. This gives \(|I|+|J|\le2\).

The displayed enumerators now follow by counting permissible ordered omission profiles \((I,J)\): sizes \((0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(2,1),(1,2),(2,2)\), with the last three types subject to index disjointness. The minimum-size and total-count formulas are the lowest-degree coefficient and evaluation at \(x=1\), respectively.

## Verification
The proof above is uniform in \(n\). As an independent finite stress test of the classification, `verify_super_crown.py` constructs \(\operatorname{Cr}_n\) directly and tests every vertex subset against the defining private-neighbor condition for \(3\le n\le8\). It then compares the complete bivariate coefficient table with the closed formula and verifies the stated minimum sizes and counts. Replay output:

`VERIFY_OK n_range=3..8 subset_checks=87360 classification_checks=87360 coefficient_checks=51 minimum_checks=6 max_order=16`

This finite replay checks implementation and boundary cases; it is not used as a proof for unbounded \(n\).

## Relationship to prior work
The 2013 foundational paper introduced super domination and gives baseline results for the parameter. A later full-text study, *Super Domination: Graph Classes, Products and Enumeration*, explicitly treats paths, cycles, stars, complete graphs, complete bipartite graphs, and friendship graphs, and begins counting minimum super dominating sets for selected families. Its searchable full text contains no occurrence of “crown” or “perfect matching”; its complete-bipartite result concerns \(K_{n,m}\), not \(K_{n,n}-M_n\). In particular, the known equality \(\gamma_{sp}(K_{n,n})=2n-2\) does not imply the deleted-matching classification here.

A 2024 paper introduces the super domination polynomial and states that explicit formulas are obtained for some graph families. Only its bibliographic record and abstract-level material were available for inspection here, so coverage by an uninspected portion of that chapter remains a residual literature risk. Targeted searches for the crown-graph aliases and the exact deleted-perfect-matching family did not locate a covering statement. The result is therefore presented with that access limitation rather than as an absolute priority claim.

## Limitations
The theorem is specific to crown graphs and does not supply a general deletion formula for super domination polynomials. The computational replay is exhaustive only through order \(16\); the all-order conclusion rests on the symbolic witness argument. The 2024 polynomial chapter was not available in full text during the comparison, so a differently indexed or inaccessible prior formula for crown graphs cannot be completely excluded.

## References
1. M. Lemańska, V. Swaminathan, Y. B. Venkatakrishnan, R. Zuazua, *Super dominating sets in graphs*, arXiv:1309.1315v1, first public version 2013-09-05.
2. D. J. Klein, J. A. Rodríguez-Velázquez, E. Yi, *On the super domination number of graphs*, arXiv:1705.00928; the record lists MSC 05C69 first.
3. M. Ghanbari, T. Jäger, L. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795; later published in *Discrete Applied Mathematics*.
4. P. A. Kaidash, *Super Domination Polynomial of a Graph*, DOI 10.1007/978-3-031-73365-9_6, 2024.
