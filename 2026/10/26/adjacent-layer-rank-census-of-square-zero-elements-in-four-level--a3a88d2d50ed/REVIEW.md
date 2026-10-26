# Self-review: square-zero adjacent-layer rank census

## Correctness — PASS
The three block equations from the square-zero condition are exhaustive. Fixing the rank of the middle block reduces the adjacent blocks to maps through its quotient and into its kernel, with standard rank-count factors. The final coupling map \((E,D)\mapsto AE+DC\) has image dimension \(as+rd-rs\), independently verified by describing two matrix subspaces and their intersection. This gives the exact number of free middle blocks and the unconstrained upper-right block. The argument covers all prime powers, zero ranks, and all positive layer sizes. An independent direct matrix-enumeration checker matched every profile coefficient in eleven configurations, plus 196 rank-count identities.

## Originality — PASS within inspected coverage
Closest published antecedent: Bardestani--Mallahi-Karai--Ram--Salmasian, arXiv:2503.15440, Theorem 2.5, already counts square-zero matrices by ambient rank for general parabolic nilradicals; Karp--Thomas, arXiv:2207.12590, Theorem 5.13, already counts Jordan types and fixed-flag Jordan-form tableaux. Neither inspected result enumerates the **simultaneous ranks of the three immediately adjacent blocks**. A concrete two-element witness in level sizes \((1,2,1,1)\) proves that identical cumulative-prefix Jordan types can have different adjacent-rank profiles. published-finding corpus and accessible historical claim searches showed no matching exact joint-profile claim. This remains a best-knowledge originality assessment, not proof of priority; an unexamined specialist block-rank formula is the principal risk.

## Value — PASS
The invariant stratifies the natural square-zero variety of a finite incidence algebra by three canonical boundary maps rather than collapsing it to the ambient Jordan type. The explicit three-variable distribution makes these strata quantitative, uniformly for all field sizes, and detects information that conventional Jordan-counting data lose. This is a motivated rank refinement of a natural four-level algebra family, not an arbitrary finite-field table.

## Limitations and checked literature
The scope is four ordered antichain layers and the square-zero locus, not all higher nilpotency orders. The general rank/Jordan census for parabolic nilradicals is prior work, not a newly asserted consequence. Principal sources inspected by full-text sections include arXiv:1703.00057, arXiv:2204.00066, arXiv:2207.12590 (Theorem 5.13), arXiv:2503.15440 (Theorem 2.5), and arXiv:2009.04243. Residual priority risk remains from other published parabolic/orbit-counting theory. Finite testing supports but does not substitute for the proof.

Self-review: passed. Independent audit: not yet performed.
