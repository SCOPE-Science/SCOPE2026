# Mathematical review

## Correctness — PASS

The centered edge vectors are Parseval because their second-moment sum is \((n-2)P_V\). A matching-selected effect equals \(2P_M/(n-2)\), where \(P_M\) is an explicit mean-zero pair-block orthogonal projection. Therefore the commutator is exactly \((R_MR_N-R_NR_M)/(n-2)^2\); the permutation product has two cycles of length \(k\) on each alternating component of length \(2k\). Fourier diagonalization yields every eigenvalue including zero multiplicities. The sine equality cases prove the commuting and maximum classifications for all even \(n\ge4\). Cyclic-order and endpoint-choice counting proves the two enumeration formulas. Explicit four-outcome sums verify joint measurability. The extracted checker passed all finite tests up to \(n=12\) described in `VERIFICATION.md`.

## Originality — PASS (best-knowledge assessment)

The closest inspected primary literature concerns Parseval-frame POVM measurability and spectra of individual observables (Kużel–Łukasiewicz, arXiv:2601.11225), edge-midpoint projection constants (Deregowska–Lewandowska, arXiv:2608.08695), and the general theory of two orthogonal projections (Halmos, 1969). These do not state the present matching-indexed commutator spectral multiset, sharp eight-cycle attainment criterion, and exact partner counts. The matching-erasure Gram norm problem and the Mercedes-frame coarse-graining commutator problem have different underlying operators and hypotheses. Searches for pair-partition conditional expectations, matching involution spectra, and matching coarse-grained frame commutators gave no verified equivalent. Generic principal-angle reductions are closely related, so unlocated equivalent specializations remain a genuine priority risk; absence of a search hit does not prove novelty.

## Mathematical value — PASS

The problem measures the failure of commutativity inside an explicitly compatible family of two-outcome quantum effects. The theorem gives every commutator eigenvalue, not merely a sample or bound; the first nonzero alternating six-cycle, exact eight-cycle sharpness threshold, and independent counts of commuting and maximizing partners connect the measurable operator quantity to finite matching topology. This natural complete classification provides a sharp finite-size benchmark without claiming arbitrary-frame generality.

## Limits and closest literature

All claims assume even \(n\ge4\), the edge-only centered simplex Parseval frame, and pairs of *perfect* matchings. Standard Halmos two-projection theory partly explains the computation but does not by itself present the alternating-cycle enumeration. Publication priority and the proof have not been independently assessed.

Self-review: passed. Independent audit: not yet performed.
