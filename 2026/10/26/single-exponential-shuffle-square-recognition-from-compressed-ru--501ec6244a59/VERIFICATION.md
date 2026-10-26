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

The bundled `verify.py` implements three logically separate descriptions: direct enumeration of equal subsequences by position subsets; enumeration of per-run counts; and independent symbolic linear-equality/exact-degree-graph tests. Their decisions agree for all 5,327 words over the binary alphabet through length 10 and over the ternary alphabet through length 7. A case with 117-bit run lengths checks that the count representation need not expand the string. Run with `python3 verify.py`; observed output: `RLE_SHUFFLE_REDUCTION_PASS words= 5327 max_binary_length=10 max_ternary_length=7 huge_run_bits= 117`.

The infinite theorem follows from the exact structural equivalence in the proof, plus the published polynomial-time solution of general capacitated integer b-matching with binary capacities. The checker does not reimplement the latter algorithm and is not a complexity-theoretic proof or an independent audit.
