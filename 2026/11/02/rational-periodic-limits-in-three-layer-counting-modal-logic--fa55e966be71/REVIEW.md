# Mathematical review

## Correctness — PASS

A direct reconstruction confirms five necessary steps: (1) independent binomial counts of fair, independent proposition labels; (2) the unique-maximum probability equals a finite binomial sum and differs from \(1/m\) by an explicit positive multiple of \(1/\sqrt n\); (3) the modal equality admits a solution only in the stated residue class and has binomial point mass \((\alpha_m+o(1))/\sqrt n\) there; (4) independent depth-two child subtrees amplify that signal to probability approaching one with stretched-exponential error; (5) independent root plurality gates realize each rational subsequential limit. Binomial local central limits have positive variance because \(m\ge2\) is fixed. Finite direct checks returned `ALL_CHECKS_OK` on the packaged source. Risks: extrapolation to nonuniform branching or correlated labels is unproved, and finite tests are not asymptotic proofs.

## Originality — PASS within examined sources

The closest motivating paper is Ghosh–Schwarzentruber, arXiv:2610.26187v1, Sections 3 and 6 (full HTML material read). Its parity nonconvergence example has two distinct limit values; it additionally studies a modified limiting probability and density of constant limits. It does not state or imply an arbitrary-modulus, rational-residue-profile theorem with an explicit stretched-exponential detector exponent from the inspected sections. Broader counting-logic expressivity in Benedikt–Lu–Motik–Tan (ICALP 2024) does not by itself imply probabilities under a uniformly random labelled full-branching tree model. Searches covering counting modalities, regular-tree limits, congruences, plurality/tie mechanisms, and periodic probability profiles found no equivalent published finding. Risks: uninspected specialized predecessors may imply this construction; the 2024 article was only checked at abstract/metadata level in this review, not certified as non-covering on its full text.

## Value — PASS

The 2026 paper explicitly raises convergence questions after presenting an oscillating parity example. The construction gives all finite moduli and all rational-valued profiles, while staying within linear counting rather than adding a modulo quantifier. The three-depth amplification method is a reusable mechanism relating almost-sure modal classification, rare local events and expressive behavior in counting-message-passing systems. The exact detector rate and finite probability formulas distinguish the result from simply restating a parity example. It does not prove a general limit classification or minimum required depth.

Self-review: passed. Independent audit: not yet performed.
