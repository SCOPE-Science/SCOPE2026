# Self-review

## Correctness

PASS. The exact clearing equations yield a contractive deficit recurrence. Back-substitution proves the threshold formula for every bank; the cyclic closure is treated separately at the full-cascade boundary. The rational verification script checks an exact four-bank example. The proof applies to every finite ring satisfying the stated assumptions, not only the example.

## Originality

PASS. The inspected 2001 clearing paper provides the general fixed-point model and default-wave algorithm but does not state the closed-form threshold sequence. The inspected 2022 ring-network study analyzes a different loss-flow model and reports only selected ring thresholds. The result is limited to a single localized shock in the proportional-payment model. Related general clearing results and a 2019 flow-network paper remain possible overlap risks; absolute novelty is not claimed.

## Value

PASS. The formula gives a complete threshold profile for the number of consecutive defaults, useful for reverse stress testing a directed ring. The exact increments show how each downstream bank’s baseline slack is amplified by the inverse product of the preceding liability shares. This is a natural structural invariant, not a numerical census or a claim about empirical bank data.

## Closest literature and limitations

Eisenberg and Noe (2001), DOI 10.1287/mnsc.47.2.236.9835, supplies the proportional-clearing framework. Eboli et al. (2022), DOI 10.1007/s10436-022-00416-9, studies related ring contagion thresholds under a different loss-flow model. Multiple simultaneous shocks, bilateral rings, bankruptcy costs, fire sales, and liquidity feedback are outside the claim. Thresholds above the shocked bank’s available resources are unreachable. Independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
