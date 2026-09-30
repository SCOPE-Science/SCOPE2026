# Exact small-order 3AP-intersecting families and a nonprincipal sharp construction
## Finding
Let \(H_n\) be the 3-uniform hypergraph on \([n]=\{1,\ldots,n\}\) whose edges are the non-trivial three-term arithmetic progressions. A family \(\mathcal F\subseteq 2^{[n]}\) is 3AP-intersecting when \(A\cap B\) contains an edge of \(H_n\) for every \(A,B\in\mathcal F\).

For every \(3\le n\le10\),
\[
\max\{|\mathcal F|:\mathcal F\text{ is 3AP-intersecting}\}=2^{n-3}.
\]
Thus the Simonovits--Sós conjectured bound is exact through order ten.

Moreover, every maximum family in this range is of one of the following two forms.

1. A principal 3AP star \(\mathcal S_T=\{A\subseteq[n]:T\subseteq A\}\), where \(T\in E(H_n)\).
2. A pair-majority family. If a pair \(P\subset[n]\) has exactly three distinct completions \(C=\{c_1,c_2,c_3\}\) with \(P\cup\{c_i\}\in E(H_n)\), then
\[
\mathcal M_{P,C}=\{A\subseteq[n]:P\subseteq A,\ |A\cap C|\ge2\}.
\]

The numbers of maximum families for \(n=3,\ldots,10\) are respectively \(1,2,4,6,10,14,19,24\). The nonprincipal counts are \(0,0,0,0,1,2,3,4\). In one-based notation the relevant pairs and completion triples are
\[
\begin{aligned}
\{3,5\}&\to\{1,4,7\},\\
\{4,6\}&\to\{2,5,8\},\\
\{5,7\}&\to\{3,6,9\},\\
\{6,8\}&\to\{4,7,10\},
\end{aligned}
\]
with each row present once its largest displayed point lies in \([n]\).

In particular, the first row gives a nonprincipal family of size \(2^{n-3}\) for every \(n\ge7\), by allowing all coordinates outside \(\{1,3,4,5,7\}\) freely. Hence fixed-3AP stars are not the only possible equality constructions for the conjectured bound.
## Assumptions and scope
A non-trivial three-term arithmetic progression is a set \(\{a,b,c\}\subset[n]\) with \(a<b<c\) and \(a+c=2b\). The quantifier in the definition includes \(A=B\), so each member of a 3AP-intersecting family itself contains a 3AP. The exhaustive classification is asserted only for \(3\le n\le10\). The pair-majority construction is asserted for every \(n\) whenever the stated codegree-three condition holds; the explicit pair \(\{3,5\}\) supplies such a construction for every \(n\ge7\).
## Proof
For the general construction, fix a pair \(P\) with three distinct completion points \(C=\{c_1,c_2,c_3\}\). Each member of \(\mathcal M_{P,C}\) contains \(P\) and at least two elements of \(C\). Any two subsets of a three-element set having size at least two intersect, so for any \(A,B\in\mathcal M_{P,C}\) there is some \(c_i\in A\cap B\cap C\). Therefore \(P\cup\{c_i\}\subseteq A\cap B\) is a 3AP. The pair is forced, four of the eight patterns on \(C\) have size at least two, and all other \(n-5\) coordinates are free, hence
\[
|\mathcal M_{P,C}|=4\cdot2^{n-5}=2^{n-3}.
\]
The family is nonprincipal because its inclusion-minimal members have four elements and no single 3AP is contained in all members.

For \(3\le n\le10\), exact classification is finite. Form a compatibility graph whose vertices are subsets of \([n]\) containing at least one 3AP and whose two distinct vertices \(A,B\) are adjacent exactly when \(A\cap B\) contains a 3AP. The 3AP-intersecting families are precisely the cliques of this graph. The accompanying verifier constructs all progressions directly, builds the complete compatibility graph, and exhaustively enumerates every maximal clique by Bron--Kerbosch search with pivoting. For every \(n\) in the stated range it records the maximum clique size and compares every maximum clique, as an exact set of bit masks, with the union of all principal stars and all pair-majority families arising from codegree-three pairs. There are no unmatched maximum cliques and no unused candidate families.

The exact census is:

| \(n\) | 3APs | maximum size | principal stars | pair-majority | all maximum families |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 1 | 1 | 0 | 1 |
| 4 | 2 | 2 | 2 | 0 | 2 |
| 5 | 4 | 4 | 4 | 0 | 4 |
| 6 | 6 | 8 | 6 | 0 | 6 |
| 7 | 9 | 16 | 9 | 1 | 10 |
| 8 | 12 | 32 | 12 | 2 | 14 |
| 9 | 16 | 64 | 16 | 3 | 19 |
| 10 | 20 | 128 | 20 | 4 | 24 |
## Verification
`verify.py` is a standard-library exhaustive verifier. It reconstructs the 3AP hypergraph and compatibility graph independently from the census data, enumerates all maximal cliques, checks the exact optimum \(2^{n-3}\), checks the family counts, derives codegree-three pairs from the progression list, and checks equality of the enumerated and predicted maximum-family sets. It also directly checks the defining intersection property for every predicted family. A successful replay prints `ALL CHECKS PASSED`.

`census.json` contains only the expected finite census and completion-pair data used for human comparison; the verifier does not read it.
## Relationship to prior work
Keevash's 2026 preprint defines the same 3AP-intersection problem, records the Simonovits--Sós conjecture \(|\mathcal F|\le2^{n-3}\), gives the fixed-3AP star as the evident sharp example, and proves the first non-trivial asymptotic density bound toward that conjecture. The older Chung--Graham--Frankl--Shearer paper is the source to which the Simonovits--Sós conjecture is attributed. The present result supplies exact finite cases through \(n=10\) and identifies additional equality constructions; it does not improve Keevash's general upper bound.
## Limitations
The exhaustive upper bound and equality classification stop at \(n=10\); no claim is made that the two displayed construction types exhaust equality cases for \(n\ge11\). The general conjecture remains open. The finite classification is supported by one complete exhaustive implementation, so independent implementation-level replication has not been performed for the \(n=10\) case. The literature comparison is best-of-knowledge rather than a proof that no unpublished or unindexed treatment exists.
## References
1. Peter Keevash, *A non-trivial bound for 3AP-intersecting families*, arXiv:2609.18870v1, 16 September 2026.
2. Fan R. K. Chung, Ronald L. Graham, Peter Frankl, and James B. Shearer, *Some intersection theorems for ordered sets and graphs*, Journal of Combinatorial Theory, Series A 43 (1986), 23--37, doi:10.1016/0097-3165(86)90019-1.
