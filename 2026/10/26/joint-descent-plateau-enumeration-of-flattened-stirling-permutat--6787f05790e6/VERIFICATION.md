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

# Reproduction instructions

Run `python3 verify.py` with Python 3.9 or newer and the standard library. The script computes a polynomial indexed by the ordered pair (number of internal descents, number of internal plateaux) from a signed-block coefficient recurrence, then independently produces all Stirling permutations by inserting each new maximum as an adjacent double-letter, retaining exactly those with nondecreasing weak-run starting values. It counts both adjacent statistics directly.

The exact tables agree for \(n=1,2,3,4,5,6,7,8\). The flattened permutation totals are \(1,2,6,24,116,648,4088,28640\). A successful run prints `VERIFICATION_OK`. The direct word generator is exhaustive within those finite values, while the theorem for all \(n\) follows from the published bijection plus the block-weight computation supplied in `RESULT.md`. These computations alone do not certify the infinite theorem, novelty, or independent validation.

Specialization checks: \(u=1\) agrees symbolically with Shankar's known descent-only Corollary 10; setting \(t=u=1\) gives the known Dowling EGF \(\exp(x+(e^{2x}-1)/2)\). No external programs, proprietary data, or unpublished inputs are required.
