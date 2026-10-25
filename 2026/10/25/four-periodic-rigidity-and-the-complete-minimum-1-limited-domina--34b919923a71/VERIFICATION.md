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

# Reproducible verification

Run `python verify.py` using Python 3.8 or later; the program uses only the standard library. The checker was executed directly from the accompanying file and returned:

`VERIFY_OK exhaustive_n=3..9 dp_n=3..60 explicit_n=3..60`

For \(3\le n\le9\), the checker constructs the full cubic Möbius ladder on \(2n\) fixed labelled vertices, enumerates every candidate subset of sizes \(n\) through the formula's proposed optimum, independently checks each vertex's dominator degree, and compares the entire exact minimum-set family against the prescribed rung words. Sizes below \(n\) are ruled out by the rigorously proved crossing-edge inequality rather than by combinatorial enumeration.

For \(3\le n\le60\), an independent four-state rung dynamic program enforces both local vertex constraints with an explicit row-switching twist at the closing seam. It checks the exact optimum value and number of minimizers without using the predicted closed form in its recurrence. All explicit candidate minimum sets are also constructed and checked directly on the original graph throughout this range.

The program's finite outputs cannot establish any all-integer identity by themselves. The universal proof and necessary/sufficient structural classification are given in `RESULT.md`; no external prover or independent review was used.
