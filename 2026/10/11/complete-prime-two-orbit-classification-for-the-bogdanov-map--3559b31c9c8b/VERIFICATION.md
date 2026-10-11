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

The self-contained proof in `RESULT.md` proves the global real classification by reversible sum/difference equations for a least-period-two pair. The machine-checkable supplement `verify_period2.py` requires Python 3 and SymPy (`python -m pip install sympy`, if absent); run `python verify_period2.py`. The script verifies the exact polynomial identities, all three invariant prime-two algebraic curves by iterating the map symbolically, direct prime-two test points and the complete involution at the common parameter point. All comparisons are exact rational or symbolic operations, not floating-point trajectory statistics. The algorithm does not enumerate infinitely many periodic points and is not a substitute for the written completeness proof.

The published primary full texts compared include Djellit–Boukemara (2004) and Dénes–Makay (2011). The founding Arrowsmith–Cartwright–Lansbury–Place paper (1993) was accessible in bibliographic metadata and abstract, but its complete text was unavailable; complete historical-priority verification remains a limitation.
