# Review

## Correctness
**PASS.** The proof uses the published local exchange relations in both orientations for one quadrangle of the pentagon. After the published boundary-one symmetry identifies opposite orientations of every length-\(2\) diagonal, the two equations give \(q_{i+1}q_i=1+q_{i+3}=q_iq_{i+1}\), so adjacent quiddity entries commute. The recurrence \(q_{i+4}=q_{i+1}q_{i+2}-1\), together with adjacent commutativity and cancellation by the unit \(q_{i+1}\), gives commutativity at cyclic distance \(2\). These two distances exhaust pairs among five indices. Height \(1\) reduces to the published equation \(ab=2\), forcing commutativity because \(2\) is central. No experimental inference is involved.

Risk: an indexing error would be decisive, so both oriented exchange equations were checked against the displayed published formula and the pentagon indexing. The proof requires frieze values to be units, exactly as in the definition.

## Originality
**PASS.** The closest inspected source, arXiv:2609.32257v1, states only the two-orientation equality for length-\(2\) diagonals (Proposition 3.6), explicitly handles height \(1\), and gives a genuinely noncommutative height-\(3\) quaternionic example. It does not state pairwise commutativity of all five height-\(2\) quiddity entries or the sharp minimal-height theorem; exact full-text search found no “height 2” occurrence. The foundational arXiv:2403.09156v2 gives the general local calculus and height-\(3\) example, but targeted full-text search found no “height 2” or “pentagon” statement. The 2025 determinant/Laurent/gluing paper supplies broader theory but no covering pentagon-rigidity statement in the inspected material. Semantic searches for equivalent formulations and pentagon/type-\(A_2\) aliases did not return a covering finding.

Risk: an older marked-surface source could contain the same consequence under different terminology; this remains a residual literature risk rather than a known implication.

## Value
**PASS.** The result identifies the exact first height at which the non-commutative frieze formalism can exhibit genuinely noncommuting values with boundary \(1\). It explains why the source's first genuinely noncommutative example occurs on a hexagon rather than a quadrangle or pentagon and gives a reusable rigidity lemma for any attempt to enumerate quaternionic or other division-ring friezes by height. The statement is structural and uniform over all division rings, not a small-instance computation.

## Closest literature and limitations
The closest literature is the 2026 normed-division-ring paper and the 2024/2025 general frieze theory by Cuntz--Holm--Jørgensen. The claim is restricted to boundary value \(1\); arbitrary coefficients are not addressed. It proves rigidity but not a classification of all commuting pentagon solutions.

Same-model review: passed. Independent audit: not yet performed.
