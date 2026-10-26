# Induced-matching enumerators and unbounded maximal-size gaps in subdivided bicliques

## Finding
Let \(2\le p\le q\) be integers and let \(H_{p,q}=S(K_{p,q})\), the graph obtained by replacing each edge of the complete bipartite graph \(K_{p,q}\) by a two-edge path with its own subdivision vertex. An **induced matching** is a set of edges whose endpoints induce a disjoint union of isolated edges. A **maximal induced matching** is inclusion-maximal, not necessarily largest.

Write \(I_{p,q}(z)\) for the cardinality generating polynomial of *all* induced matchings (including the empty matching) and \(M_{p,q}(z)\) for that of inclusion-maximal induced matchings. Then
\[
I_{p,q}(z)=\sum_{a=0}^{p}\sum_{b=0}^{q}
\binom pa\binom qb (q-b)^a(p-a)^b z^{a+b},
\]
and
\[
\begin{aligned}
M_{p,q}(z)={}&q^p z^p+p^q z^q\\
&+\sum_{a=0}^{p-1}\sum_{b=0}^{q-1}
\binom pa\binom qb (p-a)!\,S(b,p-a)\\
&\hspace{28mm}\cdot(q-b)!\,S(a,q-b)z^{a+b}.
\end{aligned}
\]
Here \(S(i,j)\) is the Stirling number of the second kind (the number of partitions of an \(i\)-element labeled set into \(j\) nonempty unlabeled blocks), with \(S(0,j)=0\) for \(j>0\) and \(0^0=1\).

In particular, the exact support of the maximal polynomial is
\[
\{k:[z^k]M_{p,q}(z)>0\}=\{p\}\cup\{q,q+1,\ldots,p+q-2\}.
\]
Thus the smallest and largest cardinalities of maximal induced matchings are \(p\) and \(p+q-2\), respectively. If \(q\ge p+2\), the \(q-p-1\) cardinalities \(p+1,\ldots,q-1\) are absent. These gaps are unbounded already when \(p=2\), in connected bipartite graphs of girth eight.

The number of minimum-cardinality maximal induced matchings is
\[
[z^p]M_{p,q}(z)=
\begin{cases}
q^p,&p<q,\\
2p^p+p!(2^p-2),&p=q.
\end{cases}
\]
The maximum induced-matching cardinality (without maximality qualification) is also \(p+q-2\).

## Assumptions and scope
The graph is finite, simple, undirected, and labeled. Its original vertex classes are \(A\) and \(B\), with respective cardinalities \(p\) and \(q\). For every \(xy\in E(K_{p,q})\), write \(w_{xy}\) for the corresponding subdivision vertex, adjacent to exactly \(x\) and \(y\). Each original-to-subdivision edge is an *incidence*. All enumerators count actual edge subsets of this fixed labeled graph, not isomorphism types. The case \(p=q=2\) is included.

## Proof
**1. Incidences as directed assignments.** Every selected edge in a matching of \(H_{p,q}\) contains exactly one original vertex. Orient the corresponding original edge in \(K_{p,q}\) from that selected original endpoint (its *tail*) toward its other endpoint (its *head*). Since selected edges form a matching, their tails are distinct. Since the matching is induced, the head of any selected incidence cannot be another selected tail: the original vertex at that head would be adjacent to a selected subdivision vertex other than the one incident to itself. Conversely, if each distinct tail is assigned a neighbor outside the tail set, the resulting incidence edges form an induced matching: the chosen subdivision vertices are distinct and none is adjacent to any selected original other than its own tail. Thus the assignments and induced matchings are in bijection.

Take \(a\) tails from \(A\) and \(b\) from \(B\). The former each independently choose one of the \(q-b\) unused vertices of \(B\); the latter each choose one of the \(p-a\) unused vertices of \(A\). There are therefore exactly \(\binom pa\binom qb(q-b)^a(p-a)^b\) induced matchings with these tail counts. Distinct assignments give distinct incidence-edge sets. This proves the formula for \(I_{p,q}(z)\), with empty choices interpreted by \(0^0=1\).

**2. Exact maximality criterion.** For a given matching, let \(T\) be the set of tails, \(U=(A\cup B)\setminus T\), and \(R\subseteq U\) the set of heads actually used. Any possible additional incidence must have a tail \(x\in U\): no selected tail can be reused. If \(x\in R\), adding an incidence at \(x\) would create an edge between that original vertex and an already selected subdivision vertex, so no extension is possible there. If \(x\notin R\), an incidence at \(x\) can be adjoined precisely when \(x\) has a neighbor in \(U\): such an edge creates no adjacency with any selected endpoint. Hence a matching is maximal **if and only if** every vertex of \(U\) that has a neighbor in the induced base graph \(K_{p,q}[U]\) belongs to \(R\).

Write \(u=p-a\) and \(v=q-b\) for the unused vertices on the two sides. If \(u,v>0\), every unused vertex has an unused neighbor; maximality is exactly the pair of surjectivity conditions: the \(b\) tails from \(B\) must hit *every* one of the \(u\) unused vertices in \(A\), and independently the \(a\) tails from \(A\) must hit all \(v\) unused vertices in \(B\). There are \(u!S(b,u)\) and \(v!S(a,v)\) functions, respectively. Summing their products gives the double sum in \(M_{p,q}(z)\).

