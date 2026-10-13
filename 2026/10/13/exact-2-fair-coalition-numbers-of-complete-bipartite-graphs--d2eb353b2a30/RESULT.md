# Exact \(2\)-fair coalition numbers of complete bipartite graphs
## Finding
Let \(K_{s,t}\) have bipartition \(X\cup Y\), where \(1\le s=|X|\le t=|Y|\). A set is \(2\)-fair dominating when every vertex outside it has exactly two neighbors in it. The \(2\)-fair coalition number is
\[
C_{2f}(K_{s,t})=
\begin{cases}
4,&(s,t)=(2,2),\\
3,&s=3\text{ and }t\in\{3,4\},\\
s+t-4,&s\ge4,\\
2,&\text{otherwise.}
\end{cases}
\]
Thus the complete-bipartite upper bounds in the initiating \(k\)-fair-coalition paper are sharp for \(s\ge5\), but the boundary family \(K_{4,t}\) has the sharper exact value \(t\), and the \(K_{3,t}\) line has the exceptional values \(3,3,2,2,\ldots\) from \(t=3\) onward.

## Assumptions and scope
Graphs are finite and simple. A \(2\)-fair dominating set \(D\) satisfies \(|N(v)\cap D|=2\) for every \(v\notin D\); the whole vertex set satisfies this condition vacuously. Two disjoint non-\(2\)-fair-dominating sets form a \(2\)-fair coalition when their union is \(2\)-fair dominating. A \(2\)-fair coalition partition is a vertex partition in which every block is either a \(2\)-fair dominating set of cardinality exactly \(2\), or has a coalition partner. The claimed formula covers all integers \(1\le s\le t\).

## Proof
Write an arbitrary set \(D\subseteq V(K_{s,t})\) by its shore occupancies
\[
a=|D\cap X|,\qquad b=|D\cap Y|.
\]
If \(a<s\), then every vertex of \(X\setminus D\) has exactly \(b\) neighbors in \(D\), so \(2\)-fair domination forces \(b=2\). Similarly, if \(b<t\), it forces \(a=2\). Consequently, when \(s,t>2\), every proper \(2\)-fair dominating set has occupancy exactly \((2,2)\).

Suppose now that \(s,t>2\) and a \(2\)-fair coalition partition \(\Pi\) has at least three blocks. No two blocks can have union equal to all of \(V(K_{s,t})\), so every coalition union is a proper \(2\)-fair dominating set. Therefore every block has an occupancy type \((a,b)\in\{0,1,2\}^2\setminus\{(0,0),(2,2)\}\), and it must have a partner of complementary type \((2-a,2-b)\). The possible complementary families are
\[
(0,1)\leftrightarrow(2,1),\quad
(1,0)\leftrightarrow(1,2),\quad
(0,2)\leftrightarrow(2,0),\quad
(1,1)\leftrightarrow(1,1).
\]
In the last family, at least two \((1,1)\)-blocks are needed if that type occurs.

For a block \(B\), put \(e(B)=|B|-1\), and let
\[
E=\sum_{B\in\Pi}e(B)=s+t-|\Pi|.
\]
Assume \(s\ge4\). If no singleton block occurs, every block has size at least two, hence \(|\Pi|\le(s+t)/2\) and, because \(s+t\ge8\), one has \(E\ge4\). If singleton blocks occur on both shores, a \((1,0)\)-singleton requires a \((1,2)\)-partner and a \((0,1)\)-singleton requires a \((2,1)\)-partner; these two size-three blocks already contribute \(2+2=4\) to \(E\). Finally suppose singleton blocks occur on only one shore, say only type \((0,1)\). They require a \((2,1)\)-block, contributing \(2\) to \(E\). If \(E\le3\), at most one further size-two block can occur. Since the total \(X\)-occupancy is at least four, equality would force that further block to contribute two \(X\)-vertices. But a type \((2,0)\) block requires a distinct \((0,2)\) partner, and a type \((1,1)\) block requires another \((1,1)\) block; either requirement raises \(E\) to at least four. This contradiction proves \(E\ge4\), hence
\[
|\Pi|\le s+t-4.
\]
The bound is attained for every \(s\ge4\) by taking one block of type \((2,1)\), one of type \((1,2)\), \(s-3\) singleton blocks of type \((1,0)\), and \(t-3\) singleton blocks of type \((0,1)\). Every \(X\)-singleton partners the \((1,2)\)-block and every \(Y\)-singleton partners the \((2,1)\)-block, while the two size-three blocks themselves have singleton partners because \(s,t\ge4\). Thus \(C_{2f}(K_{s,t})=s+t-4\).

