# Review of Edge general position number of crown graphs

## Correctness
PASS. In a crown graph every geodesic containing three edges is a length-\(3\) path between one deleted matched pair. Encoding the edge \(a_i b_j\) as the arc \(i\to j\) converts those forbidden triples exactly into transitive directed triangles. For every arc of a transitive-triangle-free digraph, endpoint out-neighborhoods are disjoint and endpoint in-neighborhoods are disjoint. Summing both inequalities and applying Cauchy--Schwarz yields the sharp upper bound \(\lfloor n^2/2\rfloor\). A balanced bidirected cut realizes equality. Exhaustive checking of every edge subset for \(n=3,4,5\) independently matches the theorem.

## Originality
PASS. The foundational 2021 paper was inspected in full searchable text and solves hypercubes, trees, and grids while explicitly leaving bipartite graphs as a direction; no crown or complete-bipartite treatment occurs. The 2024 extremal paper was inspected through its open full text and treats size-minus-one, small values, and block graphs, with no crown or complete-bipartite occurrence. The available full text of the 2025 paper on diameter-\(3\) and value-\(4\) regimes was also searched and contains no crown or complete-bipartite occurrence. Exact searches using crown, \(K_{n,n}\) minus a perfect matching, deleted matching, and the transitive-triangle formulation did not locate the all-\(n\) formula. The already known special cases \(\operatorname{Cr}_3\cong C_6\) and \(\operatorname{Cr}_4\cong Q_3\) are explicitly excluded from the originality claim as isolated prior cases.

## Value
PASS. Crown graphs are a standard dense regular bipartite family and were not covered by the main exact families in the introducing paper. The theorem gives a sharp quadratic law and a structural reduction to a clean directed-extremal problem, rather than a one-off computation. It also unifies the previously known \(C_6\) and \(Q_3\) special cases and supplies an exact benchmark for the broader bipartite direction identified in the foundational work.

Self-review: passed. Independent audit: not yet performed.
