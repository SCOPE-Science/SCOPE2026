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

The forward image of a partial order is extensive, idempotent and additive; equality of the two compositions on singletons is sufficient by union preservation. In /workspace/reproductions/modal.py I independently enumerated the three orientations (including absent edge) of each unordered pair, imposed transitivity, and used sets and repeated simultaneous closure to enumerate orbits. Every seed in every commuting ordered pair is included; 2^n−1 rounds suffice because each nonstable round adds at least one subset. Counts of full triples at n=1,2,3,4 are 2,16,180,960. At n=4: 219 posets, 22735 commuting pairs, orbit histogram at sizes 2,4,…,16 is (48124,102252,107568,59376,29280,12144,4056,960), successful seed size counts are (168,624,168) at sizes 1,2,3, there are zero comparable successes, and the least total strict edge count is 4. The same reproduction evaluated all sixteen displayed words right-to-left for the given witness. No ≤3-world carrier can reach 15 subsets. An automorphism preserving the two named relations and seed commutes with all three unary maps, so in a full orbit it fixes every subset, in particular every singleton. Thus the labelled action is free and gives 960/24=40 classes without quotienting by an operation swap.

## originality

PASS

The checked catalogue and primary sources cover the general closure-complement setting and related commuting-operator counts, but not the sharp finite T0 realization and census of ordered, commuting closure pairs with a fixed generating subset.

## value

PASS

The 14-set single-closure comparison motivates this finite threshold; the commuting and T0 constraints make an admissible full witness nontrivial. The exact whole four-world census, rigidity and least-edge condition are reusable benchmarks for unary generation in finite closure spaces; they are not a selected sample or just a relabeling of the classical bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
