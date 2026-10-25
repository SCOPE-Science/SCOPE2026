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
# Verification details

The deterministic standalone checker `verify.py` was executed in the same directory as `certificate_rank3_n5.txt` using Python's standard library. The output was:

```text
VERIFY_OK individual_extremal_checks= 3000 rank_three_pairs= 20 fixed_idempotents= 20 moved_idempotents= 1
```

It reconstructs the monotone maps from their exact finite coordinates; for every admissible parameter and every integer \(3\leq n\leq12\), it checks both mutual-inverse compositions, involutivity, precise idempotent fixed sets, and transposition-count identities. Separately it parses the twenty-pair five-point certificate, verifies disjointness, verifies each mutual-inverse identity on the full five-point chain, checks that precisely the twenty remaining rank-three elements are idempotent, and identifies the unique moved idempotent.

These checks do not establish the infinite statements: those follow from the explicit algebraic involutions and inverse relations proved in `RESULT.md`. The nonexistence of an all-idempotent-fixing involution on five points follows from the exact 21-versus-60 parity count and the impossibility of nonidempotent self-inverse monotone maps, not from unsuccessful search. The certificate proves the sharp attained finite case. Independent audit was not performed.
