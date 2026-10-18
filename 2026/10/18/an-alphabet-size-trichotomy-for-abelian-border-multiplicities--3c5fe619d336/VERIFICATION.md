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
# Verification

Run `python3 artifacts/verify.py` in the folder containing RESULT.md. It independently compares direct complete enumeration of word borders, a vector-valued mirrored-pair dynamic program, and first-return renewal probabilities for each alphabet size 2, 3, 4 through length eight. It separately checks the published ternary count of Abelian-unbordered words through length ten, plus rational return-count identities.

The bundled program completed successfully with the message `PASS: 24 exact word enumerations, renewal PGFs, and published ternary anchors`. These are finite consistency tests. The proof for all lengths, all fixed alphabets and all three limiting laws is in RESULT.md; verification does not infer an infinite theorem from finite data. The Tauberian and Fourier-asymptotic steps are mathematical arguments and have not been independently audited.
