---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification

Run `python verify.py` from this package. No network access, randomness, nonstandard modules, or other package files are required. The verifier evaluates the five explicit affine forms on the unit square by exact rational convex-polygon clipping. It includes all half-unit strips meeting every current polygon and sums exact shoelace areas.

The first check reconstructs the mod-two coefficient residues, establishes that all ten distinct pairs of forms are linearly independent, and confirms that among the five four-subsets only the set of times \(\{0,1,3,4\}\) has zero total residue. Odd-moment vanishing also follows from the analytic inversion symmetry (proved in `RESULT.md`).

The second check groups 168 rational polygons into all 32 sign words and verifies each probability is \((1+\varepsilon_0\varepsilon_1\varepsilon_3\varepsilon_4/21)/32\). The third check independently computes the exceptional four-form correlation using 156 rational polygons and obtains exactly \(1/21\). Marginal checks prove all length-four consecutive word probabilities equal \(1/16\). Both exhaustive area totals equal one.

Observed execution: `VERIFY_OK` with counts `[2,4,16,56,168]` and `[2,4,44,156]`, two probability masses `11/336` and `5/168`, and exceptional moment `1/21`. This is an exact finite certificate for the specified integral, not an assertion that finite samples establish any infinite-time property. Infinite-time stationarity and local four-block invariance are supplied analytically by Haar preservation.

Limitations: there has been no external independent audit; other partitions and nonconsecutive time selections are not covered.
