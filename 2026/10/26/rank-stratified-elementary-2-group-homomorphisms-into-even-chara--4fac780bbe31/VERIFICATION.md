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

To reproduce the finite experiments, run `python3 check.py`. The checker implements multiplication in \(\mathbb F_2\) and \(\mathbb F_4\), enumerates all square-one generator images and their commuting tuples, independently computes first-coordinate ranks by Gaussian elimination and compares each rank fiber with the closed counting formula. It passes \(14\) cases; its final line is `HEISENBERG_ELEMENTARY_2_HOMS_OK 14 cases`.

The infinite statement is proved algebraically in `RESULT.md`. Critical checks are: deriving square-one and commutation equations from the stated group law, identifying alternating product matrices supported on a rank-\(d\) image with alternating forms on its dual, checking each column-lift multiplicity \(q^{b-d}\), and counting surjective linear maps to the selected image. The limit fixes \(q,r\), and the proof does not certify other asymptotic regimes.

No external independent audit was performed. The embedded checker and written proof do not establish global literature priority. The single-involution case is known previously.
