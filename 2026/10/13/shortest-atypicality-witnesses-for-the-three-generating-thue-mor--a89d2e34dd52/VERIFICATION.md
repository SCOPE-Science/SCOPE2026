---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The frozen proof's third spelled-out image is wrong: with a mapped to a and b mapped to bab, aabbaab maps to aababbabaabab, agreeing with the frozen binary certificate 0010110100101. The complete corrected RESULT.md fixes the false equality, supplies occurrence offsets and explains a second exact factor bound; the primary minimum values and certificate are unchanged. Independent replay (/workspace/branches/check_thue_morse_factors.py, Python 3) took a different direction from the frozen verifier. In the fixed point, every factor of length at most 13 lies in one or two consecutive length-16 substitution blocks; all four adjacent pairs of block types occur in mu^3(a), so mu^7(a) suffices to cover the full language needed. For each feasible positive image-length pair (r,s) with Ar+Bs within the claimed cap, I cut actual factors in that prefix according to the pattern and recovered only consistent pairs of letter images. The procedure is exhaustive because any feasible witness has such a cut, and conversely any consistent cut determines its two images. I excluded precisely the powers of mu and their output complements. The domains contain 228, 12 and 36 possible assignments; the minima are 13, 8 and 13, and exactly the stated pair and its complement attain each optimum. The direct occurrence offsets for the three chosen images are 29, 20 and 9. All shorter candidates are accounted for; no assertion is made for other atypical words. The frozen verifier and certificate were inspected, not executed.

## originality

PASS

The supported claim after correction is the set of exact shortest lengths and the complete minimizing sets for the three canonical generating patterns, including the genuinely shorter witness for aabab. The source already gives attaining witnesses for abaaba and aabbaab, and their existence at those lengths is not credited as new.

## value

PASS

The three inputs are canonical because they generate the atypical class under variants and factors, not because they happen to make for a small search. Minimum local witness length measures how early the obstruction to global preservation can be demonstrated. Exact lower bounds and complete optimizer pairs answer that question for the full generator set, including a shorter certifiable witness for the first generator. The result does not claim a new theory of all atypical factors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
