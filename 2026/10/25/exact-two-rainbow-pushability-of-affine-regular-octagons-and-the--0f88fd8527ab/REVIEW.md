# Scientific review: exact two-rainbow pushability of affine-regular octagons

## Correctness — PASS
The definition is the two-law, independent, collectively balanced vertex statistic of [1]. For a polygon, sharing a facet is equivalent to equal or adjacent indices, so the displayed bilinear objective matches the event. Separate linear-program reductions ensure an optimum with at most three positive masses in each law. On a fixed support face the quadratic interior/boundary argument reduces the global upper bound to a finite exact stationary computation. The supplied standalone verifier explores all 920 symmetry-reduced support pairs with exact \(\mathbb Q(\sqrt2)\) arithmetic, enumerating 126 admissible stationary candidates and obtaining the reported maximum. Direct exact checks establish positivity, normalization, collective balance, and attainment by the displayed two-plus-three support witness. The 12 separately balanced extreme laws and their 144 pairs give the sharp comparison value. Finite numerical optimization was only an independent sanity check, not an infinite proof.

## Originality — PASS with recorded residual risks
The primary paper [1] defines the invariant and proves a general facet-depth bound, but the inspected Sections 3–4 and the open-problem discussion do not state an octagonal computation or a separate-balance comparison. Published-record searches under terms including regular octagon, vertex laws, common facets, balance, and \(\pi_2\) returned octagonal norm geometry and other polygon invariants, but no result implying this exact probability. Other exact values for distinct pentagonal, hexagonal and cross-polytopal geometries do not imply the octagonal optimization. This is a best-knowledge noncoverage comparison, not a proof of global priority. Unindexed probability-geometric formulations and private/unpublished calculations remain possible.

## Value — PASS
The source introduces an explicitly motivated invariant and asks for further exact examples. The regular octagon is the canonical centrally symmetric polygon after the square and hexagon. Its value is unexpectedly only slightly above \(1/2\), and the strict comparison with separately centred laws exposes the geometric role of *collective* balance. The exact radical, attainment, and finite algebraic proof provide a reproducible, genuinely geometric classification of the optimum value rather than an arbitrary numerical sample. The result is limited to two laws and affine-regular octagons.

## Evidence and restrictions
Primary literature: [1] arXiv:2610.17157v1. Reproducible exact calculation: `verify_octagon.py`, executed successfully. Full derivation and definitions: `RESULT.md`. The verifier does not attempt an independent human audit, which remains outstanding.

Self-review: passed. Independent audit: not yet performed.
