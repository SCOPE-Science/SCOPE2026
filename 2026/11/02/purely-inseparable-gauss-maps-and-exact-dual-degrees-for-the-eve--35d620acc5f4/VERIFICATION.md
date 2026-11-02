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
# Verification notes

The standalone `check_gauss.py` is included with the research files and depends only on Python's standard library. Execute `python3 check_gauss.py` and check its final output is `VERIFY_OK`. It expands \(f'= -B^{r-1}\) in selected characteristics, computes integer gcd relations and genus/delta identities, and prints sample \(q\deg C^\vee=Nq^2\) values. These are finite consistency checks; the field-degree argument and valuations in `RESULT.md` are the actual general proof.

The original paper's stated genus \((q^2-1)q^n/2\) is independently reproduced by subtracting all cusp delta-invariants from the arithmetic genus. We have not independently checked the dual's singularities, nor has an independent mathematical review been carried out.
