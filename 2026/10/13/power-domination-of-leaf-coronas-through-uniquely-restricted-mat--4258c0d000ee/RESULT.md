# Power domination of leaf coronas through uniquely restricted matchings

## Finding

Let \(G=(V,E)\) be a finite nonempty simple graph. Its **leaf corona** \(W(G)=G\circ K_1\) has a private leaf \(v'\) adjacent only to each original vertex \(v\in V\). For an initial selected set \(S\subseteq V(W(G))\), put
\[
 R=\{v\in V:v\in S\},\qquad
 L=\{v\in V:v'\in S\},\qquad
 A=L\setminus R,\qquad
 U=V\setminus\bigl(N_G[R]\cup L\bigr).
\]
Here \(N_G[R]\) is the union of closed neighborhoods of vertices of \(R\). Form the bipartite graph \(B_G(A,U)\) on the disjoint parts \(A\) and \(U\), retaining exactly the edges of \(G\) between these parts. A matching is **uniquely restricted** if the graph induced by its saturated vertices has exactly one perfect matching.

**Matching theorem.** For every such \(G\) and every \(S\), the set \(S\) power dominates \(W(G)\) if and only if \(B_G(A,U)\) has a uniquely restricted matching saturating all of \(U\). The empty matching is allowed when \(U=\varnothing\). Thus its entire power-domination polynomial is given by the exact, nonovercounting classification
\[
 \mathcal P(W(G);z)=\sum_{R,L\subseteq V}z^{|R|+|L|}
 \mathbf 1\!\left\{B_G\bigl(L\setminus R,V\setminus(N_G[R]\cup L)\bigr)
 \text{ has a uniquely restricted matching saturating its second part}\right\}.
\]

If \(G\) has **no even cycle**, this condition reduces to the Hall inequalities
\[
 \bigl|N_G(X)\cap A\bigr|\geq |X|\quad\text{for every }X\subseteq U,
\]
because each bipartite graph \(B_G(A,U)\) is then a forest. In particular, when \(G\) is any finite forest, the complete polynomial \(\mathcal P(W(G);z)\) is computable by the constant-width rooted-tree recursion below, in polynomial time, with no enumeration over selected subsets or matchings. These statements together constitute the finding.

## Assumptions and scope

Graphs are finite, undirected, unweighted, simple, and nonempty; disconnected graphs and isolated vertices are permitted. The power-domination process first observes every initially selected vertex and all its neighbors, then repeatedly allows an observed vertex with exactly one unobserved neighbor to observe that neighbor. \(\mathcal P(H;z)=\sum_{S}z^{|S|}\) counts exactly those initial vertex sets \(S\) that eventually observe all of \(H\). The two decisions at each original vertex, selecting \(v\) and selecting \(v'\), are independent. The result is an exact finite-graph theorem, not an asymptotic approximation.

The matching classification holds for arbitrary bases, including ones with even cycles. The Hall simplification applies when the base has no even cycle. The stated polynomial-time implementation is proved only for forest bases, not for all base graphs. In particular, the result does **not** assert a polynomial-time algorithm for arbitrary \(G\).

## Proof

### 1. Where propagation can occur

Fix \(R,L\subseteq V\). Immediately after the initial domination step, the observed original vertices are exactly \(C=N_G[R]\cup L\), while the observed private leaves are exactly those indexed by \(R\cup L\). Every original vertex in \(U=V\setminus C\) therefore has an unobserved private leaf. A vertex of \(R\) has no unobserved original neighbor from the start. A vertex of \(C\setminus (R\cup L)\) retains an unobserved private leaf until all of its original neighbors are observed; consequently it cannot force an unobserved original vertex. The same applies to any original vertex subsequently observed by a force: until its private leaf is observed it cannot force another original vertex, and once its private leaf is observed it has no unobserved original neighbors. A private leaf cannot force an original vertex that is already observed, and no initially unobserved private leaf can help observe an original vertex.

It follows that every force on an initially unobserved original vertex has an agent in \(A=L\setminus R\). Conversely, each vertex of \(A\) is initially observed together with its private leaf, and can force an original vertex as soon as it has exactly one unobserved original neighbor. Once it forces such a vertex, it never forces another one. After all original vertices have become observed, every still-unobserved private leaf is the only unobserved neighbor of its original vertex and can be forced. Thus the entire problem reduces precisely to covering \(U\) by forces from \(A\) along the edges of \(B_G(A,U)\).

### 2. Force sequences and uniquely restricted matchings

Suppose these forces cover \(U\). List them in an order compatible with the process, as \(a_1\to u_1,\ldots,a_t\to u_t\), where \(t=|U|\). Every agent is distinct, so the corresponding edges form a matching \(M\) saturating \(U\). When \(a_i\) forces \(u_i\), none of the later targets \(u_j\) (\(j>i\)) has yet been observed; therefore \(a_i u_j\notin E(G)\). In the biadjacency matrix between the matched agents and the ordered targets, all diagonal entries are one and all entries strictly above the diagonal are zero. A nonidentity perfect matching would yield a nonzero permutation selecting a nonzero entry above the diagonal, which is impossible. Hence \(M\) is uniquely restricted.

Conversely, take a uniquely restricted matching \(M=\{a_i u_i\}_{i=1}^t\) saturating \(U\). Draw a directed arc from \(i\) to \(j\) whenever \(i\neq j\) and \(a_i u_j\) is an edge. A directed cycle would exchange the matched edges along an alternating cycle, creating a second perfect matching on the same endpoints. Hence this digraph is acyclic and has a sink. The agent at a sink is adjacent to exactly its own matched target among the still-unobserved targets, so it may force that target. Remove this matched pair and repeat: unique restriction survives deletion of a matched pair, and a new sink exists. This observes all of \(U\). The remaining private leaves can then be forced. The two implications prove the matching theorem and the displayed all-set polynomial without counting matching witnesses multiple times.

A bipartite cycle has even length. If the base has no even cycle, its subgraph \(B_G(A,U)\) has no cycle, so each of its matchings is uniquely restricted: two distinct perfect matchings on the same saturated vertices would have a cycle in their symmetric difference. Ordinary Hall's marriage theorem then gives the stated inequalities.

For comparison, take the four-cycle \(G=C_4\) with cycle indices \(0,1,2,3\), and choose only the private leaves at indices \(0\) and \(2\). Then \(A=\{0,2\}\), \(U=\{1,3\}\), and \(B_G(A,U)\) is a four-cycle. A matching saturating \(U\) exists, but it is not uniquely restricted; neither observed agent has a unique unobserved neighbor. Thus replacing unique restriction by an arbitrary matching would incorrectly accept this set.

### 3. Constant-width enumerator for forest bases

It is enough to treat one rooted tree \(T\), since power domination and its polynomial factor over components. At each vertex \(v\), write the selection bits \(r_v=\mathbf1_{\{v\in S\}}\) and \(\ell_v=\mathbf1_{\{v'\in S\}}\). Let \(c_v=1\) if any child of \(v\) has its original vertex selected, otherwise \(c_v=0\). If the original parent of \(v\) has selection bit \(\rho\in\{0,1\}\), define the **role** of \(v\):
\[
 t(v;\rho)=
 \begin{cases}
 a,&r_v=0,\ \ell_v=1,\\
 u,&r_v=\ell_v=c_v=\rho=0,\\
 o,&\text{otherwise}.
 \end{cases}
\]
The roles \(a,u,o\) mean respectively eligible agent, unobserved target, and other; they reproduce the sets \(A,U\) of the matching theorem. Write \(m_v^{(\rho)}\subseteq\{0,1\}\) for the feasible number of matching edges from \(v\) to its parent, using edges within the rooted subtree and requiring every target in that subtree to be matched. Feasibility of a parent edge is provisional: compatibility with the parent's role is checked at the parent. Encode each feasibility set by a two-bit mask. The complete subtree interface is
\[
 \sigma_v=\bigl(r_v,\ell_v,c_v,m_v^{(0)},m_v^{(1)}\bigr),
\]
with at most \(2\cdot2\cdot2\cdot4\cdot4=128\) possible states. Its weight polynomial counts selections in the subtree yielding that state, **not** the number of matching witnesses.

The state is computed bottom-up by the following Boolean finite-state transition. Fix \(r_v,\ell_v\). While processing children, maintain the OR \(c\) of their selected-original bits and, for each hypothetical role \(t\in\{o,a,u\}\), a set \(B_t\subseteq\{0,1\}\) of feasible numbers of child edges matched to \(v\). Initially \(c=0\) and \(B_o=B_a=B_u=\{0\}\). For a child \(w\), its state provides \(F=m_w^{(r_v)}\) and its role \(t_w=t(w;r_v)\). Define \(\delta(t,t_w)=1\) exactly when one role is \(a\) and the other is \(u\), and zero otherwise. Update \(c\leftarrow c\lor r_w\). For each \(t\) and \(j\in\{0,1\}\), the new feasible counts satisfy
\[
 \begin{aligned}
 B'_t(0)&=B_t(0)\wedge F(0),\\
 B'_t(1)&=\bigl(B_t(1)\wedge F(0)\bigr)
 \vee\bigl(B_t(0)\wedge F(1)\wedge\delta(t,t_w)\bigr),
 \end{aligned}
\]
where a set evaluated at \(0\) or \(1\) denotes its Boolean membership. Repeat independently across all children. When the last child has been processed, for each \(\rho\in\{0,1\}\) let \(t=t(v;\rho)\); form
\[
 \begin{aligned}
 m_v^{(\rho)}(0)&=
 \begin{cases}
 B_u(1),&t=u,\\
 B_t(0)\vee B_t(1),&t\in\{o,a\},
 \end{cases}\\
 m_v^{(\rho)}(1)&=\mathbf1_{\{t\in\{a,u\}\}}\,B_t(0).
 \end{aligned}
\]
A target must have exactly one incident matching edge; an agent has at most one; an ordinary vertex has none. These are precisely the conditions in the displayed recurrence. At the root there is no parent edge, so retain exactly states with \(0\in m_{\mathrm{root}}^{(0)}\). Multiply the child weight polynomials when combining independently chosen child selections, and add the weight \(z^{r_v+\ell_v}\) at \(v\). Group identical resulting states by **adding** their weight polynomials. In particular, several compatible matchings for a single selected set contribute only a Boolean feasibility value, not multiple polynomial terms. This recursion produces \(\mathcal P(W(T);z)\) exactly.

There are at most \(128\) interface states and at most \(2\cdot4^3=128\) partial child aggregates for fixed local selection bits. Each child update uses only a constant number of state pairs and polynomial additions/multiplications. Polynomials have degree at most twice the number of original vertices; using ordinary polynomial multiplication gives at most \(O(n^3)\) integer arithmetic operations for a base forest with \(n\) vertices. Coefficients have \(O(n)\) bits because they count subsets of \(2n\) vertices, so bit complexity is also polynomial. The procedure works at arbitrary branching degrees and includes isolated original vertices.

## Verification

The supplied standalone `verify.py` (Python standard library only) independently simulates the power-domination process on all initial subsets of the leaf coronas of the \(208\) graph-isomorphism representatives on one through six vertices. It separately enumerates target-saturating matchings and tests unique restriction on their matched endpoints. These implementations agree for \(676900\) initial subsets. On the \(42\) forest representatives, the finite-state polynomial agrees coefficient by coefficient with direct enumeration for \(93924\) initial subsets. It also checks the cyclic four-vertex counterexample and small path-corona polynomials. Execute `python verify.py` from the directory containing this document; the captured output is in `verification_output.txt`. The verification is finite corroboration, not the proof for arbitrary graph order.

## Relationship to prior work

Brimkov, Patel, Suriyanarayana, and Teich introduced the power-domination polynomial, gave general zero-forcing criteria and a corona formula for \(G\circ K_s\) when \(s>1\), and explicitly asked in Question 3 for an efficient computation of the polynomial for \(G\circ K_1\). Their general criteria are foundational and already imply exhaustive methods; the present contribution is the specialized exact matching characterization and polynomial-time all-coefficient algorithm for **every forest base**. It is a partial answer to their arbitrary-base question, not an affirmative answer in full generality.

Whitlatch, Shultis, Ramirez, Ortiz, and Kniahnitskaya counted power-dominating sets in complete rooted \(m\)-ary trees by a separate recursive technique. Their Theorem 1 concerns that specific tree family (and not the leaf-corona operation on an arbitrary forest) and does not give the classification or constant-width recursion above. The notion of uniquely restricted matching was previously introduced by Golumbic, Hirst, and Lewenstein; its definition is used here, not claimed as new. Existing generic power-domination algorithms and counting frameworks may also give algorithms for bounded-treewidth families; no first-ever complexity-class result is asserted. Related published research records concerning minimum power-dominating sets of threshold graphs and other domination polynomials concern different graph families or invariants.

## Limitations

The matching theorem is existential for arbitrary bases; finding a suitable uniquely restricted matching for general \(B_G(A,U)\), or summing over all sensor sets for a general base, is not proved polynomial-time. Hall's inequalities are equivalent only under the stated absence-of-even-cycles hypothesis. The recursion requires a forest base and does not establish any new closed-form coefficient sequence, unimodality, or root-location property for all forests. All-set enumerations for other special tree families may overlap on isolated small examples. The finite program checks graph orders only through six; its success alone cannot establish the infinite theorem. Earlier unindexed or indirectly equivalent literature is a residual priority risk.

## References

1. B. Brimkov, R. Patel, V. Suriyanarayana, and A. Teich, *Power domination polynomials of graphs*, first public arXiv version 28 May 2018, arXiv:1805.10984, especially Theorem 5, Proposition 20, and Question 3. https://arxiv.org/pdf/1805.10984
2. S. Kniahnitskaya, M. Ortiz, O. Ramirez, K. Shultis, and H. Whitlatch, *Counting Power Domination Sets in Complete m-ary Trees*, arXiv:2201.09111 (2022); *Theory and Applications of Graphs* 10(1), Article 4 (2023), Theorem 1. https://arxiv.org/html/2201.09111v1 ; https://doi.org/10.20429/tag.2023.100104
3. M. C. Golumbic, T. Hirst, and M. Lewenstein, *Uniquely restricted matchings*, *Algorithmica* 31 (2001), 139–154. https://doi.org/10.1007/s00453-001-0004-z
