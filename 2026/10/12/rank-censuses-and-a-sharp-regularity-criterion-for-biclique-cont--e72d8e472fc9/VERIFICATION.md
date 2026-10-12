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

The proof's fiber argument, section equivalence, multinomial allocation, and idempotent cases were checked symbolically as written in `RESULT.md`. The finite cross-checker is `verify.py`, which uses only Python's standard library.

Execute `python3 verify.py` from this directory. It enumerates every partial map on each listed graph and evaluates continuity by inspecting **all full vertex and edge preimages**, independent of the fiber-formula derivation. It computes empirical rank enumerators for all maps, nonregular maps (testing continuous sections), and idempotents (evaluating \(f^2=f\)), and matches them against separately implemented closed-form expressions. It also independently searches for full-semigroup witnesses \(fgf=f\) on graphs with at most four vertices.

Verified totals, as (all, nonregular, idempotent), were: \(K_{1,1}\): (9,0,6); \(K_{1,2}\): (36,4,14); \(K_{1,3}\): (185,36,31); \(K_{1,4}\): (1278,288,68); \(K_{2,2}\): (169,16,36); \(K_{2,3}\): (874,174,86); \(K_{3,3}\): (4489,756,220). The verifier terminates with `VERIFY_OK`.

These checks are finite tests, not exhaustive over all graph sizes; correctness for arbitrary \(m,n\ge2\) depends on the five-step mathematical argument. The novel scope excludes the previously enumerated star cases. No independently audited certification is claimed.
