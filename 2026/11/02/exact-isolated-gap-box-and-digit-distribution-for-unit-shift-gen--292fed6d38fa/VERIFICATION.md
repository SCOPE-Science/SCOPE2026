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

# Reproducibility of the isolated-gap classification

The ordinary Python 3 verifier `verify_repunit_isolated.py` was executed against this theorem's exact generator formula. It independently computes each Apéry set via Dijkstra shortest paths over residues, compares it to the digit-height formula, checks membership through all gaps up to the computed Frobenius number, constructs the isolated-gap set using both adjacent membership tests, and compares the result to the claimed digit box and stratum counts.

Observed complete output:

```
PASS: 24 complete families; 84180 gaps classified; 1533 isolated gaps; 154 strata checked
```

The tested parameter region is all \(2\le b\le6\), \(2\le n\le6\) with repunit multiplicity \(r_n\le5000\). The theorem domain is \(n\ge3\); dimension two is tested as a boundary check. These computations establish exact finite cases only. The universally quantified theorem is supported by the proof in `RESULT.md`, which uses the previously established Apéry formula explicitly acknowledged there.

No independent audit or external formal certification has been performed.
