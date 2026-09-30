# Independent audit — 2026-09-29

**Record:** `2026/09/17/all-rate-growth-weighted-mutation-chemostat--23a37c2c63fd`  
**Audited source tree:** `b9d6556a9fc4514b33ca0597e81881a04f91dc3b`  
**Repository:** `SCOPE-Science/SCOPE2026` at checked commit `253a0fe5d0217455660a277f9adb940030e567ad`  
**Overall independent-audit verdict:** **PASS**

## Correctness — PASS

The reversible symmetrization is consistent with the stated column convention.  The generalized Rayleigh quotient is valid for every positive mutation intensity even when I+epsilon A is indefinite, because the top quotient is positive (test vector sqrt(pi)); strict decrease of D(s)^{-1} therefore gives strict substrate monotonicity.  Perron-Frobenius then gives the claimed equilibrium threshold.  At the critical dilution, V=p^T x is nonincreasing; states with s=s_in and x nonzero immediately leave the zero-derivative set through the substrate equation, while the stated biomass-substrate estimate gives boundedness, so LaSalle yields attraction and the separate q=s_in-s estimate gives Lyapunov stability.  The mutation-intensity derivative is nonpositive and can vanish only on ker A; the generalized eigen-equation then forces equal endpoint growth rates, and the large-epsilon limit is the stated pi-weighted harmonic mean.

## Originality — PASS

The motivating Alvarez-Latuz--Bayen--Coville preprint explicitly treats the growth-weighted cyclic example with a sufficient epsilon<=1/2 condition and reports larger-epsilon substrate monotonicity numerically rather than proving it.  Altenberg supplies the broad reduction phenomenon for conservative mixing but not the all-rate substrate monotonicity/equilibrium/critical-washout package proved here.  No covering theorem was located in the searched sources.  The historical Lobry Section 4.2 and the final HAL/journal text were not available in full through the inspected route, so priority is qualified rather than absolute.

## Scientific value — PASS

The theorem removes the small-rate restriction in the motivating substrate-dependent example, extends the mechanism to arbitrary finite irreducible reversible mutation networks, and sharpens the washout statement at the exact threshold.  It also cleanly leaves coexistence stability outside its scope.

## Sources used in the independent comparison

- https://arxiv.org/abs/2501.08011 — Motivating chemostat preprint; Section 4.2 uses growth-weighted cyclic mutation and leaves the larger-rate monotonicity as numerical evidence beyond its sufficient small-rate condition.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3309728/ — Altenberg reduction phenomenon; supports the mixing-direction context but does not supply the full theorem audited here.
- https://arxiv.org/abs/2110.09582 — Related constant-mutation chemostat model, materially different from the substrate-dependent growth-weighted setting.

## Limitations and residual uncertainty

- The audit did not read Lobry, La compétition dans le chémostat (2013), Section 4.2, or the final HAL v2 full text; these remain residual priority risks.
- The theorem itself is restricted to reversible growth-weighted mutation and does not establish arbitrary-rate stability of the coexistence equilibrium.

This independent audit is scoped to correctness, originality, and scientific value.  Repository material was used as evidence only; no GitHub modification was made during the audit.
