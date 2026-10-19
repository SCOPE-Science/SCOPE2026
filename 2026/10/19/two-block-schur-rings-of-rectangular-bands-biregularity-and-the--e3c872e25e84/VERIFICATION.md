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
# Verification

The standalone `verify.py` was executed from the packaged code path and returned `VERIFY_OK`. It checks direct block-sum multiplication on all nonempty two-colorings of rectangles of sizes \(2\times2\), \(3\times3\), \(3\times4\), and \(4\times4\), compares with the exact graph-theoretic criterion, and tests all color-preserving automorphism orbits for those Schur partitions. It directly checks the \(4\times6\) non-automorphic example.

For the first non-automorphic threshold it enumerates every sequence of six endpoint pairs on four vertices (\(6^6=46656\) possibilities), filters to row degree three, and independently counts the three multiplicity profiles and automorphic status: \(60\) matrices of multiplicities \((3,3)\), \(1080\) of multiplicities \((2,2,1,1)\), and \(720\) of multiplicities \((1,1,1,1,1,1)\). After identifying complements, this certifies the finite integer counts \(968\), \(428\) and \(540\).

Finite computations do not prove any unbounded statement. The general graph criterion, exhaustive type classification and sharp minimality are proved mathematically in the accompanying result. No independent external validation is claimed.
