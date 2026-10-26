# Self-review

## Correctness — PASS
The projection-to-cycle lemma establishes the sharp lower bound and an explicit construction attains it. Every optimal placement lifts a minimum cycle dominating set, and the only possible cyclic deficit profiles are completely treated. The adjacent/disjoint short-gap cases and the non-generic size-four instance are distinguished. The independent graph-based enumeration (`VERIFY.py`) confirms the formula through order parameter 15 and the local lift criterion through 13. These computations are checks; the infinite quantifiers are discharged by the gap proof.

## Originality — PASS, with residual risk
Saibavani–Parvathi 2019 gives the minimum power domination number, but not all optimizers. Brimkov et al. 2018 explicitly exclude the attached-single-leaf case from their corona polynomial formula and ask about its enumeration. Bläsius–Göttlicher–Schirneck 2026 provides a general algorithmic framework; its abstract does not state the closed formula. The recent paper's full text was not available, and independent priority assessment has not occurred. Targeted research-record and literature searches yielded no equivalent minimum-set sunlet census.

## Value — PASS
The coefficient at the smallest power in a graph's power-domination polynomial counts all optimal sensor configurations. Here that count is exact at every graph size and nontrivially depends on the order modulo three, with an exceptional four-cycle. The complete lift classification explains the phenomenon and advances a natural boundary case singled out in the corona polynomial literature without claiming to solve the full polynomial.

## Scope and limits
One private leaf per cycle vertex; all minimum-size power dominating sets, not all inclusion-minimal sets or all sizes. Independent validation and historical priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
