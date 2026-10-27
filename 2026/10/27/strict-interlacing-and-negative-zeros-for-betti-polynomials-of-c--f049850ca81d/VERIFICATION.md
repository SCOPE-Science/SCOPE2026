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

# Verification of the theorem

The mathematical argument is the induction in `RESULT.md` and is uniform for \(r\ge2\) and every \(n\ge0\). In its critical root evaluation, the interlaced lower polynomial and the derivative have the same sign at each simple negative zero, and the term weighted by \(r-2\) cannot reverse that sign. The two outer sign changes use the monic degree and the constant term one. Thus root existence and distinctness follow without a numerical root solver.

Run `python3 verify.py` with an ordinary Python 3 interpreter. The standalone script uses only its standard library. It reconstructs the published additive Chow decomposition from all ordered integer compositions with jumps at least two, a separate Stirling-number expansion, and the three-term differential recurrence. In this package the execution result was `VERIFY_OK r-values=6 n=0..8 crosschecked_pairs=54`. It covers exactly \(r\in\{2,3,4,5,7,11\}\) and \(0\le n\le8\); it is not an exhaustive check for unbounded \(r\) or \(n\). Three handlisted published table entries are compared, and every tested polynomial is checked for degree, positive coefficients and palindromicity.

The principal possible scientific failure mode would be an incorrect derivation of recurrence (4) or a sign mismatch in (5). These are explicitly exposed as algebraic identities in `RESULT.md`, so a reader can independently reconstruct them. Originality is a literature-comparison judgment, not mathematically certified priority. Independent audit and independent validation have not been performed.
