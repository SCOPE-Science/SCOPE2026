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

The package checker was run from the included `verify_gap.py` path using Python 3.13.5 and only standard-library modules. It returned `PASS`; it enumerated 2,596 exponent tuples and verified 2,595 nonminimizers. The candidate divisor ratio was computed exactly as \(62496/12155\). Outward-rounded interval arithmetic enclosed the gap in \((0.1690,0.1691)\), and the lower bound at the cutoff exceeded the exact rational threshold \(10960297/1920000\). The finite search, support-reduction proof, and universal tail bound together establish the stated global minimum.

Limitations: the claim is only for integers with exactly seven distinct prime factors. The code does not prove the unrestricted Robin inequality or the Riemann hypothesis. The referenced notebook in the primary paper was not retrieved; this is recorded as a residual literature risk, not as proof of overlap.

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
