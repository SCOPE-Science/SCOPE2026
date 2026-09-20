# Mixed cluster joins and an explicit clique partition-cover deficit constant

## Statement

For a finite simple graph $G$, let $\operatorname{cp}(G)$ be the minimum number of cliques whose edge sets partition $E(G)$, and let $\operatorname{cc}(G)$ be the minimum number of cliques whose edge sets cover $E(G)$. Put
\[
\sigma_n=\max_{|V(G)|=n}\bigl(\operatorname{cp}(G)-\operatorname{cc}(G)\bigr),\qquad
 d_n=\left\lfloor\frac{n^2}{4}\right\rfloor-\sigma_n.
\]

The following heterogeneous cluster-join family has both clique parameters in closed form.

**Theorem.** Let $p,q\ge 2$ and $h,\ell\ge 1$, and let $0\le r\le \ell$. Define
\[
G=\left(\bigsqcup_{i=1}^{h}K_p\right)\vee
\left(rK_{q+1}\sqcup(\ell-r)K_q\right).
\]
Write
\[
d_p=\binom p2,\qquad d_q=\binom q2,\qquad
 a=h d_p,\qquad b=\ell d_q+r q,
\]
and
\[
s=hp(\ell q+r).
\]
If
\[
 d_p\le \ell,\qquad
 \left\lceil\frac{h d_p}{\ell}\right\rceil\le d_q,
 \qquad
 \binom{q+1}{2}\le h,
\]
then
\[
\boxed{\operatorname{cc}(G)=h\ell}
\]
and
\[
\boxed{\operatorname{cp}(G)=s-2a-b
=hp(\ell q+r)-2h\binom p2-\ell\binom q2-rq.}
\]
Consequently
\[
\operatorname{cp}(G)-\operatorname{cc}(G)
=s-2a-b-h\ell.
\]

This includes unequal cluster sizes and permits a one-vertex size correction in any chosen subset of the clusters on the second side.

## Proof

### Clique covering number

For every pair of clusters $A_i$ on the first side and $B_j$ on the second side, $A_i\cup B_j$ is a clique. These $h\ell$ cliques cover all edges, so $\operatorname{cc}(G)\le h\ell$.

For the reverse inequality, choose one representative from every $A_i$ and one from every $B_j$. The chosen vertices induce $K_{h,\ell}$. A clique of $G$ contains representatives from at most one first-side cluster and at most one second-side cluster, hence covers at most one of the $h\ell$ selected crossing edges. Thus every clique cover has at least $h\ell$ members.

### Clique partition lower bound

For a cut $V(G)=A\dot\cup B$ with $a$ internal edges in $A$, $b$ internal edges in $B$, and $s$ crossing edges, the Erdős--Faudree--Ordman cut bound gives
\[
\operatorname{cp}(G)\ge s-a-b-\min\{a,b\}.
\]
For completeness, one orientation of the bound follows by applying, to each clique meeting the two sides in $x$ and $y$ vertices,
\[
xy\le 1+2\binom x2+\binom y2.
\]
Summing over an edge partition gives $s\le \operatorname{cp}(G)+2a+b$; swapping the two sides gives the symmetric companion inequality.

The hypothesis $\lceil h d_p/\ell\rceil\le d_q$ implies $a\le \ell d_q\le b$, and therefore
\[
\operatorname{cp}(G)\ge s-2a-b.
\]

### Matching the lower bound

List the $d_p$ internal edges of every $A_i$ as $e_{i,0},\ldots,e_{i,d_p-1}$. Assign $e_{i,u}$ to the second-side cluster
\[
 B_{(i d_p+u)\bmod \ell}.
\]
Because $d_p\le\ell$, a fixed $A_i$ uses every cluster pair $A_i$--$B_j$ at most once. Across all $a=h d_p$ assignments, the loads on the $B_j$ differ by at most one, so every load is at most $\lceil a/\ell\rceil\le d_q$.

For each $B_j$, pair the assigned first-side internal edges with distinct internal edges of $B_j$. Each paired pair of edges spans a $K_4$; use that $K_4$ as one member of the partition. Every first-side internal edge is now covered exactly once, and exactly $a$ second-side internal edges have been used. Since no cluster pair receives two such $K_4$'s, their crossing edges are pairwise disjoint.

Let $e_j$ be the number of internal edges of $B_j$, so $e_j$ is either $d_q$ or $\binom{q+1}{2}$. If $t_j$ of those edges were used in $K_4$'s, there remain $e_j-t_j$ internal edges. Exactly $h-t_j$ first-side clusters have an unused cluster pair with $B_j$, and
\[
e_j-t_j\le h-t_j
\]
by $e_j\le\binom{q+1}{2}\le h$. Assign every remaining internal edge of $B_j$ to a distinct unused first-side cluster and make a triangle from that edge and any one vertex of the assigned $A_i$. These triangles use no crossing edge already used by a $K_4$, and no two such triangles share a crossing edge.

