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

# Reproducibility checks

The accompanying self-contained program `check_septic.py` uses only the Python standard library and can be run with `python3 check_septic.py`. A successful run prints `"status": "VERIFY_OK"`.

The program independently calculates the six-direction triangular-lattice return-walk number for \(3\le N\le12\) using a dynamic program, evaluates the exact Franel-binomial finite sum, and compares the two for every tested \(N\). For \(3\le N\le7\), a separate multinomial-histogram sum independently counts root-of-unity zero-sum tuples. Normalized sample-node Hessians are checked with direct determinant expansion in \(\mathbb Z[\zeta]\) for \(N=5,6,7\). It also checks the rational-point formula against independent sign enumeration for \(N\le8\), and confirms the predicted residual quadratic-point count is integral through \(N=12\); the Galois pairing itself is proved symbolically.

These computations do not enumerate every singular point or every Hessian in arbitrary dimension. The proof in `RESULT.md` supplies the all-dimensional classification and all arithmetic quantifiers. No independent audit or external certification has been performed.
