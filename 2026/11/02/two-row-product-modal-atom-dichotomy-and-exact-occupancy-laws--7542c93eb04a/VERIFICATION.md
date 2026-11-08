---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Depth-one propositional/vertical formulas identify each realized ordered pair of colours; if the top-row support E differs from its transpose, a depth-two horizontal diamond picks one row, hence 2|E| atoms. If E=E^T, matching ordered-pair labels across rows defines a modal bisimulation giving |E| atoms. The asymmetric support upper bound is sharply attained, explaining nonmonotonicity. Standard surjective occupancy yields exactly t!S(m,t) words per fixed t-type support, and transpose-invariant supports are counted by coefficients of (1+z)^q(1+z^2)^[q(q-1)/2]. The first missing ordered type gives the stated positive leading expectation correction. Independent direct refinement on all 526 nonempty supports for q=2,3 confirmed the atom-count dichotomy.

## originality

PASS

Aghamov et al (arxiv:2606.31852, EPTCS 447) analyze modal axioms for neighborhood full products, while Shapirovsky–Sliusarev arxiv:2404.01670 study qualitative local tabularity. Neither accessible inspected theorem supplies the precise two-row S5 frame support-vs-transpose atom dichotomy, the depth-two sharpness, or exact occupancy probability law. Earlier specialized bisimulation-count literature remains a plausible risk.

## value

PASS

Sharp finite-modal atoms and depth, the nonmonotone column phenomenon, an exact occupancy distribution, and a positive leading asymptotic correction are concrete structural and probabilistic invariants for a natural S5 product frame; they go beyond a standard qualitative finite-model property.

The dated certificate retains the supplied scientific assessment, sources and limitations.
