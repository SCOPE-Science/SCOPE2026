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
The attached `verify.py` independently checks every squarefree integer with exactly four distinct primes and \(2\le n\le1{,}000{,}000\), computes \(\sigma(n)\) and \(\varphi(n)\) exactly, and checks that the only hits are \(10659\), \(12441\), and \(24969\). It also replays the complete positive-divisor branches of
\[
(r-17)(s-17)=288,\qquad (r-9)(s-9)=80.
\]
Finite checks corroborate, but do not prove, all-height uniqueness; the unrestricted proof is in `RESULT.md`.
