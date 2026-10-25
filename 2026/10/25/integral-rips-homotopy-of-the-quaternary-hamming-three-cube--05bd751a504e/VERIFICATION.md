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

# Reproduction and scope

Run `python3 verify.py` from this directory with Python 3 (standard library). No remote services, stored face files, mathematical packages, or precomputed matching certificates are required.

The standalone program checks all Hamming-distance pairs, the 508 maximal facets (12 coordinate planes, 64 radius-one balls, 432 parity tetrahedra), exactly 830,101 faces including the empty face, the 414,848 augmented acyclic-matching pairs, 405 unmatched three-dimensional faces, and every one of the 6,539,456 directed Hasse incidences using complete topological sorting. Expected terminal line: `VERIFY_OK`.

The proof of the 81-circle scale-one stage follows separately from 48 coordinate tetrahedra intersecting only at vertices, with each collapsed to a three-edge tree: \(48\cdot3-64+1=81\). Scales zero and three are immediate from the integer Hamming metric. The finite executable does not prove a formula for other alphabet sizes, nor does it provide an independent external audit.
