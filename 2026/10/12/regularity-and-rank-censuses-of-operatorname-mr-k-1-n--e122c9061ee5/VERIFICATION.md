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

Verified the full inverse-face continuity definition, including empty domain, singleton image and target-edge preimages. If no target center, a map has all singleton fibers or exactly one source edge fiber; if target center is present, the rank-two edge and rank>=3 centered-star cases exhaust possibilities. Rank enumeration yields R_n, and the regularity obstruction is precisely center as singleton fiber mapping to a leaf while at least one other target leaf is used. Idempotence requires fixing the entire image, giving E_n=(1+z)^(n+1)+nz(1+z)^(n-1)+nz. Independent full partial-map enumeration for n=2,3,4,5 gave totals (36,185,1278,10857), nonregular (4,36,288,2500), idempotents (14,31,68,149). Additionally, all candidate regular witnesses were exhausted for n=2,3 with zero mismatches. The proof, not the small enumerations, establishes every n>=3.

## originality

PASS

The 2026 Margolis–Rhodes work introduces exactly this inverse-face monoid and gives general regular-J-class structure and explicit path/cycle enumerations; the read abstract does not establish the submitted full star rank, nonregular and idempotent polynomials. Forward partial endomorphisms on stars are distinct because they preserve edges forward, while here inverse images of all faces must be simplices. Resultary semantic query found no direct same rank enumerators; absolute priority remains unproved. The 2026 monoid paper full text could not be inspected, so potential implicit star specialization remains a named residual risk.

## value

PASS

The star is the first branching tree family, and an entire rank-refined full transformation monoid with a sharp regularity obstruction is a natural structural baseline for the new inverse-face construction. The idempotent census and rank distribution are exact families, not an arbitrary one-off count; different from forward-endomorphism censuses and path/cycle enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
