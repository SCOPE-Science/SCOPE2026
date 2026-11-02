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

# Reproducibility

Execute `python3 verify.py` using Python 3 and only its standard library. The source iterates the complete set of labeled Prüfer words of length \(n-2\) over \(n\) labels for every \(3\le n\le8\); it decodes each word into edges and reconstructs vertex degrees from edges (rather than trusting symbol counts). Independently, it constructs conditional empty-box distributions through Stirling-number surjection counting. It compares exact masses, conditional expectations, every stochastic dominance and incomparability stated for the finite cases, and the degree-leaf covariance. It additionally checks exact mean crossover fractions for \(4\le n\le10\).

The completed verification returned 255 exact assertions passed and 280391 independently decoded trees (3+16+125+1296+16807+262144). No Monte Carlo or floating-point comparisons are used in these checks. All larger sizes rest on the finite-symbol coupling and inequalities in the mathematical proof; an exhaustive computation for small sizes does not prove an infinite classification.

The proof is restricted to uniform labeled unrooted Cayley trees; the independent audit has not been performed. Classical exact degree-sequence enumerators contain much of the foundational probability calculation, so historical novelty concerns the complete stochastic comparability diagram and threshold, not the enumerator.
