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
# Reproduction of finite checks

Use Python 3 with only the standard library. In the folder containing the files run:

`python3 verify.py`

`python3 verify_all_relations.py`

The first program exhaustively enumerates \((n+1)^n\) upward-flat threshold-row presentations for each \(n=1,\ldots,6\); its final marker is `VERIFY_OK`. It tests direct worldwise semantics, the adjacent-input normal form, each rank count, and the upward-flat fibre cardinalities. The second enumerates all \(2^{n^2}\) raw binary relations for each \(n=1,\ldots,4\); its final marker is `RAW_VERIFY_OK`. It checks operation equality, unique minimum-arrow representatives, and unrestricted relation-fibre multiplicities. These finite checks do not establish the universal quantifier \(\forall n\); that follows from the symbolic proof in RESULT.md. The checks do not establish mathematical originality or constitute any external audit.
