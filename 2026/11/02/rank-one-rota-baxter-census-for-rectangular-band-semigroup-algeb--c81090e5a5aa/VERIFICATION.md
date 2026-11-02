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

The file `verify_rectangular_band.py` is a standalone Python 3 standard-library program. It constructs products directly from the semigroup law, enumerates each nonzero rank-one endomorphism exactly once by normalizing its image line, and verifies the full weight-zero Rota–Baxter equation on each ordered pair of semigroup basis elements. It independently computes the square-zero versus non-square-zero image split and compares with the closed formula.

Seven exhaustive cases were executed: \((m,n,q)=(1,1,2),(1,2,3),(1,3,2),(2,2,2),(2,2,3),(2,2,4),(2,3,2)\). The final program line was `RECTANGULAR_BAND_RANK_ONE_RB_OK`. In particular, totals were \(0,8,21,35,164,471,429\), in that order. The nonprime field case uses its own addition/multiplication tables. No numerical enumeration was used as a substitute for the proof for all \(m,n,q\).

The argument is a finite-dimensional algebraic classification and contains no infinite computation. Restrictions: linear rank one, rectangular-band semigroup algebras, weight zero, finite fields, individually labeled maps. Historical publication priority and external independent correctness have not been certified.
