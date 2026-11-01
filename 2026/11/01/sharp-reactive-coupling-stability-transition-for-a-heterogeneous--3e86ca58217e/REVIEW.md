# Scientific assessment

## Correctness — PASS

The exact phase-locked orbit satisfies the full nonlinear equations because its three complex side vectors sum to zero and the radial squares equal the growth rates minus three. The full six-real-dimensional linearization is reconstructed without discarding amplitude or phase directions. The characteristic polynomial factors into one symmetry-zero mode and an explicitly listed quintic. Independent reconstruction of each five leading Hurwitz minors from the stated Jacobian matches the written formulas exactly. The strictly monotone cubic cutoff gives a unique positive stability boundary. The Routh first-column signs prove precisely two unstable eigenvalues below the boundary and zero above; at equality the auxiliary quadratic and the positive cubic factor establish a simple imaginary pair and three stable eigenvalues. The simple cutoff yields transverse crossing. The verifier prints `EXACT_CERTIFICATE_OK`.

Risks and limits: this is a linear orbital stability theorem, not proof of a nonlinear secondary branch, its critical normal-form coefficient, or global attraction.

## Originality — PASS under examined evidence

The October 2026 source constructs and numerically samples the polygonal phase-locked manifold, including an unstable triangular region within its tested parameter plane. An exact analytic existence example of a stable heterogeneous triangle is also known. Neither establishes the complete stability/instability phase diagram as the imaginary coupling traverses all real values with a fixed linearly spaced growth triple, nor the exact unique crossing polynomial, exact unstable index, and simple imaginary-pair boundary. Nearby older work on globally coupled amplitude oscillators addresses clustering, strong-coupling synchronization, or delayed control with substantially different scope. Relevant indexed mathematical findings and the source's polygon formulas were compared by claim and implication, not by title matching.

Risks and limits: no mathematical priority claim can be absolute. Some historical articles were available only at abstract level; independent bibliographic assessment remains important.

## Value — PASS

The source's numerical triangular-sector instability and broader configuration dependence naturally ask whether a three-active-oscillator zero-mean polygon has an exact reactive-coupling stabilization threshold. The squared side lengths \((49,169,289)\) form an arithmetic progression, so the example respects the source's natural linear-growth heterogeneity instead of imposing a generic unrelated parameter slice. The theorem computes the entire one-parameter phase diagram, exhibits stabilization by reactive coupling in the smallest nondegenerate polygon, and identifies the exact spectral mechanism. The classification is more informative than either a stable isolated example or a finite numerical scan, and it is useful for oscillator-coupling design and bifurcation benchmarks.

## Closest sources and limitations

Zhao–Uchida (2026), arXiv:2610.08239v1, Sections 2 and 5–7, supplies the polygonal family, numerical stability survey, and dimensionality. Lee–Ott–Antonsen (2013), arXiv:1304.3974, treats a broad heterogeneous global-coupling setting, with its directly retrieved abstract describing different synchronization and clustering regimes; its full text was not materially inspected here. Schneider (2013) treats delayed feedback for a three-oscillator rotating wave, not the zero-delay unequal-growth spectral threshold; only its abstract was inspected. Independent audit and validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
