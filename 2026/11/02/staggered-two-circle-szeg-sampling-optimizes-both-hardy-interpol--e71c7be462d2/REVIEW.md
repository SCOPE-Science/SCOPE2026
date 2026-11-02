# Scientific review

**Correctness — PASS.** The normalized Hardy kernel is explicitly defined and yields a positive definite \(2k\)-point Gram matrix for \(0<r<s<1\). Fourier alias summation produces all \(k\) two-by-two blocks. Positive diagonal congruence orders both their smallest and largest eigenvalues, making the \(k-1\) and zero sectors globally extremal. Strict monotonicity of two-by-two eigenvalues in the off-diagonal magnitude proves the unique staggered optimizer. The exact positive determinant gives the sharp exponential asymptotic without subtractive cancellation. An actual standalone checker executes 6099 finite assertions; these are auxiliary to, not replacements for, the proof.

**Originality — PASS, provisional.** Speransky–Terekhin (2018), Baranov–Batenev (2022), and Groenewald–ter Horst–Woerdeman (2024) were compared at the level of their Hardy sampling/interpolation statements and relevant proofs. None of their inspected results specifies the angularly optimized two-radius Gram spectrum. The closest inspected single-radius Szegő orbit theorem determines determinant stability and a one-radius geometric spectrum, but its hypotheses do not cover distinct radii and its conclusions cannot imply the mixed-radius sharp minimax and condition-number law. Historical-priority uncertainty remains, particularly under alternative Cauchy-matrix or optimal-node terminology.

**Value — PASS.** Equally spaced radial sampling layers arise naturally in constructive Hardy representation and interpolation. The exact inter-layer offset simultaneously controls worst-case noise amplification and maximal evaluation gain, a stronger design statement than a determinant optimum alone. The rate \((rs)^{-2k}\) for Gram conditioning gives a sharp limit on recovery as the node count grows, with an explicit radii-dependent prefactor.

**Residual limitations.** The node count must agree on the two rings; each ring is regular and equally weighted; radii are distinct and fixed in the asymptotic. No independently validated priority or proof certification is asserted.

Self-review: passed. Independent audit: not yet performed.
