---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For progression-free integer A with <=2 unordered distinct-pair representations per sum, Parseval of P^2 separates diagonal, unique and double-collision terms, giving ||P||_4^4=2m²-m+8Σcos(phi). Two distinct four-point collision supports on m<=5 would overlap in >=3 points; alternative completions of three ordered points force a three-term AP, so R<=1 and all cosine terms can be minimized. For A={0,1,3,4,9,10}, independent complete pair-sum enumeration gives exactly 3 collisions and unique rank-two phase relation. The exact identity cos(a)+cos(g)+cos(a+g)=2cos x cos y+2cos²x−1 has min −3/2, giving minimum 66−12=54; independent unimodular phase witness and direct convolution both give 54, rather than unattainable formal value 42.

## originality

PASS

One-relation L4 minimizations and Sidon/B2 representation multiplicity are known, but the simultaneous collision-phase compatibility condition, the sharp no-frustration boundary at m=5, and explicit minimal six-point obstructed support with exact value 54 do not follow from Neuwirth's one-collision result. Distinct from other published Fourier support moment results in Resultary (triangular multivariate aperture, four-point geometries). Best-of-knowledge with stated specialized merit-factor literature risk.

## value

PASS

Determines the first possible cardinality at which additive collision phases cannot all be optimized independently, a natural structural barrier in sparse Fourier L4/unconditionality optimization. A sharp small-support threshold plus explicit frustrated witness is reusable even without full six-point classification; not an arbitrary unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
