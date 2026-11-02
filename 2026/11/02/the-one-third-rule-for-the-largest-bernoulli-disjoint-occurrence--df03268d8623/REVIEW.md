# Review of the one-third BK-gap optimizer

## Correctness — PASS

The proof identifies the disjoint-witness event exactly as \(S_n\ge2k\), then establishes an exact first-difference equation for the gap. Two terms of the binomial mass dominate before one third. After one third, the factorial ratio of the two disjoint-witness masses decreases by at least a factor six at successive admissible thresholds; the sole delicate residue class \(n\equiv0\pmod3\) is settled by a strictly monotone three-coin coupling and explicit initial values. This supplies a complete all-integer proof, not extrapolation from enumeration. Binomial large deviations give the rate corollary. A standalone exact-integer checker corroborates 1,311,695 test assertions including every dimension through 1100.

## Originality — PASS (qualified)

Tesio, arXiv:2610.32658v1, proves quantitative BK-gap lower bounds and discusses selected threshold events, but the inspected full text does not state an exact all-integer optimizer. Cerf–Tesio, arXiv:2607.02272v2, treats equality, not gap maximization. General binomial-tail and prior limiting-window analyses do not imply strict finite-dimensional unimodality of this specific difference without an additional argument. Mathematical-record searches for fair-cube BK gaps, aliases and the \(n/3\) optimizer did not identify an equivalent theorem. Such searches cannot prove priority, and a stronger unpublished or differently phrased binomial inequality remains a possibility.

## Value — PASS

The restricted optimization is natural: for a fixed cube dimension and a canonical one-parameter family of increasing events, it identifies exactly which threshold makes disjoint occurrence most deficient relative to the BK product bound. The optimizer is unique in every dimension, including all congruence classes, and the resulting maximum has a sharp entropy decay of its distance from one. This resolves a complete finite extremal question that asymptotic threshold-window descriptions alone do not answer. It is not claimed to be a general improvement of the BK inequality for arbitrary increasing events.

## Scientific limitations

All assertions concern identical Hamming thresholds under fair independent bits. The supplementary computer verification is finite and not an independent proof. Historical-priority comparison cannot exclude all stronger results. Independent mathematical verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
