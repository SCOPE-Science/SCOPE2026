# Review

## Correctness

PASS. The binary noise set consists of the two alternating words. Their output sets coincide exactly for complementary inputs, so the confusability graph is a perfect matching on the complement pairs. This gives the exact optimum, all extremizers, and their count. For \(q\ge3\), the recursive construction avoids at most two symbols at each step and represents every target difference as the difference of two admissible noise words; hence any two inputs share an output.

## Originality

PASS, with a deliberately narrow scope. The closest inspected literature gives a general finite-state zero-error criterion and capacity formula, and treats a different run-length constraint. It does not state the exact finite-block binary maximum-codebook classification or its count for the proper-colouring noise constraint. The general criterion does cover the no-pair branch for \(q\ge3\); that branch is not presented as a new general capacity theorem. The literature searches are not exhaustive.

## Value

PASS. Exact finite-block optima and a complete census of all optimal codebooks are natural coding invariants: an asymptotic rate alone does not identify the finite-block penalty or the full set of optimal designs. The classification is self-contained and applies at every blocklength.

Closest literature: arXiv:2006.00892v1 and arXiv:2108.03874v1. Limitations: deterministic worst-case noise only; no stochastic channel claims; no independent audit or independent validation.

Self-review: passed. Independent audit: not yet performed.
