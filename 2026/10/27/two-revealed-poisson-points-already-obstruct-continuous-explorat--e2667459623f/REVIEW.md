# Independent mathematical audit

## correctness

PASS

The nontrivial occupancy cylinders are {000,100}, {010,011}, and {101,111}; the other two rows select all cells. Agreement on a selected prefix preserves the occupancy bit and endpoint there, so the table gives a graph-measurable stopping set on all locally finite counting measures. Measurability follows by measurable cell counts and first-point thresholds. For the diffuse PPP each occupied prefix contributes exactly one point almost surely and the row counts are 0,1,1,1,0,2,2,2. On the empty configuration (an atom of probability exp(-3)) the final target has measure 2, hence monotone intensity-continuity gives a finite deterministic t before attainment with U=A_t(0) of measure in (0,1). This also holds if attainment at infinity is allowed as the increasing union. U meets C2 or C3 in positive measure. On a positive-probability no-hit-in-U event the occupancy is 101 if C2 was met or 010 if C3 was met: prescribe the points in the necessary cell complements, each of positive measure. The stopping-set property fixes the observed history through t, so attainment is still ahead and the omitted part of U cannot be removed. Even for a completed observed-history filtration, the event of agreeing histories through t is an observation atom containing the empty configuration, which cannot be changed by a null exception. The same contradiction can avoid the stopping-time property altogether: choose measure(U)<1/4 and require all prescribed points in the final quarters of their cells outside U, making target mass >1, so attainment before t is impossible by mass monotonicity. This is a continuum proof; check_result.py was inspected but not executed, and its finite cases cannot establish nonattainment.

## originality

PASS

Pass for the at-most-two diffuse threshold example and nonattainment under modulo-intensity stopping, not for the underlying three-cell decision logic or the general existence of nonattainable stopping sets. The closest whole-cell example has precisely the same Boolean rule after complementing two input bits, important structural overlap. The complement and first-point truncation together are needed to retain the obstruction under the stringent actual revealed-point budget. Neither the inspected whole-cell theorem nor the one-point attainability theorem contains the resulting bounded-point counterexample.

## value

PASS

A sharp threshold at two revealed points answers the immediate next case of the one-point theorem. Achieving it with a graph-measurable set on a compact diffuse model, and defeating even intensity-equivalent explored regions, are substantive constraints; the earlier examples with unbounded revealed counts could not answer this threshold question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
