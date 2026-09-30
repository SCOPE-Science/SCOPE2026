# Independent audit — 2026-09-30

Record: `2026/09/19/real-compact-operators-single-commutators--99c7fbfeedaf`  
Assigned and audited source tree: `d698d58514c6eb4bad990f0c87a36e5902778aca`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `5f8898bb7cb687906c34581a9e44a5ff04718657`  
Disposition: **passed**

## Correctness

**independently_supported_with_source_portability_check**. The real-field reduction is coherent. The diagonal-balancing lemma uses only the real quadratic form q(x)=<Rx,x> and trace invariance on two-dimensional compressions; the greedy sign ordering yields residual partial sums tending to zero. For a non-trace-class compact, a sparse orthonormal sequence makes PT+TP-PTP trace class. If the symmetric compression is non-trace-class, the displayed uniformly bounded real 2x2 similarities create diagonal mass of both signs; if the skew part is non-trace-class, the real rotation-block decomposition and fixed shear create pairs (-s_n,s_n). An l1 diagonal perturbation cannot destroy either divergence, so the real balancing lemma gives zero diagonal. Liu's zero-diagonal and trace-class constructions use finite trace-zero matrix commutators plus block/Sylvester/Neumann operations; Tran's theorem supplies the finite matrix input over the same real field, and the remaining scalar shifts and block algebra can be chosen real. The finite-rank Anderson carrier has an explicit real-matrix form in the later commutator literature. The nonseparable extension is valid because the closed span of ran T+ran T* is separable and reducing, with T zero on its orthogonal complement.

## Originality

**qualified_real_field_extension_with_inaccessible_prior**. Liu's September 2026 theorem explicitly treats separable infinite-dimensional complex Hilbert space, while Tran's matrix commutator bound explicitly works over both real and complex fields. Current searches did not locate the resulting all-compact single-commutator theorem over a real Hilbert space. The field-sensitive ingredients are genuine but substantially reuse Liu's new architecture. Fan–Fong's 1987 paper 'Operators similar to zero diagonal operators' is the most relevant older source; open-access searches did not expose the full article and authorized Oxford retrieval returned no verified PDF. Thus no claim is made about its detailed field conventions, and it remains a residual prior-art risk for the zero-diagonal reduction, though not evidence of the full all-compact theorem.

## Scientific value

**high_value_field_extension**. The theorem closes a natural field gap in the new commutator-width-one result and preserves the universal square-root norm scale. It also isolates an explicit real replacement for the complex phase-balancing step, which is necessary because complexification alone does not preserve a single real commutator representation.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/real-compact-operators-single-commutators--99c7fbfeedaf
- https://arxiv.org/abs/2609.20672
- https://arxiv.org/abs/2609.20161
- https://arxiv.org/abs/1303.4844
- https://www.jstor.org/stable/20489272
## Literature access note

Peng Fan and Che-Kao Fong, Operators Similar to Zero Diagonal Operators (1987): Bibliographic/JSTOR issue pages were available but not the full article text. Authorized retrieval reached the publisher and returned no verified PDF. The source is not claimed to have been read in full.

## Limitations

- The proof is an adaptation of Liu's complex construction and its detailed field portability is essential.
- The universal constant is not optimized, and no stronger Schatten membership of the factors is proved.
- Finite-dimensional real spaces are necessarily excluded because commutators have trace zero.
- Fan–Fong (1987) could not be inspected in full after open-access and authorized institutional attempts.
