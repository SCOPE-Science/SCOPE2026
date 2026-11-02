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

# Verification of the geometric reserve theorem

Run `python3 verify_reserve.py` with Python 3 (standard library only). A reproduced execution is stored in `verification_output.txt` and reports `CHECKS_OK 1761`.

The script checks the exact finite count \(Z_N(K,d)\) against independent exhaustive integer-state enumeration; checks inverse directed-edge detailed balance for the two-level positive/nonpositive transfer rule using exact rational arithmetic; checks the closed radical normalization and positive/negative mean constraints for five parameter pairs; and compares exact finite stationary reserve distributions for \(N=50,100,300\) and rate ratios \(p/q\in\{1,1/2,1/4\}\) with the geometric limits. A separate edge-reversibility check covers equal-rate transitions.

The theoretical proof uses a full-span bivariate lattice local central limit theorem for the tilted variable \((Y,(-Y)_+)\). Its support contains \((0,0),(1,0),(-1,1)\), so the lattice period is one and the covariance is nondegenerate. The parameters stay in a compact part of \((0,1)^2\), providing uniform exponential moments and a uniform characteristic-function gap away from the origin. This yields the local asymptotic and the needed global \(O(N^{-1})\) point-mass bound. No numerical experiment is asserted to prove the infinite convergence; no second-order asymptotic or mixing-time claim is made.

Independent audit has not been performed.
