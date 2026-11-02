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

`verify.py` is the standalone reproducibility program. Run `python3 verify.py` using Python 3.9 or newer (standard library only). The program implements matrix multiplication, constructs the full linear commutator map for each tested element, performs finite-field Gaussian elimination, independently counts graph components, and compares both. For the small exhaustive cases, it independently enumerates every commuting partner. It also enumerates diagonal occupancy profiles to verify exact first two moments.

Observed output included `EXHAUSTIVE 2 1 elements 8`, `EXHAUSTIVE 2 2 elements 256`, `EXHAUSTIVE 3 1 elements 27`, sampled tests at \((q,n)=(2,3),(3,2),(5,2)\), exact occupancy checks for \(q=2,3,5\) through \(n=4\), and `VERIFY_OK 291 exhaustive elements`.

The code uses modular arithmetic for the tested **prime fields** only. The mathematical proof is valid for arbitrary prime-power field orders and does not rely on these tests. No finite test is used as evidence for the asymptotic convergence. The graph-connectivity bound, the multinomial central limit theorem, and the Gaussian-product calculation are verified analytically in `RESULT.md`.
