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

The mathematical proof in `RESULT.md` is the infinite certificate. The standalone stdlib `verify.py` is a finite cross-check.

Run `python3 verify.py` in the directory containing this file. A successful execution prints `VERIFY_OK`. The script forms the binary prefix of length \(2^{15}\), independently extracts observed factor sets for lengths through \(40\), compares their minimal absent words to the explicit families, enumerates every binary test word through length \(12\), and cross-checks the generating-series coefficients. It neither assumes a finite prefix captures every factor at all lengths nor promotes enumeration to proof of the infinite statement.

Independent scientific audit has not been performed.
