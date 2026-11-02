# Maximal mutual-visibility sets in clique expansions of trees and sparse spectra of clique paths

## Finding

Let \(T\) be any finite nonempty tree. Replace each \(v\in V(T)\) by a *labeled* clique \(B_v\) of positive order \(w_v\); for distinct base vertices, join their whole cliques if and only if the base vertices are adjacent. Denote the resulting graph by \(G(T,\mathbf w)\). A subset \(X\) is a **mutual-visibility set** if for every two distinct \(a,b\in X\) there exists an \(a,b\)-geodesic whose internal vertices avoid \(X\). Let
\[
Q_{T,\mathbf w}(z)=\sum_{X\text{ inclusion-maximal mutual-visibility}}z^{|X|}.
\]

**Tree expansion theorem.** If \(T\) has one vertex \(v\), then \(Q_{T,\mathbf w}(z)=z^{w_v}\). For \(|V(T)|\ge2\), let \(\mathcal H(T)\) comprise all connected subtrees \(H\) of \(T\) on at least two vertices such that
\[
\deg_H(v)\ge2\quad\Longrightarrow\quad N_T(v)\subseteq V(H).
\tag{1}
\]
For \(H\in\mathcal H(T)\), denote its degree-one and degree-at-least-two vertex sets by \(L(H)\) and \(I(H)\), respectively. Then
\[
\boxed{Q_{T,\mathbf w}(z)=\sum_{H\in\mathcal H(T)}\left(\prod_{v\in I(H)}w_v\right)z^{\sum_{v\in L(H)}w_v+\sum_{v\in I(H)}(w_v-1)}.}
\tag{2}
\]
In particular, the corresponding maximal sets are **exactly** those obtained by taking every vertex in each leaf fiber, every vertex except one freely chosen omitted vertex in each internal fiber, and no vertices outside \(H\).

**Uniform clique paths.** For \(n\ge2\) and \(m\ge1\), put \(G_{m,n}=P_n\circ K_m\), equivalently \(P_n\boxtimes K_m\) (in this special case the strong and lexicographic products agree). Every eligible subtree is a consecutive interval on at least two base vertices, so
\[
\boxed{Q_{m,n}(z)=\sum_{j=0}^{n-2}(n-j-1)m^jz^{2m+j(m-1)}.}
\tag{3}
\]
For \(m\ge2\), all \(n-1\) powers in (3) are distinct and have positive coefficients. If \(m\ge3\), exactly \(m-2\) whole-number cardinalities lie strictly between successive supported powers, regardless of \(n\). These are unbounded gaps even in connected **unit interval graphs**: assign every vertex in the \(i\)-th fiber the unit interval \([i,i+3/2]\), uniformly rescaled to length one, to represent this graph by intersections. The minimum and maximum maximal-set orders are \(2m\) and \(nm-n+2\). The coefficient at the largest order is \(m^{n-2}\); the total count for \(m\ge2\) is
\[
Q_{m,n}(1)=\frac{m^n-nm+n-1}{(m-1)^2}.
\tag{4}
\]
For \(m=1\), coinciding powers add to \(Q_{1,n}(z)=\binom n2 z^2\).

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled; \(T\) is a tree, \(w_v\in\mathbb Z_{\ge1}\). For a nontrivial subtree \(H\), its vertices have \(H\)-degree at least one; the phrase *internal vertex* means degree at least two, not an internal vertex of the expanded graph. Count a maximal set once, regardless of which geodesics witness visibility. The empty set, singleton sets, and sets in a single fiber may be mutual-visible but cannot be inclusion-maximal when \(T\) has an edge.

## Proof

**1. A fiberwise geodesic criterion.** If \(u\ne v\) in the tree, any shortest path in \(G(T,\mathbf w)\) between a vertex of \(B_u\) and a vertex of \(B_v\) follows the unique \(u,v\)-path in \(T\), choosing exactly one vertex in every intermediate fiber. The shortest length is \(d_T(u,v)\). Distinct vertices of a common fiber are adjacent. Thus two selected vertices in distinct fibers can avoid other selected vertices on a geodesic if and only if **each intermediate fiber has at least one unselected vertex**. This applies even when an intermediate fiber contains no selected vertices.

**2. Steiner-hull criterion.** Let \(X\) occupy at least two distinct fibers and let \(H\) be the unique smallest subtree containing all occupied base vertices. Every leaf of \(H\) is occupied. By the criterion in step 1, \(X\) is mutual-visible if and only if \(B_v\setminus X\ne\varnothing\) for every \(v\in I(H)\). Necessity follows by choosing selected vertices in occupied leaves on opposite sides of any internal \(v\); sufficiency follows because all intermediate base vertices of any occupied pair lie in \(I(H)\).

