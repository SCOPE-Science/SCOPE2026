---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Using the four actual length-21 generator rows of Kawamoto–Kato–Maruta Example 2.1 and alpha^2=alpha+1, a fresh independent GF(4) implementation enumerated all 85 nonzero projective points and 85 planes, without sampling. Hyperplane multiplicities exactly reproduce the printed 1..10 spectrum (2,4,12,12,22,16,6,4,3,4). For n=21,q=4,w=3 the sole exceptional plane residue is 0 mod4: 12 four-planes and 4 eight-planes. Counting every incidence yields (N0,...,N7)=(2,1,16,9,25,23,2,7). Unique depth-one point is (0,0,1,3), with zero generator multiplicity; depth two occurs 16 times. Incidence checksum is 336=16*21. This complete finite enumeration proves the finite claim subject to faithful transcription of the printed matrix, which was directly inspected in the primary rendered article.

## originality

PASS

The primary 2026 article presents the matrix, global hyperplane-weight spectrum, and a witness point of 1-local three-weight behavior, but does not classify all projective points by incident exceptional planes. The global spectrum alone lacks incidence-intersection data and cannot force the histogram or uniqueness. No equivalent exact table was found in targeted mathematical record searches.

## value

PASS

Uniqueness of the motivating 1-local witness, contrast with the 16 two-local centers, and the complete 85-point depth distribution answer natural questions about rigidity and local geometry for a source example introducing a new code invariant. The exact incidence statistic is not derivable from published aggregate weight data alone; a full finite census is an appropriate scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
