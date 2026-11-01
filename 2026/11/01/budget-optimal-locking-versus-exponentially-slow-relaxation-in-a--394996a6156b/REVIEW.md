# Scientific review

## Correctness — PASS

The asserted domain is an autonomous attractive Kuramoto triad with intrinsic frequencies \((-\omega,0,\omega)\), \(\omega>0\), off-diagonal budget \(K>0\), and finite exponent \(p\ge0\). Relative phase equilibria satisfy \(\sin u=\sin v\). This supplies an **exhaustive** two-branch classification, not an unsupported symmetric ansatz: the nonsymmetric complement has a negative Laplacian trace and is linearly unstable; the symmetric branch has two explicitly evaluated nonneutral eigenvalues. Strict concavity of its scalar balancing response on \((0,\pi/2)\) gives the fold and exact necessary-and-sufficient criterion for exponential attraction. An exact envelope derivative proves threshold monotonicity; the spectral limit yields its exponentially small relaxation gap. Continuous positive gap values and both vanishing endpoints establish existence, not uniqueness, of a finite rate optimum.

The included `verify.py` passed symbolic Laplacian identities, 400 direct equilibrium/eigenvalue cases, threshold samples, and asymptotic diagnostics. These samples are corroboration only. The unreduced phase-space zero eigenvalue is correctly handled by taking the quotient by common rotation.

## Originality — PASS under the inspected evidence

The full accessible HTML of Pando et al., arXiv:2603.29648v2, was read in its model, generalized allocation, analytical and supplemental strong-coupling sections. It proposes the budget-normalized power weighting and analyzes large random ensembles, with approximate strong-lock calculations, but does not provide this exact three-site nonlinear locking/budget/rate trade-off. Zhao–Zhou arXiv:2407.11314v2 treats an isosceles triangle with identical intrinsic frequencies, so its equilibrium classifications do not cover a detuned triad. Xin–Kikkawa–Liu 2016 addresses uniform all-to-all couplings, not power-weighted cross-link allocation. Closest published mathematical-result searches disclosed results on Stuart–Landau triads, repulsive discrete triangles, and a four-node Braess locking effect; their assumptions are not those of this theorem. Generic Jacobian, gradient-system and weighted-Laplacian arguments are prior tools.

Residual risk: an overlooked small-network Kuramoto optimization paper, or a broad weighted-triangle result specialized to exactly these parameters, could subsume the claim. No independence or exhaustive priority is asserted.

## Value — PASS

The work answers a concrete budget-constrained design question at the smallest nontrivial symmetric heterogeneous motif. Its exact threshold is not merely an isolated parameter value: it gives an all-exponent phase portrait, a strict opposite direction of onset and long-time robustness, and the existence of a nontrivial interior optimal allocation exponent for actual decay rate. This clarifies why an exponent optimized for existence of locking need not optimize synchronization time and supplies a finite-network contrast with the intermediate-exponent behavior reported for large random ensembles. The finding is local, not a global basin theorem, and does not extrapolate to arbitrary networks.

Self-review: passed. Independent audit: not yet performed.
