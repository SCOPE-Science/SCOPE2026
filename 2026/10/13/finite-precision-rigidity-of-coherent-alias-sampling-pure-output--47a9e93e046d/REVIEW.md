# Review

## Correctness
PASS. The explicit retained-garbage tuples yield an exact positive Gram decomposition. Since all exchanged-branch deficits are strictly positive, rank one forces every alias to have the same image; the remaining unswapped terms then force all noncentral thresholds to vanish. Uniform sampled probabilities imply a positive-mass conservation equation. Its support forces the alias self-map to be a permutation and its weights to be constant along each cycle. The state is therefore exactly maximally mixed, with the stated spectral distances and entropy. The proof covers all powers-of-two address and precision sizes; finite enumeration is corroborative only.

## Originality
PASS, with a specified residual coverage risk. Babbush et al. (2018), Eq. (38), already contain the explicit alias-sampler garbage state. Liu et al. (2026), Eq. (7) and Section 2.3, already know the output probabilities and acknowledge retained garbage. Neither inspected source states the **complete legal-table iff theorems** for pure output and uniform output, nor the universal exact uniform-output maximal-mixing and fidelity consequences. The later clean polynomial-state sampler constructs a different new-output-register and fiber-uncomputation scheme. Targeted exact-source, alias, equivalent-formulation, and stronger-coverage searches identified no dominating theorem. The strongest originality risk is that the result could have been independently extracted as a corollary of the 2018 full-state representation under other terminology.

## Value
PASS. The source explicitly motivates separate benchmarks for classical probability reproduction and coherent state preparation. The theorem turns that distinction into a complete finite-precision rigidity principle, showing that perfect uniform sampling always creates exactly the maximally mixed address and maximally entangles it with retained registers, unless the circuit is changed or garbage is cleaned. The pure-output classification identifies the only legal exceptions and the role of strict bit-width storage. This is a structural all-table limitation rather than a one-off numerical example.

## Closest literature and limitations
The three closest papers are arXiv:2605.18877v1, DOI 10.1103/PhysRevX.8.041015, and arXiv:2610.03800v1. All supply important background; the 2018 source already contains a garbage-state formula, and the October 2026 work supplies a genuine cleanup construction for a different sampler. The theorem is specific to retained-garbage compare-and-swap with strict b-bit keeps and does not rule out any clean alternative or quantify full-oracle simulation error.

Self-review: passed. Independent audit: not yet performed.
