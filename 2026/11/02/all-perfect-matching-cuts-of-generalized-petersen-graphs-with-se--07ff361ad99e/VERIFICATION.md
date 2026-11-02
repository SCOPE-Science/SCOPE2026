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
The included `verify.py` is standalone Python 3 (standard library only). It enumerates all 128 local seven-bit words, confirms the exact set of 28 admitted words, proves a closed-walk-preserving pruning leaves two self-loops plus two five-cycles, and checks the transition equations against direct graph vertex-color enumeration for orders \(5\le n\le10\). It independently enumerates all outer words through \(n=18\), constructs the complementary five-periodic solutions for all multiples of five up to 210, and terminates with `VERIFY_OK` when assertions hold.

The proof of the infinite theorem is in the finite-state automaton equivalence, the complete finite 128-case certificate and the directed-cycle core. Finite graph tests only provide additional checks. The certificate was assessed under self-review; independent audit was not performed.
