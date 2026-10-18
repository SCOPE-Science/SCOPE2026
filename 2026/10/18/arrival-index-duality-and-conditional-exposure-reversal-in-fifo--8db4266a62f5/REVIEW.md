# Scientific review: arrival-index duality and conditional exposure reversal

## Correctness — PASS

For any FIFO sample path, the \(k\)-th last predecessor of customer \(i\) overlaps its arrival for longer than \(\ell\) precisely when the \(k\)-th next arrival overlaps customer \(i-k\) for longer than \(\ell\); in both directions the necessary and sufficient inequality is \(D_{i-k}>A_i+\ell\). Stationary arrival indexing therefore equates both exceedance distributions and all independent-mark exposure probabilities. Conditional on the tagged sojourn, earlier exposures use only past arrivals/services/marks, whereas later exposures use future renewal increments and their independent marks, giving conditional independence. In a unit-service \(M/D/1\) queue, the predecessor count is a staircase function of the workload while the later marked Poisson arrivals have a continuous exponential survival probability. The displayed threshold inequalities follow from \(b_\ell(t)\ge t-2\) and \(-\log(1-p)>\lambda p\); the workload stationary transform gives the exact common marginal. The theorem distinguishes the sojourn-time atom and exceptional integer points. The independent finite checker passed 1,180,980 exact rank assertions, 40 conditional-risk checks and a separate simulation sanity check; the analytic proof, not these finite checks, supplies the universal quantifiers.

## Originality — PASS, qualified

Newman and Pender (2026), arXiv:2610.09019v1, explicitly formulate Conjecture 3.10 for earlier/later customer exposure in \(G/G/1\) and investigate \(M/M/1\) and approximated \(M/G/1\) laws. Their visible paper does not give the stated exact deterministic-service conditional reversal or common directional probability. Boxma and Pender (2025), DOI 10.1007/s11134-025-09938-1, already establish the pairwise \(G/G/1\) overlap formula, and stationary nonovertaking gives unmarked overlap symmetry as an elementary consequence. The newness assessment rests on the explicit marked-risk conjecture resolution and strict conditional reversal; the FIFO rank shift alone is not claimed as independently new. The 2025 priority-queue overlap work concerns a different discipline. General Palm-mass transport, queueing transforms, or earlier work could subsume part of the present formulation and require independent priority inspection.

## Value — PASS

A published explicit conjecture asserts both an unconditional directional infection symmetry and a much stronger conditional identical-distribution assertion. The result establishes a sharp logical distinction: unconditional symmetry remains valid throughout stationary FIFO queues, while conditional direction preference reverses on positive-probability regions in a standard \(M/D/1\) model. Exact marginal and conditional formulas replace a numerical-only comparison and permit model calibration. The claim is neither a new queueing workload transform nor a rebranding of an unmarked symmetry; it answers the infectious-mark question and identifies an observable conditional failure.

## Closest literature and limitations

The closest texts are arXiv:2610.09019v1, DOI 10.1007/s11134-025-09938-1, and *The Number of Overlapping Customers in Priority Queues* (2025). The first motivated the open issue; the second supplies fundamental existing overlap identities; the third treats a related but differently disciplined model. Stationarity and FIFO are necessary for the stated symmetry proof. Conditional independence uses renewal structure and independent marks and a deterministic threshold; conditional risk reversal is shown only for \(M/D/1\). No independent external audit or exhaustive priority verification has occurred.

Self-review: passed. Independent audit: not yet performed.
