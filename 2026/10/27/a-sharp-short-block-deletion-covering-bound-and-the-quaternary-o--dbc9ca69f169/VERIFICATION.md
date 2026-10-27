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

Run `python3 verify.py` with a standard Python 3 interpreter. The checker uses only `fractions`, `itertools`, and `collections` from the standard library.

It enumerates the fifteen equality patterns on four positions in restricted-growth normal form and recomputes every distinct deletion shadow's rational weight sum. Those fifteen computations cover the entire infinite alphabet family by alphabet-relabeling invariance. It additionally checks the symbolic weight-sum formula against direct enumeration for alphabet sizes 2 through 8, then constructs the descendants of all 19 explicitly listed quaternary codewords, confirms that exactly 64 different target words are reached and that their multiplicity distribution is 60 covered once and 4 twice. The recorded exact output is in `verification_output.txt`; successful execution prints `VERIFY_OK`.

The universal lower-bound step is established mathematically in `RESULT.md` from the complete equality-pattern list and symbolic counting identity; checking sizes 2 through 8 is independent corroboration, not the basis for extrapolation. There is no computational claim about all larger alphabets, no use of floating-point optimality gaps, and no external formal certification.