**3. Saturation forced by inclusion-maximality.** Suppose \(X\) is inclusion-maximal and \(H\) is its Steiner hull. If a leaf fiber has a missing vertex, adding it preserves the hull and cannot introduce a fully selected internal fiber. Hence every leaf fiber is full. If some internal fiber contains at least two unselected vertices, add one of them; an unselected vertex remains there and the hull is unchanged. Hence every internal fiber has exactly **one** omitted vertex. By step 2, neither a set occupying just one fiber nor the empty set can be maximal in a nontrivial base tree: one can add a vertex in an adjacent fiber and retain mutual visibility.

**4. The closed-internal-vertex condition.** If any \(v\in I(H)\) has a neighbor \(u\notin V(H)\), adding a vertex from \(B_u\) does not make any formerly full leaf fiber internal; \(v\) was already internal and remains missing one vertex. Therefore the addition is mutual-visible, a contradiction. Thus condition (1) is necessary.

Conversely, assume (1). Construct \(X\) by filling leaf fibers and taking all but one vertex of each internal fiber. Step 2 proves visibility. Adding any omitted vertex of an internal fiber makes that fiber full, obstructing every geodesic between two selected vertices in leaf fibers lying on opposite sides of it. Any outside base vertex \(u\) has a unique attachment \(a\) to \(H\) along the path to \(H\); by (1) this attachment must be a **leaf** of \(H\). Adding a vertex in \(B_u\) now forces the formerly full fiber \(B_a\) to lie internally on the shortest path from the new vertex to a selected vertex of another leaf fiber of \(H\). That geodesic has no unselected choice in \(B_a\), so visibility is destroyed. Hence \(X\) is inclusion-maximal. The leaves of \(H\) remain occupied and span \(H\), so \(H\) and the omitted internal vertices are uniquely recoverable. This proves the bijection and (2).

**5. Counting for paths.** A connected subtree of \(P_n\) with at least two vertices is a consecutive interval of length \(j+2\) for some integer \(0\le j\le n-2\). Every internal vertex of such an interval has both path neighbors inside it, so condition (1) holds. There are \(n-j-1\) positions, two leaf fibers each of order \(m\), and \(j\) internal fibers each with \(m\) possible omitted vertices and \(m-1\) selected vertices. Its contribution is therefore \((n-j-1)m^jz^{2m+j(m-1)}\). Summing proves (3). The support and minimum/maximum claims follow. Summing the arithmetico-geometric series yields (4). For \(m=1\), all exponents equal two, with total \(\sum_{j=0}^{n-2}(n-j-1)=\binom n2\).

## Verification

The accompanying standard-library program `verify.py` independently builds the clique-expanded graph from its edges, computes **all shortest-path interior masks** by breadth-first search, enumerates vertex subsets, and tests mutual visibility and inclusion-maximality directly. It compares the exact cardinality coefficients against a separate enumeration of admissible base subtrees and the leaf/internal weights. The completed direct test returned:

`VERIFY_OK graph_instances=214 candidate_subsets=185798 maximum_order=12`

These are finite checks, not a proof for arbitrary orders. The all-order proof is given above. Execute `python3 verify.py` from an extracted package directory.

## Relationship to prior work

Cicerone, Di Stefano, Klavžar, and Yero investigate mutual visibility in strong products and give scalar bounds and formulas for several product classes; these results motivate the strong-product specialization but do not supply the full maximal-set enumeration above [1]. Brešar and Yero study the *minimum order of inclusion-maximal* mutual-visibility sets (the lower invariant), not the multiplicities of every possible maximal-set size [2]. Bujtás, Klavžar, and Tian introduce polynomials enumerating mutual-visibility sets of all sizes, including a general relationship to maximal sets; that general relationship does not constitute formula (2) or its closed clique-path specialization [3]. The ordinary-tree leaf/Steiner characterization in [4] covers the one-vertex-per-fiber limit and is not claimed here as new. The principal contribution is the weighted tree expansion bijection together with the labeled enumerator and unbounded gaps in unit interval graphs. No claim of exhaustive publication priority is made.

## Limitations

The theorem assumes the base is a tree and every fiber is a clique joined completely along base edges; arbitrary chordal graphs or nonclique fibers are not covered. The formula for a general tree is a sum over eligible subtrees, not a claimed polynomial-time counting algorithm. Numerical tests do not replace the proof. Existing studies of maximal mutual-visibility sets may contain equivalent formulations under different terminology, so novelty remains subject to external literature review; no independent mathematical audit is asserted.

## References

[1] S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, *Mutual-visibility in strong products of graphs via total mutual-visibility*, arXiv:2210.07835, first public version 2022-10-14, https://arxiv.org/abs/2210.07835.

[2] B. Brešar, I. G. Yero, *Lower (total) mutual-visibility number in graphs*, arXiv:2307.02951, first public version 2023-07-06, https://arxiv.org/abs/2307.02951.

[3] C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066, first public version 2024-12-04, https://arxiv.org/abs/2412.03066.

[4] Tonny K. B. and M. Shikhi, *On the Mutual-Visibility of Tree Graphs*, arXiv:2601.08270, first public version 2026-01-13, https://arxiv.org/abs/2601.08270.
