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

The accompanying `verification.py` uses only Python's standard library and exact rational arithmetic. Run `python verification.py` from this directory. Its sole JSON output line matches `certificate.json` exactly, including the trailing newline.

The program checks every labeled simple graph with one through five vertices (1,099 graphs), comparing the square-cycle condition to clique-union structure. It also constructs a heterogeneous target-proportional directed example on six sites and verifies all state-edge balance identities, detects the two-site unbalanced directed obstruction, and checks an exact cycle-product ratio on a three-site path. The tested graphs are finite and do not substitute for the unrestricted proof. The unrestricted result is proved in the accompanying scientific manuscript by necessary square-cycle identities and an explicit reversible measure.

The calculation does not establish that the result has passed an independent external audit, and does not resolve possible bibliographic equivalents.
