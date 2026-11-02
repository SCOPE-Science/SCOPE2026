# Scientific review

## Correctness (C): PASS
The general lower bound is the published BWT factor-two run bound. The upper bounds are 34 explicit ternary last columns. Their complete stable-sorting permutations are single cycles; exact Hamming distances to sorted columns give the optimal cyclic run count. Two independently formulated standalone checkers verify the entire range 31–64, the second by reconstructing the necklaces and sorting every rotation. Unlike an extrapolation, each asserted length is certified separately; no claim extends past length 64.

## Originality (O): PASS
The closest primary source, Kumallagov (arXiv:2606.01267v1), states the all-length problem as a conjecture and provides direct witnesses only through length 12, plus an arithmetic family that already implies six cases in the claimed range (36, 37, 52, 53, 60, 61). The 2025 Fici–Gabory–Romana–Sciortino existence theorem does not bound cyclic input runs. The 28 other lengths in the present interval are not covered by these published statements. Earlier finite results through length 30 are excluded from the claim. Direct searches for equivalent formulations, the sharpness function, and interval-specific results did not identify stronger published coverage; lack of a search hit is not proof of absolute priority. Residual risk: unpublished or differently indexed certificates could exist.

## Value (V): PASS
The open conjecture asks for the attainability of the exact factor-two BWT run amplification. A contiguous interval through the natural dyadic cutoff 64, exceeding the previously recorded cutoff 30, gives exact values at 28 lengths not implied by the currently inspected arithmetic theorem. Moreover, every witness is a perturbation of an alternating binary last column in at most six locations. This is a checkable, mathematically motivated finite sharpness cutoff and a sparse-witness phenomenon; it does not purport to settle the infinite problem.

## Closest literature and limits
The sharpness problem and Hamming/cycle equivalence come from Kumallagov (2026); the general unclustered-existence theorem and cycle criterion are also in Fici et al. (2025). The proof is a finite certificate combined with a known unconditional lower bound. It does not enumerate all minimizers, show minimal sparse perturbation size, or prove all-length sharpness.

Self-review: passed. Independent audit: not yet performed.
