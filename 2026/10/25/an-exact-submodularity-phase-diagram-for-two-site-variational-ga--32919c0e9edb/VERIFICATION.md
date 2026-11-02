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

I independently formed the four Nyström matrices and symbolic inverse-matrix combination M=I+(I+K)^−1−(I+Q1)^−1−(I+Q2)^−1. Its normalized symmetric/antisymmetric eigenvalues simplify exactly to 2A_+ and −2A_- as stated. Symbolic differentiation reproduces dC/dtau=r²*tau*((1−r^4)*tau²+(r²+3)*tau+(r²+1))/(H+ H- D)>0 and C(0)=0. Positive semidefinite nested Nyström increments and logdet(I+X)<=tr(X) show monotonicity for all responses. The independent exact counterexample gives Gamma=1/36+(1/2)log(20/27)=−0.1222745184; weak-r expansion follows from coefficients.

## originality

PASS

Best-of-knowledge claim is not established by the sources actually recovered: An exact singleton gain and monotonicity do not determine the sign of Gamma=F({1})+F({2})−F(empty)−F({1,2}); this exact quadratic sign classification is therefore not a renamed consequence of mutual information submodularity. Priority is qualified by incomplete full-text access.

## value

PASS

Diminishing returns is a precise condition for greedy guarantees; the exact smallest nontrivial response-dependent phase diagram and robust opposite-sign weak-correlation counterexamples distinguish this objective from Gaussian mutual information. Natural motivated structural counterexample, not a claimed general large-kernel classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
