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
# Reproducibility and limits
The proof is analytic and valid for arbitrary finite factor dimensions and all \(1\le p\le\infty\). Its critical nonstandard steps are (i) forcing independent-block decomposition of unique extremal ellipsoids; (ii) exact block gauge supremum identities; (iii) strict weighted-product extremization; and (iv) equality cases of the scalar Hölder inequalities. All steps are written in `RESULT.md`.

Run `python3 checker.py` with Python 3's standard library. It tests three block-dimension vectors, eight exponent values including \(p=1,2,\infty\), and 36,000 scalar feasibility samples, alongside the exact dimension-weight and entropy normalization identities. The checker is finite corroboration, not a substitute for the proof or a certification of novelty.

The references were compared by their displayed mathematical statements and inspected relevant primary sections. The possibility of an unlocated equivalent classical direct-sum statement remains. No independent mathematical audit has been performed.
