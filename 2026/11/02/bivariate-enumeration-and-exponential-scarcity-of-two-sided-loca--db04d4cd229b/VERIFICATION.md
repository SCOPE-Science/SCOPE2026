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
# Reproducibility and verification

The complete derivation is given in RESULT.md. To replay the finite part using a fresh Python 3 installation (no nonstandard packages), run `python3 verify_cycle_partitions.py` in a directory containing that file.

The program performs these independently implemented checks: direct graph adjacency tests for every labelled vertex subset for \(5\le n\le16\); cyclic forbidden-factor tests; determinant expansion of the two matrices by permutations and polynomial arithmetic; coefficient extraction using the respective polynomial recurrence; equality of the two methods for every coefficient of the size variable. A successful check terminates with `VERIFY_OK n=5..16 all labelled 2^n subsets; determinants via permutations; independent neighborhood and forbidden-word checks`.

The local word theorem, rational generating functions and strict dominant-root comparison are proved for all \(n\ge5\) in RESULT.md. Finite enumeration verifies but cannot replace those arguments. Approximate roots are rounded numerical consequences, not proof certificates. Independent audit has not been performed.
