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

# Verification methods and limits
The matrix normal form is derived from the Leibniz condition without computational assumptions. A separate exact finite-field script checks the rank of the full Leibniz equation matrix, verifies the closed counts, and samples the Leibniz identity directly. Run `python3 artifacts/verify.py` in a directory containing the embedded `artifacts` folder. Expected final line: `VERIFY_OK_FILIFORM_DERIVATIONS`.

Tested field orders: \(2,3,4,5\); the characteristic-two extension field uses \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\). Each rank count was exhaustively computed for each of those fields; the program does not enumerate all prime powers. It does not certify historical originality or provide independent audit.
