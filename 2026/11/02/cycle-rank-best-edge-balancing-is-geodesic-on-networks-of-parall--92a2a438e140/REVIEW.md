# Scientific review

## Correctness — PASS

The proof fixes a finite connected simple host whose every nontrivial block is a bundle of internally disjoint paths. It enumerates **all** simple cycles by two-path unions, derives exact edge rank as the number of opposite-parity paths, and proves that every allowed update reduces the block minority count by one, including ties. It proves the lower bound on *all* edge-reversal sequences by observing that a reversal can change only one path parity in one block; therefore cycle-best-edge achieves the global shortest distance exactly. The negative-cycle-count decrement and the uniform-cycle/uniform-edge tie law follow from the same ranks without approximations. Code exhaustively checks 9,168 states and 77,792 legal transitions on small hosts, and rationally checks tie cases. Finite checking corroborates but is not used to infer the infinite-size theorem.

## Originality — PASS, with residual risks

The directly motivating 2022 study proves convergence for **complete networks** under a **triangle** rank and explicitly leaves sparse-host extensions for further investigation. Its proof does not imply that every cycle-rank move on a noncomplete multi-path block network is a shortest route to balance. The 2016 simple-cycle balance paper counts cycles rather than prescribing a greedy transition. The 2022 frustration-critical study gives structural switching and minimum-frustration background, not the all-trajectory result or probability law. The 1978 balancing-process paper is especially relevant to the shortest-distance component, but only its abstract was accessible; the original dynamic and exact tie distribution remain separate mathematical assertions. Searches of the accessible scientific literature and mathematical-record index did not identify an equivalent or stronger published statement, which is evidence of noncoverage but not proof of absolute priority.

## Mathematical value — PASS

The general sparse-network problem permits problematic trajectories under natural edge-flipping rules. This theorem identifies an unbounded-cycle-rank, noncactus family with extensive overlapping cycles on which the **exact** finite number of interventions is globally optimal for *every* choice history; its monotone cycle energy gives a concrete absence-of-blinkers certificate. The exact tie law additionally isolates a length-induced social-polarity bias even when half of the terminal pathways initially favor each sign. These address the structural and dynamical issues motivating sparse-host extensions, rather than recomputing an arbitrary small case or merely restating the known frustration index.

## Limits and closest literature

The definition uses all negative simple cycles; it is not the triangle-only process of the motivating paper. Length-weighted cycle ranks and general noncomplete hosts are not covered. Full-text priority assessment of Katai and Iwai (1978) could not be completed. No independent external validation was performed.

Self-review: passed. Independent audit: not yet performed.
