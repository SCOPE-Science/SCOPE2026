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

The standalone `verify.py` constructs all weak-composition cells in dimensions two and three for unordered configurations of three distinct points on a rose. Its first boundary builder uses signs of the two endpoint faces of each ordered coordinate polytope. Its second uses the labeled deletion formula from the integral equivariant rose model and the missing-vertex orientation convention. After accounting for an overall top-cell orientation reversal, all entries match.

The script performs explicit integral column eliminations that leave exactly \(\binom b2\) diagonal entries with magnitude two. Rank tests over characteristics two, three, five, and seven independently corroborate the free ranks and the characteristic-two rank jump. The calculation was run successfully for all cycle ranks \(1\le b\le15\), plus the rank-zero case; its final output was `ALL_CHECKS_OK`. For orientation calibration it independently regenerates the known two-particle formula, obtaining exactly \(b\) diagonal entries of magnitude two.

Run from the extracted package using `python3 verify.py`. This is a bounded reproducibility test: it is not a proof for unbounded cycle rank. The general theorem follows from the explicit integral cell-boundary analysis in `RESULT.md`. Borel–Moore, not ordinary singular, homology is calculated. No independent mathematical audit has been performed.
