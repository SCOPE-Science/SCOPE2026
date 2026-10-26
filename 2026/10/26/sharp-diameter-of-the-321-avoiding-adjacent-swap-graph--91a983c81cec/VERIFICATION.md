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

# Reproduction and limits

The included `verify_catalan_diameter.py` script needs Python 3.8+ with only the standard library. Execute `python3 verify_catalan_diameter.py`. It enumerates all 321-avoiding permutations through length eight, constructs the allowed adjacent swaps, derives lower-cover and join-irreducible masks, tests their rank identities, and conducts exhaustive BFS from every vertex. It checks every pairwise graph distance against the asserted ideal-coordinate Hamming distance and the corresponding parity-sharp diameter.

Expected vertex counts for sizes one through eight: `1, 2, 5, 14, 42, 132, 429, 1430`. Expected diameters: `0, 1, 4, 7, 12, 17, 24, 31`. Successful execution prints `VERIFY_OK`.

The computational check has finite scope. The all-size conclusion is established by the mathematical proof, including the weak-order semilattice metric lemma, inversion bound, uniqueness of even-size maximizer and construction of extremal pairs. No independently reviewed certificate is asserted.
