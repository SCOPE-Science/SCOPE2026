# Mathematical review: finite-field dihedral quandle idempotents

## Correctness

PASS. Finite Fourier inversion is legal precisely because the characteristic is coprime to the odd order \(n\). Expanding the specified multiplication yields \(A_k=A_{-k}A_{2k}\). Support is a union of \(\Gamma\)-orbits; cancellation on any active orbit gives \(A_{-k}=A_k^{-1}\) and \(A_{2k}=A_k^2\), leading to the two explicit root-exponent cases. Frobenius descent across cyclically permuted \(\Gamma\)-orbits imposes exactly the three root conditions counted by \(g_D\). The inverse transform returns all and only the base-field idempotents. Direct exhaustive enumeration and independent inverse-transform constructions agree in the documented finite examples.

## Originality

PASS within inspected coverage, subject to stated residual risk. The basic Fourier equation is not new: Elhamdadi–Ta–Virgin, arXiv:2609.03799, use this recurrence over the complex numbers. Elhamdadi–Nunez–Singh–Swain, arXiv:2204.11288, address quandle algebra idempotents and coverings, not this complete nonmodular finite-field orbit census. Small-order integral and finite-field examples are also known. The assessed claim is the exact arithmetic classification for arbitrary odd \(n\), every finite field of characteristic prime to \(n\), and the additional Frobenius conditions when the field does not split the \(n\)-th roots. The known Fourier recurrence strongly motivates the proof and leaves a possibility that the finite-field extension occurs elsewhere; no priority beyond the searches and material inspected is certified.

## Value

PASS. Idempotent sets are basic invariants of a nonassociative algebra, while general counting was unavailable in the compared finite-field setting. The theorem classifies the entire set rather than a sample or one tiny algebra and separates split and nonsplit field behavior by a precise Galois-orbit mechanism. Arithmetic sensitivity occurs already for the same eleven-element quandle over different finite fields, with both the count and actual idempotents explicitly obtainable.

## Literature limits

The 2026 Fourier analysis provides a precursor recurrence. Earlier R3 and R5 calculations are special cases, not independent results claimed here. Some older quandle-ring articles and a thesis were available only in part; an equivalent older characterization cannot be ruled out. The characteristic-dividing-order case is excluded, and finite calculations supplement rather than replace proof.

Self-review: passed. Independent audit: not yet performed.
