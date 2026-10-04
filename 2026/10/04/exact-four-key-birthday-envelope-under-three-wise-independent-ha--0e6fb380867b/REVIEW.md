# Review

## Correctness

PASS. Symmetrization preserves the objective and all three-coordinate marginals. The five occupancy types have exact equal-pair/equal-triple counts, so three-wise independence becomes two linear moment constraints. Eliminating variables reduces the all-distinct mass to a one-dimensional interval, and explicit nonnegative occupancy laws attain both endpoints. A direct pattern calculation proves that uniformization within each occupancy orbit gives every concrete triple probability \(1/q^3\).

Decoded replay: `VERIFY_OK symbolic_checks=4997 exact_assignment_checks=14 triple_tables_checked=23912 mixture_checks=485`.

## Originality

PASS, with a stated access risk. The full arXiv text of Pătraşcu--Thorup was inspected at its three-independence, collision, fourth-moment, and appendix passages. It does not state this exact four-key all-distinct interval. The Cornell record for Schmidt--Siegel--Srinivasan was inspected for limited-independence scope. published-finding corpus searches for the claim, aliases, birthday/collision formulations, and orthogonal-array formulations returned the pairwise occupancy theorem as the closest statement; its indexed exact range is different because it fixes only the pair-collision moment. Its repository full text could not be fetched, which is retained as a residual risk.

## Value

PASS. Four keys are exactly the first birthday experiment not determined by three-wise independence. The result gives the complete attainable no-collision interval, sharp endpoint constructions, and interpolation for every \(q\ge4\), directly quantifying the robustness of the birthday phenomenon under a standard limited-independence assumption.

Same-model review: passed. Independent audit: not yet performed.
