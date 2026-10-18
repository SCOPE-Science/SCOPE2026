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

The accompanying `verify.py` was executed with Python 3 and reported `VERIFY_OK: 1566 exact rational formula/order/orbit checks`. The script constructs the full integer Laplacian of \(K_1\vee(rK_m)\), adds the two diagonal pinning gains over the rational numbers, inverts by exact Gauss--Jordan elimination, and compares every tested inverse trace with the stated closed forms. Tests cover three orbit representatives across twelve graph-size combinations and five gains, plus all pairs across six size combinations and two more gains.

The analytical proof uses the exact Laplacian eigenspaces, a block Schur-complement identity, Sherman--Morrison, and strict polynomial inequalities in the three parameters. The code is a finite consistency check, not a proof over all graph sizes and real gains. The 2020 windmill-coherence primary study was only accessible through its abstract, so equivalent previously published finite-gain coverage remains an unresolved research risk. The result has not undergone independent audit.
