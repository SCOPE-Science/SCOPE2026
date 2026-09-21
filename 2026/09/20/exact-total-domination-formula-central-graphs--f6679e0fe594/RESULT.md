# Exact vertex-cover formula for total domination of central graphs

## Statement

Let $G$ be a finite simple graph with no isolated vertices.  Its central graph
$C(G)$ is obtained by subdividing every edge of $G$ once and then joining every
pair of original vertices that are nonadjacent in $G$.

For a set $R\subseteq V(G)$, define the partial edge-cover number
\[
\rho_G(R)=\min\{|F|:F\subseteq E(G),\;R\subseteq V(F)\},
\]
where $V(F)$ is the set of endpoints incident with edges of $F$.  For a vertex
cover $A$ of $G$, put
\[
R_G(A)=\{v\in V(G): A\subseteq N_G[v]\}.
\]
Then
\[
\boxed{
\gamma_t(C(G))=
\min_{A\text{ a vertex cover of }G}
\bigl(|A|+\rho_G(R_G(A))\bigr).
}
\tag{1}
\]

Moreover, for every $R\subseteq V(G)$,
\[
\rho_G(R)=|R|-\nu(G[R]),
\tag{2}
\]
where $\nu$ is the ordinary matching number.  Hence (1) can be written entirely
in terms of vertex covers and induced-subgraph matchings:
\[
\boxed{
\gamma_t(C(G))=
\min_{A\text{ a vertex cover of }G}
\left(|A|+|R_G(A)|-\nu(G[R_G(A)])\right).
}
\tag{3}
\]

A useful equality criterion follows immediately:
\[
\boxed{
\gamma_t(C(G))=\tau(G)
\iff
\text{$G$ has a minimum vertex cover that is a total dominating set of $\overline G$.}
}
\tag{4}
\]

## Proof of the exact formula

Write $c_{uv}$ for the subdivision vertex corresponding to an edge $uv\in E(G)$.
Let $S$ be a total dominating set of $C(G)$ and set
\[
A=S\cap V(G),\qquad
F=\{uv\in E(G):c_{uv}\in S\}.
\]
Every subdivision vertex $c_{uv}$ has exactly the two original endpoints $u,v$
as neighbors.  Since $c_{uv}$ must be dominated by $S$, at least one of $u,v$
belongs to $A$.  Thus $A$ is a vertex cover of $G$.

Now fix an original vertex $v$.  Its original-vertex neighbors in $C(G)$ are
exactly the vertices $a\ne v$ such that $av\notin E(G)$; its remaining neighbors
are the subdivision vertices on edges incident with $v$.  Consequently, if
$v\in R_G(A)$, then every member of $A$ lies in $N_G[v]$, so no member of $A$
is an original-vertex neighbor of $v$ in $C(G)$.  Total domination of $v$ therefore
forces some selected subdivision vertex $c_e\in S$ with $e$ incident with $v$.
Thus $F$ covers every vertex of $R_G(A)$, and
\[
|S|=|A|+|F|\ge |A|+\rho_G(R_G(A)).
\]
Taking the minimum over total dominating sets gives the lower bound in (1).

Conversely, let $A$ be any vertex cover of $G$, and let $F\subseteq E(G)$ cover
$R_G(A)$.  Define
\[
S=A\cup\{c_e:e\in F\}.
\]
Every subdivision vertex is dominated by an endpoint in $A$, because $A$ is a
vertex cover.  If $v\in R_G(A)$, then an edge of $F$ incident with $v$ supplies a
neighboring selected subdivision vertex.  If $v\notin R_G(A)$, choose
$a\in A\setminus N_G[v]$.  Then $a\ne v$ and $av\notin E(G)$, so $a$ and $v$ are
adjacent original vertices in $C(G)$.  Hence every original vertex is also
dominated by $S$.  Therefore $S$ is a total dominating set of $C(G)$, proving
the reverse inequality and hence (1).

## Partial edge covers and matching

Let $M$ be a maximum matching of $G[R]$.  The vertices of $R$ uncovered by $M$
are independent in $G[R]$; otherwise an edge between two of them could be added
to $M$.  Since $G$ has no isolated vertices, choose one incident edge of $G$ for
each uncovered vertex.  These chosen edges are distinct from one another and from
$M$, so together with $M$ they cover $R$ using
\[
|M|+(|R|-2|M|)=|R|-|M|
\]
edges.  Thus $\rho_G(R)\le |R|-\nu(G[R])$.

