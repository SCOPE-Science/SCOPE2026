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

Run `python verify.py` with Python 3, `networkx` and `sympy`. The program independently builds two exact moment polynomials from root-to-vertex path sets for each tree root, then checks both asymptotic coefficients and the exact three-vertex threshold identity. It is expected to print a single `PASS` line. The proof of arbitrary tree size is combinatorial and analytical in `RESULT.md`; the verifier is restricted to trees with three through nine vertices and must not be interpreted as infinite computation. Bibliographic originality has not been independently certified; selected historical primary full-text sections were inaccessible.
