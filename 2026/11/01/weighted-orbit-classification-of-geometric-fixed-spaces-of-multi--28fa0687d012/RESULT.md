# Weighted-orbit classification of geometric fixed spaces of multipartite total cut complexes

## Finding
Let \(G=K_{a_1,\ldots,a_k}\) be a finite complete multipartite graph, \(k\ge2\), and let \(d\ge2\). Let \(\Gamma\) be any group of graph automorphisms preserving each of the \(k\) named parts setwise. Suppose \(a_i\ge d\) for each part. List the sizes of the \(\Gamma\)-orbits contained in part \(i\) as positive integers \(w_{i,1},\ldots,w_{i,r_i}\), with sum \(a_i\). Define \(T_i=a_i-d\), and let \(Q_i\) be the augmented weighted-threshold simplicial complex on these \(r_i\) orbit labels, with faces the subsets of total orbit weight at most \(T_i\). Then the geometric fixed-point space of the total \(d\)-cut complex has the homotopy type
\[
\left|\Delta_d^t(G)\right|^\Gamma\simeq \Sigma^{k-1}(Q_1*\cdots*Q_k),
\]
where joins and suspensions are interpreted in the augmented simplicial sense (in particular \(\{\varnothing\}\) represents a formal \((-1)\)-sphere in joins).

There is an explicit **integral homology and sphere-wedge classification**. Sort each part's weights as \(u_{i,1}\le\cdots\le u_{i,r_i}\), and set
\[
P_i(z)=\sum_{\substack{B\subseteq\{2,\ldots,r_i\}\\T_i-u_{i,1}<\sum_{j\in B}u_{i,j}\le T_i}}z^{|B|}.
\]
For every integer \(j\ge0\), the reduced integral Betti number is
\[
\operatorname{rank}\widetilde H_j\!\left(|\Delta_d^t(G)|^\Gamma;\mathbb Z\right)
=[z^{j-k+2}]\prod_{i=1}^kP_i(z),
\]
and all reduced integral homology is free abelian. The fixed space is homotopy equivalent to the wedge of the corresponding spheres (or contractible when every coefficient is zero). This formula can have *simultaneously nonzero Betti numbers in different dimensions*, even though the ambient complete multipartite cut complex has homology concentrated in one dimension.

For example, take \(G=K_{9,4}\), \(d=4\), and an orbit profile \((1,1,2,2,3)\) on the first part and \((4)\) on the second. The resulting geometric fixed space is \(S^2\vee S^2\vee S^3\), whereas the ambient space is a wedge of \(56\) five-spheres (the ambient type is known from the literature).

## Assumptions and scope
We use the standard total cut complex convention: its facets are complements of independent \(d\)-sets of graph vertices. For a complete multipartite graph, every independent set is contained in a single part; consequently, the ordinary and total \(d\)-cut complexes coincide on this graph family. The action preserves each part, but need not act transitively in any part and may couple actions between different parts. All data below depend only on the orbit sizes within each part, not on the abstract subgroup structure. Empty realizations and ghost vertices are handled with augmented complexes. The main theorem assumes \(a_i\ge d\) for all \(i\).

If some part size is less than \(d\) but another is at least \(d\), the geometric fixed space is contractible; if all part sizes are less than \(d\), the total cut complex and its fixed space are void. These boundary cases are separate from the sphere-counting formula.

## Proof
**1. Fixed-space triangulation.** If a finite group acts simplicially on a complex, a point is geometrically fixed precisely when its barycentric coordinates are constant on each vertex orbit. In each invariant face, the orbit barycenters form a simplex; gathering these simplices yields a PL triangulation whose vertices are admissible orbits. For an orbit-label set \(S\), its union of original vertices is a face of \(\Delta_d^t(G)\) precisely when the complement contains an independent \(d\)-set. This occurs if and only if there is some part \(i\) with
\[
\sum_{u\in S\cap\Omega_i}w_u\le a_i-d=T_i.
\]
Thus the fixed locus is PL homeomorphic to the simplicial complex \(K\) on all orbit labels whose faces satisfy this disjunction. In particular, the geometric fixed space is not confused with the subcomplex of vertexwise fixed original vertices.

**2. Exact Alexander dual description.** Let \(E_i\) be the complex on the orbit labels in part \(i\) whose faces have total weight at most \(d-1\). The join \(E=E_1*\cdots*E_k\) contains precisely those orbit-label subsets which, in each part, have total weight at most \(d-1\). By taking complements of orbit subsets inside the full orbit-label set, the face condition in step 1 becomes
\[
K=E^\vee=(E_1*\cdots*E_k)^\vee.
\]
Within each part, \(Q_i=E_i^\vee\): indeed, \(S\in E_i^\vee\) if and only if the complement of \(S\) has total weight at least \(d\), equivalently \(\sum_{u\in S}w_u\le a_i-d\). For nonfull \(E_i\), the Alexander dual of a join is the union of two cones, whose intersection is the join of the two individual Alexander duals:
\[
(E_A*E_B)^\vee=(E_A^\vee*\Delta_B)\cup(\Delta_A*E_B^\vee).
\]
Each term is contractible, and their intersection is \(E_A^\vee*E_B^\vee\). The union therefore has the homotopy type of its suspension. Induction over the parts gives \(K\simeq\Sigma^{k-1}(Q_1*\cdots*Q_k)\); this also covers \(Q_i=\{\varnothing\}\) under the stated augmented convention. If a part has size \(a_i<d\), its corresponding \(E_i\) is the full simplex; its orbit labels cone off the fixed locus provided another part admits an independent \(d\)-set. If none does, there are no facets at all.

