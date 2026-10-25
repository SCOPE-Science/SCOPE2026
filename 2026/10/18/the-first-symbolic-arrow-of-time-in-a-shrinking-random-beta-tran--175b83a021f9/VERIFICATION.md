---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For finite n>=3, the original shrinking random beta maximal-entropy measure has a finite first-return graph with two excursion paths per length k=2..n and Parry return probability lambda^-k. The ordinary-time digit law is the length-biased stationary suspension of iid blocks b(1-b)^(k-1), each probability q_k/2=lambda^-k. Complement and stationarity identities force reversal symmetry for lengths <=4; rational row elimination gives one-dimensional length-five antisymmetric space with exactly eight nonzero unordered reversal pairs, all of magnitude |Delta|. Direct prefix conditioning yields Delta=(q2-q2²-q3)/(8mu)=-lambda^{-(n+3)}/(2mu)<0; hence TV5=8|Delta|. The characteristic renewal identity implies lambda_n↗2 with n(2-lambda_n)→0 and mu_n→3, giving 2^n TV5→1/6. Independently rebuilt rational length-biased finite-state transition chain for four distinct distributions n=3..6, exactly verified all <=4 reversals, eight five-symbol discrepancies and coefficient. The finite checks do not prove the all-n exponential limit, which is analytic.

## originality

PASS

Jiang–Dajani 2016 introduce exactly the shrinking random beta graph and its original-system Parry maximal-entropy structure, not the reversal asymmetry of the ordinary-time binary branch digit process. Arola-Fernández–Lacasa prove general stationary binary symbols cannot witness irreversibility for m<4, while here the extra complement symmetry extends that universal threshold to 4 and the finite beta family first exhibits it at m=5 with an exact shrinking coefficient.

## value

PASS

Short-word time-arrow detection is a natural observable in symbolic dynamics and nonequilibrium statistics. Establishing its exact shortest detecting length and complete first discrepancy profile, together with a sharp exponential collapse along a prescribed beta family, gives a motivated and usable invariant rather than a formal reparameterization of the old return graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
