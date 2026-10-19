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

# Analytical and exact-arithmetic verification

The proof establishes the safe pair intervals directly from the two forbidden endpoint sets, identifies all possible fourfold-map inverse branches, and computes the exact powers of their nonnegative transfer matrix. It separately checks odd observations and the parameter breakpoints. The countable infinite survivor set follows from the complete finite inverse-branch graph, not from an orbit enumeration.

Run `python verify.py` from this package. This script independently uses exact rational interval preimages under the original doubling map, intersects with the alternating safe sets, and compares their measures to the piecewise formula for rational test widths across all parameter regimes, including equality boundaries. It also verifies representative stated infinite-survivor points over finite forward depths. Successful output: `VERIFY_OK 3165 exact rational comparisons and orbit checks`.

The program's finite rational samples do not certify arbitrary real widths, arbitrary observation lengths or entire infinite orbits. Those claims instead use the complete symbolic inverse-branch proof in `RESULT.md`. The historical-priority comparison is not independently certified.
