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
The argument is fully analytical and reduces global extremality to the single strict crossing of two positive integral kernels. In particular, the sign argument uses ordered supports, not finite root scans. The independent-audit field states only that no independent audit has been performed.

## Reproducibility
Run `python3 CHECK.py` with Python 3 standard library. Expected output:

`VERIFY_OK roots=5 critical_moments=20 isotropic_checks=3 closed_example=1`

The checker uses deterministic composite Simpson quadrature. It tests the values of five optimizers, local directions of extremality, volume-based invariance at the critical moment for four dimension pairs and five aspect ratios, the isotropic second-moment formula for three dimension pairs, and one elementary closed-form first moment.

## Limits of numerical checks
Numerical quadrature has floating-point and discretization error and verifies only sampled inputs. The uniqueness claim, general moment ranges, endpoint crossings, and exact special formulas are established in the proof. The numeric values reported to 12 significant digits are reproducibility benchmarks rather than independent scientific certification.
