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

The proof was replayed symbolically from the stated hypotheses.

For each \(i\), quotienting by \(N_i\) sends every \(a_{ij}\in N_i\) to \(e\). Because \(a_{ji}\notin N_i\), each incoming parameter survives in \(G/N_i\). This establishes \(G\models\Diamond\theta_i\).

For \(i\ne j\), the formula \(\theta_i\) contains \(a_{ij}=e\), while \(\theta_j\) contains \(a_{ij}\ne e\). Since homomorphisms preserve \(e\), any future of a \(\theta_i\)-world still has \(a_{ij}=e\), so no such future satisfies \(\theta_j\). Substituting \(\theta_i,\theta_j\) into the displayed \(\mathsf{S4.3}\) axiom \(.3\) makes its antecedent true and consequent false.

The finite-abelian corollary was checked against the standard subgroup-lattice criterion: a nontrivial finite abelian group has a chain of subgroups exactly when it is cyclic of prime-power order. For \((C_p)^n\), the number of one-dimensional subspaces is \((p^n-1)/(p-1)\).

No finite experiment is used to infer an infinite statement. No independent audit or formal proof assistant verification has been performed.