It remains to resolve \(s\le3\). For \(s=3\), any partition with at least three blocks must obey the complementary-type rule above. If a family \((0,1)\leftrightarrow(2,1)\) or \((0,2)\leftrightarrow(2,0)\) occurs, the partner with two \(X\)-vertices leaves only one \(X\)-vertex for all remaining blocks, which cannot support any required complementary pair. Hence only the \((1,0)\leftrightarrow(1,2)\) family or the self-complementary \((1,1)\) family can occur. Three \((1,1)\)-blocks give exactly \((s,t)=(3,3)\). In the other family, the total \(X\)-occupancy three forces one \((1,0)\)-block and two \((1,2)\)-blocks, giving exactly \((s,t)=(3,4)\). Both yield valid three-block partitions. Therefore the value is \(3\) for \(K_{3,3}\) and \(K_{3,4}\), and \(2\) for \(K_{3,t}\) with \(t\ge5\).

For \(s=2<t\), every proper \(2\)-fair dominating set must contain all of \(X\). If a coalition partition had at least three blocks, a coalition union would be proper and would therefore contain both vertices of \(X\). If those vertices lie in distinct blocks, no third block can form such a union with either one; if they lie in the same block, that block is itself \(2\)-fair dominating and cannot be a coalition partner. Thus the maximum is \(2\). For \(K_{2,2}\), all four singletons form a valid four-block partition by pairing the two singletons on each shore. For \(s=1\), every coalition partition has size at most two because any proper \(2\)-fair dominating set would have to contain all degree-one vertices; the exceptional proper set in \(K_{1,2}\) is itself a two-vertex fair block and cannot supply a partner to the remaining singleton. A two-block coalition partition exists in every case, completing the formula.

## Verification
The accompanying `verify.py` independently constructs \(K_{s,t}\), tests the definition of \(2\)-fair domination directly, enumerates all set partitions for every profile with \(s+t\le9\), and compares the exact optimum against the displayed formula. It also checks the explicit infinite-family constructions for all \(4\le s\le t\le40\). The computation is corroborative; the proof above is uniform in \(s,t\).

## Relationship to prior work
Jafari and Alikhani introduced \(k\)-fair coalitions in arXiv:2509.11358v1. Their Theorem 3.3 gives upper bounds for complete bipartite graphs in the nontrivial ranges and exact values on the boundaries \(k=s=t\), \(k=s<t\), and \(k>s\). Specializing their bounds to \(k=2\) does not determine \(K_{3,t}\) or \(K_{4,t}\), and it gives only an upper bound for the large-shore regime. The theorem here closes the \(k=2\) complete-bipartite case exactly. In particular, it shows that the published upper bound \(t+1\) on \(K_{4,t}\) is not tight: the exact value is \(t\).

The ordinary \(k\)-coalition parameter has a different condition—at least \(k\) neighbors rather than exactly \(k\)—and its complete-bipartite formula therefore does not imply this result. Existing fair-domination classifications determine which sets are fair dominating, but do not by themselves solve the coalition-partition extremum.

## Limitations
The result is specific to the \(2\)-fair coalition number. It does not give the full \(k\)-fair coalition number for arbitrary \(k\ge3\), nor does it classify all extremal partitions. The literature comparison found no exact \(2\)-fair complete-bipartite formula beyond the initiating paper's partial bounds, but a poorly indexed equivalent formulation remains a residual bibliographic risk.

## References
1. A. Jafari and S. Alikhani, *\(k\)-Fair Coalitions in Graphs*, arXiv:2509.11358v1, first public 2025-09-14. 2020 MSC: 05C69, 05C85.
2. B. Brešar, M. A. Henning, and B. Samadi, *On \(k\)-coalition in graphs: bounds and exact values*, arXiv:2507.18306v1, 2025. This concerns ordinary \(k\)-coalitions, not the fair variant.
