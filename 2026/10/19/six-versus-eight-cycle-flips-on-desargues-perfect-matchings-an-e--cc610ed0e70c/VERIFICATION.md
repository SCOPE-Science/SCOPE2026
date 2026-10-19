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

# Reproducible finite verification

Run from this document's directory:

```
python3 verify_gp.py
python3 verify_incidence.py
```

Only the standard library is required. The complete `state_transition_certificate.json` stores all \(60\) matchings of the two/three-subset inclusion model and both lists of \(120\) hexagon and \(60\) octagon transitions. Both verifiers recompute, rather than merely trust, those labels. `verify_gp.py` enumerates the vertex-simple actual cycles of \(GP(10,3)\) and toggles each; it checks the explicit model isomorphism against the certificate. `verify_incidence.py` generates bijections independently, recomputes the permanent by mask dynamic programming, and constructs the flip graphs by permutation-difference tests justified by girth six. It also checks all \(120\) induced \(S_5\) actions, parity classes, the doubled-\(K_6\) subdivision, and per-state distance profiles. Each included `.out` is the actual expected program output and must terminate in `VERIFY_OK` when replayed from the packaged paths.

No finite check in this package proves a theorem about larger generalized Petersen or middle-level graphs; the exact claim concerns only the twenty-vertex Desargues graph. Independent external verification has not been performed.
