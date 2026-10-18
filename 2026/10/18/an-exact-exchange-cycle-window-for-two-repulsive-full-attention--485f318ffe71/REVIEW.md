# Review: An exact exchange-cycle window for two repulsive full-attention tokens

## Correctness — PASS

The orthonormal sum/difference basis gives an exact conjugacy to the positive scalar ratio map and the exact sign rule. The derivative is positive throughout the claimed sharpness and step range, excluding hidden scalar period doubling; the critical asymptotics follow from controlled expansions at infinity and zero. Endpoint configurations are treated separately and the normalization is never zero except at the expressly excluded consensus point at unit step. The analytic all-parameter proof is supplemented, not replaced, by the standalone checker.

## Originality — PASS with residual risk

Altafini's full-attention discrete model, arXiv:2610.13518v1, is compared at its governing equation and positive top-eigenvalue hypothesis; that hypothesis excludes negative identity value feedback. Gao, Yang and Chen's repulsive model, arXiv:2609.28448v1, excludes self-attention diagonals, which for two tokens eliminates sharpness-dependent behavior. The prior attractive identity-value two-token analysis and indexed analogues therefore do not imply the unmasked negative-value result. Unknown equivalent generic scalar-map or projective formulations remain a genuine bibliographic risk; no search can certify universal absence.

## Mathematical value — PASS

The result settles the global regime structure of the simplest nontrivial repulsive full-attention system, including a finite interval of stable exchange two-cycles and two exact critical relaxation amplitudes. It isolates an interpretable self-loop effect that disappears when diagonals are masked. It is not claimed to generalize to all attention kernels, sharpness values or token counts.

## Closest references and limits

C. Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1 (2026); Q. Gao, Z. Yang and X. Chen, *Nonequilibrium Phases of Repulsive Self-Attention*, arXiv:2609.28448v1 (2026); C. Altafini, *Multistability of Self-Attention Dynamics in Transformers*, arXiv:2511.11553v1 (2025; only abstract-level material inspected). The proof assumes exactly two unit tokens, softmax sharpness at most one third, negative identity value feedback, full self-inclusion and step at most two. The sharpness restriction is sufficient, not asserted necessary.

Self-review: passed. Independent audit: not yet performed.
