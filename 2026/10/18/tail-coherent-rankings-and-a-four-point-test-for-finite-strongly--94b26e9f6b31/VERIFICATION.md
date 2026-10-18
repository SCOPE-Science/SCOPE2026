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

# Computational verification and boundaries

The supplied `verify.py` enumerates all labelled ranking profiles satisfying the proved four-point criterion through five worlds, computes isomorphism orbits, and compares the four-point condition with the literal subset-based strong-density equation through four worlds. Command: `python3 verify.py`. Expected final output: `VERIFY_OK`.

The separate `verify_direct.c` avoids all ranking assumptions. It exhaustively constructs all centered, total, functional choice tables on four worlds and tests the original strong-density equation on every nonempty nested antecedent. Compile with `cc -O3 -std=c11 verify_direct.c -o verify_direct` and execute `./verify_direct`. Expected final output: `raw=331776 dense=138`.

The code is not an infinite-size proof. The all-size classification and algorithm follow from the contraction-consistency, transitive-tournament and suffix-coherence arguments in `RESULT.md`. No outside independent audit is asserted or implied.
