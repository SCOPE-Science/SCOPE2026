# Self-review

## Correctness
PASS. The proof derives the complete area formula directly from 14 facet areas using Cauchy’s identity, optimizes it globally over two exhaustive spherical chambers, and proves exact equality directions and unique thresholds. The lower-bound proof uses extreme rays and the triangle inequality; the upper-bound proof uses Cauchy–Schwarz and checks its feasible equality rays. The `verify.py` direct convex-hull method checked 5,460 cases including both crossing parameters, and is supplemental to the all-real proof.

## Originality
PASS relative to inspected, accessible evidence. Earlier exact regular truncated octahedron and cuboctahedron brightness results cover the fixed parameters \(c=3/2\) and \(c=2\), which are openly excluded as new special cases. Fully inspected earlier mathematical results for the same family determine the facet-network spectrum, maximal contained tetrahedral volume, and ordinary illumination number. The known facet areas and Cauchy identity are inputs; none of these theorems classifies two separate continuum brightness-orientation crossovers at \(c=(7+\sqrt7)/6\) and \(c=(4-\sqrt2+\sqrt{10-6\sqrt2})/2\). General shadow optimization literature was checked via its accessible bibliographic description but not full text, leaving historical-priority uncertainty.

## Mathematical value
PASS. Maximum and minimum brightness and their complete equality sets are natural extremal invariants of this familiar family, and both exact transition parameters lie strictly inside a single fixed combinatorial interval. The value rests on this double orientation phase diagram and not on computing already tabulated face areas or reproducing the known fixed-body cases.

## Limitations and comparison risks
This is a theorem for three-dimensional orthographic projected area only, not an all-dimensional or all-convex-body bound. Historical priority is provisional; Burger–Gritzmann’s primary full text was unavailable by the online attempts. The earlier single-polytope shadow results and Cauchy’s formula are explicitly acknowledged. Finite numerical confirmations do not establish an infinite theorem.

Self-review: passed. Independent audit: not yet performed.
