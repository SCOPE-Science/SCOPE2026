---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For balanced P_s with s in (0,1), the source-prescribed centered ordinary Sinkhorn derivative is s². Direct independent symbolic differentiation of the Xu-Chen two-state fixed-mu recurrence reconstructs the displayed 2x2 Jacobian, trace (a²+a−1+(a+3)s²)/(1+a)² and determinant s²/(1+a)², a=sqrt(2mu). Jury inequalities 1±trace+det>0 and det<1 hold for 0<a<sqrt(2). Unique positive solution of G_s(a)=a²+(1−s)²a−(1−s)(1+3s)=0 satisfies a<=1 and gives positive repeated eigenvalue q=s/(1+a). Determinant lower bound for a<a_* and negative characteristic value at q_* for a>a_* prove uniqueness of global spectral minimum in permitted range; G_s(1/s−1) factors as ((s−1)(s+1)²(2s−1))/s² to give exact one-quarter comparison. Independently checked the symbolic Jacobian, determinant, Schur identities, rate-minimax and switch factors with SymPy, and inspected the source nonlinear finite-difference verifier without claiming to have run it; no global rate or critical pure-geometric prefactor asserted.

## originality

PASS

Original Xu-Chen Acc-Sinkhorn algorithm and its global O(1/k²) homotopy theory are prior. The final theorem is a sharp local fixed-parameter spectral-minimax phase diagram for its exact two-state recurrence on positive balanced two-atom kernels. Gao et al analyze standard Sinkhorn and a distinct algorithm; Thibault et al analyze SOR overrelaxation. No inspected source covers the same fixed-parameter update and 1/4 switch.

## value

PASS

The result identifies an exact minimal 2x2 problem where a purported acceleration method can remain slower than ordinary Sinkhorn even with optimal tuning. The unique optimizer and transition in the nontrivial singular mode make a motivated, method-specific design and diagnostic result. It is not claimed to beat SOR, optimize wall-clock cost or describe arbitrary matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
