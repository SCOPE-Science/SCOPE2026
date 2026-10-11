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

Run `python3 verify_dyadic_powers.py` using the standalone standard library. The program constructs each source-block budget exactly as a rational fraction for positive powers through \(500\) and output dyadic blocks through index \(20\); it checks that only powers \(1\) and \(5\) differ from the baseline power norm and checks the associated exact rational values. It tests finitely many cases and cannot establish the infinitely quantified result. That result is proved analytically in RESULT.md by the two-source-block decomposition and strict estimates uniform in every positive integer power.

The norm-attaining equality cases follow from the unique maximizing output block and saturation of separate input budgets. Those logical steps were reconstructed and checked, not inferred from a numerical experiment. The original paper's published two-sided bounds were checked against its stated theorem and proof. No claims about independent assessment or priority certification are made.
