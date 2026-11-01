# Scientific assessment

## Correctness — PASS

The complete proof is an exact vertex-and-cone argument. Retained cube corners require disjoint strict orthants, and each cut edge adjacent to the all-negative corner whose singleton weight exceeds the threshold requires an additional mutually disjoint illumination cone. An explicit direction family matches that lower bound for every cut-edge intersection, including tied subset sums. Fractional weights obey the same disjoint-cone lower bound. The full proof does not infer universal claims from finite enumeration. The standalone exact rational checker passed 354 parameter systems and 15,035 tests; independent vertex enumeration was used for selected small-dimensional instances.

## Originality — PASS, subject to historical-priority uncertainty

The nearest published results are the one-corner example of Livshyts and Tikhomirov; the later independent shallow corner-truncation construction; Ivanov's general theorem for primitive polytopes; and Gorodzha's universal fractional illumination bound. Their full statements or relevant proof material were compared for implication, rather than only for terminology. The earlier one-corner calculation is a special case, and no novelty is claimed for it. Neither independent shallow corner cuts nor a general upper bound gives the weighted all-threshold formula or the exact singleton-cancellation rule. The possibility of an older equivalent result about clipped boxes remains unresolved; publication priority is not independently established.

## Value — PASS

The result classifies both illumination invariants for an all-dimensional continuum of anisotropic clipped cubes, replacing a geometric covering problem with an exact weighted Boolean subset count. It finds the necessary additional cut-edge correction overlooked by naive retained-vertex counting, describes every tied/non-tied threshold jump, and establishes integrality of the fractional relaxation throughout the family. For instance, weights \((3,1,1)\) at threshold \(5/2\) require five directions despite having only four original cube vertices. This is a motivated complete classification, rather than merely a small numerical computation.

## Limits and closest references

The result assumes one halfspace and strictly positive weights. No conclusion is drawn for multiple cuts or general polytopes. An equivalent older treatment under a different name could have escaped indexing. Relevant works: Ivanov, arXiv:2607.08944; Gorodzha, arXiv:2609.23913; Livshyts–Tikhomirov, arXiv:1710.05070; Naszódi (2009); and *Independent corner truncations realize the high illumination spectrum near the cube* (2026).

Self-review: passed. Independent audit: not yet performed.
