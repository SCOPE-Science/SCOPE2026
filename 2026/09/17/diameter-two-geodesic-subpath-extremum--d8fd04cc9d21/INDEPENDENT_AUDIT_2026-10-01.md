# Independent audit — 2026-10-01

## Final claim

Balanced complete bipartite graphs uniquely maximize geodesic subpaths at diameter two

## Disposition

**Passed.** Correctness, originality, and value all pass for the final claim as stated in `RESULT.md`; no claim repair is required.

## Correctness

For any simple \(n\)-vertex graph \(H\), if \(c_x\) is the number of edges crossing from \(N(x)\) to its complement, then summing over \(x\) gives \(\sum_x c_x=2m(H)+2p_3(H)\), where \(p_3\) counts induced three-vertex paths. Since \(c_x\le d(x)(n-d(x))\le\lfloor n^2/4\rfloor\), one obtains \(m+p_3\le (n/2)\lfloor n^2/4\rfloor\). Equality forces every vertex cut complete and balanced; the nonadjacency relation then yields the balanced complete bipartite graph (with the small \(n=3\) weighted-lemma exception harmless because \(K_3\) has diameter one). For a graph of diameter exactly two, every geodesic has length 0, 1 or 2, so \(gpn(G)=n+m+p_3\), proving the stated extremum. An independent exhaustive labeled-graph check for \(3\le n\le6\) reproduced the bound and equality counts.

## Originality

The 2026 primary paper defines the geodesic subpath number, gives a general exponential upper bound, and explicitly leaves maximal-graph questions open; its full text does not contain a diameter-two theorem. The closest induced-open-triangle literature maximizes \(p_3\) alone, while the audited lemma maximizes the weighted quantity \(m+p_3\), which is exactly what diameter-two geodesic counting requires.

### Equivalent formulations

Searches:
- Resultary semantic search for geodesic subpath number diameter two balanced complete bipartite weighted induced P3
- Web searches for geodesic subpath number plus diameter two and for weighted edge/open-triangle extremals

Evidence:
- Resultary's exact match was this record; a later SCOPE path-blow-up record concerns lower bounds outside diameter two, not this theorem.

Reasoning: The theorem is equivalent to a sharp weighted \(m+p_3\) inequality only after the diameter-two geodesic decomposition; no prior source stating that weighted inequality was located.

### Broader coverage

Searches:
- Knor, Sedlar, Škrekovski and Zhang, Counting Geodesic Paths in Graphs, Mediterranean J. Math. 23 (2026), article 171
- Pyatkin, Lykhovyd and Butenko, The maximum number of induced open triangles in graphs of a given order, Optimization Letters 13 (2019)

Evidence:
- Knor et al. give the invariant, a general upper bound, formulas for selected families and open extremal problems; Pyatkin et al. show balanced complete bipartite graphs maximize induced open triangles alone.

Reasoning: Neither source implies the weighted edge-plus-open-triangle extremum: maximizing \(p_3\) alone does not control the additional \(m\) term.

### Exact database or table

The theorem is an all-order proof, not a finite-table extrapolation.

Searches:
- Searches for exact \(gpn\) tables and induced-open-triangle extremal tables for diameter-two graphs

### Claim versus prior implication

The audited weighted inequality supplies a new implication needed to solve the natural diameter-two subclass and is not a corollary of the two closest prior results separately.

Evidence:
- The primary paper's general upper bound is much broader but not sharp here; its conclusion notes even the bipartite extremal problem remains interesting. The open-triangle theorem omits the edge term.

### Source inspections

- **Counting Geodesic Paths in Graphs** — NOT_COVERING. Material read: Open full text including the definition, Theorem 2, family computations, conclusion, complete-bipartite discussion and Problem 15. Evidence: The paper gives no diameter-two extremal theorem and explicitly leaves further maximal classes open. Source: https://doi.org/10.1007/s00009-026-03159-3
- **The maximum number of induced open triangles in graphs of a given order** — PARTIAL_COMPONENT_NOT_COVERING. Material read: Abstract/result statement and bibliographic scope. Evidence: It maximizes induced open triangles alone, not \(m+p_3\). Source: https://doi.org/10.1007/s11590-018-1330-2

### Residual risks

- A weighted open-triangle inequality could exist under different terminology, but targeted implication and alias searches did not locate one; the primary geodesic paper itself does not state the diameter-two result.

## Value

Diameter two is a natural, broad metric class in which the new invariant becomes exactly tractable. The result gives an all-order sharp maximum, a unique extremal graph up to isomorphism, and a reusable weighted induced-\(P_3\) inequality; it also advances the source paper's explicit extremal program rather than selecting an arbitrary finite slice.

## Limitations

The extremal theorem is for connected graphs of diameter exactly two; it does not solve the unrestricted or all-bipartite maximum problem for the geodesic subpath number.
