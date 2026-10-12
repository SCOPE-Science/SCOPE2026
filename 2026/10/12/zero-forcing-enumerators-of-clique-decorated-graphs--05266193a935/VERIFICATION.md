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

# Verification of the clique-decorated zero-forcing identity

The structural proof in `RESULT.md` is the complete, unrestricted mathematical argument. In particular, its four steps identify the initial-white-pair obstruction, activate all effective roots, simulate legal base forces, and project any successful decorated forcing process back to the base. Counting local alternatives supplies every coefficient with no assumption of connectedness.

To corroborate the proof by finite computation, execute `python3 verify.py` in the directory containing `verify.py`. The script independently constructs each decorated adjacency list, enumerates every initial colored subset, computes iterative ordinary zero-forcing closure, compares this closure against the structural test, and separately constructs polynomial coefficients by local weight multiplication. It checks all 75 labeled base graphs of sizes one through four and 221 uniform/nonuniform clique-size profiles with total decorated order at most 12. The resulting 624,824 direct subset comparisons and 1,230 coefficient comparisons passed; details are preserved in `verification_output.txt`.

Finite exhaustive experiments on the stated small graphs are finite results only; they neither establish an unrestricted graph theorem nor settle possible priority conflicts. The unrestricted quantifiers follow from the combinatorial proof. The proof does not cover private cliques of order one; the path on four vertices supplies a direct counterexample to substituting size one into the transformation. Independent verification is not claimed.
