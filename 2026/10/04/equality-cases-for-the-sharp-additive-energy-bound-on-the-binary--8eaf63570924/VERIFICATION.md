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

The proof was checked line by line for the exact domain \(A\subseteq\{0,1\}^d\) with addition in \(\mathbb Z^d\), including the last-coordinate energy decomposition, equality in Cauchy--Schwarz, the sharp scalar equality cases, the difference-multiplicity rigidity lemma, and the converse count.

`verify_extremizers.py` is a supplementary exact finite check. It enumerates all nonempty subsets through \(d=4\), computes energy with integer pair-sum counts, independently recognizes proper affine Boolean cubes, and requires exact agreement. Its stored output is `verification_output.txt` and ends in `VERIFY_OK`.

Finite verification is not an infinite proof. The all-dimensional conclusion rests on the induction and rigidity argument in `RESULT.md`. The originality conclusion is literature-dependent and retains the residual risks recorded in `AUDIT.json`.
