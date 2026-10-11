---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

On the right exterior half-line the maximal profile is a decreasing convex envelope, so its positive increments are nonincreasing and are majorized by the singleton increments \(s_j=1/[(j+1)(j+2)]\). The second-rightmost support point improves the prefix at \(L\) by at least \(1/[(L+1)(2L+1)]\). Abel summation of \(s_j^2-d_j^2\) against prefix defects is nonnegative termwise, and retaining the \(L-1\) term gives exactly the tail loss \(2/[L(L+1)^2(L+2)(2L+1)]\). Inserting this into the published \(2m\)-boundary decomposition and dividing by \(\|\Delta 1_S\|_2^2=2m\) yields the stated deficit. The packaged finite checks agree with these exact identities but are not used as the infinite proof.

## originality

PASS

The primary 2026 preprint proves the sharp \(\ell^p\) first-difference constant for characteristic functions and states a singleton extremizer, using local Karamata majorization. Its inspected theorem/proof does not state a geometry-dependent quantitative deficit for non-singletons or classify all finite equality cases via a positive margin. Fresh Resultary search returned the audited theorem as the exact matching quantitative refinement.

## value

PASS

The result turns a sharp inequality into a computable stability statement and exact finite equality classification, with the deficit controlled by natural support geometry. Such quantitative nonextremality information is a motivated structural refinement even without claiming the optimal stability constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
