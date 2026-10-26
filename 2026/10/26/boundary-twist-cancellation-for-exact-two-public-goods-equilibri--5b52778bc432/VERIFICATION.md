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

Run `python3 verify_twist.py` using standard Python 3: the checker constructs each graph from its edges, independently tests every candidate profile against all local best responses, and compares exact producer-count dictionaries for each \(n=3,\ldots,9\). This checks 699008 labeled profiles over fourteen instances, and completes with `PASS`.

Run `python3 certify_transfer.py` with SymPy installed: the checker builds the sixteen-state transfer matrix, verifies row-swap commutation and invariant bases, verifies both symbolic characteristic polynomials, and checks symbolic trace formulas for lengths three through nine. It completes with two `PASS` lines.

The all-length proof follows from the transfer construction and **symbolically exact** characteristic factors stated in `RESULT.md`, combined with the formal-logarithm identity. The direct enumeration tests are finite and do not prove the theorem by themselves. No external or independent audit is claimed.
