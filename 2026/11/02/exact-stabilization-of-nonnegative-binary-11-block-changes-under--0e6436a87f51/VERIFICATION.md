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

# Verification evidence and limits

Execute `python3 check_11_block_law.py` with Python 3 and SymPy. The actual bundled checker was executed successfully: `VERIFY_OK`.

The script reconstructs the full eight-state transition matrices and exact infinite zero-suffix expectation. It checks all seven nonnegative generating polynomials through a twelfth shift, proves the characteristic and Cayley–Hamilton matrix identities, checks the exact proper rational increment, verifies the sharp seventh-shift transition, and compares the symbolic masses against direct finite binary enumerations at seven shift parameters. Rational polynomial divisions and matrix identities use exact arithmetic; no numerical approximation is required for the infinite theorem.

The direct enumerations are corroboration rather than extrapolation. They alone would not prove the uniform statement. The proof additionally uses the elementary approximation of the carry process by residue classes, with a geometric bound on the unresolved tail.

Independent validation and independent audit have not been performed.
