---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For binary circular words excluding cyclic 000 and 111, the ten permitted four-grams are arcs of a six-vertex de Bruijn digraph. A profile is realizable exactly when its nonnegative integral circulation has connected positive support. Solving the five independent balance variables gives B(z)=(1+z^6)/[(1-z^2)(1-z^3)^2(1-z^4)(1-z^6)]. The six simple directed cycles have exactly two vertex-disjoint pairs; their positive union contributions are z^6/(1-z^3)^2 and z^6/[(1-z^2)(1-z^4)], yielding C(z) after subtraction of zero. Nonzero genuine poles at the necessary roots imply least quasi-period twelve; pole at 1 gives n^4/5184. Fresh independent direct enumeration compared profile sets and generating-function coefficients for n=1..17.

## originality

PASS

Restricted de Bruijn/Ehrhart methods and generic quasipolynomial degree were known; the exact two-disconnected-family correction and explicit rational function for oriented cyclic length-four multiplicity profiles are not supplied by the inspected antecedents.

## value

PASS

Exact profile capacity answers a natural noiseless read-multiset reconstruction problem with two simultaneous run constraints. It characterizes every feasible observation vector and the exact maximal zero-error code size, not just approximate growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
