# Scientific review

## Correctness (C): PASS
The universal lower bound uses the published factor-two amplification theorem for the Lyndon representative of a primitive necklace, whose linear and cyclic run counts agree. For the upper bound, every one of the 67 witnesses in `witnesses.json` was checked against the full stable-rank BWT reconstruction and against independently sorted circular rotations by `verify.py`. The actual program and its recorded success output are included. The claim is limited to the explicitly certified integer interval and its extension to larger alphabets by inclusion.

## Originality (O): PASS within inspected evidence
The closest direct work is Kumallagov (2026), which states the conjectured all-length sharpness and proves a universal lower bound, initial cases, and arithmetic subsequences. Fici et al. (2026) establish totally unclustered outputs but do not impose the minimum-run inverse condition. Mantaci et al. (2017) establish the half-length lower bound but not existence in every length. Full-text inspection of Fici et al. and of the Mantaci author postprint supports these distinctions. Indexed published-result and literature searches for the exact invariant, single-cycle characterization, finite ranges, and conjecture did not reveal coverage of the consecutive interval from 14 through 80. The central 2026 preprint was available as an abstract and indexed technical summary, not as readable full text, leaving a specific residual duplication risk. Selected lengths in the interval can already be covered by its arithmetic constructions; the independently assessed contribution is the *whole consecutive interval*, not those instances individually.

## Value (V): PASS
The theorem certifies 67 consecutive, exact extremal values in a natural optimization problem recently isolated as a conjecture. A single seed family or an isolated next integer would provide weak evidence; this complete initial window is a stronger reproducible benchmark for proposed constructive proofs and indicates no finite exceptions through 80. Its certificate is compact, deterministic, and independently replayable, yet no infinite generalization is claimed.

## Limits and bibliography
It remains possible that a source not available in full, an appendix, or another database contains an equivalent consecutive-window computation. This does not give a general existence construction for all lengths. The lower-bound proof uses Mantaci et al. (2017), and the motivation and competing partial coverages are Fici et al. (2026) and Kumallagov (2026), bibliographically identified in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