For the reverse inequality, let $F$ be any edge set covering $R$, and let $M$ be
a maximum matching among the edges of $F$ having both endpoints in $R$.  No edge
of $F$ joins two vertices of $R$ left unmatched by $M$.  Each of the
$|R|-2|M|$ unmatched vertices of $R$ therefore needs a distinct edge of
$F\setminus M$ to cover it.  Hence
\[
|F|-|M|\ge |R|-2|M|,
\]
so $|F|\ge |R|-|M|\ge |R|-\nu(G[R])$.  This proves (2), and (3) follows.

## Equality with the vertex-cover lower bound

The 2019 general lower bound $\tau(G)\le\gamma_t(C(G))$ is immediate from (1).
Equality in (1) can occur at $\tau(G)$ precisely when some minimum vertex cover
$A$ has $R_G(A)=\varnothing$.  The latter condition says that for every
$v\in V(G)$ there is an $a\in A$ with $a\notin N_G[v]$, equivalently a vertex
$a\in A$ adjacent to $v$ in $\overline G$.  This is exactly the statement that
$A$ is a total dominating set of $\overline G$, proving (4).

The 2019 upper bound
\[
\gamma_t(C(G))\le\tau(G)+\rho(G)
\]
also follows from (1), because $\rho_G(R)\le\rho(G)$ for every $R$.  Thus (1)
strictly refines the previous general two-sided estimate by identifying exactly
which original vertices still require subdivision-vertex support after a vertex
cover has been selected.

For example, if $G=K_n$, then $R_G(A)=V(G)$ for every vertex cover $A$, so (1)
recovers
\[
\gamma_t(C(K_n))=n-1+\left\lceil\frac n2\right\rceil.
\]
For sufficiently long paths, a minimum alternating vertex cover has
$R_G(A)=\varnothing$, recovering the known equality with $\tau(P_n)$.

## Literature context and originality

Kazemnejad and Moradi (2019) introduced the general study of total domination in
central graphs.  Their Theorem 1.1 proves the tight bounds
\[
\tau(G)\le\gamma_t(C(G))\le\tau(G)+\rho(G),
\]
and the paper computes exact values for several families, including paths, cycles,
complete graphs and complete multipartite graphs.  The directly inspected full
text also poses further central-graph total-domination questions.  Formula (1)
refines their general theorem to an exact optimization identity for every finite
simple graph without isolated vertices.

Chen, Sohn and Wang (2020) subsequently study the tree case, relate
$\gamma_t(C(T))$ to $\tau(T)$, characterize a tree equality involving
$\alpha(C(T))$, and solve one problem from the 2019 paper.  The accessible abstract
and bibliographic record were inspected; the complete theorem text of that paper
was not directly inspected here, so a differently phrased tree-specialized
antecedent remains a literature risk.  Even if such a tree specialization exists,
(1)--(4) apply to arbitrary graphs without isolated vertices.

Later central-graph work located in the search includes ordinary domination and,
most recently, independent domination.  These concern different parameters.  No
source located in searches by total domination, central graphs, vertex covers,
edge covers, complement formulations and matching formulations stated (1), (3),
or (4).  Originality is therefore claimed only to the best of our knowledge.

## Verification

A finite sanity check is provided in `artifacts/verify_formula.py`.  It enumerates
all connected graphs with at least two vertices in the NetworkX Graph Atlas,
computes the right side of (3) by exhaustive vertex-cover search and matching,
and independently computes $\gamma_t(C(G))$ as a binary mixed-integer linear
program on the central graph.  All 995 graphs agree.  This computation supports,
but does not replace, the proof above.

## Limitations

- Formula (3) is an exact structural identity, not a claim of a polynomial-time
  algorithm for computing $\gamma_t(C(G))$.
- The 2020 central-tree article was checked through its abstract and bibliographic
  record rather than a complete direct reading of its theorem text; this is the
  most relevant residual literature uncertainty.
- Search cannot exclude an equivalent result indexed under different terminology,
  especially a formulation using partial edge covers or total domination in the
  complement.
- Originality is to the best of our knowledge.

## References

1. F. Kazemnejad and S. Moradi, *Total domination number of central graphs*,
   Bulletin of the Korean Mathematical Society 56 (2019), 1059--1075.
   https://doi.org/10.4134/BKMS.b180891
2. X.-G. Chen, M. Y. Sohn and Y.-F. Wang, *Total domination number of central
   trees*, Bulletin of the Korean Mathematical Society 57 (2020), 245--250.
   https://doi.org/10.4134/BKMS.b190162
3. S. Fujita, F. Kazemnejad and B. Pahlavsay, *New classification of graphs in
   view of the domination number of central graphs*, arXiv:2204.10292 (2022).
   https://arxiv.org/abs/2204.10292
4. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar and
   A. Serrano-Díaz, *Independent domination in central graphs*, arXiv:2609.16357
   (2026). https://arxiv.org/abs/2609.16357
