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
# Exact checks and limits

Run `python3 verify.py` with Python 3.9 or newer. It uses only the standard library. Successful output is exactly:

`VERIFY_OK: independent dual-ray enumeration, lattice indices, and canonical index for n=2..512`

The checker reconstructs the three-column determinants and the vertex-difference character cone for each tested integer, enumerates the primitive rays from all cross products of the four character generators, validates the complete dual-facet incidence, recomputes rank-two lattice indices, and tests the rational canonical support character with minimal Cartier index.

The tests cover the integer range \(2\le n\le512\) and are finite checks, not an exhaustive proof for all integers. The general proof in `RESULT.md` establishes the universal classification using exact symbolic formulas for arbitrary \(n\). All geometric statements assume \(p\mid n\) and an algebraically closed field. There is no independent mathematical audit.
