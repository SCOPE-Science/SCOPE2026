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

# Exact finite verification

Run `python3 verify.py` with Python 3.9 or later, without external dependencies. The input is the deterministic rule assigning each cell \((r,c)\) symbol \(r+c\pmod6\); all 36 cells and the matching order are specified in the code and in the proof. The checker verifies all 3108 nonempty simplices, the five nonzero face counts, 1500 matched pairs, all 10656 oriented Hasse incidences, a full acyclic topological sort, the signed critical Morse boundary with 327 nonzero coefficients of magnitude at most 3, and the exact integral Smith diagonal with nine unit entries. Its expected ending is `VERIFY_OK ... betti2 14 betti3 75`.

No float arithmetic, randomized search, remote certificate, or previously stored log is used. The finite computation is complete for precisely the cyclic order-six object. The degree matrix and connectivity assumptions required to promote its homology to the homotopy type are proved in `RESULT.md`. This is a self-review, not independent validation.
