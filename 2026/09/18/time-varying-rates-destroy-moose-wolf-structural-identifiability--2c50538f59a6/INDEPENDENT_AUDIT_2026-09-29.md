# Independent audit — Exact gauge family defeats structural identifiability in the time-varying Moose–Wolf models

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/time-varying-rates-destroy-moose-wolf-structural-identifiability--2c50538f59a6`  
**Audited tree:** `d3a13ea0cfa47c906901ca7c24075c564d0b1db7`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The non-identifiability claim follows exactly by algebraic elimination. After dividing the two ODEs by the positive observed states, the two unknown time-dependent rates can be solved pointwise for any positive choice of the three constant interaction parameters. Substitution reproduces the prescribed trajectory identically in both the Holling-II and ratio-dependent models. On compact positive trajectories the reconstructed death rate can be kept positive by increasing C; when x<1 the reconstructed growth rate can likewise be kept positive by increasing A, and local admissibility is stable around interior positive solutions. The source paper itself explicitly says its structural-identifiability calculation assumes α*(τ)=α0 and δ*(τ)=δ0 are scalar parameters, so that calculation does not establish identifiability of the non-autonomous model with free functions.

## Originality

**PASS.** General structural-identifiability theory for time-varying parameters and unknown inputs is established prior work and is excluded from the novelty claim. The source-specific contribution is the explicit three-constant gauge for both Moose–Wolf equations and the direct diagnosis of the frozen-parameter inference. Searches using the exact arXiv identifier, model title, identifiability/non-identifiability, gauge/symmetry, and both functional-response names did not locate an earlier source-specific correction. Recency is the main residual risk because the source preprint was posted one day before the SCOPE record.

## Scientific Value

**PASS.** The gauge invalidates unique ecological-parameter recovery at the ODE-model level even with perfect continuous observation of both populations, and it identifies what kind of extra structure is needed to restore identifiability. This directly affects interpretation of inverse-model parameter estimates while carefully leaving trajectory prediction and architecture-restricted identifiability outside scope.

## Independent checks

- Solved the Holling equations pointwise for α(t) and δ(t) after dividing by x and y; substitution cancels exactly for arbitrary positive constants A,B,C.
- Repeated the derivation with denominator By+x for the ratio-dependent model; the same three-constant freedom remains.
- Checked positivity logic on compact positive trajectories: x/(B+x) and x/(By+x) have positive minima, so sufficiently large C makes δ positive; for x<1 sufficiently large A makes α positive.
- Read arXiv:2609.20793v1 open-access HTML: the paper explicitly states that its structural identifiability analysis assumes α*(τ)=α0 and δ*(τ)=δ0 are scalar rather than time-dependent functions and reports global identifiability for that frozen surrogate.
- Verified that the record does not overclaim architecture-restricted non-identifiability: a finite neural-network rate class is explicitly left for separate analysis.

## Literature and prior-art boundary

- https://arxiv.org/html/2609.20793v1 — Singh and Kumari (2026), source paper; Section 3.3 explicitly freezes the two time-varying rates to scalars for its structural-identifiability calculation.
- https://arxiv.org/abs/2211.13507 — Martinelli, general analytical identifiability framework for nonlinear ODEs with time-varying parameters/unknown inputs.
- https://arxiv.org/abs/2407.02771 — Conrad and Eisenberg, prior work on the effect of forcing-function assumptions on structural identifiability.

## Limitations

- The result treats α(t) and δ(t) as free functions in the differential-equation model; a fixed finite neural-network architecture can impose additional restrictions and requires its own identifiability analysis.
- The displayed formulas require x,y>0 and x^4≠1; carrying-capacity contact needs a separate compatibility analysis.
- The result does not address finite-sample uncertainty, optimization, forecasting skill, or biological plausibility of every gauge-equivalent rate pair.

## Repository identity

The assigned source-tree SHA `d3a13ea0cfa47c906901ca7c24075c564d0b1db7` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
