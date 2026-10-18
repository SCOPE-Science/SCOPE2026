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

# Reproducible checks

Execute `python3 verify_caps.py` using Python 3; no third-party packages are needed. The script constructs directed geodesic graph examples, independently counts linear extensions by subset dynamic programming, counts lattice-valued feasible Lipschitz potentials directly from graph edge inequalities, and obtains an exact leading-volume coefficient from the forward difference of the degree-\(d\) Ehrhart counting polynomial. It runs \(11\) weighted examples plus \(3\) unweighted diameter-three examples and finishes with `ALL EXACT TESTS PASS`.

The checker tests concrete finite instances only. Its use of forward differences is valid for the stated integral constraint polytopes and half-open caps, but its finite runs do not prove the asserted identity for arbitrary graph size or nonintegral weights. The general proof is given in `RESULT.md`. No independently authored or externally certified audit has been performed.
