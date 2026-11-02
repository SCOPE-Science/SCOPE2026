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

Run `python3 checker.py` using Python 3 and its standard library. This reproducible script enumerates \(1^1+2^2+3^3+4^4+5^5+6^6=50,069\) mappings, checks full conditional distribution and factorial moments against separately enumerated occupancy experiments, confirms conditional stochastic ordering and exact covariance identities, and tests the asymptotic scale at three larger sizes. The observed result was `PASS: 241 exact/numerical assertions, 50069 mappings exhaustively enumerated`.

Proof of the unrestricted conclusions is the combinatorial conditioning, occupancy coupling and analytic estimates in RESULT.md. Exhaustive checks stop at six vertices and cannot certify larger cases or priority. The source papers were inspected to the extent explicitly stated in the scientific review; no independent mathematical audit has been performed.
