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

# Verification and reproducibility

The core theorem is an infinite all-parameter statement proved by the nine pair-colour support calculation and the unlimited three-pebble strategy in `RESULT.md`. The direct finite checker `verify.py` is an independent corroboration of this critical support lemma, not a substitute for its proof.

The checker builds six affine geometries and one Paley-type Hadamard design, validates all block intersections and pair-of-points counts, then computes the actual third-vertex colour-pair support for every ordered vertex pair. It confirms uniformity among the nine first/second colours, equality of all support tables inside the two-per-class family and inside the at-least-three family, and different tables between them. It tests the exact existence of two-block covers. The last two example families include designs that differ in rank and block-intersection parameters.

To reproduce: run `python3 verify.py` in the package directory. Exact stdout from the successful check is `verification_output.txt`.

The calculation covers seven finite examples only; no finite enumeration alone certifies all designs or historical novelty. Independent audit has not been performed.
