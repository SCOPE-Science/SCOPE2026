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

The exact-arithmetic checker `CHECK.py` was executed with Python 3 and SymPy. It certified all six vertices at each of two heights by symbolic affine inequalities valid for all integers \(m\ge3\). For every intersection that is not a vertex it found an inequality violated strictly throughout the same parameter half-line. It checked all \(15\) vertex-pair squared distances for each polygon using nonnegative rational coefficients after the substitution \(u=m-3\), as well as the exact diametral witnesses and asymptotic limiting gap.

The source's complementary-section Ehrhart theorem was inspected in the public 2022 preprint. No finite experiment is used in place of the symbolic universal proof. No independent audit or external formal proof was performed. Possible equivalent unindexed literature remains a bibliographic limitation.
