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

The primal unit ball has exactly the 16 oriented edge molecules because every nonedge pair has a length-two geodesic. Total unimodularity of the reduced incidence constraints makes dual vertices integral; independent reconstruction gives exactly 26 extreme dual functionals and 128 norming pairs. The repository certificate contains 416 exact rational dual certificates, one for every primal/dual operator-norm evaluation; this audit parsed the actual certificate and verified every coefficient identity and that every dual weight sum is at most two, proving \(\|T\|\le2v(T)\). Independently reconstructing the explicit witness gives numerical radius one and operator norm two. Thus the index is exactly one half.

## originality

PASS

The closest primary paper gives the complete two-dimensional/free-space-of-three-points formula and proves that value one half is equivalent to an equilateral three-point metric. It does not cover the four-dimensional free space over the five-point wheel. Targeted searches and related published results did not locate a theorem implying the wheel value.

## value

PASS

The five-point wheel is a canonical smallest non-complete wheel, and its exact index gives a concrete boundary to the complete three-point rigidity theorem. The exact certificate also provides a reproducible benchmark for higher-dimensional Lipschitz-free numerical-index computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
