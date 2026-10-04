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
# Verification

The proof is analytic. The accompanying script is an exact-rational replay of
the lattice formulas and finite examples.

For each tested threshold \(a\), the script checks the breakpoint, the maximum
of \(T_k/V_k\), the exact consecutive-slope identity, strict slope decrease,
the location of every sampled hull point, exact attainment by rational
two-uniform mixtures, and many random finite mixtures.

The script does not infer the universal theorem from enumeration. The theorem
follows from the mixture representation and symbolic hull calculation.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK ratio_checks=37350 slope_checks=34949 point_checks=42400 construction_checks=19500 random_mixture_checks=3200`.
