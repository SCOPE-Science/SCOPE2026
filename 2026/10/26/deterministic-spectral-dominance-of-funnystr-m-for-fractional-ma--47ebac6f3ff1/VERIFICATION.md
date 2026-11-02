---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Factor N_q(A^p;Omega) as X X^T. Its nonzero eigenvalues are generalized Ritz values of (Omega^T A^(2qp) Omega,Omega^T A^((2q-1)p) Omega). For every nonzero sketch vector, t↦log(w^T A^t w) is convex (second derivative is a weighted log-eigenvalue variance), implying pointwise Rayleigh ratio R_p <= R_1^p for 0<p<1, reversed for p>1. Courant–Fischer yields all k ordered spectral inequalities. N_q(B) lies between 0 and B by an orthogonal-projector factorization; Löwner–Heinz makes both fractional residuals PSD, so nuclear norms equal trace deficits. For diagonal A_L and Omega_L the exact quotient is (u^5+1)/(u+1), yielding E_direct/E_fun∼2L^(1/4).

## originality

PASS

Best-of-knowledge originality: inspected the frozen final theorem and compared mathematical implications with published related sources rather than titles. The cited ingredients and simpler special cases are prior; the claimed additional precise joint law/spectral bound/bridge law/Dyck rigidity/cyclic construction is not established by the inspected results. Unlocated equivalent prior coverage remains an explicit risk.

## value

PASS

A deterministic, same-sketch, all-rank spectral comparison between two commonly used low-rank matrix-function pipelines. The trace residual gap can diverge on explicit 2×2 SPD examples, giving a sharp and actionable distinction between competing approximation procedures beyond empirical performance reports.

The dated certificate retains the supplied scientific assessment, sources and limitations.
