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

The faithful order-q action has multiplier minus one invertible modulo p, so it is fixed-point-free on the nonidentity cyclic kernel. Projection to the prime quotient shows every nonkernel subgroup has a kernel intersection P_i and a complement coset, with exactly p to the a-minus-i conjugates at level i. If two q-containing subgroups are incomparable, a common q-subgroup would force containment because the kernel subgroups form a chain; their intersection is therefore the smaller kernel part. Were they permutable, their product would be a subgroup whose order contains q squared, impossible inside the group. Thus permutability is exactly comparability. Counting contained lower-level subgroups and one supergroup at each higher level gives the partner count and the displayed relative-degree formula; every kernel subgroup is normal and has degree one. Independent arithmetic recomputation reproduced the formula values for the four verifier parameter families, while the frozen verifier checks set-product permutability directly.

## originality

PASS

Lazorec–Tărnăuceanu compute relative subgroup commutativity degrees for families with a prime kernel and cyclic prime-power complement, including the one-nonnormal-class Frobenius direction. Their full primary text does not cover the reversed growth direction with a cyclic prime-power kernel and prime complement, whose subgroup lattice has nonnormal Frobenius subgroups at every kernel level. Resultary searches returned the audited theorem and related elementary-abelian or cyclic-subgroup variants, but no prior theorem implying the full displayed relative function.

## value

PASS

The relative subgroup commutativity function is an established invariant, and this theorem resolves it on an infinite metacyclic Frobenius family whose subgroup lattice is materially richer than the previously computed prime-kernel direction. The comparability criterion is a reusable structural lemma and the resulting exact function is a natural complete classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
