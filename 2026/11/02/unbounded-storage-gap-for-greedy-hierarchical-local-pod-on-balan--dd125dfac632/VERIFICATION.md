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

# Reproducibility record

Execute `python3 verify.py` from the folder containing the standalone verifier. It uses Python 3 standard library `fractions.Fraction` and integer arithmetic, requires no third-party dependencies, and contains 3,550 deterministic checks. Tests include exact Gram matrices for three finite sizes, rank/budget comparisons at every dyadic node for six sizes, root/children storage inequalities, and exhaustive dynamic-programming selection of the cheapest cut of the declared binary hierarchy for five sizes.

Actual successful program output includes exact costs at \(r=2,4,8,16,32\), and the terminal message `PASS: 3550 exact assertions; universal result relies on algebra, not these finite tests`.

The infinite family and asymptotic limit are proved symbolically in `RESULT.md`; the finite tests do not establish the all-dimension claim. The public references support the definition of the compression scheme. An inaccessible potentially related specialist manuscript and the absence of independent mathematical audit limit historical-priority confidence, not the stated exact checks.
