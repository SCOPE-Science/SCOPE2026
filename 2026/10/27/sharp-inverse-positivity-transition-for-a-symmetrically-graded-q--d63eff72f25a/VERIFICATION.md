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

# Exact symbolic verification

Run `python verify_q2_threshold.py` using Python 3.10+ and SymPy 1.11+. The program constructs the 5-by-5 one-dimensional mass/stiffness matrices from the local Q2 Gauss–Lobatto rule, forms the two-dimensional 25-by-25 stiffness, verifies the four parity-block inverses symbolically, reduces 625 Green entries to 55 reflection-and-transposition classes, and checks the precise polynomial coefficient signs. The decisive root lies strictly in the rational interval \(41999/10000<t_*<21/5\). Every assertion is exact (integer and symbolic rational algebra). Numerical root approximation is not used by the certificate.

A successful replay prints: `PASS: 25-by-25 exact stiffness inverse, 55 symmetry classes`, followed by the counts 45/10 and the exact negative entry at \(t=5\). The proof requires Descartes' one-positive-root principle to turn the certified coefficients and endpoint signs into a global interval assertion; no finite test points are used in place of that argument. External independence and wider publication-priority verification have not been performed.
