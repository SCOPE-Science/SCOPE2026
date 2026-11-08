# Self-review

**Final claim.** The open Lovász neighborhood complex of \(K_5\mathbin\square C_4\) is integrally homotopy equivalent to \(\bigvee^{53}S^2\vee\bigvee^4S^3\). The published longer-cycle result explicitly omits this four-cycle boundary.

## Correctness — PASS
The full finite face set has 950 nonempty simplices, derived independently as submasks of the 20 open neighborhoods and as all vertex sets with common graph neighbor. The exact 446-pair acyclic matching leaves critical-cell counts \((c_0,c_2,c_3)=(1,53,4)\); all 3,260 directed Hasse incidences were checked and the entire graph topologically sorted. The four critical three-cell boundaries vanish over \(\mathbb Z\) by signed gradient recursion **and** direct unit-pivot cancellation on the entire original boundary matrices. Since the two-skeleton is simply connected, Hurewicz turns these zero integral boundary maps into nullhomotopic attaching maps. The result follows by Forman's theorem. The fixed finite enumeration is exhaustive, not an infinite extrapolation.

## Originality — PASS on inspected evidence
Kozlov (arXiv:math/0503613, Sections 4 and 7) proves general graph-complex simple-homotopy relations, not a calculation for this product. Matsushita (arXiv:1210.2803) concerns fundamental-group characterization. The closest exact-product study, *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, explicitly requires \(n\ge5\) and excludes \(n=4\). Its conclusion has a nontrivial circle and therefore cannot be substituted into this simply connected exception. Shukla (arXiv:1802.04526) handles graphs of maximum degree three or four-regular circulants; the present graph is six-regular. Chauhan–Shukla–Vinayak (arXiv:2512.04486) treat a different, total two-cut simplicial complex. The indexed result searches, aliases, and actual accessible own claims revealed no direct or dominating statement. An inaccessible or unindexed equivalent published result remains a limitation; a failed search alone is not a novelty proof.

## Mathematical value — PASS
The four-cycle is the first nontrivial boundary specifically excluded by the natural longer-cycle classification. The excluded-case mechanism (distinct opposite vertices sharing two centers) invalidates that proof, so the actual integral homotopy type is mathematically unresolved by its assumptions. The first clique width where two-sphere and three-sphere summands differ, \(m=5\), gives a concrete natural mixed-dimensional obstruction test. Exact simply connected homotopy and attaching maps are stronger than the Euler characteristic or mod-two Betti numbers, and this datum can serve as a boundary condition for a uniform short-cycle theory. No arbitrary parameter slicing or claim of a general formula is made.

## Remaining limitations
All certified assertions concern only the named 20-vertex graph. The certificate uses Python 3 standard-library exhaustive enumeration and integral chain cancellation. No equivariant or homeomorphism classification is claimed. Publication-priority uncertainty remains, and an independent audit is still necessary.

Self-review: passed. Independent audit: not yet performed.
