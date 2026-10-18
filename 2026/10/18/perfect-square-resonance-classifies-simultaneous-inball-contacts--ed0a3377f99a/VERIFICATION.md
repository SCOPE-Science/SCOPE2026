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

The accompanying `check_contact_resonance.py` uses only Python's standard library. Run `python3 check_contact_resonance.py` from this directory; no dependency installation, network resource or special data file is required.

The checker reconstructs integer parameter vectors for 431 permitted contact sets in dimensions 2–24. It certifies 9,605 comparisons between square-root-normalized facet distances by rational upper/lower bounds computed from integer square roots (with denominator scale \(10^{45}\)); verifies strict discrete concavity of the engineered cumulative slack sequence, positivity of all reconstructed increments and exact telescoping; and verifies the dimension-four witness with two simultaneously tangent upper cardinalities. An exact arithmetic argument, not the test range, establishes the general necessity and sufficiency.

The source theorem underlying the facet inequalities is Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, Theorem 2.3(c). The earliest identified supporting public source, Behrend et al., *Partial permutohedra*, arXiv:2207.14253, first appeared 2022-07-28 and is classified primarily under MSC2020 52B05. The new proof is self-contained once the published facet system is accepted.

Scientific limits: integer parameters with first parameter at least two, and Euclidean metric in original coordinate space. Finite exact-arithmetic tests do not certify all dimensions. Independent mathematical validation has not been performed.
