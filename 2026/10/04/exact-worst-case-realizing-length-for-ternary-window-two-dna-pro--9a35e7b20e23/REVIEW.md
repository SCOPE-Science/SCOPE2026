# Same-model review

## Correctness
**PASS.** The claim concerns the exact maximum of the shortest circular-string realization length over all feasible strict rankings for \(q=3\) and \(\ell=2\). Flow conservation gives three reverse-edge pairs with a common nonzero gap. After quotienting only symmetries that preserve the length objective, there are exactly \(420\) shape classes. For a fixed positive gap \(t\), every rank inequality is a lower-bound difference constraint after substituting \(H_i=L_i+t\); longest-path closure gives the componentwise least nonnegative solution and therefore the exact minimum of the positive linear length objective. The verifier checks every shape for \(1\le t\le28\), finds an optimum at most \(86\) for each, and excludes \(t\ge29\) because the gap contribution alone is at least \(87\). The unique worst shape has an independent hand lower bound of \(86\), attained by the displayed balanced matrix, whose Eulerian realization is explicitly checked.

Risk: the finite proof depends on the correctness of a small exact difference-constraint enumeration. The package supplies the complete standard-library verifier and an independent analytic lower bound for the extremal shape; no floating solver or heuristic output is used.

## Originality
**PASS.** The 2019 primary source defines shortest realizing length and gives only an upper-bound framework for its constructed family; for the complete \(q=3,\ell=2\) repository it reports \(30240\) feasible rankings and a computer-derived bound \(c_3\le16\) on representative maximum entries, not the exact value of the worst shortest length. The 2022 follow-up improves constructions and realization lengths but does not state the exact all-ranking value \(86\) in the inspected full text. Targeted semantic searches for the exact value, the shortest-string invariant, the \(30240\)-ranking base case, and the \(c_3\le16\) discussion returned no matching published finding.

Two 2026 papers are highly relevant by title: one enumerates feasible permutations using hyperplane arrangements, and one studies structure and distance properties. Metadata and available descriptions were inspected, but their full texts were not retrievable through the lawful open routes attempted. Neither available description mentions shortest realizing-string length. This is retained as a real residual risk rather than converted into a novelty claim from failed access.

## Value
**PASS.** The shortest realizing-string length is explicitly identified by the foundational paper as an important practical parameter. The ternary window-two case is the smallest nontrivial base repository used by that work, and the exact value \(86\) replaces a coarse representative-size bound by a sharp worst-case molecule length over the entire base space. The result also identifies exactly \(72\) extremal rankings and gives a compact extremal certificate. This is a natural finite invariant of the published model rather than an arbitrary slice or a recomputation of the already known count \(30240\).

Same-model review: passed. Independent audit: not yet performed.
