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

Run the included `verify_subregular_unit_centralizers.py` with Python 3. The program uses no third-party packages and enumerates every unit and every commuting unit partner for \((q,m)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)\). The \(q=4\) test uses \(\mathbb F_2[z]/(z^2+z+1)\). It compares literal \((m+1)\)-dimensional matrix commutation to the compact three-coordinate criterion for \((2,2)\), \((2,3)\) and \((3,2)\), tests all three predicted strata and centralizer sizes, and checks every numerical conjugacy-class and commuting-pair identity.

The completed replay printed `VERIFY_OK_SUBREGULAR_UNIT_CENTRALIZERS`; for \((q,m)=(2,2)\) it found 8 units, 5 classes, 40 commuting pairs; for \((3,2)\), 108 units, 20 classes, 2160 commuting pairs; and for \((4,2)\), 576 units, 51 classes, 29376 commuting pairs. Other checked cases also passed. The proof in RESULT.md is symbolic and covers all \(m\ge2\) and all prime powers; these bounded computations support, but do not imply, the general statement.
