---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The exact Gram projector P_j=I−a_j a_j^T/||a_j||² for A_t rows yields F1=1+t², F2=1+1/(1+t²), F3=t^−2+1+t² and F1<F2,F3 for 0<t≤1/2. For j=1 projected rows t e2 and e3 have nonzero residual only at row2, acceptance probability t²/(1+t²) and geometric mean (1+t²)/t²; the first accepted step reaches e2 exactly. For j=2 the active row1 projected squared norm 1/(1+t²) competes with an inactive projected row3 of squared norm 1; its raw acceptance probability 1/(2+t²), and one accepted step also reaches e2. Independent symbolic rational calculations verified projectors, objectives, rejection probabilities and updates. The asserted unboundedness applies ONLY to raw IID proposals, not accepted iteration complexity.

## originality

PASS

Sun–Qi–Han–Xie already prescribe squared projected-row-norm proposal probabilities, nonzero-residual resampling and a Frobenius singleton-row design criterion, and study convergence in accepted steps. Their actual Algorithm 1/Remark 3.1 does not present this Frobenius-optimal versus alternative raw-proposal divergence with one accepted step each. Earlier Lok–Rebrova subspace-constrained Kaczmarz gives framework, but not the exact regret family. One can derive a rejection penalty from their sampling formula, yet this explicit arbitrarily bad surrogate counterexample is the substantive claim.

## value

PASS

Expected raw attempts can dominate runtime while the accepted-step complexity hides the overhead. This three-dimensional exact counterexample proves that choosing a constraint by a natural residual Frobenius criterion can be arbitrarily suboptimal for a separate, implementation-relevant resource, with a competing legal constraint and identical accepted progress. It does not allege failure of the accepted-iteration convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
