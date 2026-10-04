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
# Verification

The proof has three independently checkable components.

First, any factorial factor contributing to a Jordan–Pólya number with largest prime divisor \(p\) must have index below the next prime after \(p\). For largest prime at most \(11\), the only non-prime factorial indices that can then occur are reduced by the six displayed identities in `RESULT.md`.

Second, the prime-valuation matrix of \(2!,3!,5!,7!,11!\) and each initial subfamily is triangular with unit diagonal. Hence it is unimodular, proving uniqueness of the integral coordinates. Adding \(13!\), the same computation gives coordinate vector \((1,-1,-1,1,0,1)\) for \(14!\), which proves failure of nonnegative prime-factorial coordinates at that support.

Third, the counting statement is a deterministic fixed-dimensional lattice-point estimate. For weights \(w_i=\log(p_i!)\), unit-cube comparison with the weighted simplex gives main volume \(T^r/(r!\prod_iw_i)\) and boundary error \(O(T^{r-1})\).

The accompanying `verify.py` checks all finite identities, the valuation determinants and the \(14!\) coordinate vector, and performs an additional semigroup comparison through \(10^{10}\). A successful replay prints a line beginning `VERIFY_OK`. This finite calculation is corroboration only; no infinite conclusion is inferred from the cutoff.
