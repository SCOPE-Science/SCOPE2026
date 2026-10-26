# Scientific review

## Correctness: PASS

The sample-and-hold integration gives the stated two-by-two map exactly. Its trace and determinant reduce the fixed-period Jury conditions to \(0<h<\min(2/k_d,2k_d/k_p)\). For two intervals, direct multiplication gives \(1-\operatorname{tr}P+\det P=k_p(a+b)(a+b-k_dab)\) and \(2(1+\operatorname{tr}P+\det P)=\Phi\). Within the individual stability range the first expression is positive and \(|\det P|<1\), so the remaining Jury condition is necessary and sufficient. The exact rational witness verifies that the unstable region is nonempty.

## Originality: PASS, with a specific residual risk

The closest literature treats constant or uncertain sampling periods through spectral-radius tests and sufficient Lyapunov/LMI conditions. The inspected 2008 full text states that fixed-period stability can be checked by the spectral radius and formulates uncertain sampling as a condition over an interval; it does not state the displayed exact period-two polynomial for this proportional-derivative double integrator. Searches for the exact model, alternating intervals, Floquet/monodromy criteria, and the polynomial boundary did not recover an implication-equivalent statement. General Floquet and Jury theory make the calculation possible, so this is a specialized exact characterization rather than a claim to a new general method. A non-indexed or inaccessible prior derivation remains a real risk.

## Value: PASS

Nonuniform sampling occurs in networked and embedded feedback, and the distinction between stability at each fixed interval and stability under switching between intervals is operationally important. The result gives a sharp, closed-form test for the natural two-period case and an exact counterexample to inferring jitter stability from two individually stable sampled maps. It is not merely a numerical example: the polynomial condition classifies every positive gain pair and every alternating interval pair inside the fixed-period stability range.

## Closest literature and limits

The broad aperiodic-sampling results do not provide this explicit necessary-and-sufficient two-period boundary in the inspected material. The claim is limited to a double integrator, fixed positive gains, zero-order hold, and an exactly alternating interval sequence. It does not imply stability for arbitrary aperiodic sequences.

Self-review: passed. Independent audit: not yet performed.
