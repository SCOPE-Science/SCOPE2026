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
# Reproducibility and limits

Run `python3 check_bichord_nonmatching.py` using Python 3 and the standard library. The program constructs each original cycle edge and each inserted chord explicitly, enumerates every size-\(t\) matching from all combinations of \(t\) edges, confirms the claimed complete list of perfect matchings, constructs every face, and independently reduces mod-two boundary matrices. It does not assume the claimed homotopy result in its code.

**Recorded checks:** Every stage at every width \(2\le t\le7\): 18 complete face enumerations, in total 148,638 nonempty faces, with direct reduced-Euler-characteristic checks. For \(2\le t\le5\), all 12 complete reduced mod-two Betti vectors were calculated and agreed with the corresponding sphere or contractible space. The recorded run ends with `REPLAY_OK total_nonempty_faces=148638; cases=18; full_mod2_homology_cases=12`.

These finite computations are not exhaustive over the unbounded parameter \(t\), do not establish integral torsion-freeness, and do not themselves prove a homotopy equivalence. The symbolic matching-enumeration, join decomposition, and CW pushout proof in `RESULT.md` establish the uniform integral claim. No separate independent audit has been performed.
