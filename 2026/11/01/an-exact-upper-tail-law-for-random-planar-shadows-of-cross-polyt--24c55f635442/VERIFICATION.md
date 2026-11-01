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

The finite checker `check.py` uses only Python's standard library and executes seeded orientation tests, deterministic two-generator containment checks, Cauchy--Binet checks, convex-hull area computations, and exact Gamma-product moment comparisons. Run `python3 check.py` from the directory containing this document and the script. The reported empirical tail proportions agree with the proved polynomial law within the specified statistical tolerances for the tested dimensions.

The crucial unlimited-parameter deductions are mathematical, not computational: the tight-frame lemma when a Plücker coordinate exceeds \(\sqrt{2/3}\), the positive upper-tail interval from the published uniqueness of maximizing coordinate planes and compactness, the exact beta law from independent sphere factors and moments, and the iid extreme-value limit. Finite tests cannot verify these for every dimension, every small threshold, or infinitely many random orientations. The interval endpoint is not evaluated numerically. No independent external audit has been performed.
