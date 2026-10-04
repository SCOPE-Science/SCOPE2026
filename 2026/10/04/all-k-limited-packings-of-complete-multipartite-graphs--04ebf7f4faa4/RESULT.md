# All \(k\)-limited packings of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with nonempty parts \(V_1,\ldots,V_r\), where \(r\ge 2\), and let \(N=\sum_i n_i\). For an integer \(k\ge1\), a set \(B\subseteq V(G)\) is a \(k\)-limited packing when \( |N[v]\cap B|\le k\) for every vertex \(v\).

Write \(b=|B|\) and \(b_i=|B\cap V_i|\). Then \(B\) is a \(k\)-limited packing if and only if either

\[b\le k,\]

or

\[b>k\quad\text{and}\quad b_i\ge b-k+1\text{ for every }i.\]

Thus all subsets of size at most \(k\) are feasible, while every larger feasible set must meet every part with a partwise quota that increases linearly with its total size.

The ordinary size enumerator is therefore

\[P_{G,k}(x)=\sum_{s=0}^{\min\{k,N\}}\binom Ns x^s+\sum_{s=k+1}^N c_sx^s,\]

where

\[c_s=[y^s]\prod_{i=1}^r\left(\sum_{j=s-k+1}^{n_i}\binom{n_i}{j}y^j\right).\]

If \(m=\min_i n_i\), then

\[L_k(G)=\min\left\{N,\max\left\{k,\min\left\{k+m-1,\left\lfloor\frac{r(k-1)}{r-1}\right\rfloor\right\}\right\}\right\}.\]

## Assumptions and scope
The graph is finite, simple, connected, and complete multipartite with \(r\ge2\) nonempty parts. The parameter \(k\) is any positive integer. No balance assumption is imposed on the part sizes. The statement concerns closed-neighborhood limited packing.

The enumerator counts every feasible vertex subset by cardinality. For \(k\ge N\), the displayed formula reduces to \(P_{G,k}(x)=(1+x)^N\) and \(L_k(G)=N\).

## Proof
Fix a part \(V_i\). For a vertex \(v\in V_i\), the closed neighborhood consists of \(v\) together with all vertices outside \(V_i\). Hence

\[|N[v]\cap B|=\begin{cases}1+b-b_i,&v\in B,\\ b-b_i,&v\notin B.\end{cases}\]

If \(b\le k\), every closed neighborhood contains at most \(b\) selected vertices, so \(B\) is automatically a \(k\)-limited packing.

Assume now that \(b>k\). If some part has \(b_i=0\), then every vertex in that part sees all \(b\) selected vertices in its closed neighborhood, contradicting \(b>k\). Thus every part contains a selected vertex. For any selected vertex in \(V_i\), feasibility is equivalent to

\[1+b-b_i\le k,\]

which is exactly

\[b_i\ge b-k+1.\]

These inequalities are also sufficient: for a selected vertex they give the required bound directly, while an unselected vertex in the same part sees only \(b-b_i\le k-1\) selected vertices. This proves the structural characterization.

For fixed \(s>k\), put \(t=s-k+1\). A feasible set of size \(s\) exists exactly when integers \(b_i\) can be chosen with \(t\le b_i\le n_i\) and \(\sum_i b_i=s\). This is equivalent to

\[t\le m,\qquad rt\le s,\qquad s\le N.\]

Necessity is immediate. For sufficiency, allocate \(t\) selected vertices to each part. The remaining demand is \(s-rt\), while the total residual capacity is \(N-rt\ge s-rt\), so the remaining selections can be distributed among the parts without exceeding any \(n_i\).

The inequalities become

\[s\le k+m-1,\qquad s\le\left\lfloor\frac{r(k-1)}{r-1}\right\rfloor,\qquad s\le N.\]

Together with the always-feasible sizes \(s\le k\), maximizing \(s\) gives the stated formula for \(L_k(G)\). The coefficient formula for \(c_s\) follows by independently choosing \(b_i\) vertices from each part under the lower quotas and extracting total degree \(s\).

For \(r=2\), this maximum simplifies to the known complete-bipartite expression \(L_k(K_{a,b})=1\) for \(k=1\), and \(L_k(K_{a,b})=\min\{k-1,a\}+\min\{k-1,b\}\) for \(k>1\), with the natural cap at the graph order when \(k\) is larger than every closed neighborhood.

## Verification
A standalone verifier exhaustively checks every ordered complete-multipartite profile of order at most \(9\), every positive \(k\) through \(N+1\), and every vertex subset. It compares the literal closed-neighborhood definition with the structural characterization, reconstructs every coefficient of \(P_{G,k}(x)\), checks the closed formula for \(L_k(G)\), and separately checks the complete-bipartite specialization.

The replay output is:

`VERIFY_OK profiles=502 subset_checks=1680156 criterion_checks=1680156 coefficient_checks=42110 bipartite_checks=276 max_order=9`

This finite census is a stress test only; the theorem for arbitrary part sizes and \(k\) is established by the proof above.

## Relationship to prior work
Gallant, Gunther, Hartnell, and Rall introduced \(k\)-limited packing and, in their early proceedings paper, gave exact values for several basic graph families. In particular, their Lemma 1.3 states the complete-bipartite value \(L_k(K_{m,n})\), which is recovered by the present formula when \(r=2\). Their paper gives bounds and structural results, not the arbitrary complete-multipartite all-set characterization or its enumerator.

Dobson, Leoni, and Nasini study the computational relation between limited packing and multiple domination on structured graph classes, including bipartite, split, strongly chordal, and \(P_4\)-tidy graphs. This establishes that the parameter is algorithmically nontrivial on broad classes but does not supply the present closed arbitrary-multipartite classification.

Gagarin and Zverovich develop probabilistic and greedy bounds for \(L_k(G)\); the full arXiv text used as the date anchor discusses general bounds and algorithms and contains no occurrence of “complete multipartite” or “complete bipartite.”

## Limitations
The result is specific to complete multipartite graphs and closed-neighborhood limited packing. It does not address total/open-neighborhood limited packing, packing functions with integer weights, limited-packing partitions, or general split and bipartite graphs.

The earliest day-level public timestamp independently verified for an accessible source used to anchor this item is the arXiv posting of Gagarin and Zverovich on 2013-11-07. An earlier LAGOS'07/2008 paper contains the complete-bipartite special case, but its exact public posting day was not independently verified here; that dating uncertainty is retained rather than replaced by an invented day.

A residual originality risk remains from older literature indexed only under alternative terminology such as closed-neighborhood packing or generalized packing, although direct searches and the highly relevant full texts inspected did not reveal the arbitrary complete-multipartite all-set statement.

## References
1. R. P. Gallant, G. Gunther, B. L. Hartnell, and D. F. Rall, “Limited Packings in Graphs,” Electronic Notes in Discrete Mathematics 30 (2008), 15–20, DOI: 10.1016/j.endm.2008.01.004. The LAGOS'07 proceedings copy contains Definition 1.1, Definition 1.2, and Lemma 1.3 with the complete-bipartite formula.
2. M. P. Dobson, V. A. Leoni, and G. L. Nasini, “The multiple domination and limited packing problems in graphs,” Information Processing Letters 111 (2011), 1108–1113, DOI: 10.1016/j.ipl.2011.09.002.
3. A. Gagarin and V. Zverovich, “The probabilistic approach to limited packings in graphs,” arXiv:1311.1707, first public arXiv posting 2013-11-07.
4. A. Gagarin and V. Zverovich, “Bounds and algorithms for limited packings in graphs,” arXiv:1407.1637, first public arXiv posting 2014-07-07.
