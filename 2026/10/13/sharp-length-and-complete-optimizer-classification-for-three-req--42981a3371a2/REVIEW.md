# Scientific review: sharp length and optimizer classification

## Correctness — PASS

The paper-model minimal-recovery and exchange theorems are applied with their exact hypotheses. Over binary rank three, a minimal recovery subset must be independent, has at most three positions, and has XOR equal to a unit column; the verifier enumerates all such subsets exactly. Monotone peeling of all disjoint triples computes the greatest exchange-closed subfamily: every deletion is forced for all possible subfamilies, and a nonempty fixed point is itself exchange-closed. Complete enumeration of all 1716 seven-column and 3003 eight-column nonzero multisets yields respectively 0 and 79 admissible cores; zero-column removal and lengthening show the global length-8 minimum. All 79 literal strong recovery selections are checked for every disjoint partial history and all three next requests, with 17 orbit checks. The actual embedded verifier ran and returned VERIFY_OK. The only reliance on external theory is the proved, stated exchange characterization; no samples are mistaken for infinite proofs.

## Originality — PASS

The 2026 primary paper already exhibits an eight-coordinate strongly-online generator (Example IV.22) but does not classify all minimum generator matrices or establish the seven-coordinate impossibility. The 2018/2022 original source formulates shortest lengths for small k among open directions and supplies broad constructions rather than this finite classification. Nearby public four-request binary batch results have different service models and do not imply the asynchronous three-request lower bound or 79-solution count. Searches of published research records and external literature did not find a dominating statement. Unindexed results may remain; absence of a search hit is not treated as novelty proof.

The closest sources are Düzgün et al., arXiv:2605.09748 (2026), and Riet et al., arXiv:1806.00592 (2018/2022). The former's eight-coordinate construction is prior art and is not claimed as new. The additional facts are the matching lower bound, all \(79\) labeled eight-column solutions, the \(17\) relabeling classes and their universal strongly-online selections. No current search establishes absolute global novelty. The public four-request dimension-three batch result is a different service condition; its full repository text was not retrieved.

## Value — PASS

This is a natural first nontrivial exact capacity and full optimizer classification for the explicitly studied 2026 asynchronous/strongly-online hierarchy at three requests: it distinguishes ordinary batch feasibility from asynchronous service, identifies sharp storage, exhibits 17 inequivalent named-message designs rather than only the previously known example, and proves every optimizer can use the stronger rule. It is not a renaming or routine corollary of the known eight-column construction. The finite parameter is mathematically motivated by the first case beyond the t<=2 general equivalence.

## Scope and scientific risks

The result applies only to full-rank binary encoders of three **named** message coordinates, three concurrent requests, and generator-column equivalence as defined. The proof uses a completely enumerated finite case, not an infinite parameter extrapolation. Unindexed historical material remains a possible originality risk. An independent mathematical audit would still be needed for publication-level confirmation.

Self-review: passed. Independent audit: not yet performed.
