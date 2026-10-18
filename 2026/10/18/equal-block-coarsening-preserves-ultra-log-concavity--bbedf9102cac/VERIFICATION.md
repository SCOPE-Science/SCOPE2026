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

# Reproducibility and limits

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses `fractions.Fraction` and `math.factorial` to check, exactly and without floating-point tolerance, 4,620 factorial-weight inequalities, 31,680 finite-support ULC-block inequalities, and 17,380 componentwise cross-pair inequalities, for 53,680 sampled exact tests. It also tests strictness when neighboring block probabilities are positive.

The executable is included in the same package as this document. These finite checks are **supporting diagnostics**; they do not prove the claims for all indices, all block widths, or all ULC input distributions. Those universal conclusions follow from the analytic two-factor cross-pair argument in RESULT.md. No unsupported computation, inaccessible certificate, or unperformed independent audit is claimed.
