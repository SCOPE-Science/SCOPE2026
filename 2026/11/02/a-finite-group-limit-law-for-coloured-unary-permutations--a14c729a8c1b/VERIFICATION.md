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

The finite checker uses only the Python 3 standard library. Execute `python checker.py` from the artifact directory. It independently enumerates permutations, colourings and all candidate automorphisms for the sizes identified in RESULT.md, then compares the exhaustive group orders with the necklace/wreath decomposition and the EGF. It also checks primitive-necklace counts and a high-precision evaluation of the binary order-two limiting constant. The observed run completed with `ALL_CHECKS_OK`.

The total-variation conclusion and exponential convergence rate depend on the symbolic combinatorial proof and uniform tail bounds in RESULT.md, not finite experiments. Numeric truncation of the infinite series includes an explicit omitted-tail bound. Source inspection identified the exact previously published rigidity count; it is not represented as a new conclusion. Independent audit and independent validation have not been performed.
