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

The claim is proved analytically; no finite experiment is used as an infinite proof.

The core rank check is exact. For a Kraus-rank-
\(r\) channel with Stinespring isometry \(V\), the operator \(V^\dagger(P\otimes I_r)V\) has rank at most \(r\). If \(r<d\), its kernel contains a unit vector. The corresponding output has zero overlap with the rank-one target projector \(P\), hence orthogonal support and trace-norm distance exactly \(2\). This also covers the boundary between approximation and impossibility: every tolerance strictly below the maximal state distance forces \(r\ge d\).

Sharpness was checked by the explicit exact-replacer Kraus family \(K_j=|G\rangle\langle j|\), whose Choi rank is \(d\). For the fermionic application, a pure \(m\)-mode bath has dimension \(2^m\), while an \(N\)-mode system has dimension \(2^N\); therefore \(m\ge N\).

No claim is made that an \(N\)-mode bath can satisfy the locality and Hamiltonian restrictions of the recent cooling construction. The external scientific inputs used are only the construction's stated architecture and the standard equivalence between Kraus rank and minimal Stinespring environment dimension.
