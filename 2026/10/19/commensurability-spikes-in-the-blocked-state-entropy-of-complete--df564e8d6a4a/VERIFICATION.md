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

Running `python3 verify_potts_bipartite.py` directly from the package succeeds using only the standard Python 3 library. The implementation independently evaluates the original pairwise edge energy for each labelled state and tests every allowed one-site and two-site recolouring. It compares those direct tests with the theorem's equipartition-or-proper criterion and exact labelled counts.

The actual completed run checked 50 part-size/palette combinations, 25,300 labelled assignments, and the two-site status of 1,986 one-site blocked assignments. Every comparison passed. Additional integer count and asymptotic-ratio spot checks were run for palettes \(q=2,3,4,5,6,7\). The small \(q=2\) checks test an extension of the argument but are not part of the stated \(q\ge3\) novelty scope.

The verification program is a finite cross-check, **not** a substitute for the unrestricted-size proof. The asymptotic statements use onto-map inclusion exclusion and Stirling's formula, which are proved in the accompanying main text. No independent scientific audit has been performed.
