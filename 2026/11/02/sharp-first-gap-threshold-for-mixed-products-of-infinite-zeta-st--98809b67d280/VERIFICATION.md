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
Run `python3 number_theory_gap_verifier.py` from the directory containing this file. It uses only Python's standard library and checks exact rational comparison inequalities plus 29 numerical examples \(2\le q\le30\). The expected final output is `VERIFY_OK cases=29 rational_inequalities=7 all_strict=True`.

## Proof verification limits
The general result is supplied by the explicit analytical proof in `RESULT.md`. A finite numerical sample does not establish the infinite quantifiers. The source-dependent inputs are exactly the stated infinite-index correspondence, gap description and endpoint formulas from Li--Yang (arXiv:2610.29100v1). The rational inequalities are proved symbolically in that document; the code provides arithmetic cross-checks. Independent mathematical audit has not been performed.
