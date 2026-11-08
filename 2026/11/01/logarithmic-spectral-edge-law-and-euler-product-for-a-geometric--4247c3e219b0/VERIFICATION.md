---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For real q>=5 the recurrence has a_n+c_n=1, P_n(1)=1 and positive reversible Jacobi weights alpha_n=sqrt(a_(n-1)c_n). Parity reorder yields J=[0 A*;A 0], with A upper bidiagonal beta_0^2=1-q^-1, beta_k^2=(1-q^-2k)(1-q^-(2k+1)), gamma_k=q^-(2k+3/2). The diagonal is uniformly bounded below above the shift norm, hence A invertible; D=I-A*A is positive trace-class. Direct expansion yields D_00=q^-1 and D_kk=(1+q^-1)q^-2k-(q+q^-1)q^-4k (k>=1), whose trace is (q²+q-1)/(q(q²-1)); triangular determinant of A gives prod_(n>=1)(1-q^-n). P_n(±1)=(±1)^n and h(2k)~constant q^k exclude endpoint atoms, while nonzero Jacobi off-diagonals give simplicity and cyclicity. The rescaling D=W^1/2 C W^1/2 with W_kk=q^-2k has C a compact perturbation of a constant tridiagonal with essential spectrum [(1-q^-1/2)^2,(1+q^-1/2)^2]; its kernel is exactly span(q^-k sqrt(h(2k))) and is isolated. Rank-one interlacing bounds positive eigenvalues between constants times q^-2j and yields N_q(epsilon)=log(1/epsilon)/(2log q)+O_q(1). I independently checked exact rational finite traces for q=5,7,11 and finite Fredholm product factors; these support but do not prove the infinite spectral assertions.

## originality

PASS

Best-of-knowledge originality of precisely the stated additional conclusion, not of its acknowledged classical object or method. Logarithmic spectral edge law and Euler product for a geometric random-walk polynomial hypergroup is not directly implied by the strongest inspected primary theorem; exact comparisons and accessible source passages appear in the four structured checks. Inaccessible sources are identified as residual risks, not counted as negative whole-document evidence.

## value

PASS

The already-discovered geometric polynomial hypergroup has a natural unresolved quantitative spectral question: how its infinite discrete support accumulates at ±1. An exact edge-count coefficient plus global rational spectral-deficit sum and Euler product are useful precisely stated invariants, not an arbitrary tiny finite calculation. The proof introduces a recurrence-specific rank-one comparison, enabling sharp log-scale spectral information beyond qualitative compactness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