Finally, use every remaining crossing edge as a two-vertex clique. This is an edge partition. It contains $a$ copies of $K_4$, $b-a$ triangles, and
\[
s-4a-2(b-a)=s-2a-2b
\]
two-vertex cliques. Hence its total size is
\[
a+(b-a)+(s-2a-2b)=s-2a-b,
\]
matching the lower bound.

## Explicit second-order constant

Let
\[
c=2^{-2/3}.
\]
For sufficiently large $n$, choose
\[
p=\lfloor c n^{1/3}\rfloor,\qquad
h=\left\lfloor\frac{n}{2p}\right\rfloor.
\]
Let $q$ be the largest integer with
\[
\binom{q+1}{2}\le h.
\]
Put $X=hp$, $Y=n-X$, and write
\[
Y=\ell q+r,\qquad 0\le r<q.
\]
Then
\[
p\sim 2^{-2/3}n^{1/3},\qquad
q\sim 2^{1/3}n^{1/3},\qquad
h\sim \frac{n}{2p},\qquad
\ell\sim\frac{n}{2q}.
\]
In particular, for all sufficiently large $n$ the three hypotheses of the theorem hold and $r\le\ell$. The resulting graph has exactly $n$ vertices.

Because $X+Y=n$ and $|X-Y|=O(p)$,
\[
\left\lfloor\frac{n^2}{4}\right\rfloor-XY=O(p^2).
\]
Using the exact formulas above,
\[
 d_n\le
 \left\lfloor\frac{n^2}{4}\right\rfloor-XY
 +2h\binom p2
 +\ell\binom q2+rq
 +h\ell.
\]
The four terms have the asymptotic expansion
\[
 d_n\le
 \left(\frac{c}{2}+\frac{1}{4\sqrt c}+\frac{1}{4\sqrt c}\right)n^{4/3}+O(n).
\]
For $c=2^{-2/3}$, all three displayed leading contributions are equal, giving
\[
\boxed{
 d_n\le \frac{3}{2^{5/3}}\,n^{4/3}+O(n)
}
\]
and therefore
\[
\boxed{
\limsup_{n\to\infty}\frac{d_n}{n^{4/3}}
\le \frac{3}{2^{5/3}}
\approx 0.9449407874.
}
\]
No optimality is claimed for this numerical constant.

## Literature context and originality boundary

Bo Ning recently proved $d_n=\Theta(n^{4/3})$. His lower-bound construction determines both clique parameters for the balanced uniform join
\[
G_{h,k}=(hK_k)\vee(hK_k)
\]
when $k$ is even and $h\ge k-1$, and then pads with isolated vertices to obtain arbitrary orders. The cut lower bound used above is due to Erdős, Faudree, and Ordman and is not new.

The contribution here is the exact attainment of that cut bound for a heterogeneous two-sided cluster join under the stated finite conditions, including the $q/q+1$ size correction, and the resulting exact-order construction yielding the explicit coefficient $3/2^{5/3}$ in the $n^{4/3}$ deficit. To the best of our knowledge, neither this mixed-cluster formula nor the displayed uniform limsup constant appears in the checked literature. Older clique-decomposition literature under different terminology and very recent unindexed work remain residual originality risks.

## Verification

The accompanying verifier constructs the graph and the stated $K_4$/triangle/edge partition directly from the definitions. It checks that every listed part is a clique, that the parts are pairwise edge-disjoint, that they cover the entire graph, and that their number equals $s-2a-b$. The supplied finite test covers 898 admissible parameter tuples with unequal cluster sizes and mixed $q/q+1$ clusters. This finite verification supports the construction; the general result is established by the proof above.

## Limitations

The theorem gives a sufficient finite parameter regime for exactness; it does not characterize every heterogeneous cluster join for which the cut bound is attainable. The coefficient $3/2^{5/3}$ is an explicit upper constant obtained from this family, not a claim of the optimal asymptotic constant in $d_n$. Cross-model review has not been performed.

**Same-model review: passed. Cross-model review: not yet performed.**

## References

1. Bo Ning, *On the difference between clique partition and clique covering numbers*, arXiv:2609.20305, 2026. https://arxiv.org/abs/2609.20305
2. P. Erdős, R. Faudree, and E. T. Ordman, *Clique partitions and clique coverings*, Discrete Mathematics 72 (1988), 93--101. https://www.renyi.hu/~p_erdos/1988-04.pdf
3. L. Caccetta, P. Erdős, E. T. Ordman, and N. J. Pullman, *The difference between the clique numbers of a graph*, Ars Combinatoria 19A (1985), 97--106. https://www.renyi.hu/~p_erdos/1985-35.pdf
