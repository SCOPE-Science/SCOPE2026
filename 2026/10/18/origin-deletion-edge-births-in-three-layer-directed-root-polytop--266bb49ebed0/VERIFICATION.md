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

# Verification of the directed-root edge graph

Run `python3 verify.py` with Python 3. The checker uses only integer arithmetic and the standard library. It enumerates every pair of root vectors in all 125 triples of part sizes between one and five. For alleged edges it verifies that the corresponding explicit potential has exactly two maximizers and hence defines an exposed edge. For alleged nonedges it checks a second distinct pair with exactly the same root sum. It also checks the closed edge formula, all three local-degree formulas, diameter at most two, and the exact number of negative-support edge witnesses associated with the singleton-middle transition.

Observed output:

```
VERIFY_OK parameter_profiles= 125 vertices_total= 3375 edges_total= 24975
```

The universal theorem is established by the explicit separating-potential construction and exhaustive algebraic pair-type case distinction in `RESULT.md`, not by finite-profile enumeration. The code is an independently executable consistency check of those constructions, not a formal proof assistant and not external validation.
