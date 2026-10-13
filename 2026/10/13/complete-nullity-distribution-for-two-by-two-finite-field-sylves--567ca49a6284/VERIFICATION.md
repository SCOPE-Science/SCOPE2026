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

Run `python3 verify.py` from the directory containing that standalone file. The standard-library-only program enumerates all ordered pairs of \(2\times2\) matrices, constructs the corresponding \(4\times4\) Sylvester operator, computes its finite-field rank, and compares the four resulting nullity counts with the displayed polynomials.

The checker exhaustively covers \(q=2,3,4,5\), including the extension field \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\). The expected four strata \((N_0,N_1,N_2,N_4)\) are \((88,72,94,2)\), \((3618,2016,924,3)\), \((43968,16800,4764,4)\), and \((290500,82800,17320,5)\). The execution success token is `VERIFY_OK`. The checker performs exhaustive **finite** tests, not a proof for all prime powers; the all-field proof is the module-Hom and similarity-class argument in `RESULT.md`. The software requires no external package or online service.

Independent audit: not performed.
