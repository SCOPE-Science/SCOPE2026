---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

The finite diagnostic `checker.py` uses only the Python 3 standard library. Run from the artifact directory as `python3 checker.py`. It independently evaluates the relation \(S\,R\,T\) as nonzero bit-mask intersection and forms modal truth sets by successor existence. It checks the tail recurrence, the complementary-parity source support, each singleton-world definition, every coordinate detector, and every world-isolating Boolean formula for orders \(1\) through \(11\), comprising \(4083\) explicit world-isolate tests across those orders.

A logically separate partition-refinement implementation computes modal observational color signatures using the initial parity proposition and sets of successor colors. It confirms that the eventual partition is discrete for orders \(1\) through \(8\). Both checks previously completed with `ALL_CHECKS_OK`.

Finite model checking is not an all-order certificate. Universal correctness is based on the symbolic identity and induction in `RESULT.md`. The exact sharpness of the rank follows from the fact that the zero-generated subalgebra contains only the two constants.

The checked model is the full unrestricted propositional complex algebra. No claim is made that its parity-of-minimum initial valuation is induced by an atomic set-theoretic sentence under principal-downset translation semantics. An independent audit has not been performed.
