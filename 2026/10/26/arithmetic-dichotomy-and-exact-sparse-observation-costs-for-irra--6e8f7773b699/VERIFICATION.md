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

The included `verification_rotation.py` builds the finite directed covering graph and tests exact rational dual witnesses using integer edge weights. Running `python3 verification_rotation.py` prints `VERIFY_OK` if all tests succeed. In particular, for cut displacement five and radius one it enumerates 128 graph vertices and 252 edges, checks no negative directed cycle under weight `11*bit-2`, and checks the period-11 word `10010000000`, proving the exact value \(2/11\) within the finite covering problem. It also checks radius-zero instances for displacements 1–9 and consecutive-window cases. The remaining universal argument is mathematical: rotation-factor fibers, density of irrational arithmetic subsequences, and finite-graph cycle decomposition; the finite checks do not prove these general lemmas by themselves.

Independent audit: not performed.
