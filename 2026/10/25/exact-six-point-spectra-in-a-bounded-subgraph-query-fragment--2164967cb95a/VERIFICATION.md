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

The embedded script `support/verify_spectrum_fragment.py` enumerates all labeled simple graphs on one through four vertices and verifies the six positive maximum-density values, the representative automorphism counts, and the reciprocal critical exponents. Its output is `VERIFICATION_OK`.

The asymptotic part is proved analytically: the fixed-subgraph threshold theorem gives deterministic occurrence limits away from the six reciprocal densities; the six witness patterns are strictly balanced; and their Poisson limits have means \(1/|\operatorname{Aut}(H)|\). At each critical exponent, the parity sentence reduces to one pattern event or its complement, yielding the probabilities stated in `RESULT.md`. Outside those exponents all six generators have deterministic zero-one limits.

The finite script is a reproducibility check, not an infinite proof certificate. Independent audit and independent validation have not been performed.
