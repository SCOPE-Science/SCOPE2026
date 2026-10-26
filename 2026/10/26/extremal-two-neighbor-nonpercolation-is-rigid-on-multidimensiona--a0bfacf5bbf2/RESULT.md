# Extremal two-neighbor nonpercolation is rigid on multidimensional cycle tori

## Finding
Let \(r\geq 1\) and \(k_1,\ldots,k_r\geq4\) be integers. Put
\[
G=\mathop{\square}_{j=1}^{r}C_{k_j},\qquad N=\prod_{j=1}^{r}k_j,\qquad K=\max_j k_j,\qquad t=|\{j:k_j=K\}|.
\]
A vertex set \(S\subseteq V(G)\) is \(P_3\)-convex when every vertex outside \(S\) has at most one neighbor in \(S\). The largest cardinality of a **proper** such set is
\[
\boxed{c_{P_3}(G)=N-\frac{2N}{K}.}
\]
There are exactly \(tK\) maximizers, and all are the complements of the following coordinate slabs: choose one coordinate \(j\) with \(k_j=K\) and one cyclically adjacent pair \(\{a,a+1\}\subseteq\mathbb Z/K\mathbb Z\); the *omitted* vertices are precisely those with \(j\)th coordinate in this pair. No other maximizer exists.

Equivalently, in synchronous or asynchronous two-neighbor bootstrap percolation on \(G\), every starting set of size strictly exceeding \(N-2N/K\) infects all vertices, and the exactly \(tK\) largest nonpercolating starting sets are those described above. The numerical threshold is already implied by Saraf--Borse--Mundhe's minimum-degree bound; the contribution here is the full equality-case rigidity and the exact optimizer census, including all tied maximum side lengths.

## Assumptions and scope
All graphs are finite, simple, undirected. The cycle \(C_k\) is the simple graph on \(\mathbb Z/k\mathbb Z\), with edges joining consecutive residues; every factor length is at least four. The Cartesian product has vertices \((x_1,\ldots,x_r)\), with an edge when exactly one coordinate moves by one along its cycle. Its degree is \(2r\). A \(P_3\)-convex set is a fixed point of the two-neighbor infection closure. The empty set is convex, the full vertex set is convex but is excluded by the word *proper*. The parameter \(c_{P_3}\) is the maximum cardinality of a proper convex set (not the usual hull number). Multiplicities count **labelled vertex subsets**, not orbits under graph automorphisms.

## Proof
**Equivalence to high-minimum-degree complements.** Write \(T=V(G)\setminus S\). The condition that every vertex \(v\in T\) has at most one neighbor in \(S\) is equivalent to
\[
T\ne\varnothing,\qquad \delta(G[T])\geq2r-1.
\]
Thus we classify all smallest nonempty vertex subsets inducing minimum degree at least \(2r-1\).

We prove by induction on \(r\) that their minimum size is \(2N/K\) and every minimizer is a thickness-two coordinate slab along a factor whose length is \(K\).

**Base \(r=1\).** A nonempty induced subgraph of a cycle having minimum degree at least one contains an edge and thus at least two vertices. On exactly two vertices, this forces a cyclically adjacent pair. There are precisely \(k_1\) such pairs, as claimed.

**Inductive step.** Permute coordinates so that \(k_1\leq\cdots\leq k_r=K\), and let \(H=\square_{j<r}C_{k_j}\), with \(M=|V(H)|=N/K\). Partition \(G\) into \(K\) cyclic slices \(H_0,\ldots,H_{K-1}\), each isomorphic to \(H\), and write \(T_i=T\cap H_i\). Within a slice there are \(2r-2\) possible neighbors; two further neighbors lie in adjacent slices.

Suppose first that at least one slice is empty. Traverse the cyclic sequence beginning immediately after an empty slice and let \(i\) be the first index with \(T_i\ne\varnothing\). Every vertex of \(T_i\) lacks its neighbor in the preceding slice. To have at least \(2r-1\) neighbors in \(T\), it must therefore have **all** \(2r-2\) neighbors within \(H_i\) and its successor in \(T_{i+1}\). Connectivity of \(H\) makes \(T_i=V(H_i)\), and all its successor-coordinate neighbors must belong to \(T_{i+1}\), so \(T_{i+1}=V(H_{i+1})\). Consequently \(|T|\geq2M\); equality entails that these two adjacent full slices comprise all of \(T\). These are exactly the slabs orthogonal to the last coordinate.

