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

# Verification of the exact density-seven enumerator

The included `verify.py` uses only Python's standard library. It recomputes the rational expressions for the two disjoint cones from the proof, then checks by **exact integer-polynomial multiplication** that their sum equals the claimed rational function. This cross-product equality verifies a polynomial identity in the formal indeterminate, and hence all infinitely many series coefficients (it is not based on finite experimental matching).

The same program independently checks all \(75,582\) binary words with exactly seven ones at lengths seven through eighteen, testing all factors directly and verifying the gap criterion in each case. An independent five-offset cone enumeration checks coefficients for lengths seven through twenty-nine. The actual successful output is included as `verification_output.txt`.

The proof of the cone split, rational summation and word-count bijection appears in `RESULT.md`; the code does not by itself prove the translation from prefix normality to the cone. It verifies the critical algebra and supplies finite diagnostic checks. No result at other densities is claimed. The verification is self-review only; independent mathematical or publication-priority review has not been performed.
