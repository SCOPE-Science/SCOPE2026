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

# Reproducibility and verification

The reproducibility program `verify.py` uses only Python 3 and SymPy. Run `python verify.py`; it tests each intended degree/signature witness in degrees 2 through 18 by exact Sturm root counting and verifies the Eisenstein reciprocal coefficient pattern. It additionally tests distinct-root counts in low coprime exponent pairs for rational values on either side of zero.

The general proof is the exact Bézout field identity, an exhaustive real monotonicity classification of a rational trinomial, Eisenstein irreducibility at 3, and explicit rational sign brackets. Finite tests do not prove a universal statement, and there is no external or independent verification. Originality comparisons are based on material actually read and reported in `AUDIT.json`.
