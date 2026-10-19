# Scientific review: cubic-chirp one-impulse Gabor tomography

## Correctness — PASS

The final claim follows from one exact ambiguity expansion, elementary imprimitive quadratic Gauss-sum reductions, prime-power root geometry, and an orthogonal Weyl-basis diagonalization of the measurement operator. For odd primes at least five, the primitive Gauss branch cannot be small enough to equal the minimum at exponent at least two; the remaining branch reduces to the nearest odd-order root to negative one. In characteristic three the quadratic coefficient gains one prime-power factor, producing a different minimum. For dyadic moduli the linear and quadratic congruence valuations classify every zero and give the rank count. The proof separately treats \(N=2\) and \(N=3\), all nonzero inputs, zero lag, and reduced Gauss modulus two. The packaged `verify.py` was executed and its output matches `verification_output.txt`; it independently reproduces the ambiguity identity, sharp minima and multiplicities, dyadic zero sets, and lifted singular values. The verification is a finite cross-check, not an infinite proof.

## Originality — PASS, best-knowledge

Actual database searches compared cubic chirps, quadratic chirps with one impulse, one-coordinate Gabor perturbations, exact ambiguity zeros and singular values, phase-retrievable Gabor frames, and modulated prime-power Gauss sums. The nearest full-text published quadratic-impulse result obtains a \(\sin(\pi/(2N))\) margin for odd \(N\); it does not cover the cubic \(\sin(\pi/(2p^{a-1}))\) improvement or the dyadic valuation-rank formula. The full-text published one-coordinate discriminant applies instead to a flat constant background. Salanevich's 2023 multi-window paper uses a polarization construction with fundamentally different inputs and conclusions. Bojarovska--Flinth establishes the general tomography criterion but not this exact evaluated window. Li's 2026 work discusses the unperturbed cubic chirp and different perturbation schemes. These implications are strictly weaker or inapplicable to the displayed specific claim. Residual risk: an unindexed earlier exact cubic-impulse ambiguity calculation or a stronger window theorem might subsume the present result.

## Mathematical value — PASS

The fixed one-spike cubic window is a natural elementary radar/Gabor design with just one amplitude defect. Its complete prime-power arithmetic obstruction, sharp singular conditioning, complete minimum multiplicity and exact dyadic nullity determine whether **all matrices** can be reconstructed from its minimal-size Weyl-orbit intensity design. The cubic-specific factor improvement over the previously published quadratic-impulse seed at odd nonprime powers is a substantive, quantitative difference, not a mere alternative proof of existence. The results do not claim full spark, best conditioning among all designs, or nonlinear phase-retrieval failure in even dimensions.

## Limits and closest primary sources

The most relevant inspected sources are Salanevich, arXiv:2307.00834, full HTML Sections I--III; Bojarovska and Flinth, arXiv:1503.05800, full preprint; Li, arXiv:2609.09614, material on unperturbed cubic chirps; and the complete published primary texts of the quadratic-impulse, one-coordinate, and Malikiosis-seed results (identifiers `03361b3cff9c`, `4ad1eba7465a`, `8ac7d311b287`). Published indices cannot establish absolute novelty. Verification files require NumPy. Independent scientific audit and testing beyond the stated families were not performed.

Self-review: passed. Independent audit: not yet performed.
