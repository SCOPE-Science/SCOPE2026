# Sharp dissociation-independence gap in connected bipartite graphs

**Same-model review: passed. Independent audit: not yet performed.**

## Statement

Let `diss(G)` denote the dissociation number of a graph `G`, the largest size of a vertex set inducing maximum degree at most 1, and let `alpha(G)` denote its independence number.

### Theorem
Let `G` be a finite simple connected bipartite graph of order `n >= 3`. Then
\[
\operatorname{diss}(G)-\alpha(G)\le \left\lfloor\frac{n-2}{2}\right\rfloor.
\]
The bound is sharp for every `n >= 3`.

Moreover, every equality graph is a tree and can be characterized completely. Write `H(q,r)` for the tree with a center `c`, `q` internally disjoint arms of length 2, and `r` arms of length 1.

- If `n=2m` is even (`m>=2`), equality holds if and only if `G` is `H(m-1,1)`. Thus the extremal graph is unique up to isomorphism.
- If `n=2m+1` is odd (`m>=2`), equality holds if and only if `G` is one of `H(m,0)` or `H(m-1,2)`. Thus there are exactly two extremal isomorphism classes.
- For `n=3`, the two descriptions coincide and give `P_3`.

For completeness, the exceptional connected bipartite graph of order 2 is `K_2`, with `diss(K_2)-alpha(K_2)=1`.

Equivalently, if `tau(G)` is the vertex-cover number and `tau_3(G)` is the minimum 3-path vertex-cover number, then for connected bipartite graphs of order `n>=3`,
\[
\tau(G)-\tau_3(G)\le \left\lfloor\frac{n-2}{2}\right\rfloor,
\]
with exactly the same equality graphs.

## Proof

For every connected graph `G` of order `n>=3`, a dissociation set cannot contain all vertices: otherwise `G` itself would have maximum degree at most 1, impossible for a connected graph on at least three vertices. Hence
\[
\operatorname{diss}(G)\le n-1.
\]
If `G` is bipartite, one of its two color classes has at least `ceil(n/2)` vertices, so
\[
\alpha(G)\ge \left\lceil\frac n2\right\rceil.
\]
Subtracting gives
\[
\operatorname{diss}(G)-\alpha(G)
\le n-1-\left\lceil\frac n2\right\rceil
=\left\lfloor\frac{n-2}2\right\rfloor.
\]

There is also an exact defect decomposition:
\[
\left\lfloor\frac{n-2}2\right\rfloor-
(\operatorname{diss}(G)-\alpha(G))
=
(n-1-\operatorname{diss}(G))
+
(\alpha(G)-\lceil n/2\rceil).
\]
Both terms on the right are nonnegative. Therefore equality in the stated bound holds if and only if
\[
\operatorname{diss}(G)=n-1
\quad\text{and}\quad
\alpha(G)=\left\lceil\frac n2\right\rceil.
\]

Assume equality, and choose a maximum dissociation set `D` of size `n-1`. Let `x` be the unique vertex outside `D`. Since `G[D]` has maximum degree at most 1, it is a disjoint union of `q` copies of `K_2` and `r` isolated vertices. Because `G` is connected, every component of `G-x` has a neighbor of `x`. For a `K_2` component, bipartiteness prevents `x` from being adjacent to both endpoints, since that would create a triangle. Thus `x` has exactly one neighbor in every component of `G-x`. Consequently `G` is exactly `H(q,r)`, and
\[
n=1+2q+r.
\]

For `H(q,r)`, deleting the center leaves `qK_2+rK_1`, so `diss(H(q,r))=n-1` whenever `n>=3`. Its independence number is
\[
\alpha(H(q,r))=\max\{q+r,q+1\}=q+\max\{r,1\}.
\]
If `n=2m`, then `2q+r=2m-1`, so `r` is positive and odd. The equality condition `alpha=m` becomes `q+r=m`; together these equations force
\[
q=m-1,\qquad r=1.
\]
If `n=2m+1`, then `2q+r=2m`. If `r=0`, equality gives `q=m`, producing `H(m,0)`. If `r>=1`, equality requires `q+r=m+1`; together with `2q+r=2m` this forces
\[
q=m-1,\qquad r=2.
\]
This proves the complete equality classification. The listed trees directly attain the bound.

Finally, `tau(G)=n-alpha(G)` and `tau_3(G)=n-diss(G)`, because the complement of a 3-path vertex cover is precisely a dissociation set. Hence `tau-tau_3=diss-alpha`, yielding the equivalent covering statement.

## Context and prior literature

Dissociation number was introduced in the node-deletion setting by Yannakakis. The dual 3-path vertex-cover language was developed subsequently; the 2013 work on vertex k-path covers explicitly records the complement relation between 3-path covers and dissociation sets.

The most directly relevant comparison is Bock, Pardey, Penso, and Rautenbach (2023), which studies improvements of `2 alpha(G) >= diss(G)`. Its full accessible text gives degree-sensitive bounds for connected bipartite graphs and notes tree extremals for those bounds. The inspected theorem statements and proofs do not state the fixed-order maximum of `diss-alpha`, the exact defect decomposition above, or the parity-sensitive complete equality classification.

Searches also covered the equivalent 3-path vertex-cover formulation and the earlier literature on computing dissociation number in bipartite graphs. No equivalent fixed-order theorem was located.

## Verification

`artifacts/verify_bipartite_gap.py` independently checks:
- every connected bipartite graph in the NetworkX Graph Atlas (orders 2 through 7), by direct subset enumeration; and
- every nonisomorphic tree through order 17, using dynamic programs for `alpha` and `diss`.

The computed maxima and extremal isomorphism-class counts agree with the theorem. Expected output is recorded in `artifacts/expected_output.txt`.

## Limitations

Originality is to the best of our knowledge. An equivalent statement could exist in unindexed literature or under the dual terminology of 3-path vertex cover / 3-path vertex deletion. The fixed-order result is elementary once the two tight constituent bounds are juxtaposed; its substantive content is the forced-tree equality structure and complete parity-sensitive classification. The theorem concerns finite simple connected bipartite graphs.

## References

1. M. Yannakakis, *Node-Deletion Problems on Bipartite Graphs*, SIAM Journal on Computing 10 (1981), 310-327. https://doi.org/10.1137/0210022
2. B. Brešar, M. Jakovac, J. Katrenič, G. Semanišin, A. Taranenko, *On the vertex k-path cover*, Discrete Applied Mathematics 161 (2013), 1943-1949. https://doi.org/10.1016/j.dam.2013.02.024
3. F. Bock, J. Pardey, L. D. Penso, D. Rautenbach, *Relating dissociation, independence, and matchings*, Discrete Applied Mathematics 322 (2022), 160-165. https://arxiv.org/abs/2202.01004
4. F. Bock, J. Pardey, L. D. Penso, D. Rautenbach, *Relating the independence number and the dissociation number*, Journal of Graph Theory 104 (2023), 320-340. https://arxiv.org/abs/2205.03404
5. R. Boliac, K. Cameron, V. V. Lozin, *On computing the dissociation number and the induced matching number of bipartite graphs*, Ars Combinatoria 72 (2004), 241-253. https://combinatorialpress.com/ars-articles/volume-072-ars-articles/
