# Scientific review

## Correctness — PASS
The assertion covers every real Hadamard matrix of an existing order, every one-entry sign change, and the induced spectral norm on complex matrices. After sign normalization, the two-mode block and orthogonal complementary block follow from the Hadamard equations. At the analytic optimum, the trace-norm lower witness is attained by the real polar orthogonal factor, and the positive operator \(X\) satisfies the exact Gram identity \(B^{\mathsf T}X^{-1}B=X\) with all diagonal entries equal to the proposed sharp constant. The classical Schur factorization inequality matches this lower witness exactly. The order-two exception is handled independently. The script provides 521 supplementary assertions in six nontrivial orders and integer scalar checks; it is not a proof by finite enumeration.

## Originality — PASS, with residual historical-priority risk
The strongest near match is Holbrook–Johnston–Schoch, arXiv:2206.02863, where the order-four one-flip example already has value \((2+3\sqrt6)/5\), and the Hadamard maximum \(\sqrt n\) and computational SDP tools are established. None of the inspected general and example results states the all-Hadamard-order one-flip law or the exact common certificate. Davidson–Donsig (arXiv:math/0506073), Cowen and collaborators (full Purdue preprint), and Christensen (arXiv:2309.17092) give general Schur multiplier factorizations and other examples, which do not imply the specific radical identity without a new symmetry calculation. An older Cowen–Dritschel–Penney article was only located bibliographically and not inspected in full; hidden coverage is possible. The lack of a matching search result is not treated as a proof of novelty.

## Mathematical value — PASS
The unperturbed Hadamard sign pattern attains the largest possible Schur multiplier norm among real sign matrices. Flipping one entry is the smallest combinatorial perturbation and a natural rigidity/stability test. The exact deficit, its independence of the Hadamard equivalence class, an explicit all-order optimizer, and a sharp certificate jointly resolve this structural family rather than provide an arbitrary sample calculation. The known four-by-four value is explicitly excluded from the novelty claim.

## Limits and provenance
This is a theorem about exactly one flipped sign and actual Hadamard orders; it does not assert all-order Hadamard existence. The construction gives a proof in real and complex operator norms, but it does not classify multi-defect patterns. The computational comparisons support the exact algebraic derivation. No external mathematical audit has been conducted. Earlier priority for the general claim remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
