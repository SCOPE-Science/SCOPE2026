---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Das's Lemma 2.2 implies that an odd-k cycle must contain a prime at most k, so it suffices to start from all primes p<=k. From those starts the dynamics stays in the finite interval 2 through 2k+2, making the census exhaustive. The inspected C++ verifier constructs the exact largest-prime-factor table through 41472, scans every odd k through 20735 and every prime start, canonicalizes directed cycles, rejects any earlier k with at least 36 cycles, and verifies exactly 36 cycles at 20735 with period histogram 4:6, 6:14, 8:10, 10:5, 12:1. An independent implementation reproduced the same strict record sequence, final count and histogram.

## originality

PASS

Das proves eventual periodicity and finiteness and reports a computation only through k=5000, where the maximum loop count is 14 at k=4479; the paper then asks whether loop counts are unbounded. Dubickas studies a broader bounded-iteration class but does not state the exact 20735 record in the inspected material. The targeted Resultary search for the map definition, k=20735 and 36 loops returned the audited finding as the direct exact hit and no earlier equivalent census.

## value

PASS

This exact census advances a numerical frontier explicitly tied to Das's open unboundedness question: it more than doubles the published attainable loop count from 14 to 36 and records the complete optimum-cycle period profile. The strict record sequence and exact cycle list provide a reusable benchmark for future arithmetic-dynamics searches even though they do not prove unboundedness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
