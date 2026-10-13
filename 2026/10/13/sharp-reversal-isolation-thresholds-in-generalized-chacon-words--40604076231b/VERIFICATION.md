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

# Verification of sharp generalized Chacon reversal-isolation cutoffs

Run `python3 verify.py` with `verify.py` and `a3_certificate.json` in the same directory. Both files use only the Python 3 standard library; there are no network, compilation, or third-party dependencies.

The verified output is:

```text
VERIFY_OK gap_recursion_parameters=13 localized_a3_factors_n19=37 a3_palindromes_n18=1 sampled_cutoffs=9 context_bounds=97
```

The program independently reconstructs the defining finite words, confirms the stated gap recurrence for the displayed parameter sample, and compares the complete list of \(37\) distinct length-\(19\) factors from \(W_3\) to the embedded finite certificate. It tests every reversal among these factors and confirms that the explicit length-\(18\) palindrome occurs. The proof in `RESULT.md` establishes that the \(37\)-factor list is exhaustive for the infinite word at that length because \(|W_2|=21\). Thus the exceptional \(a=3\) subclaim is not an inference from a finite prefix alone.

For \(a\ge4\), the parameter sample and checked algebraic context maxima are supplementary consistency checks. The complete infinite proof is the direct structural induction and the four bounds in `RESULT.md`; the checker by itself is not an exhaustive proof over arbitrary parameters. The literature-priority assessment remains subject to the limitations in `REVIEW.md`.
