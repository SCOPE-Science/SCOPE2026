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

# Verification and limits

For the exact analytical claim, see the cyclotomic trace lemma and spectral-projection argument in `RESULT.md`. The all-size conclusion does not rely on finite enumeration. Run `python check.py` in a Python environment with NumPy, SymPy and SciPy. The checker constructs adjacency matrices directly, obtains an independent eigenvector projection for each \(2\le n\le30\), tests the exact polynomial gcd for \(2\le n\le60\), and compares numerical finite-loss evolution for five graph sizes. In total 93 checks passed during preparation. The test suite is a reproducibility aid, not independent scientific validation. There is no independent audit or external certification.
