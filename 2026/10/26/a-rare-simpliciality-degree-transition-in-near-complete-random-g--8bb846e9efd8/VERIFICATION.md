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

# Reproduction and limitations

Run `python3 verify_simplicial.py` with Python 3.9 or later. No third-party modules, external services, or data files are required. The observed output was:

```
VERIFY_OK checks=70; exhaustive_graphs_n2_to_n6=33866; numeric_n=1000,10000,40000
```

The executable enumerates all simple labeled graphs for vertex counts two through six and checks exact rational probabilities at edge probabilities \(2/5\) and \(3/4\) for each degree of the marked vertex. It also numerically checks the direction of convergence for five positive parameter values. The checks are finite, and the normalized rare-event exponent, full large-deviation principle, and asymptotic localization rely on the mathematical proof rather than the computation. No independent scientific validation has been performed.
