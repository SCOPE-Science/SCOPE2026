# Independent mathematical audit

## correctness

PASS

Reconstructed the full-limit and compactness proof for trace characters (χ_j(e)=j+1) with Haar probability. Clebsch–Gordan applied to the square of the packet and Haar orthogonality give the nonnegative quadruple tensor even for complex input. Opposite parities give zero; otherwise counting common weights agrees with NΔ/2 to within one, including touch/disjoint cases. Since (Σ|a_j|)^4≤N², this gives a uniform O(1/N) normalized error. Replacing Δ by its cell averages costs another O(1/N) by Lipschitz continuity and the same bound. Expansion of the parity indicator gives exactly the two functionals on the ordinary and alternating profiles, with factor 1/4. Each fixed triangular indicator gives a compact Hilbert–Schmidt operator; a strongly convergent kernel image paired against a bounded weakly convergent second factor gives pointwise convergence of B_t, with |B_t| bounded by the squared norm. This alone gives weak continuity of the integral by dominated convergence; the frozen strip/equicontinuity argument also works. Positivity and homogeneity force the ball maximum onto the unit sphere and permit a nonnegative maximizer. The oscillating cell signs are weak-* null, so testing both weak limits against p,q gives total squared norm at most one. The inequality ||f||⁴+||h||⁴≤1 supplies the upper bound; normalized cell averages of a nonnegative maximizer recover it. Replacing near-optimal arrays by moduli does not decrease the fourth moment. Equality in the channel inequality forces one channel to have unit norm, and |⟨E_N,q⟩|≤⟨A_N,|q|⟩ for nonnegative A_N excludes a surviving alternating channel when A_N tends weakly to zero. Therefore along subsequences the moduli converge strongly to maximizers by equality of norms. The ramp triangular integral gives 136/315 before the quarter factor (independently cross-checked by bounded scalar quadrature). The packaged script was read, not executed. Its verification note's 'normalized' characters means orthonormal trace characters, not division by dimension; the frozen theorem's normalization is explicit.

## originality

PASS

The supported distinct result is a sharp full finite-target norm limit for the growing central packet, together with strong L² precompactness of all near-extremizer modulus profiles. The exact weighted Jacobi, sine and bandlimited equivalents were considered. The closest indexed proofs treat fixed-width packets, with a different scale and finite-dimensional profile problem. The inspected primary weighted Nikolskii theorems either concern endpoint evaluation/supremum norms, or give a lower-limit result at finite target exponent, not the stated full central limit and all-sequence compactness.

## value

PASS

This resolves a natural sharp synthesis norm for a full increasing sequence of central Fourier spaces. A matching variational limit is more informative than an order estimate, and the proof explains why parity does not permit a gain by splitting mass. Strong subsequential convergence of all near-optimal modulus profiles gives structure not implied by a numerical value of the norm. The claim remains useful without a closed-form maximizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
