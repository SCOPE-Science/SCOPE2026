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

# Reproduction of checks

Use a standard Python 3 interpreter: `python3 check.py`. No third-party modules or external data are needed. The script compares the coordinate-support/inclusion-exclusion expression with the independently simplified closed polynomial for each integer \(5\le n\le15\) and checks its Euler specialization. It then enumerates all projective \(\mathbb F_7\)-points with normalized leading nonzero coordinate, reproducing \(365\) points for \(n=5\) and \(3102\) points for \(n=6\). The latter count is smaller by \(2\cdot7^2\) than the algebraically closed polynomial evaluated at seven because the relevant finite-field quadric is nonsplit. These are exact finite checks, not a replacement for the arbitrary-\(n\) proof.

The mathematical proof is in `RESULT.md`, and the checker is entirely self-contained. The proof assumes an algebraically closed characteristic-zero field, particularly for nonsingularity of the quadratic form and its split-cell decomposition. No independent external audit has occurred.
