# Sharp translation threshold for geometric-support Abelian pattern Sturmian words

## Finding
For each integer \(b\ge2\) and each integer \(c\ge-1\), put
\[
E_{b,c}=\{b^j+c:j=0,1,2,\ldots\}\subseteq\mathbb N_0.
\]
Define the bipartite sum-incidence graph \(G(E)\) with left vertices \(L_r\) and right vertices \(R_s\), for \(r,s\in\mathbb N_0\), and with an edge \(L_rR_s\) if and only if \(r+s\in E\). Then
\[
\boxed{G(E_{b,c})\text{ is a forest}\quad\Longleftrightarrow\quad c<b(b-2).}
\]
Equivalently, by the forest characterization of Zeng, Xue and Zeng, the characteristic infinite binary word \(\mathbf1_{E_{b,c}}\) is Abelian pattern Sturmian exactly for those parameters. For each \(c\ge b(b-2)\), a simple cycle of length \(2(b+1)\), involving only the first three support values, gives a finite obstruction. Thus the classification is sharp, and requires no eventual or asymptotic qualifications.

For example, the support \(\{2^j-1:j\ge0\}\) qualifies but \(\{2^j:j\ge0\}\) does not. For base \(3\), the allowed nonnegative offsets are exactly \(0,1,2\); for base \(4\), they are exactly \(0,1,\ldots,7\).

## Assumptions and scope
The base \(b\) and translation \(c\) are integers. The restriction \(c\ge-1\) ensures that *every* translated geometric term is nonnegative, so the support starts at the power with exponent zero; deleting an initial segment of negative terms is a different problem. A forest is an undirected simple graph with no finite cycle. Isolated vertices are allowed. All support sets in the theorem are infinite with infinite complements.

The dynamical terminology follows Zeng, Xue and Zeng, who prove that a binary characteristic word is Abelian pattern Sturmian if and only if its associated bipartite sum-incidence graph is a forest. Their result is an input, not part of the new theorem. The novelty assessed here is the exact two-parameter threshold and its constructive obstruction.

## Proof
Write \(a_j=b^j+c\). These are strictly increasing nonnegative integers. Let \(M_j\) be the set of edges whose endpoint labels sum to \(a_j\). Each \(M_j\) is a matching: for each nonnegative left index \(r\le a_j\), exactly one right index \(a_j-r\) occurs.

**First two levels.** The graph \(M_0\cup M_1\) is a forest. Any cycle in a union of two matchings must alternate between the matchings. Traversing a two-step segment from a left vertex through a right vertex to the next left vertex shifts the left index by the fixed nonzero amount \(a_1-a_0=b-1\), up to choosing one of the two traversal orientations. An alternating cycle has a consistent orientation of the two matching types, hence would repeatedly shift by the same nonzero integer, and could not return. Equivalently, each connected component is a path (possibly a singleton edge), not a cycle.

**Attaching all higher levels below the threshold.** Assume \(c<b(b-2)\). For every \(j\ge1\),
\[
a_{j+1}-2a_j=(b-2)b^j-c>0.
\]
For \(b=2\), the hypothesis forces \(c=-1\), so the displayed inequality also holds. Suppose the edge graph from levels \(0,\ldots,j\) is a forest. Every vertex incident to an old edge has its numerical index at most \(a_j\). Every edge in the next matching \(M_{j+1}\) has endpoint indices summing to \(a_{j+1}>2a_j\), so it has at most one endpoint incident to an old edge. Since \(M_{j+1}\) is itself a matching, all its edges attach new pendant vertices, or form new isolated edges; they cannot create a cycle. Induction proves acyclicity for every finite union of levels. Any cycle in the infinite graph would use finitely many levels, so no such cycle exists.

