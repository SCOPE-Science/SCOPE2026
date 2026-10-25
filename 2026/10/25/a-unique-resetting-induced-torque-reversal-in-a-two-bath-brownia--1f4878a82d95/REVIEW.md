# Scientific review: unique torque reversal under one-coordinate Poisson intervention

## Correctness — PASS

The claim concerns \(a,b,D_x,D_y>0\), \(ab>c^2\), \(c\ne0\), and \(0\le\theta<1\). Synchronous coupling of trajectories with shared thermal drivers and Poisson events is contractive because the positive-definite harmonic restoring force contracts Euclidean differences and each jump does not expand them. The quadratic Lyapunov inequality provides finite stationary second moments and a unique invariant law. Stationary generator identities exactly close on three quadratic moments. Independently reconstructing the three-by-three determinant gives \(\Delta>0\); Cramer's rule gives the torque polynomial in \(p=r(1-\theta)\). An explicit positive derivative proves the threshold \(q_*(p)\) is strictly monotone with endpoints one and infinity, yielding the necessary and sufficient reversal condition and unique stall. Exact rational checks exercised 347 admissible parameter sets but are not substituted for the proof.

## Originality — PASS, residual priority risk

The no-reset result of Filliger and Reimann (2007) is strictly weaker: it yields only the zero-intervention endpoint. Olsen and Löwen (2024) examine partial reset of coupled degrees of freedom, but their Fourier--Laplace moment hierarchy assumes a spatially homogeneous free marginal propagator (their equation (4)), which a symmetrically coupled confining harmonic well does not possess. Abdoli, Olsen, and Löwen (2024) treat shear drift, with no stationary law under the stated unconfined coordinate-only reset, and not the present two-bath conservative well. Abdoli and collaborators' magnetic/shear gyrator reversals use altered continuous forces, not these jumps; their results do not logically yield the temperature-ratio threshold or its monotonicity. No equivalent classification was located in the searches undertaken, though general linear jump-diffusion moment methods or unindexed specialist research could predate the formulation. The full text of a partially relevant one-dimensional thermodynamic-work paper was not established; its abstract alone cannot exclude broader coverage.

## Mathematical value — PASS

The theorem gives a complete physically interpretable sign-phase classification for a minimal coupled two-thermostat machine under local stochastic intervention. Its exact boundary separates one-reversal and no-reversal regimes; strict global monotonicity rules out multiple reversals, determines the unique stall explicitly, and shows resetting the cooler coordinate cannot produce a positive-rate reversal. The high-rate residual torque identifies an intervention-induced torque even without temperature contrast. These are structural exact parameter statements rather than isolated numerical examples or a reparameterization of the no-reset formula.

## Verification and limits

The standalone `verify.py` was run successfully using exact rational arithmetic. Publicly claimed evidence is limited to the proven conservative potential torque, not angular probability-current winding or total energetic work of jumps. References were compared by their logical premises and observables; no claim of exhaustive literature coverage or independent external certification is made. Particular uncertainty remains about unlocated published treatments of general linear stochastic systems with subcoordinate contraction.

Self-review: passed. Independent audit: not yet performed.
