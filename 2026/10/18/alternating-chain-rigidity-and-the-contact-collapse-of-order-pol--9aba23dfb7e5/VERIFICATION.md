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

# Verification record

The proof uses exact filter geometry: every antichain supports a free filter subcube; longest-chain ranks partition the ground set into antichains; and signed-chain widths are exactly suffix-walk spans. It applies without finite-size restrictions. The contact comparison uses a separately published facet formula for the enriched chain polytope, not an assumed equivalence of the two polytopes.

The `verify.py` program was executed with Python 3, without third-party packages. It exhaustively checked 407 transitively closed naturally labeled posets on one to five elements, testing 89,794 nonzero ternary directions and counting 1,760 predicted equality witnesses. It also checked the signed suffix-walk formula on every longest chain in each tested poset. The observed terminal message was:

```
PASS: 407 posets, 89794 directional checks, 1760 shortest-unit-direction witnesses
```

These checks provide finite corroboration only. They are not exhaustive for unbounded dimension and do not replace the general proof. A separate independent mathematical audit has not been performed.
