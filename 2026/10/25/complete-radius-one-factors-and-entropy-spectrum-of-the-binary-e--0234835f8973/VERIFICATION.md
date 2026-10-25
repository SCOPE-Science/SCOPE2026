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

# Verification of the result

Run `python3 verify.py`. It uses only the Python standard library and reconstructs the finite parity graph, all output transitions, the closed determinized state spaces, equality of regular languages, the 256-rule census, surjectivity, and the exact integer characteristic polynomials. It separately constructs admissible input blocks through length ten (for outputs through length eight) and checks their emitted languages against the transducer. The closed powerset reachability is the unrestricted finite certificate; enumerated short blocks are corroboration, not an infinite proof. An independent mathematical audit has not been performed.
