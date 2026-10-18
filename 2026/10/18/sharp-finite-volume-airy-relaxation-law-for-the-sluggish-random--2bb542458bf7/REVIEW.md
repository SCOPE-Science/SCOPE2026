# Scientific review: confined sluggish-walk spectral gap

## Correctness

**PASS.** The exact reversible Dirichlet form follows from neighboring conductances \(w_kP(k,k+1)=1\). Discrete Sturm oscillation and reflection parity identify the first nonconstant mode as odd. A half-chain variational principle, an explicitly bounded mass-quadrature expansion, and simple-eigenvalue perturbation of a weighted Sturm–Liouville problem prove the two-term finite-volume law, including the nonzero coefficient. The Airy equation supplies an unambiguous first positive root. The supplied verifier checks transition normalization, detailed balance, both spectral reductions and numerical constants; finite enumeration is not used as the proof of the asymptotic claim.

## Originality

**PASS within inspected literature, subject to independent priority review.** The closest source [1] establishes the unconstrained sluggish walk and its \(t^{1/3}\) scaling, but its inspected text does not treat finite symmetric reflecting boxes or spectral-gap corrections. The general HCTRW analysis [2] permits finite reflecting graphs and general spectral representations but does not already state the Airy spectral constant or its order-\(L^{-4}\) lattice correction. The later direct sluggish-walk successor [3] concerns unbounded arcsine path observables. Searches using aliases for reflecting birth–death chains, space-dependent diffusivity, weighted Sturm–Liouville eigenvalues and the numerical constant found no exact coverage in the accessible evidence. A more specialized, unlocated source or an implicit derivation from general theory remains possible.

## Scientific value

**PASS.** A finite trap is a natural regulator for the spatially increasing waiting times in [1]. The result gives the *exact leading finite-size relaxation scale and its first nonuniversal correction*, a physically measurable equilibration time beyond the unbounded spreading exponent. The correction separates the microscopic trap-weight offset from the reflecting boundary half-cell, permitting quantitative comparison between lattice and hydrodynamic descriptions. It is not a mere recomputation of the source's position density, nor a small unmotivated numerical slice.

## Scope and limitations

The result is for the finite, symmetric, rejected-outward-step confinement of the exact \(1/(|k|+2)\) model. Changed wall conventions and other power-law exponents are not covered. General finite-chain spectral machinery applies, so independent review should particularly investigate whether a previous paper has already performed this precise weighted Airy limit and first correction.

Self-review: passed. Independent audit: not yet performed.
