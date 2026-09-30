# Exact weak rainbow saturation of stars from a linear-size threshold
## Finding
Let \(S_\ell\) denote the star on \(\ell\) vertices. For every integer \(\ell\ge 3\) and every integer \(n\ge 2\ell-3\),
\[
\operatorname{rwsat}(n,S_\ell)=\binom{\ell}{2}-1.
\]
Thus the known exact star value already holds from a linear threshold in \(\ell\), including all star orders \(\ell\ge3\).

## Assumptions and scope
All graphs are finite and simple. The weak rainbow saturation definition is the one of Li--Ma--Xie: an edge-colored graph \(F\) is weakly \(H\)-rainbow saturated if its nonedges admit a fixed ordering such that, for every pairwise-distinct assignment of colors to those nonedges, inserting them in that order makes each inserted edge lie in a newly created rainbow copy of \(H\). By Lemma 2.4 of Li--Ma--Xie, a weakly \(H\)-rainbow saturated graph may be recolored so that all initial edges have distinct colors while retaining the property. We therefore work with a rainbow initial graph.

Put \(r=\ell-1\). For a vertex \(v\), let \(d(v)\) be its degree in the initial graph and let \(a(v)\) be the number of previously inserted edges incident with \(v\) at the stage under consideration.

## Proof
We first record the exact local rule for inserting a missing edge \(xy\). Call \(v\) strong if \(d(v)\ge r\) or \(a(v)\ge r-1\), borderline if \(d(v)=r-1\) and \(a(v)\le r-2\), and low if \(d(v)\le r-2\) and \(a(v)\le r-2\).

**Local rule.** The edge \(xy\) is guaranteed to create a rainbow \(S_\ell\) containing \(xy\), for every pairwise-distinct coloring of the inserted edges, if and only if at least one endpoint is strong or both endpoints are borderline.

For sufficiency, if \(d(x)\ge r\), then among the at least \(r\) pairwise-distinct initial colors at \(x\), at most one can equal the color of \(xy\); hence \(xy\) together with \(r-1\) suitable initial edges forms a rainbow star. If \(a(x)\ge r-1\), then \(xy\) and \(r-1\) previously inserted edges at \(x\) already have pairwise-distinct colors. If both endpoints are borderline, each has \(r-1\) initial incident colors, and because the initial graph is rainbow and \(xy\) was initially absent, the two initial color sets are disjoint. The color of \(xy\) can meet at most one of those two sets, so one endpoint supplies a rainbow star using only its initial incident edges and \(xy\).

For necessity, suppose neither endpoint is strong and they are not both borderline. If one endpoint, say \(y\), is borderline and \(x\) is low, color the current edge with one initial color at \(y\), and color each previously inserted edge at \(y\) with a distinct remaining initial color there. At \(x\), reuse distinct initial colors on as many previously inserted incident edges as possible and give any remaining such edges fresh colors. The initial color sets at \(x\) and \(y\) are disjoint, so this assignment is compatible with pairwise distinctness of inserted-edge colors. Then the number of distinct colors incident with \(y\), including the current edge, is at most \(r-1\), and at \(x\) it is at most \(\max\{d(x),a(x)\}+1\le r-1\). If both endpoints are low, use a fresh color on \(xy\) and perform the same maximal reuse independently at the two endpoints; both see at most \(r-1\) distinct colors. Extend the partial assignment to all other nonedges with unused fresh colors. Thus no rainbow \(S_\ell\) containing \(xy\) is forced. This proves the local rule.

We now prove the lower bound. Let \(F\) be weakly \(S_\ell\)-rainbow saturated on \(n\ge2r-1\) vertices, let \(m=e(F)\), and suppose for contradiction that
\[
m\le \binom{r+1}{2}-2.
\]
Partition the vertices according to initial degree:
\[
A=\{v:d(v)\ge r\},\qquad B=\{v:d(v)=r-1\},\qquad C=\{v:d(v)\le r-2\}.
\]
Write \(a=|A|\), \(b=|B|\), and \(q=a+b\). For \(r\ge3\), first \(a\le r-2\). Indeed, the degree sum gives \(ar\le2m\le r^2+r-4\), so if \(a\ge r-1\) then only \(a=r-1\) or \(a=r\) can occur; but the number of edges incident with \(A\) is at least
\[
ar-\binom a2,
\]
which is already at least \(\binom{r+1}{2}-1\) in either case, a contradiction. Also
\[
q(r-1)+a\le \sum_{v\in A\cup B}d(v)\le2m\le r^2+r-4,
\]
so \(q\le r+1\).

Some vertex outside \(A\) must eventually become strong. Otherwise the local rule allows no inserted edge between \(C\) and \(B\cup C\). Hence every \(c\in C\) would have been initially adjacent to all of \(B\cup(C\setminus\{c\})\), so \(d(c)\ge n-a-1\). Since \(d(c)\le r-2\), this gives \(a\ge n-r+1\ge r\), contradicting \(a\le r-2\). If \(C\) were empty, then \(n=q\le r+1<2r-1\), also impossible for \(r\ge3\).

