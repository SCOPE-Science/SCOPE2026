---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independent likelihood calculation: among the eight ordered sign vectors only (+,-,-) and its reverse can affect the loss, since a coalition containing the largest weight and any other weight strictly wins under both weightings. Under the positive state the difference of the two exceptional likelihoods is ((1+4yz)x-y-z)/2, and under the negative state the two likelihoods exchange roles. Thus Bayes follows the largest signal iff x>(y+z)/(1+4yz), whereas effort weights do so iff x>y+z (with the specified fair tie at equality). The effort tie loses half the likelihood difference, xyz; a Bayesian tie has zero loss independent of the action chosen. For s=y+z<=1/2 the open gap is less than 2syz<=s^3/2; for s>=1/2 it is less than (1/2-y)(1/2-z)<=(1-s)^2/4. The tie case is below 1/32. At (1/2-1/N,1/4,1/4), N>10, the gap is 1/16-5/(8N). For <=2 signals both weights are strictly increasing in effort and the effort ranking suffices. The proof, not the finite grid, covers all permitted real efforts.

## originality

PASS

The effort model and log-odds comparator are known. The distinct supported claim is the exact fixed-effort regret, including its linear-weight tie surface, and the sharp nonattained 1/16 frontier for the first loss-producing committee size. No equivalent or dominating statement was established by the inspected evidence.

## value

PASS

Effort weighting is motivated by existing governance models, and two voters cannot distinguish the effort and Bayes orderings. At the first committee size where aggregation can be suboptimal, the exact regret and its 6.25-point worst-case frontier distinguish a potentially material statistical loss from strategic incentive effects. The exceptional tie surface and limiting, highly asymmetric profile matter to evaluating the rule, rather than being an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
