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

# Reproducible checks

From the directory containing the accompanying `verify.py`, run:

```sh
python3 verify.py
```

The self-contained Python 3 program needs only the standard library. It checks exact subset-recursion coefficients for 1,441 labeled trees with 2–6 vertices and 238 connected labeled unicyclic graphs with 3–5 vertices. It also checks the independently expressed \(n!\)-ordering cut-sum against subset recursion on six representative graphs, and solves their full transient continuous-time Markov equations exactly over rational numbers at \(\lambda=20\) and \(\lambda=60\), observing convergence toward the derived coefficients. No file beyond the supplied program is used.

**Limits:** The computational census is finite, and the six finite-rate solutions are examples only. The general assertion for every connected graph and all fixed sizes as \(\lambda\to\infty\) is proved analytically in RESULT.md. This reproduction does not establish global bibliographic novelty or constitute an independent audit.
