# Zero-forcing sets of rook graphs via leaf-accessible bipartite forests

## Finding
For every pair of integers \(m,n\ge 2\), the ordinary zero-forcing sets of the rectangular rook graph \(R_{m,n}=K_m\square K_n=L(K_{m,n})\) are characterized by the following finite, static condition. Given an initial blue set \(S\subseteq V(R_{m,n})\), let \(H_S\) be the spanning subgraph of \(K_{m,n}\) whose edges correspond to initially white rook vertices. For \(i\in\{0,1\}\), let \(a_i\) and \(b_i\) be the numbers of degree-\(i\) vertices in the left and right classes of \(H_S\), respectively. Then
\[
 S\text{ is zero forcing}\ \Longleftrightarrow\
 H_S\text{ is a forest and }\bigl[(a_0>0\ \land\ (b_0+b_1>0))\ \lor\ (b_0>0\ \land\ (a_0+a_1>0))\bigr].
\]
In particular this is an exact test for **every** initial set, not only sets of minimum size.

The characterization gives a complete coefficient formula for the ordinary zero-forcing polynomial. For integers \(r\ge1\), \(\ell\ge0\), put
\[
Q_{r,\ell}(t)=\sum_{j=0}^{r}\binom rj(t-1)^j(r-j)^\ell,
\]
with \(0^0=1\). For formal variables \(u,v,z\) and parameters \(\alpha,\beta,p,q\), put
\[
F_{\alpha,\beta;p,q}(u,v,z)=\exp\!\left(\alpha u+\beta v+\sum_{a,b\ge1}\frac{u^av^bz^{a+b-1}}{a!\,b!}\,Q_{a,b-1}(p)Q_{b,a-1}(q)\right).
\]
Set
\[
\begin{aligned}
\mathcal W(u,v,z)={}&F_{1,1;1,1}-F_{1,0;1,0}-F_{0,1;0,1}\\
&+F_{0,0;1,0}+F_{0,0;0,1}-F_{0,0;1,1},
\end{aligned}
\]
where the arguments \((u,v,z)\) on the right are understood. If \(\mathcal Z_{m,n}(x)=\sum_{S\text{ zero forcing}}x^{|S|}\), then
\[
\boxed{\mathcal Z_{m,n}(x)=m!n!\sum_{k=0}^{mn}[u^mv^nz^k]\mathcal W(u,v,z)\,x^{mn-k}.}
\]
Thus a single explicit exponential construction evaluates every coefficient for arbitrary finite \(m,n\), without simulating color changes.

Define \(\mathrm{St}_2(r,s)\) to be the Stirling number of the second kind, with \(\mathrm{St}_2(0,0)=1\) and \(\mathrm{St}_2(r,s)=0\) for \(s>r\). The exact number of minimum-cardinality zero-forcing sets is
\[
\boxed{\begin{aligned}
N_{m,n}={}&m(m-1)^{n-1}\bigl[n^{m-2}-n!\,\mathrm{St}_2(m-2,n)\bigr]\\
&+n(n-1)^{m-1}\bigl[m^{n-2}-m!\,\mathrm{St}_2(n-2,m)\bigr].
\end{aligned}}
\]
The minimum cardinality is the already-known \(mn-m-n+2\); it is **not** a novelty claim.

## Assumptions and scope
All graphs are finite, simple and undirected. Rook vertices are ordered pairs \((i,j)\), and two are adjacent precisely if they have one coordinate in common. The zero-forcing rule is ordinary (not skew or positive-semidefinite): an already blue vertex with exactly one white neighbor changes that neighbor blue. The bipartite graph \(H_S\) retains **all** \(m+n\) vertices, including isolated ones. All coefficient extractions are formal and finite at each fixed \((m,n)\). Factorials, binomial coefficients and the values of \(Q_{r,\ell}\) are ordinary integer expressions.

## Proof
**Static characterization.** Identify the rook vertex \((i,j)\) with edge \(ij\) of \(K_{m,n}\). At any stage, let \(H\) comprise the currently white edges. A blue edge \(ab\notin H\) has exactly \(\deg_H(a)+\deg_H(b)\) white rook-neighbors. Therefore it can force a white edge exactly when one endpoint is isolated in \(H\) and the other has degree one. The forced white edge is incident to that degree-one vertex; the forcing action deletes it from \(H\).

If \(H\) contains a cycle, consider the first edge on that cycle which could be deleted. Immediately before its deletion every cycle edge is still present, so both of its endpoints have white degree at least two. But a white edge can be forced only if it is incident to a degree-one endpoint. This is impossible; all such cycles survive, and the initial set fails to force.

Suppose instead that \(H\) is a forest. The displayed degree condition is exactly the existence of either an isolated left vertex and a right vertex of degree zero or one, or the symmetric alternative. If there is at least one white edge and both sides already contain isolated vertices, choose a leaf of the forest. If the leaf lies on the right, use an isolated left vertex to obtain a blue edge which forces the leaf's unique white edge; similarly for a left leaf. The isolated vertices persist under deletion, so repetition removes every white edge. If initially only the left side has an isolate while the right has a degree-one vertex, use the blue edge between them to remove the latter vertex's unique white edge: an isolated right vertex is created, and the preceding argument applies. The symmetric case is identical. If the condition fails, no blue edge has a unique white neighbor, so no first force is possible. Empty \(H\) is trivially completed. This proves both directions for all \(m,n\ge2\).

