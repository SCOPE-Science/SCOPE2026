---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Specialization of Schäfer–Anandkumar defining exact CGD formula to unconstrained zero-sum f=x^TCy, g=−f yields x+=(I+η²CC^T)^−1(x−ηCy), y+=(I+η²C^TC)^−1(y+ηC^Tx), every η>0. SVD gives on each σ>0 singular plane 1/(1+q²)[[1,−q],[q,1]] with q=ησ, singular norm factor (1+q²)^−1/2 and rotation arctan q. Orthogonal projections onto ker C^T and ker C are invariant; all positive singular modes vanish exponentially so iterates converge to the Euclidean projection onto Nash set for arbitrary rectangular C. Exact distance²=sum_j(a_j²+b_j²)/(1+η²σ_j²)^k; sharp worst-mode at smallest nonzero σ. C=0 is identity; approximate inner solves excluded. Independently checked rank-deficient rectangular numeric singular modes and nullspace invariants.

## originality

PASS

The defining CGD NeurIPS 2019 Schäfer–Anandkumar article contains the matrix inverse and local exponential stability, plus a full-rank/scalar bilinear example. It does not in the inspected defining sections state the arbitrary-rank Nash-manifold orthogonal-projection selection or the exact singular-value-by-singular-value distance law. Anagnostides–Penna arXiv:2010.03211 primarily covers historical OGDA schemes and frequency-domain bilinear stability, different update. Generic resolvent spectral facts make the derivation natural but do not constitute a sourced same-CGD closed-form projection theorem; Resultary/primary searches found no decisive domination.

## value

PASS

The update has a continuum of equilibria for rank-deficient games; which equilibrium is selected is a meaningful implicit-bias question not addressed by a unique-equilibrium contraction bound. The exact global all-η, all-rank selection and sharp modal rate quantify stronger-interaction stability and diagnose cost/convergence tradeoffs without demanding a nonlinear generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
