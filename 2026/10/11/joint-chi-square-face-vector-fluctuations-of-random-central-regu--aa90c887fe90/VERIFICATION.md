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

# Verification of finite and limiting claims

The included `verify.py` uses deterministic-seed Gaussian samples and NumPy/SciPy. Install its listed numerical dependencies with `python -m pip install -r requirements.txt`, then run `python verify.py`; successful execution prints `VERIFY_OK`. The checks include vertex-by-vertex edge-section construction, convex-hull comparison for 125 actual sections, Euler face relations, finite-dimensional mean calibration at 3 dimensions and 65,000 simulations each, and leading-order fixed-face-rank profile tests.

The proof in `RESULT.md` establishes the generic-sign face bijection, Gaussian realization, random-threshold central limit lemma, second-order binomial expansion, DKW uniform integrability, and exact pair-quadrant mean; the script is a supplement, not a certificate of results for all dimensions. The script does not exhaust all possible sign patterns or sample directions. The fixed-rank joint limit and its asymptotic covariance concern \(N\to\infty\), and no independently performed audit is asserted.
