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

The general theorem is proved symbolically in `RESULT.md`; the executable check is supplementary.

`verify.py` exhaustively enumerates all order-preserving maps for \((m,n)=(2,3),(3,2),(3,3),(4,2),(4,3)\). It computes winding degree from lifted increments, connects maps by valid single-coordinate comparable changes, and verifies the theorem's component count and isolated extremal components.

Expected totals are \(48/1\), \(200/3\), \(234/7\), \(1156/7\), and \(1248/3\), where each pair is maps/components in the order listed above. These checks include shorter-to-longer, unequal-size, diagonal, divisibility, nondivisibility, and higher-degree cases. They do not certify the infinite parameter family.
