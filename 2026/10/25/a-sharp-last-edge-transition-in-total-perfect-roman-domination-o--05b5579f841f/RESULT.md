# A sharp last-edge transition in total perfect Roman domination of matching-deleted bicliques

## Finding
For integers \(n\ge3\) and \(0\le k\le n\), let \(G_{n,k}\) be obtained from \(K_{n,n}\), with parts \(A=\{a_1,\dots,a_n\}\) and \(B=\{b_1,\dots,b_n\}\), by deleting exactly the edges \(a_ib_i\) for \(1\le i\le k\). Write \(\gamma_{tR}^{p}(G)\) for the total perfect Roman domination number and \(Q(G)\) for the number of minimum-weight functions on the fixed labeled graph. Then
\[
\gamma_{tR}^{p}(G_{n,k})=\begin{cases}4,&0\le k<n,\\6,&k=n,\end{cases}\qquad
Q(G_{n,k})=\begin{cases}(n-k)^2,&0\le k<n,\\ n^2(n-1)+13\mathbf1_{\{n=3\}},&k=n.\end{cases}
\]
Thus deleting the last edge of a perfect matching raises the optimum by exactly two, while changing the census from one optimum to \(n^2(n-1)\) (or \(31\) when \(n=3\)).

Every minimum function is explicitly classified. For \(k<n\), choose indices \(i,j>k\), label \(a_i,b_j\) by \(2\), and label every other vertex by \(0\). For \(k=n\) and \(n\ge4\), the minimum functions are precisely these two types, all unspecified vertices labeled \(0\):

* Type M: for any \(i\), place \(2\) at \(a_i,b_i\) and \(1\) at \(a_u,b_v\), where \(u,v\ne i\). There are \(n(n-1)^2\) choices.
* Type X: for distinct \(i,j\), place \(2\) at \(a_i,b_j\) and \(1\) at \(a_j,b_i\). There are \(n(n-1)\) choices.

For \(n=k=3\), these types remain, and there are exactly thirteen additional minimum functions: the all-one function and twelve functions with exactly one label \(2\). For each vertex \(a_i\) labeled \(2\), label both other vertices of \(A\) by \(1\) and label \(b_i,b_j\) by \(1\), for one choice \(j\ne i\), leaving the remaining \(B\) vertex at zero. Include the six analogous functions with \(A\) and \(B\) exchanged.

## Assumptions and scope
All graphs are finite, simple and undirected. A **total perfect Roman dominating function** (TPRDF) is \(f:V(G)\to\{0,1,2\}\) such that (i) every zero-labeled vertex has **exactly one** neighbor labeled \(2\) and (ii) every positive-labeled vertex has a positive-labeled neighbor. Equivalently the positive-induced subgraph has minimum degree at least one. Its weight is \(\omega(f)=\sum_{v\in V(G)}f(v)\). The theorem holds for every integer \(n\ge3\), including the small boundary \(n=3\), and every matching-deletion length \(0\le k\le n\), with labeled vertices kept distinct for counting.

## Proof
**The case \(k<n\).** The vertices with indices \(i>k\) have every opposite-part neighbor. Hence putting \(2\) on \(a_i,b_j\) for \(i,j>k\) and zero elsewhere is valid: the positive support is an edge and each zero sees exactly one \(2\). This gives weight four.

A valid function with no \(2\) must label every vertex positively, yielding weight at least \(2n\ge6\). With exactly one \(2\), say at \(a_i\), the other \(n-1\) vertices of \(A\) cannot be zero, and some vertex of \(B\) must be positive to give \(a_i\) a positive neighbor. Thus weight is at least \(2+(n-1)+1=n+2\ge5\). At least two labels \(2\) cost four, so the optimum is four. An optimum must therefore have exactly two labels \(2\), no labels \(1\). To avoid isolated positive vertices, the two \(2\)-vertices must be in opposite parts and adjacent. Write them as \(a_i,b_j\). Every remaining vertex must see exactly one \(2\). If \(i\le k\), then \(b_i\) is a zero that cannot see \(a_i\), unless \(j=i\), but \(a_i b_i\) would then be a deleted edge; hence \(i>k\). Symmetrically \(j>k\). This gives precisely \((n-k)^2\) optima.

**The crown case \(k=n\): an upper bound and structural reductions.** Here \(a_i\) and \(b_i\) are the unique nonadjacent opposite-part pair for index \(i\). Put \(2\) on \(a_i,b_i\), and put \(1\) on \(a_u,b_v\) with \(u,v\ne i\). All four positive vertices have positive neighbors, and each zero has exactly one \(2\)-neighbor. This is Type M with weight six. If \(i\ne j\), put \(2\) on \(a_i,b_j\) and \(1\) on \(a_j,b_i\); this is Type X, also valid and of weight six.

