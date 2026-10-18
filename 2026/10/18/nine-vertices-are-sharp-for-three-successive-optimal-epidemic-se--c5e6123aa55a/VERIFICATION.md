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

# Exact verification

Run `python3 verify_three_sentinel_winners.py` with Python 3 and no third-party modules. The completed run printed the tree-class counts `1,1,1,2,3,6,11,23`, precisely one eight-vertex tree with three cumulative-profile Pareto candidates, and successful exact coefficient verification of that exceptional tree and of both nine-vertex witness polynomial identities. The checker also verifies strict cumulative-profile domination of all noncandidate vertices in the witness.

The classification is exact for all real \(0<p<1\): the proof uses symbolic polynomial factorizations, strict signs of their monotonically varying factors, and an exhaustive finite census. The reported decimal root values are informational only. The result makes no claim of universal graph-size classifications beyond the stated sharp minimum or of independent validation. The code is supplied in the package itself; independent execution outside this submission remains optional and unperformed.
