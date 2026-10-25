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

# Reproducibility

Run `python verify_monotone_census.py` and `python verify_jarvis_independently.py` with both files in the same directory. No nonstandard Python packages, external libraries, web services, files from other records, randomness, or approximations are needed. The main checker evaluates all 65536 point subsets, deduplicates exact strict-vertex hulls, exhausts all critical normal rays and open sectors, and verifies generic/non-generic agreement and the complete table. The secondary checker rebuilds the hull collection using gift wrapping and tests 288 nonzero objective vectors in the integer box \([-8,8]^2\) against the exact certificate for every polygon.

Actual run of primary checker: `CERT_OK polygons 2719 diameters [(1, 516), (2, 1686), (3, 516), (4, 1)]` followed by the seven by-vertex strata and `UNIQUE_EXTREMAL` for the eight-vertex polygon. Actual run of secondary checker: `independent hulls 2719`; `independent objective sample consistency 2719`. Both exited successfully. The secondary finite direction sample corroborates rather than establishes objective completeness; the exact ray/sector coverage proof and primary certificate do that. Nothing in these checks amounts to independent scientific auditing or historical priority certification.
