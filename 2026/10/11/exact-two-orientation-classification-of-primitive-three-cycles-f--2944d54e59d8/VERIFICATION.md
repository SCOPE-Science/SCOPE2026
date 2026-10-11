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
The independently readable `verify.py` program uses Python 3 and only `fractions.Fraction`. Invoke it with `python3 verify.py`. It reproduces `CHECK_OK exact rational triangles: 1184 counts [1138, 18, 28]`, comparing rational closed-form candidate coordinates, actual orthogonal-projection selections on every step, the two strict inequality triples, and least-period checks. The scanned exact grid uses \(u=n/8\) for integers \(-12\le n\le24\) and \(v=m/8\) for \(1\le m\le32\). These experiments do not prove the theorem outside the finite grid; the mathematical proof rests on exhaustion of two cyclic line itineraries, affine contraction uniqueness, and exact symbolic distance formulas. Equality boundaries obey the tie-as-fixed definition and are excluded. No independent human audit or external validation has been performed.
