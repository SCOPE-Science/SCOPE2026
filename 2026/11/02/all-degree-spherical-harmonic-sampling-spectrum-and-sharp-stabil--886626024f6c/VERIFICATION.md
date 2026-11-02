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

# Verification record

The exact certificate `check_e6.py` reconstructs 36 representatives of the 72-root configuration with integer coordinates and no external packages, verifies all 36-by-36 signed and unsigned adjacency identities, checks Gegenbauer recurrence values and the spectral rank and condition-number conclusions in forty initial degrees using fractions. The infinite extension is a written algebraic argument: explicit residue-class formulas for the Gegenbauer values and strict rational inequalities for odd degrees at least five and even degrees at least ten. The global condition-number bound uses separate decreasing tail comparisons starting at odd degree seven and even degree twelve.

A second numerical linear-algebra calculation checked the eigenvalue multiplicities of the 36-by-36 signed and unsigned adjacency matrices. This is a computational cross-check, not external validation. A reader can verify the full finite certificate by executing `python3 check_e6.py`; the proof does not infer an infinite statement from forty computed cases. No external mathematical audit or independent validation has been performed.
