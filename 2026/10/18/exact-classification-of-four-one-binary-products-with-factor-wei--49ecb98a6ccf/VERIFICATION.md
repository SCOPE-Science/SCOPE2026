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
# Verification record

The product identity and case distinctions in `RESULT.md` are a complete proof for all positive integer exponents satisfying the domain constraints. The `VERIFY.py` program computes independent integer products and their exact binary weights for every \(1\le u,v<w\le80\), without using the proof's symbolic carry cases.

Run `python3 VERIFY.py` with Python 3.10 or later. The program asserts the equivalence of the exact product weight and the five parameter families, verifies all lower-weight exceptions in the test grid, and prints a `VERIFIED` summary. No network resources or nonstandard dependencies are needed.

The finite grid is a consistency check, not an exhaustive infinite proof. Originality is assessed only against inspected sources, and no independent audit or external verification is claimed.
