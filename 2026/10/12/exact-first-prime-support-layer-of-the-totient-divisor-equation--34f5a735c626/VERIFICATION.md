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

# Verification of the first-support classification

Execute `python3 verify.py` with the Python 3 standard library. Its output is recorded in `verification_output.txt`; both are included with the proof. The script checks all \(72\) exponent-and-prime candidates inside the *proved* bounds using two independently evaluated integer equations; it also verifies every rational comparison and performs the supplemental direct regression for \(1\le m\le50000\).

The unbounded part is established mathematically, not numerically: odd \(m\) are excluded; even \(m\) with fewer than four primes are excluded by \(\varphi(4m)>m\); four-support candidates have prime support \(\{2,3,5,r\}\), where \(r\in\{7,11,13\}\); the final prime appears to exponent one; and the other exponents are bounded by \(a\le4,b\le3,c\le2\). This implies that the seventy-two-case verification is exhaustive for **all** integers under consideration. The separate regression through \(50000\) serves only to detect implementation errors.

Independence status is not performed; no external mathematical validation is claimed.
