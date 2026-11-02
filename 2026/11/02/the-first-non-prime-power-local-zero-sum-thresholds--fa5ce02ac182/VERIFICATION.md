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

# Verification instructions

Run `python3 verify.py` with Python 3 and no nonstandard packages. Expected output starts with `VERIFY_OK`, and gives \(3944\) admissible-prefix nodes, maximal bad length \(12\), and a residue-count histogram whose last nonempty index is \(12\).

The enumerator uses mathematical exactness: for each allowed unit residue, its state consists of seven sets of residues modulo \(36\). Induction on sequence length shows these are precisely the sums of subsequences with \(0,1,\ldots,6\) selected terms. It visits all sorted sequences with a leading \(1\) and all legal extensions; normalized bad sequences must appear in its search tree. The pruning condition is hereditary, so skipping those subtrees cannot hide a longer counterexample. No arbitrary search depth or numerical tolerance is used.

The script additionally checks that the target gcd class consists exactly of \(\{6,30\}\), is preserved by unit multiplication, and that a concrete twelve-entry witness avoids it in *every* nonempty subsequence length. An unrelated implementation using 36-bit masks independently reproduced the maximal depth and node count.

The theorem is finite and specific to \(n=6\); the verifier is an exact exhaustive check, not a statement about general composite moduli. Independent audit has not been performed.
