---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Read the exact all-dimensional RESULT.md proof and verify.py. The no-jump generator L=iJA-kappa e1e1*/2 is Hurwitz: Re eigenvalue=-kappa|v1|²/(2||v||²) and v1=0 forces zero all coordinates by path recurrence. Therefore Q=int_0^infinity exp(L*t) exp(Lt) dt is unique positive Hermitian Lyapunov solution L*Q+QL=-I. For i<=j the proposed Qij=(N+1-j)(i/kappa+(i-1)kappa/(4J²)) if even separation, otherwise -i(N+1-j)/(2J); adjacent bulk affine cancellation and first-site sink boundary cancel every off-diagonal residual, diagonal residual -1. Boundary conventions b_(N+1)=0 complete the proof. For site m the diagonal mean is (N+1-m)(m/kappa+(m-1)kappa/(4J²)); convexity uniquely optimizes at 2J sqrt(m/(m-1)) for m>=2, m1 has no finite optimizer. Fresh independent exact SymPy rational calculations verified the full Lyapunov equality for 24 distinct (N,J,kappa) cases and all tested optima. Finite tests support, not prove, all N.

## originality

PASS

Best-of-knowledge PASS for all-state finite-path Lyapunov matrix and general interior localized optimal rate, with acknowledged pre-existing localized endpoint and N3 formulas. Full primary Zhang et al 2017 and Riberi 2026 are materially read. Neither supplies the displayed matrix on finite uniform paths at arbitrary N and arbitrary initial coherences; generic Lyapunov theory itself is classical.

## value

PASS

The full finite-N integrated survival-time operator handles coherent superpositions, interference and arbitrary density matrices, not merely localized launch. Its closed entries and sharp site-dependent but terminal-length-independent optimal rate solve a natural first-passage and transport design problem. Special endpoint and three-site localized cases are known, not presented as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
