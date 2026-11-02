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

# Reproducibility

From this package's extracted folder run `python verify.py`. The script uses only Python's standard library and `fractions.Fraction`; no external dependency is needed. It verifies all 125 rational configurations from the five-value grid on the reciprocal three-vertex path and all 625 such configurations on a nonreciprocal reversible four-vertex path. The test also evaluates exact mixed second differences in an ordered chamber and proves by rational calculation that the balanced directed triangle changes its arithmetic opinion sum by -1/27 from the explicit state (0,1/3,2/3). It confirms unequal cycle products 1 and 1/8. These are diagnostics for the algebraic derivation in RESULT.md, not exhaustive tests of all real configurations or arbitrary graph orders. The proof of universality is mathematical rather than experimental.

No independent audit or external certification has been performed.
