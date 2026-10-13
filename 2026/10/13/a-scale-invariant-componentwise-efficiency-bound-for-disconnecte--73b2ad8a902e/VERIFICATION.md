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
The symbolic argument was checked directly against the source coefficient decompositions. Under exact detailed balance, an interacting pair has potential/social coefficient ratio \(p_ip_j/(p_i+p_j)\), and a player-specific term has ratio \(p_i\). The no-cross-edge assumption makes both objectives additive over interaction components.

The bundled `verify.py` checks representative arithmetic consequences: invariance of each component ratio under positive scaling; the two-disconnected-pair example in which the global source coefficient expression grows as \(2C\) while the component certificate stays \(2\); and the normalization \(c_k=1/M_k\) for several explicit component vectors. These computations are sanity checks, not substitutes for the general proof.

Limits: the verification does not cover approximate \(\alpha>0\) games, signed component costs, or cross-component interactions. It does not establish that the coefficient certificate equals the actual price of stability.
