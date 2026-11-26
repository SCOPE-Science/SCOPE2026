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

Until the first private arrival the two agents value the same items, so the absolute difference of their common-good counts is a pointwise parity lower bound. Give each private good to its valuer. With private counts A and B, and with X the common-good count of agent 1 minus that of agent 2, zero envy is exactly the feasibility interval −A≤X≤B. Alternation can keep X in {−1,0} or {0,1} throughout: pick the side made feasible by the first private arrival. That interval only expands, so this single allocation realizes the parity bound before the arrival and zero thereafter. Neutrals change neither count; no private arrival leaves a parity-only stream, and an initially private good gives a zero optimum. The pointwise bound proves both the unweighted and nonnegatively weighted claims; choosing the alternation phase by a preliminary scan costs O(m) overall. In the displayed pair of streams, a wrong assignment of the first common good leaves the other agent envying by one for every round, irrespective of future choices. With a correct first choice, giving later goods to their valuers attains cost 1. The two indistinguishable first choices give the deterministic lower and upper bound m. For a randomized rule with first-choice probability p, the two fixed inputs have expected costs at least 1+(m−1)p and 1+(m−1)(1−p); a fair coin followed by assigning to valuers attains their smallest possible maximum. Both optima equal 1. This is expected minimax only on that input pair, for m≥2, with an oblivious adversary. The source DP code tests cumulative values on finitely many instances; the argument above, not those tests, establishes simultaneous pointwise optimality for all horizons. The frozen checker is documented in VERIFICATION.md; no replay of that source script was needed.

## originality

PASS

The identical-binary parity behavior is already covered by pointwise greedy optimality. The supported distinct contribution is the heterogeneous binary extension (one allocation reaching the exact minimum at all prefixes, including after the first private arrival), together with the exact unknown-future two-input competitive gap for cumulative maximum envy. The strongest inspected primary and catalogue statements do not give this combination or imply either distinct conclusion. This is a best-of-knowledge comparison, not a priority certification.

## value

PASS

The prefix criterion is stronger than minimizing the sum, and unlike a general dynamic program the theorem identifies exactly what future information matters: the first private good's valuer determines a single balancing phase that makes all subsequent envy vanish. This yields a linear-time exact allocation and robustness to arbitrary nonnegative prefix weights. The indistinguishable-stream construction shows that loss of this small piece of foresight can produce unbounded multiplicative cost even under an oblivious choice of input, separating tractability from online information requirements without overstating the exact unrestricted ratio.

The dated certificate retains the supplied scientific assessment, sources and limitations.
