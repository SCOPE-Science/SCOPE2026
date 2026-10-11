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

# Reproducibility and limits

Execute `python3 CHECK.py` after extracting the provided files to one directory; the checker requires only Python 3 and the standard-library `fractions` module. It implements rational polynomial reduction modulo the cubic relation \(t^3=t^2+2\), verifies four defining-polynomial evaluations, verifies four consecutive conjugate-map transitions, and checks that all four states have distinct third coordinates. A successful run prints `CHECK_OK exact polynomial ring, four distinct states, four transitions`.

The universal affine exclusion is proved directly in the mathematical proof by exact identities; the finite computational check neither replaces that proof nor establishes global completeness for quadratic polynomials. The Jacobian nilpotence and conjugacy follow from displayed explicit symbolic identities valid for every polynomial \(P\), not from numerical experiments. The statements concern iteration and least period; no independent audit or external certification is claimed.
