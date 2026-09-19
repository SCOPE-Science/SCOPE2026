# A missing-edge range for consecutive spanning-forest ratios

Let $G$ be a simple connected graph on $n\ge 2$ vertices, with $m$ edges. For $1\le s\le n$, let $F_s(G)$ denote the number of spanning forests of $G$ with exactly $s$ connected components; thus $F_1(G)=T(G)$ is the number of spanning trees. Put
\[
\rho_s(G):=\frac{F_s(G)}{F_{s-1}(G)},\qquad 2\le s\le n.
\]

Bencs and Csikvári recently conjectured that for every simple connected $n$-vertex graph,
\[
\rho_s(G)\ge \rho_s(K_n)
\]
for every $2\le s\le n$, with equality only for $K_n$ [1, Conjecture 5.8]. They proved the $s=2$ case [1, Lemma 3.9].

## Main theorem

For every $2\le s\le n$, if
\[
\boxed{\quad m\le \binom n2-\binom{n-s}{2},\quad}
\]
then
\[
\boxed{\quad \rho_s(G)\ge \rho_s(K_n).\quad}
\]
Moreover, equality is possible only when $G=K_n$.

Equivalently, if $h=\binom n2-m$ is the number of missing edges of $G$, then the conjectured ratio inequality is guaranteed at level $s$ whenever
\[
\boxed{\quad h\ge \binom{n-s}{2}.\quad}
\]
Thus a graph with $h$ missing edges automatically satisfies the conjecture throughout the high-component tail $n-s\le r$, where $\binom r2\le h$.

## Sparse and planar consequences

For $s\ge 3$, the edge threshold above is smallest at $s=3$ and equals
\[
\binom n2-\binom{n-3}{2}=3n-6.
\]
Combining the theorem for $s\ge3$ with the already established universal $s=2$ case of Bencs--Csikvári gives:

**Corollary.** If $G$ is simple, connected, and
\[
m\le 3n-6,
\]
then the full consecutive-ratio conjecture holds for every $2\le s\le n$.

In particular, every connected simple planar graph satisfies
\[
\boxed{\quad
\frac{F_s(G)}{F_{s-1}(G)}\ge
\frac{F_s(K_n)}{F_{s-1}(K_n)}
\quad(2\le s\le n),
\quad}
\]
with equality at any level only when $G=K_n$. For planar graphs with $n\ge5$, all these inequalities are therefore strict.

Multiplying the consecutive inequalities also gives, for these graphs,
\[
\frac{F_s(G)}{T(G)}\ge \frac{F_s(K_n)}{T(K_n)}
\qquad(2\le s\le n),
\]
so the corresponding componentwise conjecture [1, Conjecture 5.7] follows as well.

The argument does not establish the stronger LYM/normalized-matching property discussed in [1]. Indeed [1] notes that the forest poset of the book graph with five triangles already fails the LYM property; that graph nevertheless satisfies the consecutive-ratio inequalities by the sparse corollary above. Thus the present sufficient condition bypasses that stronger, generally false route.

## Proof

Consider the bipartite inclusion graph whose left class is the set of $s$-component spanning forests of $G$ and whose right class is the set of $(s-1)$-component spanning forests, with adjacency when the latter is obtained from the former by adding one edge.

Every $(s-1)$-component forest has exactly $n-s+1$ edges. Deleting any one of them produces an $s$-component forest, so every vertex on the right has degree exactly $n-s+1$.

An $s$-component forest has exactly $n-s$ edges. It has at most
\[
m-(n-s)=m-n+s
\]
unused graph edges available to add, and only unused edges joining two different forest components are valid extensions. Hence its degree in the inclusion graph is at most $m-n+s$. Double-counting inclusion edges gives
\[
(n-s+1)F_{s-1}(G)
\le (m-n+s)F_s(G),
\]
and therefore
\[
\boxed{\quad
\rho_s(G)\ge \frac{n-s+1}{m-n+s}.
\quad} \tag{1}
\]

