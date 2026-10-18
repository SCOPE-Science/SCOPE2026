# Self-review

## Correctness: PASS

The exact-integer floor inequalities reduce the dynamics on each protected diamond shell to a bijective phase rotation. All four sector parameterizations include the axes without gaps; their \(4r+1\) phase residues are disjoint and exhaustive, and the next phase is always incremented by one. At the reciprocal threshold the starting point crosses to the next shell exactly once, follows its unperturbed phase arc without hidden floor activations, crosses back exactly once, and traverses the original complete shell before its first return. The distinct phase paths prove the **least** period, not merely a return bound. The embedded `verify.py` reproduces small itineraries and tests the formulas for many integer parameters, but the all-integer proof is in `RESULT.md`.

## Originality: PASS, subject to historical-priority risk

Akiyama–Pethő (2012) establish infinitely many periodic orbits for each parameter and do not state the sharp central-shell transition. Reeve-Black–Vivaldi (2012) analyze the near-integrable polygonal limit and periodic-orbit densities, not the exact threshold \(\lambda=1/q\) and the complete \(8q-2\) finite itinerary. Their 2014 linked-strip work concerns large-scale asymptotics. Akiyama–Mance (2025) prove bounded-start periodicity and discuss parameter partitions, but neither their theorems nor the examined results provide the uniform \(q\)-formula or its two-shell composition. These are scientific *implication comparisons*, not merely title matching. Searches of the mathematical-results corpus and relevant literature found no equivalent or stronger assertion for the same exact map and parameter range. Priority may still be affected by earlier unindexed round-off literature or explicit computations not located.

## Mathematical value: PASS

The first nontrivial integer-scale activation is a natural threshold in the well-studied rounded Hamiltonian rotation, whose global periodicity remains difficult. The result describes all surviving central periods, counts their lattice states, and proves an **exact universal period jump** accompanied by a precise cross-shell merger. This is more informative than examples of periodic points or a consequence of the known qualitative existence theorems. The integer-indexed thresholds are forced by the floor discontinuities rather than selected as arbitrary slices.

## Scope and residual risk

The exact theorem concerns the specified floor map, \(q\ge2\), the protected shells, and the sharp first threshold. It does not characterize exterior cycles or later parameter changes. Earlier historical derivations not indexed in accessible records cannot be ruled out. The checks are a self-review, not independent expert validation.

Self-review: passed. Independent audit: not yet performed.
