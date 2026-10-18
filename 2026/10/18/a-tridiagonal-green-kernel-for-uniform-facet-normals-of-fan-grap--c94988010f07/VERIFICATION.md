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

# Verification of the finite covariance calculation

Run `python3 verify_fan_facets.py` with Python 3 standard library. The program enumerates every \(\{-1,0,1\}\)-valued vector on a path with up to nine vertices, checks all Lipschitz edge inequalities, and constructs the tight-edge graph including its hub. Connectedness is verified by an explicit graph traversal. Therefore it does not assume the local zero-run characterization being tested.

For each of eight sizes \(m=2,\ldots,9\), exact rational arithmetic compares every computed second moment against the proposed Green-kernel expression and independently inverts the covariance by Gauss–Jordan elimination. The inverse is checked for strictly negative adjacent entries, for vanishing nonadjacent entries, and for its explicit diagonal formula. All eight complete finite tests passed.

The finite tests are not an exhaustive check for unbounded dimensions. The proof for every \(m\ge3\) appears in `RESULT.md`. The bulk limit follows analytically from the characteristic roots. No independent scientific audit has been performed.
