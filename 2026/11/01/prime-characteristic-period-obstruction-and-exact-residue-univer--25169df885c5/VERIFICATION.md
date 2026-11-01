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

Run `python verification/verify.py` and `python verification/verify_uniform.py` in the unpacked directory. Both require only the Python 3 standard library. Their corresponding saved stdout files are `verification/verification_output.txt` and `verification/uniform_output.txt`.

The first program directly simulates 87,400 labelled finite-field vertex configurations in 14 cases and compares the complete pair \((T,\ell)\) with the closed distribution. Cases include distinct shore sizes congruent modulo the field characteristic, zero residues, and all three residue-count regimes. The second program independently evolves all core-state vectors for 1,135 residue patterns: 66,420 states over \(\mathbb F_3\) and 406,875 over \(\mathbb F_5\). It checks transient bounds, divisibility by the claimed universal period, and exclusion of characteristic-square factors. Output ends in `MODULAR_MULTIPARTITE_VERIFY_OK` and `UNIFORM_PERIOD_VERIFY_OK` diagnostics.

The scripts are exhaustive only over their expressly enumerated finite inputs; they cannot establish the infinite statements. The proofs for arbitrary positive shore sizes, prime characteristics and part counts are the factorization, invariant residue-group decomposition, Jordan-length argument and rank-one orbit analysis in RESULT.md. No independent audit was performed.
