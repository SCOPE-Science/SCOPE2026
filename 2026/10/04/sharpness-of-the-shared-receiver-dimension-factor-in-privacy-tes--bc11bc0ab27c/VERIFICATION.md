---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Specified partial decoder maps send distinct orthonormal input basis elements to distinct outputs and therefore extend to permutation unitaries in dimension Md, including d<M because (M-1)d>=M-d. The displayed unit range vectors have r=min(M,d) identical summands and all other summands orthogonal, so inner product r/M. The external overlap upper bound ||PQ||<=min(1,d/M), stated explicitly in Wilde abstract, closes equality. Does not assert channel/capacity exponent optimality.

## originality

PASS

Best-of-knowledge, implication-based comparison of exact theorem and primary findings; not a guarantee of globally exhaustive prior art. The prior bound implies ||PQ||<=d/M but not ||PQ||=d/M; constructing matching range vectors proves the missing opposite inequality. Equality under arbitrary M,d could be pre-existing in unchecked appendices.

## value

PASS

Equality for a sharp upper bound explicitly used as a main ingredient in a private-communication strong converse is a motivated extremal calibration. It shows no universal improvement to the receiver dimension factor without additional hypotheses; it does not claim overall converse exponent sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
