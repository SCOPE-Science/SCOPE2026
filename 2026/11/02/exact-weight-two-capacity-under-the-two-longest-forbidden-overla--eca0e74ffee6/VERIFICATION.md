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

The cyclic-rotation orbits of two-marker supports are indexed by shorter separation d. Their periods are n for d<n/2 and n/2 for antipodal d=n/2. In a single orbit, rotations by one or two correspond to forbidden overlap lengths n−1,n−2, so any chosen phases must have cyclic distance≥3, giving floor(P_d/3). The construction selects phases r=3j in each orbit; its proof splits shifted-prefix/suffix tests by whether zero, one, or two support markers are dropped and rules out cross-orbit violations, including even antipodal ties and self-pairs. Independent direct pairwise checking confirmed constructed code sizes and both overlap constraints for every n=4..50. This supports the all-n orbit argument but cannot prove it by enumeration.

## originality

PASS

Blackburn et al (2022/2023) prove unrestricted-alphabet overlap code bounds and constructions; Yazdi et al (2017) WMU primer codes and balanced composition. Neither broad theorem exactly determines this sparse weight-two optimum; the natural rotation-orbit argument supplies matching upper and lower bounds.

## value

PASS

A sharp infinite-family fixed-composition synchronization-code capacity with an attaining construction and a genuine antipodal parity correction, not obtainable from generic unrestricted overlap bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
