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

# Verification and limits

The supplied `verify.py` performs an independent Gram-moment reconstruction, numerical matrix inversion, direct edgewise absolute-kernel integration, exact rational special cases and three symbolic Taylor-series comparisons. Its execution returned `PASS 3065 assertion groups; infinite assertions come from the proof in RESULT.md` with Python 3, NumPy and SymPy.

For every integer \(n\ge3\), the actual proof is the explicit rank-three reproducing kernel, a strict vertex-localization argument, a complete sign-interval proof, an exact edge-integral summation and analytic Taylor expansions in the three fixed residue classes. The verification program does not purport to enumerate all integers, all possible older literature, or all choices of input function. A separate historical-priority audit and an independent proof review have not been performed.