**Enumerating marked forests.** A spanning forest of a complete bipartite graph consists of isolated left vertices, isolated right vertices and nontrivial bipartite tree components. In a component with \(a\ge1\) labeled left vertices and \(b\ge1\) labeled right vertices, bipartite Prüfer coding gives a pair of independent words: one of length \(b-1\) using left labels, and one of length \(a-1\) using right labels. For each vertex, the degree is one plus its number of appearances in the corresponding word. The number of degree-one vertices is consequently the number of absent labels. Inclusion–exclusion gives exactly \(Q_{r,\ell}(t)\) as the word enumerator weighted by \(t\) for each absent label. Thus the weighted tree polynomial is \(Q_{a,b-1}(p)Q_{b,a-1}(q)\), and the labeled exponential formula gives \(F_{\alpha,\beta;p,q}\), with \(\alpha,\beta\) marking isolated vertices.

To obtain the permitted forests, let \(a_0,b_0\) and \(a_1,b_1\) have their earlier meanings. A forest fails the degree condition precisely in one of the following disjoint situations: both sides have no isolates; the left side has an isolate but the right side has neither an isolate nor a leaf; or the right side has an isolate but the left side has neither an isolate nor a leaf. In \(F\), setting an isolate marker to zero forbids isolates of that class and setting a leaf marker to zero forbids degree-one vertices in nontrivial components. Inclusion–exclusion for these three classes therefore gives the six signed terms defining \(\mathcal W\). Every white forest on \(m+n\) prescribed vertices with \(k\) edges corresponds bijectively to an initial blue set of size \(mn-k\), proving the coefficient formula.

**Minimum sets.** A permitted forest has at least one isolate and hence at most \(m+n-2\) edges. Equality is attained for a single isolated left vertex together with a tree on the other \(m+n-1\) vertices whose right part has a leaf, or the symmetric configuration. Thus the minimum size of a zero-forcing set is \(mn-(m+n-2)\), agreeing with the earlier line-graph theorem. To count these sets, consider the first type. There are \(m\) choices for the isolated left vertex; on the remaining \(m-1\) left and \(n\) right vertices there are \((m-1)^{n-1}n^{m-2}\) labeled bipartite spanning trees. Of these, the trees with **no right leaf** have \((m-1)^{n-1}n!\,\mathrm{St}_2(m-2,n)\) choices: their right-label Prüfer word has length \(m-2\) and must use every right label. Subtraction counts those with a right leaf. Add the symmetric count for an isolated right vertex. The two cases are disjoint because a maximally edged forest has exactly two components and only one is isolated. This yields \(N_{m,n}\).

## Verification
The accompanying standalone Python program `verify.py` enumerates all white-edge subsets for eight labeled boards with sizes \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)\). For each of the 104272 configurations it executes the ordinary color-change process directly and independently tests the forest-and-degree criterion. It separately evaluates the six exponential-formula terms by weighted component partition recursion, compares every polynomial coefficient with the direct census, and checks the minimum-set Stirling formula. The program reports `VERIFY_OK boards=8 exhaustive_subsets=104272 six_EGF_terms=passed minimum_count=passed` when all tests succeed. These finite tests corroborate the preceding unrestricted combinatorial proof; they do not prove infinitely many cases by themselves.

## Relationship to prior work
The ordinary zero-forcing process was introduced by the AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, *Linear Algebra and its Applications* **428** (2008), 1628–1648 (first available online November 26, 2007). Fallat and Soltani, *Line graphs: their maximum nullities and zero forcing numbers*, *Czechoslovak Mathematical Journal* **66** (2016), 743–755, especially Theorem 3.4, recover the minimum size for \(K_m\square K_n\), but do not give the full all-set criterion or full zero-forcing polynomial. Boyer and collaborators, *The zero forcing polynomial of a graph*, arXiv:1801.08910, develop the counting framework and calculate other graph families, but do not present this rook-graph enumerator. Pelayo and Abara, *Maximal failed zero forcing sets for products of two graphs*, arXiv:2202.04997, §3.1 Theorem 3.7, give the extremal failed zero-forcing number \(mn-4\) when one complete factor has order at least four; this is a different one-parameter result, not a counting formula for all zero-forcing sets. The present claim comprises the full forest criterion, the complete polynomial and the enumerated minimum sets, not the previously known extremal sizes.

## Limitations
Only ordinary zero forcing of Cartesian products of **two** complete graphs with both factors of order at least two is treated. This is a mathematical derivation and self-review, not an independent audit. A literature comparison does not establish absolute priority; an equivalent all-set enumeration under different terminology remains possible. The six-term generating function is an exact coefficient formula rather than a claim of uniformly fast computational complexity at large orders.

## References
1. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, *Linear Algebra Appl.* **428** (2008), 1628–1648. DOI: https://doi.org/10.1016/j.laa.2007.10.009. First available online 2007-11-26.
2. S. Fallat and A. Soltani, *Line graphs: their maximum nullities and zero forcing numbers*, *Czechoslovak Math. J.* **66** (2016), 743–755. https://dml.cz/dmlcz/145869.
3. K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910, version posted 2018-01-26. https://arxiv.org/abs/1801.08910.
4. P. A. B. Pelayo and M. N. M. Abara, *Maximal failed zero forcing sets for products of two graphs*, arXiv:2202.04997, first posted 2022-02-10. https://arxiv.org/abs/2202.04997.
