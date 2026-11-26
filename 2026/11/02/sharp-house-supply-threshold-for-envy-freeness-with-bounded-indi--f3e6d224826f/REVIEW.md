# Independent mathematical audit

## correctness

PASS

The sharp theorem survives unchanged. The implementation sentence at frozen RESULT.md line 25 did not distinguish testing the neighborhood cardinality of the current agent set from testing whether that set still contains a Hall violator. The cardinality-only deletion test can stop too early: take top sets {h},{h},{x,y},{x,y} on four active houses h,x,y,w. All four agents are deficient and each triple has three neighbors, but the first pair is deficient. The complete replacement at /workspace/repairs/5/RESULT.md uses a polynomial matching test for each restricted agent set with the house side fixed. Unsaturability is retained at each deletion. At termination every proper subset is saturable by restricting a matching of a single-deletion set, so Hall implies that the returned set itself is inclusion-minimal deficient. Its neighborhood has size z−1 for z agents, and z≥2. Each participation when at least n houses are active spends one entire current top tier, and no agent with only one surviving tier can participate because she sees all active houses. For any prefix begun with at least n houses, summing z−1≤(n−1)z/n and counting at most k−1 participations per agent bounds deletions by (n−1)(k−1). Thus the algorithm retains at least n houses after every prefix and terminates in a covering top-choice matching. Identical tiers of size n−1 force envy at the lower supply, or no injection when k=1. The minimization takes at most n² matching tests per round and at most m rounds. Independent bounded bitmask checks found zero failures in 6,561 profiles at (n,k,m)=(2,3,4) and 32,768 at (3,2,5); they found 78 obstructions in 4,096 at (3,2,4) and 6 in 729 at (2,3,3). The corrected shrinking rule returned an inclusion-minimal set on each of 12,802 unsaturable graphs among all 50,625 top-choice graphs with four agents, four houses and nonempty agent neighborhoods. Replay: node /workspace/review-evidence/5.js. These finite checks do not establish the universal bound or the running time. Frozen verification notes and code were inspected, not executed or modified.

## originality

PASS

The repaired claim credits the polynomial top-choice Hall-elimination algorithm and minimal-set existence to prior work; the supported distinct result is the sharp uniform bounded-tier supply guarantee. The inclusion-minimal matching-test correction repairs correctness, not originality. The decisive additive tier budget and tight worst-case supply are not stated or supplied by specializing the inspected unrestricted algorithm's existence/complexity result. The readily derived dichotomous case is not separately credited as new. A bounded follow-up search for the two specific supply bounds produced no new plausible primary candidate, not evidence of historical absence.

## value

PASS

The result asks for the smallest stock of houses that guarantees a feasible no-envy assignment under an interpretable restriction on individual preference coarseness. An existence algorithm does not tell a planner what stock necessarily suffices. The tier-edge accounting gives a tight answer under heterogeneous weak orders and the identical-order obstruction shows precisely why one fewer house can fail, without transfers. This value is retained by the implementation repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
