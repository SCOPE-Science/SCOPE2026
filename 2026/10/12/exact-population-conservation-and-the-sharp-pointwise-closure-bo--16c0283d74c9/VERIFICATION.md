---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Summing the precisely stated Neumann spatial SIR equations after τS=τI=τR=1 cancels infection/recovery terms, yielding n_t=DSΔS+DIΔI+DRΔR (+χ∇·(S∇log I)); Neumann fluxes imply ∫n conserved, while ∫S falls by ∫βSI/N when β,N>0. For every smooth positive initial triple with n=N0, pairwise cosine zero-sum perturbations force equal compartment diffusivities. In chemotaxis, fixing I constant first forces DS=DR; at cosine midpoint for I=1+εcos(kx), ∂²_x log I=−ε²k² while ΔI=0, so χ must vanish; equal diffusions and χ=0 suffice by Neumann heat uniqueness. Independent symbolic midpoint evaluation and perturbation checks matched. No claim about special pointwise-constant solutions when iff universal criterion fails.

## originality

PASS

For the precise 2026 chemotactic diffusive SIR PDE, standard integrated conservation is not newly claimed. The source-specific conjunction of correction to mislabeled susceptible mass and a universal necessary-and-sufficient pointwise constant-population closure criterion is distinct from the inspected generic global-mass and equal-diffusion accounts. The primary preprint full text was not freshly retrievable; only abstract, actual package PDE reproduction and prior citations inspected. Qualified best-of-knowledge conclusion with explicit limitation.

## value

PASS

Numerical spatial SIR population diagnostics often confuse the integrated compartment sum with susceptible mass or pointwise constant N. A sharp all-smooth-data coefficient criterion, including chemotactic obstruction, supplies an actionable structural boundary and counterexamples for interpreting such models. Conservation identity alone is textbook, but universal necessity and source-specific mismatch provide value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
