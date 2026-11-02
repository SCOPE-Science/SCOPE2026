# Self-review

## Correctness — PASS

For the explicitly defined 12-vertex 30-edge icosahedral graph, the recursive matching enumeration exhausts each state exactly once by matching the least remaining vertex. Every possible pair is checked for legal 4/6-cycle symmetric difference; independently a dual dodecahedral construction enumerates all simple 4/6-cycles and toggles them. Both programs assert 125 states, 300 four-flip edges, 580 six-flip edges, six 4-flip components sized 120+5, exact edge partition by five frozen states, 880 total edges and the full distance degree profiles. BFS from every vertex certifies eccentricity 3 and the sharp cutoff. All assertions passed on extracted actual source programs.

The proof is a finite exact theorem. The complete matching recurrence, the exact cycle predicate and exhaustive BFS from each configuration make the computation a certificate for the stated finite graph, not a sampled heuristic. The independent dual construction prevents agreement solely from sharing the same graph representation or flip classifier.

## Originality — PASS, qualified

Known icosahedron five-edge-colouring, five cubic matchings and the 125 total are explicitly excluded. Direct comparisons with Pisanski--Servatius, Van Cleemput--Zamfirescu 1-factorization Kempe equivalence, Bonamy et al. 4-flip complexity, Ito et al. unrestricted cycle flips and matching/edge-colouring tables show none of the inspected statements imply the claimed restricted 4/6-cycle graph metric. Three actual semantic research-record searches returned no covering result; this is not proof of global novelty, and unavailable full book material remains a residual risk.

The closest source is Pisanski--Servatius, *Configurations from a Graphical Viewpoint*, chapter 3 (DOI 10.1007/978-0-8176-8364-1); the source already describes the five special cubic matchings and their full edge partition. Van Cleemput--Zamfirescu (arXiv:2008.03173), Proposition 3, proves **two Kempe equivalence classes of whole 1-factorizations**, which is a distinct reconfiguration model. Bonamy et al. (arXiv:1904.06184) supply a broad four-flip framework, and Ito et al. (arXiv:1907.01700) study arbitrary alternating-cycle changes. These are genuinely relevant and credited. None of the available examined passages specifies the 4/6-cycle restricted icosahedron matching graph. The complete publisher chapter text was not available and could hide an equivalent fact; a semantic search is not proof of novelty.

## Value — PASS

This is a natural sharp local-transformation threshold on a canonical five-regular Platonic graph: length four strands precisely five configurations, but length six connects all, with complete 125-state exact transition geometry and a uniform diameter three. The five frozen perfect matchings recover a classical symmetric 1-factorization dynamically, and precise degree/distance distributions quantify mobility rather than merely reproducing a known matching count. The finite object is structurally canonical, not an arbitrary parameter slice.

The sharp cutoff and complete metric quantify a natural obstruction and activation under constrained reconfiguration on a standard polyhedral graph. The isolated-set edge partition is an explanatory structural feature, though its geometric existence is already known.

## Limits

Exact finite fixed-graph classification only. No arbitrary-graph algorithm, infinite-family extension, or independent scholarly audit. Known icosahedral 5-edge-colouring and five special cubic matchings excluded from new contribution. Publisher full-text chapter not accessible; alternative historical index terms remain an originality risk.

Self-review: passed. Independent audit: not yet performed.
