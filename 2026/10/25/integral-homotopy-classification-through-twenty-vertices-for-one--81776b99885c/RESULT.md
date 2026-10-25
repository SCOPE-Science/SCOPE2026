# Integral homotopy classification through twenty vertices for one-arc-punctured bidirected cycles

## Finding
Let \(D_n\) be the bidirected cycle on \(\mathbb Z/n\mathbb Z\) with the single backward arc \(1\to0\) deleted. For every integer \(4\le n\le20\), the simplicial complex \(X(D_n)\) of directed linear forests has an integral homotopy equivalence
\[
X(D_n)\simeq S^{n-2}\vee\bigvee^{r(n)} S^{\lfloor(n-2)/2\rfloor},\qquad
r(n)=\begin{cases}2&n\equiv0\pmod4,\\0&n\equiv1\pmod4,\\1&n\equiv2,3\pmod4.\end{cases}
\]
A zero-fold wedge contributes nothing. This is a classification of seventeen consecutive finite orders, not an assertion for larger \(n\).

## Assumptions and scope
The digraph has vertices \(0,\ldots,n-1\), forward arcs \(f_i:i\to i+1\) for all \(i\) and backward arcs \(b_i:i+1\to i\) for \(1\le i<n\), with indices modulo \(n\). A face of \(X(D_n)\) is a set of arcs forming disjoint directed simple paths (isolated vertices allowed). The only directed cycles compatible with the indegree/outdegree-at-most-one condition in this underlying cycle are the two-edge opposite-orientation cycles and the two coherently oriented full cycles. The all-backward cycle is unavailable because \(b_0\) is deleted.

## Proof
**1. Simplicial fibers.** An admissible backward-arc subset \(B\subseteq\{b_1,\ldots,b_{n-1}\}\) permits exactly those forward arcs \(f_i\) for which \(B\cap\{b_{i-1},b_i,b_{i+1}\}=\varnothing\), interpreting \(b_0\) as absent. For \(B\ne\varnothing\), forward subsets form the full simplex on the permitted forward arcs; for \(B=\varnothing\), they form the boundary of the full \((n-1)\)-simplex (the all-forward directed cycle is forbidden). In each nonempty forward simplex, match faces by toggling its least-index forward arc. For \(B=\varnothing\), toggle \(f_0\) except where this would complete the forbidden all-forward face. This leaves its face \(\{f_1,\ldots,f_{n-1}\}\) unmatched, together with the usual base vertex when the empty face is not paired. The matchings are acyclic in each fixed-\(B\) fiber, hence jointly acyclic by the order-preserving fiber map to the Boolean poset of backward subsets.

**2. Remaining upper filter.** A backward-only face survives exactly if \(B\) covers every forward index, equivalently
\[
\bigcup_{b_j\in B}\{j-1,j,j+1\}=\mathbb Z/n\mathbb Z.
\]
Call this upward-closed family \(\mathcal D_n\). Match within \(\mathcal D_n\) successively by toggling \(b_1,b_2,\ldots,b_{n-1}\), always pairing only two currently unmatched faces. For each of the seventeen integers \(4\le n\le20\), the attached standalone program enumerates **all** members of \(\mathcal D_n\), builds **every** covering relation, reverses exactly the selected matching relations, and exhaustively topologically sorts the resulting directed Hasse graph. It thereby proves acyclicity for every case, not merely a random sample. It also proves the following complete list of remaining backward-only faces (where \(\{1,3,\ldots,n-1\}\) means odd indices):

- If \(n\equiv1\pmod4\), none.
- If \(n\equiv2\pmod4\), the single face \(\{b_1,b_3,\ldots,b_{n-1}\}\).
- If \(n\equiv3\pmod4\), the single face indexed by \(\{1,2,5,6,\ldots,n-2\}\), taking blocks \(1,2\pmod4\) with the last incomplete block as specified by the verification algorithm.
- If \(n\equiv0\pmod4\), the two faces indexed by all odd indices and by the complete blocks \(1,2\pmod4\).

