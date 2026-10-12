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

The universal proof is symbolic. It first derives the full automorphism normal form from the defining brackets, then counts ranks of \(\phi-I\) after partitioning \((a,h)\) by the vanishing pattern of \(a-1\), \(h-1\), \(ah-1\), and \(a^2h-1\). For odd fields the only multi-collision outside the identity is \((a,h)=(-1,1)\). The identity-diagonal stratum reduces to an explicit lower-triangular \(3\times3\) rank calculation.

`verify.py` exhaustively enumerates the automorphism parameters for \(q=3,5,7\). It checks the full fixed-dimension distribution, the group-order sum, and Burnside average \(5\). For \(q=3\) it also constructs actual element-orbits and verifies that they coincide with the five intrinsic layers. A successful replay ends with `VERIFY_OK`.

The computational replay is deliberately finite and uses prime fields only. It is not evidence for all extension fields by itself; arbitrary odd prime powers are covered by the symbolic parameter and rank argument. Characteristic \(2\) is outside the theorem.
