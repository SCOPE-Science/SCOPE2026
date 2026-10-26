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

# Verification record

The proof uses exact linear-algebra rank inequalities over an arbitrary field; no computational conjectures are assumed. The relevant identities are (i) principal right and left ideal dimensions as sums of leading and trailing principal-corner ranks, (ii) the sharp inequalities \(\operatorname{rank}(X^{[j]})\le\min(r,j-1)\) and \(\operatorname{rank}(X_{[i]})\ge\max(r-i+1,0)\), (iii) the nonvanishing of the superdiagonal-product minor at equality, and (iv) rank-preserving rook moves proving interval attainability.

Run with Python 3 from the package directory: `python check.py`. Successful output: `TRIANGULAR_ONE_SIDED_GAP_OK 13 exhaustive field-and-size cases`. The script enumerates all radical matrices for field sizes \(2,3,4,5\) at stated small dimensions, constructs products with triangular matrix units directly in smaller instances, computes independent ideal-span ranks and compares all fixed-rank gap and endpoint predictions. The computation is exhaustive only in those thirteen finite cases; the written algebraic proof covers all fields and sizes.

No independent mathematical audit was performed. The finite tests do not establish publication priority, rule out an indirect consequence of older orbit classifications, or resolve the uncounted nonextremal gap fibers.
