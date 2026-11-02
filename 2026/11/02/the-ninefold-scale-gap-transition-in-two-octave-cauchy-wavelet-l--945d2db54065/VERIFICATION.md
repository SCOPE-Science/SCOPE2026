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

# Verification notes

The accompanying `check.py` executes 205 deterministic assertions. It verifies the derivative identity, rational exact Sturm variations and squarefreeness for each \(k=2,\ldots,8\); it also tests the exact signed rational derivative evaluations for \(9\le k\le39\) and numerical peak bounds for several ratios. Invocation: `python check.py`, requiring SymPy. At the documented run, all 205 assertions passed.

The assertions are not a finite exhaustive verification of all \(k\ge9\). The proof in `RESULT.md` supplies the uniform symbolic inequalities, three-root Descartes bound, exact global-peak comparison, spectral change of variables, and large-ratio expansion. The normalization is fixed explicitly; no separate independent certificate or external mathematical review is claimed. General scale-only diagonalization and 2022 wavelet norm bounds are credited rather than asserted as newly discovered.