**3. One-part weighted-threshold decomposition.** Fix a part and abbreviate the sorted weights by \(u_1\le\cdots\le u_r\) and the budget by \(T=a-d\). In \(Q=\{S:\sum_{j\in S}u_j\le T\}\), the closed star of the least-weight vertex is the subcomplex of all faces \(S\) for which \(S\cup\{1\}\) is allowed, and hence is contractible whenever \(u_1\le T\). Every face outside this star is a subset \(B\subseteq\{2,\ldots,r\}\) whose weight satisfies \(T-u_1<\sum_{j\in B}u_j\le T\). Such a face is maximal in \(Q\), and every proper subface is in the star: removing any weight at least \(u_1\) leaves weight at most \(T-u_1\). Consequently, \(Q\) is obtained from a contractible star by gluing one simplex of dimension \(|B|-1\) along its entire boundary for each such \(B\). The attaching maps are null-homotopic in the star. Hence \(Q\simeq\bigvee_B S^{|B|-1}\), with the standard augmented interpretation of \(|B|=0\). If \(u_1>T\), then \(Q=\{\varnothing\}\), and its enumerator is \(P(z)=1\). This directly proves the polynomial \(P_i\) formula, including torsion-freeness.

**4. Joins and degrees.** The reduced homology of joins of these sphere wedges is given by tensor products with the usual degree shift. Joining one sphere of dimension \(|B_i|-1\) from each part gives dimension \(\sum_i|B_i|-1\); the additional \(k-1\) suspensions yield dimension \(\sum_i|B_i|+k-2\). Multiplicities multiply, producing the coefficient formula. Because the homotopy decomposition is explicitly into wedges of spheres, all integral homology is free.

**5. Mixed-dimensional instance.** For weights \((1,1,2,2,3)\) and budget \(5\), the qualifying subsets among the remaining weights \((1,2,2,3)\) have weights in \((4,5]\): two pairs \((2,3)\) and the triple \((1,2,2)\). Thus \(P_1(z)=2z^2+z^3\). The second part has weight \((4)\) and budget zero, so \(P_2(z)=1\). The two-part coefficient formula gives \(\widetilde\beta_2=2\), \(\widetilde\beta_3=1\), and zero otherwise, proving the claimed mixed wedge. A known nonequivariant calculation gives ambient rank \(\binom83\binom33=56\) in degree five.

## Verification
The standalone Python script `verify.py` constructs the orbit-simplex complex directly from the original cut-facet rule, independently computes finite mod-two boundary ranks, and compares them to the coefficient formula. It exhaustively compares 2,474 two-part orbit profiles with total sizes between two and five and at most eight orbit labels; separately checks the mixed-dimensional \(K_{9,4}\) example; and checks 80 seeded multipartite profiles with at most eight orbit labels. Exact output from the packaged script:

```
exhaustive bipartite weight-profile checks: 2474
mixed-dimensional example [[1, 1, 2, 2, 3], [4]] threshold 4 Betti {2: 2, 3: 1}
80 seeded multipartite profiles checked (up to 8 orbit vertices)
```

These are finite mod-two checks; the all-parameter integral and homotopy statements follow from the mathematical proof, not from finite enumeration.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue (2024), **Topology of Cut Complexes of Graphs**, arXiv:2304.13675, Theorems 7.4, 7.8 and 7.9, already prove equivariant homotopy models and describe the **ambient** nonequivariant sphere count and homology representation for multipartite ordinary cut complexes. Their equivariant model is strong prior coverage, and fixed-point homotopy types are implicitly determined by that model. The present statement does **not** claim discovery of the ambient wedge type, the general equivariant model or the existence of fixed-point models. Its additional explicit content is the calculation of the geometric fixed loci directly in terms of arbitrary within-part orbit weights, including a closed full-dimensional Betti polynomial and mixed-dimensional wedge phenomena. These calculations do not appear as such in the cited theorems; the explicit coefficient formula requires the orbit-weight threshold reduction and the star-attachment argument above.

Carnero Bravo (2026), **Total cut complexes and their duals**, arXiv:2602.21427, motivates the total-cut formulation and develops its Alexander duals and examples; it does not provide these fixed-space orbit-weight formulas. These comparisons concern scientific statements and their logical implications, not merely terminology or titles.

## Limitations
The subgroup must preserve individual part classes; automorphisms exchanging equal-sized parts are not classified here. The main coefficient formula assumes every part admits an independent \(d\)-set. The statement does not produce a canonical equivariant splitting of the ambient integral homology, nor does it infer fixed spaces from rational invariant subspaces. Although the cited 2024 equivariant homotopy theorem substantially overlaps the setup, it does not itself list the explicit orbit-weight fixed-space Betti polynomial. Possible equivalent derivations in other literature remain a risk; there has been no independent expert validation.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, especially Section 7.1 and Theorems 7.4, 7.8–7.9. https://arxiv.org/html/2304.13675v2
2. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first public version 24 February 2026). https://arxiv.org/abs/2602.21427
