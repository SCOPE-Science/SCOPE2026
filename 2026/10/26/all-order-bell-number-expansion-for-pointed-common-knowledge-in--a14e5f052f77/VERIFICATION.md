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

# Verification and reproducibility

Execute `python checker.py` to verify the exact integer root-component histograms for all ordered pairs of partitions through \(n=6\), all ordered triples through \(n=4\), and the corresponding exact rational pointed common-knowledge probabilities for \(p=1/2\). The computation uses only Python's standard library, enumerates partitions independently of the connected-tuple recurrence, and checks equality by assertions.

The remaining asymptotic verification is deductive: the ratio of consecutive crude component weights is bounded below half-size by a constant strictly below one, using Bell-number adjacent-ratio asymptotics; symmetry relates large components to small components with an exponentially decreasing marking factor. The resulting tail bound is of the claimed size for each fixed truncation order. The code does not and cannot certify the asymptotic statement for infinitely many sizes. Older general weighted-component theorems may independently cover the result; no exhaustive priority claim is made. Independent audit has not been performed.
