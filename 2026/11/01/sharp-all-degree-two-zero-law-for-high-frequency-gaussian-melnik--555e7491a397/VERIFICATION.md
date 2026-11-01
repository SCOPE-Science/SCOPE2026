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

# Reproduction and verification

Run `python3 verification.py` with Python 3. No extra dependencies are required.

The checker numerically re-evaluates the exact \(N=1\) Rayleigh integral for six frequencies and confirms agreement with \(t/\sqrt{1+t^2}\) within an explicit quadrature tolerance. It separately checks the infinite sums \(\sum_{k\ge2}kq^k\) and \(\sum_{k\ge2}(k^2+k^3)q^k\) against their rational closed forms, and examines the predicted high-frequency leading coefficient. The included script completed successfully in the recorded verification.

The infinite-degree bounds, two-critical-point argument, Gaussian independence, and all-frequency probability inequalities are justified analytically in `RESULT.md`. Finite quadratures and truncated power series are diagnostic checks only; they are not substituted for proofs. No exact probability for the perturbed finite-amplitude system is asserted, and no independent validation was performed.
