# Same-model review

## Correctness
**PASS.** The final claim is a necessary-condition theorem, not a claimed proof of Liu's conjecture. For the lower endpoint, the boundary defect on an isosceles triangle is derived directly from the definitions; the tangent-half-angle substitution gives the stated rational function \(L(t)\), whose derivative has exactly one positive critical point in the relevant interval. The sign of the affine defect then gives strict boundary failure for every \(\lambda<\lambda_*\), and continuity supplies genuine interior failures. For the upper endpoint, the collapsing right-triangle family has \(\varepsilon F_\lambda\to(2-\lambda)(1-q)\), so \(\lambda>2\) gives strict failures, again stable under an interior perturbation. The packaged checker replays all numerical diagnostics from the saved source.

## Originality
**PASS.** The 2014 source was read at the conjecture statement. Candidate-specific semantic searches and exact-constant searches found no published-finding match. The highly plausible 2017 and 2018 full texts were inspected at their actual displayed propositions: they prove different squared-distance parameterized inequalities and do not imply this first-power boundary window. The available prior-finding corpus was compared by source identifier, title aliases, the endpoint \(3/5\), and the displayed first-power pattern; the nearest related item concerns a different 2016 Liu Erdős–Mordell parameter conjecture with a different defect ratio. Residual risk remains that an older or differently indexed note contains the same boundary analysis.

## Value
**PASS.** The parameter range is part of the mathematical content of Liu's explicit open conjecture. Determining unavoidable endpoints is therefore a motivated structural question, not an arbitrary numerical slice. The optimized lower obstruction is exact for a natural symmetry-and-boundary family, and the upper analysis proves the conjectured endpoint \(2\) cannot be enlarged at all. The result materially narrows what any eventual extension or sharp formulation can say while carefully avoiding a claim of solving the conjecture.

Closest literature and limitations are described in `RESULT.md` and `AUDIT.json`.

Same-model review: passed. Independent audit: not yet performed.
