# Independent audit — 2026-09-29

Record: `2026/09/18/finite-precision-autoregressive-finite-state-collapse--d45f7b366886`  
Assigned and audited source tree: `0515637c14891b0478264bdc5600f167e3844c9c`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**supported**. The finite-state construction matches the explicit q-decimal semantics of Qiao–Yu–Qiu–Gao. Their Appendix C bounds every rounded scalar to a finite grid plus special values, proves finite periodicity of the recursively rounded RoPE matrices, and uses exactly the saturation threshold 10^(2q)+1: that many copies of any positive rounded exponential (minimum 10^(-q)) force the rounded softmax denominator past 10^q to Inf, after which their convention c/Inf=0 makes the head output zero. Therefore old positions can be grouped exactly by layer, RoPE phase and hidden-vector type, with multiplicities capped at B_q. If no capped positive type occurs, every positive multiplicity is stored exactly, including cases where several unsaturated types jointly overflow the denominator. Causality freezes old hidden vectors, so the new position can be propagated block by block and the capped histograms updated deterministically. The finite-state orbit argument then gives uniform bounded halting, ultimate periodicity of every nonhalting deterministic continuation, finite range for total generators, and regularity for total deciders. The displayed state-count is deliberately crude but valid.

## Originality

**qualified_model_specific**. Qiao et al. prove finite-precision incompleteness by a repeated-block argument for their non-converging Turing-machine class, not the all-prefix capped sufficient state or the iterative bounded-generation/ultimate-periodicity statement. Jerad–Svete–Li–Cotterell independently characterize a related fully uniform finite-precision soft-attention model with component-periodic RoPE by a regular temporal-logic class, so regular recognition under periodic finite precision is important prior art and is correctly excluded from the novelty claim. Targeted searches did not locate the model-specific autoregressive orbit theorem for Qiao's overflow semantics. The claim remains qualified because both relevant preprints are extremely recent.

## Scientific value

**meaningful_structural_sharpening**. The theorem strengthens the motivating limitation from a selected family of computations to a global dynamical statement for every deterministic autoregressive trajectory in the exact model: halting reasoning has a model-dependent constant length bound and nonhalting reasoning eventually cycles. That is a useful clarification of what iterative decoding can and cannot buy under this particular fixed-precision arithmetic.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/finite-precision-autoregressive-finite-state-collapse--d45f7b366886
- https://arxiv.org/abs/2609.20335
- https://arxiv.org/abs/2608.11909
- https://arxiv.org/abs/2310.07923

## Limitations

- The theorem is specific to Qiao et al.'s finite q-decimal arithmetic, recursively rounded periodic RoPE and explicit Inf division convention.
- It assumes deterministic decoding with fixed tie-breaking and does not cover stochastic sampling, external tools or memory, growing precision, or nonperiodic realized positional state.
- The state-count is an upper bound, not a minimal automaton size.
- Originality is qualified by the closely related regular-language characterization of Jerad et al. and the recency of both 2026 preprints.
