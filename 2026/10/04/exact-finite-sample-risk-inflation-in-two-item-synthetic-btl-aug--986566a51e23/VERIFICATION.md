---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The accumulated empirical win probability is a bounded martingale. Its conditional variance increment and the identity for \(E[P(1-P)]\) give the exact recurrence \(h_{t+1}=h_t(1-1/(m(t+1)^2))\), hence the finite product for MSE and the conditional no-self-correction formula. Bounded martingale convergence gives the limit, Euler's sine product evaluates the infinite product, and the Taylor series gives the strict finite-m correction to \(\pi^2/6\). Independent exact-rational state propagation and long-product numerical checks agree with the symbolic proof.

## originality

PASS

The broad accumulation literature already establishes reciprocal-square variance accumulation and the asymptotic \(\pi^2/6\) pathway; those are not treated as new. The audited claim instead gives an exact finite-m Bernoulli product law, exact infinite-round sine-product value, strict finite-m correction and conditional no-self-correction identity in the two-item BTL specialization. The complete accessible Dey--Donoho text is asymptotic/general and does not give this finite Bernoulli law. Only the introductory/model portions of the very recent Jin--Yu preprint were obtained before a permitted later full-text retrieval was safety-blocked; that inaccessible remainder is retained as a residual risk rather than used to assert whole-document noncoverage.

## value

PASS

Two-item BTL is the exact Bernoulli boundary model of a current iterative-ranking augmentation problem. The theorem quantifies every finite round and finite batch, separates inherited initial error from synthetic dispersion, and identifies the exact finite-batch correction to the known asymptotic pi^2/6 pathway. That is a natural benchmark for the broader model-collapse theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
