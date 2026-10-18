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

The exact argument uses Bézout, the elliptic chord--tangent law, and group totals; the existence of near transversals follows from Goddyn--Halasz, Theorem 2. The classification of full group transversals follows from their Theorem 4. Cichacz's zero-sum partition theorem independently covers the zero-defect cases and is prior, not novel evidence.

Run `python3 verify.py` using Python's standard library. The script checks cyclic group triple witnesses for \(1\le m\le200\) and four smooth short Weierstrass models with \(N\in\{6,12,18,24\}\) and unique rational involution, then verifies actual projective collinearity determinants. It also finds four disjoint zero-sum triples on the smooth cubic \(y^2=x^3+1\) over \(\mathbb F_7\), with four rational two-torsion points. Such finite checks do not establish the infinite existence theorem or literature uniqueness. They are reproducibility evidence only.
