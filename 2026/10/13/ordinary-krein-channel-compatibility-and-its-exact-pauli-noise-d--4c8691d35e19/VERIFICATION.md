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

The universal classification is proved analytically in `RESULT.md`. With the source's normalization of Choi matrices,
\[
C_{\Xi_\Phi}=(J_A^{\mathsf T}\otimes J_B)C_\Phi.
\]
Both ordinary and twisted complete positivity mean that the corresponding Choi matrices are positive semidefinite. Multiplication by a Hermitian involution cannot preserve positivity on a nonzero negative eigenspace; this forces the original Choi matrix onto the positive eigenspace and hence forces all Kraus operators to intertwine the two fundamental symmetries.

For qubits with \(J=Z\), the explicit Kraus pair
\[
K_0=\operatorname{diag}(1,\overline c),\qquad K_1=\operatorname{diag}(0,\sqrt{1-|c|^2})
\]
is trace preserving and produces exactly the phase-damping map whenever \(|c|\le1\).

The Pauli diamond bound is analytic: a computational-basis input witnesses \(2(q_X+q_Y)\), and an explicit mixture of identity and \(Z\)-conjugation attains this bound by the triangle inequality for differences of quantum channels. The diamond norm is not halved.

The bundled checker verifies the Choi-support/Kraus identities for several complex coherence factors, rules out an \(X\)-only channel under \(J=Z\), and tests the matching Pauli-channel distance witnesses for exact rational probabilities. These finite checks are *not* an infinite-dimensional proof, and the theorem itself is restricted to finite dimensions.

Independent external validation has not been performed.
