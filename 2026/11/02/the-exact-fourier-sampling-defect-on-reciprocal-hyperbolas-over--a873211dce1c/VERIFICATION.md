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

## Checks and limitations
The proof's coefficient-field step uses the elementary fact that \(\mathbb Q(\zeta_p)\) and \(\mathbb Q(\zeta_{p-1})\) are linearly disjoint. The fiber step checks all \(p\) phases and proves a complete if-and-only-if using the involution \(u\mapsto(b/a)u^{-1}\). The character computation establishes the precise kernel direction. Cases \(a=b=0\), exactly one zero parameter, square/non-square ratio, and \(p=3\) are explicit.

Run `python verify_kloosterman.py` with NumPy installed. It performs 178 direct numerical rank tests at ten odd primes, including all degenerate parameter types. Floating point singular-value thresholds are not exact certificates. No external or independent audit has been performed.
