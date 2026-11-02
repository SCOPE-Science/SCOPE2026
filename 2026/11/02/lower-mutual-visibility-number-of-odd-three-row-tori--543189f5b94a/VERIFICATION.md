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

# Verification of the odd three-row torus result

Run `python3 verify.py` using Python 3 and the standard library only. The code builds \(C_3\square C_n\), obtains graph distances by breadth-first search, tests \(X\)-visibility by recomputing distances while forbidding other members of \(X\), and checks maximality against every outside vertex.

The checker verified inclusion-maximality of the explicit five-set for odd \(n=5,7,9,11,13,15,17,19,21,31,41,51\); it independently enumerated every subset with one to four vertices for \(n=5,7,9\). The executable returned `VERIFY_OK` on the delivered source. This finite test does not establish the theorem for all odd \(n\); the symbolic row-occupancy argument and six maximality cases in `RESULT.md` do.

No external audit, proof-assistant formalization, or complete literature-priority guarantee has been performed.
