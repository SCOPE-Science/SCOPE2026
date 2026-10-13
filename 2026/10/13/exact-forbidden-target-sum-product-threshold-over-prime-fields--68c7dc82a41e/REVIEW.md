# Scientific review

## Correctness — PASS

The independent-set correspondence is exact, including equal summands/products represented by graph loops. The sum involution gives the sharp universal upper bound. The colored graph has only alternating cycles and paths, together with isolated double-colored edges and an exceptional isolated looped point; the only obstruction to saturating all sum pairs is one path whose endpoints are the two multiplicative square roots. For nondegenerate square targets, a projective transformation relates their connectivity to its even order. The repeated-eigenvalue case \(a=4\) has odd projective order \(p\) and no loss. A standard-library verifier computed exact maxima independently for all 4,178 prime-target pairs through prime 199, and directly enumerated subsets for primes through 13. Residual risk: an unnoticed path-endpoint parity case or algebraic conjugation slip, though these were explicitly checked in the proof and examples.

## Originality — PASS

Tang's arXiv:2603.29992, §§1–2, proves the target-1 construction and its half threshold, and gives the six-cycle decomposition specifically for \(x\mapsto1-x\) and \(x\mapsto1/x\). Its full text was inspected. The present theorem treats every nonzero target and identifies a new, genuinely varying arithmetic obstruction. Rescaling cannot equate the problems because sums and products scale by different powers. Searches of relevant literature and indexed mathematical-result records did not find a theorem stating or implying this exact projective-order dichotomy. Shao's arXiv:2604.17117 concerns asymptotic global sum/product sizes and does not assert a simultaneous omitted-target criterion. Residual risk: an unindexed equivalent result in finite-field graph theory; The relevant theorem and proof outline in Shao's original PDF were inspected; the remaining pages were not reviewed exhaustively.

## Value — PASS

The motivating target-1 result refutes a proposed universal covering property. It leaves the natural question of what happens for an arbitrary specified missing residue. The formula completely answers that question and reveals a sharp parity/Legendre-symbol phase transition: the maximum can decrease by exactly one and never more. This gives a structural obstruction that neither the existence theorem at target 1 nor the elementary half-density upper bound detects. It is a full natural parameter classification, not a chosen numerical example.

Self-review: passed. Independent audit: not yet performed.
