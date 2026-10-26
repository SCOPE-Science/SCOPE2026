# Biased tree orientations: a strict path extremum and a four-vertex sign transition

## Finding
Let \(T\) be any finite tree on \(n\ge2\) vertices. Choose a bipartition \(V(T)=A\sqcup B\), and independently orient each edge from \(A\) to \(B\) with probability \(p\in(0,1)\), or the other way with probability \(q=1-p\). Let \(S\) and \(K\) be the numbers of sources and sinks, respectively. Write \(d_v\) for degree, and \(g_p(k)=q p^{k-1}+p q^{k-1}\). Then
\[\operatorname{Cov}(S,K)=\sum_{uv\in E(T)}g_p(d_u+d_v)-\sum_{v\in V(T)}(pq)^{d_v}.\]
For every \(n\ge4\) and \(0<p<1\), this covariance is uniquely maximized, up to graph isomorphism, by the path \(P_n\), and its sharp maximum is
\[\operatorname{Cov}_{P_n}(S,K)=pq\big((n-3)-(3n-8)pq\big).\]
In particular, on four vertices the maximum is \(pq(p-q)^2\), positive exactly when \(p\ne1/2\). At unbiased orientation \(p=1/2\), positive covariance requires at least five vertices; under any fixed noncentral bias, four vertices already suffice. For all \(n\ge5\) and all \(0<p<1\), the path maximum is positive. For orders two and three the sole tree shapes have covariance \(0\) and \(-(pq)^2\), respectively.

## Assumptions and scope
All graphs are finite simple undirected trees, with at least two vertices; the bipartition is arbitrary and its interchange exchanges \(p\) and \(q\), leaving the covariance unchanged. All edges orient independently. A source has indegree zero, a sink has outdegree zero. The parameter is any real \(0<p<1\), without asymptotic restrictions. The path is unique among unlabeled tree shapes for every \(n\ge4\). This does not claim a universal lower extremizer under bias.

## Proof
Write \(I_v\) and \(J_v\) for the source and sink indicators. At any vertex, \(I_v J_v=0\), and \(\mathbb E I_v\mathbb E J_v=(pq)^{d_v}\), regardless of its bipartition side. At nonadjacent vertices their incident orientation variables are disjoint, so their source/sink covariance vanishes. For adjacent \(u,v\) with total degree \(k=d_u+d_v\), the sum of the two ordered mixed covariances equals \(q p^{k-1}+p q^{k-1}=g_p(k)\). Summing over all ordered vertex pairs proves the first formula.

For path orders \(n\ge3\), exactly two vertices have degree one, and \(n-2\) vertices have degree two. When \(n\ge4\), two terminal edges have endpoint-degree sum three and \(n-3\) interior edges have sum four. Substitution gives \(2g_p(3)+(n-3)g_p(4)-2pq-(n-2)(pq)^2=pq((n-3)-(3n-8)pq)\). Direct substitution separately gives the cases \(n=2,3\).

It remains to establish the strict path extremum. Set \(h(j)=(pq)^j\), so \(g_p(j)\) is strictly decreasing in \(j\). Every nonpath tree has a branching vertex \(w\) of degree \(d\ge3\) with at least two internally vertex-disjoint pendant paths (choose a branching vertex peripheral in the subtree induced by branching vertices). Pick two such arms, of lengths \(a,b\ge1\), with terminal leaf \(y\) on the second. Delete the first edge \(wr\) of the first arm and insert \(yr\). This preserves the tree and changes only \(d_w:d\to d-1\) and \(d_y:1\to2\); the degree of \(r\) is \(t\in\{1,2\}\). The change in the negative vertex sum, namely old vertex penalty minus new, is
\[h(1)-h(2)+h(d)-h(d-1)=(1-pq)\big(pq-(pq)^{d-1}\big)>0.\]

All incident edges of \(w\) except the two chosen-arm edges weakly improve their \(g_p\)-contributions (in fact strictly when present), since its degree decreases. When \(b=1\), the contribution on \(wy\) remains unchanged and replacing \(wr\) with \(yr\) strictly improves it by \(g_p(t+2)-g_p(t+d)>0\). Thus the full covariance strictly increases.

When \(b\ge2\), the changes on the edge \(w\)–(first vertex of the second arm), the old final edge of that arm, and the moved first-arm edge sum to
\[g_p(d+1)-g_p(d+2)+g_p(4)-g_p(3)+g_p(t+2)-g_p(d+t).\]
If \(t=1\), this reduces to \(g_p(4)-g_p(d+2)>0\). If \(t=2\), it is \(B_d=2g_p(4)-g_p(3)+g_p(d+1)-2g_p(d+2)\). Here \(B_3=0\), and for every integer \(d\ge3\),
\[B_{d+1}-B_d=(pq)^2(1-2p)\big(q^{d-2}-p^{d-2}\big)\ge0.\]
The factors \(1-2p=q-p\) and \(q^{d-2}-p^{d-2}\) have the same sign. Hence \(B_d\ge0\). The vertex contribution above is always strictly positive. Each move therefore strictly increases covariance. It decreases \(\sum_v\max\{d_v-2,0\}\) by exactly one and eventually yields a path, proving uniqueness.

Finally, since \(pq\le1/4\), the bracket in the path formula is at least \((n-4)/4\), strictly positive for \(n\ge5\). At \(n=4\) it equals \(1-4pq=(p-q)^2\), giving the stated sign threshold.

## Verification
The accompanying `verify.py` checks the local covariance formula against direct enumeration of independent edge orientations and the strict path inequality on every nonisomorphic tree through eight vertices, for exact parameters \(p\in\{1/3,2/5,1/2\}\). All cases passed. The proof above is for every finite order and all real \(p\in(0,1)\); these finite checks are supplemental, not an infinite certificate.

## Relationship to prior work
Conte, Grossi, Marino and Rizzi (2018) study algorithms enumerating graph orientations subject to source prescriptions, rather than extremizing the joint covariance of source and sink counts. Collares et al. (2018, arXiv:1811.03080) examine orientations of random graphs with forbidden directed patterns. An earlier special-parameter result established sharp source–sink covariance bounds for uniformly oriented trees, \(p=1/2\). The present quantified family does not follow from that one-parameter theorem: it treats all \(p\in(0,1)\), proves a parameter-uniform strict path inequality, and detects positive covariance on four vertices outside the fair point.

## Limitations
This result applies to the bipartition-homogeneous independent edge-bias model on trees only, not arbitrary edge-specific biases or general graphs. It does not establish the minimizing tree under bias. Earlier equivalent results in specialized orientation-enumeration or degree-index literature may exist and would affect priority; independent audit has not been performed.

## References
1. A. Conte, R. Grossi, A. Marino and R. Rizzi, *Efficient enumeration of graph orientations with sources*, Discrete Applied Mathematics **246** (2018), 22–37, DOI:10.1016/j.dam.2017.08.002.
2. M. Collares, Y. Kohayakawa, R. Morris and G. O. Mota, *Counting restricted orientations of random graphs*, arXiv:1811.03080 (first posted 2018-11-07).
