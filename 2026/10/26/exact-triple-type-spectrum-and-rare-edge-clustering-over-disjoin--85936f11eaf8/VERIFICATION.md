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

# Verification scope
The proof is mathematical and applies for all fixed integers \(r\ge3\), \(k\ge3\), and all \(b\ge1\). The accompanying `verify.py` independently implements a literal finite-graph \(K_{r+1}\)-freeness test and a separate common-neighbour test. For selected small cases they agree on all inspected neighbourhood matrices. A two-block direct-graph test checks the independence across distinct parameter cliques. The exact four-base triple identity and the ordering of the first three bases are also exercised. The output file `verification-output.txt` records the actual successful execution.

Execute `python3 verify.py` using Python 3.9 or later; no third-party libraries are needed. Finite computations do not prove claims for arbitrarily large parameters, do not constitute literature originality certification, and do not constitute independent audit. No results about repeated tuple coordinates or algebraic types are checked.