All have simplex dimension \(\lfloor(n-2)/2\rfloor\). Since this is an upper filter in the entire face poset, an upward gradient step cannot leave it; the union with the forward-fiber matching is therefore acyclic. Consequently \(X(D_n)\) has a Morse CW model with one vertex, one \((n-2)\)-cell, and exactly \(r(n)\) cells of dimension \(\lfloor(n-2)/2\rfloor\).

**3. The high-dimensional attaching map is null.** Let \(A\) be the full-forward boundary, a simplicial \(S^{n-2}\) inside \(X(D_n)\). The vertex map \(f_i\mapsto f_i\), \(b_i\mapsto f_i\) takes every face to a *proper* forward subset and is a simplicial retraction onto \(A\). Indeed, if the image contained every \(f_i\), the absence of \(b_0\) forces \(f_0\), which rules out \(b_1,b_{n-1}\); successive propagation forces all \(f_i\), the forbidden directed cycle. Thus the inclusion of \(A\) is split-injective on integral homology, and the unique Morse top-dimensional cell carries a primitive class. For \(n\ge6\), the lower Morse skeleton is a simply connected wedge of spheres of dimension at least two. Relative Hurewicz for the one-cell attachment and the degree-one map from \(A\) force the unique top attaching class to vanish: in the relative homotopy exact sequence, a generator of the relative \((n-2)\)-group comes from the sphere inclusion. Hence the CW model splits as the asserted wedge. For \(n=5\), there are no lower positive cells, so the model is \(S^3\). At \(n=4\), direct face enumeration gives the full-forward tetrahedral boundary \(S^2\), one filled backward triangle, and exactly three mixed edges from distinct backward to distinct forward vertices; this is \(S^2\vee S^1\vee S^1\).

## Verification
Run `python3 punctured_bidirected_verify.py` with Python 3. The verifier computes the coverage predicate independently of the face enumerator, all domination-filter faces, all second-stage matched edges and all reversed Hasse relations for each \(4\le n\le20\), verifies every relevant DAG by topological sorting, and compares the final critical faces with their explicit closed pattern. For \(4\le n\le10\), it additionally constructs every directed-forest face directly from arc compatibility and verifies that a separately executed full lexicographic matching leaves precisely the same critical cells. The deterministic recorded output is in `punctured_bidirected_verify.out` and ends with `ALL_OK 17 orders; 164172 dominating faces; 1070871 verified Hasse edges`.

## Relationship to prior work
Caputi, Collari and Smith (arXiv:2601.05670v1, January 9, 2026), Conjecture 2.11, proposed the **integral homology** ranks of the one-arc-deleted bidirected polygon and reported computational checks only up to fourteen vertices. The theorem above instead establishes complete **integral homotopy types** for seventeen orders, including six beyond that reported numerical range, with a full discrete-Morse acyclicity check and a geometric argument excluding higher attaching-map obstructions. Their Theorem 2.10 concerns the full bidirected cycle, not the one-arc deletion. Their Proposition 2.13 requires deleting at least three consecutive reverse arcs, which is not this situation. Earlier work by Caputi, Collari, Di Trani and Smith studies distinct oriented polygons, paths and related digraphs. Published exact equivariant homology for unpunctured bidirected polygons does not imply the punctured homotopy classification.

## Limitations
The complete enumeration is restricted to \(4\le n\le20\): the visible period-four pattern is **not** established for arbitrary \(n\). Numerical Morse output on its own would not exclude a Hopf-type top-cell attachment; the proof uses the explicit simplicial retraction and relative Hurewicz for this essential step. No assertion is made for the completely bidirected cycle, for removal of two reverse arcs, or for different multipath definitions. The finite verification is deterministic but has not undergone independent external validation. Bibliographic searches cannot rule out unindexed results.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (first public version January 9, 2026), particularly Definition 1.2, Theorem 2.10, Conjecture 2.11, Proposition 2.13 and Section 3. https://arxiv.org/abs/2601.05670
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, published in Mathematika 70 (2024), e12235. https://arxiv.org/abs/2208.04656
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, for discrete Morse reduction.
