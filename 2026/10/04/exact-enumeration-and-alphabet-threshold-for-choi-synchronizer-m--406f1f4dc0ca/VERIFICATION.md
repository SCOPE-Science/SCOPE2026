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

The proof was checked symbolically at the orbit level. For an orbit \((a_0+i,b_0+i)\), writing \(\psi(a_0+i,b_0+i)=z_i+i\) was verified to transform the two coordinate-avoidance inequalities into \(z_i\notin\{a_0,b_0\}\) and the translation inequality into \(z_{i+1}\ne z_i\). The orbit sizes and orbit counts were recomputed from the additive order \(p\) of \(1\).

The accompanying `verify_psi.py` independently constructs examples in additive coordinate models for \(q\in\{4,5,8,9,25\}\), checks every ordered pair against all three inequalities, confirms \(N(4)=2304\) from the closed formula, and exhaustively checks that no map exists for \(q=2\) or \(q=3\). The program prints `VERIFY_OK` on success.

The finite computations do not establish the general theorem; the infinite family is justified by the orbit-coloring proof. The verification also does not test the later DNA-specific encoding/decoding algorithms.
