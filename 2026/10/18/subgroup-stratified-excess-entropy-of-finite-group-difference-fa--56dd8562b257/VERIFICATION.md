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

The repaired finite-block identity follows by conditioning the n+k inputs on their deterministic differences: there are k disjoint chains and each chain's posterior is its product-law weight across simultaneous left translates. The true lift ensures a positive denominator, change of reference lift permutes the probabilities, and a chain with no output contributes q_1=H(mu). Bounded conditional entropy gives the entropy rate. On each half, the strong law identifies the exact boundary orbit, since starting with gX_j changes all reconstructed letters by left translation and hence changes the limiting law to mu(g^-1 x). The halves use disjoint iid tails given the boundary; translating a tail and its boundary by an element of K_mu preserves law and differences, so the two conditional laws depend only on the orbit vector. Conditional independence given that vector and recovery from both halves yield H(C); uniformity within each orbit gives the log term. This works with zeros, nonnormal subgroups and singleton group. The set of limits follows from closed symmetry constraints, finiteness of the subgroup lattice, and mixing with a full-support law of distinct orbit masses to realize each subgroup. The order-two transposition subgroup example in S3 gives k times the entropy of masses (1/2,1/3,1/6). Replay: repaired RESULT.md, all three proof sections. Frozen VERIFICATION.md and verify.py were inspected, not run; the reported 38 numerical finite-block comparisons are not the infinite proof.

## originality

PASS

The supported distinct claim is the arbitrary finite-group excess entropy and complete subgroup-indexed set of perturbation limits, with the finite posterior formula, not the already known biased-binary reconstruction and discontinuity. The closest indexed additive binary result and inspected group-related factor literature do not supply the nonnormal left-action classification.

## value

PASS

The theorem computes a natural infinite-observation information observable and ties its loss exactly to an identifiable group symmetry, including with degenerate laws. The subgroup cluster classification gives a precise discontinuity diagram rather than only a generic jump or an isolated binary example; nonnormal subgroups genuinely exercise the side of the action.

The dated certificate retains the supplied scientific assessment, sources and limitations.
