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
# Verification

The proof is symbolic for every odd prime power. The bundled `verify.py` is a corroborative finite check: for each odd prime \(q\le101\), it chooses a quadratic nonresidue \(d\), realizes the anisotropic norm conic as \(x^2-dy^2=1\), and checks:

1. the conic has exactly \(q+1\) points;
2. the zero pair-sum has multiplicity \(q+1\), while every nonzero pair-sum has multiplicity at most two;
3. the exact constant-function collision energy is \(3q(q+1)\), matching the sharp formula.

Run with `python3 verify.py`. Finite testing is not used to justify prime-power generality or uniqueness of extremizers; those follow from the proof in `RESULT.md`.
