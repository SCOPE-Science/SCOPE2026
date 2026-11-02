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

# Verification and reproducibility

Run `python3 verify_two_pendants.py`. It compares an independently assembled full Laplacian and Poisson-uniformized heat column difference against the analytic four-mode formula, checks the bridge-plus-clique primal cost, and confirms the proposed Kantorovich potential. Integral extreme dual potentials are also enumerated for smaller cliques.

Observed:

```text
CHECK_OK separate_Laplacian_uniformization_and_transport=21 exact_dual_cases=15
CHECK_OK unique_dual_witness=verified extrema sampled, onset=p_minus_3, large_clique_limit=2
```

The finite numerical program is not an exhaustive all-size certificate; the full theorem relies on the explicit Metzler positivity proof, transport primal/dual equality, two-sector ODE calculation and the asymptotic limits in RESULT.md. The uniqueness proof is analytic, not established by the finite enumerator. Independent audit has not been performed.
