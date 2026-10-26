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

# Reproduction and scope

Run `python verify.py` using Python 3.10 or later. The verifier uses only the standard library; no downloaded packages, external sources, or randomness are required. It checks all eight possible ballot types, including empty ballots, for each anonymous three-candidate profile with one to six voters. Its deterministic terminal output reports profile counts \(8,36,120,330,792,1716\) and strong-nonnesting counts \(0,0,0,0,0,3\), followed by `PASS`. It tests the complete irresolute winner sets rather than selecting convenient tie-breakers.

The exact mathematical argument is in `RESULT.md`, which proves the bound for any number of voters using inequalities on approval-type counts. The verifier supplies an independent small-case cross-check but does not formally certify the infinite proof. Only self-review was performed; independent audit remains unperformed. No claim is made for more than three candidates or for committee sizes beyond one and two.
