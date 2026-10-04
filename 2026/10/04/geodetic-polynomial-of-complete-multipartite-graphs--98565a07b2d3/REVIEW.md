# Same-model review

## Correctness
**PASS.** In a complete multipartite graph, an omitted vertex \(v\in V_i\) can lie internally on a shortest path between selected vertices only when those endpoints are two selected vertices in one common part \(V_j\) with \(j\ne i\). Conversely any such pair has a length-two geodesic through \(v\). This proves the criterion \(s_i<n_i\Rightarrow H(S)\setminus\{i\}\ne\varnothing\) exactly. Partitioning subsets by zero, one, or at least two heavy parts gives the polynomial without approximation. The accompanying exhaustive checker reconstructs shortest-path coverage from graph distances and agrees with the criterion, coefficients, and minimum formula on every tested profile.

## Originality
**PASS for the stated all-set characterization and ordinary geodetic polynomial.** The closest broader prior work computes only the minimum geodetic number on distance-hereditary graphs, while the complete-multipartite literature surfaced in the comparison concerns strong or edge variants. The geodetic-polynomial paper establishes the invariant but its accessible abstract only says that selected specific graphs are computed. Searches by complete-multipartite terminology, complete-bipartite specialization, geodesic convexity, and polynomial/enumerator aliases did not expose the displayed arbitrary-part all-set formula. The scalar geodetic-number corollary is explicitly excluded from the novelty claim.

Residual risk remains because the full text of the original geodetic-polynomial paper was not accessible through the inspected public record, and one later strong-geodetic PDF could not be fetched directly. Neither accessible record supplied the ordinary arbitrary complete-multipartite all-set polynomial.

## Value
**PASS.** The geodetic polynomial is an established enumerative invariant, and complete multipartite graphs are a canonical diameter-two family. The result upgrades minimum-cardinality information to an exact description of every feasible set and every coefficient of the cardinality enumerator. The criterion is structural rather than an arbitrary finite slice: it identifies exactly which part profiles generate geodesic coverage.

Same-model review: passed. Independent audit: not yet performed.
