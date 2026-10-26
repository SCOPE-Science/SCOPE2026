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

Run `python VERIFY.py` with NumPy and SciPy. The checker runs 50,000 deterministic-seed samples of the strict tanh angular inequality; 175 finite root searches across seven \((J,K)\) settings; and 7,000 long-time angular-speed comparisons. The actual run yielded all three PASS lines. Numerical sampling is not an exhaustive root search and does not prove infinite-time statements. Global conclusions are proved by the monotone inverse-tanh equilibrium argument, hyperbolic repulsion, Poincare--Bendixson and angular winding in RESULT.md. The equality regime \(K=J-1\) is included in the analytic equilibrium proof. No external independent audit was conducted.
