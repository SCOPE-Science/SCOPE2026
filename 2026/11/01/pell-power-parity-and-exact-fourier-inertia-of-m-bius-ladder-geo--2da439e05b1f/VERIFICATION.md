---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and proof checkpoints

Run `python check_mobius.py` with Python 3 and the script's NumPy and SymPy dependencies. The determinant check constructs the graph from its generators, computes shortest-path distances by breadth-first search, and compares exact integer determinants with the signed formulas for \(3\le n\le16\). At \(n=3,4,5,6\) the determinants are \(112,-99,-4352,-1127\), respectively. The script also tests the Pell–Lucas trigonometric product through \(m=79\) and includes checks of the individual Fourier eigenvalues and their signs; those spectral checks concern inputs to the determinant computation, not an additional finding.

These finite computations do not prove the infinite family. In `RESULT.md`, the critical product steps are that the odd-sine product controls both frequency parities when \(n\) is odd, and that for even \(n\) the odd frequencies cancel in reciprocal pairs while the remaining product is a Chebyshev quotient with a half-Pell–Lucas square value.
