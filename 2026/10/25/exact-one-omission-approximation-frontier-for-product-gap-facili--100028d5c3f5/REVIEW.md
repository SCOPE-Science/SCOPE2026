# Scientific review: one-omission product-gap frontier

## Correctness
PASS. Positive-gap sampling weights and omitted-agent costs yield an exact expectation identity. Pigeonhole plus the line metric gives the unrestricted optimum as the minimum adjacent gap. An adjacent pair containing the minimum gap supplies a strict universal upper bound, while the endpoint-short-gap construction converges to the claimed supremum. Every sampled omission has positive weight, proving the precise characterization of welfare-optimal gap patterns. `VERIFY.py` independently enumerates subsets with exact rational arithmetic. Boundary cases with repeated locations have zero optimum and are excluded from the ratio.

## Originality
PASS, subject to a specific priority risk. The mechanism is known from Jia (arXiv:2608.19633) under Product-Gap and Chan–Lin–Wang (arXiv:2608.22484) under Gap-Product; no novelty is claimed for it. Both give unrestricted \(2k\) bounds. The inspected Section 5 main theorem and proof of Chan–Lin–Wang do not state the sharp finite-population \(k-\tfrac12\) frontier, the exact one-omission expected-cost identity, or the welfare-optimality pattern classification; its displayed intermediate inequality yields only \(k\) in this regime. A full-text inspection of Jia's earlier preprint was not possible, though its accessible abstract and technical summaries report only the unrestricted \(2k\) bound. Accordingly the remaining risk is unindexed or uninspected equivalent specialization, not a proven priority date.

## Value
PASS. The minimal-overcapacity case \(n=k+1\) is the first population where any facility can be omitted. Its exact bound quantifies the finite-population gap from the known unrestricted asymptotic ratio, for every facility count, and the independent-set condition on long gaps explains when randomization has no welfare cost despite nonuniform locations. For the strategyproof three-facility case it sharpens the general bound of six to a sharp \(5/2\) at four agents. The scope is finite-population welfare only and does not assert strategyproofness for four or more facilities.

Self-review: passed. Independent audit: not yet performed.
