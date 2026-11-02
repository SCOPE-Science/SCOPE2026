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

# Reproduction and limits

The accompanying `checker.py` uses only Python standard-library modules. Invoke it with `python3 checker.py` in a directory containing that file. The observed output from the packaged source is:

```text
PASS 3311 exact and symbolic assertions plus bounded Monte Carlo diagnostics; finite tests are not asymptotic proofs.
```

The code constructs the entire exact distribution of the three edge-type counts from the part-size transition probabilities, then independently constructs it by enumerating actual labeled feasible edges on all tripartite graphs with part sizes up to three each. It checks normalization, terminal feasibility and agreement of the two exact distributions. Using a coefficient dictionary for multivariate polynomials, it proves by exact arithmetic that the proposed fluid solution satisfies all three ODEs and verifies the exact edge-intensity cancellation identities. It checks rational integrated-count identities, evaluates the ratio on thousands of rational triples and performs bounded seeded Monte Carlo diagnostics at larger sizes.

**Scope of evidence:** The asymptotic finite-horizon limit, the interchange of the terminal and scaling limits, and the global real-parameter optimization are established in `RESULT.md` by martingale/Gronwall, a deterministic truncation argument and elementary inequalities, respectively. Finite enumerations and finite grids cannot prove statements over every size or real triple; randomized diagnostic accuracy is not used as an acceptance criterion. The inspection did not obtain the full text of the older Dyer–Frieze paper. No independently audited mathematical certificate or publication-priority certificate is claimed.
