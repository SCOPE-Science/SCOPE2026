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

# Mathematical verification and limits

The theorem is proved analytically by an exact reduction of the real zero-sum distance-power quadratic form, a two-dimensional generalized eigenvalue calculation, and implicit differentiation of its smaller characteristic root. Its quantifiers cover every integer \(r\ge3\), every integer \(u\ge4\), and every positive integer split \(a+b=u\). The endpoint \(p=\wp\) is included; exponents greater than the threshold fail negative type.

The accompanying `verify.py` is self-contained Python source apart from NumPy. Running it produced these diagnostics: 1,308 high-precision characteristic-equation residual tests; 1,080 strict/flat adjacent-balancing comparisons; 133 full-distance-matrix eigenvalue calculations at, below, and above the theoretical threshold; and six exact-fraction reversal examples. The full-matrix tests construct the distance matrix independently of the reduced characteristic polynomial. These checks do not exhaust the unbounded parameter ranges, which are settled by the proof in `RESULT.md`.

Scientific comparison inspected the full available content of a 2011 source on negative type of finite metric spaces and the author-posted 2000 source on hypermetric two-distance spaces. The published 1990 embedding reference remained inaccessible in full text. The originality assessment is literature-based, not a claim of machine-certified uniqueness.

Self-review: passed. Independent audit: not yet performed.