We classify all functions of weight at most six by the number \(T\) of vertices labeled \(2\). If \(T=0\), all \(2n\) vertices must be labeled \(1\), which has weight at least six, with equality only for \(n=3\). If \(T=1\), suppose \(a_i\) has label \(2\). Every other vertex in \(A\) must be positive (no \(2\) lies in \(B\)). The nonneighbor \(b_i\) must also be positive. To ensure that \(a_i\) has a positive neighbor, some \(b_j\) with \(j\ne i\) must be positive. Consequently the weight is at least \(2+(n-1)+2=n+3\); equality with six occurs only for \(n=3\), with exactly the six functions just described for \(A\), and six more on swapping the parts.

If \(T=2\) and the two \(2\)'s lie in the same part, say \(a_i,a_j\), every other vertex of \(A\) must be positive, and every \(b_\ell\) with \(\ell\notin\{i,j\}\) must be positive because it sees both \(2\)'s and therefore cannot be zero. The weight is at least \(4+2(n-2)=2n\). For \(n\ge4\) this is at least eight. When \(n=3\), the only possible weight-six pattern forces the remaining \(a_\ell,b_\ell\) to be \(1\) and all other \(B\)-vertices to be zero; then \(a_\ell\) has no positive neighbor, contradicting totality. Thus no such function can have weight six.

If \(T=2\) with the two \(2\)'s in opposite parts, say \(a_i,b_j\), then for \(i=j\) they are nonadjacent, and each requires an additional positive neighbor in the opposite part, necessarily indices different from \(i\); achieving weight six forces exactly Type M. For \(i\ne j\), zero labels at \(a_j\) and \(b_i\) would have no \(2\)-neighbor, so these two vertices must be positive. Weight six forces exactly their label \(1\), giving Type X.

If \(T=3\) and weight is at most six, all three positive vertices must have label \(2\), all others zero, and their induced subgraph must have no isolated vertex. Three twos in one part are isolated. Otherwise two lie in one side, say \(a_i,a_j\), and the third is \(b_\ell\). For the two \(A\)-vertices to have positive neighbors, \(\ell\ne i,j\). But then the zero \(a_\ell\) is nonadjacent to the sole \(B\)-vertex labeled \(2\), so it has no \(2\)-neighbor. This is impossible. Finally \(T\ge4\) costs at least eight. Thus the only weight-six configurations are exactly the stated types and the thirteen \(n=3\) exceptions; in particular there are no lower-weight configurations.

Counting Type M gives \(n(n-1)^2\), counting Type X gives \(n(n-1)\), and their supports and labels distinguish them. Their sum is \(n^2(n-1)\). When \(n=3\), the all-one function and the twelve one-\(2\) functions increase the census by thirteen. This completes the proof. \(\square\)

## Verification
The accompanying standalone `verify_transition.py` (Python 3.8+, standard library only) constructs the adjacency list for each graph directly and enumerates every labeling of total weight at most six without assuming the theorem. It separately generates all asserted minimum configurations and compares them as exact labeled vertex assignments, as well as checking each optimal value and coefficient. Run `python3 verify_transition.py`; a successful run ends with `VERIFY_OK 39 n,k cases` for every \(3\le n\le8\) and \(0\le k\le n\). This finite verification corroborates the proof but is not the proof of the infinite statement.

## Relationship to prior work
Almulhim (2023) studies total perfect Roman domination and formulates precisely the joint requirements of a unique \(2\)-neighbor for every zero and a positive-induced graph with no isolates. It gives results for complete multipartite graphs, but deleting a matching from a complete bipartite graph changes the zero constraints and takes the graph outside the complete-multipartite family, so those formulas do not imply the transition or the optimizer census.

A separate published online result, *Perfect Roman domination of crown graphs* (2026), proves \(\gamma_R^p(K_{n,n}-M)=4\) and exactly \(n\) optimum functions **without** imposing the positive-support totality condition. Its weight-four extremizers have two \(2\)'s on a deleted matching pair, which are isolated from each other in the positive support, and hence violate the total condition. Thus neither the optimum six nor its optimizer count follows from that result. Related formulas for ordinary total Roman domination and for perfect Roman domination on complete multipartite graphs likewise use different conditions.

## Limitations
The theorem is restricted to deletion of a matching from balanced complete bipartite graphs, with \(n\ge3\). It does not determine full weight polynomials, other graph perturbations, or unbalanced two-part graphs. Numerical checks stop at \(n=8\); the proof is independent of that cutoff. The priority comparison covers identified indexed sources and relevant accessible full texts; an unindexed treatment of total perfect Roman domination on crown or matching-deleted bipartite graphs could still overlap.

## References
1. A. Almulhim, “Total Perfect Roman Domination,” *Symmetry* **15** (2023), article 1676, DOI: 10.3390/sym15091676, published August 31, 2023, https://www.mdpi.com/2073-8994/15/9/1676.
2. “Perfect Roman domination of crown graphs,” public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-perfect-roman-domination-of-crown-graphs--e57b781e4a71. Note this concerns perfect, not total perfect, Roman domination.
3. S. Banerjee, J. M. Keil, and D. Pradhan, “Perfect Roman domination in graphs,” *Theoretical Computer Science* **796** (2019), 1–21, DOI: 10.1016/j.tcs.2019.08.017.
