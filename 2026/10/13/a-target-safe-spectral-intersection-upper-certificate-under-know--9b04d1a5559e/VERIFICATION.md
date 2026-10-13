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

The proof is analytic; no finite numerical experiment or external certificate is used to establish the theorem.

For each competitor \(j\neq k\), membership in the chosen spectral subspace of \(M_k-M_j\) gives exactly the score inequality required by the fixed tie rule: strict positivity when \(j\prec k\), and nonnegativity when \(k\prec j\). Because the witness lies in the intersection of all these subspaces, all inequalities hold simultaneously, so the predicted label is \(k\).

If \(p_k=\langle U\psi|P_k|U\psi\rangle>0\), orthogonal projection gives the normalized vector \(P_kU|\psi\rangle/\sqrt{p_k}\). Its overlap with \(U|\psi\rangle\) is exactly \(\sqrt{p_k}\); unitary pullback preserves the overlap, hence the source fidelity distance is \(1-\sqrt{p_k}\).

The projector \(P_k\) is determined by the known POVM, so the probability \(p_k\) is obtainable from the derived binary readout \(\{P_k,I-P_k\}\) allowed by the source upper-bound access model.

Limits checked: the theorem is conditional on \(p_k>0\); a zero target-safe intersection or zero overlap makes the certificate vacuous. No claim is made that the intersection contains every target-class state or that the bound equals the optimal targeted radius.
