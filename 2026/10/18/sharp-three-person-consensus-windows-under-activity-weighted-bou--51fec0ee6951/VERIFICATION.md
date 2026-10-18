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

The source file `check.py` is a standalone Python 3 standard-library program. Run `python3 check.py` in the package directory. It uses `fractions.Fraction` and performs 23,670 exact comparisons over rational initial positions, confidence bounds, positive heterogeneous weight triples, the equality thresholds, and the two complementary weight-response formulas. A passing run prints `PASS 23670 exact comparisons`.

For mathematical verification, first derive each unordered selection probability from the source node-first conditional selection rule. The first effective interaction is geometric competition between at most two receptive edges. Its midpoint effect produces either one isolated agent or an all-receptive three-agent system. In the latter case the common opinion mean stays invariant and total quadratic disagreement decreases conditionally by at least a fixed positive fraction, proving almost-sure asymptotic consensus. Finally derive the nonempty and overlap conditions of the two *strict* intervals in the free parameter \(b\), including equality cases at \(c=2/3\) and \(c=3/4\).

The checker does not prove the all-time almost-sure limit by enumeration, and it does not establish novelty or independent external validation. The result is scoped to a three-person fixed-weight maximum-compromise model.
