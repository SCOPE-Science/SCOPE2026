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

Execute `python3 verify_double_sixes.py` in this directory. The verifier requires only Python 3's standard library. It constructs the 27 line classes in the standard blow-up basis, the 36 root-pair representatives, and all 36 double-six incidence columns by integer intersections.

The exact tests check all 36 column sums equal \(4(-K_S)\), each column has 12 entries, each row has 16 entries, and line-pair common-incidence counts are 8 (meeting) and 6 (skew). It verifies a primitive rank-six Picard quotient coordinate system and computes the rank of the reduced 21-by-36 matrix modulo 2 with bit elimination. Integer fraction-free elimination gives the displayed maximal-rank minor determinant \(-65536\). A primitive integer row covector evaluates to \(-4\) on all columns; this certifies order-four torsion modulo the full image. These facts together determine every nonzero Smith invariant factor without reliance on a numerical singular-value or floating-point calculation.

Expected final output line: `VERIFY_OK`.

The verification establishes the formal integral incidence statement from the standard cubic-surface configuration. It does not test arbitrary equations of cubic surfaces, their arithmetic descent, the literature's historical completeness, or any external independent audit.
