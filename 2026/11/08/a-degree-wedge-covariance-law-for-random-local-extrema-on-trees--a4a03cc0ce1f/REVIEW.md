# Review: degree–wedge covariance of random local extrema

## Correctness

**PASS.** All quantifiers and conventions are fixed: a deterministic simple tree of order at least two, iid continuous labels, every vertex (including leaves) eligible for a strict maximum or minimum. The covariance expansion is supported by a three-case neighborhood-overlap partition: self pairs, adjacent vertices, distance-two vertices, and disjoint neighborhoods beyond distance two. The adjacent beta integral gives the positive kernel \(F(a,b)\). Conditional independence after exposing the unique intervening label gives the exact negative ratio \(-F(a,b)/(a+b+1)\), with no dependence on the central degree. The path and star formulas follow by exact finite motif counts. The extracted standalone `verify.py` passed 3086 rational checks; the infinite statement rests on the proof, not on finite enumeration.

## Originality

**PASS, qualified.** Searches of graph extrema, random rankings, peak/valley cross covariance, equivalent acyclic orientations and fixed-tree neighborhood overlap revealed no explicit all-tree cross-covariance with the positive edge/negative distance-two kernel. Baldi–Rinott–Stein's accessible conference text analyzes marginal local-extrema counts and normal approximations, not the asserted cross-kernel; Kitaev's full preprint covers marginal one-line peak/valley enumerators, while Clark's tree topology is sampled at random, rather than held fixed. A previously recorded independent-edge source/sink covariance law does not imply the result: its orientation model has independent edge directions, whereas a random vertex order has shared vertex comparisons and a genuine distance-two interaction. A longer related 1989 chapter was not accessible for complete comparison, and the path specialization has plausible older implicit coverage; these remain explicit risks, not evidence of uniqueness.

## Value

**PASS.** Joint extrema-count uncertainty for random functions on trees is a motivated probability question. The exact local kernel gives a complete structural rule computable from degree-decorated edges and wedges, with a precise change of sign by graph distance that does not occur for independent edge orientations. It also explains why a five-vertex path already has positive maximum–minimum covariance while stars remain negative at all orders. The result is not merely a table entry or numerical observation.

## Limitations and priority risks

The theorem does not classify signs for every tree or claim a path/star extremal envelope. The older general local-extrema literature may contain a disguised joint-moment derivation; a relevant long book chapter was not available in full. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