Now perform the same count for $K_n$. If an $s$-component forest has component orders $a_1,\dots,a_s$, its number of valid one-edge extensions is exactly
\[
\sum_{i<j}a_i a_j
=\binom n2-\sum_i\binom{a_i}{2}.
\]
For positive integers $a_i$ summing to $n$, this quantity is minimized when the component sizes are
\[
(n-s+1,1,\dots,1).
\]
Thus every $s$-component forest of $K_n$ has at least
\[
D_{n,s}:=\binom n2-\binom{n-s+1}{2}
\]
valid extensions. A second double count yields
\[
(n-s+1)F_{s-1}(K_n)
\ge D_{n,s}F_s(K_n),
\]
so
\[
\boxed{\quad
\rho_s(K_n)\le \frac{n-s+1}{D_{n,s}}.
\quad} \tag{2}
\]

The hypothesis is exactly what is needed to compare the denominators:
\[
\begin{aligned}
m\le \binom n2-\binom{n-s}{2}
&=D_{n,s}+n-s,\\
\text{hence}\qquad m-n+s&\le D_{n,s}.
\end{aligned}
\]
Combining (1) and (2) proves
\[
\rho_s(G)\ge \rho_s(K_n).
\]

For strictness, if
\[
m<\binom n2-\binom{n-s}{2},
\]
then $m-n+s<D_{n,s}$, so the comparison is already strict. It remains to consider equality in the edge threshold. If $2\le s\le n-2$, the complete-graph bound (2) is itself strict: besides forests with component profile $(n-s+1,1,\dots,1)$, $K_n$ also has forests with profile
\[
(n-s,2,1,\dots,1),
\]
whose extension degree is strictly larger than $D_{n,s}$. Hence the average extension degree is larger than the minimum. If $s\in\{n-1,n\}$, the threshold equals $\binom n2$, so equality in the threshold forces $G=K_n$. This proves the stated equality condition.

## Verification

The accompanying script directly enumerates acyclic edge subsets in every connected graph from the NetworkX graph atlas on $2$ through $7$ vertices. It checks the theorem by exact integer cross-multiplication, not floating-point arithmetic, and separately checks the planar corollary.

The recorded run checked 995 connected graph types, 5,332 level instances satisfying the missing-edge criterion, and all 4,474 forest-ratio levels across 774 planar graph types. No violation was found. This finite verification is supporting evidence only; the theorem is proved above.

## Originality and limitations

To the best of our knowledge, the missing-edge criterion and the planar/sparse corollaries are not stated in the inspected literature. The September 2026 Bencs--Csikvári preprint explicitly presents the consecutive-ratio statement as Conjecture 5.8 and proves only its $s=2$ case; its inspected text does not contain the threshold above or a planar-graph resolution. Searches using consecutive spanning-forest ratios, forest component ratios, normalized matching/LYM terminology, planar graphs, and missing-edge formulations found no equivalent result.

Two older sources remain the main residual originality risks. Myrvold's 1992 paper on counting $k$-component forests was inspected at the abstract/metadata level and is algorithmic in focus. Teranishi's 2005 paper studies the number of spanning forests and gives several bounds, but the full text was not inspected here. An unpublished Eaton--Kook--Thoma manuscript titled *Monotonicity for Complete Graphs and Symmetric Complete Bipartite Graphs* is cited in OEIS and may contain related inequalities for the complete-graph forest sequence; no accessible full text was located. Either older source could overlap with an ingredient such as (2), although no evidence found indicates the cross-graph missing-edge theorem or planar corollary is already present.

The criterion is sufficient, not claimed necessary. It leaves the low-component ratios of graphs denser than the displayed threshold unresolved, except for $s=2$, which is already known universally from [1]. No independent validation is asserted.

## References

[1] F. Bencs and P. Csikvári, *An inequality for the number of independent sets of matroids with an application to the forest-tree ratio of graphs*, arXiv:2609.18611v1 (submitted 16 September 2026). https://arxiv.org/abs/2609.18611

[2] W. Myrvold, *Counting k-component forests of a graph*, Networks 22 (1992), 647--652. https://doi.org/10.1002/net.3230220704

[3] Y. Teranishi, *The number of spanning forests of a graph*, Discrete Mathematics 290 (2005), 259--267. https://doi.org/10.1016/j.disc.2004.10.014
