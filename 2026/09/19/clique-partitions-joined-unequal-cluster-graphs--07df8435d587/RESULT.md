# Exact clique partition numbers for joined unequal cluster graphs

Let
\[
J_h(r,s):=(hK_r)\vee(hK_s),\qquad 2\le r\le s,
\]
where each side is a disjoint union of `h` cliques and the join adds every edge between the two sides.  Write `cc(G)` for the minimum number of cliques covering the edges of `G`, and `cp(G)` for the minimum number of cliques partitioning its edges.

## Theorem

Put
\[
\tau(s):=\chi'(K_s)=
\begin{cases}
s-1,&s\text{ even},\\
s,&s\text{ odd}.
\end{cases}
\]
If `h >= tau(s)`, then
\[
\boxed{\operatorname{cc}(J_h(r,s))=h^2}
\]
and
\[
\boxed{
\operatorname{cp}(J_h(r,s))
=h^2rs-2h\binom r2-h\binom s2.
}
\]
Equivalently, the Erdős--Faudree--Ordman crossing-edge lower bound is sharp on this entire two-parameter family.  Hence
\[
\boxed{
\operatorname{cp}(J_h(r,s))-\operatorname{cc}(J_h(r,s))
=h^2(rs-1)-2h\binom r2-h\binom s2.
}
\]

For the symmetric specialization `r=s=k`, this gives
\[
\operatorname{cp}((hK_k)\vee(hK_k))
=h^2k^2-3h\binom k2
\]
whenever `h >= chi'(K_k)`.  Thus the even-`k` formula of Ning's Proposition 3.1 extends to odd `k` as well: for odd `k`, it holds for every `h >= k`.

No novelty is claimed for the boundary case `r=1`: the older theorem for a graph joined to a sufficiently large independent set already covers that case.

## Proof

Write
\[
A=A_0\dot\cup\cdots\dot\cup A_{h-1},\qquad
B=B_0\dot\cup\cdots\dot\cup B_{h-1},
\]
with each `A_i` a copy of `K_r` and each `B_j` a copy of `K_s`.

### Clique covering number

The `h^2` sets `A_i union B_j` are cliques and cover every edge, so `cc(J_h(r,s)) <= h^2`.

Conversely choose one representative from every `A_i` and every `B_j`.  These `2h` representatives induce `K_{h,h}`.  A clique of `J_h(r,s)` can meet at most one `A_i` and at most one `B_j`, because distinct clusters on the same side are anticomplete.  Hence a clique covers at most one edge of the selected `K_{h,h}`.  Its `h^2` edges therefore force at least `h^2` covering cliques.  Thus `cc(J_h(r,s))=h^2`.

### Lower bound for the partition number

Across the cut `(A,B)` there are
\[
S=h^2rs
\]
edges, while the numbers of internal edges are
\[
a=h\binom r2,\qquad b=h\binom s2.
\]
Since `r<=s`, we have `a<=b`.  The Erdős--Faudree--Ordman inequality
\[
\operatorname{cp}(G)\ge S-a-b-\min\{a,b\}
\]
therefore gives
\[
\operatorname{cp}(J_h(r,s))
\ge h^2rs-2h\binom r2-h\binom s2.
\]

### A partition attaining the bound

Take optimal proper edge-colorings
\[
E(K_r)=R_0\dot\cup\cdots\dot\cup R_{u-1},
\qquad
E(K_s)=S_0\dot\cup\cdots\dot\cup S_{t-1},
\]
where `u=chi'(K_r)` and `t=chi'(K_s)`.  The color classes are matchings.  They may be chosen so that every class of `K_q` has size `q/2` for even `q`, and `(q-1)/2` for odd `q`.  Consequently `u<=t` and, after relabeling colors,
\[
|R_c|\le |S_c|\qquad(0\le c<u).
\]
For `c>=u`, put `R_c=emptyset`.

Use cluster indices modulo `h`.  Since `h>=t`, for each fixed `i` the cluster pairs
\[
(A_i,B_{i+c}),\qquad 0\le c<t,
\]
are all distinct.

