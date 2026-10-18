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

Run `python3 check_palindromes.py` in the directory containing this file. Standard Python 3 is sufficient.

The script constructs all \(2^{16}=65536\) local pairing choices on the binary order-five de Bruijn digraph and checks the complete \(32\)-edge orbit criterion. Separately, it backtracks over unused five-bit edges in a direct Euler-tour search and tests cyclic length-six palindrome strings, rather than trusting the local pairing labels. The two histograms must agree and equal `{'A': 512, 'AB': 256, 'B': 512, 'none': 768}`; the output reports `ORDER5_PALINDROME_PROFILE_PASS` when all assertions succeed.

Both searches are exhaustive at order five. Neither code path proves or simulates arbitrary larger orders; the all-order parity and pair statement follows from the local-permutation proof in `RESULT.md`. There is no independent audit, and no claim that the finite certificate settles untested distributions at other orders.
