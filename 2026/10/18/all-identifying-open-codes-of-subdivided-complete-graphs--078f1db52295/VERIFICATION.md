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

# Reproducibility and mathematical verification

The package contains a self-contained `verify.py`, requiring only Python 3's standard library. Run `python verify.py`. It checks the code definition on the actual incidence graph, independently checks the selected-edge condition, extracts the full coefficient polynomial through a signed exponential-formula expansion, and compares the proposed exact minima and multiplicities.

For \(n=3,4,5\), every code subset is checked directly (\(64\), \(1{,}024\), and \(32{,}768\) possibilities). For \(n=3,4,5,6\), all \(2^{\binom n2}\) subsets of edges are evaluated. The counts of admissible edge subsets are \(4,38,728,26{,}864\), with minimum-edge multiplicities \(3,16,125,90\); the corresponding minimum-code counts are \(9,64,625,540\). The independent generating-function coefficient tests pass in each of these four sizes. There are no probabilistic or timeout-dependent acceptance steps.

For general \(n\), correctness comes from the six-step mathematical proof in RESULT.md. The finite enumeration neither establishes completeness of the bibliography nor replaces an independent proof review. Independent audit status is not performed.
