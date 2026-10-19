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

The theorem is proved symbolically in `RESULT.md`: exact group-algebra identification, automorphism reductions for nonzero linear and quadratic strata, tensor homology when the leading quadratic has rank two, and alternating-form counts for all fibers. Nothing here claims external validation.

Reproduce the direct \(\mathbb F_2\) check with `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`. It enumerates every one of the \(2^{20}\) quadratic/cubic coefficient combinations (with higher terms zero), checks another 40,000 full augmented elements and validates that the symbolic polynomial totals \(2^{31}\). It printed `VERIFY_OK_GROUP_ALGEBRA_5`.

Reproduce the independent actual extension-field \(\mathbb F_4\) checker with `python3 verify_gf4.py`. It computes direct matrix ranks over the irreducible polynomial arithmetic in characteristic two for 580 prescribed and independently sampled full elements, printing `VERIFY_OK_GROUP_ALGEBRA_GF4`.

The computations corroborate rather than prove the formula for all finite fields of characteristic two. No unrestricted machine certificate, expert assessment or independent audit has been performed. The result does not claim validity for any other number of generators or arbitrary modules.
