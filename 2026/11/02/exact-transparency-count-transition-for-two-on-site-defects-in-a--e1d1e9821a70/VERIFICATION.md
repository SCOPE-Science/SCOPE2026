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

# Verification instructions and limits

Run `python3 checker.py` with a standard Python 3 interpreter. The checker independently computes finite-chain transfer matrices of the full two-defect scattering problem, and compares reflected amplitudes at analytically predicted transparent wave numbers. It also counts roots of the equal-sign phase equation for integer distances \(1\le L\le17\), checks unequal magnitudes, and tests the square-root band-edge scaling.

Observed checker result: `PASS: 2714 direct checks; maximum reflection amplitude at predicted transparent points 5.32e-13.` The complete assertion for arbitrary \(L\), real potentials and all propagating energies is analytic, as proved in RESULT.md, and is **not** inferred from sampled parameter values.

The present verification is not an independent audit of correctness or historical priority. One directly relevant 1996 journal article is accessible only through its abstract, and its possible exact coverage remains unresolved. The analytic theorem does not apply at nonpropagating band edges or to complex/on-bond/long-range defects.
