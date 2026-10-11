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
# Reproducibility and proof limits

Run `python3 artifacts/verify.py` from the package root using the Python standard library. The program reconstructs the cubic group algebra, verifies the complete complex-coefficient sixth-moment identity by exact integer coefficient comparison, checks the seven residue multiplicities and total collision energy, and evaluates sample data and seven equality witnesses. The output is `VERIFY_OK exact_complex_polynomial=PASS cubic_fibers=7 energy=111 samples=250 extremizers=7`.

The exact group-algebra verification establishes the algebraic expansion for arbitrary complex inputs once the formal conjugation is interpreted as specified. It does not prove the global polynomial inequality by enumeration. That step is proved directly by the nonnegative cyclic square identity, Cauchy--Schwarz, AM--GM, and equality analysis in RESULT.md. The numerical tests are finite corroboration, not certificates of optimality or uniqueness. The literature comparison is selective; no exhaustive priority certificate or independent audit is claimed.
