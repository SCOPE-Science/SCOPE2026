---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

One exact replay is via binary digits, avoiding exceptional dyadic points: a uniform point of either half has a fixed first bit with an iid fair suffix. In a half, contraction prepends another copy of the current first bit and expansion deletes a copy. The run length of that first bit minus one is the shell depth; at entrance its law is P(K=k)=2^(−k−1). On crossing, the unrevealed suffix after the new first bit is again independent fair, even conditional on the previous shell history and waiting time. Thus the hitting probability of −1 from k is 1 for inward or zero drift and (v/u)^(k+1) for outward probability u>v. Averaging over K gives v/(2u−v), which equals ρ=(1−Δ)/(1+3Δ) on the favored half. The other half returns with certainty. Multiplying the conditional probabilities at successive crossings gives N=2G+s, with a geometric number of successful round trips, and at equality p=q every next crossing is certain. The geometric moments give 2ρ/(1−ρ)=(1−Δ)/(2Δ) on the favored side and one more elsewhere. Log ρ∼−4Δ gives the rate-2 limit for ΔN. On the original probability-one strong-law event for the map choices, removing the finitely many steps before the last crossing does not change the drift; translating depth to endpoint distance proves both logarithmic rates without assuming iid choices after conditioning on no future crossing. Read VERIFICATION.md and the two implementations in check.py; the 96 exact finite comparisons are frozen reports, not executed here or used to prove infinite behavior.

## originality

PASS

The distinct supported contribution relative to the earlier inspected literature is the biased all-time crossing law, parity and near-fair scaling from uniform-half starts, not the maps, partitions or gambler’s-ruin formula. The strongest Resultary match is materially equivalent on the crossing law (for both starts via the reset), and has broader results on other observables. It has a later documented catalogue publication date, so it is not evidence that the frozen claim was previously established. This is an evidence-bounded finding, not a claim of unique historical priority.

## value

PASS

Total alternations are a natural measure of escape and persistence for this endpoint-intermittent pair, not a selected finite-time statistic. The exact biased renewal law locates the transition from finitely many alternations to almost-sure recurrent crossing, and its parameter scaling quantifies how trapping emerges. This useful exact fact was not given by the earlier fair-choice limit laws. Its scope does not include quenched initial points or the last-crossing time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
