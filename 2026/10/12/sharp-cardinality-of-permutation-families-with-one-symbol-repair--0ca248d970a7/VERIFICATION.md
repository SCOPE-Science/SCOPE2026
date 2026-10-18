---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The observer map i->j(i) is a finite loop-free functional digraph: each weak component contains a directed cycle of length >=2. Fixed value at any cycle vertex determines the values throughout the component by traversing inverse repair equations. Processing t components of sizes s_j bounds family size by product_r (n-sum_{h<r}s_h). Even n gives 2^m m!. Odd n forces one size>=3, placed first, and gives n(n-3)(n-5)...2. The construction with a three-letter (r,f(r),g(f(r))) prefix and h-paired suffix realizes equality at all odd lengths, including n=3. Independent n=3,5,7,9,11 construction/repair enumeration obtains 3,10,56,432,4224.

## originality

PASS

The 2016 Raviv–Yaakobi–Médard preprint includes an unqualified n!! equality but the two-symbol block construction requires 2|n. For odd n=5, its blanket 5!!=15 prediction conflicts with rigorously proved upper 10. The surviving contribution is the corrected sharp odd-length optimum and matching triple-prefix construction. The 2018 journal full text remains inaccessible and could contain a later correction.

## value

PASS

The fixed-observer permutation locality maximum is a natural exact coding parameter; the odd case was previously bounded between a smaller pair-block construction and a larger general bound. The explicit corrected optimum and construction solve the natural parity gap and correct the invalid general equality extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
