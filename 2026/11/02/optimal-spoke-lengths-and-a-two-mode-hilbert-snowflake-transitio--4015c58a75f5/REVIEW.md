# Review of the weighted-wheel Hilbert-snowflake classification

## Correctness — PASS

The claimed interval and optimization are derived from the exact all-parameter zero-sum quadratic identity in `RESULT.md`. The boundary distances are computed explicitly, including ties at half-unit and unit spoke lengths. The decomposition into mean and cycle-contrast spaces is orthogonal for the powered-distance form; the highest contrast eigenvalue is obtained by the minimum Fourier frequency of the rim adjacency matrix. The global scalar coefficient is strictly increasing in the exponent, and the contrast coefficient is strictly increasing when the rim nonneighbor distance exceeds one. These facts prove the absence of reentrant negative type and establish endpoint equality spaces. The crossover and unique spoke-length maximizer follow from an explicit monotonicity calculation, not numerical optimization.

The standalone metric-matrix checker `verify.py` reconstructs all shortest-path distances without using the closed metric formulas and checks 10,362 numerical assertions, including finite dimensions, perturbations of both sides of the exponent, critical equality multiplicities, and quadratic form identities. Those checks are supplementary; the symbolic proof covers all integers and the entire real parameter range. Its asymptotic calculations rely on Taylor estimates with fixed radial weight where stated.

## Originality — PASS, qualified

The most relevant primary sources were inspected at their substantive result sections. Obata's 2017 wheel paper proves the **unweighted** exponent-one quadratic embedding constant and its parity distinction. Lou–Obata–Huang (arXiv:2001.06752, 2020) give general join-graph QEC machinery and, in Example 3.6, recover the **unweighted** wheel result. Neither provides the weighted radial metric, a variable-powered distance matrix, the two-mode crossover, the sharp radial optimizer, or critical Hilbert embedding ranks. Robertson (arXiv:2309.16070, 2023) states the general negative-type/Hilbert correspondence, and its calculated graph examples are complete bipartite and Hamming metrics, not this weighted wheel family.

The most closely related indexed wheel results encountered concern the Löwner ellipsoid of the wheel's symmetric edge polytope, the polytope's Euclidean inradius, and linear Lipschitz extensions from regular Euclidean polygons. They optimize or classify different objects and do not imply the claimed powered geodesic-distance threshold. Existing wheel QEC results are important specializations, rather than proof of the variable-exponent radial phase diagram. Related earlier findings involving cycle heat flow, Lipschitz-free cycle geometry, and graph negative type were checked for scientific overlap; they do not assert the present radial-wheel exponent classification.

Residual originality risk: an equivalent distance-kernel computation might exist under generalized roundness, Euclidean distance matrix completion, or radial two-distance metric terminology without being located by the searches. The novelty judgment is a best-knowledge assessment, not certification of historical priority. The theorem is deliberately phrased to credit the general Fourier and Schoenberg criteria.

## Mathematical value — PASS

The metric wheel interpolates naturally between a half-length radial hub, whose rim distances are equilateral, and the usual unit-edge wheel. The threshold changes controlling eigenspace at a **unique, exactly characterized radial weight**. The optimum solves a genuine geometric design question (which radial length maximizes Hilbert-snowflake embeddability), while the critical nullity jumps according to the parity of the rim. The sharp \(2/n\) boundary layer distinguishes a global balancing obstruction from a high-frequency oscillatory obstruction. For four rim vertices, the optimal embedding becomes an actual square with its Euclidean center. These structural and geometric conclusions are stronger than merely replaying the known ordinary unweighted QEC formula.

The result is restricted to uniform radial weights in the interval where all rim nonneighbors have equal geodesic distance; it makes no statement about nonuniform wheels, alternative edge lengths, arbitrary graph joins, or distorted Hilbert embeddings. Historical equivalence risk remains, but the proved natural optimization, complete parameter classification, and endpoint geometry give substantive mathematical value.

## Closest primary literature and limits

1. N. Obata, *Quadratic Embedding Constants of Wheel Graphs* (2017), DOI `10.4036/iis.2017.S.02`, Theorem 1.1 and Section 4. The inspected four-page text treats unit-edge wheel QEC only.
2. Z. Lou, N. Obata and Q. Huang, *Quadratic Embedding Constants of Graph Joins*, arXiv:2001.06752v1 (posted 2020-01-19), especially Theorem 3.1 and Example 3.6 in the full HTML version. The formulas concern the original unpowered shortest-path matrix.
3. G. Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, arXiv:2309.16070v1 (posted 2023-09-27), Sections 1 and 4. General definitions and metric embeddings; graph examples are not weighted wheels.

Self-review: passed. Independent audit: not yet performed.
