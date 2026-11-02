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

# Reproducibility and limits

Run `python CHECK_MONOMIAL.py` and `python CHECK_FIXED.py` with Python 3.8+ and its standard library. The scripts emit the recorded outputs in `CHECK_MONOMIAL.out` and `CHECK_FIXED.out` respectively, ending in `VERIFY_OK`.

`CHECK_MONOMIAL.py` enumerates every structure matrix over \(\mathbb F_2\) and \(\mathbb F_3\) in dimensions two and three, applies Gaussian elimination to select invertible matrices, verifies automorphisms by direct multiplication of basis squares, and checks the calculated expectation bound and Burnside orbit integrality. Observed class numbers are \(4,33,7,249\) for \((q,n)=(2,2),(2,3),(3,2),(3,3)\).

`CHECK_FIXED.py` independently enumerates every matrix entry assignment for each monomial map in those same four cases. Its direct fixed-equation tally exactly matches a separate index-orbit calculation for every map, including singular matrices as required by the proof's intermediate step.

The checkers cover finite cases, not the infinite limiting statement, and use only prime fields. The written proof supplies the arbitrary-prime-power theorem and all asymptotic estimates; numerical agreement is supporting evidence, not a certification of historical originality or an independent proof audit.
