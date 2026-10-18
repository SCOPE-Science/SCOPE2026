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

A coordinate order α has a unique affine-normalized representative α_0=0,α_1=1; distinct normalized orders are distinct dimension-two codes. For equal-length words d_insdel=2(q-LCS), and the maximum LCS among distinct affine permutations α and uα+v gives τ=q-1-L_max (constant codewords have LCS<=1). The reduction of LCS between permutations to strict LIS of position indices is exact. An independently written finite-field/LIS C++ exhaustive enumeration reproduced the eight τ histograms for all (q-2)! normalized orders, notably 362880 q=11 codes times 109 nonidentity transforms. An independent q=13 LCS dynamic-programming check reproduced histogram 3:6,4:37,5:73,6:39 and τ=6; the Hamming radius is 5. No q=13 full census or larger-q claim follows.

## originality

PASS

Best-of-knowledge statement-level originality based on the named searches and primary-source comparisons below; previously established prerequisites and tabulated partial cases are expressly excluded from novelty. Unindexed equivalent results are not ruled out.

## value

PASS

The complete first eight field-size distribution for every dimension-two full-length RS evaluation order is a natural exact synchronization-code invariant, refining known zero-radius results and providing a concrete field-13 strict improvement witness. Exact finite classifications serve as sharp benchmarks rather than arbitrary toy examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
