# Self-review

## Correctness — PASS

The exact discrepancy dynamics give a complete reduction of unit-chore Prop1 to an integral upper-discrepancy bound. The three-agent eight-state transition table proves an infinite-horizon induction and handles all ties. A separate finite exhaustive greedy recurrence checks all four-agent prefixes of length at most four, including all eligibility sets and all tie responses. The adaptive five-job tree has no surviving branch, and an independent minimax calculation returns first forced failure at five. The all-\(n\) three-job obstruction for at least five agents is algebraic, not extrapolated from computation.

## Originality — PASS, with historical-priority uncertainty

The closest source is Biburger–Megow–Shahkarami, arXiv:2610.08064 (October 6, 2026): it proves order-of-growth deterministic approximation guarantees and develops an adaptive lower-bound method, but the inspected material does not give this exact agent-versus-horizon frontier. Its general lower-bound idea accounts for the simpler large-population part. Sun–Wang–Li, arXiv:2602.18098, treats offline proportionality and does not decide online irrevocable feasibility. Searches of public research records, literature on online fractional rounding and unit restricted assignment, and relevant neighboring exact findings identified no covering theorem. No exhaustive historical priority or external certification is claimed.

## Mathematical value — PASS

The result locates the precise transition from permanent online Prop1 feasibility to forced failure for unit chores under eligibility constraints. The four-agent five-item threshold is a genuine exceptional case, distinct from the easily constructed three-item adversary for five or more agents. It offers a benchmark for future restricted-assignment algorithms and separates a small exact structural frontier from previously known asymptotic approximation bounds.

## Limitations

Claims are confined to identical unit-size chores, deterministic online assignments, publicly revealed eligibility sets, and adaptive adversarial arrivals. The four-agent four-job guarantee rests on a fully specified finite recurrence, whose included program should be inspected and rerun independently. Results for arbitrary job sizes and randomization are not asserted; unindexed historical prior work remains possible. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