For every `i,c`, inject `R_c` into `S_c`.  For every paired pair of edges `e in R_c` and `f in S_c`, include the `K_4` induced by the endpoints of `e` and `f`.  For each unpaired edge `f in S_c`, include a triangle consisting of the endpoints of `f` together with one fixed vertex of `A_i`.

These cliques are pairwise edge-disjoint.  Internal edges are plainly used once.  For crossing edges it is enough to examine one cluster pair `(A_i,B_{i+c})`.  Both `R_c` and `S_c` are matchings: distinct `K_4`'s are vertex-disjoint inside that pair; the triangles use disjoint `B`-edges; and a triangle cannot repeat a crossing edge of a `K_4` because its `B`-edge is disjoint from every paired `B`-edge in the same matching.  Different cluster pairs have disjoint sets of crossing edges.  Use every still-unused crossing edge as a two-vertex clique.

There are `a` copies of `K_4` and `b-a` triangles.  The `K_4`'s use `4a` crossing edges and the triangles use `2(b-a)`, so the number of remaining crossing-edge cliques is
\[
S-4a-2(b-a)=S-2a-2b.
\]
The total number of cliques is therefore
\[
a+(b-a)+(S-2a-2b)=S-2a-b,
\]
which is exactly the lower bound.  This proves the theorem.

## Context and significance

Ning's 2026 paper determines the correct `Theta(n^{4/3})` deficit in the maximum possible difference `cp(G)-cc(G)`.  Its lower-bound construction is the symmetric joined-cluster graph `(hK_k) vee (hK_k)`, and Proposition 3.1 determines both clique parameters when `k` is even and `h>=k-1`, using a one-factorization of `K_k`.

The theorem above shows that the same crossing-edge bound remains exactly attainable after two simultaneous changes: the cluster sizes may be unequal, and the parity restriction disappears.  The construction explains the asymmetric equality mechanism: internal edges on the smaller-cluster side are paired with internal edges on the larger-cluster side inside `K_4`'s, while the surplus internal edges on the larger side are absorbed by edge-disjoint triangles.  An optimal edge-coloring of the larger clique schedules both types without crossing-edge collisions.

The 1988 Erdős--Faudree--Ordman paper supplies the crossing-edge inequality used for the lower bound.  It also treats examples with internal edges on both sides, but the relevant examples there are lower-bound calculations rather than this exact joined-cluster formula.  The 1985 Caccetta--Erdős--Ordman--Pullman paper contains an exact theorem for joining a graph to a sufficiently large independent set; this includes `r=1` but not the `r,s>=2` theorem stated here.

## Verification

`artifacts/verify_joined_cluster_partition.py` implements the edge-coloring construction directly and checks that every graph edge appears in exactly one generated clique.  The recorded verification covers all `2 <= r <= s <= 10` at `h=chi'(K_s)` and `h=chi'(K_s)+1`, for 90 parameter cases.  It also checks the resulting clique count against the closed formula.  This finite verification supports the construction but is not used in the general proof.

## Limitations

The sufficient threshold `h>=chi'(K_s)` is not claimed to be optimal; the same formula may hold for additional smaller values of `h`.  The theorem keeps the same number `h` of clusters on the two sides.  The case `r=1` is already covered by older work and is not part of the originality claim.  Originality is asserted only to the best of our knowledge: older clique-partition literature is broad and uses several equivalent set-representation and covering formulations, so an equivalent construction under different terminology remains a residual risk.  Independent audit has not been performed.

## References

1. B. Ning, *On the difference between clique partition and clique covering numbers of graphs*, arXiv:2608.11536 (2026). https://arxiv.org/abs/2608.11536
2. P. Erdős, R. Faudree, and E. T. Ordman, *Clique partitions and clique coverings*, Discrete Mathematics 72 (1988), 93--101. https://doi.org/10.1016/0012-365X(88)90197-5
3. L. Caccetta, P. Erdős, E. T. Ordman, and N. J. Pullman, *The difference between the clique numbers of a graph*, Ars Combinatoria 19A (1985), 97--106. https://www.renyi.hu/~p_erdos/1985-35.pdf
