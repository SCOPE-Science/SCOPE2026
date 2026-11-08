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

# Exact-rational verification

Run `python verify.py` in the same directory. It builds the five-site hypergraph specified in the finding and computes exact \(30\)-transient-state fixation probabilities by the full bit-mask chain. As a separate cross-check, it lumps the two interchangeable leaves into \(22\) transient equivalence classes, constructs that chain from canonical configurations, and exactly compares the single-mutant vectors for \(r=1\), \(r=3/2\), and \(r=2\).

All listed rational fixation probabilities and signs are asserted and substitution-checked. The neutral derivative is computed by differentiating the unreduced transition probabilities and solving the resulting derivative system. The check asserts \(\rho_H'(1)=2036/4965\), \(\rho_M'(1)=2/5\), and positive difference \(10/993\). The uniqueness of the transient solution follows from connectedness and almost-sure absorption, independently of the computation.

Checks do **not** establish the number of positive-fitness crossover roots, a root's exact location, or results for other hypergraphs. These are not claimed. No independent external validation has been performed.
