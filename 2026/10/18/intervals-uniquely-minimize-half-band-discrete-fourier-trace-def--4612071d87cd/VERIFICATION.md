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

# Verification details
The proof is analytical: direct Fourier integration, trace expansion, an induction on the sample cardinality for all odd-distance cutoffs, and an absolutely convergent nonnegative layer-cake expansion. The sharp uniform constant is checked independently by the two-site example \(\{0,3\}\).

The included `verify.py` is standalone and requires only Python's standard library. Run `python verify.py` after extraction. It enumerates every subset of a specified finite integer grid with several small cardinalities, using exact rational edge and weighted sums. Those finite checks are diagnostic, not a replacement for the all-cardinality induction. No interval computation, code execution or finite scan is claimed to certify the theorem's historical priority.
