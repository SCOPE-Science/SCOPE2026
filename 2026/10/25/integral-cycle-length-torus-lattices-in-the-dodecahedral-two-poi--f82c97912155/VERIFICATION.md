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

The standalone `verify.py` reconstructs the 20-vertex graph and checks isomorphism with \(G(10,2)\). The unordered two-point cubical chain ranks are \((190,540,375)\). Exact boundary tests establish \(\partial_1\partial_2=0\); the rank of the second boundary is at least \(339\) by two exact finite-field reductions.

The verifier enumerates all \(1168\) simple cycles and \(823\) vertex-disjoint cycle pairs; checks every corresponding integral product-torus boundary; constructs the 36 disjoint-pentagon cycles; and checks a 36-by-36 integer determinant equal to \(-1\). This certifies the integral basis by primitivity plus the rational rank bound. All twelve length-pair coordinate matrices are reconstructed in the entire 375-dimensional chain group; exact Smith normal forms give the quotient groups in `RESULT.md`.

For reproducibility run `python verify.py` with `requirements.txt`. The verifier is a complete finite calculation for this one graph. The graph-configuration deformation retraction is a standard external theorem and is not proved by the program. No other graph family, additional particle numbers, or independent review is certified.
