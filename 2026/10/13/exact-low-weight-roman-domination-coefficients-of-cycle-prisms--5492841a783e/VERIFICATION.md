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
# Verification of exact Roman-prism coefficient laws

Run `python3 verify.py` with Python 3 standard library; no external data or unbundled libraries are required.

The verifier constructs every one of the 81 two-column states and all 601 allowed triples, checks the nonnegative reduced exponents from the published potential table, and verifies the entire exact integer identity `B0^3 == B0^7`, not merely its trace. It checks the required base trace vectors `(0,4,0,0)` and `(5,6,4,2,4)` and the coefficient laws through order 100. It separately enumerates every vertex labeling on cycle prisms of sizes 3 through 6 using the graph adjacency condition, and independently enumerates valid cyclic column words. All corresponding Roman-domination polynomial coefficients agree.

Actual local execution outcome: `VERIFY_OK states=81 edges=601 potential_nonnegative=yes`; `VERIFY_OK matrix_identity=B0^3=B0^7 zero_traces_3..6= [0, 4, 0, 0]`; `VERIFY_OK first_ratios_3..7= [5, 6, 4, 2, 4]`; `VERIFY_OK independent_full_polynomial_bruteforce_n=3..6 assignments= 597780`; `VERIFY_OK coefficient_laws_n=3..100 exact_identity_used=yes`.

The finite enumeration and bounded coefficient checks are not infinite proofs. The all-order assertion is obtained from the exact finite matrix identity and the transfer-matrix and potential telescoping arguments written in `RESULT.md`. The checks do not establish priority or independent certification.
