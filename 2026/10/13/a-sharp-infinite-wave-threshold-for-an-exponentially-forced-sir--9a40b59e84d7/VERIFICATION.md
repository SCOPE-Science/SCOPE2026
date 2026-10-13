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

# Reproduction and boundaries

Execute `python3 verify.py` from the same directory. The program uses only Python's standard library; on successful exact checks it prints `VERIFY_OK`.

The checker reconstructs identities in the polynomial ring \(\mathbb{Q}[a,\gamma,Q,P]\), confirms the forward and inverse transformations of the SIR derivatives after cancellation of common positive factors, verifies the conserved energy derivative, and reproduces the incidence log-slope identity at \(P=1\). It independently checks \(N=\gamma=1\), \(a=1/2\), \(\beta_0=5\), \(S_0=2/5\), \(I_0=1/10\), \(R_0=1/2\), \(Q_0=2\), \(P_0=1\), and \(E>3/2\) by the elementary inequality \(\log2<1\).

Infinite periodicity is **not** inferred from numerical trajectories: it follows from the rigorous regular-level, coercivity, and planar-flow proof in `RESULT.md`. No integration grid, approximate peak count, or test output certifies the unbounded-time behavior. Verification is same-model only; independent assessment has not been performed.
