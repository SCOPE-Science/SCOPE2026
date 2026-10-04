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

The final claim was verified by a direct proof, with no numerical or finite-enumeration step.

For the direction from \(f\) to \(f^q\), the check isolates the only delicate point: an \(f\)-ergodic measure need not be \(f^q\)-ergodic. Its \(f^q\)-ergodic components form a finite cyclic family and therefore have equal \(f^q\)-entropy; the common value is \(q h_\mu(f)\).

For the reverse direction, the compact set \(\Lambda=\bigcup_{j=0}^{q-1}f^j(K)\) was checked to be \(f\)-invariant, and the phase average \(\mu=q^{-1}\sum_j f_*^j\nu\) was checked directly to be \(f\)-ergodic by testing every \(f\)-invariant measurable set. Entropy affinity and the standard power law then give \(h_\mu(f)=h_\nu(f^q)/q\).

The proof depends on invertibility in the reverse topological-entropy step, because \(f^j\) is used as a conjugacy from \(K\) onto \(f^j(K)\). No statement for general non-invertible maps is verified here.
