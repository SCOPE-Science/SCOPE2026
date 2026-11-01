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
# Verification of the crown-graph theorem

Run `python3 VERIFY_CROWN.py` with Python 3.8 or later and standard-library modules only. The verifier compares independently enumerated induced-subgraph two-independence faces with the proposed simplex cover for each integer n from 3 through 6; calculates reduced boundary ranks over characteristics 2, 3 and 5; and checks the signed Lefschetz character under every automorphism of the form (permutation, class exchange). It prints `CROWN_TWO_INDEPENDENCE_NERVE_CHARACTER_FINITE_CHECKS_OK` upon success.

Recorded verified finite values: \(n=3\) has 6,15,14,3 faces by dimension and rank-one H2; \(n=4\) has 8,28,32,8 faces and rank-three H2; \(n=5\) has 10,45,60,20,2 faces and rank-six H2; \(n=6\) has 12,66,100,45,12,2 faces and rank-ten H2. The automorphism checks number 12, 48, 240 and 1440 respectively.

The universal proof is the pair of simplicial-nerve reductions in RESULT.md. The finite tests cannot prove any statement for arbitrarily large n, nor the universal quotient contractibility or integral module isomorphism; those follow from the explicit all-n equivariant cover and integral graph chain complex.
