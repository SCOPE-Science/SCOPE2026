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

# Reproduction and limits

Install a Python 3 environment satisfying `requirements.txt`, then run `python verify.py` from the package directory. It prints `VERIFY_OK` after exact identities in \(\mathbb F_3[x,y,z,w,t]\), a complete four-point projective \(\mathbb F_3\) enumeration, verification of the characteristic-three local completed-square formula, and the integer Smith form for the five-by-five reduced \(K_{2,4}\) Laplacian.

The program uses exact arithmetic and reproduces the computation needed for the rank/Smith certificate. Flatness, weighted-projective vertex avoidance, the stability criterion, algebraic closure of the conics, Néron graph theory, and Galois descent of the torus require the mathematical proof in `RESULT.md`, rather than machine output alone. Symbolic identities do not independently establish historical originality.
