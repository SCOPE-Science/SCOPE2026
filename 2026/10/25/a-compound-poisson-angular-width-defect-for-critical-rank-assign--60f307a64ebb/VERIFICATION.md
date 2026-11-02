---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For a Gaussian matrix centered to the sum-zero tangent hyperplane, loss of a support function is unchanged by centering; the spherical width defect is (D+(G)+D+(-G))/||projected G||. One-sided zero loss exactly means top-k entries form a k-matching; uniform ranks yield (N)_k²/(N²)_k. For k~c sqrt N, top-ranked pair row/column collisions converge to marked Poisson intensity 2c² du dv on 0<u<v<1, giving mean c² per tail. Triple overlaps have vanishing expectation. Gaussian ranked extreme gaps scale as -log v/t_N; density 2v for v yields Exp(rate 2). Deleting weaker cells and inserting next ranked nonconflicting cells give a sandwich for actual k-matching optimization. Top/bottom rank sets couple asymptotically independently, and projected norm/sqrt(N²-1)->1, so total scaled defect tends to compound Poisson intensity 2c², Exp(2) jumps; no-loss atom e^-2c² is proved by collision counts rather than weak convergence. Independent exact enumeration confirmed the one-sided count at N=3,4,5, k<=N.

## originality

PASS

Geometric descriptions of k-matching/assignment polytopes and exponential-cost assignment expectations do not imply a Gaussian spherical *width-loss difference* law under critical k/√N. The main theorem includes a joint two-sided compound Poisson limit, an atom, and the exact finite-N one-sided normal-fan agreement probability. Priority qualified by older assignment-probability literature not wholly inspected.

## value

PASS

A natural random-direction question about the normal fans of two closely related assignment polytopes exhibits a sharp k~sqrt N collision transition and a full non-Gaussian compound-Poisson law; the exact finite normal-fan agreement measure complements the limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
