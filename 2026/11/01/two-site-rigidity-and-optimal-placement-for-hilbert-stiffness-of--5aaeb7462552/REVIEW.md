# Independent mathematical audit

## correctness

PASS

Aggregating the core and leaf coefficients at site j into β_j gives the centered form −βᵀCβ/2+Σ t_j z_j², where z_j is the leaf coefficient: on the zero-sum space each pendant cut contributes exactly its length times z_j². Independently, the cyclic second difference of the distance row has spikes +2 at 0 and −1 at (n±1)/2 for odd n. Fourier transforming yields λ_j=−1/[2(1+(−1)^j cos(πj/n))] at nonconstant frequencies, maximized exactly at j=2,n−2 with value −a. For even n the two negative spikes coalesce to −2 at n/2, giving λ_j≤0 with zeros at nonconstant even frequencies, and hence persistent core-only zeros under arbitrary pendant lengthening. For odd n the uniform distance block's upper eigenvalue λ−t+√(λ²+t²) increases strictly with λ and exceeds the constant zero-sum direction's value −t at λ=−a. This gives γ=(a+t−√(a²+t²))/2 with only the two real frequency-two modes at the minimum. Their normalized leaf-coordinate vectors are ρ(cos(4πj/n),sin(4πj/n)), by the core-to-leaf ratio 1:−q. Equality after PSD updates requires a minimizer of the original form annihilated by every positive update. One leaf imposes just one equation; two different leaves give determinant proportional to sin(4πd/n), nonzero for odd n. This covers arbitrary positive increment sizes. The isolated double eigenvalue splits to first order by the compressed 2×2 update, whose trace and determinant are ρ²(u+v) and ρ⁴uv sin²θ; the complementary spectral gap gives the O(ε²) error. At fixed u+v the smaller root is optimized by equal allocation and maximizing sin²θ. Odd n makes the available angles a permutation of 2πr/n for nonzero r; the nearest quadrature is exactly π/(2n) away. Thus the stated gain and placement hold to first order, without asserting finite-budget optimality. Exact proof reconstruction, not the frozen numerical diagnostics, establishes these conclusions.

## originality

PASS

The normalization and related cycle/sunlet parity results are known. The distinct supported claim is the weighted reinforcement threshold and optimal infinitesimal placement, not the uniform base spectrum. Neither the inspected closest Resultary records nor the matching metrics/results in the available primary literature give that perturbation claim.

## value

PASS

This answers a concrete design question for a natural graph metric: what smallest support can change the worst centered embedding direction, and where is it best spent at first order? The odd cycle's double Fourier mode makes all individual reinforcements ineffective but every distinct pair effective, while an even-cycle obstruction survives arbitrary pendant changes. The exact placement and allocation criterion supplies information not contained in the binary support threshold or uniform spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
