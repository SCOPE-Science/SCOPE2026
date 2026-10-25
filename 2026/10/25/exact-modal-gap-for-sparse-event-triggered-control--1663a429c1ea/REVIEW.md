# Review summary

## Correctness

**PASS.** The proof reconstructs the pulse and zero-input state transitions in a common orthonormal eigenbasis. It derives the trigger equation as a convex combination of exponentials, proves no crossing can occur before the minimum individual modal crossing, exhibits a minimizing pure mode attaining equality, and handles the case where no mode can retrigger. The numerical script is only a consistency check; the proof is analytic.

## Originality

**PASS, subject to the stated residual risks.** The closest full-text source is Banno et al., whose Theorem 1 gives a generic lower bound for the same sparse event-triggered architecture but does not state the exact modal minimum or equality cases. The 2021 preliminary conference version could not be read in full, and the 2018 intermittently-actuated-control paper was available only as an abstract. Their possible overlap is recorded as a residual risk rather than treated as disproved.

## Value

**PASS.** The exact minimum zero-input interval is directly relevant to hardware duty-cycle and intermittent-actuation scheduling. It identifies the worst common eigenmode, proves that mixtures cannot force an earlier trigger, classifies the no-trigger case, and sharpens the generic published bound by at least a factor of two in the stated class.

## Closest literature and limitations

Banno et al., “Sparse event-triggered control of linear systems,” DOI 10.1002/rnc.6278, first published 15 July 2022, provides the model and a generic interval bound. Their 2021 conference predecessor is bibliographically verified but its full text was inaccessible. Wang et al. (2018) study intermittently actuated control but only the abstract was accessible. The exact result assumes commuting symmetric generators, a Euclidean quadratic function, exact parameters, and no disturbance or actuator constraints. Semantic search results are not a uniqueness proof.

Self-review: passed. Independent audit: not yet performed.
