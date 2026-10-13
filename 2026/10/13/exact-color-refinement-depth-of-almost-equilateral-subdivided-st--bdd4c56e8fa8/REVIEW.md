# Review

## Correctness

PASS. The proof reduces round-\(r\) colors on a tree to rooted depth-\(r\) truncations, using the standard universal-cover characterization of color refinement. For the stated spider family, those truncations are captured exactly by clipped distances to the center and the leaf on the same arm. The two stabilization thresholds arise from two independent obstructions: the short and long leaves cannot split before round \(a+1\), and the long arm retains at least two indistinguishable internal positions until round \(\lceil c/2\rceil\). The converse checks that no other collisions survive beyond the maximum of those thresholds.

The standalone checker directly recomputed all refinement partitions on \(4860\) parameter triples and compared intermediate partitions with the claimed descriptor rule in \(10650\) round-level checks.

## Originality

PASS with residual literature risk. The closest primary source inspected was Krebs--Verbitsky, arXiv:1407.3175, especially its definition of color refinement and Lemma 2.6 identifying colors with truncated universal covers. That source provides the general mechanism but not the almost-equilateral subdivided-star formula.

Targeted searches using “subdivided star,” “spider tree,” “color refinement,” “1-WL,” “Weisfeiler--Leman,” “equitable partition,” and “stabilization” did not locate a matching theorem. Semantic-database results on spider trees concerned unrelated invariants such as curvature distortion. Existing path results are not equivalent: the branching center is a persistent typed endpoint, and the exceptional-arm threshold \(a+1\) has no path analogue.

Residual risk remains that a specialized graph-isomorphism or tree-canonization source states the same formula under different terminology.

## Value

PASS. Subdivided stars are a canonical first branching family beyond paths, and color-refinement iteration count is a standard depth parameter in finite model theory and graph isomorphism. The formula isolates two distinct mechanisms—symmetry breaking at the exceptional branch and inward propagation along the longest arm—and exhibits a genuine discontinuity between the equilateral case and an arbitrarily small arm-length perturbation. The exact all-round descriptor is also reusable for related logical-depth calculations.

Self-review: passed. Independent audit: not yet performed.
