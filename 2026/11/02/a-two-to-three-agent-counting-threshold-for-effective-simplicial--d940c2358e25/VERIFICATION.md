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

# Reproducibility and scope of verification

Run `python checker.py` in this directory using Python 3. The program directly enumerates all subsets of facets satisfying owner knowledge and the (SN) external-uncertainty clause, independently of the claimed counting formulas. It then compares with the two-agent degree product and three-agent bipartite edge-cover enumeration.

The executed result was:

```
ALL_CHECKS_OK two_agent_graphs=116 three_agent_graphs=145
```

Tests cover 116 bipartite graphs (two-agent complexes) and 145 bipartite graphs embedded as three-agent complexes, including instances with isolated outside vertices and zero capacity. The checker has no external imports or data dependencies. The general counting theorem follows from the full bijections in `RESULT.md`; finite exhaustive tests are not proofs for unrestricted input size. The published counting-hardness premise is Amarilli--Monet--Senellart (2017), Appendix D, Theorem D.1. No independent audit has been performed.
