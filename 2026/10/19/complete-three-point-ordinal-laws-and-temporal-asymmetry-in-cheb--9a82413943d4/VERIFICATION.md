---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The increasing arcsine coordinate h(y)=(1−cos(πy))/2 conjugates degree b to its full-branch folding map. Composition gives folded slopes q and q²; the inverse branches have equal weight and Lebesgue measure is invariant. The affine comparison slopes are distinct on each fine cell, so ties have zero measure. Pairing consecutive affine cells gives the two-point probabilities and the cumulative rising measure at even fine boundaries. For p102, a coarse crossing on even cell j occurs at j/(q−1), also the crossing in even fine cell J=j(q+1); on odd cell j the crossing at (j+1)/(q+1) is the crossing in even fine cell J=(j+1)(q−1). This verifies the key cumulative evaluations, including the endpoint case for odd q. For p012 the preimage count below the middle value is j+1 on the even-cell rising region and j on the odd-cell rising region. Summing these contributions and substituting in the three stationary pair marginals plus normalization yields the six stated masses. Summing absolute differences over the three index-reversal pairs yields the two positive TV formulas and the two leading coefficients. Value reflection is not time reversal (for example odd q is value-symmetric but TV remains positive). Independent exact affine-cell checks for q=2 through 8 agree; replay: python3 /workspace/branches/d802ba63-eb62-4aac-9925-3ac3baef7676/ordinal_law_check.py; corresponding ordinal_law_check.txt is in the same directory. These samples corroborate the all-q derivation and do not replace it. Frozen verifier inspected, not executed.

## originality

PASS

Pass for the combined exact all-degree, all-lag law and temporal TV, not for the logistic special case or the general use of ordinal quantifiers. The strongest retrieved comparisons concern q=2 alone, different branch orientations, or different observables. None supplies the parity-uniform classification.

## value

PASS

These are exact, monotone-coordinate-invariant benchmarks at every integer lag for a natural expanding dynamical family. In particular the parity split distinguishes a value-reflection-symmetric but still temporally asymmetric family, and identifies two different sharp rates' leading constants. This is more than checking forbidden orders or tabulating one slope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