Now suppose every slice is nonempty. Each induced \(H[T_i]\) has minimum degree at least \((2r-1)-2=2r-3\). By the induction hypothesis, with \(L=k_{r-1}\leq K\),
\[
|T|=\sum_{i=0}^{K-1}|T_i|\geq K\frac{2M}{L}\geq2M.
\]
If equality holds, necessarily \(K=L\) and every \(T_i\) is a minimum induced subgraph of \(H\) of minimum degree \(2r-3\). By induction, each \(T_i\) is a two-adjacent-layer slab in a longest factor of \(H\); each of its selected vertices therefore has **exactly** \(2r-3\) neighbors inside its slice. To achieve \(2r-1\) neighbors in \(G[T]\), both neighbors in the preceding and succeeding slices must be present. Thus \(T_i\subseteq T_{i-1}\cap T_{i+1}\) for every \(i\). Going around the cycle forces all \(T_i\) to be the same coordinate subset. Hence \(T\) is one of the induction-hypothesis slabs extended across the entire last factor. Its thin factor also has length \(L=K\).

Conversely, any thickness-two slab orthogonal to a coordinate of length \(K\) is an induced subgraph of minimum degree \(2r-1\): its vertices have two neighbors in each of the other \(r-1\) factors and exactly one neighbor along the thin factor. The displayed bound and exhaustive equality classification follow.

Different slabs are distinct because each factor length is at least four, and a two-layer restriction along one coordinate is distinguishable from restrictions along other coordinates. There are \(K\) cyclic adjacent pairs in each of the \(t\) longest factors, hence exactly \(tK\) minimum complements and maximal proper convex sets.

Finally, the closure of any nonpercolating starting set \(A\) under the two-neighbor rule is a proper \(P_3\)-convex superset \(\overline A\). Thus \(|A|\leq|\overline A|\leq N-2N/K\). At equality, \(A=\overline A\), so every maximum nonpercolating starting set is one of the listed convex sets. This proves both percolation assertions.

## Verification
The standalone script `VERIFY.py` reconstructs Cartesian-product adjacency independently from the theorem's induction. It examines every vertex subset of sizes up to the predicted minimum complement size for \(C_4\square C_4\), \(C_4\square C_5\), and \(C_5\square C_5\), checking minimum induced degree and all equality cases; it also checks all predicted slabs and deterministic random subsets in eight higher-dimensional examples. Run it with `python3 VERIFY.py`. Finite checks are corroboration, not proof of the unlimited-dimensional theorem.

## Relationship to prior work
Dourado, Grippo, Lin, and Protti (2026, arXiv:2603.04706v1) study \(P_3\)-convex-set enumeration and give algorithms and extremal results for several other graph classes. Their available full HTML text does not give the present multidimensional-torus equality classification.

Saraf, Borse, and Mundhe (2020, arXiv:2001.11781v1, Section 2, especially Lemmas 2.3--2.5) prove the *previously known* minimum-size bound for subgraphs of \(\square C_{k_j}\) with prescribed minimum degree. At minimum degree \(2r-1\), their bound is \(2N/K\) and their construction provides a width-two slab. Accordingly, neither the numerical bound nor the construction by itself is claimed as new. The additional result here is that **every** extremizer must be such a slab, with a complete count including ties, and that the equality classification transfers to largest nonpercolating starting configurations.

Borse and Saraf (2018/2019, DOI:10.1016/j.akcej.2018.07.001) study existence and orders of cubic subgraphs of Cartesian products of cycles. Their discussed existence results do not state the present all-dimensional optimizer classification. Priority under other terminology for equality cases remains a risk.

## Limitations
All cyclic factor lengths are at least four. This is an extremal theorem, not a formula for the entire \(P_3\)-convex-set polynomial or all smaller closed sets. It treats threshold two, not higher-neighbor percolation. The size threshold is not new; the equality-case rigidity and optimizer enumeration are the claimed refinements. Independent mathematical review and a comprehensive historical-priority audit have not been performed.

## References
1. M. C. Dourado, L. N. Grippo, M. C. Lin, F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1 (first posted 2026-03-05), https://arxiv.org/html/2603.04706v1.
2. J. B. Saraf, Y. M. Borse, G. Mundhe, *On conditional connectivity of the Cartesian product of cycles*, arXiv:2001.11781v1 (2020), https://arxiv.org/abs/2001.11781.
3. Y. M. Borse, J. B. Saraf, *Existence of 3-regular subgraphs in Cartesian product of cycles*, AKCE International Journal of Graphs and Combinatorics 16 (2019), 332--342, DOI:10.1016/j.akcej.2018.07.001.
