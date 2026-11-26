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

On an S5 cluster, every contingency value is constant. XOR with a cluster-constant bit preserves variation, so an outer contingency on a normal form tests only the local linear parity. Induction gives existence even for nested formulas and infinite clusters. On singletons with valuations 0 and e_i one recovers the constant and k local coefficients. On a cluster with an affine basis for the full span every nonzero parity varies, giving the sum T of all modal coefficients. For span s-perp only s among the nonzero parities is constant, so testing that hyperplane recovers T XOR b_s; testing all but one gives the omitted b_s from T. This establishes uniqueness and the fixed teaching family of size D=k+2^k using at most k+1 worlds. With at most k worlds the span is proper, so the number of varying parity indicators 2^k-2^(k-dim L) is even; the all-modal XOR vanishes. Conversely a combination vanishing on all such examples has zero constant and local parts by the singletons, and b_s=T for every s by the hyperplanes, making its relation space exactly one-dimensional. The full-span cluster violates the relation. For k=1 the hyperplane is the zero space and the omitted-test construction needs no hyperplane examples. Fewer than D labels give fewer than D linear constraints on a difference and cannot identify any target. That proves the class counts, both cutoff directions and optimality over the full stipulated fragment.

## originality

PASS

The earlier affine-hull signature result materially covers the model compression upper bound and already gives enough to obtain sharp compression of individual theories in the restricted language. Credit that overlap. The supported distinct claim is the algebra of formula functions for the smaller XOR/contingency basis, its exact dimension and optimal variable-fixed formula teaching, and the one-dimensional loss and explicit separating identity at k worlds. The earlier result counts pointed theories and does not give these formula-space facts.

## value

PASS

The restricted language is a natural precise affine test case for expressive power with a genuinely bundled operator. Its dimension classifies arbitrary syntax, the evaluation-rank loss identifies exactly what small-world testing misses, and one optimal nonadaptive family works for all targets. Counting the model signatures does not answer any of those evaluation-rank questions. The contribution is a structural classification and sharp boundary, not the bare numerical sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