Let \(x\) be the first vertex outside \(A\) that becomes strong. Before that moment a vertex of \(C\) can receive inserted edges only from \(A\), hence at most \(a\le r-2\) of them; therefore \(x\in B\). To acquire \(r-1\) inserted incident edges before any earlier promotion, \(x\) must have at least \(r-1\) initial nonneighbors in \(A\cup B\). Consequently
\[
d_{F[A\cup B]}(x)\le q-r,
\]
so \(q\ge r\). There are only two cases.

If \(q=r\), then \(x\) is isolated in \(F[A\cup B]\), whence
\[
e(F[A\cup B])\le\binom{r-1}{2}.
\]
Using \(m\ge\sum_{v\in A\cup B}d(v)-e(F[A\cup B])\), we obtain
\[
m\ge r(r-1)+a-\binom{r-1}{2}=\binom{r+1}{2}-1+a,
\]
a contradiction.

If \(q=r+1\), then \(d_{F[A\cup B]}(x)\le1\). When \(a\ge1\),
\[
e(F[A\cup B])\le\binom r2+1,
\]
and hence
\[
m\ge(r+1)(r-1)+a-\binom r2-1=\binom{r+1}{2}-2+a\ge\binom{r+1}{2}-1.
\]
When \(a=0\), all \(r+1\) vertices of \(A\cup B=B\) have total degree \(r-1\), while \(x\) has internal degree at most one. Therefore
\[
2e(F[B])\le1+r(r-1),
\]
so \(e(F[B])\le\binom r2\), and
\[
m\ge(r+1)(r-1)-\binom r2=\binom{r+1}{2}-1.
\]
Again we have a contradiction. Thus the lower bound holds for \(r\ge3\). For \(r=2\), a graph with at most one initial edge on at least three vertices cannot start a valid completion: the endpoints of the sole edge are the only possible borderline vertices and are already adjacent, while every other vertex is low. Hence at least two initial edges are required, equal to \(\binom32-1\).

For the matching upper bound, take a rainbow copy of \(K_\ell\) with one edge \(pq\) deleted and make the remaining \(n-\ell\) vertices initially isolated. Let \(R\) be the other \(\ell-2=r-1\) core vertices. Every vertex of \(R\) is initially strong, while \(p\) and \(q\) are borderline. Insert \(pq\) first. Since \(n-\ell\ge\ell-3=r-2\), select distinct isolated vertices \(z_1,\ldots,z_{r-2}\). For each \(z_j\), first insert all \(r-1\) edges from \(R\) to \(z_j\); each is legal through its strong endpoint in \(R\), and afterward \(z_j\) is strong. Then insert \(pz_j\) and \(qz_j\), legal through \(z_j\). After these steps, \(p\) and \(q\) have each accumulated \(1+(r-2)=r-1\) inserted incident edges and are strong. For every remaining isolated vertex, insert edges from any \(r-1\) already strong vertices to it; this promotes that vertex to strong. Once all vertices are strong, insert every remaining nonedge in arbitrary order. The initial graph has
\[
\binom\ell2-1
\]
edges, proving the upper bound and completing the theorem.

## Verification
The proof was reconstructed from the definition, including the universal quantifier over all pairwise-distinct colors of inserted edges. A direct finite-state enumerator exhaustively checked the local rule for \(r=2,3,4\). A separate graph enumerator verified the construction for \(3\le\ell\le12\), checked one larger order for each tested \(\ell\), and exhaustively recovered the exact small values \(\operatorname{rwsat}(3,S_3)=2\), \(\operatorname{rwsat}(4,S_3)=2\), \(\operatorname{rwsat}(4,S_4)=4\), \(\operatorname{rwsat}(5,S_4)=5\), \(\operatorname{rwsat}(5,S_5)=8\), \(\operatorname{rwsat}(6,S_5)=9\), and \(\operatorname{rwsat}(7,S_5)=9\). These checks are supplementary to the proof, not substitutes for it.

## Relationship to prior work
Bo, Lian and Liu determine the star value \(\binom{\ell}{2}-1\) in their September 2026 preprint under a substantially larger parameter range; their stated star theorem requires \(\ell\ge6\) and \(n\ge3\ell^2\). The argument above gives the same exact value for every \(\ell\ge3\) once \(n\ge2\ell-3\). Li, Ma and Xie introduced the weak rainbow saturation framework used here and proved the rainbow-recoloring lemma needed in the reduction.

## Limitations
The threshold \(n\ge2\ell-3\) is sufficient, not claimed optimal. Exhaustive small cases already show that the same exact value can hold below this threshold for some \((n,\ell)\), while other smaller orders have different values. Originality is asserted only on a best-of-knowledge basis after searches of the current literature and published-finding corpus; no independent audit, formal proof assistant verification, or expert attestation has been performed.

## References
1. Jiawen Bo, Xiaopan Lian, Jianing Liu, *Weak rainbow saturation numbers of paths, stars and cycles*, arXiv:2609.03823v1, first posted 2026-09-03.
2. Xihe Li, Jie Ma, Tianying Xie, *Weak Rainbow Saturation Numbers of Graphs*, Journal of Graph Theory 109 (2025), 35--42, DOI: 10.1002/jgt.23211; preprint arXiv:2401.11525.
