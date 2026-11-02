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

Execute `python3 verify.py` with Python 3 and no external packages. The verifier enumerates every length-\(2n\) balanced bridge for each \(1\le n\le9\), groups them by the full ordered list of excursion semilengths, and uses rational arithmetic to test both conditional expectations. Every bridge, not a sample of bridges, is enumerated in that finite range. It also checks independent coefficient formulas through \(n=100\). The completed execution passed 1,267 assertions.

The analytic proof in `RESULT.md` establishes the all-positive-integer case using a Catalan first-return generating function, the exact mean of the squared-height energy, and fair conditional excursion signs. The numerical checks do not by themselves establish an infinite identity, nor has the result undergone independent audit. Originality remains subject to historical full-text coverage limits stated in `REVIEW.md`.
