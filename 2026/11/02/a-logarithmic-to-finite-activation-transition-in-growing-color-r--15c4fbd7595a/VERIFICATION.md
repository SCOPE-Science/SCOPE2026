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

For t existing vertices, unchosen parents retain unit weight; total weight S_{t-1}=t+c sum_{j<t}j^alpha, so exact activation conditional probability p_t=(t-I_{t-1})/S_{t-1}. Conditioning yields mean and variance recursions, with negative feedback coefficient (1-1/S); independent finite Markov transition masses through n=250 stayed normalized to 2.22e-16. For alpha<=1, Lambda=sum t/S diverges with power/log rate and correction sum E I/S =o(Lambda). Bounded-increment martingale strong law and triangular array CLT (predictable quadratic variation ~Lambda; Lindeberg) prove a.s. count, Gaussian and variance. For alpha>1 summable expected hazards gives finitely many first selections. Expected late count asymptotic equals sum q_t; pair-probability bound <=q_s q_t and Bonferroni yield last-activation sharp tail and power moment cutoff. Conditional eternal-star survival yields infinite product. Finite program matches full-history recursions only, not infinite proof.

## originality

PASS

Best-of-knowledge originality limited to the final stated novel assertion, not the model, known general machinery or prior exact identities. Primary texts were materially compared for actual logical implication. Accessible published-research semantic search did not establish implication-equivalent coverage; residual risks are explicitly retained. Earlier model/method results are explicitly credited.

## value

PASS

The activated-parent count measures structural branching diversity and the time to the last newly activated branch, natural observables not determined by single-color marginals. The universal alpha=1 trichotomy, central-limit scales, positive star probability and sharp late-activation tail identify a substantive boundary in a growing reinforced graph family, rather than arbitrary finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
