---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The input is a mixture of two product states and has Xu's Eq. (12) form in the normalized independent Alice basis {|0⟩,|u⟩}. The different operation basis has dual rows (1,−4/3) and (0,5/3), which give the stated rank-one operators. Direct rational multiplication gives the unnormalized second Alice block σ with trace 1769/2601, normalization Z=659/867 and output second-block probability 1769/2636. For a state classical on Bob, I is the entropy of the Alice marginal minus the average Alice conditional entropy, since the entropy of the Bob weights cancels. Both input conditionals and the first output conditional are pure; the stated three trace-one discriminants therefore give the displayed entropy calculation. Independent rational interval reproduction (independent_check.py) reconstructed the matrices and enclosures using integer square roots and explicit bounds on the atanh-series tail, establishing 1/30<Δ_nats<1/20. A separate high-precision evaluation of the entropy formula gives Δ=0.05728010640002332764… bits; decimals are not the strict certificate. The finite example proves the Eq. (21) infimum is negative and refutes universal Eq. (22). A one-dimensional subsystem gives I=0 throughout, so 2×2 is the smallest dimension in which this violation can occur. The sum effect has eigenvalues 5 and 5/9, so dividing the Kraus operators by sqrt(5) gives a physical success branch; its conditioning, not deterministic channel evolution, is decisive. Frozen code inspected, not executed.

## originality

PASS

The supported distinct claim is the exact, separable zero-oblique-discord, two-qubit violation of Xu's specific universal conjecture, not the general possibility that probabilistic operations can change correlations. The exact conjecture and map were checked in the cited preprint. The nearest inspected filtering paper and catalogue counterexample do not cover this normalized bipartite operation and witness. This is not a comprehensive priority finding.

## value

PASS

An exact, low-dimensional and separable counterexample settles a stated universal conjecture and shows that even at a zero-oblique-discord input the proposed information-theoretic quantity can be strictly negative. The positive certified margin makes this a counterexample to the intended normalized operation, rather than a floating-point or trace-convention artifact. Its value does not depend on uniqueness or optimality of the witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