**Explicit cycles at or above the threshold.** Conversely assume \(c\ge b(b-2)\), and put \(q=b-1\) and \(a=c+1=a_0\). The first three support values are
\[
a_0=a,\qquad a_1=a+q,\qquad a_2=a+(b+1)q.
\]
Define \(b+1\) distinct left vertices \(L_{iq}\) for \(0\le i\le b\), and \(b+1\) distinct right vertices
\[
R_{a-iq}\quad(0\le i<b),\qquad R_{a+q}.
\]
The first \(b\) right indices are nonnegative because
\[
a-(b-1)q=c+1-(b-1)^2\ge0,
\]
and they are pairwise distinct. The final right index \(a+q\) exceeds all the others. For \(0\le i<b\), the edges
\[
L_{iq}R_{a-iq}\in M_0,
\qquad L_{(i+1)q}R_{a-iq}\in M_1
\]
are present. The last right vertex connects \(L_{bq}\) through an edge in \(M_2\), since \(bq+(a+q)=a_2\), and connects \(L_0\) through an edge in \(M_1\). These edges form a simple cycle with \(2(b+1)\) distinct vertices. Thus the graph is not a forest. This also proves the stated obstruction remains valid for every larger translation.

Combining the two directions gives the exact equivalence. Applying the cited forest characterization yields the statement about Abelian maximal pattern complexity. No finite computational testing is used to establish either implication.

## Verification
A standalone, standard-library Python checker (`verify.py`) independently constructs finite incidence graphs with disjoint-set cycle detection and verifies the explicit cycle coordinates, matchings and strict-growth inequalities. It passes 336 exact-integer diagnostic assertions for bases \(2\) through \(8\), translations bracketing the predicted threshold, and finite initial segments. These diagnostics are *not* a proof of the infinitely many cases or of the infinite-word characterization. The preceding graph proof handles all allowed integers and the infinite limit.

## Relationship to prior work
Zeng, Xue and Zeng (2026) characterize Abelian pattern Sturmian characteristic words by forestness of the sum-incidence graph. Their sufficient-growth criterion, Proposition 7.14, establishes forestness when consecutive support elements satisfy a strict doubling condition; their example uses the support \(\{3^j:j\ge0\}\). That sufficient criterion does not determine forestness for every translation: for instance, \(\{3^j+2:j\ge0\}\) violates the strict doubling condition at the first transition, yet is a forest by the theorem above. Nor does a sufficient growth condition give the explicit nonforest cycles or the sharp cutoff.

The published note *Sharp logarithmic support envelope for Abelian pattern Sturmian words* proves a necessary bound on support position and exhibits the extremal support \(\{2^j-1:j\ge0\}\). Such a necessary support bound does not imply this exact translation-by-translation forest classification. Earlier work of Kamae, Widmer and Zamboni introduced Abelian maximal pattern complexity, but does not state the geometric-support threshold in its accessible abstract.

## Limitations
The classification concerns the particular two-parameter support family and the exact infinite graph. It does not classify arbitrary exponentially sparse sets, nonintegral bases or translations that delete negative initial terms. The source theorem identifying forests with Abelian pattern Sturmian words is taken as published; no independent proof of that substantial external theorem is attempted here. The original 2026 arXiv paper's abstract and mathematical statement were available, but its full primary text could not be retrieved in this review; comparisons with its Proposition 7.14 and example used a publicly available mathematical note that quotes and discusses them. An earlier equivalent formulation under additive graph terminology cannot be ruled out, and no independent mathematical audit has been performed.

## References
1. Qingcheng Zeng, Yumei Xue, Cheng Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059v1, first posted 23 September 2026. Forest characterization in the abstract; Proposition 7.14 and Example 7.15 discussed in reference 2.
2. *Sharp logarithmic support envelope for Abelian pattern Sturmian words*, published mathematical record, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-logarithmic-support-envelope-for-abelian-pattern-sturmian--71c60228ce20 (RESULT.md inspected).
3. Teturo Kamae, Steven Widmer, Luca Q. Zamboni, *Abelian maximal pattern complexity of words*, Ergodic Theory and Dynamical Systems 35 (2015), 142–151, first published online 13 August 2013, doi:10.1017/etds.2013.51.