If \(u=0\), then there can be no tails in \(B\), because no vertex of \(A\) is available as their head. All \(p\) vertices of \(A\) are tails, and their heads may be chosen arbitrarily in \(B\), giving \(q^p\) maximal matchings of size \(p\): there is no edge in the unused base graph, so maximality is automatic. Symmetrically \(v=0\) contributes \(p^q\) maximal matchings of size \(q\). Both boundary families are disjoint, and \(u=v=0\) produces no matching. This completes the formula for \(M_{p,q}(z)\).

**3. Cardinality spectrum.** For an interior maximal matching, surjectivity requires \(b\ge u\) and \(a\ge v\). Equivalently, \(u+v\le q\) and \(u+v\le p\), so \(u+v\le p\). Since \(u,v\ge1\), its cardinality \(a+b=p+q-u-v\) lies in \([q,p+q-2]\). Conversely, for each integer \(k\) in that interval put \(s=p+q-k\), choose \(u=1\), \(v=s-1\), and hence \(a=p-1\), \(b=q-s+1\). Since \(2\le s\le p\le q\), the two required surjections exist; every such \(k\) occurs. The two boundary families add only sizes \(p\) and \(q\), proving the displayed support, including the balanced case.

**4. Extremal multiplicities.** If \(p<q\), only the all-\(A\)-tails boundary contributes at degree \(p\), giving \(q^p\). If \(p=q=r\), both boundaries contribute \(2r^r\). The interior matchings of size \(r\) have \(u+v=r\), so their two surjections are bijections. Their number is
\[
\sum_{u=1}^{r-1}\binom ru\binom r{r-u}u!(r-u)!
=r!\sum_{u=1}^{r-1}\binom ru=r!(2^r-2).
\]
Finally, the assignment bijection bounds every induced matching by \(p+q-2\): if tails occur on both sides, at least one head must remain unused as a tail on each side; if only one side supplies tails, there are at most \(q\le p+q-2\). Taking all but one original vertex in each part as tails, with all tails on each side pointing to the uniquely omitted opposite-side vertex, attains \(p+q-2\). This proves every asserted extremal statement.

## Verification
The standalone Python 3 script `verify.py` builds each subdivided biclique directly from an adjacency matrix, independently generates incidence edges, and checks pairwise endpoint incompatibilities. It enumerates every candidate edge subset of sizes up to the proved upper bound \(p+q-2\), and tests maximality by attempting every possible additional edge. For nine labeled graphs, from \((p,q)=(2,2)\) through \((4,4)\), it examined \(2{,}191{,}336\) candidate subsets; every coefficient of both polynomials agreed. It also checked integer identities, minimum coefficients, and all support endpoints for \(2\le p\le20\), \(p\le q\le26\). For instance,
\[
M_{2,5}(z)=25z^2+42z^5,\qquad
M_{3,4}(z)=64z^3+189z^4+12z^5.
\]
The verifier and its recorded output are included. Enumerating finite instances is corroboration, not a proof of the all-parameter theorem.

## Relationship to prior work
Yuan, Yang, Zheng and Gong (2024) establish extremal bounds on the **total number** of maximal and maximum induced matchings in connected graphs of a fixed order. Their general bound cannot determine the present graph-specific cardinality coefficients, two surjection constraints, or gaps in the maximal-size spectrum. The primary version lists 05C31 first among its graph-theory classifications.

Basavaraju, Heggernes, van 't Hof, Saei and Villanger (2013) give a universal bound for triangle-free graphs, attained by disjoint copies of \(K_{3,3}\), and an enumeration algorithm. The subdivided bicliques here are triangle-free but their exact distribution does not follow from the general upper bound. Earlier formulations of induced matching as independent sets of the square of a line graph yield an equivalence, but not these explicit coefficients without additional analysis. Previous subdivision results on dissociation and domination involve different admissibility and maximality predicates, and likewise do not entail the two-sided surjection classification. No earlier source inspected contained the present closed formulas; bibliographic priority is not certified.

## Limitations
The explicit double-sum formulas and gap theorem require the full, one-step subdivision of \(K_{p,q}\) with \(p,q\ge2\). They do not assert a corresponding formula for arbitrary subdivisions or general bipartite graphs. Some potentially relevant older lower-induced-matching literature was available only through abstract/indexed metadata and could hide equivalent statements; unindexed equivalent work is a remaining priority risk. The theorem has received self-review only, not an independent mathematical audit.

## References
1. B.-J. Yuan, Z.-Y. Yang, L. Zheng, and S.-C. Gong, *Maximal and maximum induced matchings in connected graphs*, arXiv:2410.11288v1 (first public 2024-10-15), https://arxiv.org/abs/2410.11288; later in *Applied Mathematics and Computation* (2025), DOI 10.1016/j.amc.2025.129432.
2. M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei, and Y. Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180v1 (2013-12-18), https://arxiv.org/abs/1312.5180; *Journal of Graph Theory* 83 (2016), 231–250, DOI 10.1002/jgt.21994.
3. Y. Orlovich, G. Finke, V. Gordon, and I. Zverovich, *Approximability results for the maximum and minimum maximal induced matching problems*, *Discrete Optimization* (2008), DOI 10.1016/j.disopt.2007.11.010. Abstract and bibliographic metadata considered; full text was not available in this examination.
