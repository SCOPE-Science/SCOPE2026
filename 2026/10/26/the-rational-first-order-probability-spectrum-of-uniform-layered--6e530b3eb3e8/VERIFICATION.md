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

# Verification notes

The theorem is proved in `RESULT.md`. Its essential infinite steps are (1) first-order bidirectional interpretation of the layered permutation and its binary cut word, (2) rationality by the regular-language generating function and the previously established first-order convergence law, (3) pairwise and self-nonoverlap of the explicit `001`-prefixed marker family, (4) invertible switching of the earliest marker, and (5) exponentially decreasing probability of no occurrence in independent disjoint windows.

`checker.py` is a standalone Python 3 program requiring no nonstandard packages. Run `python checker.py` in a directory containing that file. A successful run prints:

`LAYERED_RATIONAL_EXACT_OK 22147 code_families 18 q_tested [2, 3, 4, 5]`

The checker tests the marker self/cross-overlap condition for sizes through 18 markers, enumerates the exact uniform cut-word/layered-permutation bijection through 12 vertices, and checks finite first-marker count equality for 2, 3, 4 and 5 markers across a range of word lengths. Finite checks neither establish an infinite asymptotic theorem nor independently establish historical priority. The argument also uses the cited earlier logical convergence theorem; it is not re-proved here.

The named separate 2026 manuscript on limit-probability density was not available for full textual comparison. Whether it or other existing literature already contains the sharper exact rational spectrum remains a priority limitation. No independent audit was performed.
