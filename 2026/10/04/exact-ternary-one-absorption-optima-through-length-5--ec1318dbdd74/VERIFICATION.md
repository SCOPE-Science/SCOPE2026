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
The verifier reconstructs the single-absorption channel directly: each adjacent pair is replaced by its saturated sum in the ternary alphabet, and deletion of the final symbol is included. It checks the explicit optimal-code witnesses in `optimal_codes.json` by direct ball intersection.

It then solves two separately generated exact binary optimization models for every blocklength from 2 through 5. Model A is set packing over received words; Model B is maximum independent set on the conflict graph. In the replay used for this package both models returned 3, 6, 13, and 29 with zero MIP gap, and the script printed `VERIFY_OK`.

The computation is finite and exhaustive at the model level. It does not certify any value for larger blocklengths. The optimizer is SciPy 1.17.0 with the bundled HiGHS backend; no proof-assistant or independently audited certificate is claimed.
