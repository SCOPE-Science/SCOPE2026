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

The mathematical proof is in `RESULT.md`; `verify.py` is a standalone Python 3 standard-library stress check. Execute `python3 verify.py` from a directory containing that file. Actual execution returned `VERIFY_OK 54007 run-cap/leading-count checks; exact 5-run and 3-run spot checks`.

The exhaustive checks cover all binary length-1-to-13 and ternary length-1-to-9 words with at most seven maximal constant runs, evaluating every permitted parameter among `k=1,2,3`. The checker generates a *set of subsequence strings* before filtering palindromes, preventing multiplicity of embeddings from contaminating the count. It separately checks an exact five-run formula and a three-run extremal formula at positive bounded parameters. The proof, not the finite computation, establishes the infinitely quantified bounds and rigidity. Independent scientific auditing and validation are not performed.
